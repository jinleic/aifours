"""Kramer–Mesner model for a CQS(g^n : s) WITH STEM invariant under a permutation group (README A0).
Adapted from the copied code/cqs_km.py (empty stem; sha256 810a3914…f5a7): group_of[p] = -1 marks a stem
point.  A 3-subset is NOT coverable iff its non-stem points (at least one, s <= 2) lie in one group, i.e. it is
contained in S ∪ G for a group G.  Columns: G-orbits of coverable 3-subsets.  Rows: G-orbits of 4-subsets
containing no non-coverable 3-subset whose development covers every triple of each column it meets exactly
once (orbit-size condition).  Generators must preserve the group partition and the stem."""
from __future__ import annotations

import lane_guard  # noqa: F401

import collections

import numpy as np

from lanelib import CNF, ksets, orbit_labels, rank


def _bad3(gA, gB, gC):
    """non-coverable: every entry is -1 (stem) or equal to the largest entry (the unique group)."""
    M = np.maximum(np.maximum(gA, gB), gC)
    return ((gA == -1) | (gA == M)) & ((gB == -1) | (gB == M)) & ((gC == -1) | (gC == M))


class CQSKMS:
    def __init__(self, n_points, group_of, gens):
        self.n = n_points
        self.group_of = np.asarray(group_of, dtype=np.int64)
        assert int((self.group_of == -1).sum()) <= 2, "at most two stem points supported"
        self.gens = [tuple(g) for g in gens]
        for g in self.gens:
            img = {}
            for x in range(self.n):
                img.setdefault(int(self.group_of[x]), set()).add(int(self.group_of[g[x]]))
            assert all(len(s) == 1 for s in img.values()), "generator does not preserve the groups"
            assert img.get(-1, {-1}) == {-1}, "generator does not preserve the stem"
        T = ksets(self.n, 3)
        Q = ksets(self.n, 4)
        gT_ = self.group_of[T]
        gQ_ = self.group_of[Q]
        t_bad = _bad3(gT_[:, 0], gT_[:, 1], gT_[:, 2])
        q_bad = np.zeros(len(Q), dtype=bool)
        for a, b, c in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
            q_bad |= _bad3(gQ_[:, a], gQ_[:, b], gQ_[:, c])
        self.T, self.Q = T, Q
        self.t_valid = ~t_bad
        self.q_valid = ~q_bad
        imT = [rank(np.asarray(g, dtype=np.int64)[T]) for g in self.gens]
        imQ = [rank(np.asarray(g, dtype=np.int64)[Q]) for g in self.gens]
        self.LT = orbit_labels(imT)
        self.LQ = orbit_labels(imQ)
        sizeT = collections.Counter(self.LT[self.t_valid].tolist())
        sizeQ = collections.Counter(self.LQ[self.q_valid].tolist())
        assert not (set(self.LT[~self.t_valid].tolist()) & set(sizeT)), "orbit mixes coverable/non-coverable triples"
        self.sizeT, self.sizeQ = sizeT, sizeQ
        self.tcols = sorted(sizeT)
        self.colidx = {c: i for i, c in enumerate(self.tcols)}
        tri = np.stack([rank(Q[:, [1, 2, 3]]), rank(Q[:, [0, 2, 3]]), rank(Q[:, [0, 1, 3]]),
                        rank(Q[:, [0, 1, 2]])], axis=1)
        self.rows, self.bad_rows = [], 0
        for lab in sorted(sizeQ):
            tl = self.LT[tri[lab]]
            c = collections.Counter(tl.tolist())
            ok = all(t in sizeT and sizeQ[lab] * m == sizeT[t] for t, m in c.items())
            if ok:
                self.rows.append((lab, tuple(sorted(self.colidx[t] for t in c))))
            else:
                self.bad_rows += 1

    def summary(self):
        return {
            "points": self.n, "coverable_triples": int(self.t_valid.sum()),
            "valid_4sets": int(self.q_valid.sum()), "columns": len(self.tcols),
            "column_orbit_sizes": dict(sorted(collections.Counter(self.sizeT.values()).items())),
            "quad_orbits": len(self.sizeQ), "valid_rows": len(self.rows), "invalid_rows": self.bad_rows,
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
        mask = np.isin(self.LQ, labs) & self.q_valid
        return [tuple(int(x) for x in b) for b in self.Q[mask]]
