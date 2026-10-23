#!/usr/bin/env python3
"""Encoder Q0: balanced multiset E0 (all 8 columns (4,3,3,3,3,3)) split by quad graph G.

Lemma (README "E0 quad-graph split"): in E0 every row lies in <= 2 quads (row budget), two
quads share <= 1 row, n2 - n0 = 13 and 2 n0 + n1 = 6, so the quads are the dual of a simple
graph G on the 8 columns with max degree <= 4 and 13..16 edges (geng 8 13:16 -D4).
Rows: one per edge {a,b} (in Q_a and Q_b), 4-deg(a) private rows per column a, n0=|E|-13
rows in no quad. Symbol 0 of column a = Q_a (fixed); symbols 1..5 = the five triples.
Symmetry breaking (lex-leader, row-major reading order): value precedence of symbols 1..5
in every column; lex(row i) <= lex(row j) for consecutive rows with identical quad
membership (private rows of one column; the no-quad rows).
Leave: row r has exactly 2 - q(r) rows it never agrees with (q(r) = #quads containing r).
"""
import json
import sys

import encode_e1


def parse_graph6(g6):
    data = [ord(ch) - 63 for ch in g6.strip()]
    n = data[0]
    bits = []
    for d in data[1:]:
        for i in range(5, -1, -1):
            bits.append((d >> i) & 1)
    edges = []
    idx = 0
    for j in range(1, n):
        for i in range(j):
            if bits[idx]:
                edges.append((i, j))
            idx += 1
    return n, sorted(edges)


def skeleton(g6):
    n, edges = parse_graph6(g6)
    assert n == 8
    deg = [0] * n
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    assert max(deg) <= 4 and 13 <= len(edges) <= 16
    rows = []  # list of frozenset of quad columns
    for a, b in edges:
        rows.append((a, b))
    for a in range(n):
        for _ in range(4 - deg[a]):
            rows.append((a,))
    for _ in range(len(edges) - 13):
        rows.append(())
    assert len(rows) == 19
    return n, edges, rows


def build(spec):
    n, edges, rows = skeleton(spec["graph6"])
    N, k, q = 19, 8, 6
    F = encode_e1.CNF()
    X = [[[F.var(("x", r, c, s)) for s in range(q)] for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            F.add(list(X[r][c]))
            for s in range(q):
                for t in range(s + 1, q):
                    F.add([-X[r][c][s], -X[r][c][t]])
            F.add([X[r][c][0]] if c in rows[r] else [-X[r][c][0]])
    for c in range(k):
        for s in range(1, q):
            F.exactly([X[r][c][s] for r in range(N)], 3)
    M = {}
    for r in range(N):
        for r2 in range(r + 1, N):
            ys = []
            for c in range(k):
                y = F.new()
                ys.append(y)
                for s in range(q):
                    F.add([-X[r][c][s], -X[r2][c][s], y])
            for i in range(k):
                for j in range(i + 1, k):
                    F.add([-ys[i], -ys[j]])
            ms = []
            for c in range(k):
                for s in range(q):
                    m = F.new()
                    F.add([-m, X[r][c][s]])
                    F.add([-m, X[r2][c][s]])
                    ms.append(m)
            M[(r, r2)] = ms
    # leave: row r misses exactly 2 - q(r) rows
    Z = {}
    for (r, r2), ms in M.items():
        z = F.new()
        Z[(r, r2)] = z
        F.add([z] + ms)
    for r in range(N):
        zr = [Z[(min(r, r2), max(r, r2))] for r2 in range(N) if r2 != r]
        F.at_most(zr, 2 - len(rows[r]))
    F.at_most(list(Z.values()), 3)
    # value precedence on symbols 1..5
    for c in range(k):
        for s in range(1, q - 1):
            P = [F.new() for _ in range(N)]
            F.add([-P[0], X[0][c][s]])
            F.add([-X[0][c][s], P[0]])
            for r in range(1, N):
                F.add([-P[r - 1], P[r]])
                F.add([-X[r][c][s], P[r]])
                F.add([-P[r], P[r - 1], X[r][c][s]])
            F.add([-X[0][c][s + 1]])
            for r in range(1, N):
                F.add([-X[r][c][s + 1], P[r - 1]])
    # row lex among interchangeable rows (consecutive in the row order)
    nlex = 0
    for r in range(N - 1):
        r2 = r + 1
        if rows[r] != rows[r2] or len(rows[r]) == 2:
            continue
        nlex += 1
        E = [F.new() for _ in range(k - 1)]
        for c in range(k):
            guard = [] if c == 0 else [-E[c - 1]]
            for s in range(q):
                for t in range(s):
                    F.add(guard + [-X[r][c][s], -X[r2][c][t]])
            if c < k - 1:
                for s in range(q):
                    F.add(guard + [-X[r][c][s], -X[r2][c][s], E[c]])
    return F, X, {"edges": edges, "rows": [list(x) for x in rows], "row_lex_pairs": nlex}


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    F, X, info = build(spec)
    F.write(sys.argv[2])
    print(json.dumps({"vars": F.nv, "clauses": len(F.clauses), **info}))
