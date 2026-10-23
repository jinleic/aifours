#!/usr/bin/env python3
"""exp_nogood.py: exploration only. Enumeration with phase-certificate nogoods (CEGAR style). Lane ame46-support.

When a found N has an explicit phase certificate C (blocks B_1..B_m with integer weights; phase_cert.py), the whole
family of supports containing C's blocks as genuine components is non-realizable by L42-10. So the engine adds the
nogood clause
    OR_{x in corners(C)} ¬n_x  OR  OR_{y on a line of some block, y not a corner} n_y,
where the second disjunction expresses closure: some block row or column holds a further N point. At e = 0 the
closure part is redundant, since each hole line holds exactly two points; it is still included for uniformity.
Found N that are excluded otherwise are blocked individually. Optionally the joint officer constraints are added
(--joint).
Soundness: a realizable N* satisfies every nogood (it cannot contain a certificate's blocks as genuine components)
and every individual blocking clause unless it equals that solution, which is excluded. So the final UNSAT still
implies that no realizable support exists for the profile.
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

RESH = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def nogood(S, cert):
    corners, others = set(), set()
    for ent in cert:
        rows, cols = RESH[ent["k"]]
        P = [pcert.unpt(c) for c in ent["corners"]]
        corners.update(P)
        for p in P:
            for x in S.points:
                if tuple(x[i] for i in rows) == tuple(p[i] for i in rows) or \
                        tuple(x[i] for i in cols) == tuple(p[i] for i in cols):
                    others.add(x)
    others -= corners
    return [-S.var[x] for x in sorted(corners)] + [S.var[y] for y in sorted(others)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--e", type=int, required=True)
    ap.add_argument("--profile", type=int, required=True)
    ap.add_argument("--budget", type=float, default=300)
    ap.add_argument("--joint", action="store_true")
    a = ap.parse_args()
    h = 36 - a.t
    prof = lte.profiles(h)[a.profile]
    if a.joint:
        S = exp_joint.build_joint(prof, a.e, h)
    else:
        S = ltg.SmallGen(prof)
        S.build_gen(a.e, h)
    for g in v2.generators(S):
        v2.add_lex_leader(S, g)
    extra, n, ng, other, t0, status = [], 0, 0, 0, time.time(), "budget"
    while time.time() - t0 < a.budget:
        p = subprocess.run(["cadical", "-q", "-t", str(int(max(1, a.budget - (time.time() - t0))))],
                           input=v2.dimacs(S.nv, S.cl + extra), capture_output=True, text=True)
        if p.returncode == 20:
            status = "COMPLETE"
            break
        if p.returncode != 10:
            status = "solver %d" % p.returncode
            break
        m = {int(v) for line in p.stdout.splitlines() if line.startswith("v ") for v in line.split()[1:]
             if int(v) > 0}
        N = [x for x in S.points if S.var[x] in m]
        n += 1
        cert = pcert.extract_certificate(N)
        if cert is not None and pcert.verify_certificate(N, cert)[0]:
            extra.append(nogood(S, cert))
            ng += 1
        else:
            extra.append([-S.var[x] for x in N])
            other += 1
            okc, _ = ltg.component_checks(N)
            if okc and a.e == 0:
                st, T = rc.completion(N)
                print("phase-consistent or unchecked N #%d; completion %s" % (n, st), flush=True)
    print("profile", prof, "joint" if a.joint else "N-only", status, "solutions", n, "nogoods", ng,
          "individual blocks", other, "elapsed %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
