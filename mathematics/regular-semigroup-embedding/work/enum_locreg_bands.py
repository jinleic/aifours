"""Enumerate (up to isomorphism) locally regular, non-regular bands of order n with at least
3 D-classes, by SAT with blocking clauses.  Output: JSON list of tables.

Usage: uv run --with python-sat python work/enum_locreg_bands.py n out.json [--max K]
"""
from __future__ import annotations

import itertools
import json
import sys

from pysat.solvers import Cadical153

from sat_small_band import build


def canon(T):
    n = len(T)
    best = None
    for p in itertools.permutations(range(n)):
        U = [[0] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                U[p[x]][p[y]] = p[T[x][y]]
        key = tuple(map(tuple, U))
        if best is None or key < best:
            best = key
    return best


def dclasses(T):
    n = len(T)
    seen, cls = set(), []
    for a in range(n):
        if a in seen:
            continue
        c = [b for b in range(n) if T[T[a][b]][a] == a and T[T[b][a]][b] == b]
        cls.append(c)
        seen.update(c)
    return cls


def main() -> None:
    n = int(sys.argv[1])
    out = sys.argv[2]
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 10**6
    P, cl = build(n)
    found = {}
    count = 0
    exhausted = False
    with Cadical153(bootstrap_with=cl) as s:
        while count < mx:
            if not s.solve():
                exhausted = True
                break
            m = set(v for v in s.get_model() if v > 0)
            T = [[next(z for z in range(n) if P[x, y, z] in m) for y in range(n)] for x in range(n)]
            count += 1
            s.add_clause([-P[x, y, T[x][y]] for x in range(n) for y in range(n)])
            if len(dclasses(T)) >= 3:
                key = canon(T)
                found.setdefault(key, [list(r) for r in key])
    res = list(found.values())
    json.dump(res, open(out, "w"))
    print(f"n={n}: {count} labelled locally-regular non-regular bands, exhausted={exhausted}; "
          f"{len(res)} iso classes with >=3 D-classes -> {out}")


if __name__ == "__main__":
    main()
