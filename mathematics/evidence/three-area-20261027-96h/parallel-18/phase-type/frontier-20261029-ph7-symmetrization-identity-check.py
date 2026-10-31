#!/usr/bin/env python3
"""Exact rational regression check of the geometric-symmetrization cover identity

    det(yI-G) = sum_L prod_{C in L}(-omega_C) det((yI-S)_{V minus cup L})

for seven-state Metzler matrices G with arbitrary support, where S_ii=G_ii,
S_ij=sqrt(G_ij G_ji), L ranges over sets of pairwise disjoint EXTRA cycles:
one-way directed cycles (omega=w, using an edge whose reverse is absent) and
virtual cycles (undirected cycles of the bidirected graph F of length>=3,
omega=(sqrt(w+)-sqrt(w-))^2).  Bidirected pairs are generated with
G_ij*G_ji a rational square, so S and every omega are rational and the FULL
polynomial identity (all eight coefficients) is checked exactly.  A Ky Fan
diagonal-sum check and a spectral-bound comparison are printed as floating
diagnostics only.  This is regression evidence for the written lemma.
"""
import itertools, random, sys
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S
y = S.symbols('y')

def det_poly(M, idx):
    if not idx: return S.Integer(1)
    sub = S.Matrix([[M[i][j] for j in idx] for i in idx])
    return S.expand((y * S.eye(len(idx)) - sub).det(method='berkowitz'))
def build(rng, density):
    n = 7; G = [[Q(0)] * n for _ in range(n)]; Sm = [[Q(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r = rng.random()
            if r < density * 0.45:      # bidirected pair with square product
                m = Q(rng.randint(1, 6), rng.randint(1, 3)); t = Q(rng.randint(1, 5), rng.randint(1, 5))
                G[i][j], G[j][i] = m * t, m / t; Sm[i][j] = Sm[j][i] = m
            elif r < density:           # one-way edge, random direction
                if rng.random() < 0.5: G[i][j] = Q(rng.randint(1, 9), rng.randint(1, 4))
                else: G[j][i] = Q(rng.randint(1, 9), rng.randint(1, 4))
    for i in range(n):
        G[i][i] = -(sum(G[i]) + Q(rng.randint(0, 4), 3)); Sm[i][i] = G[i][i]
    return G, Sm
def extra_cycles(G, Sm):
    n = 7; out = []
    bid = lambda i, j: G[i][j] != 0 and G[j][i] != 0
    for k in range(3, n + 1):
        for verts in itertools.combinations(range(n), k):
            a = verts[0]; seen = set()
            for rest in itertools.permutations(verts[1:]):
                seq = (a,) + rest; edges = [(seq[i], seq[(i + 1) % k]) for i in range(k)]
                w = Q(1)
                for i, j in edges: w *= G[i][j]
                if w == 0: continue
                if all(bid(i, j) for i, j in edges):
                    und = frozenset(frozenset(e) for e in edges)
                    if und in seen: continue
                    seen.add(und)
                    wr = Q(1); sp_ = Q(1)
                    for i, j in edges: wr *= G[j][i]; sp_ *= Sm[i][j]
                    assert sp_ * sp_ == w * wr
                    out.append((frozenset(verts), w + wr - 2 * sp_, 'virtual'))
                else:
                    out.append((frozenset(verts), w, 'one-way'))
    return out
rng = random.Random(20261029)
for trial in range(8):
    density = [0.35, 0.5, 0.65, 0.8][trial % 4]
    G, Sm = build(rng, density)
    lhs = det_poly(G, list(range(7)))
    cyc = extra_cycles(G, Sm)
    cache = {}
    def dS(rest):
        key = tuple(sorted(rest))
        if key not in cache: cache[key] = det_poly(Sm, list(key))
        return cache[key]
    total = dS(range(7)); nL = 1
    # sets of 1 or 2 disjoint extra cycles (three disjoint cycles of length>=3 need >=9 states)
    for vs, om, _ in cyc:
        total -= om * dS([v for v in range(7) if v not in vs]); nL += 1
    for (v1, o1, _), (v2, o2, _) in itertools.combinations(cyc, 2):
        if v1 & v2: continue
        total += o1 * o2 * dS([v for v in range(7) if v not in v1 and v not in v2]); nL += 1
    assert S.expand(lhs - total) == 0, trial
    nvirt = sum(1 for c in cyc if c[2] == 'virtual')
    import numpy as np
    Gf = np.array([[float(x) for x in row] for row in G]); Sf = np.array([[float(x) for x in row] for row in Sm])
    sG = max(np.linalg.eigvals(Gf).real); ev = np.linalg.eigvalsh(-Sf)
    kf = min(sum(-Sf[k][k] for k in J) - sum(sorted(ev)[:4]) for J in itertools.combinations(range(7), 4))
    print(f'trial {trial} density {density}: exact full identity PASS; extra cycles {len(cyc)} (virtual {nvirt}); L-terms {nL}; '
          f'diagnostics s(S)-s(G)={max(-ev)-sG:.3e} (<=0 expected), min KyFan slack={kf:.3e} (>=0 expected)')
print('PASS: exact geometric-symmetrization cover identity on all seeded trials')
