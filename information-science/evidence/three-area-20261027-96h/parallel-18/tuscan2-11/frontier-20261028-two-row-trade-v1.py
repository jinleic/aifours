#!/usr/bin/env python3
"""Exhaust all adjacency-preserving two-row replacements of one T1 square.

For each unordered pair of actual rows, the remaining nine rows are frozen.
Add a formal sentinel to the two removed rows and partition their residual
arcs into two directed Hamilton cycles by choosing orientations of the
bipartite matching components. Every two-row T1-preserving replacement is
covered, up to swapping the two row slots (which preserves all event counts).
Distance-two events are scored only inside the resulting LINEAR rows.

Usage: python3 SCRIPT T1_CANDIDATE.json OUTPUT.json
Any zero-score table requires independent original-row verification. A local
failure excludes only this candidate's exact two-row neighborhood.
"""
import hashlib
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

N = 11
SENTINEL = N
SIZE = N + 1


def event_counts(rows, distance):
    return Counter((row[c], row[c + distance])
                   for row in rows for c in range(N - distance))


def stats(counter):
    excess = sum(count - 1 for count in counter.values() if count > 1)
    pair_collisions = sum(count * (count - 1) // 2 for count in counter.values())
    return excess, pair_collisions


def successor(row):
    seq = [SENTINEL] + list(row)
    result = [None] * SIZE
    for a, b in zip(seq, seq[1:] + seq[:1]):
        result[a] = b
    return result


def decode_single_cycle(succ):
    if len(set(succ)) != SIZE:
        raise AssertionError("component switch did not produce a permutation")
    seen = {SENTINEL}
    row = []
    v = SENTINEL
    for _ in range(N):
        v = succ[v]
        if v in seen:
            return None
        seen.add(v)
        row.append(v)
    if succ[v] != SENTINEL or len(seen) != SIZE:
        return None
    return row


def components(p, q):
    inverse = [None] * SIZE
    for tail, head in enumerate(p):
        inverse[head] = tail
    relative = [inverse[q[v]] for v in range(SIZE)]
    seen, output = set(), []
    for v in range(SIZE):
        if v in seen:
            continue
        cycle = []
        at = v
        while at not in seen:
            seen.add(at)
            cycle.append(at)
            at = relative[at]
        if at != v:
            raise AssertionError("relative map is not a permutation cycle")
        if len(cycle) < 2:
            raise ValueError("removed rows share an augmented adjacency arc")
        output.append(cycle)
    return output


def main(argv):
    if len(argv) != 3:
        raise ValueError("usage: SCRIPT T1_CANDIDATE.json OUTPUT.json")
    source, destination = Path(argv[1]), Path(argv[2])
    raw = source.read_bytes()
    rows = json.loads(raw).get("rows")
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError("expected eleven permutations of 0..10")
    c1, c2 = event_counts(rows, 1), event_counts(rows, 2)
    if len(c1) != N * (N - 1) or any(count != 1 for count in c1.values()):
        raise ValueError("input does not have exact directed linear adjacency coverage")
    if len({row[0] for row in rows}) != N or len({row[-1] for row in rows}) != N:
        raise AssertionError("adjacency-exact rows must have distinct starts and ends")

    start = time.monotonic()
    initial_excess, initial_score = stats(c2)
    best_score, best_excess = initial_score, initial_excess
    best_rows = [row[:] for row in rows]
    best_pair = None
    pair_records = []
    orientations = 0
    hamilton_splits = 0
    strict_improvements = 0
    for i, j in itertools.combinations(range(N), 2):
        p, q = successor(rows[i]), successor(rows[j])
        parts = components(p, q)
        fixed = [row for r, row in enumerate(rows) if r not in (i, j)]
        fixed_d2 = event_counts(fixed, 2)
        pair_best = initial_score
        pair_splits = 0
        # Bit 0 is fixed to 0; complementing all bits exchanges the two
        # replacement rows and leaves the unordered pair/events unchanged.
        for variable_mask in range(1 << (len(parts) - 1)):
            p_new, q_new = p[:], q[:]
            for component in range(1, len(parts)):
                if variable_mask & (1 << (component - 1)):
                    for v in parts[component]:
                        p_new[v], q_new[v] = q_new[v], p_new[v]
            orientations += 1
            a, b = decode_single_cycle(p_new), decode_single_cycle(q_new)
            if a is None or b is None:
                continue
            pair_splits += 1
            hamilton_splits += 1
            combined = fixed_d2.copy()
            combined.update((row[c], row[c + 2]) for row in (a, b) for c in range(N - 2))
            excess, score = stats(combined)
            pair_best = min(pair_best, score)
            if score < initial_score:
                strict_improvements += 1
            if score < best_score or (score == best_score and excess < best_excess):
                best_score, best_excess = score, excess
                best_rows = [row[:] for row in rows]
                best_rows[i], best_rows[j] = a, b
                best_pair = [i + 1, j + 1]
        pair_records.append({"removed_rows_1based": [i + 1, j + 1],
                             "matching_components": len(parts),
                             "orientation_representatives": 1 << (len(parts) - 1),
                             "hamilton_splits": pair_splits,
                             "best_d2_pair_collisions": pair_best})

    # Independently reconstruct final score directly from all actual rows before
    # emitting the externally verifiable candidate format.
    final_d1, final_d2 = event_counts(best_rows, 1), event_counts(best_rows, 2)
    d1_excess, d1_pairs = stats(final_d1)
    d2_excess, d2_pairs = stats(final_d2)
    if d1_pairs != 0 or d2_pairs != best_score or d2_excess != best_excess:
        raise AssertionError("final candidate accounting mismatch")
    result = {
        "schema": 1, "kind": "exhaustive_adjacency_preserving_two_row_trades",
        "source": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "initial_d1_pair_collisions": 0, "initial_d2_pair_collisions": initial_score,
        "row_pairs_checked": len(pair_records), "orientation_representatives_checked": orientations,
        "hamilton_splits_checked": hamilton_splits, "strict_improving_splits": strict_improvements,
        "best_changed_rows_1based": best_pair,
        "best_pair_collision_score": d1_pairs + d2_pairs,
        "d1_pair_collisions": d1_pairs, "d2_pair_collisions": d2_pairs,
        "d1_excess_events": d1_excess, "d2_excess_events": d2_excess,
        "zero_score_claim": d1_pairs == 0 and d2_pairs == 0,
        "rows": best_rows, "per_pair": pair_records,
        "elapsed_ms": round((time.monotonic() - start) * 1000),
        "scope": "All replacements of exactly two given row slots preserving the other nine and all original D1 adjacencies, modulo swapping those two rows. No Latin or wrap constraint. Local exhaustion is not global nonexistence.",
    }
    with destination.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(destination), "source_sha256": result["source_sha256"],
                      "row_pairs_checked": len(pair_records),
                      "orientation_representatives_checked": orientations,
                      "hamilton_splits_checked": hamilton_splits,
                      "strict_improving_splits": strict_improvements,
                      "initial_d2_pair_collisions": initial_score,
                      "best_d2_pair_collisions": d2_pairs,
                      "best_changed_rows_1based": best_pair,
                      "zero_score_claim": result["zero_score_claim"],
                      "elapsed_ms": result["elapsed_ms"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
