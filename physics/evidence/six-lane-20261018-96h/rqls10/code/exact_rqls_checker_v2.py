#!/usr/bin/env python3
"""exact_rqls_checker_v2: independent definition-level exact checker for a (maximal-cardinality) 1-RQLS(v).

Independent of exact_rqls_checker_v1 (old lane): zero tests use the trace form of Q(zeta_N) (alpha = sum_j a_j zeta^j is
0 iff sum_j a_j c_N(j - k) = 0 for k = 0..phi(N)-1, c_N = Ramanujan sums), not reduction modulo Phi_N; nonparallelism
uses the Cauchy-Schwarz equality test |<x,y>|^2 = n_x n_y (exactly the linearly dependent pairs), not 2x2 minors.
Input JSON (same schema as v1): {"v", "N", "B": v x v ints, "cells": v x v of {"n": int > 0, "x": [coord_0..coord_{v-1}]}},
each coord a list of [exponent, integer coefficient]; the cell vector is x / sqrt(n).
Predicates: P1 B Latin; P2 <x,x> = n; P3 <x,y> = 0 for distinct cells of every row, column and B-class; P4 no pair of
distinct cells is parallel. Prints a JSON report; exit 0 iff all hold. Standard library only.
"""
import json, math, sys


def mobius(n):
    res, p, m = 1, 2, n
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


def ramanujan(N):
    divs = [d for d in range(1, N + 1) if N % d == 0]
    c = []
    for j in range(N):
        g = math.gcd(j, N)
        c.append(sum(d * mobius(N // d) for d in divs if g % d == 0))
    return c


class Field:
    def __init__(self, N):
        self.N = N
        self.c = ramanujan(N)
        self.phi = sum(1 for k in range(1, N + 1) if math.gcd(k, N) == 1)

    def vec(self, pairs):
        a = [0] * self.N
        for e, co in pairs:
            a[e % self.N] += int(co)
        return a

    def mul(self, a, b):
        N = self.N
        out = [0] * N
        nzb = [(j, bj) for j, bj in enumerate(b) if bj]
        for i, ai in enumerate(a):
            if ai:
                for j, bj in nzb:
                    out[(i + j) % N] += ai * bj
        return out

    def conj(self, a):
        N = self.N
        return [a[(-j) % N] for j in range(N)]

    def add(self, a, b, s=1):
        return [x + s * y for x, y in zip(a, b)]

    def is_zero(self, a):
        N, c = self.N, self.c
        nz = [(j, aj) for j, aj in enumerate(a) if aj]
        for k in range(self.phi):
            if sum(aj * c[(j - k) % N] for j, aj in nz) != 0:
                return False
        return True

    def const(self, n):
        a = [0] * self.N
        a[0] = n
        return a


def main():
    data = json.load(open(sys.argv[1]))
    v, N, B = int(data["v"]), int(data["N"]), data["B"]
    F = Field(N)
    rep = {"checker": "exact_rqls_checker_v2", "v": v, "N": N, "P1": True, "P2": True, "P3": True, "P4": True, "failures": []}

    def fail(k, msg):
        rep[k] = False
        if len(rep["failures"]) < 20:
            rep["failures"].append(msg)
    full = list(range(v))
    if len(B) != v or any(sorted(r) != full for r in B) or any(sorted(B[i][j] for i in range(v)) != full for j in range(v)):
        fail("P1", "B not a Latin square")
    X, n = {}, {}
    for i in range(v):
        for j in range(v):
            cell = data["cells"][i][j]
            n[(i, j)] = int(cell["n"])
            if n[(i, j)] <= 0 or len(cell["x"]) != v:
                fail("P2", "cell %s malformed" % ((i, j),))
            X[(i, j)] = [F.vec(p) for p in cell["x"]]

    def inner(p, q):
        s = [0] * N
        for xp, xq in zip(X[p], X[q]):
            s = F.add(s, F.mul(F.conj(xp), xq))
        return s
    for p in X:
        if not F.is_zero(F.add(inner(p, p), F.const(n[p]), -1)):
            fail("P2", "norm of %s" % (p,))
    lines = [[(i, j) for j in range(v)] for i in range(v)] + [[(i, j) for i in range(v)] for j in range(v)]
    if rep["P1"]:
        lines += [[(i, j) for i in range(v) for j in range(v) if B[i][j] == s] for s in range(v)]
    bad = 0
    for L in lines:
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                if not F.is_zero(inner(L[a], L[b])):
                    bad += 1
                    fail("P3", "line pair %s %s" % (L[a], L[b]))
    rep["nonorthogonal_line_pairs"] = bad
    rep["lines_checked"] = len(lines)
    cells = sorted(X)
    parent = {p: p for p in cells}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    par = 0
    for a in range(len(cells)):
        for b in range(a + 1, len(cells)):
            p, q = cells[a], cells[b]
            s = inner(p, q)
            if F.is_zero(F.add(F.mul(s, F.conj(s)), F.const(n[p] * n[q]), -1)):
                par += 1
                parent[find(p)] = find(q)
                fail("P4", "parallel %s %s" % (p, q))
    rep["parallel_pairs"] = par
    rep["distinct_rays"] = len({find(p) for p in cells})
    rep["ALL_PASS"] = all(rep[k] for k in ("P1", "P2", "P3", "P4"))
    print(json.dumps(rep, indent=1))
    return 0 if rep["ALL_PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())
