#!/usr/bin/env python3
"""Exact complex-phase solver for zero-excess AME(4,6) supports.

A support splits into P (words isolated in every pair system) and E. In the
zero-excess case every E row and column of every 2|2 flattening has exactly two
entries and the E part of each flattening is a disjoint union of full 2x2 blocks.
By the block lemma (Pandya arXiv:2610.16673v1 Lemma 1, reproved in the packet):
with all E moduli 1/sqrt72 and P moduli 1/6, the state is AME iff for every block
(rows r,r', columns c,c') of every cut  phi_rc - phi_rc' - phi_r'c + phi_r'c' = pi
(mod 2pi).  Writing phi = 2 pi psi, this is M psi = 1/2 (mod Z^m).  It is solvable
over R iff every integer left-kernel vector y of M has even coordinate sum; the
real (sign-only) version is the stronger F2 condition.  When solvable, a rational
solution is produced and the resulting tensor is verified EXACTLY in Z[zeta_L]
(polynomial reduction modulo the cyclotomic polynomial) for all three cuts.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import itertools
import json
from math import gcd
from pathlib import Path

CUTS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
PAIRS = list(itertools.combinations(range(4), 2))
WORDS = list(itertools.product(range(6), repeat=4))


class Fail(ValueError):
    pass


def load_model(path):
    true = set()
    for line in path.read_text().splitlines():
        if line.startswith('v '):
            true.update(int(t) for t in line[2:].split() if int(t) > 0)
    E = sorted(w for k, w in enumerate(WORDS) if 1 + k in true)
    P = sorted(w for k, w in enumerate(WORDS) if 1297 + k in true)
    return E, P


def load_pandya(path):
    E, P = [], []
    signs = {}
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        a, b, *terms = line.split()
        for t in terms:
            w = (int(a), int(b), int(t[1]), int(t[2]))
            if t[0] == 's':
                P.append(w)
            else:
                E.append(w)
                signs[w] = 0 if t[0] == '+' else 1
    return sorted(E), sorted(P), signs


def blocks(E, P):
    """Return list of blocks (r1,r2,c1,c2 words) for each cut; verify zero excess."""
    Eset, Pset = set(E), set(P)
    if Eset & Pset:
        raise Fail('E and P overlap')
    for i, j in PAIRS:
        cnt = defaultdict(int)
        for w in P:
            cnt[(w[i], w[j])] += 10
        for w in E:
            cnt[(w[i], w[j])] += 1
        for v in itertools.product(range(6), repeat=2):
            if cnt[v] not in (2, 10):
                raise Fail(f'pair system {(i, j)} value {v} has code {cnt[v]}')
    out = []
    for rows, cols in CUTS:
        R = defaultdict(set)
        for w in E:
            R[(w[rows[0]], w[rows[1]])].add((w[cols[0]], w[cols[1]]))
        seen = set()
        bl = []
        for r1 in sorted(R):
            if r1 in seen:
                continue
            partners = [r for r in R if r != r1 and R[r] & R[r1]]
            if len(partners) != 1 or R[partners[0]] != R[r1] or len(R[r1]) != 2:
                raise Fail('residual is not a union of full 2x2 blocks')
            r2 = partners[0]
            seen |= {r1, r2}
            c1, c2 = sorted(R[r1])

            def w(r, c):
                x = [0] * 4
                x[rows[0]], x[rows[1]] = r
                x[cols[0]], x[cols[1]] = c
                return tuple(x)
            bl.append((w(r1, c1), w(r1, c2), w(r2, c1), w(r2, c2)))
        out.append(bl)
    return out


def hnf_with_transform(M):
    """Integer row reduction: returns (H, U) with U unimodular, U M = H echelon."""
    m = len(M)
    n = len(M[0]) if m else 0
    A = [list(row) + [1 if k == i else 0 for k in range(m)] for i, row in enumerate(M)]
    piv_row = 0
    pivots = []
    for col in range(n):
        if piv_row >= m:
            break
        while True:
            nz = [i for i in range(piv_row, m) if A[i][col] != 0]
            if not nz:
                break
            best = min(nz, key=lambda i: abs(A[i][col]))
            A[piv_row], A[best] = A[best], A[piv_row]
            done = True
            for i in range(piv_row + 1, m):
                if A[i][col]:
                    q = A[i][col] // A[piv_row][col]
                    A[i] = [x - q * y for x, y in zip(A[i], A[piv_row])]
                    if A[i][col]:
                        done = False
            if done:
                break
        if any(A[i][col] for i in range(piv_row, m)):
            pivots.append(col)
            piv_row += 1
    H = [row[:n] for row in A]
    U = [row[n:] for row in A]
    return H, U, pivots


def solve(E, P, bl):
    idx = {w: k for k, w in enumerate(E)}
    M = []
    for cutbl in bl:
        for a, b, c, d in cutbl:
            row = [0] * len(E)
            row[idx[a]] += 1
            row[idx[b]] -= 1
            row[idx[c]] -= 1
            row[idx[d]] += 1
            M.append(row)
    H, U, pivots = hnf_with_transform(M)
    r = len(pivots)
    kernel = U[r:]
    sums = [sum(y) for y in kernel]
    complex_ok = all(s % 2 == 0 for s in sums)
    # real F2 solvability: M t = 1 over F2
    rows2 = [(sum((x & 1) << k for k, x in enumerate(row)), 1) for row in M]
    piv2 = {}
    real_ok = True
    for mbits, rhs in rows2:
        while mbits:
            h = mbits.bit_length() - 1
            if h in piv2:
                pm, pr = piv2[h]
                mbits ^= pm
                rhs ^= pr
            else:
                piv2[h] = (mbits, rhs)
                break
        else:
            if rhs:
                real_ok = False
    res = {'equations': len(M), 'variables': len(E), 'integer_rank': r,
           'integer_left_kernel_dimension': len(kernel), 'kernel_vector_sums': sums,
           'complex_phase_solvable': complex_ok, 'real_sign_solvable': real_ok}
    if not complex_ok:
        return res, None
    half = [Fraction(1, 2)] * len(M)
    Uc = [sum(Fraction(u) * c for u, c in zip(urow, half)) for urow in U]
    for i in range(r, len(M)):
        if Uc[i].denominator != 1:
            raise Fail('kernel condition mismatch')
    psi = [Fraction(0)] * len(E)
    for i in reversed(range(r)):
        col = pivots[i]
        acc = Uc[i] - sum(Fraction(H[i][k]) * psi[k] for k in range(col + 1, len(E)))
        psi[col] = acc / H[i][col]
    for row, val in zip(M, [Fraction(1, 2)] * len(M)):
        s = sum(Fraction(x) * p for x, p in zip(row, psi))
        if (s - val).denominator != 1:
            raise Fail('rational solution does not satisfy congruences')
    L = 2
    for p in psi:
        L = L * p.denominator // gcd(L, p.denominator)
    expo = {w: int((psi[idx[w]] * L) % L) for w in E}
    return res, (L, expo)


def poly_mod(a, m):
    a = list(a)
    while len(a) >= len(m):
        c = a[-1]
        if c:
            s = len(a) - len(m)
            for k, mk in enumerate(m):
                a[s + k] -= c * mk
        a.pop()
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_divexact(a, b):
    a = list(a)
    q = [0] * (len(a) - len(b) + 1)
    for i in reversed(range(len(q))):
        c = a[i + len(b) - 1] // b[-1]
        q[i] = c
        for k, bk in enumerate(b):
            a[i + k] -= c * bk
    if any(a):
        raise Fail('inexact polynomial division')
    return q


def cyclotomic(L):
    phi = {}
    for d in range(1, L + 1):
        if L % d:
            continue
        p = [-1] + [0] * (d - 1) + [1]
        for e in range(1, d):
            if d % e == 0:
                p = poly_divexact(p, phi[e])
        phi[d] = p
    return phi[L]


def verify_exact(E, P, L, expo):
    """Build all three flattenings and check F F^dagger = 2 I exactly in Z[zeta_L, sqrt2]."""
    PhiL = cyclotomic(L)
    Pset = set(P)
    checks = 0
    for rows, cols in CUTS:
        F = defaultdict(dict)
        for w in E:
            F[(w[rows[0]], w[rows[1]])][(w[cols[0]], w[cols[1]])] = ('E', expo[w])
        for w in P:
            F[(w[rows[0]], w[rows[1]])][(w[cols[0]], w[cols[1]])] = ('P', None)
        keys = list(itertools.product(range(6), repeat=2))
        for r1 in keys:
            for r2 in keys:
                poly = [0] * L
                sqrt2_sq = 0
                for c, (k1, e1) in F[r1].items():
                    if c not in F[r2]:
                        continue
                    k2, e2 = F[r2][c]
                    if k1 == 'P' and k2 == 'P':
                        sqrt2_sq += 1
                    elif k1 == 'E' and k2 == 'E':
                        poly[(e1 - e2) % L] += 1
                    else:
                        raise Fail('P and E share a column')
                poly[0] += 2 * sqrt2_sq
                target = 2 if r1 == r2 else 0
                poly[0] -= target
                if poly_mod(poly, PhiL):
                    raise Fail(f'Gram entry wrong at cut {rows} rows {r1},{r2}')
                checks += 1
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source', type=Path)
    ap.add_argument('out', type=Path)
    ap.add_argument('--pandya', action='store_true')
    a = ap.parse_args()
    if a.out.exists():
        raise SystemExit('refusing to overwrite')
    raw = a.source.read_bytes()
    if a.pandya:
        E, P, signs = load_pandya(a.source)
    else:
        E, P = load_model(a.source)
    bl = blocks(E, P)
    res, sol = solve(E, P, bl)
    res.update({'source_sha256': hashlib.sha256(raw).hexdigest(), 'support': len(E) + len(P),
                'E': len(E), 'P': len(P), 'blocks_per_cut': [len(x) for x in bl]})
    if sol is not None:
        L, expo = sol
        res['phase_denominator_L'] = L
        res['exact_gram_entries_checked'] = verify_exact(E, P, L, expo)
        res['exact_AME_verified'] = True
        res['witness'] = {'E_words_and_zeta_L_exponents': [[list(w), expo[w]] for w in E],
                          'P_words_coefficient_one_sixth': [list(w) for w in P],
                          'normalization': 'psi_w = zeta_L^{a_w}/sqrt72 on E, 1/6 on P'}
    with a.out.open('x') as f:
        f.write(json.dumps(res, indent=1) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k != 'witness'}))


if __name__ == '__main__':
    try:
        main()
    except Fail as exc:
        raise SystemExit(f'FAIL: {exc}')
