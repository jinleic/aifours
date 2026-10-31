#!/usr/bin/env python3
"""Independently check fixed-row edge support by a memoized suffix DP.

For each admissible prefix state (used symbols, previous, last), return BOTH
(1) the number of admissible complete suffixes and (2) the union of directed
adjacency events occurring in at least one such suffix. The recurrence visits
no explicit list of row permutations. Missing required adjacency pairs give
an exact candidate-specific noncompletion certificate, not a T2(11) no-go.

Usage: python3 SCRIPT CANDIDATE.json OUTPUT.json FIXED_ROWS
"""
import functools
import hashlib
import json
import sys
import time
from collections import Counter
from pathlib import Path

N = 11
ALL = (1 << N) - 1


def main(argv):
    if len(argv) != 4:
        raise ValueError("usage: SCRIPT CANDIDATE.json OUTPUT.json FIXED_ROWS")
    source, destination = Path(argv[1]), Path(argv[2])
    fixed = sorted({int(x) - 1 for x in argv[3].split(",")})
    if not fixed or len(fixed) >= N or not set(fixed).issubset(range(N)):
        raise ValueError("fixed rows must be a nonempty proper subset of 1..11")
    raw = source.read_bytes()
    rows = json.loads(raw).get("rows")
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError("expected eleven permutations of 0..10")
    retained = [rows[i] for i in fixed]
    firsts, lasts = [r[0] for r in retained], [r[-1] for r in retained]
    if len(set(firsts)) != len(firsts) or len(set(lasts)) != len(lasts):
        raise ValueError("fixed rows already repeat a first or last symbol")
    event_counts = [Counter((row[i], row[i + d]) for row in retained for i in range(N - d))
                    for d in (1, 2)]
    if any(v != 1 for counts in event_counts for v in counts.values()):
        raise ValueError("fixed rows already repeat an event")
    used1, used2 = set(event_counts[0]), set(event_counts[1])
    firsts, lasts = set(firsts), set(lasts)
    started = time.monotonic()

    @functools.lru_cache(None)
    def suffix(mask, previous, last):
        if mask == ALL:
            return (0, 0) if last in lasts else (1, 0)
        count, union = 0, 0
        for symbol in range(N):
            if mask & (1 << symbol) or (last, symbol) in used1:
                continue
            if previous != N and (previous, symbol) in used2:
                continue
            child_count, child_union = suffix(mask | (1 << symbol), last, symbol)
            if child_count:
                count += child_count
                union |= child_union | (1 << (N * last + symbol))
        return count, union

    total, union = 0, 0
    for first in range(N):
        if first in firsts:
            continue
        count, edge_union = suffix(1 << first, N, first)
        total += count
        union |= edge_union
    required = {(a, b) for a in range(N) for b in range(N) if a != b} - used1
    unsupported = sorted([list(pair) for pair in required
                          if not union & (1 << (N * pair[0] + pair[1]))])
    result = {
        "schema": 1, "kind": "independent_fixed_row_adjacency_support_dp",
        "source": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "fixed_rows_1based": [i + 1 for i in fixed],
        "fixed_first_symbols": sorted(firsts), "fixed_last_symbols": sorted(lasts),
        "fixed_d1_events": len(used1), "fixed_d2_events": len(used2),
        "eligible_single_row_count": total,
        "required_adjacency_count": len(required),
        "unsupported_required_adjacencies": unsupported,
        "suffix_states": suffix.cache_info().currsize,
        "elapsed_ms": round((time.monotonic() - started) * 1000),
        "scope": "DP exhausts every possible single actual row compatible with the given fixed rows, same-distance events, and distinct starts/ends. Any unsupported required adjacency proves no full completion of those fixed rows. This does not decide the original unrestricted problem or validate an unrelated SAT proof.",
    }
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(destination), "source_sha256": result["source_sha256"],
                      "fixed_rows_1based": result["fixed_rows_1based"],
                      "eligible_single_row_count": total,
                      "unsupported_required_adjacencies": unsupported,
                      "suffix_states": result["suffix_states"], "elapsed_ms": result["elapsed_ms"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
