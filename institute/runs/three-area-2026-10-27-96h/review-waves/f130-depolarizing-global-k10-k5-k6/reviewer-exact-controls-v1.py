#!/usr/bin/env python3
"""reviewer-exact-controls-v1.py

Independent exact (Gaussian-rational) controls for review
f130-depolarizing-global-k10-k5-k6.  Written by the reviewer from the
mathematics alone.  Imports no author module and executes no author code;
the three manifest inputs are touched only as raw bytes for SHA-256 receipts.

Run:    python3 -B reviewer-exact-controls-v1.py
Writes: reviewer-exact-controls-v1.result.json next to this file.
Exit 0 iff every control's observed status equals its predicted status
(positive controls must PASS, negative controls must FAIL as predicted).

Conventions (all reviewer's own):
  * qubit site i in {0,1,2,3}; basis label x = 8*x0+4*x1+2*x2+x3, site 0 is
    the leftmost ket symbol / most significant bit.
  * erase(X,i) = I_i (x) Tr_i X  (UNnormalised erasure).
  * H1(X) = sum_i I_{~i} (x) X_i,  H2(X) = sum_{i<j} I_{~ij} (x) X_ij,
    H3(X) = sum_i erase(X,i).
  * spinflip(X) = Y^{(x)4} X^T Y^{(x)4} (plain transpose, no conjugation).
  * F(X) = sum_i sum_{a in {X,Y,Z}} sigma_i^a X sigma_i^a  (non-identity Paulis).
  * channel(X,p): sequential single-site maps X -> (1-p) X + (p/2) erase(X,i).
"""
import hashlib
import itertools
import json
import os
import random
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
EVID = ('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/'
        'parallel-18/depolarizing-majorization4')
INPUTS = [
    ('frontier-20261028-98-rank6-global-k10.md',
     '05c04b8b093835c2a0fe63e849e2552c012ef1d33a7b35e78a9738ebce0799f2'),
    ('frontier-20261028-97-rank6-tail-check.py',
     '16e3f2b3ec6572d2d1ff3c8caea863affec342db7e0bf3753b0f44e43555175f'),
    ('frontier-20261028-100-rank10-11-global-k5-k6.md',
     '108322fa2469cb6a374b9b8cca633e78e8810169f6cdb7b7183cef26cdb188db'),
]


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        h.update(fh.read())
    return h.hexdigest()


# ----------------------------------------------------------------- Gaussian rationals
class G:
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        self.re = re if type(re) is Fr else Fr(re)
        self.im = im if type(im) is Fr else Fr(im)

    def __add__(s, o):
        return G(s.re + o.re, s.im + o.im)

    def __sub__(s, o):
        return G(s.re - o.re, s.im - o.im)

    def __neg__(s):
        return G(-s.re, -s.im)

    def __mul__(s, o):
        if type(o) is G:
            return G(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
        return G(s.re * o, s.im * o)

    __rmul__ = __mul__

    def conj(s):
        return G(s.re, -s.im)

    def __eq__(s, o):
        if type(o) is not G:
            o = G(o)
        return s.re == o.re and s.im == o.im

    def __hash__(s):
        return hash((s.re, s.im))

    def iszero(s):
        return s.re == 0 and s.im == 0

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __repr__(s):
        if s.im == 0:
            return str(s.re)
        return f'({s.re}{"+" if s.im >= 0 else "-"}{abs(s.im)}i)'


ZERO, ONE, IMAG = G(0), G(1), G(0, 1)


def gs(x):
    return x if type(x) is G else G(x)


# ----------------------------------------------------------------- exact matrices
def zeros(n, m=None):
    m = n if m is None else m
    return [[G() for _ in range(m)] for _ in range(n)]


def eye(n, s=1):
    M = zeros(n)
    for i in range(n):
        M[i][i] = gs(s)
    return M


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(A, s):
    s = gs(s)
    return [[A[i][j] * s for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    C = zeros(n, m)
    for i in range(n):
        Ai = A[i]
        for l in range(k):
            a = Ai[l]
            if a.re == 0 and a.im == 0:
                continue
            Bl = B[l]
            Ci = C[i]
            for j in range(m):
                b = Bl[j]
                if b.re == 0 and b.im == 0:
                    continue
                Ci[j] = Ci[j] + a * b
    return C


def madj(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def mT(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def mtr(A):
    acc = G()
    for i in range(len(A)):
        acc = acc + A[i][i]
    return acc


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def is_herm(A):
    return meq(A, madj(A))


def tr_prod(A, B):
    acc = G()
    for i in range(len(A)):
        Ai = A[i]
        for j in range(len(B)):
            acc = acc + Ai[j] * B[j][i]
    return acc


def kron(A, B):
    nA, mA, nB, mB = len(A), len(A[0]), len(B), len(B[0])
    C = zeros(nA * nB, mA * mB)
    for i in range(nA):
        for j in range(mA):
            a = A[i][j]
            if a.iszero():
                continue
            for k in range(nB):
                for l in range(mB):
                    C[i * nB + k][j * mB + l] = a * B[k][l]
    return C


def diag_real(A):
    out = []
    for i in range(len(A)):
        assert A[i][i].im == 0
        out.append(A[i][i].re)
    return out


def ldl_psd(M):
    """Exact test M >= 0 (Loewner) for Hermitian Gaussian-rational M by LDL* with
    zero-pivot handling: a zero pivot requires a zero remaining row, else not PSD."""
    n = len(M)
    assert is_herm(M), 'ldl_psd: input not Hermitian'
    A = [row[:] for row in M]
    piv = []
    for k in range(n):
        d = A[k][k]
        assert d.im == 0
        if d.re < 0:
            return False, piv, f'negative pivot {d.re} at step {k}'
        if d.re == 0:
            for j in range(k + 1, n):
                if not A[k][j].iszero():
                    return False, piv, f'zero pivot with nonzero off-diagonal at step {k}'
            piv.append(Fr(0))
            continue
        piv.append(d.re)
        inv = Fr(1) / d.re
        for i in range(k + 1, n):
            if A[i][k].iszero():
                continue
            f = A[i][k] * inv
            for j in range(k + 1, n):
                if A[k][j].iszero():
                    continue
                A[i][j] = A[i][j] - f * A[k][j]
    return True, piv, 'ok'


# ----------------------------------------------------------------- qubit structure
NQ, D = 4, 16


def bit(x, i):
    return (x >> (NQ - 1 - i)) & 1


def setbit(x, i, s):
    mask = 1 << (NQ - 1 - i)
    return (x | mask) if s else (x & ~mask)


def wt(x):
    return bin(x).count('1')


P_I = [[ONE, ZERO], [ZERO, ONE]]
P_X = [[ZERO, ONE], [ONE, ZERO]]
P_Y = [[ZERO, G(0, -1)], [G(0, 1), ZERO]]
P_Z = [[ONE, ZERO], [ZERO, G(-1)]]


def local_op(ops):
    M = ops[0]
    for U in ops[1:]:
        M = kron(M, U)
    return M


def site_op(P, i):
    return local_op([P if j == i else P_I for j in range(NQ)])


Y4 = local_op([P_Y] * NQ)
ZS = [site_op(P_Z, i) for i in range(NQ)]
PAULI_SITES = [(i, site_op(P, i)) for i in range(NQ) for P in (P_X, P_Y, P_Z)]


def erase(X, i):
    R = zeros(D)
    for x in range(D):
        for y in range(D):
            if bit(x, i) != bit(y, i):
                continue
            R[x][y] = X[setbit(x, i, 0)][setbit(y, i, 0)] + X[setbit(x, i, 1)][setbit(y, i, 1)]
    return R


def erase_set(X, S):
    for i in S:
        X = erase(X, i)
    return X


def H1(X):
    R = zeros(D)
    for i in range(NQ):
        R = madd(R, erase_set(X, [j for j in range(NQ) if j != i]))
    return R


def H2(X):
    R = zeros(D)
    for i, j in itertools.combinations(range(NQ), 2):
        R = madd(R, erase_set(X, [k for k in range(NQ) if k not in (i, j)]))
    return R


def H3(X):
    R = zeros(D)
    for i in range(NQ):
        R = madd(R, erase(X, i))
    return R


def spinflip(X):
    return mmul(mmul(Y4, mT(X)), Y4)


def F_map(X):
    R = zeros(D)
    for _, S in PAULI_SITES:
        R = madd(R, mmul(mmul(S, X), S))
    return R


def marginal(X, i):
    M = zeros(2)
    for s in (0, 1):
        for s2 in (0, 1):
            acc = G()
            for x in range(D):
                if bit(x, i) == s:
                    acc = acc + X[x][setbit(x, i, s2)]
            M[s][s2] = acc
    return M


def bloch(M2):
    return [tr_prod(M2, P) for P in (P_X, P_Y, P_Z)]


def channel(X, p):
    t, b = Fr(1) - p, p / 2
    for i in range(NQ):
        X = madd(mscale(X, t), mscale(erase(X, i), b))
    return X


def channel_expansion(X, p):
    t, b = Fr(1) - p, p / 2
    R = zeros(D)
    for k in range(NQ + 1):
        for S in itertools.combinations(range(NQ), k):
            R = madd(R, mscale(erase_set(X, list(S)), t ** (NQ - k) * b ** k))
    return R


def ref_spectrum_sorted(p):
    # diagonal of Phi_p^{(x)4}(|0000><0000|): eigenvalue a^{4-wt(x)} b^{wt(x)} at basis label x
    a, b = 1 - p / 2, p / 2
    return sorted(a ** (NQ - wt(x)) * b ** wt(x) for x in range(D))


def ref_bottom(r, p):
    return sum(ref_spectrum_sorted(p)[:r], Fr(0))


def ref_bottom_formula(r, p):
    a, b = 1 - p / 2, p / 2
    assert 5 <= r <= 11
    return b ** 4 + 4 * a * b ** 3 + (r - 5) * a ** 2 * b ** 2


# ----------------------------------------------------------------- vectors / projectors
def ket(x):
    v = [G() for _ in range(D)]
    v[x] = ONE
    return v


def vec(entries):
    v = [G() for _ in range(D)]
    for x, c in entries.items():
        v[x] = gs(c)
    return v


def inner(u, v):
    acc = G()
    for a, b in zip(u, v):
        acc = acc + a.conj() * b
    return acc


def proj(vecs):
    for a in range(len(vecs)):
        for b in range(len(vecs)):
            assert inner(vecs[a], vecs[b]) == (ONE if a == b else ZERO), 'proj: not orthonormal'
    Q = zeros(D)
    for v in vecs:
        for x in range(D):
            if v[x].iszero():
                continue
            for y in range(D):
                Q[x][y] = Q[x][y] + v[x] * v[y].conj()
    return Q


def is_projector(Q, r):
    return is_herm(Q) and meq(mmul(Q, Q), Q) and mtr(Q) == G(r)


def conj_by(U, X):
    return mmul(mmul(U, X), madj(U))


# ----------------------------------------------------------------- randomness (deterministic)
RND = random.Random(20261028)


def rand_gint():
    return G(RND.randint(-3, 3), RND.randint(-3, 3))


def rand_herm():
    B = [[rand_gint() for _ in range(D)] for _ in range(D)]
    return madd(B, madj(B))


def rand_density(rank):
    A = [[rand_gint() for _ in range(rank)] for _ in range(D)]
    M = mmul(A, madj(A))
    tr = mtr(M)
    assert tr.im == 0 and tr.re > 0
    return mscale(M, Fr(1) / tr.re)


# ----------------------------------------------------------------- bookkeeping
RESULTS = []


def record(name, kind, predicted, observed, detail):
    """kind: 'positive' (predicted PASS) or 'negative' (predicted FAIL)."""
    RESULTS.append({'control': name, 'kind': kind, 'predicted': predicted,
                    'observed': observed, 'as_predicted': predicted == observed,
                    'detail': detail})
    flag = 'OK ' if predicted == observed else '!! '
    print(f'{flag}{name}: predicted={predicted} observed={observed}')


def pos(name, ok, detail):
    record(name, 'positive', 'PASS', 'PASS' if ok else 'FAIL', detail)


def neg(name, ok, detail):
    record(name, 'negative', 'FAIL', 'PASS' if ok else 'FAIL', detail)


def fs(x):
    return str(x)


# ================================================================= controls
def control_conventions():
    # Z_i diagonal convention and kron consistency
    ok = all(diag_real(ZS[i])[x] == (1 - 2 * bit(x, i)) for i in range(NQ) for x in range(D))
    # erase vs Pauli-twirl form: erase(X,i) == 1/2 sum_{a=0..3} sigma_i^a X sigma_i^a
    X = rand_herm()
    for i in range(NQ):
        tw = mscale(X, Fr(1, 2))
        for (j, S) in PAULI_SITES:
            if j == i:
                tw = madd(tw, mscale(mmul(mmul(S, X), S), Fr(1, 2)))
        ok = ok and meq(tw, erase(X, i))
    pos('C0 conventions: Z_i diagonal = (-1)^{x_i}; erase == half Pauli twirl', ok, {})


def control_spectral_tables():
    Ztot = zeros(D)
    for i in range(NQ):
        Ztot = madd(Ztot, ZS[i])
    zt = sorted(diag_real(Ztot), reverse=True)
    top = {r: sum(zt[:r], Fr(0)) for r in range(1, D + 1)}
    three = {}
    for i in range(NQ):
        Z3 = zeros(D)
        for j in range(NQ):
            if j != i:
                Z3 = madd(Z3, ZS[j])
        d = sorted(diag_real(Z3), reverse=True)
        three[i] = {r: sum(d[:r], Fr(0)) for r in range(1, D + 1)}
    Z0 = zeros(D)
    for i in range(NQ):
        Z0 = madd(Z0, site_op([[ONE, ZERO], [ZERO, ZERO]], i))
    z0 = sorted(diag_real(Z0))
    bottom = {r: sum(z0[:r], Fr(0)) for r in range(1, D + 1)}
    ok = True
    ok &= all(top[r] == 12 for r in (5, 6, 10, 11))
    ok &= all(three[i][r] == v for i in range(NQ) for r, v in ((5, 9), (6, 10), (10, 10), (11, 9)))
    ok &= all(three[i][r] <= 10 for i in range(NQ) for r in (5, 6, 10, 11))
    ok &= all(bottom[r] == 2 * r - 6 for r in (5, 6, 10, 11))
    ok &= zt[:6] == [4, 2, 2, 2, 2, 0] and z0[:6] == [0, 1, 1, 1, 1, 2]
    # N >= 2I - 2E0 - Pi1 on the diagonal
    Nd = [Fr(wt(x)) for x in range(D)]
    rhs = [2 - (2 if x == 0 else 0) - (1 if wt(x) == 1 else 0) for x in range(D)]
    ok &= all(Nd[x] >= rhs[x] for x in range(D))
    detail = {'Ztot_top_r': {r: fs(top[r]) for r in range(1, D + 1)},
              'three_site_top_r_site0': {r: fs(three[0][r]) for r in range(1, D + 1)},
              'three_site_top_r_for_ranks_7_8_9': [fs(three[0][r]) for r in (7, 8, 9)],
              'sum_proj0_bottom_r': {r: fs(bottom[r]) for r in range(1, D + 1)},
              'N_minus_(2I-2E0-Pi1)_diag_min': fs(min(Nd[x] - rhs[x] for x in range(D)))}
    pos('C1 spectral tables: S<=12, three-site<=10 at ranks 5/6/10/11, bottom-r of sum|0><0| = 2r-6, N>=2I-2E0-Pi1', ok, detail)
    # informational: three-site cut differs at ranks 7,8,9
    pos('C1b informational: three-site top-r at ranks 7,8,9 exceeds 10 (proof step (4) unavailable there)',
        all(three[0][r] > 10 for r in (7, 8, 9)), {r: fs(three[0][r]) for r in (7, 8, 9)})


def control_2x2_identity():
    ok = True
    pts = []
    for q in (Fr(1, 5), Fr(1, 2), Fr(3, 4), Fr(9, 10)):
        for c in (Fr(0), Fr(1, 3), Fr(2, 3), Fr(1)):
            det = (1 + c - 2 * c * q) * c * (2 * q - 1) - 4 * c * c * q * (1 - q)
            ok &= det == c * (2 * q - 1 - c)
            pts.append([fs(q), fs(c), fs(det)])
    pos('C2 2x2 block determinant identity det = c(2q-1-c) on 4x4 rational grid (bidegree (2,2) => identity)', ok, {'points': pts})


def build_reviewer_projectors():
    v0 = vec({0: Fr(12, 13), 15: G(0, Fr(5, 13))})
    w1 = [ket(1), ket(2), ket(4), ket(8)]
    Q = {}
    Q[5] = proj([v0] + w1)
    Q[6] = proj([v0] + w1 + [ket(3)])
    Q[10] = proj([v0] + w1 + [ket(3), ket(5), ket(6), ket(9), ket(10)])
    Q[11] = proj([v0] + w1 + [ket(3), ket(5), ket(6), ket(9), ket(10), ket(12)])
    Qt = proj([ket(0)] + w1 + [ket(3)])  # tight diagonal rank-6
    va = vec({0: Fr(24, 25), 15: Fr(7, 25)})  # author's packet-described projector, rebuilt from text
    Qa = proj([va, ket(1), ket(2), ket(3), ket(4), ket(8)])
    return Q, Qt, Qa


def reviewer_local_unitary():
    U0 = mscale([[G(3), G(0, 4)], [G(0, 4), G(3)]], Fr(1, 5))
    U0 = mscale(U0, IMAG)  # det -1: in U(2) but not SU(2), tests U(2) covariance
    U1 = mscale([[G(3), G(4)], [G(-4), G(3)]], Fr(1, 5))
    U2 = mscale([[G(5), G(0, 12)], [G(0, 12), G(5)]], Fr(1, 13))
    U3 = mscale([[G(4), G(0, 3)], [G(-3), G(0, 4)]], Fr(1, 5))
    for U in (U0, U1, U2, U3):
        assert meq(mmul(U, madj(U)), eye(2))
    return local_op([U0, U1, U2, U3])


def dual_lemma_unrotated(Q, r, label):
    assert is_projector(Q, r)
    margs = [marginal(Q, i) for i in range(NQ)]
    bl = [bloch(m) for m in margs]
    assert all(b[0].iszero() and b[1].iszero() and b[2].im == 0 for b in bl), 'marginals must be Z-diagonal here'
    mz = [b[2].re for b in bl]
    assert all(m >= 0 for m in mz)
    S = sum(mz, Fr(0))
    c = (S - 10) / 2
    q = Q[0][0]
    assert q.im == 0
    q = q.re
    A = msub(madd(H1(Q), spinflip(Q)), eye(D, 2 * r - 5))
    okpsd, piv, why = ldl_psd(A)
    d = diag_real(msub(H1(Q), eye(D, 2 * r - 5)))
    checks = {
        'projector': True,
        'S_le_12': S <= 12,
        'three_site_le_10': all(S - mz[i] <= 10 for i in range(NQ)),
        'm_i_ge_S_minus_10': all(mz[i] >= S - 10 for i in range(NQ)),
        'H1Q_formula_2rI_plus_half_sum_mZ': meq(H1(Q), madd(eye(D, 2 * r), mscale(sum_mZ(mz), Fr(1, 2)))),
        'eig_at_1111_equals_minus_c': d[15] == -c,
        'other_diag_ge_c_when_S_gt_10': (S <= 10) or all(d[x] >= c for x in range(D - 1)),
        'q_ge_(1+c)/2_when_S_gt_10': (S <= 10) or q >= (1 + c) / 2,
        'trQPi1_le_4': sum((Q[x][x].re for x in range(D) if wt(x) == 1), Fr(0)) <= 4,
        'occupancy_S_le_8_plus_4q': S <= 8 + 4 * q,
        'dual_operator_psd_exact_LDL': okpsd,
    }
    detail = {'rank': r, 'm': [fs(m) for m in mz], 'S': fs(S), 'c': fs(c), 'q': fs(q),
              'branch': 'S>10' if S > 10 else 'S<=10', 'ldl': why,
              'positive_pivots': sum(1 for p in piv if p > 0), 'zero_pivots': sum(1 for p in piv if p == 0),
              'checks': checks}
    return all(checks.values()), detail, mz


def sum_mZ(mz):
    R = zeros(D)
    for i in range(NQ):
        R = madd(R, mscale(ZS[i], mz[i]))
    return R


def dual_lemma_rotated(Q, r, U, mz_ref, label):
    Qr = conj_by(U, Q)
    ok = is_projector(Qr, r)
    margs = [marginal(Qr, i) for i in range(NQ)]
    bl = [bloch(m) for m in margs]
    nondiag = [not margs[i][0][1].iszero() for i in range(NQ)]
    m2 = [sum((b.abs2() for b in bl[i]), Fr(0)) for i in range(NQ)]
    ok &= all(nondiag)
    ok &= all(m2[i] == mz_ref[i] ** 2 for i in range(NQ))
    A = msub(madd(H1(Qr), spinflip(Qr)), eye(D, 2 * r - 5))
    okpsd, piv, why = ldl_psd(A)
    ok &= okpsd
    A0 = msub(madd(H1(Q), spinflip(Q)), eye(D, 2 * r - 5))
    cov = meq(A, conj_by(U, A0))
    ok &= cov
    # covariance pieces separately
    ok &= meq(H1(Qr), conj_by(U, H1(Q))) and meq(spinflip(Qr), conj_by(U, spinflip(Q)))
    detail = {'rank': r, 'marginals_nondiagonal_each_site': nondiag,
              'bloch_norm_sq_matches_unrotated': [fs(x) for x in m2],
              'ldl': why, 'positive_pivots': sum(1 for p in piv if p > 0),
              'zero_pivots': sum(1 for p in piv if p == 0), 'covariance_exact': cov,
              'rotated_marginal_site0': [[repr(e) for e in row] for row in margs[0]]}
    return ok, detail


def control_dual_lemma():
    Q, Qt, Qa = build_reviewer_projectors()
    U = reviewer_local_unitary()
    MZ = {}
    for r in (5, 6, 10, 11):
        ok, det, mz = dual_lemma_unrotated(Q[r], r, f'Q{r}')
        MZ[r] = mz
        pos(f'C3 dual lemma, reviewer rank-{r} projector (Z-diagonal marginals, S>10 branch), exact', ok and det['branch'] == 'S>10', det)
    for r in (5, 6, 10, 11):
        ok, det = dual_lemma_rotated(Q[r], r, U, MZ[r], f'Q{r}rot')
        pos(f'C4 dual lemma, reviewer rank-{r} projector after U(2)^(x)4 Gaussian-rational rotation (non-diagonal marginals), exact', ok, det)
    ok, det, _ = dual_lemma_unrotated(Qt, 6, 'Qtight')
    pos('C5 tight diagonal rank-6 projector {0000,wt1 x4,0011}: S=12, c=1, q=1, dual operator PSD with a zero pivot', ok and det['S'] == '12' and det['zero_pivots'] >= 1, det)
    # N1 threshold sensitivity
    A = msub(madd(H1(Qt), spinflip(Qt)), eye(D, Fr(7) + Fr(1, 1000)))
    okpsd, piv, why = ldl_psd(A)
    neg('N1 same tight projector against false threshold 7+1/1000 must fail LDL', okpsd, {'ldl': why})
    # author's packet-described projector, rebuilt independently from the text
    ok, det, _ = dual_lemma_unrotated(Qa, 6, 'Qauthor')
    quoted = det['S'] == '7108/625' and det['c'] == '429/625' and det['q'] == '576/625' and det['positive_pivots'] == 16
    pos('C6 packet-98 described projector rebuilt from text: S=7108/625, c=429/625, q=576/625, 16 positive pivots', ok and quoted, det)
    return Q, Qt, Qa, U


def control_2x2_lemma_on_projector(Q6):
    R = spinflip(Q6)
    q = R[15][15]
    assert q.im == 0
    q = q.re
    E = proj([ket(15)])
    c0 = 2 * q - 1
    results = {}
    for name, c, predicted_psd in (('c=(S-10)/2 interior', Fr(69, 169), True), ('c=2q-1 boundary', c0, True), ('c=2q-1+1/1000', c0 + Fr(1, 1000), False)):
        M = madd(R, mscale(msub(eye(D), mscale(E, 2)), c))
        okpsd, piv, why = ldl_psd(M)
        results[name] = {'c': fs(c), 'psd': okpsd, 'ldl': why, 'zero_pivots': sum(1 for p in piv if p == 0)}
        if predicted_psd:
            pos(f'C7 2x2 lemma on 16x16: spinflip(Q6)+c(I-2E), {name}, q={q}', okpsd, results[name])
        else:
            neg(f'N2 2x2 lemma hypothesis sharpness: spinflip(Q6)+c(I-2E), {name}, must fail', okpsd, results[name])


def control_identity():
    X = rand_herm()
    rho = rand_density(3)
    ok = True
    for M, lbl in ((X, 'random Hermitian Gaussian-integer X'), (rho, 'random rank-3 rational density')):
        lhs = madd(msub(H2(M), H1(M)), eye(D, mtr(M)))
        rhs = madd(madd(M, spinflip(M)), mscale(F_map(M), Fr(1, 2)))
        ok &= meq(lhs, rhs)
        # alternating erasure form of the spin flip
        alt = zeros(D)
        for k in range(NQ + 1):
            for S in itertools.combinations(range(NQ), k):
                alt = madd(alt, mscale(erase_set(M, list(S)), (-1) ** k))
        ok &= meq(alt, spinflip(M))
    pos('C8 identity H2-H1+Tr(X)I = X + spinflip(X) + F(X)/2 and spinflip = sum_S (-1)^|S| E_S, exact on random inputs', ok, {})
    # negative: wrong coefficient on F
    lhs = madd(msub(H2(rho), H1(rho)), eye(D))
    rhs_bad = madd(madd(rho, spinflip(rho)), F_map(rho))
    neg('N3 identity with coefficient 1 on F must fail', meq(lhs, rhs_bad), {})
    # single-qubit spin flip
    B = [[rand_gint() for _ in range(2)] for _ in range(2)]
    M2 = madd(B, madj(B))
    sf2 = mmul(mmul(P_Y, mT(M2)), P_Y)
    pos('C8b one-qubit spin flip Y M^T Y = Tr(M) I - M, exact', meq(sf2, msub(eye(2, mtr(M2)), M2)), {})
    # self-adjointness in the trace pairing
    A, Bm = rand_herm(), rand_herm()
    sa = (tr_prod(A, H1(Bm)) == tr_prod(H1(A), Bm) and tr_prod(A, H2(Bm)) == tr_prod(H2(A), Bm)
          and tr_prod(A, spinflip(Bm)) == tr_prod(spinflip(A), Bm))
    pos('C9 H1, H2, spinflip self-adjoint in the trace pairing, exact on random Hermitian pair', sa, {})
    return rho


def control_erasure_expansion(rho):
    ok = True
    details = {}
    for p in (Fr(2, 5), Fr(2, 3), Fr(4, 3)):
        t, b = 1 - p, p / 2
        out = channel(rho, p)
        ok &= meq(out, channel_expansion(rho, p))
        lower = madd(madd(eye(D, b ** 4), mscale(H1(rho), t * b ** 3)), mscale(H2(rho), t ** 2 * b ** 2))
        rem = msub(out, lower)
        ok &= meq(rem, madd(mscale(H3(rho), t ** 3 * b), mscale(rho, t ** 4)))
        okpsd, piv, why = ldl_psd(rem)
        details[fs(p)] = {'remainder_psd': okpsd, 'ldl': why}
        if p <= 1:
            ok &= okpsd
    pos('C10 channel == erasure expansion; remainder == t^3 b H3 + t^4 rho; remainder PSD at p=2/5, 2/3', ok, details)
    rho0 = proj([ket(0)])
    p = Fr(4, 3)
    t, b = 1 - p, p / 2
    rem = msub(channel(rho0, p), madd(madd(eye(D, b ** 4), mscale(H1(rho0), t * b ** 3)), mscale(H2(rho0), t ** 2 * b ** 2)))
    okpsd, piv, why = ldl_psd(rem)
    neg('N4 retained-erasure Loewner bound (10) at p=4/3 on |0000> must FAIL (t<0): mirror is required for p>1', okpsd, {'ldl': why, 'remainder_at_0000': fs(rem[0][0].re)})


def control_mirror(rho, Q6):
    ok = True
    det = {}
    for p in (Fr(4, 3), Fr(5, 4)):
        out = channel(rho, p)
        mir = channel(rho, 2 - p)
        ok &= meq(spinflip(out), mir)
        ok &= tr_prod(Q6, out) == tr_prod(spinflip(Q6), mir)
        ok &= ref_spectrum_sorted(p) == ref_spectrum_sorted(2 - p)
        det[fs(p)] = {'trQ_out': fs(tr_prod(Q6, out).re), 'tr_sfQ_mirror': fs(tr_prod(spinflip(Q6), mir).re)}
    pos('C11 mirror: spinflip(Phi_p(rho)) == Phi_{2-p}(rho); Tr[Q Phi_p] == Tr[sf(Q) Phi_{2-p}]; reference spectra equal, exact', ok, det)


def control_full_chain(Q, U, rho):
    psi = vec({0: Fr(3, 1), 6: Fr(2, 1), 9: G(0, 2), 15: Fr(1, 1)})
    nrm = inner(psi, psi)
    assert nrm.im == 0
    rho_pure = mscale(proj_unnormalised(psi), Fr(1) / nrm.re)
    assert is_projector(rho_pure, 1)
    p = Fr(2, 5)
    t, b = 1 - p, p / 2
    ok = True
    det = {}
    for lbl, st in (('rank3_mixed', rho), ('pure_reviewer', rho_pure)):
        h1, h2, h3, out, Fst, sf_st = H1(st), H2(st), H3(st), channel(st, p), F_map(st), spinflip(st)
        for r in (5, 6, 10, 11):
            for frame, Qr in (('unrotated', Q[r]), ('rotated', conj_by(U, Q[r]))):
                tq = tr_prod(Qr, out).re
                th1, th2, th3, tqr = tr_prod(Qr, h1).re, tr_prod(Qr, h2).re, tr_prod(Qr, h3).re, tr_prod(Qr, st).re
                decomp = b ** 4 * r + t * b ** 3 * th1 + t ** 2 * b ** 2 * th2 + t ** 3 * b * th3 + t ** 4 * tqr
                dual = tr_prod(st, madd(H1(Qr), spinflip(Qr))).re
                ident = dual - r + tqr + tr_prod(Qr, Fst).re / 2
                ref = ref_bottom(r, p)
                c = {'decomposition_exact': tq == decomp,
                     'trQH1_ge_2r-6': th1 >= 2 * r - 6,
                     'trQH2_ge_r-5': th2 >= r - 5,
                     'trQH2_identity_exact': th2 == ident,
                     'dual_ge_2r-5': dual >= 2 * r - 5,
                     'ref_formula_matches_sorted_spectrum': ref == ref_bottom_formula(r, p),
                     'trQ_out_ge_ref_bottom_r': tq >= ref}
                ok &= all(c.values())
                det[f'{lbl}/r{r}/{frame}'] = {'trQ_out': fs(tq), 'ref_bottom_r': fs(ref), 'trQH1': fs(th1), 'trQH2': fs(th2),
                                              'dual': fs(dual), 'checks': c}
    pos('C12 full chain at p=2/5: exact decomposition, Tr QH1>=2r-6, Tr QH2>=r-5 via identity, Tr[Q Phi]>=reference bottom-r (ranks 5,6,10,11; unrotated and rotated Q)', ok, det)
    # equality case: product reference with its own bottom-r eigenprojector
    rho0 = proj([ket(0)])
    out0 = channel(rho0, p)
    ok = True
    det = {}
    order = sorted(range(D), key=lambda x: -wt(x))  # ascending eigenvalue for p<=1
    for r in (5, 6, 10, 11):
        Qb = proj([ket(x) for x in order[:r]])
        tq = tr_prod(Qb, out0).re
        ok &= tq == ref_bottom(r, p)
        det[f'r{r}'] = {'trQ_out': fs(tq), 'ref': fs(ref_bottom(r, p))}
    pos('C13 equality case: |0000> with its own bottom-r eigenprojector attains the reference bound exactly (bound is tight)', ok, det)


def proj_unnormalised(v):
    Q = zeros(D)
    for x in range(D):
        if v[x].iszero():
            continue
        for y in range(D):
            Q[x][y] = v[x] * v[y].conj()
    return Q


def main():
    t0 = utc()
    receipts = {'clock_start_utc': t0, 'python': sys.version.split()[0],
                'script_sha256': sha256_file(os.path.abspath(__file__)),
                'inputs_sha256_recomputed': []}
    for name, expected in INPUTS:
        path = os.path.join(EVID, name)
        got = sha256_file(path)
        receipts['inputs_sha256_recomputed'].append({'file': name, 'sha256': got, 'matches_manifest': got == expected,
                                                     'bytes': os.path.getsize(path)})
    control_conventions()
    control_spectral_tables()
    control_2x2_identity()
    Q, Qt, Qa, U = control_dual_lemma()
    control_2x2_lemma_on_projector(Q[6])
    rho = control_identity()
    control_erasure_expansion(rho)
    control_mirror(rho, Q[6])
    control_full_chain(Q, U, rho)
    all_ok = all(r['as_predicted'] for r in RESULTS) and all(x['matches_manifest'] for x in receipts['inputs_sha256_recomputed'])
    receipts['clock_end_utc'] = utc()
    summary = {'positive_controls': sum(1 for r in RESULTS if r['kind'] == 'positive'),
               'negative_controls': sum(1 for r in RESULTS if r['kind'] == 'negative'),
               'all_as_predicted': all_ok}
    out = {'scope': 'exact finite controls on reviewer-chosen instances; not a universal proof',
           'receipts': receipts, 'summary': summary, 'controls': RESULTS}
    outpath = os.path.join(HERE, 'reviewer-exact-controls-v1.result.json')
    with open(outpath, 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print(json.dumps({'summary': summary, 'receipts': receipts}, indent=1, sort_keys=True))
    sys.exit(0 if all_ok else 1)


if __name__ == '__main__':
    main()
