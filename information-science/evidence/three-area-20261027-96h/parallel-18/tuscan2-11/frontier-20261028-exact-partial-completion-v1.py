#!/usr/bin/env python3
"""Bounded exact completion of explicitly frozen actual T2(11) row slots.

Enumerate every single permutation compatible with the fixed rows at both
linear distances and with their necessarily unique starts/ends; then solve an
exact cover over the missing adjacency events, additionally requiring D2 and
endpoint disjointness. Completed exhaustion is only a result for the stated
fixed rows. A resource stop is UNKNOWN, never UNSAT.

Usage: python3 SCRIPT INPUT.json OUTPUT.json FIXED_ROWS SECONDS NODE_CAP ROW_CAP
FIXED_ROWS is a comma-separated list of 1-based row slots. Output is exclusive.
Any witness is written in the standard row-result format and must be checked
by frontier-20261028-tuscan-check-v1.py.
"""
import hashlib
import json
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

N = 11


class BudgetExceeded(Exception):
    pass


def main(argv):
    if len(argv) != 7:
        raise ValueError("usage: SCRIPT INPUT.json OUTPUT.json FIXED_ROWS SECONDS NODE_CAP ROW_CAP")
    source, output = Path(argv[1]), Path(argv[2])
    fixed = sorted({int(x) - 1 for x in argv[3].split(",")})
    seconds, node_cap, row_cap = map(int, argv[4:])
    if not fixed or len(fixed) >= N or not set(fixed).issubset(range(N)):
        raise ValueError("fixed row indices must be a nonempty proper subset of 1..11")
    if not (1 <= seconds <= 600 and 1 <= node_cap <= 100000000 and 1 <= row_cap <= 1000000):
        raise ValueError("resource bounds out of range")
    raw = source.read_bytes()
    rows = json.loads(raw).get("rows")
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError("candidate is not eleven permutations of 0..10")
    fixed_rows = [rows[i] for i in fixed]
    counts = [Counter((row[i], row[i + d]) for row in fixed_rows for i in range(N - d))
              for d in (1, 2)]
    starts = [row[0] for row in fixed_rows]
    ends = [row[-1] for row in fixed_rows]
    conflict = {
        "distance1": sorted([list(k) for k, v in counts[0].items() if v > 1]),
        "distance2": sorted([list(k) for k, v in counts[1].items() if v > 1]),
        "duplicate_start_symbols": sorted(x for x, count in Counter(starts).items() if count > 1),
        "duplicate_end_symbols": sorted(x for x, count in Counter(ends).items() if count > 1),
    }
    started = time.monotonic()
    deadline = started + seconds
    nodes = 0
    cover_nodes = 0
    eligible = []
    enumeration_complete = False
    cover_complete = False
    witness = None
    coverage = Counter()
    row_digest = hashlib.sha256()
    budget_reason = None
    required = {(a, b) for a in range(N) for b in range(N) if a != b} - set(counts[0])
    required_mask = sum(1 << (N * a + b) for a, b in required)

    def budget_check():
        if nodes + cover_nodes > node_cap:
            raise BudgetExceeded("node_cap")
        if (nodes + cover_nodes) % 1024 == 0 and time.monotonic() >= deadline:
            raise BudgetExceeded("wall_time")

    def enumerate_rows(prefix, mask, mask1, mask2):
        nonlocal nodes
        nodes += 1
        budget_check()
        if len(prefix) == N:
            if prefix[-1] in end_set:
                return
            if len(eligible) >= row_cap:
                raise BudgetExceeded("row_cap")
            row = tuple(prefix)
            eligible.append((row, mask1, mask2))
            row_digest.update(bytes(row))
            for a, b in zip(row, row[1:]):
                coverage[(a, b)] += 1
            return
        for x in range(N):
            if mask & (1 << x) or (not prefix and x in start_set):
                continue
            if prefix and (prefix[-1], x) in counts[0]:
                continue
            if len(prefix) > 1 and (prefix[-2], x) in counts[1]:
                continue
            next1 = mask1 | (1 << (N * prefix[-1] + x)) if prefix else mask1
            next2 = mask2 | (1 << (N * prefix[-2] + x)) if len(prefix) > 1 else mask2
            prefix.append(x)
            enumerate_rows(prefix, mask | (1 << x), next1, next2)
            prefix.pop()

    def solve_cover(chosen, used1, used2, chosen_starts, chosen_ends):
        nonlocal cover_nodes, witness
        cover_nodes += 1
        budget_check()
        outstanding = required_mask & ~used1
        if not outstanding:
            if len(chosen) != N - len(fixed):
                raise AssertionError("unexpected number of completion rows")
            witness = list(chosen)
            return True
        if len(chosen) >= N - len(fixed):
            return False
        # Choose the uncovered adjacency with the fewest eligible compatible
        # rows. This is exact: every completion must cover that event once.
        best_options = None
        remaining_bits = outstanding
        while remaining_bits:
            least = remaining_bits & -remaining_bits
            edge_index = least.bit_length() - 1
            options = [i for i in by_edge[edge_index]
                       if not (eligible[i][1] & used1 or eligible[i][2] & used2)
                       and eligible[i][0][0] not in chosen_starts
                       and eligible[i][0][-1] not in chosen_ends]
            if not options:
                return False
            if best_options is None or len(options) < len(best_options):
                best_options = options
                if len(options) == 1:
                    break
            remaining_bits ^= least
        for i in best_options:
            row, m1, m2 = eligible[i]
            chosen.append(i)
            if solve_cover(chosen, used1 | m1, used2 | m2,
                           chosen_starts | {row[0]}, chosen_ends | {row[-1]}):
                return True
            chosen.pop()
        return False

    with output.open("x", encoding="utf-8") as stream:
        result = {
            "schema": 1, "kind": "bounded_exact_fixed_row_completion",
            "source": str(source), "source_sha256": hashlib.sha256(raw).hexdigest(),
            "fixed_rows_1based": [i + 1 for i in fixed],
            "free_rows_1based": [i + 1 for i in range(N) if i not in fixed],
            "limits": {"seconds": seconds, "node_cap": node_cap, "row_cap": row_cap},
            "fixed_conflicts": conflict,
            "scope": "Only the specified fixed rows; no claim about the unrestricted problem. Exhaustive-negative output requires completed row generation and completed exact cover. Independently verify every claimed witness.",
        }
        if any(conflict.values()):
            result["status"] = "fixed_rows_immediately_incompatible"
        else:
            start_set, end_set = set(starts), set(ends)
            try:
                enumerate_rows([], 0, 0, 0)
                enumeration_complete = True
                unsupported = sorted(required - set(coverage))
                result["unsupported_required_adjacencies"] = [list(pair) for pair in unsupported]
                if unsupported:
                    result["status"] = "no_completion_unsupported_adjacency"
                    cover_complete = True
                else:
                    by_edge = defaultdict(list)
                    for i, (_, m1, _) in enumerate(eligible):
                        bits = m1
                        while bits:
                            bit = bits & -bits
                            by_edge[bit.bit_length() - 1].append(i)
                            bits ^= bit
                    if solve_cover([], 0, 0, set(), set()):
                        result["status"] = "candidate_witness_requires_independent_check"
                        full = [list(row) for row in rows]
                        for slot, row_index in zip((i for i in range(N) if i not in fixed), witness):
                            full[slot] = list(eligible[row_index][0])
                        result.update({"rows": full, "zero_score_claim": True,
                                       "best_pair_collision_score": 0, "d1_pair_collisions": 0,
                                       "d2_pair_collisions": 0, "d1_excess_events": 0,
                                       "d2_excess_events": 0})
                    else:
                        result["status"] = "no_completion_exhaustive_exact_cover"
                    cover_complete = True
            except BudgetExceeded as exc:
                budget_reason = str(exc)
                result["status"] = "unknown_budget_exhausted"
        result.update({
            "enumeration_complete": enumeration_complete,
            "exact_cover_complete": cover_complete,
            "enumeration_nodes": nodes,
            "cover_nodes": cover_nodes,
            "eligible_row_count": len(eligible),
            "eligible_row_sequence_sha256": row_digest.hexdigest(),
            "budget_reason": budget_reason,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "required_adjacency_count": len(required),
            "eligible_adjacency_support_counts": [
                {"event": list(pair), "eligible_rows": coverage[pair]} for pair in sorted(required)
            ] if enumeration_complete else None,
        })
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"output": str(output), "status": result["status"],
                      "fixed_rows_1based": result["fixed_rows_1based"],
                      "enumeration_complete": enumeration_complete,
                      "exact_cover_complete": cover_complete,
                      "enumeration_nodes": nodes, "cover_nodes": cover_nodes,
                      "eligible_row_count": len(eligible), "budget_reason": budget_reason,
                      "unsupported_required_adjacencies": result.get("unsupported_required_adjacencies"),
                      "elapsed_ms": result["elapsed_ms"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(str(exc)) from exc
