"""Resumable cube-and-conquer driver (README §1 limits; never deletes; checkpoint = one JSON line per finished cube).

cube : march_cu CNF -d DEPTH -o CUBES   (cubes written inside the lane)
solve: each cube "a l1 .. lk 0" is solved as CNF + k unit clauses streamed to CaDiCaL's stdin (no per-cube CNF copies),
       native time limit -t; results appended to RESULTS.jsonl (cube index, literals, status, exit, seconds).
       Already-recorded cubes are skipped (resume). Workers <= --jobs. Timeouts/errors are UNKNOWN, never UNSAT.
cover: CNF + negated cubes (one clause per cube) — must be UNSAT for the cube set to be exhaustive (refuted lookahead
       leaves are covered by this formula); solved like any instance (proof via proof_run.py when certifying).

python -B cnc_run.py cube  --cnf X.cnf --depth 10 --cubes X.d10.icnf --march ../env/cnc/march_cu/march_cu
python -B cnc_run.py solve --cnf X.cnf --cubes X.d10.icnf --results X.d10.results.jsonl --jobs 3 --time 1800
python -B cnc_run.py cover --cnf X.cnf --cubes X.d10.icnf --out X.d10.cover.cnf
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import threading
import time


def read_cubes(path):
    cubes = []
    for line in open(path):
        if line.startswith("a "):
            lits = [int(t) for t in line.split()[1:]]
            assert lits[-1] == 0
            cubes.append(lits[:-1])
    return cubes


def split_cnf(path):
    with open(path) as fh:
        header = fh.readline()
        assert header.startswith("p cnf")
        body = fh.read()
    _, _, nv, nc = header.split()
    return int(nv), int(nc), body


def cmd_cube(a):
    t0 = time.time()
    with open(a.cubes + ".march.log", "x") as log:
        r = subprocess.run([a.march, a.cnf, "-d", str(a.depth), "-o", a.cubes], stdout=log, stderr=subprocess.STDOUT)
    rec = {"mode": "cube", "argv": sys.argv, "exit": r.returncode, "secs": round(time.time() - t0, 1),
           "cubes": len(read_cubes(a.cubes)) if os.path.exists(a.cubes) else None,
           "cnf_sha256": hashlib.sha256(open(a.cnf, "rb").read()).hexdigest(),
           "cubes_sha256": hashlib.sha256(open(a.cubes, "rb").read()).hexdigest() if os.path.exists(a.cubes) else None}
    with open(a.cubes + ".receipt.json", "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


def cmd_solve(a):
    nv, nc, body = split_cnf(a.cnf)
    cubes = read_cubes(a.cubes)
    done = set()
    if os.path.exists(a.results):
        for line in open(a.results):
            done.add(json.loads(line)["cube"])
    lock = threading.Lock()

    def run(k):
        lits = cubes[k]
        t0 = time.time()
        p = subprocess.Popen(["cadical", "-q", "-t", str(a.time)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, text=True)
        payload = "p cnf %d %d\n" % (nv, nc + len(lits)) + body + "".join("%d 0\n" % l for l in lits)
        out, _ = p.communicate(payload)
        status = {10: "SAT", 20: "UNSAT"}.get(p.returncode, "UNKNOWN")
        rec = {"cube": k, "lits": lits, "status": status, "exit": p.returncode, "secs": round(time.time() - t0, 1)}
        if status == "SAT":
            rec["model"] = [int(t) for line in out.splitlines() if line.startswith("v ") for t in line.split()[1:]]
        with lock:
            with open(a.results, "a") as fh:
                fh.write(json.dumps(rec) + "\n")
        return rec

    todo = [k for k in range(len(cubes)) if k not in done]
    print(json.dumps({"cubes": len(cubes), "already_done": len(done), "todo": len(todo)}), flush=True)
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for rec in ex.map(run, todo):
            print(json.dumps({k: rec[k] for k in ("cube", "status", "secs")}), flush=True)
            if rec["status"] == "SAT" and a.stop_on_sat:
                break


def cmd_cover(a):
    nv, nc, body = split_cnf(a.cnf)
    cubes = read_cubes(a.cubes)
    with open(a.out, "x") as fh:
        fh.write("p cnf %d %d\n" % (nv, nc + len(cubes)))
        fh.write(body)
        for lits in cubes:
            fh.write(" ".join(str(-l) for l in lits) + " 0\n")
    print(json.dumps({"cover_cnf": a.out, "negated_cubes": len(cubes)}))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["cube", "solve", "cover"])
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--cubes", required=True)
    ap.add_argument("--depth", type=int, default=10)
    ap.add_argument("--march", default=None)
    ap.add_argument("--results")
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--time", type=int, default=1800)
    ap.add_argument("--stop-on-sat", action="store_true")
    ap.add_argument("--out")
    a = ap.parse_args()
    {"cube": cmd_cube, "solve": cmd_solve, "cover": cmd_cover}[a.mode](a)


if __name__ == "__main__":
    main()
