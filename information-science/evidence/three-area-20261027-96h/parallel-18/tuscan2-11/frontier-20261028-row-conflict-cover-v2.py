#!/usr/bin/env python3
"""Exact candidate-specific event/endpoint row-change obstruction.

An edge joins rows if they repeat a directed event at the SAME linear
distance, or share a first or last symbol. Any complete adjacency-exact array
has every symbol as first and last exactly once. Thus a repair leaving both
ends of an edge unchanged cannot be a witness. Enumerating row-index subsets
finds every minimum cover of these necessary constraints. This is a bound only
for the supplied candidate, not a global no-go or a completion guarantee.

Usage: python3 SCRIPT CANDIDATE.json OUTPUT.json
"""
import hashlib
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

N = 11


def main(argv):
    if len(argv) != 3:
        raise ValueError("usage: SCRIPT CANDIDATE.json OUTPUT.json")
    source, destination = map(Path, argv[1:])
    raw = source.read_bytes()
    rows = json.loads(raw).get("rows")
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError("expected eleven actual permutations of 0..10")

    by_distance = {}
    edges = set()
    for d in (1, 2):
        owners = defaultdict(set)
        for r, row in enumerate(rows, 1):
            for c in range(N - d):
                owners[(row[c], row[c + d])].add(r)
        event_conflicts = []
        for pair, row_set in sorted(owners.items()):
            if len(row_set) > 1:
                pairs = list(itertools.combinations(sorted(row_set), 2))
                edges.update(pairs)
                event_conflicts.append({"event": list(pair), "rows_1based": sorted(row_set)})
        by_distance[str(d)] = event_conflicts

    # Exact adjacency coverage requires every symbol to start and end exactly
    # once. Capture those additional necessary pairwise repair conflicts.
    endpoint_conflicts = {}
    for label, position in (("starts", 0), ("ends", -1)):
        owners = defaultdict(list)
        for r, row in enumerate(rows, 1):
            owners[row[position]].append(r)
        endpoint_conflicts[label] = []
        for symbol, row_indices in sorted(owners.items()):
            if len(row_indices) > 1:
                edges.update(itertools.combinations(row_indices, 2))
                endpoint_conflicts[label].append({"symbol": symbol, "rows_1based": row_indices})

    all_rows = tuple(range(1, N + 1))
    minimum = None
    covers = []
    subsets_checked = 0
    for size in range(N + 1):
        for cover in itertools.combinations(all_rows, size):
            subsets_checked += 1
            chosen = set(cover)
            if all(u in chosen or v in chosen for u, v in edges):
                covers.append(list(cover))
        if covers:
            minimum = size
            break
    # Rebuild each frozen complement from original rows: every one must be a
    # conflict-free partial array at BOTH distances, confirming the incidence
    # cover is not a mere count of event labels.
    for cover in covers:
        for d in (1, 2):
            events = [(row[c], row[c + d])
                      for r, row in enumerate(rows, 1) if r not in cover
                      for c in range(N - d)]
            if len(events) != len(set(events)):
                raise AssertionError("cover complement contains a collision")
        frozen = [row for r, row in enumerate(rows, 1) if r not in cover]
        if len({row[0] for row in frozen}) != len(frozen) or len({row[-1] for row in frozen}) != len(frozen):
            raise AssertionError("cover complement repeats a start or end")

    result = {
        "kind": "candidate_specific_exact_event_endpoint_row_conflict_cover",
        "source": str(source),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "row_indexing": "1-based; original row slots",
        "events": "ordered pairs; linear distances 1 and 2 counted separately",
        "conflicts_by_distance": by_distance,
        "conflicts_by_endpoint": endpoint_conflicts,
        "conflicting_row_pairs": [list(edge) for edge in sorted(edges)],
        "minimum_rows_that_must_change": minimum,
        "all_minimum_covers": covers,
        "subsets_checked_up_to_minimum": subsets_checked,
        "every_cover_complement_event_and_endpoint_unique": True,
        "meaning": "Any witness retaining rows outside a changed set byte-identically must hit every event or endpoint conflict. Minimum covers satisfy these necessary conditions among frozen rows, but do not prove a full completion. No claim about arrays unrelated to this candidate.",
    }
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(destination), "source_sha256": result["source_sha256"],
                      "minimum_rows_that_must_change": minimum,
                      "all_minimum_covers": covers,
                      "subsets_checked_up_to_minimum": subsets_checked,
                      "conflicting_row_pairs": result["conflicting_row_pairs"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
