"""One-shot normalized N4 Bose-certificate candidate screen, not a P44 proof.

PREPARATION ONLY. Do not execute, import for a probe, or run a test suite before
an exact named parent GO. No solver fallback, subprocess, network, environment
installation, adaptive input grid, or hierarchy escalation is implemented.
All numerical witnesses and PSD residuals remain candidate evidence only.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime
import hashlib
import importlib.metadata
import importlib.util
from itertools import combinations_with_replacement, permutations
import json
from math import factorial, sqrt
import os
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
NAME = "physics-ppt44-normalized-n4-001"
DECISION = "GO_ONCE_FOR_FROZEN_CANDIDATE_ASSAY_ONLY"
D, N, RAW_DIM = 4, 4, 32768
PAIRS = tuple((p, q) for p in range(16) for q in range(p, 16))
EXPECTED_VERSIONS = {"numpy": "2.5.4", "scipy": "1.18.1",
                     "cvxpy": "1.9.3", "clarabel": "0.11.1"}
THREAD_KEYS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
               "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
LAUNCH_CUTOFF = datetime.fromisoformat("2026-10-27T10:35:38-07:00")
SCIENCE_CUTOFF = datetime.fromisoformat("2026-10-27T11:05:38-07:00")
DEADLINE = float("inf")
RAM_CEILING = 8 * 1024**3
STOP_STATE = None  # Atomic (first signal, request count) snapshot; never reset.


class ControlledStop(Exception):
    pass


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def observed_clock():
    return datetime.now().astimezone().isoformat()


def peak_rss_bytes():
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else 1024 * value)


def check_clock():
    stop_state = STOP_STATE
    if stop_state is not None:
        raise ControlledStop(f"received first stop signal {stop_state[0]}")
    if time.monotonic() >= DEADLINE:
        raise ControlledStop("cooperative scientific deadline reached")
    if peak_rss_bytes() > RAM_CEILING:
        raise ControlledStop("observed peak RSS exceeded frozen8GiB ceiling")


def on_signal(signum, _frame):
    global STOP_STATE
    previous = STOP_STATE
    STOP_STATE = (signum, 1) if previous is None else (previous[0], previous[1] + 1)


def write_json_new(path, value):
    with Path(path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, allow_nan=False)
        handle.write("\n")


def validate_admission(args):
    """Metadata-only fail-closed gate, before importing scientific packages."""
    go_path = args.go.resolve()
    go = json.loads(go_path.read_text())
    if go.get("decision") != DECISION or go.get("name") != NAME:
        raise ValueError("not the exact frozen candidate-assay GO")
    if go.get("owner") != "PhysicsPPT44":
        raise ValueError("GO owner mismatch")
    request_path = Path(go["request"]).resolve()
    if request_path.parent != ROOT:
        raise ValueError("request is not inside the exclusive P44 root")
    if digest(request_path) != go["request_sha256"]:
        raise ValueError("request snapshot hash mismatch")
    request = json.loads(request_path.read_text())
    source = Path(__file__).resolve()
    checker = (source.parent / "normalized_bose_n4_definition_checker_v1.py").resolve()
    input_path = args.input.resolve()
    for key, path in (("source", source), ("definition_checker", checker),
                      ("input", input_path)):
        if Path(request[key]).resolve() != path or Path(go[key]).resolve() != path:
            raise ValueError(f"{key} path mismatch")
        actual = digest(path)
        if actual != request[key + "_sha256"] or actual != go[key + "_sha256"]:
            raise ValueError(f"{key} snapshot hash mismatch")
    interpreter = Path(sys.executable).resolve()
    if digest(interpreter) != go["interpreter_sha256"]:
        raise ValueError("interpreter identity mismatch")
    if digest(interpreter) != request["interpreter_sha256"]:
        raise ValueError("request interpreter identity mismatch")
    for key in THREAD_KEYS:
        if os.environ.get(key) != "1":
            raise ValueError(f"thread overlay {key}=1 is required before imports")
    if os.environ.get("PYTHONDONTWRITEBYTECODE") != "1":
        raise ValueError("read-only environment requires PYTHONDONTWRITEBYTECODE=1")
    if args.output.resolve().parent != ROOT:
        raise ValueError("output is outside the exclusive P44 root")
    if args.output.resolve() != Path(go["output_path"]).resolve():
        raise ValueError("output path is not admitted")
    if args.output.resolve() != Path(request["output_path"]).resolve():
        raise ValueError("output path differs from frozen request")
    if args.seconds != request["internal_seconds"] or args.seconds != go["internal_seconds"]:
        raise ValueError("scientific time bound differs from request/GO")
    now = datetime.now().astimezone()
    if now >= datetime.fromisoformat(go["launch_admission_expires_pt"]):
        raise ValueError("GO launch admission has expired")
    if now >= LAUNCH_CUTOFF:
        raise ValueError("round new-native-launch cutoff reached")
    science_end = min(SCIENCE_CUTOFF,
                      datetime.fromisoformat(go["scientific_deadline_at_pt"]))
    remaining = (science_end - now).total_seconds()
    if remaining <= 0:
        raise ValueError("round scientific deadline reached")
    versions = {name: importlib.metadata.version(name) for name in EXPECTED_VERSIONS}
    if versions != EXPECTED_VERSIONS:
        raise ValueError(f"dependency metadata mismatch: {versions}")
    return {"go": go, "go_path": str(go_path), "go_sha256": digest(go_path),
            "request_path": str(request_path), "request_sha256": digest(request_path),
            "source_sha256": digest(source), "definition_checker_sha256": digest(checker),
            "input_sha256": digest(input_path), "interpreter": str(interpreter),
            "interpreter_sha256": digest(interpreter), "dependency_versions": versions,
            "checker_path": checker, "seconds": min(args.seconds, remaining)}


def row_number(aux, physical, bob):
    result = aux * D + physical
    for state in bob:
        result = result * 8 + state
    return result


def sym_add(column, aux, physical, bob_states, weight):
    # Main implementation sums all24 permutations, including duplicate terms.
    for bob in permutations(tuple(bob_states)):
        column[row_number(aux, physical, bob)] += weight / factorial(N)


def remove_pair(total, pair):
    remaining = list(total)
    for item in pair:
        remaining.remove(item)
    return tuple(remaining)


def main_columns(spin):
    for physical in range(D):
        if spin == "J3half":
            for down in range(D):
                for up in combinations_with_replacement(range(D), 3):
                    check_clock()
                    column = defaultdict(float)
                    sym_add(column, 0, physical, (D + down, *up), 1)
                    sym_add(column, 1, physical, (down, *up), -1)
                    yield column, [physical, down, list(up)]
        elif spin == "J1half":
            for total in combinations_with_replacement(range(D), N):
                counts = Counter(total)
                pairs = [pair for pair in combinations_with_replacement(range(D), 2)
                         if not (Counter(pair) - counts)]
                reference = pairs[0]
                for down in pairs[1:]:
                    check_clock()
                    column = defaultdict(float)
                    sym_add(column, 0, physical,
                            (*remove_pair(total, down), *(D + value for value in down)), 1)
                    sym_add(column, 0, physical,
                            (*remove_pair(total, reference),
                             *(D + value for value in reference)), -1)
                    for value in reference:
                        sym_add(column, 1, physical,
                                (D + value, *remove_pair(total, (value,))), 1)
                    for value in down:
                        sym_add(column, 1, physical,
                                (D + value, *remove_pair(total, (value,))), -1)
                    yield column, [physical, list(total), list(reference), list(down)]
        else:
            raise ValueError("unknown frozen spin sector")


def make_basis(spin):
    rows, cols, values, descriptors = [], [], [], []
    for index, (column, description) in enumerate(main_columns(spin)):
        clean = {row: value for row, value in column.items() if value != 0}
        norm = sqrt(sum(value * value for value in clean.values()))
        if norm == 0:
            raise ArithmeticError("zero main highest-weight column")
        for row, value in sorted(clean.items()):
            rows.append(row)
            cols.append(index)
            values.append(value / norm)
        descriptors.append(description)
    expected = {"J3half": 320, "J1half": 260}[spin]
    if len(descriptors) != expected:
        raise ArithmeticError("main highest-weight dimension mismatch")
    return (sp.csc_matrix((values, (rows, cols)), shape=(RAW_DIM, expected)),
            descriptors)


def raising_residual(basis):
    rows, cols, values = [], [], []
    coo = basis.tocoo()
    for index, (row, col, value) in enumerate(zip(coo.row, coo.col, coo.data)):
        if index % 2048 == 0:
            check_clock()
        left, packed = divmod(int(row), 8**N)
        aux, physical = divmod(left, D)
        bob = []
        for exponent in range(N - 1, -1, -1):
            state, packed = divmod(packed, 8**exponent)
            bob.append(state)
        if aux == 1:
            rows.append(row_number(0, physical, bob))
            cols.append(int(col))
            values.append(value)
        for site in range(N):
            if bob[site] >= D:
                raised = bob[:]
                raised[site] -= D
                rows.append(row_number(aux, physical, raised))
                cols.append(int(col))
                values.append(value)
    raised = sp.csc_matrix((values, (rows, cols)), shape=basis.shape)
    return float(np.max(np.abs(raised.data))) if raised.nnz else 0.0


def contraction_map(basis):
    # Independent checker does NOT use this grouped Bell-contraction encoding.
    rows, cols, values = [], [], []
    coo = basis.tocoo()
    for index, (row, col, value) in enumerate(zip(coo.row, coo.col, coo.data)):
        if index % 2048 == 0:
            check_clock()
        left, packed = divmod(int(row), 8**N)
        alice_aux, alice_physical = divmod(left, D)
        bob_first, spectators = divmod(packed, 8**(N - 1))
        bob_aux, bob_physical = divmod(bob_first, D)
        if (alice_aux, bob_aux) == (0, 1):
            sign = 1.0
        elif (alice_aux, bob_aux) == (1, 0):
            sign = -1.0
        else:
            continue
        rows.append(16 * spectators + D * alice_physical + bob_physical)
        cols.append(int(col))
        values.append(sign * value)
    return sp.csr_matrix((values, (rows, cols)),
                         shape=(16 * 8**(N - 1), basis.shape[1]))


def prepare_block(spin):
    basis, descriptors = make_basis(spin)
    residual = raising_residual(basis)
    if residual > 1e-11:
        raise ArithmeticError("main highest-weight raising control failed")
    gram = (basis.T @ basis).toarray()
    minimum_gram = float(np.linalg.eigvalsh(gram)[0])
    if minimum_gram <= 1e-10:
        raise ArithmeticError("highest-weight Gram is not numerically positive definite")
    contraction = contraction_map(basis)
    physical_slices = [contraction[p::16, :].tocsc() for p in range(16)]
    rows, cols, values = [], [], []
    size = basis.shape[1]
    for index, (p, q) in enumerate(PAIRS):
        check_clock()
        coefficient = physical_slices[p].T @ physical_slices[q]
        if p != q:
            coefficient = coefficient + coefficient.T
        coefficient = coefficient.tocoo()
        rows.append(coefficient.row * size + coefficient.col)
        cols.append(np.full(coefficient.nnz, index, dtype=np.int64))
        values.append(coefficient.data)
    linear = sp.csc_matrix((np.concatenate(values),
                            (np.concatenate(rows), np.concatenate(cols))),
                           shape=(size * size, len(PAIRS)))
    identity_lift = (contraction.T @ contraction).toarray()
    return {"basis": basis, "descriptors": descriptors, "gram": gram,
            "identity_lift": identity_lift, "linear": linear, "size": size,
            "raising_residual": residual, "minimum_gram": minimum_gram}


def vectorize_witness(witness):
    return np.array([witness[p, q] for p, q in PAIRS], dtype=float)


def evaluate_blocks(blocks, witness, mu, *, singlet_scale=1.0, trace_factor=2.0):
    theta = vectorize_witness(witness)
    result = {}
    for spin, block in blocks.items():
        size = block["size"]
        matrix = singlet_scale * np.asarray(block["linear"] @ theta).reshape(size, size)
        matrix += mu * (block["gram"] -
                        trace_factor * singlet_scale * block["identity_lift"])
        if np.max(np.abs(matrix - matrix.T)) > 1e-9:
            raise ArithmeticError("main affine block lost symmetry")
        result[spin] = (matrix + matrix.T) / 2
    return result


def generalized_minima(matrices, blocks):
    result = {}
    for spin, matrix in matrices.items():
        check_clock()
        result[spin] = float(la.eigh(matrix, blocks[spin]["gram"],
                                   subset_by_index=[0, 0], eigvals_only=True,
                                   check_finite=True, driver="gvx")[0])
    return result


def compare_definition(matrices, checker, witness, mu, **options):
    raw = checker.blocks(witness, mu, **options)
    differences = {}
    for spin, matrix in matrices.items():
        difference = float(np.max(np.abs(matrix - raw[spin])))
        scale = 1 + float(np.max(np.abs(raw[spin])))
        if difference > 1e-9 * scale:
            raise ArithmeticError("independent full raw-tensor block comparison failed")
        differences[spin] = difference
    return differences


def fixed_controls(blocks, checker):
    omega4 = np.eye(4).reshape(16)
    projector4 = np.outer(omega4, omega4)
    y_control = (31 * np.eye(16) - 8 * projector4) / 29
    mu_control = 4 / 29
    positive = evaluate_blocks(blocks, y_control, mu_control)
    minima = generalized_minima(positive, blocks)
    margin = 28 / 49387
    if min(minima.values()) < margin - 1e-8:
        raise ArithmeticError("exact positive-control PSD-margin calibration failed")
    objective = float(omega4 @ y_control @ omega4 / 4)
    if abs(objective + 1 / 29) > 1e-12:
        raise ArithmeticError("known-SN4 control objective differs from -1/29")
    raw_differences = compare_definition(positive, checker, y_control, mu_control)
    omega2 = np.zeros(16)
    omega2[0] = omega2[5] = 1
    y_mutant = (15 / 14) * np.eye(16) - (4 / 7) * np.outer(omega2, omega2)
    if abs(float(omega2 @ y_mutant @ omega2 / 2) + 1 / 14) > 1e-12:
        raise ArithmeticError("wrong-normalization rank2 witness control is malformed")
    mutants = {}
    for label, mu, options in (
        ("wrong_trace_factor1", 1.0, {"trace_factor": 1.0}),
        ("wrong_normalized_singlet", 0.5, {"singlet_scale": 0.5}),
    ):
        mutant = evaluate_blocks(blocks, y_mutant, mu, **options)
        mutant_minima = generalized_minima(mutant, blocks)
        if min(mutant_minima.values()) < -1e-8:
            raise ArithmeticError("fixed wrong-normalization positive mutant control failed")
        correct = evaluate_blocks(blocks, y_mutant, mu)
        correct_minima = generalized_minima(correct, blocks)
        if min(correct_minima.values()) >= -1e-8:
            raise ArithmeticError("correct normalization failed to reject false rank2 witness")
        mutants[label] = {"wrong_cone_minima": mutant_minima,
                          "correct_cone_minima": correct_minima,
                          "independent_differences": compare_definition(
                              mutant, checker, y_mutant, mu, **options)}
    gram_differences = {spin: float(np.max(np.abs(block["gram"] - np.eye(block["size"]))))
                        for spin, block in blocks.items()}
    if min(gram_differences.values()) <= 1e-3:
        raise ArithmeticError("basis unexpectedly orthonormal: wrong-Gram control needs review")
    return {"fixed_positive_objective": objective, "positive_minima": minima,
            "proved_gram_scaled_margin": margin, "raw_definition_differences": raw_differences,
            "wrong_normalization_controls": mutants,
            "nonidentity_gram_differences": gram_differences}


def density_from_packet(packet):
    result = np.zeros((16, 16), dtype=np.int64)
    for item in packet["vectors"]:
        vector = np.zeros(16, dtype=np.int64)
        for index, coefficient in item["entries"]:
            vector[index] = coefficient
        result += item["weight"] * np.outer(vector, vector)
    if int(np.trace(result)) != 49:
        raise ArithmeticError("main target trace differs from49")
    return result.astype(float) / 49


def solve_once(blocks, density, checker):
    check_clock()
    remaining = DEADLINE - time.monotonic()
    if remaining < 25:
        raise ControlledStop("insufficient internal deadline for a new frozen solve")
    theta = cp.Variable(len(PAIRS))
    mu = cp.Variable(nonneg=True)
    trace_vector = np.array([1.0 if p == q else 0.0 for p, q in PAIRS])
    constraints = [trace_vector @ theta == 16, mu <= 1]
    for block in blocks.values():
        size = block["size"]
        affine = cp.reshape(block["linear"] @ theta, (size, size), order="C")
        affine += mu * (block["gram"] - 2 * block["identity_lift"])
        constraints.append(affine >> 0)
    objective_vector = np.array([density[p, q] * (1 if p == q else 2)
                                 for p, q in PAIRS])
    problem = cp.Problem(cp.Minimize(objective_vector @ theta), constraints)
    limit = min(60.0, remaining - 20)
    before = time.monotonic()
    value = problem.solve(solver=cp.CLARABEL, verbose=False, warm_start=False,
                          max_iter=120, time_limit=limit, max_threads=1,
                          direct_solve_method="qdldl", chordal_decomposition_enable=False,
                          tol_gap_abs=1e-8, tol_gap_rel=1e-8, tol_feas=1e-8)
    check_clock()
    if problem.status != cp.OPTIMAL:
        raise ControlledStop(f"solver status {problem.status}; no retry or fallback")
    if value is None or theta.value is None or mu.value is None:
        raise ArithmeticError("solver returned no finite certificate values")
    objective_value = float(value)
    if not np.isfinite(objective_value):
        raise ArithmeticError("solver returned a nonfinite objective value")
    numbers = np.asarray(theta.value, dtype=float)
    parameter = float(mu.value)
    if not np.isfinite(numbers).all() or not np.isfinite(parameter):
        raise ArithmeticError("solver returned nonfinite certificate values")
    witness = np.zeros((16, 16))
    for number, (p, q) in zip(numbers, PAIRS):
        witness[p, q] = witness[q, p] = number
    matrices = evaluate_blocks(blocks, witness, parameter)
    minima = generalized_minima(matrices, blocks)
    differences = compare_definition(matrices, checker, witness, parameter)
    trace_error = abs(float(np.trace(witness)) - 16)
    direct_objective = float(np.sum(witness * density))
    if not np.isfinite(direct_objective):
        raise ArithmeticError("reconstructed physical objective is nonfinite")
    if not np.isfinite(trace_error) or trace_error > 1e-6 or not -1e-7 <= parameter <= 1 + 1e-7:
        raise ArithmeticError("returned candidate violates frozen scalar/trace constraints")
    if min(minima.values()) < -1e-6:
        raise ArithmeticError("returned candidate lifted-block residual is too negative")
    if abs(direct_objective - objective_value) > 1e-6:
        raise ArithmeticError("solver objective differs from reconstructed physical trace")
    return {"solver_status": problem.status, "objective": direct_objective,
            "mu": parameter, "trace_error": trace_error, "lifted_minima": minima,
            "raw_definition_differences": differences, "elapsed_seconds": time.monotonic() - before,
            "solver_time_limit": limit, "witness": witness.tolist()}


def main():
    global DEADLINE, np, sp, la, cp
    parser = argparse.ArgumentParser()
    parser.add_argument("--go", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--seconds", required=True, type=float)
    args = parser.parse_args()
    if not 0 < args.seconds <= 600:
        parser.error("seconds must lie in (0,600]")
    admission = validate_admission(args)
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    start = time.monotonic()
    DEADLINE = start + admission["seconds"]
    receipt = {key: value for key, value in admission.items()
               if key not in ("go", "checker_path")}
    receipt.update({"name": NAME, "status": "INITIALIZING",
                    "scientific_scope": "one normalized-N4 candidate screen; not a P44 proof",
                    "float_boundary": "No exact PSD reconstruction or formal acceptance is performed",
                    "phases": []})
    output_created = False
    exit_code = 0
    try:
        check_clock()
        os.mkdir(args.output)
        output_created = True
        receipt.update({"status": "RUNNING", "observed_start": observed_clock(),
                        "pid": os.getpid(), "pgid": os.getpgrp(), "argv": sys.argv})
        write_json_new(args.output / "run-start.json", receipt)
        check_clock()
        import numpy as np
        import scipy.sparse as sp
        import scipy.linalg as la
        import cvxpy as cp
        check_clock()
        packet = json.loads(args.input.read_text())
        spec = importlib.util.spec_from_file_location("p44_n4_independent_checker",
                                                       admission["checker_path"])
        if spec is None or spec.loader is None:
            raise ImportError("cannot load the pinned independent checker")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        receipt["exact_input_controls"] = module.exact_input_check(packet, check_clock)
        density = density_from_packet(packet)
        blocks = {spin: prepare_block(spin) for spin in ("J3half", "J1half")}
        checker = module.DefinitionChecker(check_clock)
        basis_checks = {}
        for spin, block in blocks.items():
            difference = block["basis"] - checker.bases[spin]
            error = float(np.max(np.abs(difference.data))) if difference.nnz else 0.0
            if error > 1e-12:
                raise ArithmeticError("independently generated bases disagree")
            basis_checks[spin] = {"size": block["size"], "difference": error,
                                  "raising_residual": block["raising_residual"],
                                  "minimum_gram": block["minimum_gram"],
                                  "linear_map_nonzeros": int(block["linear"].nnz)}
        receipt["basis_controls"] = basis_checks
        write_json_new(args.output / "basis-descriptors.json",
                       {spin: block["descriptors"] for spin, block in blocks.items()})
        receipt["fixed_controls"] = fixed_controls(blocks, checker)
        receipt["phases"].append({"phase": "fixed_controls_complete", "observed": observed_clock()})
        write_json_new(args.output / "fixed-controls.json", receipt["fixed_controls"])
        separable = np.zeros((16, 16))
        separable[0, 0] = 1
        receipt["separable_control"] = solve_once(blocks, separable, checker)
        write_json_new(args.output / "separable-control.json", receipt["separable_control"])
        if receipt["separable_control"]["objective"] < -1e-7:
            raise ArithmeticError("separable control falsely has a negative2-block-positive witness")
        receipt["phases"].append({"phase": "separable_control_complete", "observed": observed_clock()})
        receipt["target"] = solve_once(blocks, density, checker)
        write_json_new(args.output / "target-candidate.json", receipt["target"])
        negative = receipt["target"]["objective"] < -1e-7
        receipt["status"] = ("FLOAT_NEGATIVE_CANDIDATE_ONLY" if negative else
                             "NO_NEGATIVE_FOUND_IN_FROZEN_CONE")
        receipt["interpretation"] = (
            "Requires separately admitted exact PSD reconstruction and full proof before acceptance"
            if negative else
            "Only this finite certificate and single input were screened; not SN2, UNSAT or a P44 no-go")
    except ControlledStop as error:
        receipt["status"] = "UNKNOWN_INTERRUPTED_OR_INCOMPLETE"
        receipt["stop_reason"] = str(error)
        exit_code = 75
    except Exception as error:
        receipt["status"] = "ERROR_NO_SCIENTIFIC_VERDICT"
        receipt["error"] = f"{type(error).__name__}: {error}"
        exit_code = 2
    finally:
        # Nonthrowing handlers stay installed: repeated requests cannot raise out
        # of settlement. This is a snapshot, not a claim about later signals.
        stop_snapshot = STOP_STATE
        if stop_snapshot is not None and exit_code == 0:
            receipt["status"] = "UNKNOWN_INTERRUPTED_OR_INCOMPLETE"
            receipt["stop_reason"] = f"received first stop signal {stop_snapshot[0]}"
            exit_code = 75
        receipt["stop_state_at_settlement_snapshot"] = (
            None if stop_snapshot is None else
            {"first_signal": stop_snapshot[0], "requests": stop_snapshot[1]})
        receipt["output_created_exclusively"] = output_created
        settlement_written = False
        try:
            receipt["elapsed_seconds"] = time.monotonic() - start
            receipt["observed_settlement"] = observed_clock()
            receipt["peak_rss_bytes"] = peak_rss_bytes()
            receipt["process_children"] = "none created; no subprocess or service API used"
            if output_created:
                write_json_new(args.output / "receipt.json", receipt)
                settlement_written = True
        except Exception as error:
            exit_code = 2
            print(json.dumps({"status": "ERROR_SETTLEMENT_NOT_WRITTEN",
                              "output": str(args.output),
                              "error": f"{type(error).__name__}: {error}"}),
                  file=sys.stderr, flush=True)
        late_stop = STOP_STATE is not None and stop_snapshot is None
        if late_stop and exit_code == 0:
            exit_code = 75
        print(json.dumps({"status": receipt["status"], "output": str(args.output),
                          "settlement_written": settlement_written,
                          "late_stop_after_snapshot": late_stop,
                          "elapsed_seconds": receipt.get("elapsed_seconds"),
                          "peak_rss_bytes": receipt.get("peak_rss_bytes")}))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
