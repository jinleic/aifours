"""Implementation 1 (explicit incidence geometry of AG(2,q); stdlib only).

Finite facts used in review/PROOF_PARTIAL.md:
  (L) For every set F of 3 parallel classes ("free") of AG(2,7) and every other class c, decide whether c is LINEAR:
      for all distinct parallel lines L0, L1 of class c and all distinct q, q' in L1, the allowed sets
      A(q) = {p in L0 : the line pq has a class in F} satisfy |A(q)| = |F| and |A(q) & A(q')| <= 1.
      Expected: exactly 2 linear classes for every 3-set F; none for |F| = 4 or 5 (controls).
  (C) Single-cycle property: for every Latin square obtained from AG(2,7) by choosing ordered distinct classes
      (rows, columns, symbols) and every pair of symbols {a,b}, the cells with symbol a or b form ONE cycle under
      row- and column-pairing (connected graph on 2n cells).
Mutation controls: Z2xZ2 (n=4) and F3xF3 (n=9) Cayley squares must FAIL (C); a corrupted slope map must change (L).

python -B impl1_incidence.py --out ../evidence/impl1.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time

INF = "inf"


def classes(q):
    return list(range(q)) + [INF]


def direction(cl):
    return (0, 1) if cl == INF else (1, cl)


def line_through(q, p, cl):
    dx, dy = direction(cl)
    return frozenset(((p[0] + t * dx) % q, (p[1] + t * dy) % q) for t in range(q))


def all_lines(q, cl):
    pts = [(x, y) for x in range(q) for y in range(q)]
    seen, out = set(), []
    for p in pts:
        L = line_through(q, p, cl)
        if L not in seen:
            seen.add(L)
            out.append(L)
    return out


def class_of(q, p1, p2, corrupt=False):
    dx, dy = (p2[0] - p1[0]) % q, (p2[1] - p1[1]) % q
    if dx == 0:
        return INF
    s = dy * pow(dx, q - 2, q) % q
    if corrupt and s in (1, 2):      # MUTATION: swap two classes in the slope map
        s = 3 - s
    return s


def linear_class(q, F, c, corrupt=False):
    lines = all_lines(q, c)
    worst = 0
    for L0, L1 in itertools.permutations(lines, 2):
        A = {}
        for qq in L1:
            A[qq] = {p for p in L0 if class_of(q, p, qq, corrupt) in F}
            if len(A[qq]) != len(F):
                return False, "allowed set size %d != %d" % (len(A[qq]), len(F))
        for a, b in itertools.combinations(L1, 2):
            worst = max(worst, len(A[a] & A[b]))
    return worst <= 1, worst


def latin_from_classes(q, r, k, s):
    """L[i][j] = index of the s-line through (i-th r-line) & (j-th k-line)."""
    R, K, S = all_lines(q, r), all_lines(q, k), all_lines(q, s)
    sidx = {}
    for t, L in enumerate(S):
        for p in L:
            sidx[p] = t
    L = [[None] * q for _ in range(q)]
    for i, Li in enumerate(R):
        for j, Lj in enumerate(K):
            (p,) = tuple(Li & Lj)
            L[i][j] = sidx[p]
    return L


def single_cycle(L):
    n = len(L)
    for a, b in itertools.combinations(range(n), 2):
        cells = [(i, j) for i in range(n) for j in range(n) if L[i][j] in (a, b)]
        adj = {c: set() for c in cells}
        for c1, c2 in itertools.combinations(cells, 2):
            if c1[0] == c2[0] or c1[1] == c2[1]:
                adj[c1].add(c2)
                adj[c2].add(c1)
        seen, stack = {cells[0]}, [cells[0]]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) != len(cells):
            return False, (a, b, len(seen), len(cells))
    return True, None


def cayley_square(elements, op):
    idx = {e: t for t, e in enumerate(elements)}
    return [[idx[op(x, y)] for y in elements] for x in elements]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    q = 7
    cls = classes(q)
    out = {"implementation": "1 (explicit AG(2,7) incidence)", "python": sys.version.split()[0],
           "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    lin = {}
    for size in (3, 4, 5):
        rows = []
        for F in itertools.combinations(cls, size):
            res = {}
            for c in cls:
                if c in F:
                    continue
                ok, info = linear_class(q, set(F), c)
                res[str(c)] = ok
            rows.append({"F": [str(x) for x in F], "linear_classes": sorted(k for k, v in res.items() if v)})
        lin[size] = rows
    out["linear_by_F_size3"] = lin[3]
    out["count_linear_per_F_size3"] = sorted({len(r["linear_classes"]) for r in lin[3]})
    out["any_linear_size4"] = any(r["linear_classes"] for r in lin[4])
    out["any_linear_size5"] = any(r["linear_classes"] for r in lin[5])
    # mutation: corrupted slope map must break the "exactly 2" law for some F
    mut = []
    for F in itertools.combinations(cls, 3):
        cnt = sum(1 for c in cls if c not in F and linear_class(q, set(F), c, corrupt=True)[0])
        mut.append(cnt)
    out["mutation_corrupt_slope_counts"] = sorted(set(mut))
    # single-cycle property for all ordered triples of classes
    bad = []
    nsq = 0
    for r, k, s in itertools.permutations(cls, 3):
        L = latin_from_classes(q, r, k, s)
        nsq += 1
        ok, info = single_cycle(L)
        if not ok:
            bad.append([str(r), str(k), str(s), info])
    out["single_cycle_squares_checked"] = nsq
    out["single_cycle_failures"] = bad
    # mutation controls for the cycle checker
    z2z2 = [(u, v) for u in range(2) for v in range(2)]
    out["mutation_Z2xZ2_single_cycle"] = single_cycle(cayley_square(z2z2, lambda x, y: ((x[0] + y[0]) % 2, (x[1] + y[1]) % 2)))[0]
    f3f3 = [(u, v) for u in range(3) for v in range(3)]
    out["mutation_F3xF3_single_cycle"] = single_cycle(cayley_square(f3f3, lambda x, y: ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)))[0]
    out["control_Z7_single_cycle"] = single_cycle(cayley_square(list(range(7)), lambda x, y: (x + y) % 7))[0]
    out["secs"] = round(time.time() - t0, 2)
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps({k: out[k] for k in ("count_linear_per_F_size3", "any_linear_size4", "any_linear_size5",
                                          "mutation_corrupt_slope_counts", "single_cycle_squares_checked",
                                          "single_cycle_failures", "mutation_Z2xZ2_single_cycle",
                                          "mutation_F3xF3_single_cycle", "control_Z7_single_cycle", "secs")}))


if __name__ == "__main__":
    main()
