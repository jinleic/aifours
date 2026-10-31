#!/usr/bin/env python3
"""CNF whose models are exactly real AME(4,6) tensors of a restricted ansatz.

Ansatz (zero excess, equal moduli): coefficients sqrt(72)*psi_w are
  +-sqrt2 on T words P (isolated in every cut), +-1 on the words E, 0 elsewhere.
Conditions encoded (all necessary AND sufficient for this ansatz to be AME):
  * in each of the six pair systems every value is carried by exactly one P word
    or by exactly two E words (never both);
  * in each cut two E rows (columns) sharing a column (row) share both columns;
  * real orthogonality: for two rows of one 2x2 block the parities of their sign
    bits differ (s11 s12 s21 s22 = -1).  Rows of distinct blocks have disjoint
    supports, so this makes every flattening times 1/sqrt2 orthogonal.
Variables e_w = 1+id(w), p_w = 1297+id(w), t_w = 2593+id(w) (sign bit of E word).
Symmetry break: 0000 in P.  The model checker verifies any model exactly.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

PAIRS = list(itertools.combinations(range(4), 2))
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
WORDS = list(itertools.product(range(6), repeat=4))
R36 = list(itertools.product(range(6), repeat=2))


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

    def xor_chain(self, xs):
        acc = xs[0]
        for x in xs[1:]:
            y = self.var()
            self.add([-acc, -x, -y])
            self.add([acc, x, -y])
            self.add([acc, -x, y])
            self.add([-acc, x, y])
            acc = y
        return acc


def word(rows, cols, r, c):
    w = [0] * 4
    w[rows[0]], w[rows[1]] = r
    w[cols[0]], w[cols[1]] = c
    return tuple(w)


def build(T, sym=True):
    cnf = CNF()
    e = {w: cnf.var() for w in WORDS}
    p = {w: cnf.var() for w in WORDS}
    t = {w: cnf.var() for w in WORDS}
    for w in WORDS:
        cnf.add([-e[w], -p[w]])
    q = []
    for (i, j) in PAIRS:
        for x, y in R36:
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
            cnf.at_most_k([e[u] for u in W], 2)
            if (i, j) == (0, 1):
                qv = cnf.var()
                q.append(qv)
                for u in W:
                    cnf.add([-p[u], qv])
                cnf.add([-qv] + ps)
    u = {}
    for w in WORDS:
        uw = cnf.var()
        u[w] = uw
        cnf.add([-uw, e[w]])
        cnf.add([-uw, t[w]])
        cnf.add([uw, -e[w], -t[w]])
    for rows, cols in CUTS:
        for side in (0, 1):
            sig = {}
            for r in R36:
                line = [word(rows, cols, r, c) if side == 0 else word(rows, cols, c, r) for c in R36]
                sig[r] = cnf.xor_chain([u[w] for w in line])
            for r1, r2 in itertools.combinations(R36, 2):
                aux = {}
                pairs = {}
                for c in R36:
                    a, b = (word(rows, cols, r1, c), word(rows, cols, r2, c)) if side == 0 else (word(rows, cols, c, r1), word(rows, cols, c, r2))
                    pairs[c] = (a, b)
                    s = cnf.var()
                    aux[c] = s
                    cnf.add([-s, e[a]])
                    cnf.add([-s, e[b]])
                for c in R36:
                    a, b = pairs[c]
                    cnf.add([-e[a], -e[b]] + [aux[d] for d in R36 if d != c])
                    cnf.add([-e[a], -e[b], sig[r1], sig[r2]])
                    cnf.add([-e[a], -e[b], -sig[r1], -sig[r2]])
    cnf.at_most_k(q, T)
    cnf.at_least_k(q, T)
    if sym:
        cnf.add([p[(0, 0, 0, 0)]])
    return cnf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('T', type=int)
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    cnf = build(a.T)
    with a.out.open('x') as f:
        f.write(f'p cnf {cnf.nv} {len(cnf.clauses)}\n')
        for c in cnf.clauses:
            f.write(' '.join(map(str, c)) + ' 0\n')
    meta = {'T': a.T, 'ansatz': 'real zero-excess, E=+-1, P=+-sqrt2', 'vars': cnf.nv, 'clauses': len(cnf.clauses),
            'cnf_sha256': hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out) + '.meta.json').open('x') as f:
        f.write(json.dumps(meta, indent=2) + '\n')
    print(json.dumps(meta))


if __name__ == '__main__':
    main()
