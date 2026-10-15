"""SAT search: Z2-graded E-unitary orthodox semigroup violating necessary condition (C3).

(C3) [proof.md, Lemma 4]: if S embeds in a semidirect product of a band by a group, then for
s, t in the same sigma-class with inverses s', t' such that s's D t't in E (q := t't, p := s's),
    q (t' s) q = q      and      q (s' t) q = q.
(Equivalently: t f t' = (tt') s f s' (tt') for all f in qEq.)

Usage: uv run --with python-sat python work/sat_search_C3.py n m [--fixE E.json] [--locreg] [--nonreg]
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def main() -> None:
    n, m = int(sys.argv[1]), int(sys.argv[2])
    fixE = json.load(open(sys.argv[sys.argv.index("--fixE") + 1])) if "--fixE" in sys.argv else None
    locreg = "--locreg" in sys.argv
    nonreg = "--nonreg" in sys.argv
    N = n + m
    E = list(range(n))
    A = list(range(n, N))
    pool = IDPool()
    cl: list[list[int]] = []

    def tgt(x, y):
        return E if (x < n) == (y < n) else A

    P = {}
    for x in range(N):
        for y in range(N):
            zs = tgt(x, y)
            for z in zs:
                P[x, y, z] = pool.id(("P", x, y, z))
            cl.append([P[x, y, z] for z in zs])
            for z1, z2 in itertools.combinations(zs, 2):
                cl.append([-P[x, y, z1], -P[x, y, z2]])
    for e in E:
        cl.append([P[e, e, e]])
    if fixE is not None:
        for x in E:
            for y in E:
                cl.append([P[x, y, fixE[x][y]]])
    for x, y, z in itertools.product(range(N), repeat=3):
        for u in tgt(x, y):
            for v in tgt(y, z):
                for w in tgt(u, z):
                    cl.append([-P[x, y, u], -P[y, z, v], -P[u, z, w], P[x, v, w]])
    Q = {}
    for s in A:
        for t in A:
            q = pool.id(("Q", s, t))
            Q[s, t] = q
            r1 = [pool.id(("R1", s, t, u)) for u in E]
            r2 = [pool.id(("R2", s, t, u)) for u in E]
            cl.append([-q] + r1)
            cl.append([-q] + r2)
            for u, rv in zip(E, r1):
                cl.append([-rv, P[s, t, u]])
                cl.append([-rv, P[u, s, s]])
            for u, rv in zip(E, r2):
                cl.append([-rv, P[t, s, u]])
                cl.append([-rv, P[u, t, t]])
        cl.append([Q[s, t] for t in A])

    roles = ["s", "t", "sp", "tp"]
    R = {r: {a: pool.id(("role", r, a)) for a in A} for r in roles}
    for r in roles:
        cl.append(list(R[r].values()))
        for a1, a2 in itertools.combinations(A, 2):
            cl.append([-R[r][a1], -R[r][a2]])
    cl.append([R["s"][n]])
    for r, rp in (("s", "sp"), ("t", "tp")):
        for a in A:
            for b in A:
                cl.append([-R[r][a], -R[rp][b], Q[a, b]])

    def onehot(name, part):
        d = {w: pool.id(("V", name, w)) for w in part}
        cl.append(list(d.values()))
        for w1, w2 in itertools.combinations(part, 2):
            cl.append([-d[w1], -d[w2]])
        return d

    def prod(name, lv, rv):
        lp = min(lv) < n
        rp = min(rv) < n
        part = E if lp == rp else A
        out = onehot(name, part)
        for a, va in lv.items():
            for b, vb in rv.items():
                for w in part:
                    cl.append([-va, -vb, -P[a, b, w], out[w]])
        return out

    p = prod("p", R["sp"], R["s"])  # s's
    q = prod("q", R["tp"], R["t"])  # t't
    # p D q in E:  pqp = p and qpq = q
    pq = prod("pq", p, q)
    pqp = prod("pqp", pq, p)
    qp = prod("qp", q, p)
    qpq = prod("qpq", qp, q)
    for w in E:
        cl.append([-pqp[w], p[w]])
        cl.append([-qpq[w], q[w]])
    tps = prod("tps", R["tp"], R["s"])  # t's
    spt = prod("spt", R["sp"], R["t"])  # s't
    v1 = prod("v1", prod("qtps", q, tps), q)
    v2 = prod("v2", prod("qspt", q, spt), q)
    # violation: v1 != q or v2 != q
    sel1, sel2 = pool.id("sel1"), pool.id("sel2")
    cl.append([sel1, sel2])
    for w in E:
        cl.append([-sel1, -v1[w], -q[w]])
        cl.append([-sel2, -v2[w], -q[w]])

    def chain_guarded(tag, word, guard):
        prev = None
        for kk, nxt in enumerate(word[1:]):
            out = {w: pool.id((tag, kk, w)) for w in E}
            if kk == 0:
                for w in E:
                    cl.append(guard + [-P[word[0], nxt, w], out[w]])
            else:
                for u in E:
                    for w in E:
                        cl.append(guard + [-prev[u], -P[u, nxt, w], out[w]])
            prev = out
        return prev

    if locreg and fixE is None:
        for a, e, x, y in itertools.product(E, repeat=4):
            if a == e:
                continue
            guard = [-P[e, a, a], -P[a, e, a]]
            L = chain_guarded(("LR_L", a, e, x, y), (a, x, e, y, a), guard)
            Rr = chain_guarded(("LR_R", a, e, x, y), (a, x, a, y, a), guard)
            for w1 in E:
                for w2 in E:
                    if w1 != w2:
                        cl.append(guard + [-L[w1], -Rr[w2]])
    if nonreg and fixE is None:
        sel = []
        for a, x, y in itertools.product(E, repeat=3):
            sv = pool.id(("NR", a, x, y))
            sel.append(sv)
            L = chain_guarded(("NR_L", a, x, y), (a, x, y, a), [-sv])
            Rr = chain_guarded(("NR_R", a, x, y), (a, x, a, y, a), [-sv])
            for w in E:
                cl.append([-sv, -L[w], -Rr[w]])
        cl.append(sel)

    with Cadical153(bootstrap_with=cl) as solver:
        ok = solver.solve()
        print(f"n={n} m={m} fixE={fixE is not None} locreg={locreg} nonreg={nonreg}: {'SAT' if ok else 'UNSAT'}")
        if ok:
            model = set(v for v in solver.get_model() if v > 0)
            table = [[next(z for z in tgt(x, y) if P[x, y, z] in model) for y in range(N)] for x in range(N)]
            print("roles:", {r: next(a for a in A if R[r][a] in model) for r in roles})
            print("table:", json.dumps(table))


if __name__ == "__main__":
    main()
