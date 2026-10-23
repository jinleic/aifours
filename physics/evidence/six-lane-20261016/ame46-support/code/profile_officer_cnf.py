#!/usr/bin/env python3
"""profile_officer_cnf.py: profile-level officer-placement relaxation. Lane ame46-support. Exploration tool.

Valid for every AME(4,6) state with a given deficit profile and any e. Variables o_x (an officer at x), x in [6]^4.
 (C1) every line (b, c) of a pair (j, k) with (b, c) not in V_j x V_k carries exactly one officer: such a line is not a
      hole line (Lemma 12: hole lines lie in V_j x V_k), so it holds exactly one officer;
 (C2) every line (a, b) in V_j x V_k carries at most one officer (L42-3);
 (C3) for an ordered pair (j, k) and a in V_j: exactly |V_k| - d_{j,a} of the lines (a, b), b in V_k, carry an
      officer, because d_{j,a} of them are hole lines (L42-8 and Lemma 12).
UNSAT of this CNF excludes the profile for every e. Here only solver status is reported; an exclusion used in a proof
needs an LRAT-checked run.
"""
import itertools
import os
import subprocess
import sys

import ame_e0_cnf as base
import large_t_e0 as lte

PAIRS = list(itertools.combinations(range(4), 2))


def build(prof):
    h = sum(prof[0])
    V = [set(range(6 - len(p), 6)) for p in prof]
    d = [{a: p[k] for k, a in enumerate(sorted(V[i]))} for i, p in enumerate(prof)]
    pts = list(itertools.product(range(6), repeat=4))
    var = {x: k + 1 for k, x in enumerate(pts)}
    F = base.CNF()
    F.nv = len(pts)
    for (j, k) in PAIRS:
        for b in range(6):
            for c in range(6):
                lits = [var[x] for x in pts if x[j] == b and x[k] == c]
                if b in V[j] and c in V[k]:
                    F.at_most_k(lits, 1)
                else:
                    F.add(lits)
                    F.at_most_k(lits, 1)
    for j in range(4):
        for k in range(4):
            if j == k:
                continue
            for a in V[j]:
                # line indicator for (a, b), b in V_k: the officer count on the line is at most one, so the indicator
                # is the OR of its points
                inds = []
                for b in sorted(V[k]):
                    lits = [var[x] for x in pts if x[j] == a and x[k] == b]
                    v = F.nv = F.nv + 1
                    F.add([-v] + lits)
                    for l in lits:
                        F.add([-l, v])
                    inds.append(v)
                want = len(V[k]) - d[j][a]
                F.at_most_k(inds, want)
                F.at_most_k([-v for v in inds], len(inds) - want)
    return F


def solve(F, tlimit=60):
    text = "p cnf %d %d\n" % (F.nv, len(F.clauses)) + "".join(" ".join(map(str, c)) + " 0\n" for c in F.clauses)
    p = subprocess.run(["cadical", "-q", "-t", str(tlimit)], input=text, capture_output=True, text=True)
    return p.returncode


if __name__ == "__main__":
    for t in [int(x) for x in sys.argv[1].split(",")]:
        h = 36 - t
        res = {}
        for prof in lte.profiles(h):
            st = solve(build(prof), int(sys.argv[2]) if len(sys.argv) > 2 else 60)
            res[tuple(map(tuple, prof))] = st
        unsat = [p for p, s in res.items() if s == 20]
        unk = [p for p, s in res.items() if s not in (10, 20)]
        print("t=%d profiles=%d UNSAT=%d SAT=%d UNKNOWN=%d" % (t, len(res), len(unsat),
                                                              sum(1 for s in res.values() if s == 10), len(unk)),
              flush=True)
        for p in unsat:
            print("  UNSAT", p, flush=True)
