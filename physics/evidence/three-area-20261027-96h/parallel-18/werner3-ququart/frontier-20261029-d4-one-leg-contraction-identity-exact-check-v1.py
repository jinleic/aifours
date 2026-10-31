#!/usr/bin/env python3
"""Exact formal check of the one-leg contraction identity (Lemma 5 of the v2 stratified packet).

Instance: d=4, n=2, E=span{e0,e1} at site 1. The identity is checked as an equality of
Hermitian quadratic forms on ALL supported vec C (128 complex coordinates), so it covers every
complex C with the stated leg support. The Haar integral over S(E) is replaced by the six
octahedron (Pauli-eigenstate) points, a spherical 2-design; the integrand has degree (2,2).
Arithmetic: Gaussian rationals built from fractions.Fraction; no floats, no target operator,
no q value of any selected C. Fault controls perturb the identity and must be detected.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json


class G:
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re = Q(re)
        self.im = Q(im)

    def __add__(self, o):
        return G(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def conj(self):
        return G(self.re, -self.im)

    def scale(self, q):
        return G(self.re * q, self.im * q)

    def iszero(self):
        return self.re == 0 and self.im == 0


ZERO = G(0, 0)
ONE = G(1, 0)
I_ = G(0, 1)
D = 4
HALF = Q(1, 2)


def k_entry(x, y, xp, yp):
    """Original local factor K=I-|Omega><Omega|/2 on (output x, input y)."""
    value = Q(1) if (x == xp and y == yp) else Q(0)
    if x == y and xp == yp:
        value -= HALF
    return value


def supported_coords(leg):
    coords = []
    for x1, y1, x2, y2 in product(range(D), repeat=4):
        if leg == 'output' and x1 > 1:
            continue
        if leg == 'input' and y1 > 1:
            continue
        coords.append((x1, y1, x2, y2))
    return coords


def lhs_matrix(coords):
    n = len(coords)
    m = [[ZERO] * n for _ in range(n)]
    for i, (x1, y1, x2, y2) in enumerate(coords):
        for j, (a1, b1, a2, b2) in enumerate(coords):
            v = k_entry(x1, y1, a1, b1) * k_entry(x2, y2, a2, b2)
            if v:
                m[i][j] = G(v, 0)
    return m


def contraction(coords, alpha, beta):
    """L maps vec C to vec X, X=<alpha|C|beta> at site 1; returns dict (x2,y2)->[(col,coeff)]."""
    rows = {}
    for col, (x1, y1, x2, y2) in enumerate(coords):
        coeff = alpha[x1].conj() * beta[y1]
        if not coeff.iszero():
            rows.setdefault((x2, y2), []).append((col, coeff))
    return rows


def add_term(acc, coords, alpha, beta, weight):
    rows = contraction(coords, alpha, beta)
    keys = [(x, y) for x in range(D) for y in range(D)]
    # KL[(x,y)][col] = sum_{(x',y')} K2[(x,y),(x',y')] L[(x',y')][col]
    kl = {}
    for (x, y) in keys:
        line = {}
        for (xp, yp) in keys:
            kv = k_entry(x, y, xp, yp)
            if kv and (xp, yp) in rows:
                for col, c in rows[(xp, yp)]:
                    line[col] = line.get(col, ZERO) + c.scale(kv)
        if line:
            kl[(x, y)] = line
    for (x, y), lrow in rows.items():
        if (x, y) not in kl:
            continue
        for ci, cval in lrow:
            left = cval.conj().scale(weight)
            for cj, kval in kl[(x, y)].items():
                acc[ci][cj] = acc[ci][cj] + left * kval


def vec(*entries):
    out = [ZERO] * D
    for idx, val in entries:
        out[idx] = val
    return out


h = Q(1, 2)
# Octahedron points u with an orthogonal partner u_perp inside E. The four non-basis points are
# stored with norm sqrt2 instead of 1; their factor s=1/2 rescales the quadratic form below.
OCT = [
    (vec((0, ONE)), vec((1, ONE)), Q(1)),
    (vec((1, ONE)), vec((0, ONE)), Q(1)),
    (vec((0, ONE), (1, ONE)), vec((0, ONE), (1, G(-1))), h),
    (vec((0, ONE), (1, G(-1))), vec((0, ONE), (1, ONE)), h),
    (vec((0, ONE), (1, I_)), vec((0, ONE), (1, G(0, -1))), h),
    (vec((0, ONE), (1, G(0, -1))), vec((0, ONE), (1, I_)), h),
]
EBASIS = [vec((0, ONE)), vec((1, ONE))]
FBASIS = [vec((2, ONE)), vec((3, ONE))]


def rhs_matrix(coords, leg, oct_weight=Q(1, 2), drop_finite=False, use_u_twice=False):
    n = len(coords)
    acc = [[ZERO] * n for _ in range(n)]
    for u, up, s in OCT:
        # The contraction X=<alpha|C|beta> is linear in conj(alpha) and in beta, so storing both
        # vectors with norm sqrt2 multiplies X by 2 and q1(X) by 4; the weight s*s=1/4 undoes it.
        partner = u if use_u_twice else up
        if leg == 'output':
            a, b = u, partner
        else:
            a, b = partner, u
        add_term(acc, coords, a, b, oct_weight * s * s)
    if not drop_finite:
        for e in EBASIS:
            for f in FBASIS:
                if leg == 'output':
                    add_term(acc, coords, e, f, Q(1))
                else:
                    add_term(acc, coords, f, e, Q(1))
    return acc


def mismatches(a, b):
    count = 0
    for ra, rb in zip(a, b):
        for x, y in zip(ra, rb):
            if not (x - y).iszero():
                count += 1
    return count


results = {}
for leg in ('output', 'input'):
    coords = supported_coords(leg)
    lhs = lhs_matrix(coords)
    exact = mismatches(lhs, rhs_matrix(coords, leg))
    faults = {
        'wrong_octahedron_weight_1_over_3': mismatches(lhs, rhs_matrix(coords, leg, oct_weight=Q(1, 3))),
        'finite_perp_term_dropped': mismatches(lhs, rhs_matrix(coords, leg, drop_finite=True)),
        'u_used_instead_of_u_perp': mismatches(lhs, rhs_matrix(coords, leg, use_u_twice=True)),
    }
    results[leg] = {
        'supported_complex_coordinates': len(coords),
        'exact_identity_mismatched_entries': exact,
        'fault_mismatched_entries': faults,
        'pass': exact == 0 and all(v > 0 for v in faults.values()),
    }

status = 'PASS' if all(r['pass'] for r in results.values()) else 'FAIL'
record = {
    'status': status,
    'instance': 'd=4, n=2, E=span{e0,e1} at site 1; output-leg identity (5) and input-leg identity (6)',
    'method': 'Exact equality of the 128x128 Hermitian quadratic-form matrices (Gaussian rationals via Fraction) on every supported vec C; Haar integral replaced by the octahedron 2-design (weight 3/6=1/2 per point).',
    'results': results,
    'scope': 'Formal finite check of one instance of the written lemma for ALL supported C; it does not check other d/n, the ladder theorem, spread criterion, any target q value, source certificate, formal kernel, independent review or novelty.',
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out = Path(__file__).resolve().parent / 'frontier-20261029-d4-one-leg-contraction-identity-exact-check-results-v1.json'
out.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
print(json.dumps(record, sort_keys=True))
if status != 'PASS':
    raise SystemExit(1)
