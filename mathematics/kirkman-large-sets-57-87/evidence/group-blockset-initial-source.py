#!/usr/bin/env python3
"""Search cyclic transversal STSs with a scalar block automorphism, then resolve.

No scalar action is imposed on resolution classes. A completed resolution is
expanded by the existing cyclic writer and checked by the independent checker.
The total deadline includes model construction and all candidate resolutions.
"""
import argparse
from collections import Counter, defaultdict
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time

from search_cyclic import orbit_key, write_certificate


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_base(blocks, v, multiplier):
    n = v - 2
    pairs = Counter(p for b in blocks for p in itertools.combinations(b, 2))
    keys = [orbit_key(b, n) for b in blocks]
    image = {tuple(sorted(multiplier*x % n if x < n else x for x in b)) for b in blocks}
    expected = v*(v-1)//6
    if len(blocks) != expected or len(set(blocks)) != expected:
        raise ValueError("wrong base block count")
    if set(pairs) != set(itertools.combinations(range(v), 2)) or set(pairs.values()) != {1}:
        raise ValueError("base does not cover every pair exactly once")
    if len(set(keys)) != expected:
        raise ValueError("base is not a translation-orbit transversal")
    if image != set(blocks):
        raise ValueError("base block set is not multiplier invariant")


def resolution_model(blocks, v, cp_model):
    model = cp_model.CpModel()
    count = (v-1)//2
    colors = [model.new_int_var(0, count-1, f"c{i}") for i in range(len(blocks))]
    incident = [[] for _ in range(v)]
    for i, block in enumerate(blocks):
        for x in block:
            incident[x].append(colors[i])
    for variables in incident:
        model.add_all_different(variables)
    # A point's incident blocks use all colors. Label them in sorted block order.
    for c, variable in enumerate(incident[0]):
        model.add(variable == c)
    return model, colors


def main():
    from ortools.sat.python import cp_model
    import ortools
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--v", type=int, required=True)
    parser.add_argument("--multiplier", type=int, required=True)
    parser.add_argument("--seconds", type=float, default=7200)
    parser.add_argument("--block-seconds", type=float, default=1800)
    parser.add_argument("--resolution-seconds", type=float, default=120)
    parser.add_argument("--max-candidates", type=int, default=100)
    parser.add_argument("--threads", type=int, default=2)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    v, n, a = args.v, args.v-2, args.multiplier
    if v < 9 or v % 6 != 3 or math.gcd(a, n) != 1:
        parser.error("v>=9 is 3 mod6 and multiplier is a unit")
    if not 1 <= args.threads <= 2 or min(args.seconds, args.block_seconds, args.resolution_seconds) <= 0:
        parser.error("threads must be 1..2 and deadlines must be positive")
    if args.max_candidates < 1:
        parser.error("max-candidates must be positive")
    if args.output.with_suffix(".json").exists() or args.output.with_suffix(".log").exists():
        parser.error("output prefix already exists; preserve earlier evidence")
    started = time.monotonic()
    deadline = started + args.seconds
    triples = list(itertools.combinations(range(v), 3))
    tids = {b: i for i, b in enumerate(triples)}
    image = [tids[tuple(sorted(a*x % n if x < n else x for x in b))] for b in triples]
    all_keys = [[("pair",)+p for p in itertools.combinations(b, 2)] + [("orbit",)+orbit_key(b, n)] for b in triples]
    required = set(k for keys in all_keys for k in keys)
    model = cp_model.CpModel()
    rows = []
    columns = defaultdict(list)
    seen = set()
    discarded = 0
    for ti in range(len(triples)):
        if ti in seen:
            continue
        orbit = []
        current = ti
        while current not in seen:
            seen.add(current)
            orbit.append(current)
            current = image[current]
        if any(n in triples[i] and n+1 in triples[i] and triples[i][0] != 0 for i in orbit):
            continue
        keys = [key for i in orbit for key in all_keys[i]]
        if len(keys) != len(set(keys)):
            discarded += 1
            continue
        variable = model.new_bool_var(f"r{len(rows)}")
        rows.append((variable, orbit))
        for key in keys:
            columns[key].append(variable)
    equalities = set()
    for key in sorted(required):
        ids = tuple(var.index for var in columns[key])
        if ids not in equalities:
            model.add_exactly_one(columns[key])
            equalities.add(ids)
    source = Path(__file__).resolve()
    receipt = {
        "v": v, "n": n, "multiplier": a,
        "restrictions": ["cyclic translation development on Z_(v-2) with two individually fixed infinities",
                         "base STS is a transversal of all triple-translation orbits",
                         "base STS blocks, but NOT its resolution, are scalar-multiplier invariant",
                         "the infinity-pair block is normalized to {0,v-2,v-1}",
                         "resolution classes are freely colored; point-0 incident blocks fix class names only",
                         "previously emitted base blocksets are excluded during subsequent enumeration"],
        "source_sha256": digest(source), "helper_sha256": digest(source.with_name("search_cyclic.py")),
        "checker_sha256": digest(source.with_name("check_lkts.py")),
        "initial_instance_sha256": hashlib.sha256(str(model.proto).encode()).hexdigest(),
        "rows": len(rows), "columns": len(required), "distinct_equalities": len(equalities),
        "discarded_colliding_orbits": discarded, "empty_columns": sum(not columns[k] for k in required),
        "threads": args.threads, "seed": args.seed, "wall_clock_cap_seconds": args.seconds,
        "block_call_cap_seconds": args.block_seconds, "resolution_call_cap_seconds": args.resolution_seconds,
        "max_candidates": args.max_candidates, "command": sys.argv,
        "python": platform.python_version(), "ortools_version": ortools.__version__,
        "build_seconds": time.monotonic()-started, "calls": [], "candidates": [], "result": "RUNNING"
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    receipt_path = args.output.with_suffix(".json")
    def save():
        receipt["total_seconds"] = time.monotonic()-started
        receipt_path.write_text(json.dumps(receipt, indent=2))
    save()
    with args.output.with_suffix(".log").open("w") as log:
        def solve(instance, stage, cap, candidate):
            remaining = deadline-time.monotonic()
            if remaining <= 0:
                return None, None
            solver = cp_model.CpSolver()
            solver.parameters.max_time_in_seconds = min(cap, remaining)
            solver.parameters.num_search_workers = args.threads
            solver.parameters.random_seed = args.seed+candidate
            solver.parameters.log_search_progress = True
            solver.parameters.log_to_stdout = False
            solver.parameters.max_memory_in_mb = 3500
            solver.log_callback = lambda text: log.write(text+"\n")
            log.write(f"\nSTAGE {stage} CANDIDATE {candidate}\n")
            call = {"stage": stage, "candidate": candidate,
                    "instance_sha256": hashlib.sha256(str(instance.proto).encode()).hexdigest(),
                    "parameters": str(solver.parameters), "limit_seconds": solver.parameters.max_time_in_seconds}
            status = solver.solve(instance)
            call.update(status=solver.status_name(status), wall_seconds=solver.wall_time,
                        branches=solver.num_branches, conflicts=solver.num_conflicts)
            receipt["calls"].append(call)
            log.flush()
            save()
            return status, solver
        for candidate in range(args.max_candidates):
            status, solver = solve(model, "blockset", args.block_seconds, candidate)
            if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                receipt["result"] = "DEADLINE" if status is None else "BLOCKSET_"+solver.status_name(status)
                break
            selected = [variable for variable, _ in rows if solver.value(variable)]
            blocks = sorted(triples[i] for variable, orbit in rows if solver.value(variable) for i in orbit)
            validate_base(blocks, v, a)
            candidate_path = args.output.parent / f"{args.output.name}-candidate-{candidate:03}.json"
            candidate_path.write_text(json.dumps({"v": v, "multiplier": a, "blocks": blocks}, separators=(",", ":")))
            item = {"candidate": candidate, "path": str(candidate_path), "sha256": digest(candidate_path),
                    "base_validation": "pair-cover, orbit-transversal, multiplier-block-invariance passed"}
            receipt["candidates"].append(item)
            coloring, colors = resolution_model(blocks, v, cp_model)
            rstatus, rsolver = solve(coloring, "unrestricted_resolution", args.resolution_seconds, candidate)
            item["resolution_status"] = "DEADLINE" if rstatus is None else rsolver.status_name(rstatus)
            if rstatus in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                base = [[] for _ in range((v-1)//2)]
                for block, color in zip(blocks, colors):
                    base[rsolver.value(color)].append(block)
                certificate = args.output.with_suffix(".txt")
                write_certificate(certificate, v, base)
                checked = subprocess.run([sys.executable, str(source.with_name("check_lkts.py")), str(certificate)], capture_output=True, text=True)
                args.output.with_suffix(".check.json").write_text(checked.stdout)
                receipt.update(result="CERTIFIED" if checked.returncode == 0 else "CHECKER_REJECTED",
                               checker_exit_code=checked.returncode, checker_stderr=checked.stderr,
                               certificate_sha256=digest(certificate))
                break
            model.add_bool_or([variable.Not() for variable in selected])
            save()
        else:
            receipt["result"] = "CANDIDATE_LIMIT"
    save()
    print(json.dumps({key: receipt[key] for key in ("v", "multiplier", "result", "total_seconds")}, indent=2))


if __name__ == "__main__":
    main()
