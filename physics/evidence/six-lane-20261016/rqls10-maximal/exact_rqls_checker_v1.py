#!/usr/bin/env python3
"""Exact definition-level checker for a maximal-cardinality 1-RQLS(v). Standard library only.

Input JSON:
  {"v": v, "N": N,
   "B": v x v integer array (transversal labels),
   "cells": v x v array of {"n": positive int, "x": [coord_0, ..., coord_{v-1}]}}
Each coord is a list of [exponent, integer coefficient] pairs and stands for sum c * zeta_N^e.
The cell vector is x / sqrt(n).

Exact predicates, evaluated in Q(zeta_N) = Z[x]/Phi_N(x) with integer coefficients:
  P1  B is a Latin square on {0..v-1}: every row and every column is a permutation.
  P2  every cell has norm 1:  sum_k x_k * conj(x_k) == n.
  P3  every line (rows, columns, classes T_s = {(i,j): B[i][j] = s}) is orthonormal: sum_k conj(x_k) y_k == 0
      for distinct cells of the line. Together with P2 this is an ONB of C^v, since v orthonormal vectors in C^v
      form a basis.
  P4  maximal cardinality: for every pair of distinct cells some 2x2 minor x_k y_l - x_l y_k != 0. Over C this
      holds iff the two vectors are not parallel, i.e. they are distinct modulo a global phase.

Conjugation is zeta^e -> zeta^(-e), the complex conjugation automorphism of Q(zeta_N).
Exit code 0 iff P1-P4 all hold.
"""
import json
import sys


def poly_divmod(a, b):
    """Integer polynomial division by monic b. Lists are lowest degree first."""
    a = list(a)
    db = len(b) - 1
    assert b[-1] == 1
    q = [0] * max(len(a) - db, 1)
    for k in range(len(a) - 1, db - 1, -1):
        c = a[k]
        if c:
            q[k - db] = c
            for t in range(db + 1):
                a[k - db + t] -= c * b[t]
    rem = a[:db] if db > 0 else []
    return q, rem


def cyclotomic(N, _cache={}):
    if N in _cache:
        return _cache[N]
    p = [-1] + [0] * (N - 1) + [1]  # x^N - 1
    for d in range(1, N):
        if N % d == 0:
            q, r = poly_divmod(p, cyclotomic(d))
            assert all(c == 0 for c in r)
            while len(q) > 1 and q[-1] == 0:
                q.pop()
            p = q
    _cache[N] = p
    return p


class Cyc:
    """Elements of Z[zeta_N] as {exponent mod N: int}. Zero-test by reduction mod Phi_N."""

    def __init__(self, N):
        self.N = N
        self.phi = cyclotomic(N)
        self.deg = len(self.phi) - 1

    def elem(self, pairs):
        d = {}
        for e, c in pairs:
            e %= self.N
            d[e] = d.get(e, 0) + int(c)
        return {e: c for e, c in d.items() if c}

    def mul(self, a, b):
        N = self.N
        out = {}
        for e1, c1 in a.items():
            for e2, c2 in b.items():
                e = (e1 + e2) % N
                out[e] = out.get(e, 0) + c1 * c2
        return {e: c for e, c in out.items() if c}

    def add(self, a, b, sign=1):
        out = dict(a)
        for e, c in b.items():
            out[e] = out.get(e, 0) + sign * c
        return {e: c for e, c in out.items() if c}

    def conj(self, a):
        N = self.N
        return {(-e) % N: c for e, c in a.items()}

    def reduce(self, a):
        poly = [0] * self.N
        for e, c in a.items():
            poly[e] += c
        _, rem = poly_divmod(poly, self.phi)
        rem = rem + [0] * (self.deg - len(rem))
        return rem

    def is_zero(self, a):
        return all(c == 0 for c in self.reduce(a))

    def equals_int(self, a, n):
        r = self.reduce(a)
        return r[0] == n and all(c == 0 for c in r[1:])


def check(data, max_report=20):
    v = int(data["v"])
    N = int(data["N"])
    K = Cyc(N)
    B = data["B"]
    rep = {"v": v, "N": N, "P1_latin": True, "P2_norms": True, "P3_lines": True, "P4_nonparallel": True,
           "failures": []}

    def fail(key, msg):
        rep[key] = False
        if len(rep["failures"]) < max_report:
            rep["failures"].append(msg)
    # P1
    if len(B) != v or any(len(r) != v for r in B):
        fail("P1_latin", "B shape")
    else:
        full = list(range(v))
        for i in range(v):
            if sorted(B[i]) != full:
                fail("P1_latin", "row %d of B not a permutation" % i)
        for j in range(v):
            if sorted(B[i][j] for i in range(v)) != full:
                fail("P1_latin", "column %d of B not a permutation" % j)
    # parse cells
    cells = data["cells"]
    X = {}
    nn = {}
    for i in range(v):
        for j in range(v):
            c = cells[i][j]
            nn[(i, j)] = int(c["n"])
            if len(c["x"]) != v:
                fail("P2_norms", "cell (%d,%d) wrong length" % (i, j))
            X[(i, j)] = [K.elem(pairs) for pairs in c["x"]]
            if nn[(i, j)] <= 0:
                fail("P2_norms", "cell (%d,%d) n<=0" % (i, j))
    XC = {p: [K.conj(z) for z in X[p]] for p in X}
    # P2
    for p in sorted(X):
        s = {}
        for z, zc in zip(X[p], XC[p]):
            s = K.add(s, K.mul(z, zc))
        if not K.equals_int(s, nn[p]):
            fail("P2_norms", "cell %s norm^2 != n" % (p,))
    # P3
    lines = [("row", i, [(i, j) for j in range(v)]) for i in range(v)]
    lines += [("col", j, [(i, j) for i in range(v)]) for j in range(v)]
    if rep["P1_latin"]:
        lines += [("class", s, [(i, j) for i in range(v) for j in range(v) if B[i][j] == s]) for s in range(v)]
    nonorth = 0
    for kind, idx, L in lines:
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                p, q = L[a], L[b]
                s = {}
                for zc, w in zip(XC[p], X[q]):
                    s = K.add(s, K.mul(zc, w))
                if not K.is_zero(s):
                    nonorth += 1
                    fail("P3_lines", "%s %d: cells %s,%s not orthogonal" % (kind, idx, p, q))
    rep["nonorthogonal_line_pairs"] = nonorth
    rep["lines_checked"] = len(lines)
    # P4
    cellsl = sorted(X)
    parent = {p: p for p in cellsl}

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    parallel_pairs = 0
    for a in range(len(cellsl)):
        x = X[cellsl[a]]
        for b in range(a + 1, len(cellsl)):
            y = X[cellsl[b]]
            found = False
            for k in range(v):
                if found:
                    break
                for l in range(k + 1, v):
                    m = K.add(K.mul(x[k], y[l]), K.mul(x[l], y[k]), -1)
                    if m and not K.is_zero(m):
                        found = True
                        break
            if not found:
                parallel_pairs += 1
                parent[find(cellsl[a])] = find(cellsl[b])
                fail("P4_nonparallel", "cells %s,%s parallel" % (cellsl[a], cellsl[b]))
    rep["parallel_pairs"] = parallel_pairs
    rep["distinct_rays"] = len({find(p) for p in cellsl})
    rep["pairs_checked"] = len(cellsl) * (len(cellsl) - 1) // 2
    rep["ALL_PASS"] = all(rep[k] for k in ("P1_latin", "P2_norms", "P3_lines", "P4_nonparallel"))
    return rep


def main():
    with open(sys.argv[1]) as fh:
        data = json.load(fh)
    rep = check(data)
    print(json.dumps(rep, indent=1))
    return 0 if rep["ALL_PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())
