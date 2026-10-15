"""SAT search for a Z2-graded E-unitary orthodox semigroup violating a free-band walk identity.

S = E u A, E = {0..n-1} (even part, must be a band), A = {n..n+m-1} (odd part).
Grading: E*E, A*A -> E ;  E*A, A*E -> A.  Then S is E-unitary orthodox with S/sigma = Z2
as soon as S is associative, E is a band and every element of A has an inverse in A.

Target violation (I1):  for s, r, t in A,   (st)(rt)(st)r != (st)r.
Rationale: in the derived category of S -> Z2 the arrows a=(1,s), b=(g,t), c=(1,r) satisfy that
the walks abc and abcbabc are equal in the free band on {a,b,c}; any embedding of S into a
semidirect product (band x| group) would force s t r = s t r t s t r, i.e. (I1) with equality.

Usage: uv run --with python-sat python work/sat_search_I1.py n m pattern [--nonregular]
  pattern: 'distinct' (t distinct from s,r), 't=s', 't=r'
"""
from __future__ import annotations

import itertools
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def main() -> None:
    n, m = int(sys.argv[1]), int(sys.argv[2])
    pattern = sys.argv[3] if len(sys.argv) > 3 else "distinct"
    nonregular = "--nonregular" in sys.argv
    N = n + m
    Eset = list(range(n))
    Aset = list(range(n, N))
    pool = IDPool()
    clauses = []

    def part(x):
        return 0 if x < n else 1

    def target(x, y):
        return Eset if part(x) == part(y) else Aset

    P = {}
    for x in range(N):
        for y in range(N):
            for z in target(x, y):
                P[x, y, z] = pool.id(("P", x, y, z))
            zs = target(x, y)
            clauses.append([P[x, y, z] for z in zs])
            for z1, z2 in itertools.combinations(zs, 2):
                clauses.append([-P[x, y, z1], -P[x, y, z2]])
    for e in Eset:
        clauses.append([P[e, e, e]])
    # associativity
    for x, y, z in itertools.product(range(N), repeat=3):
        for u in target(x, y):
            for v in target(y, z):
                for w in target(u, z):
                    # (xy)z = w  <->  x(yz) = w
                    clauses.append([-P[x, y, u], -P[y, z, v], -P[u, z, w], P[x, v, w]])
    # regularity of odd elements
    for s in Aset:
        qs = []
        for t in Aset:
            q = pool.id(("Q", s, t))
            qs.append(q)
            # s t s = s
            r1 = [pool.id(("R1", s, t, u)) for u in Eset]
            clauses.append([-q] + r1)
            for u, rv in zip(Eset, r1):
                clauses.append([-rv, P[s, t, u]])
                clauses.append([-rv, P[u, s, s]])
            # t s t = t
            r2 = [pool.id(("R2", s, t, u)) for u in Eset]
            clauses.append([-q] + r2)
            for u, rv in zip(Eset, r2):
                clauses.append([-rv, P[t, s, u]])
                clauses.append([-rv, P[u, t, t]])
        clauses.append(qs)

    # violation of (I1) for a fixed triple
    s0, r0 = n, n + 1
    t0 = {"distinct": n + 2, "t=s": n, "t=r": n + 1}[pattern]
    assert max(s0, r0, t0) < N, "m too small for pattern"

    def val(name, part_elems):
        return {z: pool.id(("V", name, z)) for z in part_elems}

    def exactly_one(vs):
        clauses.append(list(vs.values()))
        for a, b in itertools.combinations(list(vs.values()), 2):
            clauses.append([-a, -b])

    def product(name, left, right):
        """left/right: dict elem->var (value one-hot); returns one-hot dict of product."""
        lp = 0 if min(left) < n else 1
        rp = 0 if min(right) < n else 1
        out_elems = Eset if lp == rp else Aset
        out = val(name, out_elems)
        exactly_one(out)
        for x, vx in left.items():
            for y, vy in right.items():
                for w in out_elems:
                    clauses.append([-vx, -vy, -P[x, y, w], out[w]])
        return out

    def const(name, x):
        d = val(name, Aset if x >= n else Eset)
        exactly_one(d)
        clauses.append([d[x]])
        return d

    S_, T_, R_ = const("s", s0), const("t", t0), const("r", r0)
    e = product("e", S_, T_)
    f = product("f", R_, T_)
    ef = product("ef", e, f)
    efe = product("efe", ef, e)
    lhs = product("lhs", efe, R_)
    rhs = product("rhs", e, R_)
    for z in Aset:
        clauses.append([-lhs[z], -rhs[z]])

    if nonregular:
        # exists a,x,y in E with a x y a != a x a y a
        sel = {(a, x, y): pool.id(("NR", a, x, y)) for a, x, y in itertools.product(Eset, repeat=3)}
        clauses.append(list(sel.values()))
        for (a, x, y), sv in sel.items():
            # compute both sides with one-hot vars conditioned on sv
            A_ = {a: pool.id(("na", a, x, y))}
            # simple direct encoding: auxiliary vars for products
            ax = {w: pool.id(("ax", a, x, y, w)) for w in Eset}
            axy = {w: pool.id(("axy", a, x, y, w)) for w in Eset}
            L = {w: pool.id(("L", a, x, y, w)) for w in Eset}
            axa = {w: pool.id(("axa", a, x, y, w)) for w in Eset}
            axay = {w: pool.id(("axay", a, x, y, w)) for w in Eset}
            R = {w: pool.id(("R", a, x, y, w)) for w in Eset}
            for w in Eset:
                clauses.append([-sv, -P[a, x, w], ax[w]])
                for u in Eset:
                    clauses.append([-sv, -ax[u], -P[u, y, w], axy[w]])
                    clauses.append([-sv, -axy[u], -P[u, a, w], L[w]])
                    clauses.append([-sv, -ax[u], -P[u, a, w], axa[w]])
                    clauses.append([-sv, -axa[u], -P[u, y, w], axay[w]])
                    clauses.append([-sv, -axay[u], -P[u, a, w], R[w]])
            for w in Eset:
                clauses.append([-sv, -L[w], -R[w]])
            del A_

    with Cadical153(bootstrap_with=clauses) as solver:
        ok = solver.solve()
        print(f"n={n} m={m} pattern={pattern} nonregular={nonregular}: {'SAT' if ok else 'UNSAT'}")
        if ok:
            model = set(v for v in solver.get_model() if v > 0)
            table = [[None] * N for _ in range(N)]
            for (x, y, z), v in P.items():
                if v in model:
                    table[x][y] = z
            print("table (row x, col y -> xy):")
            for x in range(N):
                print(" ".join(str(table[x][y]) for y in range(N)))


if __name__ == "__main__":
    main()
