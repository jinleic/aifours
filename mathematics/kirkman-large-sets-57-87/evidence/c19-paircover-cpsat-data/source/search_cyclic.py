#!/usr/bin/env python3
"""Cyclic LKTS search: a resolved KTS transverse to Z_(v-2) triple orbits.

Requires ortools. Example (from target dir):
  UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools python work/search_cyclic.py --v 9 --seconds 120 --threads 4 --output evidence/cyclic9
Point action: translation on 0..v-3, fixing v-2 and v-1.
Each resolution class is canonically labelled by the difference of its infinity-1
block; class 0 contains {0, infinity-1, infinity-2}. This is WLOG.
"""
import argparse
from collections import defaultdict
import hashlib
import itertools
import json
from pathlib import Path
import platform
import subprocess
import sys
import time


def orbit_key(block, n):
    finite = [x for x in block if x < n]
    fixed = tuple(x for x in block if x >= n)
    return min(tuple(sorted((x - t) % n for x in finite)) + fixed for t in finite)


def write_certificate(path, v, base):
    n = v - 2
    with Path(path).open("w") as stream:
        stream.write(f"# Developed under Z_{n}; fixed points {n}, {n+1}\nLKTS {v}\n")
        for t in range(n):
            stream.write(f"\nKTS {t}\n")
            for c, parallel in enumerate(base):
                stream.write(f"CLASS {c}\n")
                for block in sorted(parallel):
                    stream.write(" ".join(str((x + t) % n if x < n else x) for x in block) + "\n")


def main():
    from ortools.sat.python import cp_model
    import ortools
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v", type=int, required=True)
    ap.add_argument("--seconds", type=float, default=120)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--reflection", action="store_true", help="negation swaps the infinities and fixes every parallel class")
    args = ap.parse_args()
    v, n = args.v, args.v - 2
    if v < 9 or v % 6 != 3 or not 1 <= args.threads <= 16:
        ap.error("v>=9 must be 3 mod6, and threads in 1..16")
    started = time.monotonic()
    model = cp_model.CpModel()
    rows = []
    constraints = defaultdict(list)
    seen = set()
    classes = (v - 1) // 2
    triples = list(itertools.combinations(range(v), 3))
    # In the reflection model, canonical class labels are the fixed 0-blocks,
    # not infinity differences: c0={0,inf1,inf2}; cd={0,d,n-d}.
    def reflection(block):
        return tuple(sorted((-x) % n if x < n else (2*n + 1 - x) for x in block))
    for b in triples:
        if args.reflection:
            rb = reflection(b)
            bundle = tuple(sorted(set((b, rb))))
            if bundle in seen:
                continue
            seen.add(bundle)
            if len(bundle) == 1:
                if b == (0, n, n+1):
                    allowed = [0]
                elif 0 in b and all(x < n for x in b):
                    allowed = [min(x for x in b if x != 0)]
                else:
                    continue
            else:
                if any(0 in bb for bb in bundle):
                    continue
                allowed = range(classes)
        else:
            bundle = (b,)
            if n in b:
                if n+1 in b:
                    if b[0] != 0:
                        continue
                    allowed = [0]
                else:
                    d = (b[1] - b[0]) % n
                    allowed = [min(d, n-d)]
            elif n+1 in b:
                allowed = range(1, classes)
            else:
                allowed = range(classes)
        common = []
        for bb in bundle:
            common.extend(("pair",) + pair for pair in itertools.combinations(bb, 2))
            common.append(("orbit",) + orbit_key(bb, n))
        if len(set(common)) != len(common):
            continue
        for c in allowed:
            keys = common + [("point", c, x) for bb in bundle for x in bb]
            if len(set(keys)) != len(keys):
                continue
            variable = model.new_bool_var(f"r{len(rows)}")
            rows.append((variable, c, bundle))
            for key in keys:
                constraints[key].append(variable)
    required = set(("pair",) + p for p in itertools.combinations(range(v), 2))
    required.update(("orbit",) + orbit_key(b, n) for b in triples)
    required.update(("point", c, x) for c in range(classes) for x in range(v))
    for key in sorted(required):
        model.add_exactly_one(constraints[key])
    proto_text = str(model.proto).encode()
    instance_hash = hashlib.sha256(proto_text).hexdigest()
    build_seconds = time.monotonic() - started
    del proto_text
    receipt = {"v": v, "group": f"Z_{n} fixes two points", "reflection_all_classes_fixed": args.reflection,
               "rows": len(rows), "columns": len(required), "empty_columns": sum(not constraints[k] for k in required),
               "instance_sha256": instance_hash, "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "wall_clock_cap_seconds": args.seconds, "threads": args.threads, "seed": args.seed,
               "build_seconds": build_seconds, "ortools_version": ortools.__version__, "python": platform.python_version(),
               "command": sys.argv, "result": "RUNNING"}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.with_suffix(".json").write_text(json.dumps(receipt, indent=2))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.threads
    solver.parameters.random_seed = args.seed
    log_path = args.output.with_suffix(".log")
    with log_path.open("w") as log:
        solver.parameters.log_search_progress = True
        solver.parameters.log_to_stdout = False
        solver.log_callback = lambda text: log.write(text + "\n")
        status = solver.solve(model)
    receipt.update(result=solver.status_name(status), solver_wall_seconds=solver.wall_time,
                   total_seconds=time.monotonic()-started, branches=solver.num_branches, conflicts=solver.num_conflicts)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        base = [[] for _ in range(classes)]
        for variable, c, bundle in rows:
            if solver.value(variable):
                base[c].extend(bundle)
        cert = args.output.with_suffix(".txt")
        write_certificate(cert, v, base)
        checked = subprocess.run([sys.executable, str(Path(__file__).with_name("check_lkts.py")), str(cert)], capture_output=True, text=True)
        args.output.with_suffix(".check.json").write_text(checked.stdout)
        receipt["checker_exit_code"] = checked.returncode
        receipt["certificate_sha256"] = hashlib.sha256(cert.read_bytes()).hexdigest()
        if checked.returncode:
            receipt["checker_error"] = checked.stderr
    args.output.with_suffix(".json").write_text(json.dumps(receipt, indent=2))
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
