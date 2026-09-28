"""Shared, option-aware CIDR coverage used by generation and validation."""
from __future__ import annotations

import ipaddress

Network = ipaddress.IPv4Network | ipaddress.IPv6Network
CIDREntry = tuple[int, Network, tuple[str, ...]]


def redundant_cidr_indices(entries: list[CIDREntry]) -> set[int]:
    """Find strict subnets with identical options, preserving equal networks.

    Only prefix lengths actually present in the same address family and option
    group can cover an entry. This avoids constructing every possible supernet
    (up to 128 per IPv6 rule). Indices belong to the caller's original lines.
    """
    networks = {(network, options) for _, network, options in entries}
    prefixes: dict[tuple[int, tuple[str, ...]], set[int]] = {}
    for _, network, options in entries:
        prefixes.setdefault((network.version, options), set()).add(network.prefixlen)
    ordered = {key: sorted(values) for key, values in prefixes.items()}
    redundant = set()
    for index, network, options in entries:
        for prefix in ordered[(network.version, options)]:
            if prefix >= network.prefixlen:
                break
            if (network.supernet(new_prefix=prefix), options) in networks:
                redundant.add(index)
                break
    return redundant


def prune_cidr_lines(lines: list[str]) -> tuple[list[str], int, int]:
    """Return retained original lines and valid CIDR counts before/after.

    Invalid entries stay in place for the validator to report. Option ordering
    and case are normalized for comparison; duplicate options are retained in
    the key to preserve the existing behavior on malformed input.
    """
    entries: list[CIDREntry] = []
    for index, line in enumerate(lines):
        parts = [part.strip() for part in line.strip().split(",")]
        if len(parts) < 2 or parts[0].upper() not in {"IP-CIDR", "IP-CIDR6"}:
            continue
        try:
            network = ipaddress.ip_network(parts[1], strict=False)
        except ValueError:
            continue
        entries.append((index, network, tuple(sorted(p.lower() for p in parts[2:]))))
    removed = redundant_cidr_indices(entries)
    return ([line for index, line in enumerate(lines) if index not in removed],
            len(entries), len(entries) - len(removed))
