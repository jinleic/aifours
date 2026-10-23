"""Minimal CNF builder + external SAT solver runner (kissat / cadical)."""
from __future__ import annotations

import hashlib
import os
import subprocess
import time


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def var(self):
        self.nv += 1
        return self.nv

    def vars(self, k):
        return [self.var() for _ in range(k)]

    def add(self, cl):
        self.clauses.append(list(cl))

    def at_most_one(self, lits):
        lits = list(lits)
        k = len(lits)
        if k <= 1:
            return
        if k <= 6:
            for i in range(k):
                for j in range(i + 1, k):
                    self.add([-lits[i], -lits[j]])
            return
        # sequential counter (Sinz)
        s = self.vars(k - 1)
        self.add([-lits[0], s[0]])
        for i in range(1, k - 1):
            self.add([-lits[i], s[i]])
            self.add([-s[i - 1], s[i]])
            self.add([-lits[i], -s[i - 1]])
        self.add([-lits[k - 1], -s[k - 2]])

    def exactly_one(self, lits):
        lits = list(lits)
        self.add(lits)
        self.at_most_one(lits)

    def dimacs(self):
        out = [f"p cnf {self.nv} {len(self.clauses)}"]
        out.extend(" ".join(map(str, c)) + " 0" for c in self.clauses)
        return "\n".join(out) + "\n"

    def write(self, path):
        data = self.dimacs()
        with open(path, "w") as f:
            f.write(data)
        return hashlib.sha256(data.encode()).hexdigest()


def solve(path, solver="kissat", timeout=600, seed=None, log=None, extra=()):
    """Run solver; return (status, model_set, seconds). status in SAT/UNSAT/UNKNOWN."""
    if solver == "kissat":
        cmd = ["kissat", "-q", f"--time={int(timeout)}"]
        if seed is not None:
            cmd.append(f"--seed={seed}")
    elif solver == "cadical":
        cmd = ["cadical", "-q", "-t", str(int(timeout))]
        if seed is not None:
            cmd.append(f"--seed={seed}")
    else:
        raise ValueError(solver)
    cmd.extend(extra)
    cmd.append(path)
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    dt = time.time() - t0
    out = p.stdout
    if log:
        with open(log, "w") as f:
            f.write(" ".join(cmd) + "\n" + out + "\n--stderr--\n" + p.stderr)
    status = "UNKNOWN"
    model = set()
    for line in out.splitlines():
        if line.startswith("s "):
            if "UNSATISFIABLE" in line:
                status = "UNSAT"
            elif "SATISFIABLE" in line:
                status = "SAT"
        elif line.startswith("v "):
            for x in line[2:].split():
                xi = int(x)
                if xi > 0:
                    model.add(xi)
    return status, model, dt
