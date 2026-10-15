#!/usr/bin/env python3
"""Cyclic LKTS exact cover with multiplier automorphism of the base resolution.

The multiplier x->a*x mod(v-2) fixes both infinities. Class 0 contains
{0,inf1,inf2}; class d is labelled by the infinity-1 block's unsigned difference.
The induced class action is d->min(a*d mod n, -a*d mod n).
Rows are complete orbits of (triple,class) placements; columns are pair,
translation-orbit, and (class,point) constraints. Repeated columns reject a row.
Run: UV_CACHE_DIR=/tmp/lkts-uv-cache uv run --with ortools python work/search_multiplier.py --v 57 --multiplier 21 --seconds 600 --threads 4 --output evidence/multiplier57-a21
"""
import argparse
from collections import defaultdict
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


def main():
    from ortools.sat.python import cp_model
    import ortools
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--v", type=int, required=True)
    ap.add_argument("--multiplier", type=int, required=True)
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    v, n, a = args.v, args.v-2, args.multiplier
    if v < 9 or v % 6 != 3 or math.gcd(a,n) != 1 or not 1 <= args.threads <= 16:
        ap.error("v>=9 is 3 mod6, multiplier is a unit, threads in1..16")
    started = time.monotonic()
    triples = list(itertools.combinations(range(v), 3))
    tids = {b:i for i,b in enumerate(triples)}
    image = [tids[tuple(sorted(a*x % n if x<n else x for x in b))] for b in triples]
    classes = (v-1)//2
    cimage = [min(a*c%n, -a*c%n) for c in range(classes)]
    tkeys = [[("pair",)+p for p in itertools.combinations(b,2)] + [("orbit",)+orbit_key(b,n)] for b in triples]
    model = cp_model.CpModel()
    columns = defaultdict(list)
    rows = []
    discarded_collisions = 0
    def allowed(b):
        if n in b:
            if n+1 in b:
                return [0] if b[0] == 0 else []
            d = (b[1]-b[0]) % n
            return [min(d,n-d)]
        return range(1,classes) if n+1 in b else range(classes)
    for ti,b in enumerate(triples):
        for c in allowed(b):
            placement = (ti,c)
            orbit = [placement]
            current = (image[ti],cimage[c])
            while current != placement:
                orbit.append(current)
                current = (image[current[0]],cimage[current[1]])
            if placement != min(orbit):
                continue
            keys = []
            for bi,ci in orbit:
                keys.extend(tkeys[bi])
                keys.extend(("point",ci,x) for x in triples[bi])
            if len(set(keys)) != len(keys):
                discarded_collisions += 1
                continue
            var = model.new_bool_var(f"r{len(rows)}")
            rows.append((var,orbit))
            for key in keys:
                columns[key].append(var)
    required = set(("pair",)+p for p in itertools.combinations(range(v),2))
    required.update(("orbit",)+orbit_key(b,n) for b in triples)
    required.update(("point",c,x) for c in range(classes) for x in range(v))
    # Distinct columns sometimes become identical after the group quotient.
    # Removing duplicate equalities is exact, and substantially reduces presolve.
    equalities = set()
    for key in sorted(required):
        ids = tuple(var.index for var in columns[key])
        if ids not in equalities:
            model.add_exactly_one(columns[key])
            equalities.add(ids)
    instance_hash = hashlib.sha256(str(model.proto).encode()).hexdigest()
    order = 1
    value = a % n
    while value != 1:
        value = value*a % n
        order += 1
    receipt = {"v":v, "translation_group":f"Z_{n}, two fixed points", "multiplier":a,
               "multiplier_order":order, "class_action":"unsigned difference multiplication",
               "rows":len(rows), "columns":len(required), "distinct_equalities":len(equalities),
               "discarded_colliding_orbits":discarded_collisions,
               "empty_columns":sum(not columns[k] for k in required), "instance_sha256":instance_hash,
               "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "helper_sha256":hashlib.sha256(Path(__file__).with_name("search_cyclic.py").read_bytes()).hexdigest(),
               "wall_clock_cap_seconds":args.seconds,"threads":args.threads,"seed":args.seed,
               "build_seconds":time.monotonic()-started,"python":platform.python_version(),
               "ortools_version":ortools.__version__,"command":sys.argv,"result":"RUNNING"}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.threads
    solver.parameters.random_seed = args.seed
    with args.output.with_suffix(".log").open("w") as log:
        solver.parameters.log_search_progress = True
        solver.parameters.log_to_stdout = False
        solver.log_callback = lambda text: log.write(text+"\n")
        status = solver.solve(model)
    receipt.update(result=solver.status_name(status),solver_wall_seconds=solver.wall_time,
                   total_seconds=time.monotonic()-started,branches=solver.num_branches,conflicts=solver.num_conflicts)
    if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
        base = [[] for _ in range(classes)]
        for var,orbit in rows:
            if solver.value(var):
                for bi,ci in orbit:
                    base[ci].append(triples[bi])
        certificate = args.output.with_suffix(".txt")
        write_certificate(certificate,v,base)
        checked = subprocess.run([sys.executable,str(Path(__file__).with_name("check_lkts.py")),str(certificate)],capture_output=True,text=True)
        args.output.with_suffix(".check.json").write_text(checked.stdout)
        receipt["checker_exit_code"] = checked.returncode
        receipt["certificate_sha256"] = hashlib.sha256(certificate.read_bytes()).hexdigest()
        if checked.returncode:
            receipt["checker_error"] = checked.stderr
    args.output.with_suffix(".json").write_text(json.dumps(receipt,indent=2))
    print(json.dumps(receipt,indent=2))


if __name__ == "__main__":
    main()
