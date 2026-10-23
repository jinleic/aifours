#!/usr/bin/env python3
"""Independent encoder Q0B (method M2) for the E0 quad-graph split; written separately
from encode_e1/encode_q0 and sharing no code with them.

Same mathematical case (graph G from geng, quads fixed), different CNF:
  * cell variables v(r,c,s) = 1 + 48 r + 6 c + s;
  * column-pair definition: for columns c1<c2, symbols (a,b) and rows r<r' the 4-clause
    -v(r,c1,a) | -v(r,c2,b) | -v(r',c1,a) | -v(r',c2,b);
  * each triple symbol 1..5 at most 3 times per column by binomial 4-subset clauses (with
    15 non-quad rows and one symbol each this forces exactly 3);
  * leave (mathematical fact: a row in t quads agrees with exactly 16+t others, so it misses
    2-t rows): for each row pair not sharing a quad, a "miss" variable u or an agreement
    witness a(r,r',c,s) -> v(r,c,s) & v(r',c,s); u forced false if either row has t=2;
    per row at most 2-t misses and at most 3 misses in total, by binomial clauses;
  * symmetry: for each column c choose the other column d maximizing |Q_d minus Q_c| (ties:
    smallest d); those rows pairwise agree in d, so they lie in distinct triples of c and
    are labeled 1,2,3(,4) in increasing row order (pure relabeling of triples of column c).
  No row symmetry breaking and no per-row budget constraints.
"""
import itertools
import json
import sys


def g6_edges(g6):
    d = [ord(ch) - 63 for ch in g6.strip()]
    n = d[0]
    bits = [(x >> i) & 1 for x in d[1:] for i in range(5, -1, -1)]
    out, idx = [], 0
    for j in range(1, n):
        for i in range(j):
            if bits[idx]:
                out.append((i, j))
            idx += 1
    return n, out


def main():
    g6, out = sys.argv[1], sys.argv[2]
    n, edges = g6_edges(g6)
    deg = [sum(1 for e in edges if a in e) for a in range(n)]
    member = []  # member[r] = set of quad columns of row r
    for a, b in sorted(edges):
        member.append({a, b})
    for a in range(n):
        member += [{a} for _ in range(4 - deg[a])]
    member += [set() for _ in range(len(edges) - 13)]
    assert len(member) == 19 and n == 8
    R, C, S = 19, 8, 6
    v = lambda r, c, s: 1 + 48 * r + 6 * c + s  # noqa: E731
    cl = []
    for r in range(R):
        for c in range(C):
            if c in member[r]:
                cl.append([v(r, c, 0)])
            else:
                cl.append([-v(r, c, 0)])
            cl.append([v(r, c, s) for s in range(S)])
            for s, t in itertools.combinations(range(S), 2):
                cl.append([-v(r, c, s), -v(r, c, t)])
    for c1, c2 in itertools.combinations(range(C), 2):
        for a in range(S):
            for b in range(S):
                for r, r2 in itertools.combinations(range(R), 2):
                    cl.append([-v(r, c1, a), -v(r, c2, b), -v(r2, c1, a), -v(r2, c2, b)])
    for c in range(C):
        for s in range(1, S):
            for quad in itertools.combinations(range(R), 4):
                cl.append([-v(r, c, s) for r in quad])
    fixed = {}
    for c in range(C):
        Qc = {r for r in range(R) if c in member[r]}
        best = None
        for d in range(C):
            if d == c:
                continue
            Qd = [r for r in range(R) if d in member[r] and r not in Qc]
            if best is None or len(Qd) > len(best[1]):
                best = (d, Qd)
        for lab, r in enumerate(sorted(best[1]), start=1):
            cl.append([v(r, c, lab)])
        fixed[c] = {"d": best[0], "rows": sorted(best[1])}
    # leave constraints (aux variables numbered after the cell variables)
    nv = R * C * S
    miss = {}
    for r, r2 in itertools.combinations(range(R), 2):
        if member[r] & member[r2]:
            continue  # already agree in a shared quad column
        wit = []
        for c in range(C):
            if c in member[r] or c in member[r2]:
                continue
            for s in range(1, S):
                nv += 1
                cl.append([-nv, v(r, c, s)])
                cl.append([-nv, v(r2, c, s)])
                wit.append(nv)
        if len(member[r]) == 2 or len(member[r2]) == 2:
            cl.append(wit)
        else:
            nv += 1
            miss[(r, r2)] = nv
            cl.append(wit + [nv])
    for r in range(R):
        mine = [u for (a, b), u in miss.items() if r in (a, b)]
        cap = 2 - len(member[r])
        for sub in itertools.combinations(mine, cap + 1):
            cl.append([-u for u in sub])
    for sub in itertools.combinations(sorted(miss.values()), 4):
        cl.append([-u for u in sub])
    with open(out, "w") as f:
        f.write("p cnf %d %d\n" % (nv, len(cl)))
        for c_ in cl:
            f.write(" ".join(map(str, c_)) + " 0\n")
    print(json.dumps({"vars": nv, "clauses": len(cl), "miss_vars": len(miss), "fixed": fixed}))


if __name__ == "__main__":
    main()
