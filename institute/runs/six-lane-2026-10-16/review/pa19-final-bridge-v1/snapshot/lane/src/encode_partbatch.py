#!/usr/bin/env python3
"""Encoder PARTBATCH (A3'' batching, method M1 family): one CNF for a BATCH of one-column
placements of an all-P1 A2 case (placements from extend_p1q.py with m = 1).

Selector t_i per placement i, clause (t_1 | ... | t_b). The first special column c* = c0 is
encoded like a free special column with exact label counts (A -> 0, B -> 1 count 4, triples
2..q-2 count 3, P -> q-1 count 2) and, guarded by t_i, the cells of placement i fixed
(positive guarded units for its A, B, P rows; guarded exclusions of labels 0, 1, q-1 for the
other rows). Symmetry: value precedence among the triple labels of c* only (the A/B order is
part of the placement); guarded by t_i, row lex between rows with identical fixed pattern
(P0 set and role in c* under placement i); column lex between consecutive identical free
special columns; the rest exactly as encode_partq.py. The CNF is UNSAT iff every placement
subcase of the batch is UNSAT (each satisfying assignment satisfies some t_i together with
that subcase's constraints, and conversely).
"""
import encode_e1
from encode_skel import rows_of


def build(spec, placements):
    # extend_p1q with m = 1 yields [[A, B, P]] per placement; accept [A, B, P] too
    placements = [pl[0] if len(pl) == 1 else pl for pl in placements]
    c0, skel, special = spec["c0"], spec["skeleton"], [list(p) for p in spec["special"]]
    N, k, q = spec.get("N", 19), spec.get("k", 8), spec.get("q", 6)
    PAIR = q - 1
    TRI = list(range(2, q - 1))
    assert all(p == [4, 4] + [3] * (q - 3) + [2] for p in special)
    profs = [[4] + [3] * (q - 1)] * c0 + special
    rows = rows_of(c0, skel, N)
    cs = c0  # the column whose placement is batched
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
    for c in range(k):
        for s in range(q):
            if c < c0 and s == 0:
                continue
            F.exactly([X[r][c][s] for r in range(N)], profs[c][s])
    sel = [F.new() for _ in placements]
    F.add(list(sel))
    for t_i, (A, B, P) in zip(sel, placements):
        role = {}
        for r in A:
            role[r] = 0
        for r in B:
            role[r] = 1
        for r in P:
            role[r] = PAIR
        for r in range(N):
            if r in role:
                F.add([-t_i, X[r][cs][role[r]]])
            else:
                for s in (0, 1, PAIR):
                    F.add([-t_i, -X[r][cs][s]])
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
        elif c == cs:
            pairs = list(zip(TRI, TRI[1:]))
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
    for t_i, (A, B, P) in zip(sel, placements):
        role = {}
        for r in A:
            role[r] = 0
        for r in B:
            role[r] = 1
        for r in P:
            role[r] = PAIR
        pattern = [(rows[r], role.get(r, -1)) for r in range(N)]
        for r in range(N):
            nxt = [r2 for r2 in range(r + 1, N) if pattern[r2] == pattern[r]]
            if not nxt:
                continue
            r2 = nxt[0]
            E = [F.new() for _ in range(k - 1)]
            for c in range(k):
                guard = [-t_i] + ([] if c == 0 else [-E[c - 1]])
                for s in range(q):
                    for t in range(s):
                        F.add(guard + [-X[r][c][s], -X[r2][c][t]])
                if c < k - 1:
                    for s in range(q):
                        F.add(guard + [-X[r][c][s], -X[r2][c][s], E[c]])
    for c in range(cs + 1, k - 1):
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
    return F, X, sel
