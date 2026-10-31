#!/usr/bin/env python3
"""Exact rational sanity check of the cover decomposition used to extend the
no-two-cycle theorem to graphs whose bidirected part is reversible.

For random rational 7x7 Metzler matrices G (seeded), G2 keeps the diagonal and
every entry G_ij with G_ij*G_ji>0.  When G2 is reversible (bidirected graph a
forest, or a bidirected triangle obeying Kolmogorov's product equality), the
identities

  [y^6..y^5] det(yI-G) = [y^6..y^5] det(yI-G2),
  [y^4] det(yI-G) = [y^4] det(yI-G2) - W1,
  [y^3] det(yI-G) = [y^3] det(yI-G2) - sum_t w_t tr(-G_{V\\t}) - C4one

are verified EXACTLY, where W1/C4one sum one-way directed 3-/4-cycles (cycles
using an edge outside G2).  This is a regression check of a standard
permutation-expansion identity, not a proof of it; the proof is written.
"""
import itertools, random, sys
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-localdeps'))
import sympy as S

def charpoly(M):
    y = S.symbols('y')
    return S.Poly(S.Matrix(M).charpoly(y).as_expr(), y).all_coeffs()  # descending, det(yI-M)
def one_way_cycles(G, G2, k):
    n = len(G); out = []
    for verts in itertools.combinations(range(n), k):
        a = verts[0]
        for rest in itertools.permutations(verts[1:]):
            seq = (a,) + rest
            edges = [(seq[i], seq[(i + 1) % k]) for i in range(k)]
            w = Q(1)
            for i, j in edges: w *= G[i][j]
            if w == 0: continue
            if all(G2[i][j] != 0 for i, j in edges): continue  # cycle inside G2
            out.append((seq, w))
    return out
def build(rng, mode):
    n = 7; G = [[Q(0)] * n for _ in range(n)]
    rnd = lambda: Q(rng.randint(1, 9), rng.randint(1, 5))
    if mode == 'forest':
        perm = list(range(n)); rng.shuffle(perm)
        for k in range(1, n):
            if rng.random() < 0.6:
                i, j = perm[rng.randrange(k)], perm[k]; G[i][j] = rnd(); G[j][i] = rnd()
    else:  # balanced bidirected triangle on 0,1,2 plus a forest edge 2-3
        a, b, c, d = rnd(), rnd(), rnd(), rnd(); e = rnd()
        G[0][1], G[1][0] = a, b; G[1][2], G[2][1] = c, d
        G[2][0] = e; G[0][2] = a * c * e / (b * d)        # Kolmogorov: 0->1->2->0 equals 0->2->1->0
        G[2][3], G[3][2] = rnd(), rnd()
    added = 0
    while added < 9:
        i, j = rng.randrange(n), rng.randrange(n)
        if i == j or G[i][j] != 0 or G[j][i] != 0: continue
        G[i][j] = rnd(); added += 1
    for i in range(n): G[i][i] = -(sum(G[i]) + Q(rng.randint(0, 3), 4))
    G2 = [[G[i][j] if (i == j or G[i][j] * G[j][i] != 0) else Q(0) for j in range(n)] for i in range(n)]
    return G, G2
rng = random.Random(20261029)
for trial in range(6):
    mode = 'forest' if trial < 4 else 'kolmogorov-triangle'
    G, G2 = build(rng, mode)
    cG, c2 = charpoly(G), charpoly(G2)
    t3 = one_way_cycles(G, G2, 3); t4 = one_way_cycles(G, G2, 4)
    W1 = sum((w for _, w in t3), Q(0))
    CW = sum((w * sum(-G[k][k] for k in range(7) if k not in seq) for seq, w in t3), Q(0))
    C4 = sum((w for _, w in t4), Q(0))
    assert cG[1] == c2[1] and cG[2] == c2[2], trial
    assert cG[3] == c2[3] - W1, trial
    assert cG[4] == c2[4] - CW - C4, trial
    print(mode, 'trial', trial, 'exact identities PASS; one-way 3-cycles', len(t3), '4-cycles', len(t4))
print('PASS: exact reversible-part cover identities on all seeded trials')
