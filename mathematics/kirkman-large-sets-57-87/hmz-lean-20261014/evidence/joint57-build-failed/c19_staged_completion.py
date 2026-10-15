#!/usr/bin/env python3
"""Pair-first completion of a frozen C19-invariant 17-KTS packing.

Search: ... search --packing PATH --solver kissat|cadical|cpsat --output PREFIX
Replay: ... replay MANIFEST --output REGENERATED_MODEL

The least remaining triple-orbit is anchored in base 0 at its canonical
representative. No second base-swap symmetry breaker is imposed. A SAT pair
cover is independently checked, then both STSs receive unrestricted resolution
searches. Blocking a candidate after UNKNOWN resolution is explicitly heuristic.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time

for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_key] = "1"

from ortools.sat.python import cp_model
import ortools
import c19_search as c19
import c19_verify as independent
from search_staged import CNF

ACTIVE_PROCESS = None
ACTIVE_SOLVER = None
STOP = threading.Event()
STOP_REASON = None
CANCELLED_AT = None
TERM_REQUESTED_PROCESS = None
HELPERS = ("c19_search.py", "c19_verify.py", "search_staged.py", "search_cyclic.py", "check_lkts.py")


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def save(path, value):
    Path(path).write_text(json.dumps(value, indent=2) + "\n")


def cancel(reason):
    global STOP_REASON, CANCELLED_AT, TERM_REQUESTED_PROCESS
    if STOP_REASON is None:
        STOP_REASON = reason
    if CANCELLED_AT is None:
        CANCELLED_AT = time.monotonic()
    STOP.set()
    if ACTIVE_SOLVER is not None:
        ACTIVE_SOLVER.stop_search()
    process = ACTIVE_PROCESS
    if process is not None and process is not TERM_REQUESTED_PROCESS and process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        TERM_REQUESTED_PROCESS = process


def watch(deadline, stop_file, finished):
    while not finished.wait(0.2):
        if STOP.is_set():
            cancel(STOP_REASON or "CANCELLED")
            continue
        if stop_file and stop_file.exists():
            cancel("PEER_VERIFIED_TARGET")
        elif time.monotonic() >= deadline:
            cancel("WALL_LIMIT")


def build_encoding(packing):
    data, orbit_ids = c19.inventory()
    assert len(packing) == 17
    used = set()
    for candidate in packing:
        actual = {orbit_ids[key] for key in independent.check_fixed(candidate)}
        assert actual == set(candidate["orbit_ids"]) and len(actual) == 28
        assert not used.intersection(actual)
        used.update(actual)
    remaining = sorted(set(range(1540)) - used)
    assert len(remaining) == 1064
    pairs = list(itertools.combinations(range(57), 2))
    pair_ids = {pair: i for i, pair in enumerate(pairs)}
    columns = [[] for _ in range(1064 + 2 * len(pairs))]
    rows = []
    for orbit_column, oid in enumerate(remaining):
        representative = data["triple_orbits"][oid]["representative"]
        for shift in range(19):
            block = c19.translate(representative, shift)
            for base in range(2):
                row_id = len(rows) + 1
                rows.append([base, oid, shift, list(block)])
                columns[orbit_column].append(row_id)
                for pair in itertools.combinations(block, 2):
                    columns[1064 + base * len(pairs) + pair_ids[pair]].append(row_id)
    assert len(rows) == 40432 and len(columns) == 4256
    assert all(len(column) == 38 for column in columns)
    assert rows[0][0:3] == [0, remaining[0], 0]
    columns.append([1])  # Swap bases, then independently translate base 0.
    return {"v": 57, "rows": rows, "columns": columns, "remaining_orbit_ids": remaining,
            "anchor": {"primary_literal": 1, "base": 0, "orbit_id": remaining[0], "shift": 0},
            "symmetry": "least remaining orbit belongs to base0 and uses its canonical representative; no 0,1-third-point ordering"}


def pair_model(encoding, blocked, kind):
    if kind == "modular":
        return modular_pair_model(encoding, blocked)
    model = cp_model.CpModel()
    variables = [model.new_bool_var(f"x{i+1}") for i in range(len(encoding["rows"]))]
    for column in encoding["columns"]:
        model.add_exactly_one(variables[index - 1] for index in column)
    for selected in blocked:
        model.add_bool_or(variables[index - 1].Not() for index in selected)
    return model, variables


def modular_pair_model(encoding, blocked):
    model = cp_model.CpModel()
    pair_keys = sorted({independent.key(pair) for pair in itertools.combinations(range(57), 2)})
    pair_ids = {pair: index for index, pair in enumerate(pair_keys)}
    columns = [[] for _ in pair_keys]
    colors = [model.new_bool_var(f"color{i}") for i in range(1064)]
    shifts = [model.new_int_var(0, 18, f"shift{i}") for i in range(1064)]
    for index in range(1064):
        representative = tuple(encoding["rows"][38 * index][3])
        incidences = []
        for j, pair in enumerate(itertools.combinations(representative, 2)):
            pair_key = independent.key(pair)
            offsets = [t for t in range(19) if independent.shifted(pair_key, t) == pair]
            assert len(offsets) == 1
            offset = offsets[0]
            incidences.append((pair_key, offset))
            if offset:
                translated = model.new_int_var(0, 18, f"mod{index}_{j}")
                model.add_modulo_equality(translated, shifts[index] + offset, 19)
            else:
                translated = shifts[index]
            value = model.new_int_var(0, 37, f"value{index}_{j}")
            model.add(value == 19 * colors[index] + translated)
            columns[pair_ids[pair_key]].append(value)
        # Exhaustively bind modular coordinates to all native placement rows.
        # AP pairs in the same pair-orbit remain separate offset incidences.
        for shift in range(19):
            block = tuple(encoding["rows"][38 * index + 2 * shift][3])
            assert Counter(independent.shifted(pair, (shift + offset) % 19)
                           for pair, offset in incidences) == Counter(itertools.combinations(block, 2))
    assert len(columns) == 84 and all(len(column) == 38 for column in columns)
    for column in columns:
        model.add_all_different(column)
    model.add(colors[0] == 0)
    model.add(shifts[0] == 0)
    decision_variables = [variable for pair in zip(colors, shifts) for variable in pair]
    for selected in blocked:
        assignment = [None] * 2128
        for literal in selected:
            index, position = divmod(literal - 1, 38)
            shift, color = divmod(position, 2)
            assignment[2 * index:2 * index + 2] = [color, shift]
        assert None not in assignment
        model.add_forbidden_assignments(decision_variables, [assignment])
    return model, (colors, shifts)


def selected_from_cp(solver, variables, kind):
    if solver is None:
        return []
    if kind == "modular":
        colors, shifts = variables
        return [38 * index + 2 * solver.value(shifts[index]) + solver.value(colors[index]) + 1
                for index in range(1064)]
    return [index + 1 for index, value in enumerate(solver.response_proto.solution) if value]


def validate_pair_cover(encoding, selected):
    assert len(selected) == 1064 and len(set(selected)) == 1064 and 1 in selected
    bases = [[], []]
    for index in selected:
        assert 1 <= index <= len(encoding["rows"])
        base, _, _, block = encoding["rows"][index - 1]
        bases[base].append(tuple(block))
    all_orbits = set()
    for blocks in bases:
        assert len(blocks) == 532 and len(set(blocks)) == 532
        assert Counter(pair for block in blocks for pair in itertools.combinations(block, 2)) == Counter(itertools.combinations(range(57), 2))
        # Full 19-element canonicalization is independent of model construction.
        orbit_keys = {independent.key(block) for block in blocks}
        assert len(orbit_keys) == 532 and not all_orbits.intersection(orbit_keys)
        all_orbits.update(orbit_keys)
    expected = {independent.key(row[3]) for row in encoding["rows"]}
    assert all_orbits == expected
    return [sorted(blocks) for blocks in bases]


def cp_solve(model, seconds, threads, seed, log_path):
    global ACTIVE_SOLVER
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max(0.001, seconds)
    solver.parameters.num_search_workers = threads
    solver.parameters.random_seed = seed
    solver.parameters.randomize_search = True
    solver.parameters.log_search_progress = True
    solver.parameters.log_to_stdout = False
    parameters = str(solver.parameters)
    ACTIVE_SOLVER = solver
    try:
        with Path(log_path).open("w") as stream:
            solver.log_callback = lambda text: stream.write(text + "\n")
            if STOP.is_set():
                return None, {"status": "UNKNOWN", "solver": "CP-SAT", "cap_seconds": seconds,
                              "wall_seconds": 0, "threads": threads, "seed": seed,
                              "parameters": parameters, "log_path": str(log_path),
                              "stop_reason": STOP_REASON}
            status = solver.solve(model)
    finally:
        ACTIVE_SOLVER = None
    info = {"status": solver.status_name(status), "solver": "CP-SAT", "cap_seconds": seconds,
            "wall_seconds": solver.wall_time, "threads": threads, "seed": seed,
            "parameters": parameters, "branches": solver.num_branches, "conflicts": solver.num_conflicts,
            "log_path": str(log_path)}
    return solver if status in (cp_model.FEASIBLE, cp_model.OPTIMAL) else None, info


def wait_native(process, seconds, grace_seconds=30):
    """Reap normally, or retain an unresponsive child after SIGTERM grace."""
    call_deadline = time.monotonic() + seconds + 5
    while True:
        if STOP.is_set():
            cancel(STOP_REASON or "CANCELLED")
            limit = CANCELLED_AT + grace_seconds
        else:
            limit = call_deadline
        remaining = limit - time.monotonic()
        if remaining <= 0:
            if process.poll() is not None:
                return process.wait()
            if STOP.is_set():
                return None
            cancel("NATIVE_EXTERNAL_WALL_LIMIT")
            continue
        try:
            return process.wait(timeout=min(0.25, remaining))
        except subprocess.TimeoutExpired:
            pass


def native_solve(path, solver_name, config, seed, seconds, primary, log_path):
    global ACTIVE_PROCESS
    cap = max(1, math.ceil(seconds))
    if solver_name == "kissat":
        command = [solver_name, f"--{config}", f"--seed={seed}", f"--time={cap}", str(path)]
    else:
        command = [solver_name, f"--{config}", f"--seed={seed}", "--shuffle=true", "--shufflerandom=true", "-t", str(cap), str(path)]
    started = time.monotonic()
    with Path(log_path).open("wb") as stream:
        ACTIVE_PROCESS = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stream,
                                          stderr=subprocess.STDOUT, start_new_session=True)
        returncode = wait_native(ACTIVE_PROCESS, seconds)
        if returncode is None:
            return [], {"status": "UNRESPONSIVE_CHILD", "solver": solver_name, "config": config,
                        "seed": seed, "threads": 1, "cap_seconds": seconds,
                        "native_rounded_cap_seconds": cap, "wall_seconds": time.monotonic() - started,
                        "command": command, "exit_code": None, "unresponsive_child_pid": ACTIVE_PROCESS.pid,
                        "termination_grace_seconds": 30, "log_path": str(log_path),
                        "log_mutable_while_child_alive": True,
                        "cleanup_complete": False, "approval_needed": "SIGTERM-unresponsive child; no force kill attempted"}
        ACTIVE_PROCESS = None  # wait_native returned only after reaping.
    selected, status = [], "UNKNOWN"
    with Path(log_path).open() as stream:
        for line in stream:
            if line.startswith("v "):
                selected.extend(value for value in map(int, line[2:].split()) if 0 < value <= primary)
            elif line.startswith("s SATISFIABLE"):
                status = "SAT"
            elif line.startswith("s UNSATISFIABLE"):
                status = "UNSAT"
    if returncode not in (0, 10, 20, -signal.SIGTERM, 128 + signal.SIGTERM):
        status = "ERROR"
    if (status == "SAT" and returncode != 10) or (status == "UNSAT" and returncode != 20):
        status = "ERROR"
    info = {"status": status, "solver": solver_name, "config": config, "seed": seed,
            "threads": 1, "cap_seconds": seconds, "native_rounded_cap_seconds": cap,
            "wall_seconds": time.monotonic() - started, "command": command,
            "exit_code": returncode, "cleanup_complete": True,
            "log_path": str(log_path), "log_sha256": digest(log_path)}
    return sorted(set(selected)), info


def resolve(blocks, seconds, threads, seed, prefix):
    anchors = sorted(block for block in blocks if 0 in block)
    assert len(anchors) == 28
    anchor_class = {block: c for c, block in enumerate(anchors)}
    anchor_points = [set(block) for block in anchors]
    model = cp_model.CpModel()
    rows = []
    block_columns = [[] for _ in blocks]
    point_columns = [[[] for _ in range(57)] for _ in range(28)]
    for bi, block in enumerate(blocks):
        if block in anchor_class:
            allowed = (anchor_class[block],)
        else:
            allowed = [c for c in range(28) if not anchor_points[c].intersection(block)]
        for c in allowed:
            variable = model.new_bool_var(f"b{bi}c{c}")
            rows.append((bi, c))
            block_columns[bi].append(variable)
            for point in block:
                point_columns[c][point].append(variable)
    for column in block_columns:
        model.add_exactly_one(column)
    for parallel in point_columns:
        for column in parallel:
            model.add_exactly_one(column)
    text = str(model.proto).encode()
    model_path = Path(str(prefix) + ".pbtxt")
    model_path.write_bytes(text)
    solver, info = cp_solve(model, seconds, threads, seed, str(prefix) + ".log")
    info.update(instance_sha256=hashlib.sha256(text).hexdigest(), model_path=str(model_path),
                rows=len(rows), symmetry="classes labeled by the 28 blocks through point0; otherwise unrestricted")
    if info["status"] == "MODEL_INVALID":
        raise RuntimeError("invalid unrestricted resolution model")
    if solver is None:
        return None, info
    classes = [[] for _ in range(28)]
    for index, selected in enumerate(solver.response_proto.solution):
        if selected:
            bi, c = rows[index]
            classes[c].append(blocks[bi])
    assert c19.check_kts(classes) == set(blocks)
    save(str(prefix) + ".classes.json", classes)
    info["expanded_KTS_check"] = "PASS"
    return classes, info


def load_blocked(manifest, encoding):
    blocked = []
    for item in manifest["blocked_candidates"]:
        assert digest(item["path"]) == item["sha256"]
        candidate = json.loads(Path(item["path"]).read_text())
        selected = candidate["selected_primary_literals"]
        validate_pair_cover(encoding, selected)
        blocked.append(selected)
    return blocked


def replay(args):
    manifest = json.loads(args.manifest.read_text())
    assert digest(manifest["packing_path"]) == manifest["packing_sha256"]
    packing = json.loads(Path(manifest["packing_path"]).read_text())
    encoding = build_encoding(packing)
    assert hashlib.sha256(encoded(encoding)).hexdigest() == manifest["encoding_sha256"]
    blocked = load_blocked(manifest, encoding)
    if args.output.exists():
        raise ValueError("replay output already exists")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if manifest["format"] == "cnf":
        cnf = CNF(args.output, len(encoding["rows"]), encoding["columns"])
        for selected in blocked:
            cnf.block(selected)
    else:
        model, _ = pair_model(encoding, blocked, manifest["cp_encoding"])
        args.output.write_text(str(model.proto))
    actual = digest(args.output)
    assert actual == manifest["instance_sha256"], (actual, manifest["instance_sha256"])
    print(json.dumps({"status": "PASS", "instance_sha256": actual, "primary_variables": 40432,
                      "blocked_candidates": len(blocked), "manifest_sha256": digest(args.manifest),
                      "replay_source_sha256": digest(__file__),
                      "scope": "reconstructed model bytes; recorded source_hashes are not authenticated and frozen sources are not loaded"}, indent=2))


def search(args):
    global STOP_REASON, ACTIVE_PROCESS
    started = time.monotonic()
    deadline = started + args.seconds
    prefix = args.output
    receipt_path = Path(str(prefix) + ".json")
    data_dir = Path(str(prefix) + "-data")
    if receipt_path.exists() or data_dir.exists():
        raise ValueError("output exists; choose a fresh prefix")
    data_dir.mkdir(parents=True)
    source_dir = data_dir / "source"
    source_dir.mkdir()
    sources = {}
    for name in (Path(__file__).name,) + HELPERS:
        original = Path(__file__).with_name(name)
        target = source_dir / name
        target.write_bytes(original.read_bytes())
        sources[name] = digest(target)
    packing_path = data_dir / "frozen-packing.json"
    packing_path.write_bytes(args.packing.read_bytes())
    packing = json.loads(packing_path.read_text())
    receipt = {"status": "RUNNING", "v": 57, "model": "frozen17 C19 KTSs; two free STS pair covers then unrestricted resolutions",
               "command": sys.argv, "source_sha256": sources[Path(__file__).name], "source_hashes": sources,
               "packing_path": str(packing_path), "packing_sha256": digest(packing_path),
               "parameters": {key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
               "python": platform.python_version(), "ortools_version": ortools.__version__,
               "wall_clock_cap_seconds": args.seconds, "thread_cap": args.threads,
               "restrictions": {"fixed_packing_frozen": True, "anchor": "least remaining orbit in base0 at canonical representative",
                                "no_other_base_swap_breaker": True, "resolution": "unrestricted for each candidate STS",
                                "blocking_after_UNKNOWN_resolution": "heuristic exclusion only; never a nonexistence proof"},
               "phases": [], "heuristically_blocked_candidates": 0}
    if args.solver != "cpsat":
        executable = shutil.which(args.solver)
        if executable is None:
            raise ValueError(f"missing native solver {args.solver}")
        receipt.update(native_solver_path=executable, native_solver_sha256=digest(executable),
                       native_solver_version=subprocess.check_output([args.solver, "--version"], text=True).strip())
    save(receipt_path, receipt)
    finished = threading.Event()
    watcher = threading.Thread(target=watch, args=(deadline, args.stop_file, finished), daemon=True)
    signal.signal(signal.SIGTERM, lambda signum, frame: cancel("SIGTERM"))
    signal.signal(signal.SIGINT, lambda signum, frame: cancel("SIGINT"))
    watcher.start()
    blocked, blocked_files = [], []
    try:
        encoding = build_encoding(packing)
        encoding_path = data_dir / "encoding.json"
        encoding_path.write_bytes(encoded(encoding))
        encoding_hash = digest(encoding_path)
        receipt.update(encoding_sha256=encoding_hash, encoding_path=str(encoding_path),
                       primary_variables=40432, exact_cover_columns=len(encoding["columns"]),
                       input_validation="PASS", build_seconds=time.monotonic() - started)
        save(receipt_path, receipt)
        attempt = 0
        while not STOP.is_set() and time.monotonic() < deadline:
            stage_start = time.monotonic()
            stage_prefix = data_dir / f"paircover-{attempt:04d}"
            instance_path = Path(str(stage_prefix) + (".pbtxt" if args.solver == "cpsat" else ".cnf"))
            if args.solver == "cpsat":
                model, variables = pair_model(encoding, blocked, args.cp_encoding)
                instance_path.write_text(str(model.proto))
                dimensions = {"variables": len(model.proto.variables), "constraints": len(model.proto.constraints),
                              "cp_encoding": args.cp_encoding, "primary_decisions": 2128 if args.cp_encoding == "modular" else 40432}
            else:
                cnf = CNF(instance_path, len(encoding["rows"]), encoding["columns"])
                for selected in blocked:
                    cnf.block(selected)
                dimensions = {"variables": cnf.variables, "clauses": cnf.clauses}
            manifest = {"format": "pbtxt" if args.solver == "cpsat" else "cnf",
                        "instance_sha256": digest(instance_path), "encoding_sha256": encoding_hash,
                        "packing_path": str(packing_path), "packing_sha256": receipt["packing_sha256"],
                        "blocked_candidates": list(blocked_files), "source_hashes": sources,
                        "anchor": encoding["anchor"], **dimensions}
            manifest_path = Path(str(stage_prefix) + ".manifest.json")
            save(manifest_path, manifest)
            build_seconds = time.monotonic() - stage_start
            cap = min(args.paircover_seconds, max(0.001, deadline - time.monotonic()))
            seed = (args.seed + attempt * 100003) % 2000000000
            if STOP.is_set():
                break
            if args.solver == "cpsat":
                solver, info = cp_solve(model, cap, args.threads, seed, str(stage_prefix) + ".log")
                selected = selected_from_cp(solver, variables, args.cp_encoding)
            else:
                selected, info = native_solve(instance_path, args.solver, args.config, seed, cap,
                                               len(encoding["rows"]), str(stage_prefix) + ".log")
            event = {"phase": "pair_cover", "attempt": attempt, "instance_sha256": manifest["instance_sha256"],
                     "manifest_path": str(manifest_path), "build_seconds": build_seconds,
                     "wall_seconds_including_build": time.monotonic() - stage_start,
                     "blocked_candidates": len(blocked), "heuristically_blocked_candidates": receipt["heuristically_blocked_candidates"],
                     **dimensions, **info}
            receipt["phases"].append(event)
            save(receipt_path, receipt)
            print(json.dumps({"phase": "pair_cover", "attempt": attempt, "status": info["status"],
                              "elapsed_seconds": time.monotonic() - started}), flush=True)
            if info["status"] == "UNRESPONSIVE_CHILD":
                receipt.update(status="STOPPED_WITH_UNRESPONSIVE_CHILD",
                               unresponsive_child_pid=info["unresponsive_child_pid"])
                break
            if info["status"] in ("ERROR", "MODEL_INVALID"):
                raise RuntimeError(f"solver error: {info}")
            if info["status"] in ("UNSAT", "INFEASIBLE"):
                receipt["status"] = "EXHAUSTED_AFTER_HEURISTIC_BLOCKS" if receipt["heuristically_blocked_candidates"] else "SOLVER_INFEASIBLE_FROZEN_PACKING"
                break
            if not selected:
                attempt += 1
                continue
            bases = validate_pair_cover(encoding, selected)
            candidate_path = Path(str(stage_prefix) + ".candidate.json")
            save(candidate_path, {"selected_primary_literals": selected, "bases": bases,
                                  "instance_sha256": manifest["instance_sha256"], "independent_STS_checks": "PASS"})
            event.update(candidate_path=str(candidate_path), candidate_sha256=digest(candidate_path), independent_STS_checks="PASS")
            classes, unresolved, refuted = [], False, False
            for base, blocks in enumerate(bases):
                if STOP.is_set() or time.monotonic() >= deadline:
                    unresolved = True
                    break
                cap = min(args.resolution_seconds, deadline - time.monotonic())
                resolution_start = time.monotonic()
                resolved, resolution_info = resolve(blocks, cap, args.threads, (seed + base + 1) % 2000000000,
                                                     str(stage_prefix) + f".resolution-{base}")
                receipt["phases"].append({"phase": "resolution", "attempt": attempt, "base": base,
                                          "candidate_sha256": digest(candidate_path),
                                          "total_stage_seconds": time.monotonic() - resolution_start, **resolution_info})
                save(receipt_path, receipt)
                if resolution_info["status"] == "INFEASIBLE":
                    refuted = True
                    break
                if resolved is None:
                    unresolved = True
                    break
                classes.append(resolved)
            if len(classes) == 2:
                certificate = Path(str(prefix) + ".txt")
                c19.write_certificate(certificate, packing, classes)
                checker = Path(__file__).with_name("check_lkts.py")
                checked = subprocess.run([sys.executable, str(checker), str(certificate)], capture_output=True, text=True)
                Path(str(prefix) + ".check.json").write_text(checked.stdout)
                if checked.returncode:
                    raise RuntimeError("independent full checker failed: " + checked.stdout + checked.stderr)
                receipt.update(status="FOUND_VERIFIED", certificate=str(certificate), certificate_sha256=digest(certificate),
                               checker_sha256=digest(checker), checker_exit_code=0)
                if args.stop_file:
                    save(args.stop_file, {"status": "FOUND_VERIFIED", "receipt": str(receipt_path),
                                          "certificate": str(certificate), "certificate_sha256": digest(certificate)})
                break
            if STOP.is_set() or time.monotonic() >= deadline:
                break
            reason = "resolution_solver_infeasible" if refuted else "resolution_unknown_heuristic"
            assert refuted or unresolved
            blocked.append(selected)
            blocked_files.append({"path": str(candidate_path), "sha256": digest(candidate_path), "reason": reason})
            if not refuted:
                receipt["heuristically_blocked_candidates"] += 1
            receipt["phases"].append({"phase": "candidate_block", "attempt": attempt, "reason": reason,
                                      "candidate_sha256": digest(candidate_path), "excluded_primary_literals": selected})
            save(receipt_path, receipt)
            attempt += 1
        if receipt["status"] == "RUNNING":
            receipt["status"] = "UNKNOWN_PEER_VERIFIED_TARGET" if STOP_REASON == "PEER_VERIFIED_TARGET" else "UNKNOWN"
    except Exception as error:
        receipt.update(status="ERROR", error=repr(error))
        raise
    finally:
        finished.set()
        watcher.join(timeout=2)
        if ACTIVE_PROCESS is not None or ACTIVE_SOLVER is not None:
            cancel("FINAL_CLEANUP")
        remaining_children = 0
        if ACTIVE_PROCESS is not None:
            if ACTIVE_PROCESS.poll() is None:
                remaining_children = 1
                receipt.update(status="STOPPED_WITH_UNRESPONSIVE_CHILD",
                               unresponsive_child_pid=ACTIVE_PROCESS.pid,
                               cleanup_complete=False,
                               approval_needed="SIGTERM-unresponsive child remains; no force kill attempted")
            else:
                ACTIVE_PROCESS.wait()
                ACTIVE_PROCESS = None
        receipt.update(total_seconds=time.monotonic() - started, stop_reason=STOP_REASON,
                       peak_self_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                       peak_child_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
                       background_children_remaining=remaining_children)
        save(receipt_path, receipt)
    print(json.dumps({"status": receipt["status"], "receipt": str(receipt_path),
                      "total_seconds": receipt["total_seconds"]}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="operation", required=True)
    run = sub.add_parser("search")
    run.add_argument("--packing", type=Path, required=True)
    run.add_argument("--solver", choices=("kissat", "cadical", "cpsat"), required=True)
    run.add_argument("--config", choices=("default", "sat", "unsat"), default="sat")
    run.add_argument("--cp-encoding", choices=("boolean", "modular"), default="modular")
    run.add_argument("--seconds", type=float, default=7200)
    run.add_argument("--paircover-seconds", type=float, default=7200)
    run.add_argument("--resolution-seconds", type=float, default=300)
    run.add_argument("--threads", type=int, default=1)
    run.add_argument("--seed", type=int, required=True)
    run.add_argument("--stop-file", type=Path)
    run.add_argument("--output", type=Path, required=True)
    again = sub.add_parser("replay")
    again.add_argument("manifest", type=Path)
    again.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.operation == "search":
        if not 1 <= args.threads <= 2 or (args.solver != "cpsat" and args.threads != 1):
            parser.error("native runners use one worker; CP-SAT uses one or two")
        if min(args.seconds, args.paircover_seconds, args.resolution_seconds) <= 0:
            parser.error("all wall caps must be positive")
        search(args)
    else:
        replay(args)


if __name__ == "__main__":
    main()
