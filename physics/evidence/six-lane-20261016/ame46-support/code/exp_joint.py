#!/usr/bin/env python3
"""exp_joint.py: exploration only. Joint N-only plus officer-placement CNF for one profile. Lane ame46-support.

The N-only CNF (SmallGen.build_gen, the families F1-F4 of L46 r2 §3 step 2) and the officer-placement CNF
(profile_officer_cnf.build, Lemma 19 of review/ENGINE_V3.r1.md) are joined by linking each hole-line indicator of
a line in V_i x V_j to "no officer on that line". This is valid for every AME state: a line meets N iff it holds no
officer (L42-2(a), L42-4).
Lex-leader constraints use the v2 generators on the N point variables; officer variables are not broken. Each
found N is blocked individually. Any N found therefore admits an officer completion, which is the projection of the
completion check. Reports the solution count within the budget and whether enumeration completed.
"""
import argparse
import subprocess
import time

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import profile_officer_cnf as poc


def build_joint(prof, e, h):
    S = ltg.SmallGen(prof)
    S.build_gen(e, h)
    F = poc.build(prof)
    off = S.nv
    for c in F.clauses:
        S.cl.append([l + off if l > 0 else l - off for l in c])
    S.nv += F.nv
    # officer point variable of x in [6]^4 is (index of x in product order) + 1 + off
    import itertools
    pts = list(itertools.product(range(6), repeat=4))
    ovar = {x: k + 1 + off for k, x in enumerate(pts)}
    for (i, j) in lte.PAIRS:
        for a in S.V[i]:
            for b in S.V[j]:
                hl = S.hl[(i, j, a, b)]
                line = [ovar[x] for x in pts if x[i] == a and x[j] == b]
                # hl -> no officer on the line; not hl -> some officer on the line
                for o in line:
                    S.cl.append([-hl, -o])
                S.cl.append([hl] + line)
    return S


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--budget", type=float, default=120)
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    S = build_joint(prof, a.e, h)
    for g in v2.generators(S):
        v2.add_lex_leader(S, g)
    blocks, n, times, t0 = [], 0, [], time.time()
    status = "budget"
    while time.time() - t0 < a.budget:
        text = v2.dimacs(S.nv, S.cl + blocks)
        t1 = time.time()
        p = subprocess.run(["cadical", "-q", "-t", str(int(max(1, a.budget - (time.time() - t0))))], input=text,
                           capture_output=True, text=True)
        times.append(time.time() - t1)
        if p.returncode == 20:
            status = "COMPLETE"
            break
        if p.returncode != 10:
            status = "solver %d" % p.returncode
            break
        model = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
                 if int(v) > 0}
        N = [x for x in S.points if S.var[x] in model]
        blocks.append([-S.var[x] for x in N])
        n += 1
    print("profile", prof, "joint", status, "solutions", n, "mean solve %.2f s" % (sum(times) / max(1, len(times))),
          "elapsed %.1f" % (time.time() - t0), "vars", S.nv, "clauses", len(S.cl))


if __name__ == "__main__":
    main()
