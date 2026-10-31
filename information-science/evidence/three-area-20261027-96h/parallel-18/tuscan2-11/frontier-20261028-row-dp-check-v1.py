#!/usr/bin/env python3
"""Independently certify best single-row replacements for one actual candidate.

For each row slot separately, freeze the other ten rows and compute the exact
minimum pair-collision score over every permutation of 0..10 by memoized suffix
DP. Directed distance-one and distance-two events are linear and separate.
This is a candidate-local statement, never an all-array nonexistence result.
Usage: python3 SCRIPT CANDIDATE.json OUTPUT.json W1 W2
"""
import functools
import hashlib
import json
import sys
import time
from collections import Counter
from pathlib import Path

N = 11
FULL = (1 << N) - 1


def events(rows, distance):
    return Counter((row[i], row[i + distance])
                   for row in rows for i in range(N - distance))


def score(counts):
    return sum(v * (v - 1) // 2 for v in counts.values())


def row_minimum(rows, row_index, w1, w2):
    remaining = rows[:row_index] + rows[row_index + 1:]
    c1, c2 = events(remaining, 1), events(remaining, 2)
    base = w1 * score(c1) + w2 * score(c2)

    @functools.lru_cache(None)
    def finish(mask, previous, last):
        if mask == FULL:
            return 0
        return min(w1 * c1[last, x] + w2 * c2[previous, x]
                   + finish(mask | (1 << x), last, x)
                   for x in range(N) if not mask & (1 << x))

    minimum_increment = min(
        w1 * c1[a, b] + finish((1 << a) | (1 << b), a, b)
        for a in range(N) for b in range(N) if a != b
    )
    return base + minimum_increment, finish.cache_info().currsize


def main(argv):
    if len(argv) != 5:
        raise ValueError("usage: SCRIPT CANDIDATE.json OUTPUT.json W1 W2")
    source, destination = Path(argv[1]), Path(argv[2])
    w1, w2 = int(argv[3]), int(argv[4])
    if not (1 <= w1 <= 50 and 1 <= w2 <= 50):
        raise ValueError("weights must be integers in 1..50")
    raw = source.read_bytes()
    rows = json.loads(raw).get("rows")
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError("expected eleven actual permutations of 0..10")
    original = w1 * score(events(rows, 1)) + w2 * score(events(rows, 2))
    started = time.monotonic()
    minima = []
    for r in range(N):
        minimum, states = row_minimum(rows, r, w1, w2)
        if minimum > original:
            raise AssertionError("current row itself must be an admissible replacement")
        minima.append({"row_1based": r + 1, "minimum_total_weighted_score": minimum,
                       "improvement": original - minimum, "memoized_states": states})
    result = {
        "kind": "independent_exact_single_row_best_response_check",
        "source": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "distance1_weight": w1, "distance2_weight": w2,
        "current_weighted_pair_collision_score": original,
        "row_minima": minima,
        "no_strict_single_row_improvement": all(x["improvement"] == 0 for x in minima),
        "elapsed_ms": round((time.monotonic() - started) * 1000),
        "scope": "Each minimum ranges over all 11! possible symbol permutations in one fixed slot with all other rows unchanged. A local optimum is not a global no-go, and does not exclude simultaneous multirow replacements.",
    }
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(destination), "source_sha256": result["source_sha256"],
                      "score": original, "row_minima": [x["minimum_total_weighted_score"] for x in minima],
                      "no_strict_single_row_improvement": result["no_strict_single_row_improvement"],
                      "elapsed_ms": result["elapsed_ms"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
