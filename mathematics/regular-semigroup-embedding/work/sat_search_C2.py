"""SAT search: Z2-graded E-unitary orthodox semigroup violating the necessary condition (C2).

(C2) [proved in proof.md, Lemma 3]: if S embeds in a semidirect product B x| G of a band by a group,
then for s, s1 in S_g and t, t1 in S_{g^-1} with inverses s', s1*, t', t1* such that
    s s' = s1 s1*,   t' t = t1* t1,   (s' s)(t t') = (s1* s1)(t1 t1*),
we must have  s t = s1 t1.

S = E u A, E = {0..n-1} band (even part), A = {n..n+m-1} (odd part, no idempotents).
Optional: --locreg  forces E to be locally regular (a = eae  =>  a x e y a = a x a y a);
          --nonreg  forces E not regular.
Usage: uv run --with python-sat python work/sat_search_C2.py n m [--locreg] [--nonreg] [--fixE file]
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def main() -> None:
    n, m = int(sys.argv[1]), int(sys.argv[2])
    locreg = "--locreg" in sys.argv
    nonreg = "--nonreg" in sys.argv
    fixE = None
    if "--fixE" in sys.argv:
        fixE = json.load(open(sys.argv[sys.argv.index("--fixE") + 1]))
        assert len(fixE) == n
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
    # inverse relation Q[s,t]: t in V(s) (s,t in A)
    Q = {}
    for s in A:
        for t in A:
            q = pool.id(("Q", s, t))
            Q[s, t] = q
            # q <-> exists u: st=u and us=s ; and exists v: ts=v and vt=t
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
            # converse direction (so q is exact): (st=u & us=s & ts=v & vt=t) -> q
            for u in E:
                for v in E:
                    cl.append([-P[s, t, u], -P[u, s, s], -P[t, s, v], -P[v, t, t], q])
        cl.append([Q[s, t] for t in A])

    # (C2) violation with fixed roles: s=n, s1, t, t1, and inverses chosen freely (selector vars)
    roles = ["s", "s1", "t", "t1", "sp", "s1p", "tp", "t1p"]
    R = {r: {a: pool.id(("role", r, a)) for a in A} for r in roles}
    for r in roles:
        cl.append(list(R[r].values()))
        for a1, a2 in itertools.combinations(A, 2):
            cl.append([-R[r][a1], -R[r][a2]])
    cl.append([R["s"][n]])  # symmetry breaking

    def inv(r, rp):
        for a in A:
            for b in A:
                cl.append([-R[r][a], -R[rp][b], Q[a, b]])

    inv("s", "sp")
    inv("s1", "s1p")
    inv("t", "tp")
    inv("t1", "t1p")

    def prod(name, lv, rv, out_part):
        out = {w: pool.id(("V", name, w)) for w in out_part}
        cl.append(list(out.values()))
        for w1, w2 in itertools.combinations(out_part, 2):
            cl.append([-out[w1], -out[w2]])
        for a, va in lv.items():
            for b, vb in rv.items():
                for w in out_part:
                    if (a, b, w) in P:
                        cl.append([-va, -vb, -P[a, b, w], out[w]])
        return out

    ssp = prod("ssp", R["s"], R["sp"], E)
    s1s1p = prod("s1s1p", R["s1"], R["s1p"], E)
    tpt = prod("tpt", R["tp"], R["t"], E)
    t1pt1 = prod("t1pt1", R["t1p"], R["t1"], E)
    sps = prod("sps", R["sp"], R["s"], E)
    ttp = prod("ttp", R["t"], R["tp"], E)
    s1ps1 = prod("s1ps1", R["s1p"], R["s1"], E)
    t1t1p = prod("t1t1p", R["t1"], R["t1p"], E)
    k = prod("k", sps, ttp, E)
    k1 = prod("k1", s1ps1, t1t1p, E)
    st = prod("st", R["s"], R["t"], E)
    s1t1 = prod("s1t1", R["s1"], R["t1"], E)
    for w in E:
        cl.append([-ssp[w], s1s1p[w]])
        cl.append([-tpt[w], t1pt1[w]])
        cl.append([-k[w], k1[w]])
        cl.append([-st[w], -s1t1[w]])

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
        print(f"n={n} m={m} locreg={locreg} nonreg={nonreg} fixE={fixE is not None}: {'SAT' if ok else 'UNSAT'}")
        if ok:
            model = set(v for v in solver.get_model() if v > 0)
            table = [[next(z for z in tgt(x, y) if P[x, y, z] in model) for y in range(N)] for x in range(N)]
            rolev = {r: next(a for a in A if R[r][a] in model) for r in roles}
            print("roles:", rolev)
            print("table:", json.dumps(table))


if __name__ == "__main__":
    main()
