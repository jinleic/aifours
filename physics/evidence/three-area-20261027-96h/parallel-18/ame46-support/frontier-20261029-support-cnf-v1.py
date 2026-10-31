#!/usr/bin/env python3
"""DIMACS generator for NECESSARY support conditions of an AME(4,6) state.

Variables: e_w (nonmaximal support word) and p_w (modulus-1/6 word), w in [6]^4,
numbered e_w = 1 + id(w), p_w = 1297 + id(w), id(w) = 216a+36b+6c+d.
For every one of the six coordinate-pair systems and every value v in [6]^2:
  * at most one p word carries v; a p-carried value carries no e word;
  * otherwise v carries between 2 and MAXM e words (no empty or singleton row).
For every 2|2 cut: two rows (columns) sharing a nonzero column (row) share another
one (complex-unitary orthogonality).  Exactly T values of the 01-pair system are
p-carried (equivalently sum p = T); if MAXM > 2, also sum e <= E.
Optional symmetry break: word 0000 is a p word (valid when T >= 1).
A SAT answer is only a candidate SUPPORT (no amplitudes); UNSAT is solver output.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

PAIRS = list(itertools.combinations(range(4), 2))
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
WORDS = list(itertools.product(range(6), repeat=4))


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.clauses.append(c)

    def at_most_k(self, xs, k):
        """Sinz sequential counter (sound and complete for 'at most k')."""
        n = len(xs)
        if k >= n:
            return
        if k == 0:
            for x in xs:
                self.add([-x])
            return
        s = [[self.var() for _ in range(k)] for _ in range(n - 1)]
        self.add([-xs[0], s[0][0]])
        for j in range(1, k):
            self.add([-s[0][j]])
        for i in range(1, n - 1):
            self.add([-xs[i], s[i][0]])
            self.add([-s[i - 1][0], s[i][0]])
            for j in range(1, k):
                self.add([-xs[i], -s[i - 1][j - 1], s[i][j]])
                self.add([-s[i - 1][j], s[i][j]])
            self.add([-xs[i], -s[i - 1][k - 1]])
        self.add([-xs[n - 1], -s[n - 2][k - 1]])

    def at_least_k(self, xs, k):
        self.at_most_k([-x for x in xs], len(xs) - k)


def build(T, EN, MAXM, sym):
    cnf = CNF()
    e = {w: cnf.var() for w in WORDS}
    p = {w: cnf.var() for w in WORDS}
    for w in WORDS:
        cnf.add([-e[w], -p[w]])
    q = {}
    for (i, j) in PAIRS:
        for x, y in itertools.product(range(6), repeat=2):
            W = [w for w in WORDS if w[i] == x and w[j] == y]
            for u, v in itertools.combinations(W, 2):
                cnf.add([-p[u], -p[v]])
            for u in W:
                for v in W:
                    if u != v:
                        cnf.add([-p[u], -e[v]])
            ps = [p[u] for u in W]
            for u in W:
                cnf.add(ps + [e[v] for v in W if v != u])
            cnf.at_most_k([e[u] for u in W], MAXM)
            if (i, j) == (0, 1):
                qv = cnf.var()
                q[(x, y)] = qv
                for u in W:
                    cnf.add([-p[u], qv])
                cnf.add([-qv] + ps)
    for rows, cols in CUTS:
        R = list(itertools.product(range(6), repeat=2))

        def word(r, c):
            w = [0] * 4
            w[rows[0]], w[rows[1]] = r
            w[cols[0]], w[cols[1]] = c
            return tuple(w)
        for side in (0, 1):
            for r1, r2 in itertools.combinations(R, 2):
                pair = {}
                for c in R:
                    a, b = (word(r1, c), word(r2, c)) if side == 0 else (word(c, r1), word(c, r2))
                    pair[c] = (a, b)
                aux = {}
                for c in R:
                    a, b = pair[c]
                    s = cnf.var()
                    aux[c] = s
                    cnf.add([-s, e[a]])
                    cnf.add([-s, e[b]])
                for c in R:
                    a, b = pair[c]
                    cnf.add([-e[a], -e[b]] + [aux[d] for d in R if d != c])
    qs = list(q.values())
    cnf.at_most_k(qs, T)
    cnf.at_least_k(qs, T)
    if MAXM > 2:
        cnf.at_most_k([e[w] for w in WORDS], EN)
    if sym:
        cnf.add([p[(0, 0, 0, 0)]])
    return cnf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('T', type=int)
    ap.add_argument('E', type=int)
    ap.add_argument('MAXM', type=int)
    ap.add_argument('out', type=Path)
    ap.add_argument('--no-sym', action='store_true')
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    cnf = build(a.T, a.E, a.MAXM, not a.no_sym)
    with a.out.open('x') as f:
        f.write(f'p cnf {cnf.nv} {len(cnf.clauses)}\n')
        for c in cnf.clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    meta = {'T': a.T, 'E': a.E, 'MAXM': a.MAXM, 'sym_0000_in_P': not a.no_sym, 'vars': cnf.nv,
            'clauses': len(cnf.clauses), 'cnf_sha256': hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out) + '.meta.json').open('x') as f:
        f.write(json.dumps(meta, indent=2) + '\n')
    print(json.dumps(meta))


if __name__ == '__main__':
    main()
