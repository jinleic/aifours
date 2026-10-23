"""Generalized Kramer–Mesner model: base j has G-stabilizer H_j and is required
to be invariant under a (possibly larger, not-in-G) group K_j with K_j ∩ G = H_j.
Rows are K_j-orbits U of triples such that U meets every G-orbit in either
nothing or exactly one H_j-orbit whose triples have G-stabilizer inside H_j,
and U covers every K_j-orbit of pairs at most once.  Columns: G-orbits
(exactly once) and per-base K_j pair orbits (exactly once)."""
from __future__ import annotations

import collections

import numpy as np

from lkts_core import closure, pair_images, pair_index_tables, triple_images, triple_index_tables


class KM2:
    def __init__(self, n, G_gens, bases, names=None):
        self.n = n
        self.G = closure(G_gens, n)
        self.order = len(self.G)
        Gset = set(self.G)
        self.H, self.K = [], []
        for Hg, Kg in bases:
            H = closure(Hg, n)
            K = closure(list(Hg) + list(Kg), n)
            assert set(H) <= Gset
            assert set(K) & Gset == set(H), "K_j ∩ G must equal H_j"
            self.H.append(H)
            self.K.append(K)
        self.names = names or [f"S{j}" for j in range(len(bases))]
        self.trip, self.tid = triple_index_tables(n)
        self.pairs, self.pid = pair_index_tables(n)
        timg = triple_images(self.G, self.trip, self.tid)
        self.timg = timg
        self.grep = timg.min(axis=0)
        self.gsize = collections.Counter(self.grep.tolist())
        self.orbit_ids = sorted(self.gsize)
        tp = np.stack([self.pid[self.trip[:, 0], self.trip[:, 1]],
                       self.pid[self.trip[:, 0], self.trip[:, 2]],
                       self.pid[self.trip[:, 1], self.trip[:, 2]]], axis=1)
        self.tp = tp
        self.rows = []
        self.cols = set(("O", O) for O in self.orbit_ids)
        for j in range(len(bases)):
            self._rows_for_base(j)

    def _rows_for_base(self, j):
        H, K = self.H[j], self.K[j]
        hord = len(H)
        Harr = np.array(H, dtype=np.int32)
        hrep = self.tid[Harr[:, self.trip[:, 0]], Harr[:, self.trip[:, 1]], Harr[:, self.trip[:, 2]]].min(axis=0)
        hsize = collections.Counter(hrep.tolist())
        Karr = np.array(K, dtype=np.int32)
        krep = self.tid[Karr[:, self.trip[:, 0]], Karr[:, self.trip[:, 1]], Karr[:, self.trip[:, 2]]].min(axis=0)
        pk = pair_images(K, self.pairs, self.pid).min(axis=0)
        pksize = collections.Counter(pk.tolist())
        for q in pksize:
            self.cols.add(("P", j, q))
        kgroups = collections.defaultdict(list)
        for t, r in enumerate(krep.tolist()):
            kgroups[r].append(t)
        for r, U in kgroups.items():
            # G-orbit decomposition of U
            byO = collections.defaultdict(list)
            for t in U:
                byO[int(self.grep[t])].append(t)
            ok = True
            for O, ts in byO.items():
                hs = {int(hrep[t]) for t in ts}
                if len(hs) != 1:
                    ok = False
                    break
                h = next(iter(hs))
                need = hord * self.gsize[O]
                if need % self.order or hsize[h] != need // self.order:
                    ok = False
                    break
            if not ok:
                continue
            c = collections.Counter()
            for t in U:
                for p in self.tp[t]:
                    c[int(pk[p])] += 1
            cols = [("O", O) for O in sorted(byO)]
            for q, m in c.items():
                if m != pksize[q]:
                    ok = False
                    break
                cols.append(("P", j, q))
            if not ok:
                continue
            self.rows.append((j, tuple(sorted(U)), tuple(cols)))

    def summary(self):
        by = collections.Counter(r[0] for r in self.rows)
        return {"G": self.order, "H": [len(h) for h in self.H], "K": [len(k) for k in self.K],
                "rows": len(self.rows), "rows_by_base": {self.names[j]: by[j] for j in range(len(self.H))},
                "cols": len(self.cols)}

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

    def develop(self, base_sets):
        cons = []
        for j, S in enumerate(base_sets):
            Sarr = np.array(sorted(S))
            seen = set()
            for gi in range(self.order):
                img = frozenset(self.timg[gi, Sarr].tolist())
                if img not in seen:
                    seen.add(img)
                    cons.append(sorted(img))
            assert len(seen) == self.order // len(self.H[j])
        return cons
