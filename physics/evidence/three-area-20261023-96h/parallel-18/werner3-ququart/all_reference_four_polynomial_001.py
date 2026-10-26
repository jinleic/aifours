"""UNEXECUTED proposal: exact universal four-block coefficient certificate.

Fresh named parent admission is REQUIRED before import/check/execute.
This is symbolic integer algebra, not a new fixed-reference sampling batch.
A negative coefficient is INCONCLUSIVE, not a negative matrix or W4 witness.
Normal exit records only a planned code; the external wrapper attests actual exit.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import itertools
import json
from math import comb
import os
from pathlib import Path
import resource
import signal
import sys
import time

ZERO_EXP = (0, 0, 0, 0)
DEADLINE = float("inf")
FIRST_STOP_SIGNAL = None
RSS_GUARD_BYTES = 512 * 1024 * 1024


class Stopped(Exception):
    pass


def rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def check_limits():
    if FIRST_STOP_SIGNAL is not None:
        raise Stopped(f"latched first stop signal {FIRST_STOP_SIGNAL}")
    if time.monotonic() >= DEADLINE:
        raise Stopped("internal monotonic deadline reached")
    if rss_bytes() > RSS_GUARD_BYTES:
        raise Stopped("cooperative RSS guard exceeded512MiB")


def on_signal(signum, _frame):
    global FIRST_STOP_SIGNAL
    if FIRST_STOP_SIGNAL is None:
        FIRST_STOP_SIGNAL = signum


def constant(value):
    return {ZERO_EXP: value} if value else {}


def variable(index):
    exp = tuple(int(i == index) for i in range(4))
    return {exp: 1}


def scale(poly, value):
    return {exp: coefficient * value for exp, coefficient in poly.items() if coefficient * value}


def add(*polys):
    answer = {}
    for poly in polys:
        for exp, coefficient in poly.items():
            answer[exp] = answer.get(exp, 0) + coefficient
    return {exp: coefficient for exp, coefficient in answer.items() if coefficient}


def mul(left, right):
    answer = {}
    for lexp, lc in left.items():
        check_limits()
        for rexp, rc in right.items():
            exp = tuple(a + b for a, b in zip(lexp, rexp))
            answer[exp] = answer.get(exp, 0) + lc * rc
    return {exp: coefficient for exp, coefficient in answer.items() if coefficient}


def product(*polys):
    answer = constant(1)
    for poly in polys:
        answer = mul(answer, poly)
    return answer


def power(poly, exponent):
    answer = constant(1)
    for _ in range(exponent):
        answer = mul(answer, poly)
    return answer


def determinant(matrix):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("nonsquare polynomial matrix")
    answer = {}
    for permutation in itertools.permutations(range(size)):
        check_limits()
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(size) for j in range(i + 1, size))
        term = product(*(matrix[i][permutation[i]] for i in range(size)))
        answer = add(answer, scale(term, -1 if inversions % 2 else 1))
    return answer


def shear(poly, axis):
    """Substitute variable_axis by variable_axis+variable_(axis+1)."""
    answer = {}
    for exp, coefficient in poly.items():
        check_limits()
        degree = exp[axis]
        for moved in range(degree + 1):
            target = list(exp)
            target[axis] -= moved
            target[axis + 1] += moved
            key = tuple(target)
            answer[key] = answer.get(key, 0) + coefficient * comb(degree, moved)
    return {exp: coefficient for exp, coefficient in answer.items() if coefficient}


def ordered_gap(poly, permutation):
    permuted = {tuple(exp[i] for i in permutation): coefficient
                for exp, coefficient in poly.items()}
    for axis in range(3):
        permuted = shear(permuted, axis)
    return permuted


def encode(poly):
    return [[list(exp), str(coefficient)] for exp, coefficient in sorted(poly.items())]


def homogeneous(poly, degree):
    return bool(poly) and all(sum(exp) == degree for exp in poly)


def defining_matrix():
    p = [variable(i) for i in range(4)]
    total = add(*p)
    e2 = add(*(mul(p[i], p[j]) for i in range(4) for j in range(i + 1, 4)))
    e3 = add(*(product(p[i], p[j], p[k]) for i in range(4)
               for j in range(i + 1, 4) for k in range(j + 1, 4)))
    w3 = add(power(total, 3), scale(mul(total, e2), 2), scale(e3, -1))
    dab = add(scale(total, 2), scale(p[0], -1), scale(p[1], -1))
    dcd = add(scale(total, 2), scale(p[2], -1), scale(p[3], -1))
    common = scale(product(w3, dab, dcd), 4)
    matrix = [[{} for _ in range(4)] for _ in range(4)]
    for i in range(4):
        matrix[i][i] = common
    alpha_ac = product(total,
                       add(scale(power(total, 2), 2), mul(add(p[0], p[2]), add(p[1], p[3]))),
                       dab, dcd)
    alpha_ad = product(total,
                       add(scale(power(total, 2), 2), mul(add(p[0], p[3]), add(p[1], p[2]))),
                       dab, dcd)
    entries = {(0, 1): alpha_ac, (2, 3): alpha_ad,
               (0, 2): scale(product(w3, dcd, add(scale(total, 2), scale(p[1], -1))), -2),
               (1, 3): scale(product(w3, dcd, add(scale(total, 2), scale(p[0], -1))), -2),
               (0, 3): scale(product(w3, dab, add(scale(total, 2), scale(p[3], -1))), -2),
               (1, 2): scale(product(w3, dab, add(scale(total, 2), scale(p[2], -1))), -2)}
    for (i, j), poly in entries.items():
        matrix[i][j] = matrix[j][i] = poly
    if any(not homogeneous(poly, 5) for row in matrix for poly in row):
        raise ArithmeticError("defining matrix degree control failed")
    return matrix, common


def controls():
    p = [variable(i) for i in range(4)]
    difference = add(p[0], scale(p[1], -1))
    addition = add(p[0], p[1])
    if mul(difference, addition) != add(power(p[0], 2), scale(power(p[1], 2), -1)):
        raise ArithmeticError("integer multiplication cancellation control failed")
    if determinant([[p[0], p[1]], [p[2], p[3]]]) != add(mul(p[0], p[3]), scale(mul(p[1], p[2]), -1)):
        raise ArithmeticError("Leibniz determinant sign control failed")
    if ordered_gap(power(difference, 2), (0, 1, 2, 3)) != power(p[0], 2):
        raise ArithmeticError("ordered-gap cancellation control failed")
    return {"integer_cancellation": "PASS", "determinant_sign": "PASS",
            "gap_composition": "PASS", "sampling": "NONE; symbolic identities only"}


def science(receipt):
    receipt["symbolic_controls"] = controls()
    matrix, common = defining_matrix()
    common_at_one = sum(common.values())
    if common_at_one != 15552:
        raise ArithmeticError("physical common-denominator calibration failed")
    receipt["defining_polynomial_matrix"] = [[encode(poly) for poly in row] for row in matrix]
    receipt["common_positive_denominator"] = encode(common)
    expected_uniform = ((1, 1), (8, 9), (47, 108), (5, 27))
    receipt["base_minors"] = []
    for size in range(1, 5):
        check_limits()
        receipt["current_minor"] = size
        minor = determinant([row[:size] for row in matrix[:size]])
        if not homogeneous(minor, 5 * size):
            raise ArithmeticError("principal-minor degree control failed")
        numerator, denominator = expected_uniform[size - 1]
        if sum(minor.values()) * denominator != numerator * common_at_one ** size:
            raise ArithmeticError("hand-derived uniform minor calibration failed")
        receipt["base_minors"].append({"size": size, "degree": 5 * size, "coefficients": encode(minor)})
        for permutation in itertools.permutations(range(4)):
            check_limits()
            receipt["current_ordering"] = list(permutation)
            transformed = ordered_gap(minor, permutation)
            last = (0, 0, 0, 5 * size)
            if transformed.get(last, 0) != sum(minor.values()) or transformed.get(last, 0) <= 0:
                raise ArithmeticError("pure-last strictness identity failed")
            negatives = [(exp, coefficient) for exp, coefficient in transformed.items() if coefficient < 0]
            record = {"minor_size": size, "ordering": list(permutation),
                      "degree": 5 * size, "pure_last_coefficient": str(transformed[last]),
                      "coefficients": encode(transformed)}
            if negatives:
                record["status"] = "NEGATIVE_COEFFICIENT_NOT_NEGATIVE_MATRIX_VALUE"
                record["first_negative"] = [list(negatives[0][0]), str(negatives[0][1])]
                receipt["cases"].append(record)
                receipt["status"] = "COEFFICIENT_ANSATZ_INCONCLUSIVE_NOT_ROUTE_FAILURE"
                return
            record["status"] = "NONNEGATIVE_COEFFICIENTS_WITH_STRICT_PURE_LAST"
            receipt["cases"].append(record)
    receipt["status"] = "COMPLETE_SYMBOLIC_FOUR_UPPER_CERTIFICATE_CANDIDATE"


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
    receipt = {"status": "UNKNOWN_INITIALIZATION_NOT_COMPLETED", "cases": [], "argv": sys.argv,
               "cooperative_seconds": args.seconds, "rss_guard_bytes": RSS_GUARD_BYTES,
               "scope": "Universal four-block coefficient certificate only; not all-reference proof or W4"}
    started = None
    exit_code = 75
    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)
    try:
        os.mkdir(args.output)
    except OSError as error:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        try:
            print(json.dumps({"status": "NO_EXCLUSIVE_OUTPUT_NO_SCIENTIFIC_VERDICT",
                              "error": f"{type(error).__name__}: {error}", "planned_exit_code": 2}), file=sys.stderr)
        except OSError:
            pass
        return 2
    try:
        started = time.monotonic()
        DEADLINE = started + args.seconds
        receipt.update({"actual_start": datetime.now().astimezone().isoformat(),
                        "pid": os.getpid(), "pgid": os.getpgid(0), "interpreter": sys.executable,
                        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
        check_limits()
        receipt["status"] = "RUNNING"
        exit_code = 0
        science(receipt)
    except Stopped as error:
        receipt["status"] = "UNKNOWN_INTERRUPTED_NOT_MATHEMATICAL_EXHAUSTION"
        receipt["stop_reason"] = str(error)
        exit_code = 75
    except Exception as error:
        receipt["status"] = "ERROR_NO_SCIENTIFIC_VERDICT"
        receipt["error"] = f"{type(error).__name__}: {error}"
        exit_code = 2
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        if FIRST_STOP_SIGNAL is not None:
            receipt["status"] = "UNKNOWN_INTERRUPTED_NOT_MATHEMATICAL_EXHAUSTION"
            receipt["stop_reason"] = f"latched first stop signal {FIRST_STOP_SIGNAL}"
            exit_code = 75
        receipt["first_stop_signal"] = FIRST_STOP_SIGNAL
        receipt["finalization_signal_policy"] = "SIGINT_AND_SIGTERM_IGNORED_UNTIL_PROCESS_EXIT"
        try:
            receipt["actual_finalization_start"] = datetime.now().astimezone().isoformat()
            receipt["elapsed_seconds"] = None if started is None else time.monotonic() - started
            receipt["max_rss_bytes"] = rss_bytes()
        except Exception as error:
            receipt["final_metadata_error"] = f"{type(error).__name__}: {error}"
            if exit_code != 75:
                receipt["status"] = "ERROR_NO_SCIENTIFIC_VERDICT"
                exit_code = 2
        receipt["planned_exit_code_after_receipt"] = exit_code
        receipt["actual_exit_attestation"] = "REQUIRED_FROM_EXTERNAL_METADATA_WRAPPER"
        receipt["receipt_plan"] = "EXCLUSIVE_X_WRITE_FLUSH_FSYNC_CLOSE_BEFORE_SYSTEMEXIT"
        written = False
        error_text = None
        try:
            with (args.output / "receipt.json").open("x") as handle:
                json.dump(receipt, handle, indent=2)
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())
            written = True
        except Exception as error:
            error_text = f"{type(error).__name__}: {error}"
            exit_code = 2
        summary = {"status": receipt["status"] if written else "FINAL_RECEIPT_WRITE_FAILED",
                   "output": str(args.output), "receipt_written": written,
                   "coefficient_cases_completed": len(receipt["cases"]), "planned_exit_code": exit_code}
        if error_text is not None:
            summary["receipt_write_error"] = error_text
        try:
            print(json.dumps(summary), file=sys.stdout if written else sys.stderr)
        except OSError:
            pass
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
