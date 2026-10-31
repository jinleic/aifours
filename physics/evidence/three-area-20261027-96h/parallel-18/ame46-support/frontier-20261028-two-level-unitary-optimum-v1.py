#!/usr/bin/env python3
"""Exhaustively optimize one arbitrary U(2) coordinate move on the 60-state.

Reads the literal CELLS data from the frozen companion source via AST literal
extraction; it never imports or executes it. Exact projective directions live
in Q(sqrt(2)); complex U(2) cannot zero a real pair outside these directions.
"""
import argparse
import ast
import collections
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import sys


def ratio(x, y):
    a, b = x
    c, d = y
    den = c * c - 2 * d * d
    if den == 0:
        raise ValueError("zero algebraic denominator")
    return Fraction(a * c - 2 * b * d, den), Fraction(b * c - a * d, den)


def perpendicular(z):
    a, b = z
    den = a * a - 2 * b * b
    if den == 0:
        raise ValueError("zero projective direction")
    return -a / den, b / den


def encode(z):
    return [[v.numerator, v.denominator] for v in z]


def parse_data(path):
    raw = path.read_bytes()
    module = ast.parse(raw, filename=str(path))
    assignments = [n for n in module.body if isinstance(n, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == "CELLS" for t in n.targets)]
    if len(assignments) != 1:
        raise ValueError("expected exactly one CELLS assignment")
    cells = ast.literal_eval(assignments[0].value)
    if len(cells) != 6 or any(len(row) != 6 for row in cells):
        raise ValueError("source must be 6 by 6")
    tensor = {}
    for a, row in enumerate(cells):
        for b, cell in enumerate(row):
            for token in cell.split():
                if len(token) != 3 or token[0] not in "+-s" or any(c not in "012345" for c in token[1:]):
                    raise ValueError(f"bad token {token!r}")
                pos = (a, b, int(token[1]), int(token[2]))
                if pos in tensor:
                    raise ValueError(f"duplicate position {pos}")
                tensor[pos] = (0, 1) if token[0] == "s" else (1 if token[0] == "+" else -1, 0)
    return tensor, hashlib.sha256(raw).hexdigest()


def analyze_pair(tensor, axis, p, q):
    fibers = collections.defaultdict(dict)
    for coordinate, coeff in tensor.items():
        if coordinate[axis] in (p, q):
            key = coordinate[:axis] + coordinate[axis + 1:]
            fibers[key][coordinate[axis]] = coeff
    one = 0
    directions = collections.Counter()
    for fiber in fibers.values():
        if len(fiber) == 1:
            one += 1
        elif len(fiber) == 2:
            directions[ratio(fiber[p], fiber[q])] += 1
        else:
            raise ValueError("fiber size not one or two")
    max_cancel = 0
    winning = []
    for z in directions:
        total = directions[z] + directions.get(perpendicular(z), 0)
        if total > max_cancel:
            max_cancel, winning = total, [z]
        elif total == max_cancel:
            winning.append(z)
    nonmonomial_support = len(tensor) + one - max_cancel
    return {
        "axis_p_q": [axis, p, q],
        "single_occupied_fibers": one,
        "double_occupied_fibers": sum(directions.values()),
        "projective_directions": [{"x_over_y_Qsqrt2": encode(z), "fiber_count": directions[z],
                                   "orthogonal_fiber_count": directions.get(perpendicular(z), 0)}
                                  for z in sorted(directions)],
        "max_cancellations": max_cancel,
        "nonmonomial_min_support": nonmonomial_support,
        "any_U2_min_support": min(len(tensor), nonmonomial_support),
        "minimizing_directions": [encode(z) for z in winning],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tensor, source_sha = parse_data(args.source)
    if len(tensor) != 60:
        raise ValueError(f"expected source support 60, got {len(tensor)}")
    rows = [analyze_pair(tensor, axis, p, q)
            for axis in range(4) for p, q in itertools.combinations(range(6), 2)]
    hist = collections.Counter(row["nonmonomial_min_support"] for row in rows)
    result = {
        "source_path": str(args.source), "source_sha256": source_sha,
        "method": "exact Q(sqrt(2)) projective-direction grouping; all complex U(2), one local pair",
        "source_support": len(tensor), "pairs_checked": len(rows),
        "nonmonomial_min_support_histogram": dict(sorted(hist.items())),
        "min_nonmonomial_support": min(row["nonmonomial_min_support"] for row in rows),
        "min_any_U2_support": min(row["any_U2_min_support"] for row in rows),
        "rows": rows,
        "limits": "Single in-harness exact symbolic implementation; no independent verifier, multi-pair/multi-party arbitrary U(6) optimization, or global minimum proof.",
    }
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    summary = {k: result[k] for k in ("source_sha256", "source_support", "pairs_checked", "nonmonomial_min_support_histogram", "min_nonmonomial_support", "min_any_U2_support", "limits")}
    json.dump(summary, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
