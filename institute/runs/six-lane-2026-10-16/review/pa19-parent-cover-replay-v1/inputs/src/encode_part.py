#!/usr/bin/env python3
"""Encoder PART (Amendment A3', method M1 family): an A2 skeleton case of a multiset whose
special columns are all P1 = (4,4,3,3,3,2), with the blocks (A, B, P) of the first m special
columns fixed (one extension produced by `extend_p1.py SPEC OUT m`), the other special
columns free. Same constraint families as encode_skel, adapted:
  * fixed special columns: A -> 0, B -> 1, P -> 5 fixed, other rows restricted to 2..4;
  * value precedence: P0 columns 1..5; fixed special columns 2..4 only (the A/B order is
    fixed by the placement); free special columns among equal counts as in encode_skel;
  * row lex only between rows with identical fixed pattern (P0 set T and roles in the fixed
    columns) -- such rows are interchangeable in the subcase;
  * column lex only between consecutive identical FREE special columns.
All breaking constraints are lex-leader for one row-major order (P0 columns, fixed special
columns, free special columns).
"""
import encode_e1
from encode_skel import rows_of


def build(spec):
    c0, skel, special = spec["c0"], spec["skeleton"], [list(p) for p in spec["special"]]
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    placed = spec["placed"]
    m = len(placed)
    assert all(p == [4, 4, 3, 3, 3, 2] for p in special)
    profs = [[4] + [3] * (q - 1)] * c0 + special
    rows = rows_of(c0, skel, N)
    fixed = {}
    for r in range(N):
        for c in range(c0):
            if c in rows[r]:
                fixed[(r, c)] = 0
    for i, (A, B, P) in enumerate(placed):
        c = c0 + i
        for r in A:
            fixed[(r, c)] = 0
        for r in B:
            fixed[(r, c)] = 1
        for r in P:
            fixed[(r, c)] = 5
    F = encode_e1.CNF()
    X = [[[F.var(("x", r, c, s)) for s in range(q)] for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            F.add(list(X[r][c]))
            for s in range(q):
                for t in range(s + 1, q):
                    F.add([-X[r][c][s], -X[r][c][t]])
            if c < c0:
                F.add([X[r][c][0]] if c in rows[r] else [-X[r][c][0]])
            elif c < c0 + m:
                if (r, c) in fixed:
                    F.add([X[r][c][fixed[(r, c)]]])
                else:
                    for s in (0, 1, 5):
                        F.add([-X[r][c][s]])
    for c in range(k):
        for s in range(q):
            if c < c0 and s == 0:
                continue
            if c0 <= c < c0 + m and s in (0, 1, 5):
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
                    mm = F.new()
                    F.add([-mm, X[r][c][s]])
                    F.add([-mm, X[r2][c][s]])
                    cl.append(mm)
            F.add(cl)
    F.at_most(zs, L)
    for c in range(k):
        if c < c0:
            pairs = [(s, s + 1) for s in range(1, q - 1)]
        elif c < c0 + m:
            pairs = [(2, 3), (3, 4)]
        else:
            pairs = [(s, s + 1) for s in range(q - 1) if profs[c][s] == profs[c][s + 1]]
        for s, s2 in pairs:
            P_ = [F.new() for _ in range(N)]
            F.add([-P_[0], X[0][c][s]])
            F.add([-X[0][c][s], P_[0]])
            for r in range(1, N):
                F.add([-P_[r - 1], P_[r]])
                F.add([-X[r][c][s], P_[r]])
                F.add([-P_[r], P_[r - 1], X[r][c][s]])
            F.add([-X[0][c][s2]])
            for r in range(1, N):
                F.add([-X[r][c][s2], P_[r - 1]])
    pattern = [tuple(fixed.get((r, c), -1) for c in range(c0 + m)) for r in range(N)]
    for r in range(N):
        nxt = [r2 for r2 in range(r + 1, N) if pattern[r2] == pattern[r]]
        if not nxt:
            continue
        r2 = nxt[0]
        E = [F.new() for _ in range(k - 1)]
        for c in range(k):
            guard = [] if c == 0 else [-E[c - 1]]
            for s in range(q):
                for t in range(s):
                    F.add(guard + [-X[r][c][s], -X[r2][c][t]])
            if c < k - 1:
                for s in range(q):
                    F.add(guard + [-X[r][c][s], -X[r2][c][s], E[c]])
    for c in range(c0 + m, k - 1):
        c2 = c + 1
        E = [F.new() for _ in range(N - 1)]
        for r in range(N):
            guard = [] if r == 0 else [-E[r - 1]]
            for s in range(q):
                for t in range(s):
                    F.add(guard + [-X[r][c][s], -X[r][c2][t]])
            if r < N - 1:
                for s in range(q):
                    F.add(guard + [-X[r][c][s], -X[r][c2][s], E[r]])
    return F, X, {"m": m}
