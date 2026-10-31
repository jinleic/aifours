#!/usr/bin/env python3
"""proof-control-t30-sat-v1.py  (reviewer-authored, f113 review)

Generates DIMACS CNF instances for the purely combinatorial content of the
t=30 case of any AME(4,6) state in a product basis.  Nothing from Sections
2-5 of the candidate is imported; only the premise's residual lemma is used
to define the abstraction, and (in modes 'eonly' and 'full') the premise's
incidence-lemma consequence r_i <= 3 is used as a WLOG relabeling
E subset {0,1,2}^4.  Mode 'unres' drops even that and lets E range over
[6]^4.

Abstraction of t=30 (n=6), for each coordinate pair ij and each cell
(a,b) in [6]^2 of the ij|kl flattening: either the cell is a P-cell
(exactly one P word projects to it, no E word) or an E-cell (no P word,
at least two E words).  Exactly 6 E-cells per pair (36 - t).  Any AME(4,6)
state with t=30 yields a model (P = modulus-1/6 positions, E = other
nonzero positions).  UNSAT therefore excludes t=30.

Modes:
  eonly : E variables only (no P).  Tests whether condition (1) with six
          6-cell projections is satisfiable by SOME E subset {0,1,2}^4 at all.
  full  : P in [6]^4, E in {0,1,2}^4.
  unres : P in [6]^4, E in [6]^4 (no r_i<=3 import).
Usage: python3 -B proof-control-t30-sat-v1.py <mode> <out.cnf> [n]
  Optional n (default 6) = residual size 36-t; then exactly n E-cells per
  pair and, in 'full'/'eonly' modes, E subset {0..r-1}^4 with
  r = floor(3n/5) (premise incidence bound).  n=6 reproduces the original.
"""
import itertools, sys
from pathlib import Path

PAIRS = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]


class CNF:
    def __init__(self):
        self.n = 0
        self.clauses = []
    def var(self):
        self.n += 1
        return self.n
    def add(self, *lits):
        self.clauses.append(tuple(lits))
    def write(self, path):
        with Path(path).open('x', encoding='utf-8') as fh:
            fh.write(f'p cnf {self.n} {len(self.clauses)}\n')
            for c in self.clauses:
                fh.write(' '.join(map(str, c)) + ' 0\n')


def exactly_k_seq(cnf, xs, k):
    """Exact Sinz-style sequential counter: s[i][j] <-> (at least j+1 of
    x_0..x_i are true).  Then sum(xs) == k  <=>  s[n-1][k-1] and not s[n-1][k]."""
    n = len(xs)
    s = [[cnf.var() for _ in range(k + 1)] for _ in range(n)]
    for i in range(n):
        x = xs[i]
        cnf.add(-x, s[i][0])
        if i == 0:
            cnf.add(-s[0][0], x)
            for j in range(1, k + 1):
                cnf.add(-s[0][j])
            continue
        for j in range(k + 1):
            cnf.add(-s[i-1][j], s[i][j])
        for j in range(1, k + 1):
            cnf.add(-x, -s[i-1][j-1], s[i][j])
        cnf.add(-s[i][0], s[i-1][0], x)
        for j in range(1, k + 1):
            cnf.add(-s[i][j], s[i-1][j], x)
            cnf.add(-s[i][j], s[i-1][j], s[i-1][j-1])
    cnf.add(s[n-1][k-1])
    cnf.add(-s[n-1][k])


def build(mode, n=6):
    cnf = CNF()
    q = 6
    ealph = range(3 * n // 5) if mode in ('eonly', 'full') else range(q)
    E = {w: cnf.var() for w in itertools.product(ealph, repeat=4)}
    P = {}
    if mode != 'eonly':
        P = {w: cnf.var() for w in itertools.product(range(q), repeat=4)}
    for (i, j) in PAIRS:
        ocells = []
        for a in range(q):
            for b in range(q):
                o = cnf.var()
                ocells.append(o)
                ecell = [E[w] for w in E if w[i] == a and w[j] == b]
                pcell = [P[w] for w in P if w[i] == a and w[j] == b]
                # o -> at least two E words in the cell
                if len(ecell) < 2:
                    cnf.add(-o)
                else:
                    for v in ecell:
                        cnf.add(-o, *[u for u in ecell if u != v])
                # not o -> no E word in the cell
                for v in ecell:
                    cnf.add(o, -v)
                if P:
                    # o -> no P word; not o -> exactly one P word
                    for v in pcell:
                        cnf.add(-o, -v)
                    cnf.add(o, *pcell)
                    for u, v in itertools.combinations(pcell, 2):
                        cnf.add(-u, -v)
        exactly_k_seq(cnf, ocells, n)
    return cnf, E, P


def main():
    mode, out = sys.argv[1], sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    cnf, E, P = build(mode, n)
    cnf.write(out)
    print(f'mode={mode} n={n} vars={cnf.n} clauses={len(cnf.clauses)} E_vars={len(E)} P_vars={len(P)}')
    with Path(out + '.map').open('x', encoding='utf-8') as fh:
        for w, v in E.items():
            fh.write(f'E {v} {" ".join(map(str, w))}\n')
        for w, v in P.items():
            fh.write(f'P {v} {" ".join(map(str, w))}\n')


if __name__ == '__main__':
    main()
