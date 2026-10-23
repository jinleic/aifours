#!/usr/bin/env python3
"""ame_e0n_cnf.py: N-only CNF for the e = 0 case (lane ame46-support).

Relaxation of ame_e0_cnf.py in which the classical officers are eliminated. Only the non-classical support N is
encoded; the classical part enters through necessary conditions it imposes on N (review/LEMMAS, Lemmas 9 and 11):
  every P-line contains 0 or exactly 2 elements of N (hole lines: exactly 2; classical lines: 0);
  hole indicator hl_L <-> (line L meets N); for every pair P, exactly h = 36 - t hole lines;
  slice consistency: for every coordinate i and value a, the number d_{i,a} of hole lines (a, b) is the same for
  every partner coordinate j != i (it equals 6 - t_{i,a});
  row overlap in every reshaping (2x2 block property under exact-two lines);
  optional SB (tau = max slice count of classical officers, review/LEMMAS 6, expressed on holes):
  every d_{i,a} >= 6 - tau, and the hole lines of slice (1, 0) are exactly (0, b), b >= tau, for each partner j;
  optional phase-obstruction families TBL and TWIN (six-element clauses).
UNSAT of this CNF excludes every AME state with e = 0 and the given t (and tau). Satisfying assignments are only
candidates: the classical completion and the full phase system must still be checked.
"""
import argparse
import itertools
import json

import ame_e0_cnf as base

R = range(6)


def build(t, tau=None, phase=("TBL", "TWIN")):
    h = 36 - t
    F = base.CNF()
    F.nv = 1296                     # only n_x variables, 1 + idx(x)
    lines = [(P, z) for P in base.PAIRS for z in itertools.product(R, repeat=2)]
    hl = {}
    for (P, z) in lines:
        mem = base.line_members(P, z)
        ns = [F.n(x) for x in mem]
        v = F.new()
        hl[(P, z)] = v
        F.add([-v] + ns)
        for nx in ns:
            F.add([-nx, v])
        for x in mem:
            F.add([-F.n(x)] + [F.n(y) for y in mem if y != x])
        F.at_most_k(ns, 2)
    for P in base.PAIRS:
        lits = [hl[(P, z)] for z in itertools.product(R, repeat=2)]
        F.at_most_k(lits, h)
        F.at_least_k(lits, h)

    def slice_lines(i, a, j):
        P = (min(i, j), max(i, j))
        return [hl[(P, (a, b) if P[0] == i else (b, a))] for b in R]

    # unary counters (totalizer-free: compare via sorting networks is overkill; use pairwise count equality through
    # "at least m" indicators defined exactly with sequential counters on 6 inputs)
    def geq_indicators(lits):
        """Return g[m] (m = 1..6) with g[m] <-> (at least m of lits). Exact definition by DP over prefixes."""
        n = len(lits)
        prev = {0: None}
        # dp[i][m]: at least m among first i
        dp = [[None] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for m in range(1, i + 1):
                v = F.new()
                dp[i][m] = v
                x = lits[i - 1]
                a = dp[i - 1][m] if m <= i - 1 else None          # at least m among first i-1
                b = dp[i - 1][m - 1] if m - 1 >= 1 else "T"       # at least m-1 among first i-1
                # v <-> a or (b and x)
                if a is not None:
                    F.add([-a, v])
                if b == "T":
                    F.add([-x, v])
                    F.add([-v, x] + ([a] if a is not None else []))
                else:
                    F.add([-b, -x, v])
                    F.add([-v, b] + ([a] if a is not None else []))
                    F.add([-v, x] + ([a] if a is not None else []))
        return {m: dp[n][m] for m in range(1, n + 1)}

    for i in range(4):
        others = [j for j in range(4) if j != i]
        for a in R:
            G = {j: geq_indicators(slice_lines(i, a, j)) for j in others}
            for j, k in zip(others, others[1:]):
                for m in range(1, 7):
                    F.add([-G[j][m], G[k][m]])
                    F.add([G[j][m], -G[k][m]])
            if tau is not None and tau < 6:
                # tau* < 6 means no fully classical slice, so every d_{i,a} >= 6 - tau
                F.add([G[others[0]][6 - tau]])
    if tau is not None:
        for j in (1, 2, 3):
            for b, v in zip(R, slice_lines(0, 0, j)):
                F.add([v] if b >= tau else [-v])
    for rows, cols in base.RESHAPINGS:
        rvals = list(itertools.product(R, repeat=2))
        for r1, r2 in itertools.combinations(rvals, 2):
            aux = {}

            def el(r, c):
                x = [0] * 4
                x[rows[0]], x[rows[1]] = r
                x[cols[0]], x[cols[1]] = c
                return tuple(x)
            for cv in rvals:
                a_ = F.new()
                aux[cv] = a_
                F.add([-a_, F.n(el(r1, cv))])
                F.add([-a_, F.n(el(r2, cv))])
            for cv in rvals:
                F.add([-F.n(el(r1, cv)), -F.n(el(r2, cv))] + [aux[c2] for c2 in rvals if c2 != cv])
    if "TBL" in phase:
        for s in base.tbl_sets():
            F.add([-F.n(x) for x in s])
    if "TWIN" in phase:
        for s in base.twin_sets():
            F.add([-F.n(x) for x in s])
    return F


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--tau", type=int, default=None)
    ap.add_argument("--phase", default="TBL,TWIN")
    ap.add_argument("out")
    a = ap.parse_args()
    phase = tuple(p for p in a.phase.split(",") if p)
    F = build(a.t, a.tau, phase)
    base.write(F, a.out, {"model": "e0 N-only", "t": a.t, "tau": a.tau, "phase": list(phase)})
    print(a.out, F.nv, len(F.clauses))


if __name__ == "__main__":
    main()
