#!/usr/bin/env python3
"""Encoder FULL2 = encode_full.py plus EXACT leave counts (Amendment A3-exact): z(r,r') is
forced false when rows r, r' agree in some column (clauses -z | -x[r][c][s] | -x[r'][c][s]), so
z is exactly "agree nowhere", and row r misses AT LEAST l(r) rows (besides at most l(r)).
Valid: row r agrees with exactly sum_c (n_{c,A[r][c]} - 1) = 18 - l(r) other rows (the agreeing
sets of different columns are disjoint), so it misses exactly l(r) rows.
Original docstring of encode_full.py:
Encoder FULL (Amendment A3, method M1 family): completion of one full skeleton.

Columns 0..c0-1 = P0 columns (symbol 0 = quad, fixed; symbols 1..5 = triples, count 3).
Columns c0.. = P1 columns (4,4,3,3,3,2): symbol 0 = A, 1 = B, 5 = P fixed; symbols 2,3,4 =
triples, count 3. Every non-triple cell is fixed, so each row's leave degree is known:
l(r) = 2 - |T(r)| - w(r). Constraints: EO cells; fixed blocks; triple counts; AMO agreements;
row r misses at most l(r) rows and at most L pairs miss in total (equality then follows by
counting); value precedence among triple symbols of every column; lex(row i) <= lex(row j)
for rows with identical fixed pattern (lex-leader of the row transposition, row-major order).
"""
import encode_e1
from encode_skel import rows_of


def build(spec):
    c0, L = spec["c0"], spec["L"]
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    rows = rows_of(c0, spec["skeleton"], N)
    placed = spec["placed"]  # per special column [A, B, P]
    ns = len(placed)
    assert c0 + ns == k
    fixed = {}  # (r, c) -> symbol for non-triple cells
    triple_syms = {}
    for c in range(c0):
        for r in range(N):
            if c in rows[r]:
                fixed[(r, c)] = 0
        triple_syms[c] = [1, 2, 3, 4, 5]
    w = [0] * N
    for i, (A, B, P) in enumerate(placed):
        c = c0 + i
        for r in A:
            fixed[(r, c)] = 0
            w[r] += 1
        for r in B:
            fixed[(r, c)] = 1
            w[r] += 1
        for r in P:
            fixed[(r, c)] = 5
            w[r] -= 1
        triple_syms[c] = [2, 3, 4]
    leave = [2 - len(rows[r]) - w[r] for r in range(N)]
    assert all(0 <= x <= L for x in leave) and sum(leave) == 2 * L, leave
    F = encode_e1.CNF()
    X = [[[F.var(("x", r, c, s)) for s in range(q)] for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            F.add(list(X[r][c]))
            for s in range(q):
                for t in range(s + 1, q):
                    F.add([-X[r][c][s], -X[r][c][t]])
            if (r, c) in fixed:
                F.add([X[r][c][fixed[(r, c)]]])
            else:
                for s in range(q):
                    if s not in triple_syms[c]:
                        F.add([-X[r][c][s]])
    for c in range(k):
        for s in triple_syms[c]:
            F.exactly([X[r][c][s] for r in range(N)], 3)
    Z = {}
    for r in range(N):
        for r2 in range(r + 1, N):
            ys = []
            ms = []
            for c in range(k):
                y = F.new()
                ys.append(y)
                for s in range(q):
                    F.add([-X[r][c][s], -X[r2][c][s], y])
                    m = F.new()
                    F.add([-m, X[r][c][s]])
                    F.add([-m, X[r2][c][s]])
                    ms.append(m)
            for i in range(k):
                for j in range(i + 1, k):
                    F.add([-ys[i], -ys[j]])
            z = F.new()
            Z[(r, r2)] = z
            F.add([z] + ms)
    for (r, r2), z in Z.items():
        for c in range(k):
            for s in range(q):
                F.add([-z, -X[r][c][s], -X[r2][c][s]])
    for r in range(N):
        zr = [Z[(min(r, x), max(r, x))] for x in range(N) if x != r]
        F.at_most(zr, leave[r])
        F.at_most([-z for z in zr], len(zr) - leave[r])
    F.at_most(list(Z.values()), L)
    for c in range(k):
        syms = triple_syms[c]
        for a, b in zip(syms, syms[1:]):
            P_ = [F.new() for _ in range(N)]
            F.add([-P_[0], X[0][c][a]])
            F.add([-X[0][c][a], P_[0]])
            for r in range(1, N):
                F.add([-P_[r - 1], P_[r]])
                F.add([-X[r][c][a], P_[r]])
                F.add([-P_[r], P_[r - 1], X[r][c][a]])
            F.add([-X[0][c][b]])
            for r in range(1, N):
                F.add([-X[r][c][b], P_[r - 1]])
    pattern = [tuple(fixed.get((r, c), -1) for c in range(k)) for r in range(N)]
    nlex = 0
    for r in range(N):
        nxt = [r2 for r2 in range(r + 1, N) if pattern[r2] == pattern[r]]
        if not nxt:
            continue
        r2 = nxt[0]
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
    return F, X, {"leave": leave, "row_lex_pairs": nlex}
