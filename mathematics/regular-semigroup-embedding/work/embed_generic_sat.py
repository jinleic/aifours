"""Generic SAT test: does a Z2-graded E-unitary orthodox semigroup S embed in B x| Z2 for SOME band B
of order k (optionally required to be locally regular)?

Unknowns: band table of B (order k), an involutive automorphism tau of B, a map beta : S -> B,
injective on each sigma-class, with beta(xy) = beta(x) . tau^{sigma(x)}(beta(y)) for all x, y
(sigma = parity); then x -> (beta(x), sigma(x)) embeds S in B x| Z2.
SAT gives an explicit embedding (certificate).  UNSAT only says: no such B of order k.

Usage: uv run --with python-sat python work/embed_generic_sat.py S.json k [--locreg]
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def main() -> None:
    T = json.load(open(sys.argv[1]))
    k = int(sys.argv[2])
    locreg = "--locreg" in sys.argv
    N = len(T)
    n = sum(1 for x in range(N) if T[x][x] == x)
    sig = [0 if x < n else 1 for x in range(N)]
    pool = IDPool()
    cl = []
    P = {(x, y, z): pool.id(("P", x, y, z)) for x in range(k) for y in range(k) for z in range(k)}
    for x in range(k):
        for y in range(k):
            cl.append([P[x, y, z] for z in range(k)])
            for z1, z2 in itertools.combinations(range(k), 2):
                cl.append([-P[x, y, z1], -P[x, y, z2]])
        cl.append([P[x, x, x]])
    for x, y, z in itertools.product(range(k), repeat=3):
        for u in range(k):
            for v in range(k):
                for w in range(k):
                    cl.append([-P[x, y, u], -P[y, z, v], -P[u, z, w], P[x, v, w]])
    tau = {(x, y): pool.id(("tau", x, y)) for x in range(k) for y in range(k)}
    for x in range(k):
        cl.append([tau[x, y] for y in range(k)])
        for y1, y2 in itertools.combinations(range(k), 2):
            cl.append([-tau[x, y1], -tau[x, y2]])
        for y in range(k):
            cl.append([-tau[x, y], tau[y, x]])
    # automorphism: P[x,y,z] & tau(x)=a & tau(y)=b & tau(z)=c -> P[a,b,c]
    for x, y, z in itertools.product(range(k), repeat=3):
        for a, b, c in itertools.product(range(k), repeat=3):
            cl.append([-P[x, y, z], -tau[x, a], -tau[y, b], -tau[z, c], P[a, b, c]])
    beta = {(s, x): pool.id(("beta", s, x)) for s in range(N) for x in range(k)}
    for s in range(N):
        cl.append([beta[s, x] for x in range(k)])
        for x1, x2 in itertools.combinations(range(k), 2):
            cl.append([-beta[s, x1], -beta[s, x2]])
    # x -> (beta(x), sigma(x)) must be injective: beta injective on each sigma-class only
    for s1, s2 in itertools.combinations(range(N), 2):
        if sig[s1] != sig[s2]:
            continue
        for x in range(k):
            cl.append([-beta[s1, x], -beta[s2, x]])
    # homomorphism conditions
    for s in range(N):
        for t in range(N):
            st = T[s][t]
            for a in range(k):
                for b in range(k):
                    if sig[s] == 0:
                        for c in range(k):
                            cl.append([-beta[s, a], -beta[t, b], -P[a, b, c], beta[st, c]])
                    else:
                        for b2 in range(k):
                            for c in range(k):
                                cl.append([-beta[s, a], -beta[t, b], -tau[b, b2], -P[a, b2, c], beta[st, c]])
    if locreg:
        # for all a <= e (ea = a, ae = a) and all x,y: a x e y a = a x a y a, via aux one-hot chains
        def chain(tag, word, guard):
            prev = None
            for kk, nxt in enumerate(word[1:]):
                out = {w: pool.id((tag, kk, w)) for w in range(k)}
                if kk == 0:
                    for w in range(k):
                        cl.append(guard + [-P[word[0], nxt, w], out[w]])
                else:
                    for u in range(k):
                        for w in range(k):
                            cl.append(guard + [-prev[u], -P[u, nxt, w], out[w]])
                prev = out
            return prev
        for a, e, x, y in itertools.product(range(k), repeat=4):
            if a == e:
                continue
            guard = [-P[e, a, a], -P[a, e, a]]
            L = chain(("LR_L", a, e, x, y), (a, x, e, y, a), guard)
            R = chain(("LR_R", a, e, x, y), (a, x, a, y, a), guard)
            for w1 in range(k):
                for w2 in range(k):
                    if w1 != w2:
                        cl.append(guard + [-L[w1], -R[w2]])
    with Cadical153(bootstrap_with=cl) as solver:
        ok = solver.solve()
        print(f"{sys.argv[1]} k={k} locreg={locreg}: {'SAT (embeds)' if ok else 'UNSAT (no band of this order)'}")
        if ok:
            m = set(v for v in solver.get_model() if v > 0)
            B = [[next(z for z in range(k) if P[x, y, z] in m) for y in range(k)] for x in range(k)]
            tv = [next(y for y in range(k) if tau[x, y] in m) for x in range(k)]
            bv = [next(x for x in range(k) if beta[s, x] in m) for s in range(N)]
            print("B:", json.dumps(B))
            print("tau:", tv, "beta:", bv)


if __name__ == "__main__":
    main()
