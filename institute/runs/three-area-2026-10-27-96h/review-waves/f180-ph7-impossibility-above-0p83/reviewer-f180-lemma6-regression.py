#!/usr/bin/env python3
"""Reviewer-authored regression control for Lemma 6 (NOT a proof; the written
proof is reconstructed in review-v1.md).

(E) EXACT: for seeded random rational 7x7 Metzler matrices G whose bidirected
pairs have square products, enumerate all extra cycles (one-way directed cycles,
virtual F-cycles with omega=(sqrt w+ - sqrt w-)^2 = w+ + w- - 2 s_Gamma), and verify
exactly the coefficient relations
   e1(A)-c[6]=0, e2(A)-c[5]=0, e3(A)-c[4]=W3, e4(A)-c[3]=T3+W4,
   e5(A)-c[2]=a2+b1+W5, e6(A)-c[1]=a3+b2+c1+W6-P33
where A=-S (S geometric symmetrization), c[k]=[y^k]det(yI-G), sums over extra
cycles C of size 3,4,5,6 with U = V minus C, P33 = sum over unordered vertex-disjoint
pairs of 3-cycles.
(F) FLOAT diagnostic: with v = sorted eigenvalues of A (numpy), check every
intermediate inequality of the proof and Y1+ >= 0, Y2b >= 0, K >= 0, beta < 0."""
import sys, itertools, random, time, math
from fractions import Fraction as Fr
import numpy as np
T0 = time.time()

def det(M):
    n = len(M); M = [row[:] for row in M]; d = Fr(1)
    for i in range(n):
        piv = next((r for r in range(i, n) if M[r][i] != 0), None)
        if piv is None: return Fr(0)
        if piv != i: M[i], M[piv] = M[piv], M[i]; d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            if M[r][i] != 0:
                f = M[r][i] / M[i][i]
                for c in range(i, n): M[r][c] -= f * M[i][c]
    return d

def ek_principal(M, idx, k):
    """e_k of the eigenvalues of the principal submatrix M[idx,idx] = sum of k x k principal minors"""
    if k == 0: return Fr(1)
    return sum((det([[M[i][j] for j in J] for i in J]) for J in itertools.combinations(idx, k)), Fr(0))

def charpoly_coeffs(G):
    """c[k] = [y^k] det(yI - G), n=7: c[k] = (-1)^(n-k) e_{n-k}(G)"""
    n = len(G); V = list(range(n))
    return {k: (-1) ** (n - k) * ek_principal(G, V, n - k) for k in range(n + 1)}

def rand_metzler(rng, density):
    n = 7; G = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r = rng.random()
            if r < density * 0.5:            # bidirected with square product
                a = Fr(rng.randint(1, 9), rng.randint(1, 4)); m = Fr(rng.randint(1, 5), rng.randint(1, 3)); k = Fr(rng.randint(1, 5), rng.randint(1, 3))
                G[i][j] = a * m * m; G[j][i] = a * k * k
            elif r < density:                # one-way edge
                if rng.random() < 0.5: G[i][j] = Fr(rng.randint(1, 9), rng.randint(1, 4))
                else: G[j][i] = Fr(rng.randint(1, 9), rng.randint(1, 4))
    for i in range(n):
        G[i][i] = -(sum(G[i][j] for j in range(n) if j != i) + Fr(rng.randint(1, 30), rng.randint(1, 5)))
    return G

def sqrt_fr(x):
    if x == 0: return Fr(0)
    p, q = x.numerator, x.denominator; rp, rq = math.isqrt(p), math.isqrt(q)
    assert rp * rp == p and rq * rq == q, 'not a square'
    return Fr(rp, rq)

def extra_cycles(G):
    n = len(G); out = []
    bid = lambda i, j: G[i][j] > 0 and G[j][i] > 0
    for k in range(3, n + 1):
        for Sset in itertools.combinations(range(n), k):
            first, rest = Sset[0], Sset[1:]
            seen_und = set()
            for perm in itertools.permutations(rest):
                cyc = (first,) + perm
                edges = [(cyc[t], cyc[(t + 1) % k]) for t in range(k)]
                if all(G[a][b] > 0 for a, b in edges) and any(G[b][a] == 0 for a, b in edges):
                    w = Fr(1)
                    for a, b in edges: w *= G[a][b]
                    out.append((frozenset(Sset), w, 'oneway'))
                key = min(cyc[1:], (cyc[1:])[::-1])
                if key in seen_und: continue
                seen_und.add(key)
                if all(bid(a, b) for a, b in edges):
                    wp = Fr(1); wm = Fr(1); s = Fr(1)
                    for a, b in edges:
                        wp *= G[a][b]; wm *= G[b][a]; s *= sqrt_fr(G[a][b] * G[b][a])
                    out.append((frozenset(Sset), wp + wm - 2 * s, 'virtual'))
    return out

rng = random.Random(1829)
nexact = 0; nfloat = 0; worst = {}
TRIALS = [(0.35, s) for s in range(4)] + [(0.6, s) for s in range(4)] + [(0.85, s) for s in range(3)]
for density, s in TRIALS:
    G = rand_metzler(rng, density); n = 7; V = list(range(n))
    S = [[G[i][i] if i == j else sqrt_fr(G[i][j] * G[j][i]) for j in range(n)] for i in range(n)]
    A = [[-S[i][j] for j in range(n)] for i in range(n)]
    c = charpoly_coeffs(G); e = {k: ek_principal(A, V, k) for k in range(8)}
    cyc = extra_cycles(G)
    W = {k: sum((w for Cs, w, _ in cyc if len(Cs) == k), Fr(0)) for k in range(3, 8)}
    comp = lambda Cs: [i for i in V if i not in Cs]
    T3 = sum((w * ek_principal(A, comp(Cs), 1) for Cs, w, _ in cyc if len(Cs) == 3), Fr(0))
    a2 = sum((w * ek_principal(A, comp(Cs), 2) for Cs, w, _ in cyc if len(Cs) == 3), Fr(0))
    a3 = sum((w * ek_principal(A, comp(Cs), 3) for Cs, w, _ in cyc if len(Cs) == 3), Fr(0))
    b1 = sum((w * ek_principal(A, comp(Cs), 1) for Cs, w, _ in cyc if len(Cs) == 4), Fr(0))
    b2 = sum((w * ek_principal(A, comp(Cs), 2) for Cs, w, _ in cyc if len(Cs) == 4), Fr(0))
    c1 = sum((w * ek_principal(A, comp(Cs), 1) for Cs, w, _ in cyc if len(Cs) == 5), Fr(0))
    three = [(Cs, w) for Cs, w, _ in cyc if len(Cs) == 3]
    P33 = sum((w1 * w2 for (C1, w1), (C2, w2) in itertools.combinations(three, 2) if not (C1 & C2)), Fr(0))
    ok = (e[1] - c[6] == 0 and e[2] - c[5] == 0 and e[3] - c[4] == W[3] and e[4] - c[3] == T3 + W[4]
          and e[5] - c[2] == a2 + b1 + W[5] and e[6] - c[1] == a3 + b2 + c1 + W[6] - P33)
    nexact += ok
    print('trial density %.2f seed %d: extra cycles %d (virtual %d), P33 %s, exact y^6..y^1 relations %s' % (
        density, s, len(cyc), sum(1 for x in cyc if x[2] == 'virtual'), 'nonzero' if P33 else '0', 'PASS' if ok else 'FAIL'))
    # float diagnostic of the inequality chain
    v = np.sort(np.linalg.eigvalsh(np.array([[float(x) for x in row] for row in A])))
    if v[0] <= 0:
        print('   (A not positive definite; float diagnostic skipped)'); continue
    E4, E3, E2, E1 = float(e[3] - c[4]), float(e[4] - c[3]), float(e[5] - c[2]), float(e[6] - c[1])
    W3, W4, W5 = float(W[3]), float(W[4]), float(W[5])
    e2_ = lambda xs: sum(a * b for a, b in itertools.combinations(xs, 2)); e3_ = lambda xs: sum(a * b * cc for a, b, cc in itertools.combinations(xs, 3))
    S4 = v[:4].sum(); S3 = v[:3].sum(); m2 = e2_(v[:4]); L4 = v[3:].sum(); s12 = v[0] + v[1]
    alpha = e3_(v[:4]) - s12 * e2_(v[3:]); beta = e2_(v[:3]) - s12 * (v[4] + v[5] + v[6])
    K = E3 - E4 * S4
    Y2b = E2 - E4 * m2 - S3 * (E3 - E4 * L4)
    Y1p = E1 - s12 * E2 - E4 * alpha - K * beta + E4 * E4 / 2
    margins = {'a3>=W3 e3(v1..4)': float(a3) - W3 * e3_(v[:4]), 'b2>=W4 e2(v1..3)': float(b2) - W4 * e2_(v[:3]),
               'c1>=W5(v1+v2)': float(c1) - W5 * s12, 'a2<=W3 e2(v4..7)': W3 * e2_(v[3:]) - float(a2),
               'b1<=W4(v5+v6+v7)': W4 * (v[4] + v[5] + v[6]) - float(b1), 'P33<=W3^2/2': W3 * W3 / 2 - float(P33),
               'W4<=K': K - W4, '-beta>0': -beta, 'K>=0': K, 'Y2b>=0': Y2b, 'Y1+>=0': Y1p}
    scale = 1 + max(abs(E1), abs(E2), abs(E3), abs(E4)) * (1 + v[-1]) ** 3
    bad = [k for k, m in margins.items() if m < -1e-9 * scale]
    nfloat += not bad
    for k, m in margins.items(): worst[k] = min(worst.get(k, float('inf')), m / scale)
    print('   float: v1=%.4g v7=%.4g, inequality chain %s, Y1+ = %.6g' % (v[0], v[-1], 'OK' if not bad else 'VIOLATED ' + str(bad), Y1p))
print('exact coefficient relations PASS on %d/%d trials; float inequality chain OK on %d trials' % (nexact, len(TRIALS), nfloat))
print('min normalised margins:', {k: '%.3g' % m for k, m in worst.items()})
print('seconds', round(time.time() - T0, 1))
sys.exit(0 if nexact == len(TRIALS) else 1)
