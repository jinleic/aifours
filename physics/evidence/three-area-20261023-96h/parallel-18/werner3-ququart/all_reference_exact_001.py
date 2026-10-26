"""Proposal-only exact all-reference-route falsification assay.

DO NOT EXECUTE without a fresh named parent GO for these exact source bytes.
Finite PSD cases cannot prove the all-reference or unrestricted W4 statements.
A negative co-Choi certificate refutes this sufficient route only, not W4.

Standard library only; no subprocess, network, model CLI or dependency changes.
The LDL/zero-pivot pattern is inherited from grouped_reference_exact_v1.py;
this is not an independent third verifier of that implementation.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import datetime
from fractions import Fraction as Q
import hashlib
import itertools
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

D = 4
PAIRS = tuple(itertools.product(range(D), repeat=2))
BASIS = tuple(itertools.product(range(D), repeat=4))
ZERO = Q(0)
ONE = Q(1)
DEADLINE = float("inf")
RSS_GUARD_BYTES = 512 * 1024 * 1024
CONTROLS = (("product", (1, 0, 0, 0)),
            ("supported_two_pair", (Q(1), Q(1), Q(1, 4), Q(1, 4))))
TARGETS = (("full_hierarchy", (16, 4, 2, 1)),
           ("full_balanced", (4, 3, 2, 1)),
           ("rank3_near_product", (8, 2, 1, 0)),
           ("rank3_distinct", (4, 2, 1, 0)),
           ("rank2_unequal", (3, 2, 0, 0)),
           ("rank3_middle_pair", (2, 1, 1, 0)),
           ("full_one_pair", (4, 4, 2, 1)))


class Stopped(Exception):
    pass


def rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def check_limits():
    if time.monotonic() >= DEADLINE:
        raise Stopped("internal monotonic deadline reached")
    if rss_bytes() > RSS_GUARD_BYTES:
        raise Stopped("cooperative RSS guard exceeded512MiB")


def on_signal(signum, _frame):
    raise Stopped(f"received signal {signum}")


def dot(left, right):
    return sum((a * b for a, b in zip(left, right) if a and b), ZERO)


def quadratic(matrix, vector):
    return sum((vector[i] * dot(row, vector)
                for i, row in enumerate(matrix) if vector[i]), ZERO)


def exact_psd(matrix):
    """Exact square completion; zero-pivot coupling gives a negative vector."""
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
        check_limits()
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
                raise ArithmeticError("negative-vector reconstruction failed")
            return {"verdict": "INDEFINITE", "failed_pivot": k,
                    "witness": list(map(str, vector)),
                    "exact_value": str(value)}
        pivots.append(pivot)
        if pivot == 0:
            continue
        for j in range(k + 1, size):
            upper[k][j] = residual[k][j] / pivot
        for i in range(k + 1, size):
            for j in range(i, size):
                value = residual[i][j] - residual[k][i] * residual[k][j] / pivot
                residual[i][j] = value
                residual[j][i] = value
    rebuilt = [[ZERO for _ in range(size)] for _ in range(size)]
    for k, pivot in enumerate(pivots):
        check_limits()
        row = upper[k][:]
        row[k] = ONE
        for i in range(size):
            for j in range(size):
                rebuilt[i][j] += pivot * row[i] * row[j]
    if rebuilt != matrix:
        raise ArithmeticError("exact LDL identity failed")
    return {"verdict": "PSD", "positive_pivots": sum(p > 0 for p in pivots),
            "zero_pivots": sum(p == 0 for p in pivots),
            "pivots": list(map(str, pivots)),
            "unit_upper_rows": [[str(upper[i][j]) for j in range(i + 1, size)]
                                for i in range(size)]}


def inverse(matrix):
    size = len(matrix)
    work = [row[:] + [Q(int(i == j)) for j in range(size)]
            for i, row in enumerate(matrix)]
    for k in range(size):
        check_limits()
        pivot_row = next((i for i in range(k, size) if work[i][k]), None)
        if pivot_row is None:
            raise ArithmeticError("singular full reference inverse")
        work[k], work[pivot_row] = work[pivot_row], work[k]
        pivot = work[k][k]
        work[k] = [value / pivot for value in work[k]]
        for i in range(size):
            if i != k and work[i][k]:
                factor = work[i][k]
                work[i] = [a - factor * b for a, b in zip(work[i], work[k])]
    result = [row[size:] for row in work]
    for i in range(size):
        for j in range(size):
            if sum((matrix[i][k] * result[k][j] for k in range(size)), ZERO) != int(i == j):
                raise ArithmeticError("full inverse product identity failed")
    return result


def weight(state):
    a, b, c, d = state
    result = [0] * D
    result[a] += 1
    result[b] -= 1
    result[c] += 1
    result[d] -= 1
    return tuple(result)


def c_entry(left, right):
    a, b, c, d = left
    e, f, g, h = right
    identity = int(a == e and b == f and c == g and d == h)
    swap1 = int(a == g and c == e and b == f and d == h)
    swap2 = int(b == h and d == f and a == e and c == g)
    both = int(a == g and c == e and b == h and d == f)
    return Q(identity) - Q(swap1 + swap2, 2) + Q(both, 4)


def physical_data(amplitudes):
    c = tuple(map(Q, amplitudes))
    norm = sum((x * x for x in c), ZERO)
    eta = [c[a] if a == b else ZERO for a, b in PAIRS]
    reference = [[(norm - (c[a] ** 2 + c[b] ** 2) / 2) * int(i == j)
                  + eta[i] * eta[j] / 4
                  for j in range(16)] for i, (a, b) in enumerate(PAIRS)]
    inv = inverse(reference)
    operators = []
    for a, b in PAIRS:
        rows = [defaultdict(Q) for _ in PAIRS]
        for column, (e, f) in enumerate(PAIRS):
            if a == b:
                rows[column][column] += c[a]
            if e == b:
                rows[a * D + f][column] -= c[b] / 2
            if f == a:
                rows[e * D + b][column] -= c[a] / 2
            if e == f:
                rows[a * D + b][column] += c[e] / 4
        operators.append([{key: value for key, value in row.items() if value}
                          for row in rows])
    weighted = [[{i: sum((inv[i][j] * value for j, value in row.items()), ZERO)
                  for i in range(16)} for row in rows] for rows in operators]
    return c, eta, reference, inv, operators, weighted


def s_entry(i, out, j, other, rows, weighted):
    return sum((value * weighted[i][other].get(k, ZERO)
                for k, value in rows[j][out].items()), ZERO)


def literal_b(matrix):
    """Second physical encoding: literal partial traces, not L's closed formula."""
    trace = sum((matrix[i][i] for i in range(16)), ZERO)
    tr2 = [[sum((matrix[u * D + b][v * D + b] for b in range(D)), ZERO)
            for v in range(D)] for u in range(D)]
    tr1 = [[sum((matrix[a * D + u][a * D + v] for a in range(D)), ZERO)
            for v in range(D)] for u in range(D)]
    return [[trace * int(a == e and b == f)
             - tr2[a][e] * int(b == f) / 2
             - tr1[b][f] * int(a == e) / 2 + matrix[i][j] / 4
             for j, (e, f) in enumerate(PAIRS)]
            for i, (a, b) in enumerate(PAIRS)]


def literal_negative_reconstruction(amplitudes, sparse, c_scale, s_sign):
    """Raw candidate check; shared rational/inverse code, NOT a third verifier."""
    check_limits()
    coeff = tuple(map(Q, amplitudes))
    eta = [coeff[a] if a == b else ZERO for a, b in PAIRS]
    reference = literal_b([[a * b for b in eta] for a in eta])
    inv = inverse(reference)
    operators = []
    for i in range(16):
        argument = [[eta[j] if row == i else ZERO for j in range(16)]
                    for row in range(16)]
        operators.append(literal_b(argument))
    # C quadratic through four explicit permutations, without c_entry.
    c_value = ZERO
    for index, value in sparse.items():
        a, b, c, d = BASIS[index]
        c_value += value * sparse.get(index, ZERO)
        for state, factor in (((c, b, a, d), Q(-1, 2)),
                              ((a, d, c, b), Q(-1, 2)),
                              ((c, d, a, b), Q(1, 4))):
            partner = ((state[0] * D + state[1]) * D + state[2]) * D + state[3]
            c_value += factor * value * sparse.get(partner, ZERO)
    s_value = ZERO
    for left, lv in sparse.items():
        check_limits()
        i, out = divmod(left, 16)
        for right, rv in sparse.items():
            j, other = divmod(right, 16)
            left_vector = operators[j][out]
            right_vector = operators[i][other]
            transformed = [dot(row, right_vector) for row in inv]
            s_value += lv * rv * dot(left_vector, transformed)
    return {"C": str(c_value), "S": str(s_value),
            "required_form": str(c_scale * c_value + s_sign * s_value),
            "encoding": "literalB partial traces plus explicit C permutations",
            "independence_limit": "shares Fraction and inverse routine; parent written reconstruction required"}


def build_matrices(amplitudes, groups):
    check_limits()
    c, eta, reference, inv, rows, weighted = physical_data(amplitudes)
    # Direct full reference comparison, independent of the diagonal formula.
    if literal_b([[a * b for b in eta] for a in eta]) != reference:
        raise ArithmeticError("literal/full reference mismatch")
    cm = [[ZERO for _ in BASIS] for _ in BASIS]
    sm = [[ZERO for _ in BASIS] for _ in BASIS]
    digest = hashlib.sha256()
    cross_count = 0
    for left, state in enumerate(BASIS):
        check_limits()
        i, out = divmod(left, 16)
        for right in range(left + 1):
            j, other = divmod(right, 16)
            cv = c_entry(state, BASIS[right])
            sv = s_entry(i, out, j, other, rows, weighted)
            if sv != s_entry(j, other, i, out, rows, weighted):
                raise ArithmeticError("co-Choi symmetry mismatch")
            if weight(state) != weight(BASIS[right]):
                cross_count += 1
                if cv or sv:
                    raise ArithmeticError("nonzero discarded phase coupling")
            cm[left][right] = cm[right][left] = cv
            sm[left][right] = sm[right][left] = sv
            digest.update(f"{left},{right}:{cv}:{sv}\n".encode())
    return cm, sm, {"upper_triangle_C_S_sha256": digest.hexdigest(),
                    "discarded_cross_weight_entries_exactly_checked": cross_count,
                    "amplitudes": list(map(str, c)),
                    "full_inverse_dimension": 16}


def assay(name, amplitudes, groups, known_positive=False):
    cm, sm, report = build_matrices(amplitudes, groups)
    report["name"] = name
    report["forms"] = {}
    for form, c_scale, s_sign in (("upper_C_minus_S", Q(1), Q(-1)),
                                   ("lower_3C_plus_S", Q(3), Q(1))):
        blocks = []
        for block_weight, indices in sorted(groups.items()):
            check_limits()
            matrix = [[c_scale * cm[i][j] + s_sign * sm[i][j]
                       for j in indices] for i in indices]
            answer = exact_psd(matrix)
            answer["weight"] = block_weight
            answer["basis_indices"] = indices
            blocks.append(answer)
            if answer["verdict"] == "INDEFINITE":
                sparse = {index: Q(value) for index, value in zip(indices, answer["witness"])
                          if Q(value)}
                raw = literal_negative_reconstruction(amplitudes, sparse, c_scale, s_sign)
                if Q(raw["required_form"]) != Q(answer["exact_value"]):
                    raise ArithmeticError("literal negative-form reconstruction mismatch")
                if Q(raw["required_form"]) >= 0:
                    raise ArithmeticError("literal candidate is not negative")
                if known_positive:
                    raise ArithmeticError("supported positive control failed")
                answer["literal_reconstruction"] = raw
                answer["sparse_witness_global_indices"] = {str(k): str(v) for k, v in sparse.items()}
                report["forms"][form] = {"verdict": "INDEFINITE", "blocks": blocks}
                report["status"] = "ROUTE_FAILURE_CANDIDATE_NOT_W4_WITNESS"
                return report
        report["forms"][form] = {"verdict": "PSD", "blocks": blocks}
    report["status"] = "LISTED_REFERENCE_EXACT_PSD_ONLY"
    return report


def controls(groups):
    logic = []
    for matrix, expected in (([[ONE, ONE], [ONE, ONE]], "PSD"),
                             ([[ZERO, ONE], [ONE, ZERO]], "INDEFINITE"),
                             ([[-ONE, ZERO], [ZERO, ZERO]], "INDEFINITE")):
        result = exact_psd(matrix)
        if result["verdict"] != expected:
            raise ArithmeticError("congruence intended-reason control failed")
        logic.append(result)
    cm, sm, metadata = build_matrices((1, 1, 0, 0), groups)
    vector = [ZERO for _ in BASIS]
    for index, (a, b, c, d) in enumerate(BASIS):
        if max(a, b, c, d) < 2:
            vector[index] = Q(int(a == b and c == d) + 2 * int(a == d and b == c))
    symmetric_value = quadratic([[cm[i][j] + sm[i][j] for j in range(256)]
                                 for i in range(256)], vector)
    if symmetric_value != -2:
        raise ArithmeticError("known symmetric-route negative control expected -2")
    positives = [assay(name, coeff, groups, known_positive=True) for name, coeff in CONTROLS]
    return {"exact_congruence_controls": logic,
            "known_symmetric_negative_control": {**metadata, "value": str(symmetric_value)},
            "supported_positive_controls": positives}


def main():
    global DEADLINE
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", required=True, type=float)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if not 0 < args.seconds <= 180:
        parser.error("seconds must lie in(0,180]")
    lane = Path(__file__).resolve().parent
    if args.output.resolve().parent != lane:
        parser.error("output must be a fresh direct child of the owned lane")
    os.mkdir(args.output)
    started = time.monotonic()
    DEADLINE = started + args.seconds
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    receipt = {"status": "RUNNING", "actual_start": datetime.now().astimezone().isoformat(),
               "pid": os.getpid(), "pgid": os.getpgid(0), "argv": sys.argv,
               "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "interpreter": sys.executable, "cooperative_seconds": args.seconds,
               "rss_guard_bytes": RSS_GUARD_BYTES,
               "scope": "fixed finite exact falsification assay; not all-reference proof or W4",
               "targets": [{"name": name, "coefficients": list(map(str, coeff))} for name, coeff in TARGETS],
               "cases": []}
    exit_code = 0
    try:
        groups = defaultdict(list)
        for i, state in enumerate(BASIS):
            groups[weight(state)].append(i)
        profile = {size: sum(len(v) == size for v in groups.values()) for size in (1, 2, 4, 12, 28)}
        if profile != {1: 12, 2: 24, 4: 6, 12: 12, 28: 1} or sum(map(len, groups.values())) != 256:
            raise ArithmeticError("exact phase-profile control failed")
        receipt["phase_profile"] = profile
        receipt["controls"] = controls(groups)
        for name, coeff in TARGETS:
            receipt["current_target"] = name
            result = assay(name, coeff, groups)
            receipt["cases"].append(result)
            if result["status"] == "ROUTE_FAILURE_CANDIDATE_NOT_W4_WITNESS":
                receipt["status"] = "ROUTE_FAILURE_CANDIDATE_REQUIRES_WRITTEN_RECONSTRUCTION"
                break
        else:
            receipt["status"] = "COMPLETE_LISTED_REFERENCES_ONLY_NO_UNIVERSAL_VERDICT"
    except Stopped as error:
        receipt["status"] = "UNKNOWN_INTERRUPTED_NOT_MATHEMATICAL_EXHAUSTION"
        receipt["stop_reason"] = str(error)
        exit_code = 75
    except Exception as error:
        receipt["status"] = "ERROR_NO_SCIENTIFIC_VERDICT"
        receipt["error"] = f"{type(error).__name__}: {error}"
        exit_code = 2
    receipt["actual_finish"] = datetime.now().astimezone().isoformat()
    receipt["elapsed_seconds"] = time.monotonic() - started
    receipt["max_rss_bytes"] = rss_bytes()
    with (args.output / "receipt.json").open("x") as handle:
        json.dump(receipt, handle, indent=2)
        handle.write("\n")
    print(json.dumps({"status": receipt["status"], "output": str(args.output),
                      "cases_completed": len(receipt["cases"]), "elapsed_seconds": receipt["elapsed_seconds"]}))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
