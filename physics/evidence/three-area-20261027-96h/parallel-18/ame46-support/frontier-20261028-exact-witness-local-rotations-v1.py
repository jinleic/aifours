#!/usr/bin/env python3
"""Exact Q(sqrt(2)) check and bounded local real-Hadamard support search.

Source: P. Pandya, arXiv:2610.16673v1, Table 1. The 36 entries below are
transcribed explicitly; a coefficient pair (a,b) represents a+b*sqrt(2).
All moves use the unnormalized block H on the selected pair and sqrt(2) I
on all other local levels, hence the depth-k tensor is divided by
sqrt(72*2**k). No floating point is used. The search is exhaustive over
ordered move sequences at the requested depth, not all local unitaries or
all AME states.
"""
import argparse
import collections
import itertools
import json
import sys

SOURCE = "https://arxiv.org/html/2610.16673#S2.T1"
CELLS = (
    ("-12 +21", "-02 +20", "-01 +10", "s44", "s55", "s33"),
    ("-01 -10", "+00 +54", "+35 +43", "-15 -32", "-23 +41", "-24 +52"),
    ("+02 +20", "-35 +43", "+00 -54", "-25 +31", "-13 +42", "+14 +51"),
    ("s34", "-23 -41", "+13 +42", "s50", "-11 +22", "s05"),
    ("s53", "+15 -32", "+25 +31", "+11 +22", "s04", "s40"),
    ("s45", "-14 +51", "+24 +52", "s03", "s30", "+12 +21"),
)
ZERO = (0, 0)


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def accumulate(out, key, value):
    value = add(out.get(key, ZERO), value)
    if value == ZERO:
        out.pop(key, None)
    else:
        out[key] = value


def source_tensor():
    tensor = {}
    for a, row in enumerate(CELLS):
        for b, cell in enumerate(row):
            for token in cell.split():
                if len(token) != 3 or token[0] not in "+-s" or any(c not in "012345" for c in token[1:]):
                    raise ValueError(f"invalid source token {token!r}")
                k, l = map(int, token[1:])
                coeff = (0, 1) if token[0] == "s" else (1 if token[0] == "+" else -1, 0)
                key = (a, b, k, l)
                if key in tensor:
                    raise ValueError(f"duplicate source coordinate {key}")
                tensor[key] = coeff
    return tensor


def hadamard(tensor, move):
    axis, p, q = move
    result = {}
    for key, coeff in tensor.items():
        j = key[axis]
        if j != p and j != q:
            accumulate(result, key, (2 * coeff[1], coeff[0]))
            continue
        target_p = key[:axis] + (p,) + key[axis + 1:]
        target_q = key[:axis] + (q,) + key[axis + 1:]
        accumulate(result, target_p, coeff)
        accumulate(result, target_q, coeff if j == p else (-coeff[0], -coeff[1]))
    return result


def verify_all_six(tensor, depth):
    """Direct coefficient trace, all six ordered party-pair marginals."""
    weight = 72 * (2 ** depth)
    norm = ZERO
    for coeff in tensor.values():
        norm = add(norm, mul(coeff, coeff))
    if norm != (weight, 0):
        raise ValueError(f"normalization numerator {norm}, expected {(weight, 0)}")
    checked = []
    for pair in itertools.combinations(range(4), 2):
        complement = tuple(i for i in range(4) if i not in pair)
        traces = collections.defaultdict(dict)
        for key, coeff in tensor.items():
            row = tuple(key[i] for i in pair)
            col = tuple(key[i] for i in complement)
            traces[col][row] = coeff
        gram = collections.defaultdict(lambda: ZERO)
        for column in traces.values():
            for i, ci in column.items():
                for j, cj in column.items():
                    gram[(i, j)] = add(gram[(i, j)], mul(ci, cj))
        target = (weight // 36, 0)
        bad = []
        for i in itertools.product(range(6), repeat=2):
            for j in itertools.product(range(6), repeat=2):
                actual = gram.get((i, j), ZERO)
                expected = target if i == j else ZERO
                if actual != expected:
                    bad.append((i, j, actual, expected))
        if bad:
            raise ValueError(f"marginal {pair} fails: {bad[:3]}")
        checked.append({"parties_zero_based": pair, "diagonal_numerator": target,
                        "offdiagonal_checked": 36 * 35, "diagonal_checked": 36})
    return {"normalization_numerator": norm, "normalization_denominator": weight,
            "marginals": checked}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, choices=(0, 1, 2, 3), default=2)
    args = parser.parse_args()
    source = source_tensor()
    if len(source) != 60:
        raise ValueError(f"source table support {len(source)}, expected 60")
    source_check = verify_all_six(source, 0)
    moves = tuple((axis, p, q) for axis in range(4) for p, q in itertools.combinations(range(6), 2))
    move_control = verify_all_six(hadamard(source, moves[0]), 1)
    mutation = dict(source)
    first_key = next(iter(mutation))
    mutation[first_key] = add(mutation[first_key], (1, 0))
    try:
        verify_all_six(mutation, 0)
    except ValueError as exc:
        if not str(exc).startswith("normalization numerator"):
            raise
        mutation_control = str(exc)
    else:
        raise ValueError("normalization mutation was incorrectly accepted")
    best = (len(source), (), source)
    hist = collections.Counter({len(source): 1})
    leaves = 0

    def visit(tensor, path):
        nonlocal best, leaves
        if len(path) == args.depth:
            leaves += 1
            return
        for move in moves:
            candidate = hadamard(tensor, move)
            new_path = path + (move,)
            support = len(candidate)
            hist[support] += 1
            if support < best[0]:
                best = (support, new_path, candidate)
            visit(candidate, new_path)

    visit(source, ())
    best_check = verify_all_six(best[2], len(best[1]))
    result = {
        "source": SOURCE,
        "coefficient_encoding": "(a,b) means (a+b*sqrt(2))/sqrt(72*2**depth)",
        "source_support": len(source), "source_exact_verification": source_check,
        "move": "on p,q: (x_p,x_q)->(x_p+x_q,x_p-x_q)/sqrt(2); other levels unchanged",
        "single_move_exact_verification": move_control,
        "normalization_mutation_control": mutation_control,
        "search": {"max_depth": args.depth, "moves_per_node": len(moves), "leaves": leaves,
                   "support_histogram_all_depths_including_root": dict(sorted(hist.items())),
                   "best_support": best[0], "best_moves_axis_p_q": best[1]},
        "best_exact_verification": best_check,
        "best_coefficients": [[*key, *value] for key, value in sorted(best[2].items())],
        "limitations": "Exact check is a single in-harness implementation; no independent checker, source-priority clearance, or all-unitary optimality follows.",
    }
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
