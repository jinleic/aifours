#!/usr/bin/env python3
"""Encoder E1 (method M1) for one normalized case of PA(N,k,q).

Case = (column profile per position, M-class representative for positions 0,1).
See README "Symmetry reduction". Writes DIMACS CNF and a JSON variable map.

Constraints (all implied by validity + normalization):
  EO   exactly one symbol per cell                      (x[r][c][s])
  AGR  y[r][r'][c] <- x[r][c][s] & x[r'][c][s];  AMO_c y[r][r'][c]
  CNT  column c >= 2 has exactly prof[c][s] rows with symbol s (sequential counters)
  FIX  columns 0,1 fixed to rows sorted by (a,b) over the 1-entries of M
  VP   columns >= 2: equal-count symbols s<s+1 in first-occurrence order
  LEX  consecutive positions >= 2 with identical profile: lex(col c) <= lex(col c+1)
  ROW  (pb) per row r: sum_c (n_{c,A[r][c]} - 1) <= N-1           [r meets each row <= once]
       and sum_c (n_{c,A[r][c]} - 1) >= N-1-L, L = number of row pairs with no agreement
       (= C(N,2) - sum_c kappa_c, fixed by the profile multiset)  [leave degree <= L]
  DUAL (dual) per column pair and ordered symbol pair: at most one row (redundant view)
"""
import json
import sys


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []
        self.names = {}

    def var(self, name):
        v = self.names.get(name)
        if v is None:
            self.nv += 1
            v = self.nv
            self.names[name] = v
        return v

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, cl):
        self.clauses.append(cl)

    def at_most(self, lits, k):
        n = len(lits)
        if k >= n:
            return
        if k == 0:
            for l in lits:
                self.add([-l])
            return
        R = [[self.new() for _ in range(k)] for _ in range(n - 1)]  # R[i][j]: >= j+1 among 0..i
        self.add([-lits[0], R[0][0]])
        for j in range(1, k):
            self.add([-R[0][j]])
        for i in range(1, n - 1):
            self.add([-lits[i], R[i][0]])
            self.add([-R[i - 1][0], R[i][0]])
            for j in range(1, k):
                self.add([-lits[i], -R[i - 1][j - 1], R[i][j]])
                self.add([-R[i - 1][j], R[i][j]])
            self.add([-lits[i], -R[i - 1][k - 1]])
        self.add([-lits[n - 1], -R[n - 2][k - 1]])

    def exactly(self, lits, k):
        self.at_most(lits, k)
        self.at_most([-l for l in lits], len(lits) - k)

    def weighted_at_most(self, groups, cap):
        """groups: list over positions of [(literal, weight>=0), ...] with exactly one literal
        true per position (guaranteed elsewhere). Enforce sum of chosen weights <= cap.
        S[c][v] (v=1..cap) is forced true when the partial sum over positions 0..c is >= v."""
        prev = None
        for c, grp in enumerate(groups):
            cur = [None] + [self.new() for _ in range(cap)]
            for v in range(2, cap + 1):
                self.add([-cur[v], cur[v - 1]])
            if prev is not None:
                for v in range(1, cap + 1):
                    self.add([-prev[v], cur[v]])
            for lit, w in grp:
                if w > cap:
                    self.add([-lit])
                    continue
                if w >= 1:
                    self.add([-lit, cur[w]])
                if prev is not None and w >= 1:
                    for v in range(1, cap + 1):
                        if v + w > cap:
                            self.add([-prev[v], -lit])
                        else:
                            self.add([-prev[v], -lit, cur[v + w]])
            prev = cur

    def write(self, path):
        with open(path, "w") as f:
            f.write("p cnf %d %d\n" % (self.nv, len(self.clauses)))
            for cl in self.clauses:
                f.write(" ".join(map(str, cl)) + " 0\n")


def fixed_rows(M):
    rows = []
    for a, row in enumerate(M):
        for b, v in enumerate(row):
            if v:
                rows.append((a, b))
    return rows  # already lexicographic in (a,b)


def build(N, k, q, profs, M, lex=True, vp=True, pb=False, dual=False, cover=False):
    F = CNF()
    X = [[[F.var(("x", r, c, s)) for s in range(q)] for c in range(k)] for r in range(N)]
    for r in range(N):
        for c in range(k):
            F.add(list(X[r][c]))
            for s in range(q):
                for t in range(s + 1, q):
                    F.add([-X[r][c][s], -X[r][c][t]])
    fr = fixed_rows(M)
    assert len(fr) == N, (len(fr), N)
    for r, (a, b) in enumerate(fr):
        F.add([X[r][0][a]])
        F.add([X[r][1][b]])
    # AGR
    for r in range(N):
        for r2 in range(r + 1, N):
            ys = []
            for c in range(k):
                y = F.var(("y", r, r2, c))
                ys.append(y)
                for s in range(q):
                    F.add([-X[r][c][s], -X[r2][c][s], y])
            for i in range(k):
                for j in range(i + 1, k):
                    F.add([-ys[i], -ys[j]])
    # CNT
    for c in range(2, k):
        for s in range(q):
            F.exactly([X[r][c][s] for r in range(N)], profs[c][s])
    # VP
    if vp:
        for c in range(2, k):
            for s in range(q - 1):
                if profs[c][s] != profs[c][s + 1] or profs[c][s] == 0:
                    continue
                P = [F.var(("p", c, s, r)) for r in range(N)]
                F.add([-P[0], X[0][c][s]])
                F.add([-X[0][c][s], P[0]])
                for r in range(1, N):
                    F.add([-P[r - 1], P[r]])
                    F.add([-X[r][c][s], P[r]])
                    F.add([-P[r], P[r - 1], X[r][c][s]])
                F.add([-X[0][c][s + 1]])
                for r in range(1, N):
                    F.add([-X[r][c][s + 1], P[r - 1]])
    # LEX
    if lex:
        for c in range(2, k - 1):
            c2 = c + 1
            if list(profs[c]) != list(profs[c2]):
                continue
            E = [F.var(("e", c, r)) for r in range(N - 1)]
            for r in range(N):
                guard = [] if r == 0 else [-E[r - 1]]
                for s in range(q):
                    for t in range(s):
                        F.add(guard + [-X[r][c][s], -X[r][c2][t]])
                if r < N - 1:
                    for s in range(q):
                        F.add(guard + [-X[r][c][s], -X[r][c2][s], E[r]])
    # ROW
    if pb:
        kap = sum(n * (n - 1) // 2 for p in profs for n in p)
        L = N * (N - 1) // 2 - kap
        assert L >= 0
        wmax = [max(p) - 1 for p in profs]
        lo = (N - 1) - L
        cap2 = sum(wmax) - lo
        for r in range(N):
            F.weighted_at_most([[(X[r][c][s], profs[c][s] - 1) for s in range(q)]
                                for c in range(k)], N - 1)
            if cap2 >= 0:
                F.weighted_at_most([[(X[r][c][s], wmax[c] - (profs[c][s] - 1)) for s in range(q)]
                                    for c in range(k)], cap2)
    # DUAL
    if dual:
        for c in range(k):
            for c2 in range(c + 1, k):
                for s in range(q):
                    for t in range(q):
                        lits = []
                        for r in range(N):
                            z = F.new()
                            F.add([-X[r][c][s], -X[r][c2][t], z])
                            lits.append(z)
                        F.at_most(lits, 1)
    # COVER: at most L row pairs agree in no column (L fixed by the profile multiset)
    if cover:
        kap = sum(n * (n - 1) // 2 for p in profs for n in p)
        L = N * (N - 1) // 2 - kap
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
    return F, X


def main():
    spec = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    F, X = build(spec["N"], spec["k"], spec["q"], spec["profiles"], spec["M"],
                 lex=spec.get("lex", True), vp=spec.get("vp", True),
                 pb=spec.get("pb", False), dual=spec.get("dual", False),
                 cover=spec.get("cover", False))
    F.write(out)
    print(json.dumps({"cnf": out, "vars": F.nv, "clauses": len(F.clauses)}))


if __name__ == "__main__":
    main()
