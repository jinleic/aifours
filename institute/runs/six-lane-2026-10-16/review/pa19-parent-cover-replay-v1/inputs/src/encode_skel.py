#!/usr/bin/env python3
"""Encoder SKEL (Amendment A2): one P0-quad skeleton of a non-balanced multiset.

Columns 0..c0-1 = P0 columns (skeleton vertices; symbol 0 = quad, fixed), columns c0..7 =
special columns (profile labels sorted by count, exact counts, free). Rows ordered: |T|=2
rows (skeleton edges), hyperedge rows, private rows by vertex, rows with T empty.
Constraints: EO cells; quad cells fixed; P0 triple symbols 1..5 exactly 3 each; special
column exact counts; AGR/AMO agreements; ROW budget sum_c (n-1) in [18-L, 18]; COVER at most
L row pairs with no agreement; value precedence (P0 symbols 1..5; equal-count special labels);
lex(row) for consecutive rows with identical T; lex(column) for consecutive special columns
with identical profile. All breaking constraints are lex-leader for one row-major order.
"""
import encode_e1


def rows_of(c0, skel, N=19):
    rows = [tuple(e) for e in skel["edges"]] + [tuple(h) for h in skel["hyper"]]
    deg = [0] * c0
    for t in rows:
        for v in t:
            deg[v] += 1
    for v in range(c0):
        rows += [(v,)] * (4 - deg[v])
    rows += [()] * skel["empty"]
    assert len(rows) == N, len(rows)
    return rows


def build(spec):
    c0, skel, special = spec["c0"], spec["skeleton"], [list(p) for p in spec["special"]]
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    bq = spec.get("base_quad", True)  # False: 18-row control variant, base profile (3^q)
    profs = ([[4] + [3] * (q - 1)] if bq else [[3] * q]) * c0 + special
    assert len(profs) == k and sum(profs[0]) == N
    rows = rows_of(c0, skel, N) if bq else [()] * N
    F = encode_e1.CNF()
    X = [[[F.var(("x", r, c, s)) for s in range(q)] for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            F.add(list(X[r][c]))
            for s in range(q):
                for t in range(s + 1, q):
                    F.add([-X[r][c][s], -X[r][c][t]])
            if c < c0 and bq:
                F.add([X[r][c][0]] if c in rows[r] else [-X[r][c][0]])
    for c in range(k):
        for s in range(q):
            if c < c0 and s == 0 and bq:
                continue
            F.exactly([X[r][c][s] for r in range(N)], profs[c][s])
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
    kap = sum(n * (n - 1) // 2 for p in profs for n in p)
    L = N * (N - 1) // 2 - kap
    assert L == spec["L"]
    wmax = [max(p) - 1 for p in profs]
    for r in range(N):
        F.weighted_at_most([[(X[r][c][s], profs[c][s] - 1) for s in range(q)] for c in range(k)], N - 1)
        F.weighted_at_most([[(X[r][c][s], wmax[c] - (profs[c][s] - 1)) for s in range(q)]
                            for c in range(k)], sum(wmax) - (N - 1 - L))
    zs = []
    for r in range(N):
        for r2 in range(r + 1, N):
            z = F.new()
            zs.append(z)
            cl = [z]
            for c in range(k):
                for s in range(q):
                    m = F.new()
                    F.add([-m, X[r][c][s]])
                    F.add([-m, X[r2][c][s]])
                    cl.append(m)
            F.add(cl)
    F.at_most(zs, L)
    # value precedence
    for c in range(k):
        for s in range(q - 1):
            if c < c0 and s == 0 and bq:
                continue
            if profs[c][s] != profs[c][s + 1]:
                continue
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
    # row lex for consecutive interchangeable rows (identical T, |T| <= 1)
    for r in range(N - 1):
        r2 = r + 1
        if rows[r] != rows[r2] or len(rows[r]) >= 2:
            continue
        E = [F.new() for _ in range(k - 1)]
        for c in range(k):
            guard = [] if c == 0 else [-E[c - 1]]
            for s in range(q):
                for t in range(s):
                    F.add(guard + [-X[r][c][s], -X[r2][c][t]])
            if c < k - 1:
                for s in range(q):
                    F.add(guard + [-X[r][c][s], -X[r2][c][s], E[c]])
    # column lex for consecutive identical special columns
    for c in range(c0, k - 1):
        c2 = c + 1
        if profs[c] != profs[c2]:
            continue
        E = [F.new() for _ in range(N - 1)]
        for r in range(N):
            guard = [] if r == 0 else [-E[r - 1]]
            for s in range(q):
                for t in range(s):
                    F.add(guard + [-X[r][c][s], -X[r][c2][t]])
            if r < N - 1:
                for s in range(q):
                    F.add(guard + [-X[r][c][s], -X[r][c2][s], E[r]])
    return F, X, {"rows": [list(t) for t in rows]}
