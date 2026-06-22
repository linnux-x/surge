#!/usr/bin/env python3
"""Prune redundant CIDR entries from a ruleset file (surge format).

If a network like 10.0.0.0/8 is present, any more specific entry
(e.g. 10.0.0.0/16) is redundant and this script removes it.

Called from the main workflow.
Uses only the Python standard library.
"""
from __future__ import annotations

import ipaddress
import sys
from pathlib import Path


def prune_redundant_cidr(filepath: str) -> tuple[int, int]:
    """Remove CIDR entries that are subnets of a broader CIDR in the same file.

    Returns (total_before, total_after).
    """
    path = Path(filepath)
    lines = path.read_text(encoding="utf-8").splitlines()

    cidrs: list[tuple[int, ipaddress.IPv4Network | ipaddress.IPv6Network]] = []
    all_nets: set[ipaddress.IPv4Network | ipaddress.IPv6Network] = set()

    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        parts = [p.strip() for p in stripped.split(",")]
        if len(parts) < 2 or parts[0].upper() not in {"IP-CIDR", "IP-CIDR6"}:
            continue
        try:
            network = ipaddress.ip_network(parts[1], strict=False)
        except ValueError:
            continue
        cidrs.append((index, network))
        all_nets.add(network)

    before = len(cidrs)
    remove: set[int] = set()

    for index, network in cidrs:
        # Check if this network is a subnet of any broader network present
        for prefix in range(network.prefixlen):
            try:
                if network.supernet(new_prefix=prefix) in all_nets:
                    remove.add(index)
                    break
            except ipaddress.NetmaskValueError:
                break

    if remove:
        path.write_text(
            "\n".join(line for index, line in enumerate(lines) if index not in remove) + "\n",
            encoding="utf-8",
        )

    after = before - len(remove)
    return before, after


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: prune_cidr.py <file> [<file> ...]")
        return 1

    for arg in sys.argv[1:]:
        before, after = prune_redundant_cidr(arg)
        removed = before - after
        if removed:
            print(f"  {arg}: pruned {removed} redundant CIDRs ({before} → {after})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
