#!/usr/bin/env python3
"""Independently inspect actual linear Tuscan-2(11) row candidates.

The checker rebuilds event lists from the complete table. It does not use the
searcher's incremental event counts or require any column/rotation condition.
Usage: python3 CHECK.py SEARCH_RESULT.json CHECK_RESULT.json
The output is created exclusively. A valid near-candidate is a successful
inspection but is_witness is false; reported-score disagreement is an error.
"""

import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

N = 11


def inspect(data):
    rows = data.get("rows")
    if not isinstance(rows, list) or len(rows) != N:
        raise ValueError("expected exactly eleven rows")
    symbols = list(range(N))
    for index, row in enumerate(rows, 1):
        if (not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != symbols):
            raise ValueError(f"row {index} is not a permutation of 0..10")

    results = {}
    for distance in (1, 2):
        occurrences = defaultdict(list)
        for row_index, row in enumerate(rows, 1):
            for col in range(N - distance):
                event = (row[col], row[col + distance])
                occurrences[event].append([row_index, col + 1, col + distance + 1])
        duplicate = [
            {"pair": list(pair), "count": len(where), "occurrences_1_based": where}
            for pair, where in sorted(occurrences.items()) if len(where) > 1
        ]
        missing = [
            [x, y] for x in range(N) for y in range(N)
            if x != y and (x, y) not in occurrences
        ]
        results[f"distance_{distance}"] = {
            "events": sum(map(len, occurrences.values())),
            "distinct_events": len(occurrences),
            "duplicate_event_types": len(duplicate),
            "excess_events": sum(item["count"] - 1 for item in duplicate),
            "pair_collisions": sum(item["count"] * (item["count"] - 1) // 2
                                   for item in duplicate),
            "duplicate_occurrences": duplicate,
            "missing_ordered_pairs": missing,
        }

    d1, d2 = results["distance_1"], results["distance_2"]
    checks = {
        "d1_pair_collisions": d1["pair_collisions"],
        "d2_pair_collisions": d2["pair_collisions"],
        "d1_excess_events": d1["excess_events"],
        "d2_excess_events": d2["excess_events"],
        "best_pair_collision_score": d1["pair_collisions"] + d2["pair_collisions"],
    }
    disagreements = {
        key: {"reported": data.get(key), "recomputed": value}
        for key, value in checks.items() if data.get(key) != value
    }
    witness = (
        d1["events"] == N * (N - 1)
        and d1["distinct_events"] == N * (N - 1)
        and d2["events"] == N * (N - 2)
        and d2["distinct_events"] == N * (N - 2)
    )
    if data.get("zero_score_claim") is not witness:
        disagreements["zero_score_claim"] = {
            "reported": data.get("zero_score_claim"), "recomputed": witness
        }
    return {
        "kind": "independent_actual_row_event_inspection",
        "n": N,
        "rows_are_permutations": True,
        "linear_not_cyclic": True,
        "column_latin_assumed": False,
        "is_witness": witness,
        "search_metric_disagreements": disagreements,
        **results,
    }


def main():
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} SEARCH_RESULT.json CHECK_RESULT.json")
    source, destination = map(Path, sys.argv[1:])
    raw = source.read_bytes()
    data = json.loads(raw)
    result = inspect(data)
    result["source_path"] = str(source)
    result["source_sha256"] = hashlib.sha256(raw).hexdigest()
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({
        "output": str(destination),
        "source_sha256": result["source_sha256"],
        "is_witness": result["is_witness"],
        "distance_1": {k: result["distance_1"][k] for k in
                       ("events", "distinct_events", "excess_events", "pair_collisions")},
        "distance_2": {k: result["distance_2"][k] for k in
                       ("events", "distinct_events", "excess_events", "pair_collisions")},
        "search_metric_disagreements": result["search_metric_disagreements"],
    }, sort_keys=True))
    if result["search_metric_disagreements"]:
        raise SystemExit("search metrics disagree with independent recomputation")


if __name__ == "__main__":
    main()
