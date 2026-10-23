#!/usr/bin/env python3
"""exp_officer_first.py: exploration only. Officer-first decomposition for one profile. Lane ame46-support.

Step A enumerates officer placements T (the Lemma 19 CNF over [6]^4) up to symmetry. It adds lex-leader constraints
on the officer variables for these generators:
- adjacent value transpositions inside each d-class of V_i;
- adjacent transpositions of the non-V values of each coordinate (all deficit 0, hence interchangeable);
- adjacent swaps of coordinates with equal profile parts.
Each found T is blocked individually.
Step B fixes, for each found T, the hole pattern: the lines of V_i x V_j that hold no officer. It then enumerates every
N of the N-only CNF with those hole indicators fixed, and applies the exact checks (components, moduli, phase). N is
not symmetry-broken in step B.
Completeness, if both steps finish with UNSAT: a true (N, T) has some image (g N, g T) with g T lex-least. That g T is
a found T, and g N is a solution of step B for it.
Reports counts and timings within the budgets.
"""
import argparse
import itertools
import subprocess
import time

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import phase_check as pc
import phase_cert as pcert
import profile_officer_cnf as poc

PTS = list(itertools.product(range(6), repeat=4))


class Box:
    pass


def officer_generators(prof):
    V = [set(range(6 - len(p), 6)) for p in prof]
    d = [{a: p[k] for k, a in enumerate(sorted(V[i]))} for i, p in enumerate(prof)]
    gens = []
    for i in range(4):
        classes = {}
        for a in range(6):
            classes.setdefault(d[i].get(a, 0), []).append(a)
        for cl in classes.values():
            for a, b in zip(cl, cl[1:]):
                gens.append({x: tuple((b if x[k] == a else a if x[k] == b else x[k]) if k == i else x[k]
                                      for k in range(4)) for x in PTS})
    sig = [tuple(p) for p in prof]
    for i in range(3):
        if sig[i] == sig[i + 1]:
            gens.append({x: tuple(x[i + 1] if k == i else x[i] if k == i + 1 else x[k] for k in range(4))
                         for x in PTS})
    return gens


def solve(text, tl):
    p = subprocess.run(["cadical", "-q", "-t", str(int(max(1, tl)))], input=text, capture_output=True, text=True)
    model = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
             if int(v) > 0}
    return p.returncode, model


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--budget-a", type=float, default=120)
    ap.add_argument("--budget-b", type=float, default=120)
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    F = poc.build(prof)
    O = Box()
    O.points, O.var, O.cl, O.nv = PTS, {x: k + 1 for k, x in enumerate(PTS)}, list(F.clauses), F.nv
    O.new = lambda: (setattr(O, "nv", O.nv + 1) or O.nv)
    for g in officer_generators(prof):
        v2.add_lex_leader(O, g)
    reps, blocks, t0, statusA = [], [], time.time(), "budget"
    while time.time() - t0 < a.budget_a:
        st, model = solve(v2.dimacs(O.nv, O.cl + blocks), a.budget_a - (time.time() - t0))
        if st == 20:
            statusA = "COMPLETE"
            break
        if st != 10:
            statusA = "solver %d" % st
            break
        T = [x for x in PTS if O.var[x] in model]
        reps.append(T)
        blocks.append([-O.var[x] for x in T])
    print("A: officer reps", len(reps), statusA, "%.1f s" % (time.time() - t0), flush=True)
    t1 = time.time()
    totN, open_ = 0, 0
    for k, T in enumerate(reps):
        if time.time() - t1 > a.budget_b:
            print("B: budget exhausted after", k, "reps")
            break
        S = ltg.SmallGen(prof)
        S.build_gen(a.e, h)
        Tset = set(T)
        for (i, j) in lte.PAIRS:
            for x1 in S.V[i]:
                for x2 in S.V[j]:
                    hole = not any(y[i] == x1 and y[j] == x2 for y in Tset)
                    S.cl.append([S.hl[(i, j, x1, x2)]] if hole else [-S.hl[(i, j, x1, x2)]])
        nb, nN, statusB = [], 0, "?"
        while True:
            st, model = solve(v2.dimacs(S.nv, S.cl + nb), 600)
            if st == 20:
                statusB = "COMPLETE"
                break
            if st != 10:
                statusB = "solver %d" % st
                break
            N = [x for x in S.points if S.var[x] in model]
            nb.append([-S.var[x] for x in N])
            nN += 1
            okc, _ = ltg.component_checks(N)
            excl = not okc
            if not excl:
                mc = ltg.moduli_certificate(N)
                excl = mc is not None and mc["verified"]
            if not excl:
                excl = pcert.extract_certificate(N) is not None
            open_ += (not excl)
        totN += nN
        print("B: rep %d: N solutions %d %s" % (k, nN, statusB), flush=True)
    print("profile", prof, "officer reps", len(reps), statusA, "total N", totN, "open (passed all checks)", open_,
          "elapsed %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
