#!/usr/bin/env python3
"""Exact checks for the explicit 4x5 PPT Schmidt-number-three source state.

State (reconstructed from Krebs-Gachechiladze, arXiv:2509.07086v1, Theorem 5, Eq. (11)):
  rho = [e0] + [e1] + [e2] + 3([02+34] + [20+33] + [04] + [23] + [30] + [32]),
  e0=|00>+|11>+|22>, e1=|01>+|12>, e2=|10>-|21>, Alice index first (4), Bob second (5).
Checks: exact PSD ranks of rho and its Bob partial transpose by Fraction Schur pivots,
and an exact degree-4 integer polynomial identity putting psi00^4 in the ideal of
3x3 minors of the range coordinate matrix (range criterion for Schmidt number >= 3).
"""
from fractions import Fraction as F
from itertools import combinations
import json

dA, dB = 4, 5
N = dA * dB
def ket(terms):
    v = [0] * N
    for a, b, c in terms:
        v[a * dB + b] += c
    return v
vecs = [ket([(0, 0, 1), (1, 1, 1), (2, 2, 1)]), ket([(0, 1, 1), (1, 2, 1)]), ket([(1, 0, 1), (2, 1, -1)]),
        ket([(0, 2, 1), (3, 4, 1)]), ket([(2, 0, 1), (3, 3, 1)]), ket([(0, 4, 1)]), ket([(2, 3, 1)]),
        ket([(3, 0, 1)]), ket([(3, 2, 1)])]
wts = [1, 1, 1, 3, 3, 3, 3, 3, 3]
rho = [[F(0)] * N for _ in range(N)]
for w, v in zip(wts, vecs):
    for i in range(N):
        if v[i]:
            for j in range(N):
                if v[j]:
                    rho[i][j] += w * v[i] * v[j]
def ptB(M):
    R = [[F(0)] * N for _ in range(N)]
    for a in range(dA):
        for b in range(dB):
            for c in range(dA):
                for d in range(dB):
                    R[a * dB + d][c * dB + b] = M[a * dB + b][c * dB + d]
    return R
def psd_rank(M):
    A = [r[:] for r in M]; rank = 0
    while A:
        if any(A[i][i] < 0 for i in range(len(A))):
            return None
        k = next((i for i in range(len(A)) if A[i][i] > 0), None)
        if k is None:
            return rank if all(x == 0 for row in A for x in row) else None
        p = A[k][k]; J = [i for i in range(len(A)) if i != k]
        A = [[A[i][j] - A[i][k] * A[k][j] / p for j in J] for i in J]; rank += 1
    return rank
r_rho, r_pt = psd_rank(rho), psd_rank(ptB(rho))
assert r_rho == 9 and r_pt == 10

# Polynomials in the 9 range coordinates psi00,psi01,psi02,psi04,psi10,psi20,psi23,psi30,psi32.
NV = 9
def var(i):
    e = [0] * NV; e[i] = 1; return {tuple(e): 1}
def padd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
        if r[k] == 0:
            del r[k]
    return r
def pmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x + y for x, y in zip(k1, k2)); r[k] = r.get(k, 0) + v1 * v2
            if r[k] == 0:
                del r[k]
    return r
def det3(M):
    out = {}
    for perm, sg in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
        out = padd(out, pmul(pmul(M[0][perm[0]], M[1][perm[1]]), M[2][perm[2]]), sg)
    return out
p00, p01, p02, p04, p10, p20, p23, p30, p32 = [var(i) for i in range(NV)]
Z = {}
m10 = {k: -v for k, v in p10.items()}
# Coordinate matrix of a general range vector (rows Alice 0..3, columns Bob 0..4).
Psi = [[p00, p01, p02, Z, p04], [p10, p00, p01, Z, Z], [p20, m10, p00, p23, Z], [p30, Z, p32, p20, p02]]
def minor(R, C):
    return det3([[Psi[r][c] for c in C] for r in R])
# Range vectors expressed in coordinates: map coordinate i -> the range vector it multiplies.
assign = {0: vecs[0], 1: vecs[1], 4: vecs[2], 2: vecs[3], 5: vecs[4], 3: vecs[5], 6: vecs[6], 7: vecs[7], 8: vecs[8]}
for a in range(dA):
    for b in range(dB):
        lin = [0] * NV
        for k, c in Psi[a][b].items():
            lin[k.index(1)] = c
        assert all(lin[i] == assign[i][a * dB + b] for i in range(NV)), (a, b)
identity = {}
for coef, mult, R, C in [(1, p00, (0, 1, 2), (0, 1, 2)), (-1, p00, (0, 1, 3), (1, 2, 3)), (-1, p00, (1, 2, 3), (0, 1, 4)),
                         (F(-1, 2), p02, (0, 1, 3), (0, 1, 3)), (F(-1, 2), p20, (1, 2, 3), (1, 2, 4))]:
    identity = padd(identity, {k: coef * v for k, v in pmul(mult, minor(R, C)).items()})
identity = {k: v for k, v in identity.items() if v != 0}
assert identity == {(4, 0, 0, 0, 0, 0, 0, 0, 0): 1}
print(json.dumps({
    'rho_PSD_rank': r_rho, 'rho_partial_transpose_PSD_rank': r_pt,
    'range_coordinates_match_nine_vectors': True,
    'degree4_identity': 'psi00^4 = psi00*M[012|012] - psi00*M[013|123] - psi00*M[123|014] - (1/2)psi02*M[013|013] - (1/2)psi20*M[123|124]',
    'consequence': 'every Schmidt-rank<=2 vector in range(rho) has psi00=0, while e0 in range(rho) has psi00=1; range criterion gives SN(rho)>=3',
    'scope': 'exact Fraction/integer arithmetic; minors M[R|C] are 3x3 minors with Alice rows R and Bob columns C'}, indent=2))
