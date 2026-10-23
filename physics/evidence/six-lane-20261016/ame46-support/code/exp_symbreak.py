#!/usr/bin/env python3
"""exp_symbreak.py: exploration only. Measures the solution rate of the N-only enumeration for one profile under
different sound symmetry-breaking sets. Lane ame46-support. Nothing here is a certificate.

Modes:
  adj   lex-leader for adjacent value transpositions inside d-classes and adjacent equal-part coordinate swaps (as v2)
  all   lex-leader for ALL value transpositions inside d-classes and ALL equal-part coordinate transpositions
  all2  'all' plus products of two value transpositions in two different coordinates
Every set is a subset of H, so the lex-least member of each orbit satisfies all of the constraints (sound).
Option --e0exact adds the redundant e = 0 constraint that each line meets N in at most 2 points; it is implied by
|N| = 2h with h hole lines per pair, each holding at least 2 points.
Prints the number of solutions found within the time budget and the mean solve time.
"""
import argparse
import itertools
import subprocess
import time

import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2


def value_transpositions(S, all_pairs):
    out = []
    for i in range(4):
        classes = {}
        for a in S.V[i]:
            classes.setdefault(S.d[i][a], []).append(a)
        for cl in classes.values():
            pairs = itertools.combinations(cl, 2) if all_pairs else zip(cl, cl[1:])
            for a, b in pairs:
                out.append((i, a, b))
    return out


def vt_map(S, i, a, b):
    return {x: tuple((b if x[k] == a else a if x[k] == b else x[k]) if k == i else x[k] for k in range(4))
            for x in S.points}


def coord_maps(S, all_pairs):
    sig = [tuple(p) for p in S.prof]
    out = []
    for i, j in itertools.combinations(range(4), 2):
        if sig[i] == sig[j] and (all_pairs or j == i + 1):
            out.append({x: tuple(x[j] if k == i else x[i] if k == j else x[k] for k in range(4)) for x in S.points})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True, help="index into large_t_e0.profiles(h)")
    ap.add_argument("--mode", choices=["adj", "all", "all2"], default="adj")
    ap.add_argument("--e0exact", action="store_true")
    ap.add_argument("--budget", type=float, default=120)
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    S = ltg.SmallGen(prof)
    S.build_gen(a.e, h)
    if a.e0exact:
        for (i, j) in lte.PAIRS:
            for b in S.V[i]:
                for c in S.V[j]:
                    lits = [S.var[x] for x in S.points if x[i] == b and x[j] == c]
                    S.amk(lits, 2)
    allp = a.mode in ("all", "all2")
    maps = [vt_map(S, *v) for v in value_transpositions(S, allp)] + coord_maps(S, allp)
    if a.mode == "all2":
        vts = value_transpositions(S, True)
        for (i1, a1, b1), (i2, a2, b2) in itertools.combinations(vts, 2):
            if i1 != i2:
                m1, m2 = vt_map(S, i1, a1, b1), vt_map(S, i2, a2, b2)
                maps.append({x: m2[m1[x]] for x in S.points})
    for g in maps:
        v2.add_lex_leader(S, g)
    blocks, n, times = [], 0, []
    t0 = time.time()
    while time.time() - t0 < a.budget:
        text = v2.dimacs(S.nv, S.cl + blocks)
        t1 = time.time()
        p = subprocess.run(["cadical", "-q", "-t", str(int(max(1, a.budget - (time.time() - t0))))], input=text,
                           capture_output=True, text=True)
        times.append(time.time() - t1)
        if p.returncode == 20:
            print("ENUMERATION COMPLETE: %d solutions in %.1f s" % (n, time.time() - t0))
            break
        if p.returncode != 10:
            print("solver status %d" % p.returncode)
            break
        model = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
                 if int(v) > 0}
        N = [x for x in S.points if S.var[x] in model]
        blocks.append([-S.var[x] for x in N])
        n += 1
    print("profile", prof, "mode", a.mode, "e0exact", a.e0exact, "constraints", len(maps), "clauses", len(S.cl),
          "solutions", n, "mean solve %.2f s" % (sum(times) / max(1, len(times))), "elapsed %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
