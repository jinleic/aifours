"""Memory-efficient Kramer–Mesner builder (same model as km2.KM2) for larger v.

Triples are ranked in colex order (rank = C(c,3)+C(b,2)+a for a<b<c); group
orbits are computed by union-find over generator images only (no |G|×C(v,3)
table).  Interface mirrors KM2: rows (j, U, cols), cols, cnf(), bases_from(),
plus `G` (group element list) for development.
"""
from __future__ import annotations

import collections

import numpy as np

from lkts_core import closure, inverse


def comb2(x):
    return x * (x - 1) // 2


def comb3(x):
    return x * (x - 1) * (x - 2) // 6


def all_triples(n):
    A, B, C = [], [], []
    for c in range(2, n):
        b = np.repeat(np.arange(1, c), np.arange(1, c))
        a = np.concatenate([np.arange(0, bb) for bb in range(1, c)])
        A.append(a); B.append(b); C.append(np.full(len(a), c))
    A = np.concatenate(A).astype(np.int64); B = np.concatenate(B).astype(np.int64); C = np.concatenate(C).astype(np.int64)
    return A, B, C


def rank3(a, b, c):
    s = np.sort(np.stack([a, b, c]), axis=0)
    return comb3(s[2]) + comb2(s[1]) + s[0]


def rank2(a, b):
    lo = np.minimum(a, b); hi = np.maximum(a, b)
    return comb2(hi) + lo


def orbit_labels(images):
    """images: list of int arrays (permutations of range(T)); returns min-label per item."""
    T = len(images[0])
    L = np.arange(T, dtype=np.int64)
    inv = [np.empty_like(im) for im in images]
    for im, iv in zip(images, inv):
        iv[im] = np.arange(T)
    allimg = images + inv
    while True:
        old = L.copy()
        for im in allimg:
            np.minimum(L, L[im], out=L)
        for _ in range(4):
            L = L[L]
        if np.array_equal(L, old):
            return L


class KM3:
    def __init__(self, n, G_gens, bases, names=None):
        self.n = n
        self.names = names or [f"S{j}" for j in range(len(bases))]
        self.A, self.B, self.C = all_triples(n)
        T = len(self.A)
        self.trip = np.stack([self.A, self.B, self.C], axis=1)
        pa = np.array([[a, b] for b in range(n) for a in range(b)], dtype=np.int64)
        self.PA, self.PB = pa[:, 0], pa[:, 1]

        def timg(g):
            g = np.asarray(g, dtype=np.int64)
            return rank3(g[self.A], g[self.B], g[self.C])

        def pimg(g):
            g = np.asarray(g, dtype=np.int64)
            return rank2(g[self.PA], g[self.PB])

        self.G = closure(G_gens, n)
        self.order = len(self.G)
        Gset = set(self.G)
        self.LG = orbit_labels([timg(g) for g in G_gens])
        self.gsize = collections.Counter(self.LG.tolist())
        self.orbit_ids = sorted(self.gsize)
        # pairs of each triple
        self.tp = np.stack([rank2(self.A, self.B), rank2(self.A, self.C), rank2(self.B, self.C)], axis=1)
        self.rows = []
        self.cols = set(("O", O) for O in self.orbit_ids)
        self.H, self.K = [], []
        for j, (Hg, Kg) in enumerate(bases):
            H = closure(Hg, n) if Hg else [tuple(range(n))]
            K = closure(list(Hg) + list(Kg), n)
            assert set(H) <= Gset and set(K) & Gset == set(H)
            self.H.append(H); self.K.append(K)
            LH = orbit_labels([timg(g) for g in Hg]) if Hg else np.arange(T)
            hsize = collections.Counter(LH.tolist())
            kg = list(Hg) + list(Kg)
            LK = orbit_labels([timg(g) for g in kg]) if kg else np.arange(T)
            PK = orbit_labels([pimg(g) for g in kg]) if kg else np.arange(len(self.PA))
            pksize = np.bincount(PK, minlength=len(PK))
            for qcol in np.unique(PK):
                self.cols.add(("P", j, int(qcol)))
            order = np.argsort(LK, kind="stable")
            Ls = LK[order]
            cuts = np.flatnonzero(np.diff(Ls)) + 1
            groups = np.split(order, cuts)
            hord = len(H)
            for U in groups:
                gl = self.LG[U]
                ok = True
                for O in np.unique(gl):
                    ts = U[gl == O]
                    hs = np.unique(LH[ts])
                    if len(hs) != 1:
                        ok = False; break
                    need = hord * self.gsize[int(O)]
                    if need % self.order or hsize[int(hs[0])] != need // self.order:
                        ok = False; break
                if not ok:
                    continue
                pl = PK[self.tp[U].ravel()]
                cnt = collections.Counter(pl.tolist())
                if any(c != pksize[p] for p, c in cnt.items()):
                    continue
                cols = [("O", int(O)) for O in sorted(set(gl.tolist()))] + [("P", j, int(p)) for p in cnt]
                self.rows.append((j, tuple(int(t) for t in U), tuple(cols)))

    def summary(self):
        by = collections.Counter(r[0] for r in self.rows)
        return {"G": self.order, "H": [len(h) for h in self.H], "K": [len(k) for k in self.K],
                "rows": len(self.rows), "rows_by_base": {self.names[j]: by[j] for j in range(len(self.H))},
                "cols": len(self.cols), "triple_orbits": len(self.orbit_ids)}

    def cnf(self):
        from satlib import CNF
        cnf = CNF()
        rv = [cnf.var() for _ in self.rows]
        bycol = {c: [] for c in self.cols}
        for i, r in enumerate(self.rows):
            for c in r[2]:
                bycol[c].append(rv[i])
        for c, lits in bycol.items():
            if not lits:
                cnf.add([])
            else:
                cnf.exactly_one(lits)
        return cnf, rv

    def bases_from(self, sel):
        out = [set() for _ in self.H]
        for i in sel:
            j, U, _ = self.rows[i]
            out[j].update(U)
        return out

    def blocks(self, tset):
        return sorted(tuple(int(x) for x in self.trip[t]) for t in tset)
