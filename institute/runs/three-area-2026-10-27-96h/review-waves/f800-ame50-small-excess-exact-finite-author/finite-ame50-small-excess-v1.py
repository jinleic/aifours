#!/usr/bin/env python3
"""UNRUN candidate; parent whole-read and separately authorize before execution.

Standard library only; no input files, network, subprocesses, or output files.
Run only after admission, with an explicit positive --max-nodes.  A node-cap
stop is INCOMPLETE, never a completed enumeration or a mathematical verdict.
"""

import argparse
import hashlib
import itertools
import json
import math
import sys


class CheckError(Exception):
    def __init__(self, reason, detail=""):
        self.reason = reason
        self.detail = detail
        super().__init__(reason + (": " + detail if detail else ""))


class NodeLimit(Exception):
    pass


def need(condition, reason, detail=""):
    if not condition:
        raise CheckError(reason, detail)


def expect_reason(reason, function, *arguments):
    try:
        function(*arguments)
    except CheckError as error:
        if error.reason != reason:
            raise CheckError("WRONG_MUTANT_REASON", reason + " got " + error.reason)
        return
    raise CheckError("MUTANT_NOT_REJECTED", reason)


def column_masks(rows, m):
    return tuple(sum(1 << i for i, row in enumerate(rows) if row & (1 << j))
                 for j in range(m))


def connected(rows, cols, m):
    seen_rows = {0}
    seen_cols = set()
    while True:
        new_cols = {j for i in seen_rows for j in range(m)
                    if rows[i] & (1 << j)}
        new_rows = {i for j in new_cols for i in range(m)
                    if cols[j] & (1 << i)}
        if new_rows == seen_rows and new_cols == seen_cols:
            return len(seen_rows) == m and len(seen_cols) == m
        seen_rows, seen_cols = new_rows, new_cols


def twin_necessary(rows, cols, m):
    if m == 2:
        return True
    for lines, other in ((rows, cols), (cols, rows)):
        low = [line for line in lines if line.bit_count() == 2]
        for line in low:
            pair = [j for j in range(m) if line & (1 << j)]
            if other[pair[0]] != other[pair[1]]:
                return False
            if other[pair[0]].bit_count() < 3:
                return False
        for a, b in itertools.combinations(low, 2):
            if a & b:
                return False
    return True


def support_reason(m, rows, use_twins):
    if m < 1 or m > 7:
        return "ORDER"
    if len(rows) != m or any(not isinstance(r, int) or r < 0 or r >= (1 << m)
                             for r in rows):
        return "SHAPE"
    cols = column_masks(rows, m)
    if any(r.bit_count() < 2 for r in rows) or any(c.bit_count() < 2 for c in cols):
        return "DEGREE"
    if sum(r.bit_count() for r in rows) - 2 * m > 5:
        return "EXCESS"
    if any((a & b).bit_count() == 1 for a, b in itertools.combinations(rows, 2)):
        return "ROW_SINGLETON"
    if any((a & b).bit_count() == 1 for a, b in itertools.combinations(cols, 2)):
        return "COLUMN_SINGLETON"
    if not connected(rows, cols, m):
        return "DISCONNECTED"
    if use_twins and not twin_necessary(rows, cols, m):
        return "TWIN_ISOLATION"
    return "ACCEPT"


def require_support(m, rows, use_twins):
    reason = support_reason(m, rows, use_twins)
    if reason != "ACCEPT":
        raise CheckError(reason)


def gram_check(matrix, scale):
    n = len(matrix)
    need(n > 0 and all(len(row) == n for row in matrix), "GRAM_SHAPE")
    for i in range(n):
        for j in range(n):
            expected = scale if i == j else 0
            row_dot = sum(matrix[i][k] * matrix[j][k] for k in range(n))
            need(row_dot == expected, "ROW_GRAM", str((i, j, row_dot, expected)))
    for i in range(n):
        for j in range(n):
            expected = scale if i == j else 0
            col_dot = sum(matrix[k][i] * matrix[k][j] for k in range(n))
            need(col_dot == expected, "COLUMN_GRAM", str((i, j, col_dot, expected)))


def masks_of(matrix):
    return tuple(sum(1 << j for j, x in enumerate(row) if x != 0) for row in matrix)


def local_controls():
    expect_reason("ORDER", require_support, 8, [3] * 8, True)
    expect_reason("SHAPE", require_support, 2, [3], True)
    expect_reason("DEGREE", require_support, 2, [3, 1], True)
    expect_reason("EXCESS", require_support, 4, [15, 15, 15, 15], True)
    expect_reason("ROW_SINGLETON", require_support, 3, [3, 6, 7], True)
    expect_reason("COLUMN_SINGLETON", require_support, 4, [15, 7, 11, 3], True)
    expect_reason("DISCONNECTED", require_support, 4, [3, 3, 12, 12], True)
    require_support(4, [3, 3, 15, 15], False)
    expect_reason("TWIN_ISOLATION", require_support, 4, [3, 3, 15, 15], True)
    positives = (
        (((3, 4), (4, -3)), 25),
        (((0, 15, 20), (15, 16, -12), (20, -12, 9)), 625),
        (((-1, 2, 2), (2, -1, 2), (2, 2, -1)), 9),
        (((0, 1, 1, 1), (1, 0, 1, -1),
          (1, -1, 0, 1), (1, 1, -1, 0)), 3),
    )
    for matrix, scale in positives:
        gram_check(matrix, scale)
        require_support(len(matrix), masks_of(matrix), True)
    expect_reason("ROW_GRAM", gram_check, ((2, 4), (4, -3)), 25)
    return {"support_rejection_reasons": ["ORDER", "SHAPE", "DEGREE", "EXCESS",
            "ROW_SINGLETON", "COLUMN_SINGLETON", "DISCONNECTED", "TWIN_ISOLATION"],
            "graph_only_accepts_twin_mutant": True,
            "exact_integer_gram_positive_controls": len(positives),
            "gram_mutant_reason": "ROW_GRAM"}


def row_weight(rows):
    factor = math.factorial(len(rows))
    for _, group in itertools.groupby(rows):
        factor //= math.factorial(sum(1 for _ in group))
    return factor


def make_cell():
    return {"graph_sorted": 0, "graph_labeled": 0, "graph_digest": hashlib.sha256(),
            "twin_sorted": 0, "twin_labeled": 0, "twin_digest": hashlib.sha256(),
            "twin_patterns": [], "twin_row_profiles": {}}


def enumerate_patterns(max_nodes):
    nodes = 0
    results = {}
    for m in range(1, 8):
        cells = [make_cell() for _ in range(6)]
        results[m] = cells
        candidates = [r for r in range(1 << m) if r.bit_count() >= 2]
        chosen = []

        def visit(first, used_excess, columns):
            nonlocal nodes
            nodes += 1
            if nodes > max_nodes:
                raise NodeLimit
            remain = m - len(chosen)
            if any(c.bit_count() + remain < 2 for c in columns):
                return
            if remain == 0:
                rows = tuple(chosen)
                if support_reason(m, rows, False) != "ACCEPT":
                    return
                excess = sum(r.bit_count() for r in rows) - 2 * m
                need(excess == used_excess and 0 <= excess <= 5, "ENUMERATOR_EXCESS")
                cell = cells[excess]
                multiplicity = row_weight(rows)
                record = bytes([m, excess]) + bytes(rows)
                cell["graph_sorted"] += 1
                cell["graph_labeled"] += multiplicity
                cell["graph_digest"].update(record)
                if support_reason(m, rows, True) == "ACCEPT":
                    cell["twin_sorted"] += 1
                    cell["twin_labeled"] += multiplicity
                    cell["twin_digest"].update(record)
                    cell["twin_patterns"].append(list(rows))
                    profile = ",".join(str(x) for x in sorted(r.bit_count() for r in rows))
                    cell["twin_row_profiles"][profile] = (
                        cell["twin_row_profiles"].get(profile, 0) + multiplicity)
                return
            row_position = len(chosen)
            for index in range(first, len(candidates)):
                row = candidates[index]
                new_excess = used_excess + row.bit_count() - 2
                if new_excess > 5:
                    continue
                if any((row & previous).bit_count() == 1 for previous in chosen):
                    continue
                next_columns = tuple(columns[j] | (1 << row_position)
                                     if row & (1 << j) else columns[j]
                                     for j in range(m))
                chosen.append(row)
                visit(index, new_excess, next_columns)
                chosen.pop()

        visit(0, 0, (0,) * m)
    return results, nodes


def check_enumeration(results):
    # These are guards, not substituted results; an unexpected count fails.
    expected_twin = {(2, 0): 1, (3, 2): 9, (3, 3): 1,
                     (4, 4): 96, (4, 5): 240}
    for m in range(1, 8):
        for excess in range(6):
            actual = results[m][excess]["twin_labeled"]
            expected = expected_twin.get((m, excess), 0)
            need(actual == expected, "TWIN_CLASSIFICATION",
                 str((m, excess, actual, expected)))
    for m, excess, expected in ((2, 0, 1), (3, 2, 9), (3, 3, 1),
                                (4, 4, 132), (4, 5, 240)):
        actual = results[m][excess]["graph_labeled"]
        need(actual == expected, "GRAPH_CLASSIFICATION", str((m, excess, actual, expected)))
    need(results[4][5]["twin_row_profiles"] == {"3,3,3,4": 96, "2,3,4,4": 144},
         "PROFILE_CLASSIFICATION", str(results[4][5]["twin_row_profiles"]))


def serializable_results(results):
    out = {}
    for m, cells in results.items():
        out[str(m)] = {}
        for excess, cell in enumerate(cells):
            out[str(m)][str(excess)] = {
                "graph_sorted": cell["graph_sorted"],
                "graph_labeled": cell["graph_labeled"],
                "graph_sha256": cell["graph_digest"].hexdigest(),
                "twin_sorted": cell["twin_sorted"],
                "twin_labeled": cell["twin_labeled"],
                "twin_sha256": cell["twin_digest"].hexdigest(),
                "twin_row_profiles_labeled": cell["twin_row_profiles"],
                "twin_sorted_row_masks": cell["twin_patterns"],
            }
    return out


def blocks(beta, gamma, delta):
    ab = {(x, x, y, delta[y]) for x in range(3) for y in range(3)}
    ac = {(x, y, x, gamma[y]) for x in range(3) for y in range(3)}
    ad = {(x, y, beta[y], x) for x in range(3) for y in range(3)}
    return ab, ac, ad


def pair_compatible(words, beta, gamma, delta):
    for a, b, c, d in words:
        if ((a == b) != (d == delta[c]) or
            (a == c) != (d == gamma[b]) or
            (a == d) != (c == beta[b])):
            return False
    return True


def require_compatible(beta, gamma, delta):
    bs = blocks(beta, gamma, delta)
    need(pair_compatible(set.union(*bs), beta, gamma, delta), "PAIR_COMPATIBILITY")


def check_blocks(beta, gamma, delta, proposed):
    correct = blocks(beta, gamma, delta)
    need(len(proposed) == 3 and all(proposed[i] == correct[i] for i in range(3)),
         "BLOCK_CONTENT")
    require_compatible(beta, gamma, delta)


def check_caps(words, pi, overrides=None):
    overrides = overrides or {}
    identity = tuple(range(3))
    for i, j in itertools.combinations(range(4), 2):
        matching = identity if i == 0 else pi
        for x, y in itertools.product(range(3), repeat=2):
            cap = overrides.get((i, j, x, y), 3 if matching[x] == y else 2)
            count = sum(w[i] == x and w[j] == y for w in words)
            need(count <= cap, "PAIR_CAPACITY", str((i, j, x, y, count, cap)))


def check_distinct(words):
    need(len(words) == len(set(words)), "DUPLICATE_WORD")


def check_forced(word, a, union):
    need(word not in union and word[0] == a, "FORCED_EXTENSION")
    for j in (1, 2, 3):
        opposite = 1 - a
        count = sum(w[0] == a and w[j] == opposite for w in union)
        need(count == 1 and word[j] == opposite, "FORCED_EXTENSION", str((a, j, count)))


def need_deficit(remaining, distinct_capacity):
    need(remaining > distinct_capacity, "NO_CAPACITY_OBSTRUCTION")


def high_block_controls():
    identity = (0, 1, 2)
    transposition = (1, 0, 2)
    perms = list(itertools.permutations(range(3)))
    compatible = []
    for beta, gamma, delta in itertools.product(perms, repeat=3):
        bs = blocks(beta, gamma, delta)
        if pair_compatible(set.union(*bs), beta, gamma, delta):
            compatible.append((beta, gamma, delta))
    need(len(compatible) == 4, "MATCHING_EXHAUSTION", str(len(compatible)))
    for beta, gamma, delta in compatible:
        need(beta == gamma == delta and all(delta[delta[x]] == x for x in range(3)),
             "MATCHING_CLASS")
    summaries = []
    for pi in (identity, transposition):
        bs = blocks(pi, pi, pi)
        check_blocks(pi, pi, pi, bs)
        union = set.union(*bs)
        fixed = sum(pi[x] == x for x in range(3))
        need([len(block) for block in bs] == [9, 9, 9], "BLOCK_SIZE")
        need(all(len(bs[i] & bs[j]) == 3 for i, j in itertools.combinations(range(3), 2)),
             "PAIR_INTERSECTION")
        need(len(bs[0] & bs[1] & bs[2]) == fixed, "TRIPLE_INTERSECTION")
        need(len(union) == 18 + fixed, "UNION_SIZE")
        for i in range(4):
            for x in range(3):
                actual = sum(w[i] == x for w in union)
                need(actual == 6 + int(pi[x] == x), "HIGH_OCCURRENCE", str((i, x, actual)))
        check_caps(union, pi)
        if pi == identity:
            need(25 - len(union) == 4, "IDENTITY_REMAINDER")
            need_deficit(25 - len(union), 1)
            summaries.append({"class": "identity", "fixed_points": fixed,
                              "block_sizes": [9, 9, 9], "pair_intersections": [3, 3, 3],
                              "triple_intersection": fixed, "union": len(union),
                              "high_occurrences": [7, 7, 7], "remaining": 4,
                              "all_low_capacity": 1})
        else:
            forced = [(0, 1, 1, 1), (1, 0, 0, 0)]
            for a, word in enumerate(forced):
                check_forced(word, a, union)
            check_distinct(list(union) + forced)
            extended = union | set(forced)
            check_caps(extended, pi)
            for i in range(4):
                for x in range(3):
                    need(sum(w[i] == x for w in extended) == 7,
                         "FORCED_EXHAUSTION", str((i, x)))
            remaining = 25 - len(extended)
            need(remaining == 4, "TRANSPOSITION_REMAINDER")
            need_deficit(remaining, 1)
            summaries.append({"class": "transposition", "fixed_points": fixed,
                              "block_sizes": [9, 9, 9], "pair_intersections": [3, 3, 3],
                              "triple_intersection": fixed, "union": len(union),
                              "high_occurrences": [6, 6, 7], "forced": forced,
                              "remaining_after_forcing": remaining, "all_low_capacity": 1})
    expect_reason("PAIR_COMPATIBILITY", require_compatible, identity, identity, transposition)
    mutated = list(blocks(identity, identity, identity))
    mutated[0] = mutated[0] - {(0, 0, 0, 0)}
    expect_reason("BLOCK_CONTENT", check_blocks, identity, identity, identity, mutated)
    trans_union = set.union(*blocks(transposition, transposition, transposition))
    expect_reason("PAIR_CAPACITY", check_caps, trans_union, transposition, {(0, 1, 0, 0): 2})
    expect_reason("FORCED_EXTENSION", check_forced, (0, 1, 1, 0), 0, trans_union)
    expect_reason("DUPLICATE_WORD", check_distinct, [(0, 1, 1, 1), (0, 1, 1, 1)])
    expect_reason("NO_CAPACITY_OBSTRUCTION", need_deficit, 1, 1)
    return {"matching_triples_inspected": len(perms) ** 3,
            "compatible_triples": len(compatible), "cases": summaries,
            "mutant_reasons": ["PAIR_COMPATIBILITY", "BLOCK_CONTENT", "PAIR_CAPACITY",
                               "FORCED_EXTENSION", "DUPLICATE_WORD", "NO_CAPACITY_OBSTRUCTION"]}


def main():
    parser = argparse.ArgumentParser(description="UNRUN exact local necessary-support candidate")
    parser.add_argument("--max-nodes", required=True, type=int)
    arguments = parser.parse_args()
    if arguments.max_nodes < 1:
        parser.error("--max-nodes must be positive")
    try:
        controls = local_controls()
        high = high_block_controls()
        results, nodes = enumerate_patterns(arguments.max_nodes)
        check_enumeration(results)
    except NodeLimit:
        print(json.dumps({"status": "INCOMPLETE_NODE_CAP", "max_nodes": arguments.max_nodes},
                         sort_keys=True))
        return 2
    except CheckError as error:
        print(json.dumps({"status": "GUARD_FAILED", "reason": error.reason,
                          "detail": error.detail}, sort_keys=True))
        return 1
    print(json.dumps({"status": "COMPLETE_NECESSARY_SUPPORT_ENUMERATION",
                      "nodes": nodes, "node_cap": arguments.max_nodes,
                      "scope": "connected square orders 1..7, excess 0..5; necessary only",
                      "controls": controls, "high_block": high,
                      "coverage": serializable_results(results)}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
