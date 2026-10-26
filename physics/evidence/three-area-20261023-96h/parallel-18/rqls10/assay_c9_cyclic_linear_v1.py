#!/usr/bin/env python3
"""Unexecuted scientific source. Run only under a separately named parent GO.

Fixed question: all relative Paley-9 cores, rho(t)=-t, arbitrary complex
compatibility phases. A verified row identity lambda*M=e_j excludes a core
pair because a phase coordinate cannot be zero. A surviving linear kernel
is NOT a phase witness, a feasible ONB triple, or a QLS(10) witness.

Only Python standard library; one process, no subprocesses/threads/network.
"""
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import os
import resource
import signal
import sys
import time

VERSION = "rqls-c9-cyclic-linear-v1"
ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
W2 = (Fraction(-3, 4), Fraction(1, 4))
WMINUS2 = (Fraction(-3, 4), Fraction(-1, 4))
_requested_stop = None


class CooperativeStop(Exception):
    pass


class ControlFailure(Exception):
    pass


def observe_utc():
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stop_signal(signum, _frame):
    global _requested_stop
    _requested_stop = signal.Signals(signum).name


def check_stop(context):
    if _requested_stop is not None:
        raise CooperativeStop(_requested_stop)
    if time.monotonic() >= context["deadline"]:
        raise CooperativeStop("COOPERATIVE_DEADLINE")


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def mul(x, y):
    return (x[0] * y[0] - 7 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


def inverse(x):
    norm = x[0] * x[0] + 7 * x[1] * x[1]
    if norm == 0:
        raise ArithmeticError("ZERO_FIELD_DIVISOR")
    return (x[0] / norm, -x[1] / norm)


def packed(x):
    denominator = math.lcm(x[0].denominator, x[1].denominator)
    return [int(x[0] * denominator), int(x[1] * denominator), denominator]


def reduced(matrix, context):
    """Exact RREF with row-combination history, over Q[s]/(s^2+7)."""
    n = len(matrix)
    rows = [list(row) + [ONE if i == j else ZERO for j in range(n)]
            for i, row in enumerate(matrix)]
    pivot_columns = []
    pivot_row = 0
    for column in range(n):
        check_stop(context)
        chosen = next((i for i in range(pivot_row, n)
                       if rows[i][column] != ZERO), None)
        if chosen is None:
            continue
        rows[pivot_row], rows[chosen] = rows[chosen], rows[pivot_row]
        factor = inverse(rows[pivot_row][column])
        rows[pivot_row] = [mul(value, factor) for value in rows[pivot_row]]
        for i in range(n):
            check_stop(context)
            if i == pivot_row or rows[i][column] == ZERO:
                continue
            coefficient = rows[i][column]
            rows[i] = [sub(value, mul(coefficient, pivot_value))
                       for value, pivot_value in zip(rows[i], rows[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == n:
            break
    return rows, pivot_columns


def forced_coordinate(rows, pivots):
    n = len(rows)
    choices = []
    for i, column in enumerate(pivots):
        if all(rows[i][j] == ZERO for j in range(n) if j != column):
            choices.append((column, rows[i][n:]))
    return min(choices, key=lambda item: item[0]) if choices else None


def kernel_basis(rows, pivots):
    n = len(rows)
    free_columns = [j for j in range(n) if j not in pivots]
    basis = []
    for free in free_columns:
        vector = [ZERO] * n
        vector[free] = ONE
        for i, pivot in enumerate(pivots):
            vector[pivot] = neg(rows[i][free])
        basis.append(vector)
    return basis


def row_identity_holds(matrix, coordinate, coefficients):
    n = len(matrix)
    for j in range(n):
        total = ZERO
        for i in range(n):
            total = add(total, mul(coefficients[i], matrix[i][j]))
        if total != (ONE if j == coordinate else ZERO):
            return False
    return True


def kernel_vector_holds(matrix, vector):
    for row in matrix:
        total = ZERO
        for a, b in zip(row, vector):
            total = add(total, mul(a, b))
        if total != ZERO:
            return False
    return True


def field_subtract(a, b):
    return ((a % 3 - b % 3) % 3) + 3 * ((a // 3 - b // 3) % 3)


def field_negative(a):
    return ((-a % 3) % 3) + 3 * ((-(a // 3)) % 3)


def character(a):
    norm = ((a % 3) ** 2 + (a // 3) ** 2) % 3
    return 0 if norm == 0 else (1 if norm == 1 else -1)


def paley_character_matrix():
    return tuple(tuple(character(field_subtract(a, b)) for b in range(9))
                 for a in range(9))


def coefficient_matrix(q, qprime, rho):
    result = []
    for i in range(9):
        row = []
        for t in range(9):
            if t == i or t == rho[i]:
                row.append(ZERO)
                continue
            difference = qprime[t][rho[i]] - q[t][i]
            if difference == 0:
                row.append(ONE)
            elif difference == 2:
                row.append(W2)
            elif difference == -2:
                row.append(WMINUS2)
            else:
                raise ArithmeticError("NON_CHARACTER_EXPONENT_DIFFERENCE")
        result.append(row)
    return result


def cycles_of(permutation):
    unseen = set(range(len(permutation)))
    cycles = []
    while unseen:
        start = min(unseen)
        cycle = []
        at = start
        while at in unseen:
            unseen.remove(at)
            cycle.append(at)
            at = permutation[at]
        cycles.append(cycle)
    return cycles


def reduced_rank_mod7(matrix):
    rows = [[value % 7 for value in row] for row in matrix]
    rank = 0
    for column in range(len(rows[0])):
        chosen = next((i for i in range(rank, len(rows)) if rows[i][column]), None)
        if chosen is None:
            continue
        rows[rank], rows[chosen] = rows[chosen], rows[rank]
        factor = pow(rows[rank][column], -1, 7)
        rows[rank] = [(value * factor) % 7 for value in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [(a - coefficient * b) % 7
                           for a, b in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def orbit_constant_reduction(rho):
    cycles = cycles_of(rho)
    nmatrix = [[1 - int(t == i) - int(t == rho[i])
                + int(rho[i] == i and t == i) for t in range(9)]
               for i in range(9)]
    return [[sum(nmatrix[orbit[0]][t] for t in other) % 7
             for other in cycles] for orbit in cycles]


def controls(q, rho, context, results):
    def require(name, condition):
        results.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise ControlFailure(name)
        check_stop(context)

    require("field_s_squared_minus7", mul((Fraction(0), Fraction(1)),
                                           (Fraction(0), Fraction(1)))
            == (Fraction(-7), Fraction(0)))
    require("field_inverse_positive_norm", mul(W2, inverse(W2)) == ONE)
    require("root_phase_product", mul(W2, WMINUS2) == ONE)
    require("character_paley_identity", all(
        sum(q[i][t] * q[t][j] for t in range(9))
        == (9 if i == j else 0) - 1
        for i in range(9) for j in range(9)))

    identity_rho = tuple(range(9))
    identity_matrix = coefficient_matrix(q, q, identity_rho)
    rows, pivots = reduced(identity_matrix, context)
    certificate = forced_coordinate(rows, pivots)
    require("identity_matching_rank9", len(pivots) == 9)
    require("identity_matching_row_certificate", certificate is not None
            and row_identity_holds(identity_matrix, *certificate))
    coordinate, coefficients = certificate
    damaged = list(coefficients)
    damaged[0] = add(damaged[0], ONE)
    require("corrupted_certificate_rejected_for_identity",
            not row_identity_holds(identity_matrix, coordinate, damaged))

    same = coefficient_matrix(q, q, rho)
    rows, pivots = reduced(same, context)
    certificate = forced_coordinate(rows, pivots)
    require("commuting_same_core_fixed_coordinate_forced",
            certificate is not None and certificate[0] == 0
            and row_identity_holds(same, *certificate))

    opposite_q = tuple(tuple(-value for value in row) for row in q)
    opposite = coefficient_matrix(q, opposite_q, rho)
    rows, pivots = reduced(opposite, context)
    certificate = forced_coordinate(rows, pivots)
    basis = kernel_basis(rows, pivots)
    require("commuting_conjugate_core_rank5", len(pivots) == 5)
    require("commuting_conjugate_core_fixed_coordinate_forced",
            certificate is not None and certificate[0] == 0
            and row_identity_holds(opposite, *certificate))
    require("commuting_conjugate_kernel_not_phase_witness",
            len(basis) == 4 and all(vector[0] == ZERO
                                   and kernel_vector_holds(opposite, vector)
                                   for vector in basis))

    require("orbit_constant_identity_restriction_rank9",
            reduced_rank_mod7(orbit_constant_reduction(identity_rho)) == 9)
    require("orbit_constant_inversion_restriction_rank5",
            reduced_rank_mod7(orbit_constant_reduction(rho)) == 5)
    nine_cycle = tuple((i + 1) % 9 for i in range(9))
    require("odd_derangement_singular_reduction_is_inconclusive",
            reduced_rank_mod7(orbit_constant_reduction(nine_cycle)) == 0)

    zero_matrix = [[ZERO] * 9 for _ in range(9)]
    rows, pivots = reduced(zero_matrix, context)
    basis = kernel_basis(rows, pivots)
    require("zero_matrix_survives_not_false_unsat", len(pivots) == 0
            and forced_coordinate(rows, pivots) is None and len(basis) == 9)


def write_json_exclusive(path, value):
    with path.open("x", encoding="utf-8") as output:
        json.dump(value, output, indent=2, sort_keys=True)
        output.write("\n")


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python3 -B assay_c9_cyclic_linear_v1.py REQUEST_JSON OUTPUT_DIRECTORY")
    request_path = Path(sys.argv[1]).resolve()
    output_directory = Path(sys.argv[2]).resolve()
    owned_root = Path(__file__).resolve().parent
    if request_path.parent != owned_root or output_directory.parent != owned_root:
        raise SystemExit("REQUEST_AND_OUTPUT_MUST_BE_DIRECTLY_INSIDE_OWNED_ROOT")
    request = json.loads(request_path.read_text(encoding="utf-8"))
    if request["algorithm_version"] != VERSION:
        raise SystemExit("REQUEST_VERSION_MISMATCH")
    if sha256_file(__file__) != request["source_sha256"]:
        raise SystemExit("SOURCE_PIN_MISMATCH")
    if sha256_file(sys.executable) != request["interpreter_sha256"]:
        raise SystemExit("INTERPRETER_PIN_MISMATCH")
    seconds = request["maximum_seconds"]
    output_cap = request["maximum_output_bytes"]
    if not isinstance(seconds, int) or not 1 <= seconds <= 600:
        raise SystemExit("COOPERATIVE_SECONDS_OUTSIDE_FROZEN_MAXIMUM")
    if output_cap != 16 * 1024 * 1024:
        raise SystemExit("OUTPUT_CAP_MISMATCH")
    if request["expected_raw_permutations"] != 40320 or request["expected_distinct_cores"] != 5040:
        raise SystemExit("COVERAGE_CONTRACT_MISMATCH")

    output_directory.mkdir(exist_ok=False)
    started_monotonic = time.monotonic()
    context = {"deadline": started_monotonic + seconds}
    signal.signal(signal.SIGTERM, stop_signal)
    signal.signal(signal.SIGINT, stop_signal)
    summary = {
        "algorithm_version": VERSION,
        "scope": "FIXED_ETAOUI_CORE_PAIR_ROUTE_RHO_INVERSION_ONLY",
        "scientific_meaning": "Exclusion certificates or surviving LINEAR kernels; NEVER phase or QLS witnesses",
        "started_observed_utc": observe_utc(),
        "pid": os.getpid(), "pgid": os.getpgid(0),
        "source_sha256": sha256_file(__file__),
        "request_sha256": sha256_file(request_path),
        "interpreter_path_observed": sys.executable,
        "interpreter_sha256": sha256_file(sys.executable),
        "python_version_observed": sys.version,
        "raw_permutations_visited": 0,
        "completed_distinct_cores": 0,
        "excluded_core_pairs": 0,
        "surviving_linear_kernels": 0,
        "target_cases_bytes": 0,
        "coverage_complete": False,
        "status": "UNKNOWN_NOT_STARTED",
    }
    control_results = []
    case_digest = hashlib.sha256()
    exit_code = 4
    try:
        q = paley_character_matrix()
        rho = tuple(field_negative(i) for i in range(9))
        summary["rho"] = rho
        controls(q, rho, context, control_results)
        seen = set()
        with (output_directory / "cases.jsonl").open("x", encoding="utf-8") as case_file:
            for rest in permutations(range(1, 9)):
                check_stop(context)
                summary["raw_permutations_visited"] += 1
                permutation = (0,) + rest
                qprime = tuple(tuple(q[permutation[t]][permutation[j]]
                                     for j in range(9)) for t in range(9))
                if qprime in seen:
                    continue
                matrix = coefficient_matrix(q, qprime, rho)
                rows, pivots = reduced(matrix, context)
                certificate = forced_coordinate(rows, pivots)
                record = {
                    "case_index": summary["completed_distinct_cores"],
                    "relative_permutation_row_to_old_label": permutation,
                    "character_rows": qprime,
                    "rank": len(pivots),
                }
                if certificate is not None:
                    if not row_identity_holds(matrix, *certificate):
                        raise ArithmeticError("PRODUCER_ROW_CERTIFICATE_IDENTITY_FAILURE")
                    record["status"] = "EXCLUDED_BY_FORCED_ZERO_PHASE_COORDINATE"
                    record["zero_coordinate"] = certificate[0]
                    record["row_certificate"] = [packed(value) for value in certificate[1]]
                else:
                    basis = kernel_basis(rows, pivots)
                    if not all(kernel_vector_holds(matrix, vector) for vector in basis):
                        raise ArithmeticError("PRODUCER_KERNEL_IDENTITY_FAILURE")
                    record["status"] = "SURVIVING_LINEAR_KERNEL_NOT_PHASE_WITNESS"
                    record["kernel_basis"] = [[packed(value) for value in vector] for vector in basis]
                serialized = json.dumps(record, separators=(",", ":")) + "\n"
                encoded = serialized.encode("utf-8")
                if summary["target_cases_bytes"] + len(encoded) > output_cap - 131072:
                    raise CooperativeStop("OUTPUT_CAP")
                case_file.write(serialized)
                case_file.flush()
                case_digest.update(encoded)
                seen.add(qprime)
                summary["target_cases_bytes"] += len(encoded)
                summary["completed_distinct_cores"] += 1
                key = "excluded_core_pairs" if certificate is not None else "surviving_linear_kernels"
                summary[key] += 1
        if (summary["raw_permutations_visited"] != 40320
                or summary["completed_distinct_cores"] != 5040):
            raise ArithmeticError("EXACT_COVERAGE_COUNT_MISMATCH")
        summary["coverage_complete"] = True
        summary["status"] = ("EVERY_CORE_PAIR_EXCLUDED_ROUTE_CLAIM_PENDING_INDEPENDENT_REPLAY"
                             if summary["surviving_linear_kernels"] == 0
                             else "SURVIVING_LINEAR_KERNEL_CANDIDATES_REQUIRE_EXACT_WRITTEN_FOLLOWUP")
        exit_code = 0
    except CooperativeStop as error:
        summary["status"] = "UNKNOWN_PARTIAL"
        summary["stop_reason"] = str(error)
        exit_code = 3
    except ControlFailure as error:
        summary["status"] = "CONTROL_FAILURE_NO_TARGET_VERDICT"
        summary["failed_control"] = str(error)
        exit_code = 2
    except Exception as error:
        summary["status"] = "ERROR_UNKNOWN"
        summary["error_type"] = type(error).__name__
        summary["error"] = str(error)
        exit_code = 4
    finally:
        summary["settled_observed_utc"] = observe_utc()
        summary["elapsed_seconds_observed"] = time.monotonic() - started_monotonic
        summary["cases_sha256"] = case_digest.hexdigest()
        summary["controls_passed"] = sum(int(item["passed"]) for item in control_results)
        summary["controls_recorded"] = len(control_results)
        maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        summary["peak_self_rss_bytes_observed"] = maxrss if sys.platform == "darwin" else maxrss * 1024
        summary["child_processes_started_by_source"] = 0
        summary["exit_code"] = exit_code
        write_json_exclusive(output_directory / "controls.json", control_results)
        write_json_exclusive(output_directory / "settlement.json", summary)
    print(json.dumps({"status": summary["status"], "coverage_complete": summary["coverage_complete"],
                      "completed_distinct_cores": summary["completed_distinct_cores"],
                      "excluded_core_pairs": summary["excluded_core_pairs"],
                      "surviving_linear_kernels": summary["surviving_linear_kernels"],
                      "output_directory": str(output_directory), "exit_code": exit_code}, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
