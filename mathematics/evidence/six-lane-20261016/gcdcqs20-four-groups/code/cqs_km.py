"""Kramer–Mesner model for a CQS(g^n : 0) (empty stem) invariant under a permutation group.

Columns: G-orbits of 3-subsets NOT contained in one group (types 2+1 and 1+1+1).
Rows: G-orbits of 4-subsets with at most two points in every group (types 2+2, 2+1+1,
1+1+1+1) whose development covers every triple of each column it meets exactly once
(orbit-size condition, computed here).  The group must preserve the group partition.
"""
from __future__ import annotations

import lane_guard  # noqa: F401

import collections

import numpy as np

from lanelib import CNF, ksets, orbit_labels, rank


class CQSKM:
    def __init__(self, n_points, group_of, gens):
        self.n = n_points
        self.group_of = np.asarray(group_of, dtype=np.int64)
        self.gens = [tuple(g) for g in gens]
        for g in self.gens:  # the group partition must be preserved
            img = {}
            for x in range(self.n):
                img.setdefault(int(self.group_of[x]), set()).add(int(self.group_of[g[x]]))
            assert all(len(s) == 1 for s in img.values()), "generator does not preserve the groups"
        T = ksets(self.n, 3)
        Q = ksets(self.n, 4)
        gT_ = self.group_of[T]
        gQ_ = self.group_of[Q]
        t_in_group = (gT_[:, 0] == gT_[:, 1]) & (gT_[:, 1] == gT_[:, 2])
        # a 4-set is valid iff no three of its points share a group
        q_bad = np.zeros(len(Q), dtype=bool)
        for a, b, c in ((0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)):
            q_bad |= (gQ_[:, a] == gQ_[:, b]) & (gQ_[:, b] == gQ_[:, c])
        self.T, self.Q = T, Q
        self.t_valid = ~t_in_group
        self.q_valid = ~q_bad
        imT = [rank(np.asarray(g, dtype=np.int64)[T]) for g in self.gens]
        imQ = [rank(np.asarray(g, dtype=np.int64)[Q]) for g in self.gens]
        self.LT = orbit_labels(imT)
        self.LQ = orbit_labels(imQ)
        sizeT = collections.Counter(self.LT[self.t_valid].tolist())
        sizeQ = collections.Counter(self.LQ[self.q_valid].tolist())
        assert not (set(self.LT[~self.t_valid].tolist()) & set(sizeT)), "orbit mixes group/non-group triples"
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
            "points": self.n, "non_group_triples": int(self.t_valid.sum()),
            "valid_4sets": int(self.q_valid.sum()),
            "columns": len(self.tcols),
            "column_orbit_sizes": dict(sorted(collections.Counter(self.sizeT.values()).items())),
            "quad_orbits": len(self.sizeQ),
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
        mask = np.isin(self.LQ, labs) & self.q_valid
        return [tuple(int(x) for x in b) for b in self.Q[mask]]
