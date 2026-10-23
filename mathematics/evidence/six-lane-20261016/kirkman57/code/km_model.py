"""Kramer–Mesner exact-cover model for an LSTS/LKTS with a prescribed group.

Model.  G acts on points 0..n-1.  The constituents fall into G-orbits; orbit j
has a base constituent S_j with stabilizer exactly-containing H_j (given).  The
large set is { g S_j : j, g in G/H_j }.  For every G-orbit O of triples exactly
one base j takes exactly one H_j-orbit W inside O, and every triple of W must
have G-stabilizer contained in H_j (equivalently |W| = |H_j||O|/|G|).  Each S_j
must be an STS: every H_j-orbit of pairs is covered exactly once.

This module only builds rows/columns; solving is done elsewhere.
"""
from __future__ import annotations

import collections

import numpy as np

from lkts_core import (closure, pair_images, pair_index_tables, triple_images,
                       triple_index_tables)


class KMModel:
    def __init__(self, n, G_gens, bases, names=None):
        self.n = n
        self.G = closure(G_gens, n)
        self.order = len(self.G)
        self.H = [closure(h, n) for h in bases]
        Gset = set(self.G)
        for h in self.H:
            assert set(h) <= Gset, "H_j must be a subgroup of G"
        self.names = names or [f"S{j}" for j in range(len(bases))]
        self.trip, self.tid = triple_index_tables(n)
        self.pairs, self.pid = pair_index_tables(n)
        self.timg = triple_images(self.G, self.trip, self.tid)
        self.trep = self.timg.min(axis=0)
        self.orbits = collections.defaultdict(list)
        for k, r in enumerate(self.trep.tolist()):
            self.orbits[r].append(k)
        self.orbit_ids = sorted(self.orbits)
        self._build()

    def _build(self):
        n = self.n
        trip = self.trip
        # pairs of every triple as pair ids
        tp = np.stack([self.pid[trip[:, 0], trip[:, 1]],
                       self.pid[trip[:, 0], trip[:, 2]],
                       self.pid[trip[:, 1], trip[:, 2]]], axis=1)
        self.tp = tp
        self.rows = []  # (orbit_rep, base j, tuple(sorted triple ids of W), cols)
        self.cols = set()
        self.pair_orbit = []
        self.pair_orbit_size = []
        for j, H in enumerate(self.H):
            pimg = pair_images(H, self.pairs, self.pid)
            prep = pimg.min(axis=0)
            self.pair_orbit.append(prep)
            cnt = collections.Counter(prep.tolist())
            self.pair_orbit_size.append(cnt)
        for O in self.orbit_ids:
            members = np.array(self.orbits[O])
            osize = len(members)
            for j, H in enumerate(self.H):
                hord = len(H)
                need = hord * osize
                if need % self.order:
                    continue
                need //= self.order  # required |W|
                Harr = np.array(H, dtype=np.int32)
                sub = trip[members]
                himg = self.tid[Harr[:, sub[:, 0]], Harr[:, sub[:, 1]], Harr[:, sub[:, 2]]]
                hrep = himg.min(axis=0)
                groups = collections.defaultdict(list)
                for t, r in zip(members.tolist(), hrep.tolist()):
                    groups[r].append(t)
                prep = self.pair_orbit[j]
                psz = self.pair_orbit_size[j]
                for r, W in groups.items():
                    if len(W) != need:
                        continue
                    c = collections.Counter()
                    for t in W:
                        for p in tp[t]:
                            c[int(prep[p])] += 1
                    ok = True
                    cols = [("O", O)]
                    for q, m in c.items():
                        if m % psz[q]:
                            raise AssertionError("non-integral pair coverage")
                        mult = m // psz[q]
                        if mult != 1:
                            ok = False
                            break
                        cols.append(("P", j, q))
                    if not ok:
                        continue
                    self.rows.append((O, j, tuple(sorted(W)), tuple(cols)))
                    self.cols.update(cols)
        # every pair orbit of every base must be coverable
        for j in range(len(self.H)):
            for q in self.pair_orbit_size[j]:
                self.cols.add(("P", j, q))
        for O in self.orbit_ids:
            self.cols.add(("O", O))

    def summary(self):
        by_base = collections.Counter(r[1] for r in self.rows)
        orb_sizes = collections.Counter(len(self.orbits[O]) for O in self.orbit_ids)
        return {
            "group_order": self.order,
            "base_orders": [len(h) for h in self.H],
            "triple_orbits": len(self.orbit_ids),
            "triple_orbit_sizes": sorted(orb_sizes.items()),
            "rows": len(self.rows),
            "rows_by_base": {self.names[j]: by_base[j] for j in range(len(self.H))},
            "columns": len(self.cols),
            "pair_orbits_by_base": [len(c) for c in self.pair_orbit_size],
        }

    def base_blocks(self, solution_rows):
        """Return list (per base) of triple-id sets for a chosen set of rows."""
        out = [set() for _ in self.H]
        for ri in solution_rows:
            O, j, W, cols = self.rows[ri]
            out[j].update(W)
        return out

    def develop(self, base_sets):
        """All constituents as lists of triple ids, by G-coset development."""
        Gl = self.G
        cons = []
        for j, S in enumerate(base_sets):
            Hset = set(self.H[j])
            seen = set()
            Sarr = np.array(sorted(S))
            for gi, g in enumerate(Gl):
                img = frozenset(self.timg[gi, Sarr].tolist())
                if img in seen:
                    continue
                seen.add(img)
                cons.append(sorted(img))
            assert len(seen) == self.order // len(Hset), (len(seen), self.order, len(Hset))
        return cons


def exact_cover(rows_cols, all_cols, limit=1, time_limit=None, order_key=None):
    """Knuth Algorithm X with MRV.  rows_cols: list of column-tuples.
    Yields solutions as lists of row indices."""
    import time
    t0 = time.time()
    X = {c: set() for c in all_cols}
    Y = {}
    for i, cols in enumerate(rows_cols):
        Y[i] = cols
        for c in cols:
            X[c].add(i)
    sol = []
    found = 0

    def select(r):
        removed = []
        for j in Y[r]:
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].remove(i)
            removed.append(X.pop(j))
        return removed

    def deselect(r, removed):
        for j in reversed(Y[r]):
            X[j] = removed.pop()
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].add(i)

    stats = {"nodes": 0}

    def solve():
        nonlocal found
        if time_limit is not None and time.time() - t0 > time_limit:
            raise TimeoutError
        if not X:
            found += 1
            yield list(sol)
            return
        c = min(X, key=lambda c: len(X[c]))
        cand = list(X[c])
        if order_key is not None:
            cand.sort(key=order_key)
        for r in cand:
            stats["nodes"] += 1
            sol.append(r)
            removed = select(r)
            yield from solve()
            deselect(r, removed)
            sol.pop()
            if limit is not None and found >= limit:
                return

    yield from solve()


def km_cnf(M, extra_forbid=()):
    """CNF: one var per row; exactly-one per column."""
    from satlib import CNF
    cnf = CNF()
    rv = [cnf.var() for _ in M.rows]
    bycol = {c: [] for c in M.cols}
    for i, r in enumerate(M.rows):
        for c in r[3]:
            bycol[c].append(rv[i])
    for c, lits in bycol.items():
        if not lits:
            cnf.add([])  # unsatisfiable column
        else:
            cnf.exactly_one(lits)
    for cl in extra_forbid:
        cnf.add(cl)
    return cnf, rv
