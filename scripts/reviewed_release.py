#!/usr/bin/env python3
"""Capture and restore the exact public artifacts reviewed in a successful dry run."""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
PUBLISH_PATHS = (
    "Rule", "clash", "Module", "README.md", "scripts/diff_report.md",
    "scripts/diff_report.json", "scripts/generation_receipt.md",
    "scripts/generation_receipt.json", "scripts/source_state.json",
)
BUNDLE_NAME = "reviewed-release.json"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def allowed(name: str) -> bool:
    path = PurePosixPath(name)
    return (
        not path.is_absolute() and ".." not in path.parts
        and str(path) == name
        and (name in PUBLISH_PATHS or any(name.startswith(p + "/") for p in PUBLISH_PATHS[:3]))
    )


def digest(payload: dict) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def capture(output: Path) -> None:
    names = git("ls-files", "--cached", "--others", "--exclude-standard", "--", *PUBLISH_PATHS).splitlines()
    files = {}
    for name in sorted(set(names)):
        path = ROOT / name
        if not allowed(name) or path.is_symlink():
            raise ValueError(f"Invalid release path: {name}")
        files[name] = base64.b64encode(path.read_bytes()).decode() if path.exists() else None
    payload = {"schema": 1, "base_sha": git("rev-parse", "HEAD"),
               "repository": os.environ["GITHUB_REPOSITORY"],
               "run_id": os.environ["GITHUB_RUN_ID"], "files": files}
    output.write_text(json.dumps({"sha256": digest(payload), "payload": payload}, sort_keys=True) + "\n")
    print(f"Reviewed release: {len(files)} paths, sha256={digest(payload)}")


def validate(bundle: dict, base_sha: str, repository: str, run_id: str) -> dict[str, bytes | None]:
    payload = bundle["payload"]
    if bundle["sha256"] != digest(payload):
        raise ValueError("Release digest mismatch")
    if (payload["schema"], payload["base_sha"], payload["repository"], payload["run_id"]) != (1, base_sha, repository, run_id):
        raise ValueError("Reviewed release does not match base SHA, repository or run ID")
    files = payload["files"]
    if not files:
        raise ValueError("Empty release")
    decoded = {}
    for name, data in files.items():
        if not allowed(name):
            raise ValueError(f"Invalid release path: {name}")
        decoded[name] = None if data is None else base64.b64decode(data, validate=True)
    return decoded


def restore(archive: Path, run_id: str) -> None:
    with ZipFile(archive) as zf:
        # Never extract arbitrary archive paths onto the checkout.
        bundle = json.loads(zf.read(BUNDLE_NAME))
    files = validate(bundle, git("rev-parse", "HEAD"), os.environ["GITHUB_REPOSITORY"], run_id)
    tracked = set(git("ls-files", "--", *PUBLISH_PATHS).splitlines())
    if not tracked.issubset(files):
        raise ValueError("Release omits tracked publish paths")
    # Validate every destination before performing any write.
    for name in files:
        path = ROOT / name
        if any((ROOT / Path(*PurePosixPath(name).parts[:i])).is_symlink()
               for i in range(1, len(PurePosixPath(name).parts) + 1)):
            raise ValueError(f"Symlink release destination: {name}")
    for name, data in files.items():
        path = ROOT / name
        if data is None:
            path.unlink(missing_ok=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f"Restored reviewed release sha256={bundle['sha256']}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("capture").add_argument("output", type=Path)
    restore_parser = commands.add_parser("restore")
    restore_parser.add_argument("archive", type=Path)
    restore_parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    if args.command == "capture":
        capture(args.output)
    else:
        restore(args.archive, args.run_id)


if __name__ == "__main__":
    main()
