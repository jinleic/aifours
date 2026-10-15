"""SAT search for the smallest band that is locally regular (every eBe regular) but not regular.

Locally regular:  for all a, e with a = eae, and all x, y:  a x e y a = a x a y a.
Not regular:      exists a, x, y with a x y a != a x a y a.

Usage: uv run --with python-sat python work/sat_small_band.py n [--all]
Prints the multiplication table of a solution (rows x, columns y, entry xy) or UNSAT.
"""
from __future__ import annotations

import itertools
import sys

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def build(n: int):
    pool = IDPool()
    cl = []
    P = {(x, y, z): pool.id(("P", x, y, z)) for x in range(n) for y in range(n) for z in range(n)}
    for x in range(n):
        for y in range(n):
            cl.append([P[x, y, z] for z in range(n)])
            for z1, z2 in itertools.combinations(range(n), 2):
                cl.append([-P[x, y, z1], -P[x, y, z2]])
        cl.append([P[x, x, x]])
    for x, y, z in itertools.product(range(n), repeat=3):
        for u in range(n):
            for v in range(n):
                for w in range(n):
                    cl.append([-P[x, y, u], -P[y, z, v], -P[u, z, w], P[x, v, w]])

    def chain(tag, word, guard):
        """one-hot value vars of the product of the fixed elements in `word`, active under guard."""
        cur = {word[0]: None}
        prev_vars = None
        prev_elem = word[0]
        for k, nxt in enumerate(word[1:]):
            out = {w: pool.id((tag, k, w)) for w in range(n)}
            if k == 0:
                for w in range(n):
                    cl.append(guard + [-P[prev_elem, nxt, w], out[w]])
            else:
                for u in range(n):
                    for w in range(n):
                        cl.append(guard + [-prev_vars[u], -P[u, nxt, w], out[w]])
            prev_vars = out
        return prev_vars

    # locally regular: for a,e,x,y with ea=a, ae=a  ->  a x e y a = a x a y a
    for a, e, x, y in itertools.product(range(n), repeat=4):
        if a == e:
            continue  # trivial
        guard = [-P[e, a, a], -P[a, e, a]]
        L = chain(("LR_L", a, e, x, y), (a, x, e, y, a), guard)
        R = chain(("LR_R", a, e, x, y), (a, x, a, y, a), guard)
        # under guard the true values must agree: forbid differing pairs
        for w1 in range(n):
            for w2 in range(n):
                if w1 != w2:
                    cl.append(guard + [-L[w1], -R[w2]])
    # not regular
    sel = []
    for a, x, y in itertools.product(range(n), repeat=3):
        s = pool.id(("NR", a, x, y))
        sel.append(s)
        L = chain(("NR_L", a, x, y), (a, x, y, a), [-s])
        R = chain(("NR_R", a, x, y), (a, x, a, y, a), [-s])
        for w in range(n):
            cl.append([-s, -L[w], -R[w]])
    cl.append(sel)
    return P, cl


def main() -> None:
    n = int(sys.argv[1])
    P, cl = build(n)
    with Cadical153(bootstrap_with=cl) as s:
        ok = s.solve()
        print(f"n={n}: {'SAT' if ok else 'UNSAT'}")
        if ok:
            model = set(v for v in s.get_model() if v > 0)
            for x in range(n):
                print(" ".join(str(next(z for z in range(n) if P[x, y, z] in model)) for y in range(n)))


if __name__ == "__main__":
    main()
