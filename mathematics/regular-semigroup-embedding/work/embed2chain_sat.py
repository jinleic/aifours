"""Decide embeddability of a Z2-graded E-unitary orthodox semigroup S, whose band E is a 2-chain band,
into a semidirect product B x| Z2 where B is a 2-chain band (the generated subband in the linked case).

Input: JSON table of S on {0..2n'-1}? No: E = {0..n-1} (the even part), A = {n..N-1} (odd part).
Unknowns: rows/cols of B (sizes It,Lt,Ib,Lb >= those of E, X fixed on the first indices),
involution g on each coordinate set, structure maps phi, psi with (F), (G), g-equivariance,
X a homomorphism, and beta(x y) = beta(x) . g^{sigma(x)}(beta(y)) for all x, y in S, where
beta(e) = X(e) for e in E and beta(s) = X(ss')Y(s's) for s in A (any inverse s'; Lemma 2).

Usage: uv run --with python-sat python work/embed2chain_sat.py S.json It Lt Ib Lb [--model out.json]
Prints SAT (embeddable, with a certificate) or UNSAT (no such B with these coordinate bounds).
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153

from twochain import decompose


def main() -> None:
    T = json.load(open(sys.argv[1]))
    It, Lt, Ib, Lb = map(int, sys.argv[2:6])
    model_out = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None
    N = len(T)
    Eset = [x for x in range(N) if T[x][x] == x]
    n = len(Eset)
    assert Eset == list(range(n)), "idempotents must be 0..n-1"
    A = list(range(n, N))
    sig = [0] * n + [1] * (N - n)
    dec = decompose([row[:n] for row in T[:n]])
    assert dec is not None, "E is not a 2-chain band"
    ct, cb = dec["ct"], dec["cb"]
    It0, Lt0, Ib0, Lb0 = dec["It"], dec["Lt"], dec["Ib"], dec["Lb"]
    assert It >= It0 and Lt >= Lt0 and Ib >= Ib0 and Lb >= Lb0
    top = set(dec["top"])

    pool = IDPool()
    cl: list[list[int]] = []

    def onehot(name, size):
        d = [pool.id((name, k)) for k in range(size)]
        cl.append(d[:])
        for a, b in itertools.combinations(d, 2):
            cl.append([-a, -b])
        return d

    # involutions g on the four coordinate sets
    def involution(name, size):
        g = [[pool.id((name, a, b)) for b in range(size)] for a in range(size)]
        for a in range(size):
            cl.append(g[a][:])
            for b1, b2 in itertools.combinations(range(size), 2):
                cl.append([-g[a][b1], -g[a][b2]])
            for b in range(size):
                cl.append([-g[a][b], g[b][a]])  # g(g(a)) = a
        return g

    gIt, gLt, gIb, gLb = (involution(nm, sz) for nm, sz in (("gIt", It), ("gLt", Lt), ("gIb", Ib), ("gLb", Lb)))
    # phi[(r,l)][i] one-hot over Ib ; psi[(r,l)][j] one-hot over Lb
    phi = {(r, l, i): [pool.id(("phi", r, l, i, k)) for k in range(Ib)] for r in range(It) for l in range(Lt) for i in range(Ib)}
    psi = {(r, l, j): [pool.id(("psi", r, l, j, k)) for k in range(Lb)] for r in range(It) for l in range(Lt) for j in range(Lb)}
    for d in list(phi.values()) + list(psi.values()):
        cl.append(d[:])
        for a, b in itertools.combinations(d, 2):
            cl.append([-a, -b])
    # (F): phi_(r,l2)(i) = phi_(r,l)(phi_(r2,l2)(i))
    for r, l, r2, l2 in itertools.product(range(It), range(Lt), range(It), range(Lt)):
        for i in range(Ib):
            for k in range(Ib):
                for m in range(Ib):
                    cl.append([-phi[(r2, l2, i)][k], -phi[(r, l, k)][m], phi[(r, l2, i)][m]])
    # (G): psi_(r,l2)(j) = psi_(r2,l2)(psi_(r,l)(j))
    for r, l, r2, l2 in itertools.product(range(It), range(Lt), range(It), range(Lt)):
        for j in range(Lb):
            for k in range(Lb):
                for m in range(Lb):
                    cl.append([-psi[(r, l, j)][k], -psi[(r2, l2, k)][m], psi[(r, l2, j)][m]])
    # equivariance: phi_(g r, g l)(g i) = g phi_(r,l)(i)
    for r, l, i in itertools.product(range(It), range(Lt), range(Ib)):
        for r2, l2, i2, k, k2 in itertools.product(range(It), range(Lt), range(Ib), range(Ib), range(Ib)):
            cl.append([-gIt[r][r2], -gLt[l][l2], -gIb[i][i2], -phi[(r, l, i)][k], -gIb[k][k2], phi[(r2, l2, i2)][k2]])
    for r, l, j in itertools.product(range(It), range(Lt), range(Lb)):
        for r2, l2, j2, k, k2 in itertools.product(range(It), range(Lt), range(Lb), range(Lb), range(Lb)):
            cl.append([-gIt[r][r2], -gLt[l][l2], -gLb[j][j2], -psi[(r, l, j)][k], -gLb[k][k2], psi[(r2, l2, j2)][k2]])
    # X homomorphism on E: phi on X-coordinates equals E's structure maps
    for (r, l), tup in dec["phi"].items():
        for i, v in enumerate(tup):
            cl.append([phi[(r, l, i)][v]])
    for (r, l), tup in dec["psi"].items():
        for j, v in enumerate(tup):
            cl.append([psi[(r, l, j)][v]])

    # symbolic elements of B: (level, row one-hot, col one-hot) where one-hot are lists of literals/consts
    def const(size, v):
        return [("c", k == v) for k in range(size)]

    def lits(vs):
        return [("v", x) for x in vs]

    def apply_perm(vec, g, size):
        out = onehot(("ap", len(cl)), size)
        for a in range(size):
            for b in range(size):
                cond = []
                kind, val = vec[a]
                if kind == "c":
                    if not val:
                        continue
                else:
                    cond.append(-val)
                cl.append(cond + [-g[a][b], out[b]])
        return lits(out)

    def X(e):
        if e in top:
            r, l = ct[e]
            return ("t", const(It, r), const(Lt, l))
        i, j = cb[e]
        return ("b", const(Ib, i), const(Lb, j))

    def gact(el):
        lev, R, C = el
        if lev == "t":
            return ("t", apply_perm(R, gIt, It), apply_perm(C, gLt, Lt))
        return ("b", apply_perm(R, gIb, Ib), apply_perm(C, gLb, Lb))

    def lookup(table, R, C, Z, size_out, size_z):
        """one-hot of table[(r,l,z)] where r~R, l~C, z~Z are symbolic one-hots."""
        out = onehot(("lk", len(cl)), size_out)
        for r in range(len(R)):
            for l in range(len(C)):
                for z in range(size_z):
                    cond = []
                    ok = True
                    for vec, idx in ((R, r), (C, l), (Z, z)):
                        kind, val = vec[idx]
                        if kind == "c":
                            if not val:
                                ok = False
                                break
                        else:
                            cond.append(-val)
                    if not ok:
                        continue
                    for k in range(size_out):
                        cl.append(cond + [-table[(r, l, z)][k], out[k]])
        return lits(out)

    def mul(a, b):
        la, Ra, Ca = a
        lb, Rb, Cb = b
        if la == "t" and lb == "t":
            return ("t", Ra, Cb)
        if la == "b" and lb == "b":
            return ("b", Ra, Cb)
        if la == "t":
            return ("b", lookup(phi, Ra, Ca, Rb, Ib, Ib), Cb)
        return ("b", Ra, lookup(psi, Rb, Cb, Ca, Lb, Lb))

    def equal(a, b):
        assert a[0] == b[0], "level mismatch"
        for va, vb in ((a[1], b[1]), (a[2], b[2])):
            for k in range(len(va)):
                (ka, xa), (kb, xb) = va[k], vb[k]
                # va[k] <-> vb[k]
                if ka == "c" and kb == "c":
                    if xa != xb:
                        cl.append([])  # contradiction
                elif ka == "c":
                    cl.append([xb] if xa else [-xb])
                elif kb == "c":
                    cl.append([xa] if xb else [-xa])
                else:
                    cl.append([-xa, xb])
                    cl.append([xa, -xb])

    inv = {s: next(t for t in A if T[T[s][t]][s] == s and T[T[t][s]][t] == t) for s in A}
    beta = {}
    for e in range(n):
        beta[e] = X(e)
    for s in A:
        sp = inv[s]
        beta[s] = mul(X(T[s][sp]), gact(X(T[sp][s])))
    for x in range(N):
        for y in range(N):
            rhs = beta[y] if sig[x] == 0 else gact(beta[y])
            equal(beta[T[x][y]], mul(beta[x], rhs))

    with Cadical153(bootstrap_with=cl) as solver:
        ok = solver.solve()
        print(f"{sys.argv[1]} It={It} Lt={Lt} Ib={Ib} Lb={Lb}: {'SAT (embeddable)' if ok else 'UNSAT'}  vars={pool.top} clauses={len(cl)}")
        if ok and model_out:
            mdl = set(v for v in solver.get_model() if v > 0)
            def perm(g, size):
                return [next(b for b in range(size) if g[a][b] in mdl) for a in range(size)]
            cert = dict(
                It=It, Lt=Lt, Ib=Ib, Lb=Lb,
                gIt=perm(gIt, It), gLt=perm(gLt, Lt), gIb=perm(gIb, Ib), gLb=perm(gLb, Lb),
                phi={f"{r},{l}": [next(k for k in range(Ib) if phi[(r, l, i)][k] in mdl) for i in range(Ib)] for r in range(It) for l in range(Lt)},
                psi={f"{r},{l}": [next(k for k in range(Lb) if psi[(r, l, j)][k] in mdl) for j in range(Lb)] for r in range(It) for l in range(Lt)},
            )
            json.dump(cert, open(model_out, "w"))


if __name__ == "__main__":
    main()
