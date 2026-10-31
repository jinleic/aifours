#!/usr/bin/env python3
"""Zero-excess AME(4,6) support CNF with fixed per-party degree profiles (v2).

Models are supports S = P u E such that, for every one of the six pair systems
(i,j) and every value (a,b):
  * either exactly one P word and no E word carries (a,b), or exactly two E words
    and no P word do;
  * the number of E-carried values (a, .) equals the prescribed degree d_i(a);
and in every 2|2 cut two E rows sharing a column share both columns (so the E part
of each flattening is a disjoint union of full 2x2 blocks).  With --real, sign bits
are added so that the +-1 (E) / +-sqrt2 (P) tensor is exactly AME (real orthogonal
blocks).  Without --real a model is only a candidate support; the exact complex
phase solver decides it.  Variables: e_w = 1+id(w), p_w = 1297+id(w),
t_w = 2593+id(w) (sign bits), id(w) = 216 w0 + 36 w1 + 6 w2 + w3.
"""
import argparse
import hashlib
import itertools
import json
import os
from pathlib import Path

PAIRS = list(itertools.combinations(range(4), 2))
CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
WORDS = list(itertools.product(range(6), repeat=4))
R36 = list(itertools.product(range(6), repeat=2))


def wid(w):
    return 216 * w[0] + 36 * w[1] + 6 * w[2] + w[3]


class Writer:
    def __init__(self, path):
        self.body = open(path, 'w')
        self.nv = 3888
        self.nc = 0

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.body.write(' '.join(map(str, c)) + ' 0\n')
        self.nc += 1

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

    def exactly_k(self, xs, k):
        self.at_most_k(xs, k)
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


def build(T, prof, real, fixp, path):
    W = Writer(path)
    e = {w: 1 + wid(w) for w in WORDS}
    p = {w: 1297 + wid(w) for w in WORDS}
    t = {w: 2593 + wid(w) for w in WORDS}
    can_e = {w: all(prof[i][w[i]] > 0 for i in range(4)) for w in WORDS}
    can_p = {w: all(prof[i][w[i]] < 6 for i in range(4)) for w in WORDS}
    for w in WORDS:
        W.add([-e[w], -p[w]])
        if not can_e[w]:
            W.add([-e[w]])
        if not can_p[w]:
            W.add([-p[w]])
        if not real:
            W.add([-t[w]])
    for (i, j) in PAIRS:
        y = {}
        for a, b in R36:
            yv = W.var()
            y[(a, b)] = yv
            Wd = [w for w in WORDS if w[i] == a and w[j] == b]
            Ws = [w for w in Wd if can_e[w]]
            Wp = [w for w in Wd if can_p[w]]
            for u, v in itertools.combinations(Wp, 2):
                W.add([-p[u], -p[v]])
            for u in Wp:
                W.add([-p[u], -yv])
            for u in Ws:
                W.add([-e[u], yv])
            W.add([yv] + [p[u] for u in Wp])
            for u in Ws:
                W.add([-yv] + [e[v] for v in Ws if v != u])
            if len(Ws) < 2:
                W.add([-yv])
            W.at_most_k([e[u] for u in Ws], 2)
        for a in range(6):
            W.exactly_k([y[(a, b)] for b in range(6)], prof[i][a])
        for b in range(6):
            W.exactly_k([y[(a, b)] for a in range(6)], prof[j][b])
    for rows, cols in CUTS:
        def word(r, c):
            x = [0] * 4
            x[rows[0]], x[rows[1]] = r
            x[cols[0]], x[cols[1]] = c
            return tuple(x)
        live_r = [r for r in R36 if prof[rows[0]][r[0]] > 0 and prof[rows[1]][r[1]] > 0]
        live_c = [c for c in R36 if prof[cols[0]][c[0]] > 0 and prof[cols[1]][c[1]] > 0]
        for r1, r2 in itertools.combinations(live_r, 2):
            for c in live_c:
                a1, a2 = e[word(r1, c)], e[word(r2, c)]
                for c2 in live_c:
                    if c2 == c:
                        continue
                    b1, b2 = e[word(r1, c2)], e[word(r2, c2)]
                    W.add([-a1, -a2, -b1, b2])
                    W.add([-a1, -a2, -b2, b1])
        if real:
            sig = {}
            for r in live_r:
                us = []
                for c in live_c:
                    w = word(r, c)
                    u = W.var()
                    W.add([-u, e[w]])
                    W.add([-u, t[w]])
                    W.add([u, -e[w], -t[w]])
                    us.append(u)
                sig[r] = W.xor_chain(us)
            for r1, r2 in itertools.combinations(live_r, 2):
                for c in live_c:
                    a1, a2 = e[word(r1, c)], e[word(r2, c)]
                    W.add([-a1, -a2, sig[r1], sig[r2]])
                    W.add([-a1, -a2, -sig[r1], -sig[r2]])
    if fixp:
        first = []
        for i in range(4):
            low = [a for a in range(6) if prof[i][a] < 6]
            if len({prof[i][a] for a in low}) != 1:
                raise SystemExit('--fix-p needs one degree class below 6 at every party')
            first.append(low[0])
        W.add([p[tuple(first)]])
    W.body.close()
    return W


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('T', type=int)
    ap.add_argument('profiles', help='four comma-separated degree lists joined by "/", e.g. 6,6,3,3,3,3/...')
    ap.add_argument('out', type=Path)
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--fix-p', action='store_true')
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    prof = [list(map(int, s.split(','))) for s in a.profiles.split('/')]
    if len(prof) != 4 or any(len(x) != 6 for x in prof):
        raise SystemExit('need four profiles of six degrees')
    for x in prof:
        if sum(x) != 36 - a.T or any(d == 1 or d < 0 or d > 6 for d in x):
            raise SystemExit(f'profile {x} inconsistent with T={a.T}')
    tmp = Path(str(a.out) + '.body')
    W = build(a.T, prof, a.real, a.fix_p, tmp)
    with a.out.open('x') as f, tmp.open() as b:
        f.write(f'p cnf {W.nv} {W.nc}\n')
        for line in b:
            f.write(line)
    os.replace(tmp, Path(str(a.out) + '.body.consumed'))
    meta = {'T': a.T, 'profiles': prof, 'real_signs': a.real, 'fix_p': a.fix_p, 'vars': W.nv,
            'clauses': W.nc, 'cnf_sha256': hashlib.sha256(a.out.read_bytes()).hexdigest()}
    with Path(str(a.out) + '.meta.json').open('x') as f:
        f.write(json.dumps(meta, indent=2) + '\n')
    print(json.dumps(meta))


if __name__ == '__main__':
    main()
