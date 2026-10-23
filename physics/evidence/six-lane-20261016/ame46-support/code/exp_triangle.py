#!/usr/bin/env python3
"""exp_triangle.py: exploration only. e = 0 doubled-triangle pattern clauses. Lane ame46-support.

Candidate lemma (e = 0), to be written before any use:
- Fix a coordinate i and values a ≠ a′ in V_i. Write points as (x_i; z), with z the other three coordinates.
- Call z (a,a′)-doubled if (a; z) and (a′; z) both lie in N.
- In a reshaping whose row pair is (i, j), the points (a; z) and (a′; z) share their column, so at e = 0 that column
  holds exactly these two points. The row (a, z_j) holds exactly two points, (a; z) and (a; z′), and the 2×2 block
  forces (a′; z′) ∈ N as well, with z′_j = z_j. Its phase congruence reads δ(z) − δ(z′) ≡ π, where
  δ(z) = φ(a; z) − φ(a′; z).
- So the doubled points form a graph whose edges are coloured by the other coordinates j, with δ jumping by π along
  every edge.
- A triangle z1, z2, z3, with z1, z2 agreeing in coordinate c1, z2, z3 in c2 and z1, z3 in c3, {c1, c2, c3} the
  three other coordinates, gives 3π ≡ 0, a contradiction.
Clause: ¬(a;z1) ∨ ¬(a′;z1) ∨ ¬(a;z2) ∨ ¬(a′;z2) ∨ ¬(a;z3) ∨ ¬(a′;z3), for every such triangle inside Π V_i.
At e = 0 the agreeing pairs automatically form closed blocks, so no closure literals are needed.
"""
import argparse
import itertools
import subprocess
import time

import exp_joint
import large_t_e0 as lte
import large_t_gen as ltg
import large_t_lex as v2
import phase_cert as pcert
import reconstruct_e0 as rc


def triangle_clauses(S):
    cl = []
    for i in range(4):
        others = [k for k in range(4) if k != i]
        c1, c2, c3 = others
        for a, a2 in itertools.combinations(S.V[i], 2):
            Z = list(itertools.product(*[S.V[k] for k in others]))
            idx = {k: n for n, k in enumerate(others)}

            def pt(val, z):
                x = [0] * 4
                x[i] = val
                for k in others:
                    x[k] = z[idx[k]]
                return tuple(x)
            for z1 in Z:
                for z2 in Z:
                    if z2[idx[c1]] != z1[idx[c1]] or z2[idx[c2]] == z1[idx[c2]] or z2[idx[c3]] == z1[idx[c3]]:
                        continue
                    for z3 in Z:
                        if z3[idx[c2]] != z2[idx[c2]] or z3[idx[c3]] != z1[idx[c3]]:
                            continue
                        if z3[idx[c1]] == z1[idx[c1]]:
                            continue
                        lits = []
                        for z in (z1, z2, z3):
                            lits += [-S.var[pt(a, z)], -S.var[pt(a2, z)]]
                        cl.append(lits)
    return cl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--budget", type=float, default=300)
    ap.add_argument("--joint", action="store_true")
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    S = exp_joint.build_joint(prof, 0, h) if a.joint else ltg.SmallGen(prof)
    if not a.joint:
        S.build_gen(0, h)
    tri = triangle_clauses(S)
    S.cl += tri
    for g in v2.generators(S):
        v2.add_lex_leader(S, g)
    blocks, n, t0, status, kinds = [], 0, time.time(), "budget", {}
    while time.time() - t0 < a.budget:
        p = subprocess.run(["cadical", "-q", "-t", str(int(max(1, a.budget - (time.time() - t0))))],
                           input=v2.dimacs(S.nv, S.cl + blocks), capture_output=True, text=True)
        if p.returncode == 20:
            status = "COMPLETE"
            break
        if p.returncode != 10:
            status = "solver %d" % p.returncode
            break
        m = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
             if int(v) > 0}
        N = [x for x in S.points if S.var[x] in m]
        blocks.append([-S.var[x] for x in N])
        n += 1
        okc, _ = ltg.component_checks(N)
        c = pcert.extract_certificate(N) if okc else None
        key = "components" if not okc else ("phase%d" % len(c) if c else "phase-consistent")
        kinds[key] = kinds.get(key, 0) + 1
        if key == "phase-consistent":
            st, T = rc.completion(N)
            print("phase-consistent N #%d completion %s" % (n, st), flush=True)
    print("profile", prof, "joint" if a.joint else "N-only", "triangles", len(tri), status, "solutions", n, kinds,
          "elapsed %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
