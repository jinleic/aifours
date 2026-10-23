"""Search-side library for the gcDCQS lane (numpy + external kissat).  Imports lane_guard first.

Group closure, colex k-set ranking, orbit labelling, CNF writer and kissat runner are adapted
from ../../mcdsqs38/code/mcdsqs_lib.py (sha256 6f4c6802…391); writes are exclusive-create.
Points are 0..n-1; a permutation p is a tuple with p[x] the image of x; comp(p, q)[x] = p[q[x]].
"""
from __future__ import annotations

import lane_guard  # noqa: F401  (must stay the first import)

import hashlib
import subprocess
import time
from collections import deque
from math import comb

import numpy as np

from lane_guard import xopen


# ------------------------------------------------------------------ arithmetic
def chi_index(w):
    """Chromatic index of STS(w), Tan–Zhou (1.1) (w ≡ 1, 3 mod 6)."""
    if w % 6 == 3:
        return (w - 1) // 2
    if w % 6 == 1:
        return {7: 7, 13: 8}.get(w, (w + 1) // 2)
    raise ValueError("w is not an STS order")


def gcsts_params(w, h):
    """(r, s) of a gcSTS(w, h): r = chi'(w), s = r - (w - h)/2 (Tan–Zhou lines 211–220)."""
    r = chi_index(w)
    return r, r - (w - h) // 2


# ------------------------------------------------------------------ groups
def comp(p, q):
    return tuple(p[x] for x in q)


def inverse(p):
    inv = [0] * len(p)
    for i, x in enumerate(p):
        inv[x] = i
    return tuple(inv)


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


# ------------------------------------------------------------------ k-sets
def ksets(n, k):
    """All k-subsets of range(n) as a (colex-ranked) int64 array."""
    from itertools import combinations
    arr = np.fromiter((x for c in combinations(range(n), k) for x in c), dtype=np.int64,
                      count=comb(n, k) * k).reshape(-1, k)
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

    def text(self):
        lines = [f"p cnf {self.nv} {len(self.clauses)}"]
        lines.extend(" ".join(map(str, c)) + " 0" for c in self.clauses)
        return "\n".join(lines) + "\n"

    def write(self, path):
        data = self.text().encode()
        with xopen(path, "xb") as f:
            f.write(data)
        return hashlib.sha256(data).hexdigest()


def parse_status(stdout):
    st, model = "UNKNOWN", set()
    for line in stdout.splitlines():
        if line.startswith("s "):
            st = {"s SATISFIABLE": "SAT", "s UNSATISFIABLE": "UNSAT"}.get(line.strip(), "UNKNOWN")
        elif line.startswith("v "):
            for x in line[2:].split():
                xi = int(x)
                if xi > 0:
                    model.add(xi)
    return st, model


def kissat(path, timeout, seed=0, log=None):
    cmd = ["kissat", "-q", f"--time={int(timeout)}", f"--seed={seed}", path]
    t0 = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True)
    dt = time.time() - t0
    if log:
        with xopen(log) as f:
            f.write(" ".join(cmd) + "\n" + p.stdout + "\n--stderr--\n" + p.stderr)
    st, model = parse_status(p.stdout)
    return st, model, dt


def sha256_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()
