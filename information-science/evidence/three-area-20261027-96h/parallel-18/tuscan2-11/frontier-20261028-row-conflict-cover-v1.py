#!/usr/bin/env python3
"""Exact candidate-specific minimum-row-change obstruction.

An edge joins two original rows if they repeat a directed event at the SAME
linear distance. Every proposed repair that leaves both endpoints unchanged
retains that collision. Enumerating subsets of the eleven row indices finds
all minimum vertex covers. This is a lower bound only for the supplied array,
not a global Tuscan-2 no-go or a guarantee that those repairs exist.

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

    result = {
        "kind": "candidate_specific_exact_minimum_row_conflict_cover",
        "source": str(source),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "row_indexing": "1-based; original row slots",
        "events": "ordered pairs; linear distances 1 and 2 counted separately",
        "conflicts_by_distance": by_distance,
        "conflicting_row_pairs": [list(edge) for edge in sorted(edges)],
        "minimum_rows_that_must_change": minimum,
        "all_minimum_covers": covers,
        "subsets_checked_up_to_minimum": subsets_checked,
        "every_cover_complement_independently_event_unique": True,
        "meaning": "Any completion that leaves all rows outside a changed subset byte-identical must change at least this many row slots. The listed minimum covers remove all pre-existing collisions among frozen rows but do not prove a full completion. No claim about arrays unrelated to this candidate.",
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
