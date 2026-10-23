"""Single-base candidate enumeration and a parallel SAT pool runner.

single_base_candidates(M, j, k): enumerate k distinct base-j STS candidates of
model M (a KM2), ignoring the other bases (G-orbit columns become at-most-one,
pair columns of base j exactly-one).  Distinctness by blocking clauses on the
selected row set.
"""
from __future__ import annotations

import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

from satlib import CNF, solve


def single_base_cnf(M, j, forbid_orbits=()):
    cnf = CNF()
    rows = [i for i, r in enumerate(M.rows) if r[0] == j]
    rv = {i: cnf.var() for i in rows}
    bycol = {}
    for i in rows:
        for c in M.rows[i][2]:
            bycol.setdefault(c, []).append(rv[i])
    for c, lits in bycol.items():
        if c[0] == "O":
            if c[1] in forbid_orbits:
                for l in lits:
                    cnf.add([-l])
            else:
                cnf.at_most_one(lits)
        else:
            cnf.exactly_one(lits)
    # every pair column of base j must be coverable
    for c in M.cols:
        if c[0] == "P" and c[1] == j and c not in bycol:
            cnf.add([])
    return cnf, rv


def single_base_candidates(M, j, k, path, timeout=60, seed=0, forbid_orbits=()):
    cnf, rv = single_base_cnf(M, j, forbid_orbits)
    sols = []
    for it in range(k):
        cnf.write(path)
        st, model, dt = solve(path, "kissat", timeout=timeout, seed=seed + it)
        if st != "SAT":
            return sols, st
        sel = sorted(i for i, v in rv.items() if v in model)
        sols.append(sel)
        cnf.add([-rv[i] for i in sel])
    return sols, "LIMIT"


def run_pool(jobs, workers=4):
    """jobs: list of dicts with keys cmd (list), log (path).  Returns list of
    (job, returncode, stdout, seconds)."""
    def run(job):
        t0 = time.time()
        p = subprocess.run(job["cmd"], capture_output=True, text=True)
        dt = time.time() - t0
        with open(job["log"], "w") as f:
            f.write(" ".join(job["cmd"]) + "\n" + p.stdout + "\n--stderr--\n" + p.stderr)
        return job, p.returncode, p.stdout, dt
    with ThreadPoolExecutor(max_workers=workers) as ex:
        return list(ex.map(run, jobs))
