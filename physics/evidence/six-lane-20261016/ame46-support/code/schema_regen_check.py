#!/usr/bin/env python3
"""schema_regen_check.py: regenerate v5 final CNFs from the text of review/V4_PROOF_SCHEMA.r2.md and compare their
SHA-256 with the reports. Lane ame46-support. It imports only the base builder (large_t_gen.SmallGen.build_gen), the
Sinz counter (ame_e0_cnf.CNF.at_most_k) and large_t_e0.profiles. These three are referenced by the schema. It does
NOT import exp_joint, profile_officer_cnf, exp_triangle, large_t_lex or large_t_joint5.
Usage: schema_regen_check.py REPORT.json [...]
"""
import hashlib
import itertools
import json
import sys

import ame_e0_cnf as base
import large_t_e0 as lte
import large_t_gen as ltg

BPAIRS = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
SPAIRS = list(itertools.combinations(range(4), 2))
PTS4 = list(itertools.product(range(6), repeat=4))


def officer_cnf(prof):
    V = [list(range(6 - len(p), 6)) for p in prof]
    d = [{a: p[k] for k, a in enumerate(V[i])} for i, p in enumerate(prof)]
    var = {y: n + 1 for n, y in enumerate(PTS4)}
    F = base.CNF()
    F.nv = 1296
    for (j, k) in SPAIRS:
        for b in range(6):
            for c in range(6):
                L = [var[y] for y in PTS4 if y[j] == b and y[k] == c]
                if b in V[j] and c in V[k]:
                    F.at_most_k(L, 1)
                else:
                    F.add(L)
                    F.at_most_k(L, 1)
    for j in range(4):
        for k in range(4):
            if j == k:
                continue
            for a in V[j]:
                inds = []
                for b in V[k]:
                    L = [var[y] for y in PTS4 if y[j] == a and y[k] == b]
                    F.nv += 1
                    v = F.nv
                    F.add([-v] + L)
                    for l in L:
                        F.add([-l, v])
                    inds.append(v)
                F.at_most_k(inds, len(V[k]) - d[j][a])
                F.at_most_k([-v for v in inds], d[j][a])
    return F


def regen(prof, e, h, triangles, sols):
    S = ltg.SmallGen([list(p) for p in prof])
    S.build_gen(e, h)
    cl = list(S.cl)
    nv0 = S.nv
    F = officer_cnf(prof)
    cl += [[l + nv0 if l > 0 else l - nv0 for l in c] for c in F.clauses]
    nv = nv0 + F.nv
    for (i, j) in BPAIRS:
        for a in S.V[i]:
            for b in S.V[j]:
                hl = S.hl[(i, j, a, b)]
                lam = [nv0 + 1 + n for n, y in enumerate(PTS4) if y[i] == a and y[j] == b]
                cl += [[-hl, -o] for o in lam] + [[hl] + lam]
    if triangles:
        for i in range(4):
            c1, c2, c3 = [k for k in range(4) if k != i]
            Z = list(itertools.product(S.V[c1], S.V[c2], S.V[c3]))

            def pt(val, z):
                x = [0] * 4
                x[i], x[c1], x[c2], x[c3] = val, z[0], z[1], z[2]
                return tuple(x)
            for a, a2 in itertools.combinations(S.V[i], 2):
                for z1 in Z:
                    for z2 in Z:
                        if not (z2[0] == z1[0] and z2[1] != z1[1] and z2[2] != z1[2]):
                            continue
                        for z3 in Z:
                            if not (z3[1] == z2[1] and z3[2] == z1[2] and z3[0] != z1[0]):
                                continue
                            lits = []
                            for z in (z1, z2, z3):
                                lits += [-S.var[pt(a, z)], -S.var[pt(a2, z)]]
                            cl.append(lits)
    # generators: coordinate swaps first, then value transpositions per d-class (first-occurrence order)
    gens = []
    sig = [tuple(p) for p in prof]
    for i in range(3):
        if sig[i] == sig[i + 1]:
            gens.append(lambda x, i=i: tuple(x[i + 1] if k == i else x[i] if k == i + 1 else x[k] for k in range(4)))
    for i in range(4):
        classes = {}
        for a in S.V[i]:
            classes.setdefault(S.d[i][a], []).append(a)
        for clv in classes.values():
            for a, b in zip(clv, clv[1:]):
                gens.append(lambda x, i=i, a=a, b=b: tuple((b if x[k] == a else a if x[k] == b else x[k]) if k == i
                                                           else x[k] for k in range(4)))
    for g in gens:
        q = None
        for p in S.points:
            x, y = S.var[p], S.var[g(p)]
            if x == y:
                continue
            if q is None:
                cl.append([-x, y])
                nv += 1
                qk = nv
                cl += [[-x, -y, qk], [x, y, qk], [-qk, -x, y], [-qk, x, -y]]
            else:
                cl.append([-q, -x, y])
                nv += 1
                qk = nv
                cl += [[-qk, q], [-q, -x, -y, qk], [-q, x, y, qk], [-qk, -x, y], [-qk, x, -y]]
            q = qk
    idx = {"".join(map(str, x)): x for x in S.points}
    for N in sols:
        cl.append([-S.var[idx[s]] for s in N])
    text = "p cnf %d %d\n" % (nv, len(cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cl)
    return hashlib.sha256(text.encode()).hexdigest()


def main():
    allok = True
    for path in sys.argv[1:]:
        rep = json.load(open(path))
        t, e, h = rep["t"], rep["e"], rep["h"]
        for pr in rep["profiles"]:
            if pr["status"] != "ENUMERATED":
                continue
            prof = [tuple(q) for q in pr["profile"]]
            sha = regen(prof, e, h, rep.get("triangles", False), [r["N"] for r in pr["reps"]])
            ok = sha == pr["final_cnf_sha256"]
            allok &= ok
            print(path.split("/")[-1], pr["index"], "MATCH" if ok else "MISMATCH", sha[:16], flush=True)
    print("all_match:", allok)


if __name__ == "__main__":
    main()
