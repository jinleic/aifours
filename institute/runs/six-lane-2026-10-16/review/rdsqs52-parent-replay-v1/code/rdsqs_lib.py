"""Search-side library for the RDSQS(52) lane (numpy + external kissat).

Points are 0..n-1; a permutation p is a tuple with p[x] the image of x.
Composition comp(p, q)[x] = p[q[x]] (q first).

Kramer–Mesner for SQS(n) under a group G: columns are G-orbits of 3-subsets,
rows are G-orbits of 4-subsets whose development covers each triple of every
triple-orbit it meets exactly once (computed from orbit sizes, independently of
any scout counts).
"""
from __future__ import annotations

import collections
import hashlib
import os
import subprocess
import time
from collections import deque
from math import comb

import numpy as np


# ------------------------------------------------------------------ groups
def comp(p, q):
    return tuple(p[x] for x in q)


def closure(gens, n, limit=10**6):
    e = tuple(range(n))
    seen = {e}
    dq = deque([e])
    gens = [tuple(g) for g in gens]
    while dq:
        a = dq.popleft()
        for g in gens:
            b = comp(g, a)
            if b not in seen:
                seen.add(b)
                if len(seen) > limit:
                    raise RuntimeError("group too large")
                dq.append(b)
    return sorted(seen)


def perm_order(p):
    from math import gcd
    n = len(p)
    seen = [False] * n
    o = 1
    for s in range(n):
        if not seen[s]:
            L, x = 0, s
            while not seen[x]:
                seen[x] = True
                x = p[x]
                L += 1
            o = o * L // gcd(o, L)
    return o


# ------------------------------------------------------------------ k-sets
def ksets(n, k):
    """All k-subsets of range(n) as a sorted (colex-ranked) int64 array."""
    from itertools import combinations
    arr = np.fromiter((x for c in combinations(range(n), k) for x in c), dtype=np.int64,
                      count=comb(n, k) * k).reshape(-1, k)
    # sort into colex order so that rank() indexes rows directly
    r = rank(arr)
    out = np.empty_like(arr)
    out[r] = arr
    return out


def rank(arr):
    """Colex rank of rows of a (m,k) int array of distinct points (any order)."""
    s = np.sort(arr, axis=1)
    k = s.shape[1]
    r = np.zeros(s.shape[0], dtype=np.int64)
    for i in range(k):
        x = s[:, i]
        # C(x, i+1)
        num = np.ones_like(x)
        den = 1
        for j in range(i + 1):
            num = num * (x - j)
            den *= (j + 1)
        r += num // den
    return r


def orbit_labels(images):
    """images: list of int arrays, each a permutation of range(m). Returns min label per item."""
    m = len(images[0])
    L = np.arange(m, dtype=np.int64)
    allimg = list(images)
    for im in images:
        iv = np.empty_like(im)
        iv[im] = np.arange(m)
        allimg.append(iv)
    while True:
        old = L.copy()
        for im in allimg:
            np.minimum(L, L[im], out=L)
        for _ in range(5):
            L = L[L]
        if np.array_equal(L, old):
            return L


# ------------------------------------------------------------------ CNF / SAT
class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, cl):
        self.clauses.append(list(cl))

    def amo(self, lits):
        lits = list(lits)
        k = len(lits)
        if k <= 1:
            return
        if k <= 5:
            for i in range(k):
                for j in range(i + 1, k):
                    self.add([-lits[i], -lits[j]])
            return
        s = [self.var() for _ in range(k - 1)]
        self.add([-lits[0], s[0]])
        for i in range(1, k - 1):
            self.add([-lits[i], s[i]])
            self.add([-s[i - 1], s[i]])
            self.add([-lits[i], -s[i - 1]])
        self.add([-lits[k - 1], -s[k - 2]])

    def exactly_one(self, lits):
        lits = list(lits)
        if not lits:
            self.add([])
            return
        self.add(lits)
        self.amo(lits)

    def write(self, path):
        lines = [f"p cnf {self.nv} {len(self.clauses)}"]
        lines.extend(" ".join(map(str, c)) + " 0" for c in self.clauses)
        data = "\n".join(lines) + "\n"
        with open(path, "w") as f:
            f.write(data)
        return hashlib.sha256(data.encode()).hexdigest()


def kissat(path, timeout, seed=0, log=None):
    cmd = ["kissat", "-q", f"--time={int(timeout)}", f"--seed={seed}", path]
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    dt = time.time() - t0
    if log:
        with open(log, "w") as f:
            f.write(" ".join(cmd) + "\n" + p.stdout[-2000:] + "\n--stderr--\n" + p.stderr)
    st = "UNKNOWN"
    model = set()
    for line in p.stdout.splitlines():
        if line.startswith("s "):
            st = "UNSAT" if "UNSAT" in line else ("SAT" if "SATISFIABLE" in line else st)
        elif line.startswith("v "):
            for x in line[2:].split():
                xi = int(x)
                if xi > 0:
                    model.add(xi)
    return st, model, dt


# ------------------------------------------------------------------ KM model
class SQSKM:
    """Kramer–Mesner model for an SQS(n) invariant under the group generated by gens."""

    def __init__(self, n, gens):
        self.n = n
        self.gens = [tuple(g) for g in gens]
        self.T = ksets(n, 3)
        self.Q = ksets(n, 4)
        gT = [rank(np.asarray(g, dtype=np.int64)[self.T]) for g in self.gens]
        gQ = [rank(np.asarray(g, dtype=np.int64)[self.Q]) for g in self.gens]
        self.LT = orbit_labels(gT) if self.gens else np.arange(len(self.T))
        self.LQ = orbit_labels(gQ) if self.gens else np.arange(len(self.Q))
        self.sizeT = collections.Counter(self.LT.tolist())
        self.sizeQ = collections.Counter(self.LQ.tolist())
        self.tcols = sorted(self.sizeT)
        self.colidx = {c: i for i, c in enumerate(self.tcols)}
        # triples of each quad (ranks)
        q = self.Q
        tri = np.stack([rank(q[:, [1, 2, 3]]), rank(q[:, [0, 2, 3]]), rank(q[:, [0, 1, 3]]), rank(q[:, [0, 1, 2]])], axis=1)
        self.rows = []      # (quad-orbit label, tuple of column indices)
        self.bad_rows = 0
        for lab in sorted(self.sizeQ):
            tl = self.LT[tri[lab]]
            c = collections.Counter(tl.tolist())
            ok = True
            for t, m in c.items():
                mult = self.sizeQ[lab] * m
                if mult % self.sizeT[t] or mult // self.sizeT[t] != 1:
                    ok = False
                    break
            if ok:
                self.rows.append((lab, tuple(sorted(self.colidx[t] for t in c))))
            else:
                self.bad_rows += 1

    def summary(self):
        return {
            "n": self.n,
            "triples": len(self.T), "quads": len(self.Q),
            "triple_orbits": len(self.tcols),
            "triple_orbit_sizes": dict(sorted(collections.Counter(self.sizeT.values()).items())),
            "quad_orbits": len(self.sizeQ),
            "quad_orbit_sizes": dict(sorted(collections.Counter(self.sizeQ.values()).items())),
            "valid_rows": len(self.rows), "invalid_rows": self.bad_rows,
            "valid_rows_by_orbit_size": dict(sorted(collections.Counter(self.sizeQ[l] for l, _ in self.rows).items())),
        }

    def cnf(self):
        cnf = CNF()
        rv = [cnf.var() for _ in self.rows]
        bycol = [[] for _ in self.tcols]
        for i, (_, cols) in enumerate(self.rows):
            for c in cols:
                bycol[c].append(rv[i])
        for lits in bycol:
            cnf.exactly_one(lits)
        return cnf, rv

    def blocks_of(self, selected_rows):
        labs = np.array([self.rows[i][0] for i in selected_rows], dtype=np.int64)
        mask = np.isin(self.LQ, labs)
        return [tuple(int(x) for x in b) for b in self.Q[mask]]


def derived(blocks, x):
    return sorted(tuple(p for p in b if p != x) for b in blocks if x in b)


# ------------------------------------------------------------------ resolution SAT
def resolution_cnf(triples, points, nclasses, anchor):
    """Unrestricted resolution of an STS on `points` into nclasses parallel classes.
    Lossless symmetry breaking: the triples through `anchor` go to classes 0..nclasses-1
    in sorted order."""
    cnf = CNF()
    tv = [[cnf.var() for _ in range(nclasses)] for _ in triples]
    through = [i for i, t in enumerate(triples) if anchor in t]
    assert len(through) == nclasses
    for c, i in enumerate(sorted(through, key=lambda i: triples[i])):
        cnf.add([tv[i][c]])
    for i in range(len(triples)):
        cnf.exactly_one(tv[i])
    inc = collections.defaultdict(list)
    for i, t in enumerate(triples):
        for p in t:
            inc[p].append(i)
    for c in range(nclasses):
        for p in points:
            cnf.exactly_one([tv[i][c] for i in inc[p]])
    return cnf, tv


def decode_resolution(model, triples, tv, nclasses):
    classes = [[] for _ in range(nclasses)]
    for i, t in enumerate(triples):
        cs = [c for c in range(nclasses) if tv[i][c] in model]
        assert len(cs) == 1
        classes[cs[0]].append(t)
    return [sorted(C) for C in classes]


def verify_resolution(triples, points, classes):
    allt = sorted(t for C in classes for t in C)
    assert allt == sorted(triples), "resolution does not list the derived design exactly"
    for C in classes:
        pts = sorted(p for t in C for p in t)
        assert pts == sorted(points), "class is not a parallel class"
    return True


# ------------------------------------------------------------------ certificate
def transport(G, reps_res, n):
    """reps_res: dict rep_point -> classes. For each x choose the least g in sorted G
    mapping some rep to x; resolution at x = g(resolution at rep)."""
    out = {}
    for g in sorted(G):
        for r, classes in reps_res.items():
            x = g[r]
            if x not in out:
                out[x] = [sorted(tuple(sorted(g[p] for p in t)) for t in C) for C in classes]
    assert sorted(out) == list(range(n)), "group does not reach every point from the representatives"
    return out


def write_certificate(path, n, blocks, res, header):
    lines = [f"# {header}", f"RDSQS {n}", "BLOCKS"]
    lines.extend(" ".join(map(str, b)) for b in sorted(tuple(sorted(b)) for b in blocks))
    for x in range(n):
        lines.append(f"POINT {x}")
        for c, C in enumerate(res[x]):
            lines.append(f"CLASS {c}")
            lines.extend(" ".join(map(str, t)) for t in C)
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    return hashlib.sha256(open(path, "rb").read()).hexdigest()
