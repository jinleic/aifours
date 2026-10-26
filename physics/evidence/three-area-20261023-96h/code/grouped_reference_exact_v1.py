"""Exact, bounded co-Choi assay for the grouped Werner-reference lemma.

Scientific execution requires a named parent GO. This file has not been run.
The result concerns GS(Omega_r), not unrestricted Werner nonnegativity.
Standard library only; no solver, subprocess, network, or dependency mutation.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import itertools
import json
import os
from pathlib import Path
import signal
import sys
import time

D = 4
PAIRS = tuple(itertools.product(range(D), repeat=2))
BASIS = tuple(itertools.product(range(D), repeat=4))
ZERO = Q(0)
ONE = Q(1)
DEADLINE = float("inf")


class Stopped(Exception):
    pass


def check_clock():
    if time.monotonic() >= DEADLINE:
        raise Stopped("monotonic scientific deadline reached")


def on_signal(signum, _frame):
    raise Stopped(f"received signal {signum}")


def dot(left, right):
    return sum((a * b for a, b in zip(left, right)), ZERO)


def quadratic(matrix, vector):
    return sum((vector[i] * dot(row, vector)
                for i, row in enumerate(matrix)), ZERO)


def exact_psd(matrix):
    """Unpivoted rational square completion, including zero-pivot witnesses."""
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("nonsquare matrix")
    if any(matrix[i][j] != matrix[j][i]
           for i in range(size) for j in range(size)):
        raise ValueError("matrix is not symmetric")
    residual = [row[:] for row in matrix]
    upper = [[ZERO for _ in range(size)] for _ in range(size)]
    pivots = []
    for k in range(size):
        check_clock()
        pivot = residual[k][k]
        vector = None
        if pivot < 0:
            vector = [ZERO for _ in range(size)]
            vector[k] = ONE
        elif pivot == 0:
            partner = next((j for j in range(k + 1, size)
                            if residual[k][j] != 0), None)
            if partner is not None:
                vector = [ZERO for _ in range(size)]
                vector[partner] = ONE
                vector[k] = -(residual[partner][partner] + ONE) / (
                    2 * residual[k][partner])
        if vector is not None:
            for previous in range(k - 1, -1, -1):
                vector[previous] = -sum(
                    (upper[previous][j] * vector[j]
                     for j in range(previous + 1, size)), ZERO)
            value = quadratic(matrix, vector)
            if value >= 0:
                raise ArithmeticError("negative witness reconstruction failed")
            return {"verdict": "INDEFINITE", "failed_pivot": k,
                    "witness": list(map(str, vector)),
                    "exact_quadratic_value": str(value)}
        pivots.append(pivot)
        if pivot == 0:
            continue
        for j in range(k + 1, size):
            upper[k][j] = residual[k][j] / pivot
        for i in range(k + 1, size):
            for j in range(i, size):
                value = residual[i][j] - (
                    residual[k][i] * residual[k][j] / pivot)
                residual[i][j] = value
                residual[j][i] = value
    # Reconstruct the entire original quadratic matrix from the congruence.
    reconstructed = [[ZERO for _ in range(size)] for _ in range(size)]
    for k, pivot in enumerate(pivots):
        row = upper[k][:]
        row[k] = ONE
        for i in range(size):
            for j in range(size):
                reconstructed[i][j] += pivot * row[i] * row[j]
    if reconstructed != matrix:
        raise ArithmeticError("exact LDL reconstruction failed")
    return {"verdict": "PSD", "positive_pivots": sum(p > 0 for p in pivots),
            "zero_pivots": sum(p == 0 for p in pivots),
            "pivots": list(map(str, pivots)),
            "unit_upper_rows": [[str(upper[i][j]) for j in range(i + 1, size)]
                                for i in range(size)]}


def weight(state):
    a, b, c, d = state
    answer = [0] * D
    answer[a] += 1
    answer[b] -= 1
    answer[c] += 1
    answer[d] -= 1
    return tuple(answer)


def c_entry(left, right):
    a, b, c, d = left
    e, f, g, h = right
    identity = int(a == e and b == f and c == g and d == h)
    swap_1 = int(a == g and c == e and b == f and d == h)
    swap_2 = int(b == h and d == f and a == e and c == g)
    both = int(a == g and c == e and b == h and d == f)
    return Q(identity) - Q(swap_1 + swap_2, 2) + Q(both, 4)


def reference_rows(rank):
    """L_r(ab), stored as sparse output rows; all reference entries are 0/1."""
    operators = []
    for a, b in PAIRS:
        rows = [defaultdict(Q) for _ in PAIRS]
        for column, (e, f) in enumerate(PAIRS):
            if a == b and a < rank:
                rows[column][column] += ONE
            if b < rank and e == b:
                rows[a * D + f][column] -= Q(1, 2)
            if a < rank and f == a:
                rows[e * D + b][column] -= Q(1, 2)
            if e == f and e < rank:
                rows[a * D + b][column] += Q(1, 4)
        operators.append([{key: value for key, value in row.items() if value}
                          for row in rows])
    return operators


def inverse_data(rank):
    if rank == 1:
        diagonal = [ONE / ((ONE - Q(int(a == 0), 2)) *
                           (ONE - Q(int(b == 0), 2))) for a, b in PAIRS]
        return diagonal, ZERO
    diagonal = [ONE / (rank - Q(int(a < rank) + int(b < rank), 2))
                for a, b in PAIRS]
    correction = ONE / ((rank - 1) * (5 * rank - 4))
    return diagonal, correction


def s_entry(i, p, j, q, rows, inverse_diagonal, correction, omega_indices):
    # Co-Choi reversal: row input i, column input j uses L_j ... L_i^dagger.
    left = rows[j][p]
    right = rows[i][q]
    value = sum((coefficient * right.get(z, ZERO) * inverse_diagonal[z]
                 for z, coefficient in left.items()), ZERO)
    if correction:
        value -= correction * sum((left.get(z, ZERO) for z in omega_indices), ZERO) * sum(
            (right.get(z, ZERO) for z in omega_indices), ZERO)
    return value


def sparse_q3(operator):
    result = ZERO
    norms = {}
    for mask in range(8):
        traced = tuple(i for i in range(3) if mask & (1 << i))
        kept = tuple(i for i in range(3) if i not in traced)
        reduced = defaultdict(Q)
        for (row, column), coefficient in operator.items():
            if all(row[i] == column[i] for i in traced):
                key = (tuple(row[i] for i in kept), tuple(column[i] for i in kept))
                reduced[key] += coefficient
        norm = sum((entry * entry for entry in reduced.values()), ZERO)
        norms[str(mask)] = str(norm)
        result += Q(-1, 2) ** len(traced) * norm
    return result, norms


def controls():
    cases = [([[ONE, ONE], [ONE, ONE]], "PSD"),
             ([[ZERO, ONE], [ONE, ZERO]], "INDEFINITE"),
             ([[-ONE, ZERO], [ZERO, ZERO]], "INDEFINITE")]
    reports = []
    for matrix, expected in cases:
        answer = exact_psd(matrix)
        if answer["verdict"] != expected:
            raise ArithmeticError("exact congruence control failed")
        reports.append(answer)
    boundary = []
    for size, expected in ((1, Q(1, 2)), (2, ZERO), (3, Q(-3, 2))):
        operator = {((0, 0, a), (1, 1, a)): ONE for a in range(size)}
        value, norms = sparse_q3(operator)
        if value != expected:
            raise ArithmeticError("rank boundary partial-trace control failed")
        boundary.append({"rank": size, "q3": str(value), "norms_by_mask": norms})
    return {"exact_congruence": reports, "werner_rank_boundary": boundary}


def assay_rank(rank):
    check_clock()
    rows = reference_rows(rank)
    inverse_diagonal, correction = inverse_data(rank)
    omega_indices = tuple(a * D + a for a in range(rank))
    groups = defaultdict(list)
    for i, state in enumerate(BASIS):
        groups[weight(state)].append(i)
    if len(groups) != 55 or max(map(len, groups.values())) != 28:
        raise ArithmeticError("torus block-count control failed")
    c_matrix = [[ZERO for _ in BASIS] for _ in BASIS]
    s_matrix = [[ZERO for _ in BASIS] for _ in BASIS]
    digest = hashlib.sha256()
    cross_weight_count = 0
    for left_index, left_state in enumerate(BASIS):
        check_clock()
        i, p = divmod(left_index, D * D)
        for right_index in range(left_index + 1):
            j, q = divmod(right_index, D * D)
            c = c_entry(left_state, BASIS[right_index])
            s = s_entry(i, p, j, q, rows, inverse_diagonal, correction, omega_indices)
            reverse = s_entry(j, q, i, p, rows, inverse_diagonal, correction, omega_indices)
            if s != reverse:
                raise ArithmeticError("co-Choi symmetry control failed")
            if weight(left_state) != weight(BASIS[right_index]):
                cross_weight_count += 1
                if c != 0 or s != 0:
                    raise ArithmeticError("nonzero discarded cross-weight matrix entry")
            c_matrix[left_index][right_index] = c
            c_matrix[right_index][left_index] = c
            s_matrix[left_index][right_index] = s
            s_matrix[right_index][left_index] = s
            digest.update(f"{left_index},{right_index}:{c}:{s}\n".encode())
    signs = {}
    for sign in (-1, 1):
        blocks = []
        for block_weight, indices in sorted(groups.items()):
            check_clock()
            block = [[c_matrix[i][j] + sign * s_matrix[i][j] for j in indices]
                     for i in indices]
            answer = exact_psd(block)
            answer["weight"] = block_weight
            answer["basis_indices"] = indices
            blocks.append(answer)
        signs[str(sign)] = {
            "verdict": "PSD" if all(b["verdict"] == "PSD" for b in blocks) else "INDEFINITE",
            "blocks": blocks}
    verdict = "GS_PSD" if all(s["verdict"] == "PSD" for s in signs.values()) else "GS_FALSE"
    if rank == 1 and verdict != "GS_PSD":
        raise ArithmeticError("published fully product positive control failed")
    return {"reference_rank": rank, "verdict": verdict,
            "upper_triangle_C_S_sha256": digest.hexdigest(),
            "cross_weight_entries_exactly_checked": cross_weight_count,
            "signs": signs,
            "scope": "co-Choi domination only; not an unrestricted Werner verdict"}


def main():
    global DEADLINE
    parser = argparse.ArgumentParser()
    parser.add_argument("--ranks", required=True)
    parser.add_argument("--seconds", required=True, type=float)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    ranks = tuple(int(value) for value in args.ranks.split(","))
    if not ranks or len(set(ranks)) != len(ranks) or any(r not in (1, 2, 3, 4) for r in ranks):
        parser.error("ranks must be distinct members of 1,2,3,4")
    if not 0 < args.seconds <= 600:
        parser.error("seconds must lie in (0,600]")
    # Existing paths are never reused or overwritten.
    os.mkdir(args.output)
    started = time.monotonic()
    DEADLINE = started + args.seconds
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    receipt = {"status": "RUNNING", "argv": sys.argv,
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "dimension_per_site": D, "ranks_requested": ranks,
               "scientific_scope": "GS(Omega_r) only, not W4", "cases": []}
    exit_code = 0
    try:
        receipt["controls"] = controls()
        for rank in ranks:
            receipt["cases"].append(assay_rank(rank))
        receipt["status"] = "COMPLETE_EXACT_GROUPED_REFERENCE_ASSAY"
    except Stopped as error:
        receipt["status"] = "UNKNOWN_INTERRUPTED"
        receipt["stop_reason"] = str(error)
        exit_code = 75
    except Exception as error:
        receipt["status"] = "ERROR_NO_SCIENTIFIC_VERDICT"
        receipt["error"] = f"{type(error).__name__}: {error}"
        exit_code = 2
    receipt["elapsed_seconds"] = time.monotonic() - started
    with (args.output / "receipt.json").open("x") as handle:
        json.dump(receipt, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"status": receipt["status"], "output": str(args.output),
                      "ranks_completed": len(receipt["cases"]),
                      "elapsed_seconds": receipt["elapsed_seconds"]}))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
