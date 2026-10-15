"""Enumerate Z2-graded E-unitary orthodox semigroups S = E u A with a FIXED band E (even part).

E is given as a JSON multiplication table on {0..n-1}; A = {n..n+m-1} is the odd part.
Grading: E*E, A*A -> E; E*A, A*E -> A.  Every element of A must have an inverse in A
(so S is regular, hence orthodox and E-unitary with S/sigma = Z2).
Solutions are deduplicated up to permutations of A combined with automorphisms of E.

Usage: uv run --with python-sat python work/enum_extensions.py E.json m out.json [--max K] [--feasible]
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def automorphisms(E):
    n = len(E)
    auts = []
    for p in itertools.permutations(range(n)):
        if all(p[E[x][y]] == E[p[x]][p[y]] for x in range(n) for y in range(n)):
            auts.append(p)
    return auts


def canon(T, n, m, auts):
    N = n + m
    best = None
    for a in auts:
        for q in itertools.permutations(range(m)):
            perm = list(a) + [n + qi for qi in q]
            inv = [0] * N
            for i, pi in enumerate(perm):
                inv[pi] = i
            # relabel: new table U[perm[x]][perm[y]] = perm[T[x][y]]
            U = [[0] * N for _ in range(N)]
            for x in range(N):
                for y in range(N):
                    U[perm[x]][perm[y]] = perm[T[x][y]]
            key = tuple(tuple(r) for r in U)
            if best is None or key < best:
                best = key
    return best


def main() -> None:
    E = json.load(open(sys.argv[1]))
    m = int(sys.argv[2])
    out = sys.argv[3]
    maxsol = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 10**9
    n = len(E)
    N = n + m
    Es = list(range(n))
    As = list(range(n, N))
    pool = IDPool()
    cl = []

    def tgt(x, y):
        return Es if (x < n) == (y < n) else As

    P = {}
    for x in range(N):
        for y in range(N):
            zs = tgt(x, y)
            for z in zs:
                P[x, y, z] = pool.id((x, y, z))
            cl.append([P[x, y, z] for z in zs])
            for z1, z2 in itertools.combinations(zs, 2):
                cl.append([-P[x, y, z1], -P[x, y, z2]])
    for x in Es:
        for y in Es:
            cl.append([P[x, y, E[x][y]]])
    for x, y, z in itertools.product(range(N), repeat=3):
        for u in tgt(x, y):
            for v in tgt(y, z):
                for w in tgt(u, z):
                    cl.append([-P[x, y, u], -P[y, z, v], -P[u, z, w], P[x, v, w]])
    for s in As:
        qs = []
        for t in As:
            q = pool.id(("Q", s, t))
            qs.append(q)
            r1 = [pool.id(("R1", s, t, u)) for u in Es]
            r2 = [pool.id(("R2", s, t, u)) for u in Es]
            cl.append([-q] + r1)
            cl.append([-q] + r2)
            for u, rv in zip(Es, r1):
                cl.append([-rv, P[s, t, u]])
                cl.append([-rv, P[u, s, s]])
            for u, rv in zip(Es, r2):
                cl.append([-rv, P[t, s, u]])
                cl.append([-rv, P[u, t, t]])
        cl.append(qs)
    if "--feasible" in sys.argv:
        with Cadical153(bootstrap_with=cl) as solver:
            print(f"E size {n}, m={m}: {'SAT (an extension exists)' if solver.solve() else 'UNSAT (no extension)'}")
        return
    auts = automorphisms(E)
    seen = {}
    exhausted = False
    with Cadical153(bootstrap_with=cl) as solver:
        count = 0
        while True:
            if count >= maxsol:
                break
            if not solver.solve():
                exhausted = True
                break
            model = set(v for v in solver.get_model() if v > 0)
            T = [[next(z for z in tgt(x, y) if P[x, y, z] in model) for y in range(N)] for x in range(N)]
            count += 1
            key = canon(T, n, m, auts)
            if key not in seen:
                seen[key] = [list(r) for r in key]
            # block this exact table (only the A-dependent part)
            block = [-P[x, y, T[x][y]] for x in range(N) for y in range(N) if not (x < n and y < n)]
            solver.add_clause(block)
    res = list(seen.values())
    json.dump(res, open(out, "w"))
    print(f"E size {n}, m={m}: {count} labelled solutions, {len(res)} up to isomorphism, exhausted={exhausted} -> {out}")


if __name__ == "__main__":
    main()
