#!/usr/bin/env python3
"""Deterministic runner for the rule pipeline shared by CI, workflows and the daily job.

Subcommands (each prints one JSON summary as the last stdout line):

  upstream       Probe upstream sources and write the candidate state to
                 scripts/source_state.next.json. Fails when any source is
                 unreachable, or (--require-known-timestamps) lacks a comparable
                 fingerprint.
  build          Regenerate rulesets, then — only if a published file changed —
                 manifests, the diff report and the receipt, always in that order.
                 Targets come from --rulesets, --all, or --from-upstream.
  verify         Run the same checks as CI. The receipt check is read-only: it
                 regenerates the receipt, compares, and restores the original bytes.
  promote-state  Move scripts/source_state.next.json over scripts/source_state.json.
                 Run only after build and verify succeeded.

The runner owns ordering and success criteria; callers (Hermes, Actions) decide
only whether to run it and how to review the result.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RULE_DIR = ROOT / "Rule"
STATE = SCRIPTS / "source_state.json"
NEXT_STATE = SCRIPTS / "source_state.next.json"
RECEIPTS = (SCRIPTS / "generation_receipt.json", SCRIPTS / "generation_receipt.md")

sys.path.insert(0, str(SCRIPTS))
from sources import RULE_SPECS  # noqa: E402


class PipelineError(RuntimeError):
    """A step failed; the message is safe to show in summaries."""


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess:
    """Run a repository script with this interpreter; output goes to stderr unless captured."""
    command = [sys.executable, "-B", *args]
    print(f"$ {' '.join(args)}", file=sys.stderr, flush=True)
    return subprocess.run(command, cwd=ROOT, text=True,
                          stdout=subprocess.PIPE if capture else sys.stderr, stderr=sys.stderr)


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True)


def published_digest() -> dict[str, str]:
    """Hash every generated rule artifact: rule lists and their snapshot records."""
    paths = sorted(RULE_DIR.glob("*.list")) + sorted((RULE_DIR / ".sources").glob("*.json"))
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def emit(summary: dict) -> None:
    print(json.dumps(summary, ensure_ascii=False))


# ── upstream ────────────────────────────────────────────────────────────────

def upstream(require_known_timestamps: bool) -> dict:
    result = run(["scripts/check_upstream_updates.py", "--state-out", str(NEXT_STATE.relative_to(ROOT))],
                 capture=True)
    lines = [line for line in (result.stdout or "").splitlines() if line.strip()]
    try:
        summary = json.loads(lines[-1])
    except (IndexError, ValueError) as exc:
        raise PipelineError("upstream check produced no summary") from exc
    if result.returncode != 0 or summary.get("status") == "failed" or summary.get("unavailable_sources"):
        raise PipelineError(f"upstream unreachable: {summary.get('unavailable_sources', '?')} source(s)")
    if require_known_timestamps and summary.get("unknown_timestamp_sources"):
        raise PipelineError(f"{summary['unknown_timestamp_sources']} source(s) lack a comparable fingerprint")
    rulesets = summary.get("rulesets")
    if not isinstance(rulesets, list) or any(name not in RULE_SPECS for name in rulesets):
        raise PipelineError("upstream summary has an invalid ruleset list")
    return summary


# ── build ───────────────────────────────────────────────────────────────────

def build(rulesets: list[str], offline: bool) -> dict:
    if not rulesets:
        return {"status": "unchanged", "rulesets": [], "changed_files": []}
    before = published_digest()
    args = ["scripts/generate_rules.py", "--rulesets", *rulesets]
    if offline:
        args.append("--offline")
    if run(args).returncode != 0:
        raise PipelineError("generate_rules.py failed")
    after = published_digest()
    changed = sorted(path for path in before.keys() | after.keys() if before.get(path) != after.get(path))
    if changed:
        # Derived artifacts follow the rules, in this order, every time a rule file changes.
        for step in (["scripts/manifest.py"], ["scripts/manifest.py", "--diff"], ["scripts/generate_receipt.py"]):
            if run(step).returncode != 0:
                raise PipelineError(f"{' '.join(step)} failed")
    return {"status": "changed" if changed else "unchanged", "rulesets": rulesets, "changed_files": changed}


# ── verify ──────────────────────────────────────────────────────────────────

def receipt_is_current() -> bool:
    """Regenerate the receipt and compare without leaving the regenerated copy behind."""
    original = {path: path.read_bytes() if path.exists() else None for path in RECEIPTS}
    try:
        if run(["scripts/generate_receipt.py"]).returncode != 0:
            return False
        return all((path.read_bytes() if path.exists() else None) == data for path, data in original.items())
    finally:
        for path, data in original.items():
            if data is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(data)


def verify_checks(ci: bool, online: bool) -> list[tuple[str, object]]:
    checks: list[tuple[str, object]] = [
        ("repository invariants", ["scripts/validate_surge_repo.py", *(["--ci"] if ci else [])]),
        ("generation receipt", receipt_is_current),
        ("unit tests", ["-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]),
        ("routing order", ["scripts/test_routing_order.py"]),
        ("whitespace", lambda: git("diff", "--check").returncode == 0),
    ]
    if online:
        checks.append(("online audit", ["scripts/audit_rules.py"]))
    return checks


def verify(ci: bool, online: bool) -> dict:
    results = {}
    for name, check in verify_checks(ci, online):
        ok = check() if callable(check) else run(check).returncode == 0
        results[name] = "pass" if ok else "fail"
        print(f"[{results[name].upper()}] {name}", file=sys.stderr, flush=True)
    # Informational, as in CI: first-match conflicts across policies are reported, never fatal.
    run(["scripts/cross_file_conflicts.py", "--summary"])
    failed = [name for name, status in results.items() if status == "fail"]
    return {"status": "failed" if failed else "passed", "checks": results, "failed": failed}


# ── promote-state ───────────────────────────────────────────────────────────

def promote_state() -> dict:
    if not NEXT_STATE.exists():
        return {"status": "unchanged", "promoted": False}
    try:
        json.loads(NEXT_STATE.read_text(encoding="utf-8"))
    except ValueError as exc:
        raise PipelineError("candidate source state is not valid JSON; not promoted") from exc
    os.replace(NEXT_STATE, STATE)
    return {"status": "changed", "promoted": True}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    up = sub.add_parser("upstream", help="probe upstream sources")
    up.add_argument("--require-known-timestamps", action="store_true")
    b = sub.add_parser("build", help="regenerate rules and derived artifacts")
    target = b.add_mutually_exclusive_group(required=True)
    target.add_argument("--rulesets", nargs="+", metavar="NAME")
    target.add_argument("--all", action="store_true", help="every ruleset (full generation)")
    target.add_argument("--from-upstream", action="store_true", help="rulesets whose upstream changed")
    b.add_argument("--offline", action="store_true", help="rebuild from pinned snapshots (see generate_rules.py)")
    b.add_argument("--require-known-timestamps", action="store_true")
    v = sub.add_parser("verify", help="run the CI checks")
    v.add_argument("--ci", action="store_true", help="CI scope of validate_surge_repo.py")
    v.add_argument("--online", action="store_true", help="also run the online audit")
    sub.add_parser("promote-state", help="adopt the candidate upstream state")
    args = parser.parse_args(argv)

    try:
        if args.command == "upstream":
            summary = upstream(args.require_known_timestamps)
        elif args.command == "build":
            if args.offline and args.from_upstream:
                parser.error("--offline cannot be combined with --from-upstream")
            if args.from_upstream:
                rulesets = upstream(args.require_known_timestamps)["rulesets"]
            elif args.all:
                rulesets = list(RULE_SPECS)
            else:
                unknown = [name for name in args.rulesets if name not in RULE_SPECS]
                if unknown:
                    parser.error(f"unknown rulesets: {', '.join(unknown)}")
                rulesets = args.rulesets
            summary = build(rulesets, args.offline)
        elif args.command == "verify":
            summary = verify(args.ci, args.online)
        else:
            summary = promote_state()
    except PipelineError as exc:
        summary = {"status": "failed", "error": str(exc)}
    emit({"command": args.command, **summary})
    return 1 if summary["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
