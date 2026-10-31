#!/usr/bin/env python3
"""f168rv-controls-v1.py -- reviewer-authored independent controls.

Review wave : f168-werner-stratified-source-independent-v2
Reviewer    : ReviewF168WernerV2 (same-harness; not human, not independent model family,
              not a formal/kernel check, not a novelty check)
Scope       : exact Gaussian-rational and high-precision numerical checks of the
              reformulations in frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md
Policy      : no author script/result is imported, opened or executed.  The author addendum
              is parsed as JSON data only (hash, keys); it is never used as evidence.
Output      : exactly one new file f168rv-controls-v1-results.json (exclusive create) next to
              this script, unless run with --dry.  Run as `python3 -B` (no bytecode cache).
Conventions : sites are 0-indexed in code (packet site k == code site k-1).  An operator on
              H_n=(C^d)^{(x)n} is a dict {(x_tuple, y_tuple): value}; x = row/output index,
              y = column/input index.  q_n(C) = sum_S (-1/2)^{|S|} ||Tr_S C||_HS^2 with
              unnormalised partial traces.
"""
import sys, os, json, hashlib, itertools, random, subprocess, platform
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, 'f168rv-controls-v1-results.json')
EVD = ('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/'
       'parallel-18/werner3-ququart/')
CAND = EVD + 'frontier-20261029-d4-q3-stratified-source-independent-frontier-v2.md'
ADD = EVD + 'frontier-20261029-d4-stratified-v2-exact-check-addendum-1.json'
EXPECT = {
    CAND: ('bf50bfbf3d0f4d24ec6a9e5fc55b19ced5cd2acdb223bbb1518fe6ebf4177329', 13054, 153),
    ADD: ('3627abce4a79020b33138e78393d179167045341e2a8e59cddaffe841417a591', 1564, 15),
}
D4 = 4
TOL = 1e-9          # numerical acceptance margin (float64 / mpmath parts only)


def clock():
    return subprocess.run(['/bin/date'], capture_output=True, text=True, check=True).stdout.strip()


def fs(x):
    return str(x)


POS, NEG = {}, {}


def pos(name, ok, **info):
    d = {'pass': bool(ok)}
    d.update(info)
    POS[name] = d
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)


def neg(name, failed, **info):
    d = {'failed_as_intended': bool(failed)}
    d.update(info)
    NEG[name] = d
    print(('NEG-OK ' if failed else 'NEG-UNEXPECTED-PASS ') + name, flush=True)


# ------------------------------------------------------------------ Gaussian rationals
class Q:
    __slots__ = ('r', 'i')

    def __init__(self, r=0, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r)
        self.i = i if isinstance(i, Fr) else Fr(i)

    def __add__(self, o):
        if isinstance(o, Q):
            return Q(self.r + o.r, self.i + o.i)
        return Q(self.r + o, self.i)
    __radd__ = __add__

    def __sub__(self, o):
        if isinstance(o, Q):
            return Q(self.r - o.r, self.i - o.i)
        return Q(self.r - o, self.i)

    def __rsub__(self, o):
        return Q(o - self.r, -self.i)

    def __mul__(self, o):
        if isinstance(o, Q):
            return Q(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)
        return Q(self.r * o, self.i * o)
    __rmul__ = __mul__

    def __truediv__(self, o):
        if isinstance(o, Q):
            den = o.r * o.r + o.i * o.i
            return Q((self.r * o.r + self.i * o.i) / den, (self.i * o.r - self.r * o.i) / den)
        return Q(self.r / o, self.i / o)

    def __neg__(self):
        return Q(-self.r, -self.i)

    def conj(self):
        return Q(self.r, -self.i)

    def abs2(self):
        return self.r * self.r + self.i * self.i

    def iz(self):
        return self.r == 0 and self.i == 0

    def __eq__(self, o):
        if isinstance(o, Q):
            return self.r == o.r and self.i == o.i
        return self.i == 0 and self.r == o
    __hash__ = None

    def c(self):
        return complex(float(self.r), float(self.i))


ZERO, ONE = Q(0), Q(1)
HN = Fr(-1, 2)


def rq(rng, k=3):
    return Q(rng.randint(-k, k), rng.randint(-k, k))


# ------------------------------------------------------------------ operators (sparse dicts)
def clean(R):
    return {k: v for k, v in R.items() if not v.iz()}


def op_lin(*pairs):
    R = {}
    for c, A in pairs:
        for k, v in A.items():
            w = v * c
            R[k] = R[k] + w if k in R else w
    return clean(R)


def op_eq(A, B):
    A, B = clean(A), clean(B)
    return A.keys() == B.keys() and all(A[k] == B[k] for k in A)


def subsets(n):
    return [S for r in range(n + 1) for S in itertools.combinations(range(n), r)]


def ptrace(C, S, n):
    rest = tuple(i for i in range(n) if i not in S)
    R = {}
    for (x, y), v in C.items():
        if any(x[s] != y[s] for s in S):
            continue
        k = (tuple(x[i] for i in rest), tuple(y[i] for i in rest))
        R[k] = R[k] + v if k in R else v
    return clean(R)


def hs2(C):
    t = Fr(0)
    for v in C.values():
        t += v.abs2()
    return t


def hsip(A, B):
    t = ZERO
    if len(A) > len(B):
        for k, w in B.items():
            v = A.get(k)
            if v is not None:
                t = t + v.conj() * w
    else:
        for k, v in A.items():
            w = B.get(k)
            if w is not None:
                t = t + v.conj() * w
    return t


def qn(C, n):
    t = Fr(0)
    for S in subsets(n):
        t += HN ** len(S) * hs2(ptrace(C, S, n))
    return t


def qform(A, B, n):
    t = ZERO
    for S in subsets(n):
        t = t + hsip(ptrace(A, S, n), ptrace(B, S, n)) * (HN ** len(S))
    return t


def embed_id(Y, S, n, d):
    """I_S (x) Y, Y an operator on the sites not in S (in increasing order)."""
    S = tuple(sorted(S))
    rest = [i for i in range(n) if i not in S]
    R = {}
    for (xr, yr), v in Y.items():
        for js in itertools.product(range(d), repeat=len(S)):
            x, y = [0] * n, [0] * n
            for a, i in enumerate(rest):
                x[i], y[i] = xr[a], yr[a]
            for a, i in enumerate(S):
                x[i] = y[i] = js[a]
            R[(tuple(x), tuple(y))] = v
    return R


def id_part(C, i, n, d):
    return op_lin((Fr(1, d), embed_id(ptrace(C, (i,), n), (i,), n, d)))


def sector(C, T, n, d):
    R = C
    for i in range(n):
        P = id_part(R, i, n, d)
        R = P if i in T else op_lin((1, R), (-1, P))
    return R


def p_odd(C, n, d, keep=lambda T: len(T) % 2 == 1):
    return op_lin(*[(1, sector(C, T, n, d)) for T in subsets(n) if keep(T)])


def kop(C, n, d):
    """(tensor_i K_i) vec C, returned as an operator: sum_S (-1/2)^|S| I_S (x) Tr_S C."""
    return op_lin(*[(HN ** len(S), embed_id(ptrace(C, S, n), S, n, d)) for S in subsets(n)])


def sector_structure_ok(Sc, T, n, d):
    for i in range(n):
        if i in T:
            if not op_eq(id_part(Sc, i, n, d), Sc):
                return False
        elif ptrace(Sc, (i,), n):
            return False
    return True


def rvec(rng, n, d, k=3):
    return {x: rq(rng, k) for x in itertools.product(range(d), repeat=n)}


def ketbra(a, b):
    R = {}
    for x, va in a.items():
        if va.iz():
            continue
        for y, vb in b.items():
            if not vb.iz():
                R[(x, y)] = va * vb.conj()
    return R


def rop(rng, n, d, k=3):
    idx = list(itertools.product(range(d), repeat=n))
    return clean({(x, y): rq(rng, k) for x in idx for y in idx})


def rrank2(rng, n, d, k=3):
    return op_lin((1, ketbra(rvec(rng, n, d, k), rvec(rng, n, d, k))),
                  (1, ketbra(rvec(rng, n, d, k), rvec(rng, n, d, k))))


def tensor(A, nA, B, nB):
    R = {}
    for (x, y), v in A.items():
        for (x2, y2), w in B.items():
            R[(x + x2, y + y2)] = v * w
    return clean(R)


def permute_sites(C, perm):
    """new site j carries old site perm[j]."""
    return {(tuple(x[p] for p in perm), tuple(y[p] for p in perm)): v for (x, y), v in C.items()}


def op1(A):
    d = len(A)
    return clean({((a,), (b,)): A[a][b] for a in range(d) for b in range(d)})


# ------------------------------------------------------------------ local d x d matrices
def mzero(d):
    return [[ZERO] * d for _ in range(d)]


def mid(d):
    return [[ONE if a == b else ZERO for b in range(d)] for a in range(d)]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    R = [[ZERO] * p for _ in range(n)]
    for a in range(n):
        for k in range(m):
            x = A[a][k]
            if x.iz():
                continue
            for b in range(p):
                y = B[k][b]
                if not y.iz():
                    R[a][b] = R[a][b] + x * y
    return R


def mdag(A):
    return [[A[b][a].conj() for b in range(len(A))] for a in range(len(A[0]))]


def mconj(A):
    return [[v.conj() for v in row] for row in A]


def madd(*pairs):
    r, c = len(pairs[0][1]), len(pairs[0][1][0])
    R = [[ZERO] * c for _ in range(r)]
    for k, A in pairs:
        for a in range(r):
            for b in range(c):
                if not A[a][b].iz():
                    R[a][b] = R[a][b] + A[a][b] * k
    return R


def meq(A, B):
    return all(A[a][b] == B[a][b] for a in range(len(A)) for b in range(len(A[0])))


def minv(A):
    n = len(A)
    M = [list(row) + [ONE if a == b else ZERO for b in range(n)] for a, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if not M[r][c].iz())
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and not M[r][c].iz():
                f = M[r][c]
                M[r] = [M[r][t] - f * M[c][t] for t in range(2 * n)]
    return [row[n:] for row in M]


def outer(u, v):
    return [[u[a] * v[b].conj() for b in range(len(v))] for a in range(len(u))]


def colv(U, j):
    return [U[a][j] for a in range(len(U))]


def cayley(rng, d, k=2):
    A = mzero(d)
    for a in range(d):
        A[a][a] = Q(0, rng.randint(-k, k))
        for b in range(a + 1, d):
            z = rq(rng, k)
            A[a][b], A[b][a] = z, -z.conj()
    I = mid(d)
    return mmul(madd((1, I), (-1, A)), minv(madd((1, I), (1, A))))


def left_site(M, C, i):
    R = {}
    d = len(M)
    for (x, y), v in C.items():
        l = x[i]
        for k in range(d):
            m = M[k][l]
            if m.iz():
                continue
            key = (x[:i] + (k,) + x[i + 1:], y)
            w = m * v
            R[key] = R[key] + w if key in R else w
    return clean(R)


def right_site(C, M, i):
    R = {}
    d = len(M)
    for (x, y), v in C.items():
        l = y[i]
        for k in range(d):
            m = M[l][k]
            if m.iz():
                continue
            key = (x, y[:i] + (k,) + y[i + 1:])
            w = v * m
            R[key] = R[key] + w if key in R else w
    return clean(R)


def contract(C, al, be, i):
    """<al|C|be>_i = (<al|_i (x) I) C (|be>_i (x) I)."""
    R = {}
    for (x, y), v in C.items():
        a, b = al[x[i]], be[y[i]]
        if a.iz() or b.iz():
            continue
        k = (x[:i] + x[i + 1:], y[:i] + y[i + 1:])
        w = a.conj() * v * b
        R[k] = R[k] + w if k in R else w
    return clean(R)


def rank_vectors(vecs, dim):
    basis = []
    for v in vecs:
        w = list(v)
        for piv, b in basis:
            if not w[piv].iz():
                f = w[piv] / b[piv]
                w = [w[t] - f * b[t] for t in range(dim)]
        nz = [t for t in range(dim) if not w[t].iz()]
        if nz:
            basis.append((nz[0], w))
            if len(basis) == dim:
                break
    return len(basis)


def leg_dim(C, i, side, d):
    cols = {}
    for (x, y), v in C.items():
        if side == 'out':
            key, k = (x[:i] + x[i + 1:], y), x[i]
        else:
            key, k = (x, y[:i] + y[i + 1:]), y[i]
        if key not in cols:
            cols[key] = [ZERO] * d
        cols[key][k] = v
    return rank_vectors(list(cols.values()), d)


def all_legs(C, n, d):
    return {f'{side}@{i + 1}': leg_dim(C, i, side, d) for i in range(n) for side in ('out', 'in')}


def op_rank(C, n, d):
    idx = list(itertools.product(range(d), repeat=n))
    pos_ = {x: j for j, x in enumerate(idx)}
    rows = {}
    for (x, y), v in C.items():
        if x not in rows:
            rows[x] = [ZERO] * len(idx)
        rows[x][pos_[y]] = v
    return rank_vectors(list(rows.values()), len(idx))


# ------------------------------------------------------------------ Lemma 5 machinery
OCT = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(1), Q(1)), (Q(1), Q(-1)), (Q(1), Q(0, 1)), (Q(1), Q(0, -1))]


def lc(a, u, b, v):
    return [a * u[k] + b * v[k] for k in range(len(u))]


def terms(C, i, E, Ep, orient, weight=3, drop_perp=False, use_u=False):
    """Method A: octahedron projective 2-design (unnormalised vectors, weight 1/(6|u|^4))."""
    e1, e2 = E
    out = []
    for al, be in OCT:
        u = lc(al, e1, be, e2)
        up = lc(-be.conj(), e1, al.conj(), e2)
        nn = al.abs2() + be.abs2()
        w = Fr(weight, 6) / (nn * nn)
        other = u if use_u else up
        X = contract(C, u, other, i) if orient == 'out' else contract(C, other, u, i)
        out.append((w, X))
    if not drop_perp:
        for ea in E:
            for fb in Ep:
                X = contract(C, ea, fb, i) if orient == 'out' else contract(C, fb, ea, i)
                out.append((Fr(1), X))
    return out


def rhs_A(C, n, i, E, Ep, orient, **kw):
    return sum((w * qn(X, n - 1) for w, X in terms(C, i, E, Ep, orient, **kw)), Fr(0))


def pauli_E(E):
    e1, e2 = E
    P = madd((1, outer(e1, e1)), (1, outer(e2, e2)))
    sx = madd((1, outer(e1, e2)), (1, outer(e2, e1)))
    sy = madd((Q(0, -1), outer(e1, e2)), (Q(0, 1), outer(e2, e1)))
    sz = madd((1, outer(e1, e1)), (-1, outer(e2, e2)))
    return P, (sx, sy, sz)


def bloch_N(E, d, sign=-1):
    """N[k,l,m,p] = int (Pi_a)_{kl} conj(Pi_b)_{mp} dmu with Pi_u=(P+n.s)/2, Pi_{u_perp}=(P-n.s)/2,
    uniform Bloch sphere: <n_j>=0, <n_j n_k>=delta_jk/3.  sign=-1: (a,b)=(u,u_perp) [correct];
    sign=+1: (a,b)=(u,u) [fault]."""
    P, sig = pauli_E(E)
    N = {}
    for k, l, m, p in itertools.product(range(d), repeat=4):
        v = P[k][l] * P[m][p].conj()
        acc = ZERO
        for s in sig:
            acc = acc + s[k][l] * s[m][p].conj()
        v = (v + acc * Fr(sign, 3)) * Fr(1, 4)
        if not v.iz():
            N[(k, l, m, p)] = v
    return N


def design_N(E, d, sign=-1):
    e1, e2 = E
    N = {}
    for al, be in OCT:
        u = lc(al, e1, be, e2)
        up = lc(-be.conj(), e1, al.conj(), e2)
        nn = al.abs2() + be.abs2()
        Pa = outer(u, u)
        Pb = outer(up, up) if sign == -1 else outer(u, u)
        for k, l, m, p in itertools.product(range(d), repeat=4):
            v = Pa[k][l] * Pb[m][p].conj() * (Fr(1, 6) / (nn * nn))
            if not v.iz():
                N[(k, l, m, p)] = N[(k, l, m, p)] + v if (k, l, m, p) in N else v
    return clean(N)


def rhs_B(C, n, i, E, Ep, orient, d):
    N = bloch_N(E, d, -1)
    unit = [[ONE if a == b else ZERO for a in range(d)] for b in range(d)]
    blocks = {(k, m): contract(C, unit[k], unit[m], i) for k in range(d) for m in range(d)}
    Ss = subsets(n - 1)
    PT = {km: [ptrace(B, S, n - 1) for S in Ss] for km, B in blocks.items()}
    cache = {}
    tot = ZERO
    for (k, l, m, p), v in N.items():
        key = ((k, m), (l, p))
        if key not in cache:
            t = ZERO
            for si, S in enumerate(Ss):
                t = t + hsip(PT[(k, m)][si], PT[(l, p)][si]) * (HN ** len(S))
            cache[key] = t
        tot = tot + v * cache[key]
    tot = tot * 3
    for ea in E:
        for fb in Ep:
            X = contract(C, ea, fb, i) if orient == 'out' else contract(C, fb, ea, i)
            tot = tot + qn(X, n - 1)
    return tot


def kmat_Q(d):
    """K = I - |Omega><Omega|/2 on C^d (x) C^d; index (k,m) -> k*d+m (k row-side, m column-side)."""
    Nn = d * d
    K = [[ONE if a == b else ZERO for b in range(Nn)] for a in range(Nn)]
    for a in range(Nn):
        for b in range(Nn):
            if a // d == a % d and b // d == b % d:
                K[a][b] = K[a][b] - Fr(1, 2)
    return K


def kron2(A, B):
    d1, d2 = len(A), len(B)
    return [[A[a // d2][b // d2] * B[a % d2][b % d2] for b in range(d1 * d2)] for a in range(d1 * d2)]


def N_as_matrix(N, d):
    M = [[ZERO] * (d * d) for _ in range(d * d)]
    for (k, l, m, p), v in N.items():
        M[k * d + m][l * d + p] = v
    return M


def ldl_psd(M):
    """Exact PSD test of a Hermitian Gaussian-rational matrix by symmetric Gaussian elimination."""
    n = len(M)
    A = [list(r) for r in M]
    minp, zeros = None, 0
    for k in range(n):
        p = A[k][k]
        if p.i != 0:
            return dict(psd=False, reason='nonreal pivot', k=k)
        if p.r < 0:
            return dict(psd=False, reason='negative pivot', k=k, pivot=fs(p.r))
        nz = [j for j in range(k + 1, n) if not A[k][j].iz()]
        if p.r == 0:
            if nz:
                return dict(psd=False, reason='zero pivot with nonzero row', k=k)
            zeros += 1
            continue
        minp = p.r if minp is None or p.r < minp else minp
        rowk = A[k]
        for i in nz:
            f = A[i][k] / p
            Ai = A[i]
            for j in nz:
                Ai[j] = Ai[j] - f * rowk[j]
    return dict(psd=True, min_positive_pivot=fs(minp), zero_pivots=zeros, n=n)


def ldl_psd_real(M):
    n = len(M)
    A = [list(r) for r in M]
    minp, zeros = None, 0
    for k in range(n):
        p = A[k][k]
        if p < 0:
            return dict(psd=False, reason='negative pivot', k=k, pivot=fs(p))
        nz = [j for j in range(k + 1, n) if A[k][j] != 0]
        if p == 0:
            if nz:
                return dict(psd=False, reason='zero pivot with nonzero row', k=k)
            zeros += 1
            continue
        minp = p if minp is None or p < minp else minp
        rowk = A[k]
        for i in nz:
            f = A[i][k] / p
            Ai = A[i]
            for j in nz:
                Ai[j] -= f * rowk[j]
    return dict(psd=True, min_positive_pivot=fs(minp), zero_pivots=zeros, n=n)


# ------------------------------------------------------------------ numpy helpers
LET = 'abcdefghijklmnopqrstuvwxyz'


def idx(x, d):
    r = 0
    for t in x:
        r = r * d + t
    return r


def to_np(C, n, d):
    Dn = d ** n
    M = np.zeros((Dn, Dn), dtype=complex)
    for (x, y), v in C.items():
        M[idx(x, d), idx(y, d)] = v.c()
    return M


def np_ptrace(M, n, S, d=4):
    rows, cols = list(LET[:n]), list(LET[n:2 * n])
    for i in S:
        cols[i] = rows[i]
    rest = [i for i in range(n) if i not in S]
    out = ''.join(rows[i] for i in rest) + ''.join(cols[i] for i in rest)
    r = np.einsum(''.join(rows) + ''.join(cols) + '->' + out, M.reshape([d] * (2 * n)))
    m = d ** len(rest)
    return np.asarray(r).reshape(m, m)


def np_q(M, n, d=4):
    t = 0.0
    for S in subsets(n):
        R = np_ptrace(M, n, S, d)
        t += (-0.5) ** len(S) * float(np.vdot(R, R).real)
    return t


def gellmann(d=4):
    B = []
    for j in range(d):
        for k in range(j + 1, d):
            S = np.zeros((d, d), complex)
            S[j, k] = S[k, j] = 1 / np.sqrt(2)
            B.append(S)
            A = np.zeros((d, d), complex)
            A[j, k], A[k, j] = -1j / np.sqrt(2), 1j / np.sqrt(2)
            B.append(A)
    for m in range(1, d):
        Dg = np.zeros((d, d), complex)
        for t in range(m):
            Dg[t, t] = 1
        Dg[m, m] = -m
        B.append(Dg / np.sqrt(m * (m + 1)))
    return B


def wodd_basis(n, d=4):
    G = gellmann(d)
    I = np.eye(d) / np.sqrt(d)
    basis = []
    for T in subsets(n):
        if len(T) % 2 == 0:
            continue
        choices = [[I] if i in T else G for i in range(n)]
        for combo in itertools.product(*choices):
            M = combo[0]
            for f in combo[1:]:
                M = np.kron(M, f)
            basis.append(M)
    return basis


def kappa_def(Fm, basis):
    Y = np.stack([(X @ Fm).reshape(-1) for X in basis], axis=1)
    H = Y @ Y.conj().T
    return float(np.linalg.eigvalsh(H)[-1])


def q_gram(Fm, n, d=4, side='right'):
    Dn = d ** n
    mats = []
    for r in range(Fm.shape[1]):
        for v in range(Dn):
            E = np.zeros((Dn, Dn), complex)
            if side == 'right':
                E[v, :] = Fm[:, r].conj()      # |v><f_r|  (C = C P_F)
            else:
                E[:, v] = Fm[:, r]             # |f_r><v|  (C = P_F C)
            mats.append(E)
    G = np.zeros((len(mats), len(mats)), complex)
    for S in subsets(n):
        M = np.stack([np_ptrace(E, n, S, d).reshape(-1) for E in mats], axis=1)
        G += (-0.5) ** len(S) * (M.conj().T @ M)
    return G


def spread(Fm, n, d=4):
    P = Fm @ Fm.conj().T
    s = 0.0
    for T in subsets(n):
        if len(T) % 2 == 0:
            continue
        R = np_ptrace(P, n, T, d)
        nr = float(np.linalg.eigvalsh(R)[-1]) if R.shape[0] > 1 else float(R[0, 0].real)
        s += 4.0 ** (-len(T)) * nr
    return s


def wrong_spread(Fm, n, d=4):
    """Deliberately wrong variant: normalised trace (average eigenvalue) instead of operator norm."""
    P = Fm @ Fm.conj().T
    s = 0.0
    for T in subsets(n):
        if len(T) % 2 == 0:
            continue
        R = np_ptrace(P, n, T, d)
        s += 4.0 ** (-len(T)) * float(np.trace(R).real) / R.shape[0]
    return s


def rand_F(nrng, n, d=4):
    A = nrng.normal(size=(d ** n, 2)) + 1j * nrng.normal(size=(d ** n, 2))
    Qm, _ = np.linalg.qr(A)
    return Qm


def rand_U(nrng, d=4):
    A = nrng.normal(size=(d, d)) + 1j * nrng.normal(size=(d, d))
    Qm, Rm = np.linalg.qr(A)
    return Qm * (np.diag(Rm) / np.abs(np.diag(Rm)))


# ------------------------------------------------------------------ mpmath helpers (n=2)
def mp_q2(M):
    tot = mp.mpf(0)
    for a in range(16):
        for b in range(16):
            tot += abs(M[a, b]) ** 2
    t = mp.mpf(0)
    for x2 in range(4):
        for y2 in range(4):
            t += abs(mp.fsum(M[4 * j + x2, 4 * j + y2] for j in range(4))) ** 2
    tot -= t / 2
    t = mp.mpf(0)
    for x1 in range(4):
        for y1 in range(4):
            t += abs(mp.fsum(M[4 * x1 + j, 4 * y1 + j] for j in range(4))) ** 2
    tot -= t / 2
    tot += abs(mp.fsum(M[a, a] for a in range(16))) ** 2 / 4
    return tot


def mp_ptr_vec2(M, S):
    """flattened Tr_S M for a 16x16 mp matrix, n=2, d=4."""
    if S == ():
        return [M[a, b] for a in range(16) for b in range(16)]
    if S == (0,):
        return [mp.fsum(M[4 * j + x2, 4 * j + y2] for j in range(4)) for x2 in range(4) for y2 in range(4)]
    if S == (1,):
        return [mp.fsum(M[4 * x1 + j, 4 * y1 + j] for j in range(4)) for x1 in range(4) for y1 in range(4)]
    return [mp.fsum(M[a, a] for a in range(16))]


def mp_gellmann(d=4):
    B = []
    s2 = mp.sqrt(2)
    for j in range(d):
        for k in range(j + 1, d):
            S = mp.matrix(d, d)
            S[j, k] = S[k, j] = 1 / s2
            B.append(S)
            A = mp.matrix(d, d)
            A[j, k], A[k, j] = mp.mpc(0, -1) / s2, mp.mpc(0, 1) / s2
            B.append(A)
    for m in range(1, d):
        Dg = mp.matrix(d, d)
        for t in range(m):
            Dg[t, t] = 1
        Dg[m, m] = -m
        B.append(Dg / mp.sqrt(m * (m + 1)))
    return B


def mp_kron(A, B):
    r1, c1, r2, c2 = A.rows, A.cols, B.rows, B.cols
    R = mp.matrix(r1 * r2, c1 * c2)
    for a in range(r1):
        for b in range(c1):
            if A[a, b] == 0:
                continue
            for c in range(r2):
                for e in range(c2):
                    R[a * r2 + c, b * c2 + e] = A[a, b] * B[c, e]
    return R


def mp_orthonormalize(cols):
    out = []
    for v in cols:
        w = v.copy()
        for u in out:
            ip = mp.fsum(mp.conj(u[t]) * w[t] for t in range(len(w)))
            w = mp.matrix([w[t] - ip * u[t] for t in range(len(w))])
        nr = mp.sqrt(mp.fsum(abs(w[t]) ** 2 for t in range(len(w))))
        out.append(w / nr)
    return out


# ================================================================== sections
def sec_inputs(R):
    out = {}
    for p, (h, b, lf) in EXPECT.items():
        data = open(p, 'rb').read()
        hh = hashlib.sha256(data).hexdigest()
        out[os.path.basename(p)] = dict(sha256=hh, bytes=len(data), LF=data.count(b'\n'),
                                        match=(hh == h and len(data) == b and data.count(b'\n') == lf))
    add = json.loads(open(ADD, 'rb').read().decode('utf-8'))
    out['addendum_parsed_as_data_only'] = dict(
        n_keys=len(add), keys=sorted(add.keys()),
        all_values_strings=all(isinstance(v, str) for v in add.values()),
        packet_sha256_equals_candidate=(add.get('packet_sha256') == EXPECT[CAND][0]),
        declared_script=add.get('script'), declared_result=add.get('result'),
        declared_verdict_NOT_USED_AS_EVIDENCE=add.get('verdict'))
    pos('inputs_sha256_bytes_LF', all(v['match'] for k, v in out.items() if 'match' in v))
    R['inputs'] = out


def sec_identity1(R):
    rng = random.Random(16801)
    rows, ok_all = [], True
    for n, kind in [(2, 'full'), (2, 'full'), (2, 'rank2'), (2, 'rank2'), (3, 'full'), (3, 'rank2')]:
        C = rop(rng, n, D4) if kind == 'full' else rrank2(rng, n, D4)
        q = qn(C, n)
        po = p_odd(C, n, D4)
        rhs = hs2(C) - 2 * hs2(po)
        kC = kop(C, n, D4)
        vq = hsip(C, kC)
        proj = op_eq(op_lin((Fr(1, 2), C), (Fr(-1, 2), kC)), po)
        idem = op_eq(p_odd(po, n, D4), po)
        Ts = subsets(n)
        secs = {T: sector(C, T, n, D4) for T in Ts}
        compl = op_eq(op_lin(*[(1, s) for s in secs.values()]), C)
        orth = all(hsip(secs[T1], secs[T2]).iz() for a, T1 in enumerate(Ts) for T2 in Ts[a + 1:])
        struct = all(sector_structure_ok(secs[T], T, n, D4) for T in Ts)
        ok = (q == rhs) and (vq == q) and proj and idem and compl and orth and struct
        ok_all = ok_all and ok
        rows.append(dict(n=n, kind=kind, q=fs(q), norm2_minus_2_Podd2=fs(rhs), vec_form_equal=(vq == q),
                         Pi_minus_eq_half_I_minus_K=proj, Podd_idempotent=idem, sectors_complete=compl,
                         sectors_pairwise_orthogonal=orth, sector_form_I_T_x_traceless=struct, ok=ok))
    pos('identity1_q_eq_norm2_minus_2_Podd2_exact_d4', ok_all, cases=rows)
    # K^2 = I and Tr K = 14 at d=4; K^2 != I at d=3
    K4, K3 = kmat_Q(4), kmat_Q(3)
    k4sq = meq(mmul(K4, K4), mid(16))
    trK4 = sum((K4[a][a] for a in range(16)), ZERO)
    pos('K_reflection_d4', k4sq and trK4 == 14, K2_eq_I=k4sq, trace_K=fs(trK4.r))
    neg('K_not_reflection_d3', not meq(mmul(K3, K3), mid(9)))
    rng3 = random.Random(16802)
    C3 = rop(rng3, 2, 3)
    q3, r3 = qn(C3, 2), hs2(C3) - 2 * hs2(p_odd(C3, 2, 3))
    neg('identity1_fails_at_d3', q3 != r3, q=fs(q3), rhs=fs(r3))
    C = rop(rng, 3, D4)
    tr = ptrace(C, (0, 1, 2), 3)
    q, rt = qn(C, 3), hs2(C) - 2 * hs2(p_odd(C, 3, D4, keep=lambda T: len(T) == 1))
    neg('identity1_fails_if_T123_sector_dropped', q != rt and bool(tr), q=fs(q), rhs_truncated=fs(rt))


def sec_dims(R):
    out, ok = {}, True
    K4 = kmat_Q(4)
    trK = sum((K4[a][a] for a in range(16)), ZERO).r
    for n in (2, 3):
        exact = (Fr(16) ** n - trK ** n) / 2
        sector_count = sum(15 ** (n - len(T)) for T in subsets(n) if len(T) % 2)
        B = wodd_basis(n)
        Mx = np.stack([b.reshape(-1) for b in B], axis=1)
        err = float(np.max(np.abs(Mx.conj().T @ Mx - np.eye(len(B)))))
        rk = int(np.linalg.matrix_rank(Mx))
        good = exact == sector_count == len(B) == rk and err < 1e-12
        ok = ok and good
        out[str(n)] = dict(trace_Pi_minus_exact=fs(exact), sector_formula=sector_count,
                           basis_size=len(B), numeric_rank=rk, orthonormality_err=err)
    pos('dim_W_odd_30_676', ok, detail=out)


def ky_fan_numeric(X, n, nrng, samples=300):
    nX2 = float(np.vdot(X, X).real)
    U, s, Vh = np.linalg.svd(X)
    r = (s[0] ** 2 + s[1] ** 2) / nX2
    X2 = (U[:, :2] * s[:2]) @ Vh[:2, :]
    Cs = X2 / np.linalg.norm(X2)
    Xh = X / np.sqrt(nX2)
    ip = abs(np.vdot(Xh, Cs)) ** 2
    qC = np_q(Cs, n)
    mx = 0.0
    Dn = X.shape[0]
    for _ in range(samples):
        a = nrng.normal(size=(Dn, 2)) + 1j * nrng.normal(size=(Dn, 2))
        b = nrng.normal(size=(Dn, 2)) + 1j * nrng.normal(size=(Dn, 2))
        Cr = a @ b.conj().T
        Cr /= np.linalg.norm(Cr)
        mx = max(mx, abs(np.vdot(Xh, Cr)) ** 2)
    ok = bool(abs(ip - r) < TOL and qC <= 1 - 2 * r + TOL and mx <= r + TOL)
    return ok, dict(ratio_sigma12_over_norm2=r, attained_overlap=ip, q_at_truncation=qC,
                    bound_1_minus_2ratio=1 - 2 * r, max_overlap_random_rank2=mx)


def rand_sl(rng, d, k=3):
    A = [[rq(rng, k) for _ in range(d)] for _ in range(d)]
    s = ZERO
    for j in range(d - 1):
        s = s + A[j][j]
    A[d - 1][d - 1] = -s
    return A


def sl2_proj(Z, d):
    t1, t2, tt = ptrace(Z, (0,), 2), ptrace(Z, (1,), 2), ptrace(Z, (0, 1), 2)
    return op_lin((1, Z), (Fr(-1, d), embed_id(t1, (0,), 2, d)), (Fr(-1, d), embed_id(t2, (1,), 2, d)),
                  (Fr(1, d * d), embed_id(tt, (0, 1), 2, d)))


def sec_theorem1(R):
    rng = random.Random(16803)
    nrng = np.random.default_rng(16804)
    rows, ok_all = [], True
    mp.mp.dps = 40
    for t in range(3):     # n = 2
        A, B = rand_sl(rng, 4), rand_sl(rng, 4)
        X = op_lin((1, embed_id(op1(A), (1,), 2, 4)), (1, embed_id(op1(B), (0,), 2, 4)))
        mem = op_eq(p_odd(X, 2, 4), X)
        nrm = hs2(X) == 4 * (hs2(op1(A)) + hs2(op1(B)))
        okn, info = ky_fan_numeric(to_np(X, 2, 4), 2, nrng)
        # mpmath corroboration
        Xm = mp.matrix(to_np(X, 2, 4).tolist())
        for a in range(16):
            for b in range(16):
                v = X.get(((a // 4, a % 4), (b // 4, b % 4)))
                Xm[a, b] = mp.mpc(mp.mpf(v.r.numerator) / v.r.denominator,
                                  mp.mpf(v.i.numerator) / v.i.denominator) if v is not None else mp.mpc(0)
        Um, Sm, Vm = mp.svd_c(Xm)
        recon = mp.mnorm(Um * mp.diag(Sm) * Vm - Xm, 1)
        nX2 = mp.fsum(abs(Xm[a, b]) ** 2 for a in range(16) for b in range(16))
        rmp = (Sm[0] ** 2 + Sm[1] ** 2) / nX2
        X2 = Um[:, 0:2] * mp.diag([Sm[0], Sm[1]]) * Vm[0:2, :]
        nX2t = mp.sqrt(mp.fsum(abs(X2[a, b]) ** 2 for a in range(16) for b in range(16)))
        Cs = X2 / nX2t
        qmp = mp_q2(Cs)
        okm = recon < mp.mpf(10) ** -30 and qmp <= 1 - 2 * rmp + mp.mpf(10) ** -30 and \
            abs(rmp - info['ratio_sigma12_over_norm2']) < 1e-10
        ok = bool(mem and nrm and okn and okm)
        ok_all = ok_all and ok
        info.update(n=2, X_in_W_odd_exact=mem, norm_formula_exact=nrm, mp_ratio=mp.nstr(rmp, 30),
                    mp_q_trunc=mp.nstr(qmp, 30), mp_svd_recon_err=mp.nstr(recon, 5), ok=ok)
        rows.append(info)
    for t in range(2):     # n = 3
        c = rq(rng)
        Ys = [sl2_proj(rop(rng, 2, 4), 4) for _ in range(3)]
        tr_ok = all(not ptrace(Y, (0,), 2) and not ptrace(Y, (1,), 2) for Y in Ys)
        X = op_lin((1, embed_id({((), ()): c}, (0, 1, 2), 3, 4)),
                   (1, embed_id(Ys[0], (0,), 3, 4)), (1, embed_id(Ys[1], (1,), 3, 4)),
                   (1, embed_id(Ys[2], (2,), 3, 4)))
        mem = op_eq(p_odd(X, 3, 4), X)
        nrm = hs2(X) == 64 * c.abs2() + 4 * sum((hs2(Y) for Y in Ys), Fr(0))
        okn, info = ky_fan_numeric(to_np(X, 3, 4), 3, nrng, samples=100)
        ok = bool(mem and nrm and tr_ok and okn)
        ok_all = ok_all and ok
        info.update(n=3, Y_in_sl4_x_sl4_exact=tr_ok, X_in_W_odd_exact=mem, norm_formula_exact=nrm, ok=ok)
        rows.append(info)
    pos('theorem1_vector_dual_instances', ok_all, cases=rows)

    # equality (single-sector, rank-one Z) -- exact
    e = lambda j: [ONE if t == j else ZERO for t in range(4)]
    Z = op1(outer(e(0), e(1)))                                   # |0><1|, traceless, rank 1
    X = embed_id(Z, (0,), 2, 4)                                   # I (x) |0><1|
    Ceq = op_lin((1, ketbra({(0, 0): ONE}, {(0, 1): ONE})), (1, ketbra({(1, 0): ONE}, {(1, 1): ONE})))
    PC = p_odd(Ceq, 2, 4)
    eq2 = (op_eq(p_odd(X, 2, 4), X) and qn(Ceq, 2) == 0 and hs2(PC) == hs2(Ceq) / 2
           and op_eq(PC, op_lin((Fr(1, 2), X))))
    Z3 = ketbra({(0, 0): ONE}, {(1, 1): ONE})                    # |00><11| in sl4 (x) sl4
    X3 = embed_id(Z3, (0,), 3, 4)
    C3 = op_lin((1, ketbra({(0, 0, 0): ONE}, {(0, 1, 1): ONE})), (1, ketbra({(1, 0, 0): ONE}, {(1, 1, 1): ONE})))
    eq3 = op_eq(p_odd(X3, 3, 4), X3) and qn(C3, 3) == 0 and hs2(p_odd(C3, 3, 4)) == hs2(C3) / 2
    pos('single_sector_rank1_equality_exact', eq2 and eq3, n2=eq2, n3=eq3,
        note='I(x)|0><1| (n=2) and I(x)|00><11| (n=3): sigma1^2+sigma2^2 = ||X||^2/2, q(X_(2)) = 0')
    # strict single-sector case: Z = |0><1| + |2><3| (rank 2): singular values of I(x)Z all 1 (8 of them)
    Zs = op1(madd((1, outer(e(0), e(1))), (1, outer(e(2), e(3)))))
    Xs = to_np(embed_id(Zs, (0,), 2, 4), 2, 4)
    sv = np.linalg.svd(Xs, compute_uv=False)
    pos('single_sector_rank2_strict', abs(sv[0] ** 2 + sv[1] ** 2 - 2) < TOL and
        abs(float(np.vdot(Xs, Xs).real) / 2 - 4) < TOL, s1s2=float(sv[0] ** 2 + sv[1] ** 2), half_norm2=4.0)

    # Section-6 non-traceless remark, exact (X is diagonal)
    A = [[Q(1) if (a, b) == (0, 0) else ZERO for b in range(4)] for a in range(4)]
    B = [[Q(2) if (a, b) == (0, 0) else ZERO for b in range(4)] for a in range(4)]
    Xn = op_lin((1, embed_id(op1(A), (1,), 2, 4)), (1, embed_id(op1(B), (0,), 2, 4)))
    diag = sorted([Xn.get(((a, b), (a, b)), ZERO).r for a in range(4) for b in range(4)], reverse=True)
    offdiag = all(k[0] == k[1] for k in Xn)
    s12 = diag[0] ** 2 + diag[1] ** 2
    n2 = hs2(Xn)
    X2n = op_lin((Fr(3), ketbra({(0, 0): ONE}, {(0, 0): ONE})), (Fr(2), ketbra({(1, 0): ONE}, {(1, 0): ONE})))
    q_tr = qn(X2n, 2)
    ok = offdiag and [fs(v) for v in diag] == ['3', '2', '2', '2', '1', '1', '1'] + ['0'] * 9 and \
        s12 == 13 and n2 == 24 and s12 > n2 / 2
    pos('nontraceless_remark_13_gt_12_exact', ok, singular_values=[fs(v) for v in diag],
        s1s2=fs(s12), half_norm2=fs(n2 / 2), q2_of_truncation=fs(q_tr))
    neg('nontraceless_violation_is_not_a_q_violation', q_tr > 0, q2_of_truncation=fs(q_tr),
        note='violating the Ky Fan inequality outside W_odd does not produce q<0: the dual needs W_odd')


def sec_theorem23(R):
    nrng = np.random.default_rng(16805)
    out, ok_all = {}, True
    for n, nrand in ((2, 6), (3, 3)):
        basis = wodd_basis(n)
        cases = []
        Fs = [('random', rand_F(nrng, n)) for _ in range(nrand)]
        Dn = 4 ** n
        # maximally correlated with all w_j = 1/2
        f0, f1 = np.zeros(Dn, complex), np.zeros(Dn, complex)
        for j in (0, 1):
            f0[idx((j,) * n, 4)] = 1 / np.sqrt(2)
        for j in (2, 3):
            f1[idx((j,) * n, 4)] = 1 / np.sqrt(2)
        Fs.append(('maxcorr_w_half', np.stack([f0, f1], axis=1)))
        # product range span{|0..0>, |1 0..0>}
        g0, g1 = np.zeros(Dn, complex), np.zeros(Dn, complex)
        g0[idx((0,) * n, 4)] = 1
        g1[idx((1,) + (0,) * (n - 1), 4)] = 1
        Fs.append(('product_E_x_0', np.stack([g0, g1], axis=1)))
        for name, Fm in Fs:
            kd = kappa_def(Fm, basis)
            G = q_gram(Fm, n)
            lmin = float(np.linalg.eigvalsh(G)[0])
            kdual = (1 - lmin) / 2
            Gl = q_gram(Fm, n, side='left')
            lmin_l = float(np.linalg.eigvalsh(Gl)[0])
            s = spread(Fm, n)
            ok = abs(kd - kdual) < TOL and abs(lmin - lmin_l) < TOL and kd <= s + TOL
            ok_all = ok_all and ok
            cases.append(dict(F=name, kappa_by_definition=kd, kappa_from_min_q=kdual,
                              min_q_right=lmin, min_q_left=lmin_l, spread_s=s, ok=ok))
        # local-unitary invariance on the first random F
        Fm = Fs[0][1]
        U = rand_U(nrng)
        for _ in range(n - 1):
            U = np.kron(U, rand_U(nrng))
        k1, k2 = kappa_def(Fm, basis), kappa_def(U @ Fm, basis)
        inv = abs(k1 - k2) < TOL
        ok_all = ok_all and inv
        out[str(n)] = dict(cases=cases, local_unitary_invariance=dict(k=k1, kU=k2, ok=inv))
        if n == 2:
            prod = [c for c in cases if c['F'] == 'product_E_x_0'][0]
            Fp = Fs[-1][1]
            ws = wrong_spread(Fp, 2)
            neg('wrong_spread_normalised_trace_violated', prod['kappa_by_definition'] > ws + 1e-6,
                kappa=prod['kappa_by_definition'], wrong_spread=ws, correct_spread=prod['spread_s'],
                note='operator norm in (3) cannot be replaced by the average eigenvalue')
    pos('theorem2_3_range_dual_and_spread_numeric', ok_all, detail=out,
        error_model='float64 Hermitian eigensolvers; kappa computed two independent ways '
                    '(W_odd Gram and 1-2kappa=min q on {C=CP_F}); agreement < 1e-9 required')

    # mpmath corroboration at n=2 (dps 40)
    mp.mp.dps = 40
    rng = random.Random(16806)
    GM = mp_gellmann()
    I4 = mp.eye(4) / 2
    Wb = []
    for M in GM:
        Wb.append(mp_kron(I4, M))
    for M in GM:
        Wb.append(mp_kron(M, I4))
    rows, okm = [], True
    for t in range(2):
        raw = [mp.matrix([mp.mpc(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(16)]) for _ in range(2)]
        fr = mp_orthonormalize(raw)
        # kappa by definition
        Y = mp.matrix(32, 30)
        for a, X in enumerate(Wb):
            for r in range(2):
                v = X * fr[r]
                for k in range(16):
                    Y[r * 16 + k, a] = v[k]
        H = Y * Y.transpose_conj()
        ev = mp.eigh(H, eigvals_only=True)
        kd = max(ev[t] for t in range(ev.rows))
        # min q on {C = C P_F}
        Es = []
        for r in range(2):
            for v in range(16):
                E = mp.matrix(16, 16)
                for y in range(16):
                    E[v, y] = mp.conj(fr[r][y])
                Es.append(E)
        G = mp.matrix(32, 32)
        for S, cS in (((), 1), ((0,), -0.5), ((1,), -0.5), ((0, 1), 0.25)):
            vecs = [mp_ptr_vec2(E, S) for E in Es]
            for a in range(32):
                for b in range(32):
                    G[a, b] += mp.mpf(cS) * mp.fsum(mp.conj(vecs[a][k]) * vecs[b][k] for k in range(len(vecs[a])))
        evg = mp.eigh(G, eigvals_only=True)
        kq = (1 - min(evg[t] for t in range(evg.rows))) / 2
        # spread
        P = fr[0] * fr[0].transpose_conj() + fr[1] * fr[1].transpose_conj()
        red1 = mp.matrix(4, 4)
        red2 = mp.matrix(4, 4)
        for a in range(4):
            for b in range(4):
                red1[a, b] = mp.fsum(P[4 * a + j, 4 * b + j] for j in range(4))   # site-1 reduction
                red2[a, b] = mp.fsum(P[4 * j + a, 4 * j + b] for j in range(4))   # site-2 reduction
        e1v, e2v = mp.eigh(red1, eigvals_only=True), mp.eigh(red2, eigvals_only=True)
        s = (max(e1v[t] for t in range(e1v.rows)) + max(e2v[t] for t in range(e2v.rows))) / 4
        good = abs(kd - kq) < mp.mpf(10) ** -30 and kd <= s
        okm = okm and good
        rows.append(dict(kappa_def=mp.nstr(kd, 30), kappa_from_min_q=mp.nstr(kq, 30), spread=mp.nstr(s, 30),
                         ok=good))
    pos('theorem2_3_mpmath_dps40_n2', okm, cases=rows)

    # Converse construction needs W_odd: exact negative with the non-traceless X
    A = [[Q(1) if (a, b) == (0, 0) else ZERO for b in range(4)] for a in range(4)]
    B = [[Q(2) if (a, b) == (0, 0) else ZERO for b in range(4)] for a in range(4)]
    Xn = op_lin((1, embed_id(op1(A), (1,), 2, 4)), (1, embed_id(op1(B), (0,), 2, 4)))
    PF = op_lin((1, ketbra({(0, 0): ONE}, {(0, 0): ONE})), (1, ketbra({(1, 0): ONE}, {(1, 0): ONE})))
    XP = {}
    for (x, y), v in Xn.items():
        for (y2, z), w in PF.items():
            if y == y2:
                XP[(x, z)] = XP[(x, z)] + v * w if (x, z) in XP else v * w
    XP = clean(XP)
    ratio = hs2(XP) / hs2(Xn)
    qXP = qn(XP, 2)
    neg('converse_fails_outside_W_odd_exact', ratio > Fr(1, 2) and qXP > 0, ratio=fs(ratio), q2_of_XPF=fs(qXP),
        note='||X P_F||^2/||X||^2 = 13/24 > 1/2 for X=|0><0|(x)I+2I(x)|0><0| not in W_odd, yet q2(XP_F)=1/4>0')


def gram_exact(fvecs, n, d, side='right'):
    ids = list(itertools.product(range(d), repeat=n))
    basis = []
    for f in fvecs:
        for v in ids:
            basis.append(ketbra({v: ONE}, f) if side == 'right' else ketbra(f, {v: ONE}))
    Ss = subsets(n)
    PT = [[ptrace(E, S, n) for S in Ss] for E in basis]
    N = len(basis)
    G = [[ZERO] * N for _ in range(N)]
    for a in range(N):
        for b in range(a, N):
            t = ZERO
            for si, S in enumerate(Ss):
                ip = hsip(PT[a][si], PT[b][si])
                if not ip.iz():
                    t = t + ip * (HN ** len(S))
            G[a][b] = t
            G[b][a] = t.conj()
    return G


def sec_certificates(R):
    out = {}
    allok = True
    for n, t_claim, name in ((2, Fr(1, 2), 'D2'), (3, Fr(3, 16), 'D3')):
        f0 = {(0,) * n: ONE, (1,) * n: ONE}       # unnormalised, ||f||^2 = 2
        f1 = {(2,) * n: ONE, (3,) * n: ONE}
        res = {}
        for side in ('right', 'left'):
            G = gram_exact([f0, f1], n, 4, side)
            real = all(v.i == 0 for row in G for v in row)
            Gr = [[v.r for v in row] for row in G]
            # q(C) >= t ||C||^2  <=>  G - 2 t I >= 0   (||C||^2 = 2 sum_r ||c_r||^2)
            M = [[Gr[a][b] - (2 * t_claim if a == b else 0) for b in range(len(Gr))] for a in range(len(Gr))]
            cert = ldl_psd_real(M)
            lmin = float(np.linalg.eigvalsh(np.array([[float(v) for v in row] for row in Gr]))[0]) / 2
            # LDL tool negative: t slightly above the numerical minimum must fail
            t_bad = Fr(lmin).limit_denominator(10 ** 6) + Fr(1, 10 ** 4)
            Mbad = [[Gr[a][b] - (2 * t_bad if a == b else 0) for b in range(len(Gr))] for a in range(len(Gr))]
            bad = ldl_psd_real(Mbad)
            res[side] = dict(real=real, certificate=cert, numeric_min_q_over_norm2=lmin,
                             t_claim=fs(t_claim), t_bad=fs(t_bad), t_bad_result=bad)
            allok = allok and real and cert['psd']
            neg(f'ldl_rejects_bound_above_minimum_{name}_{side}', not bad['psd'], t_bad=fs(t_bad))
        out[name] = res
    pos('maxcorr_exact_psd_certificates_D2_half_D3_3over16', allok, detail=out)

    # Z_2 / Z_3 witnesses: all legs of dimension 4, strictly positive
    wit = {}
    okw = True
    for n, name in ((2, 'Z2'), (3, 'Z3')):
        f0 = {(0,) * n: ONE, (1,) * n: ONE}
        f1 = {(2,) * n: ONE, (3,) * n: ONE}
        g0 = {(0,) * n: ONE, (2,) * n: ONE}
        g1 = {(1,) * n: ONE, (3,) * n: ONE}
        C0 = op_lin((1, ketbra(g0, f0)), (1, ketbra(g1, f1)))
        legs = all_legs(C0, n, 4)
        q0 = qn(C0, n)
        rk = op_rank(C0, n, 4)
        good = all(v == 4 for v in legs.values()) and rk == 2 and q0 > 0
        okw = okw and good
        wit[name] = dict(legs=legs, rank=rk, q=fs(q0), norm2=fs(hs2(C0)), ok=good)
    pos('zero_leg_witnesses_all_legs_4_strictly_positive', okw, detail=wit)

    # openness illustration (numeric): factor perturbations keep rank 2, legs 4, s<1/2, q>0
    nrng = np.random.default_rng(16807)
    n = 3
    Dn = 64
    f0, f1, g0, g1 = (np.zeros(Dn, complex) for _ in range(4))
    for j in (0, 1):
        f0[idx((j,) * 3, 4)] = 1
    for j in (2, 3):
        f1[idx((j,) * 3, 4)] = 1
    for j in (0, 2):
        g0[idx((j,) * 3, 4)] = 1
    for j in (1, 3):
        g1[idx((j,) * 3, 4)] = 1
    rows, okp = [], True
    for eps in (1e-3, 1e-2, 5e-2):
        for _ in range(3):
            pf = [v + eps * (nrng.normal(size=Dn) + 1j * nrng.normal(size=Dn)) for v in (f0, f1)]
            pg = [v + eps * (nrng.normal(size=Dn) + 1j * nrng.normal(size=Dn)) for v in (g0, g1)]
            C = np.outer(pg[0], pf[0].conj()) + np.outer(pg[1], pf[1].conj())
            Fm, _ = np.linalg.qr(np.stack(pf, axis=1))
            s = spread(Fm, 3)
            qv = np_q(C, 3) / float(np.vdot(C, C).real)
            T = C.reshape([4] * 6)
            legs = []
            for i in range(3):
                Mo = np.moveaxis(T, i, 0).reshape(4, -1)
                Mi = np.moveaxis(T, 3 + i, 0).reshape(4, -1)
                legs += [int(np.linalg.matrix_rank(Mo, tol=1e-8)), int(np.linalg.matrix_rank(Mi, tol=1e-8))]
            good = s < 0.5 and qv >= 1 - 2 * s - TOL and qv > 0 and all(v == 4 for v in legs)
            okp = okp and good
            rows.append(dict(eps=eps, spread=s, q_over_norm2=qv, bound=1 - 2 * s, legs=legs, ok=good))
    pos('openness_illustration_numeric', okp, cases=rows,
        note='illustration only; openness itself follows from continuity, not from sampling')


def sec_lemma4(R):
    rng = random.Random(16808)
    rows, ok = [], True
    for (m, k) in ((1, 1), (1, 2), (2, 1)):
        A, B = rrank2(rng, m, 4), rop(rng, k, 4)
        lhs = qn(tensor(A, m, B, k), m + k)
        rhs = qn(A, m) * qn(B, k)
        rows.append(dict(m=m, k=k, lhs=fs(lhs), rhs=fs(rhs), ok=lhs == rhs))
        ok = ok and lhs == rhs
    u = rvec(rng, 1, 4)
    q1u = qn(ketbra(u, u), 1)
    nu = sum((v.abs2() for v in u.values()), Fr(0))
    ok = ok and q1u == nu * nu / 2
    # site permutation: C' (x) |u><u| with the rank-one factor at site 1 vs site 3
    Cp = rrank2(rng, 2, 4)
    P3 = tensor(Cp, 2, ketbra(u, u), 1)
    P1 = permute_sites(P3, (2, 0, 1))
    perm_ok = qn(P3, 3) == qn(P1, 3) == qn(Cp, 2) * q1u
    ok = ok and perm_ok
    pos('lemma4_factorisation_exact', ok, cases=rows, q1_uu_eq_norm4_over_2=(q1u == nu * nu / 2),
        permutation_invariance=perm_ok)


def sec_lemma5(R):
    rng = random.Random(16809)
    U = cayley(rng, 4)
    unitary = meq(mmul(mdag(U), U), mid(4))
    E = (colv(U, 0), colv(U, 1))
    Ep = (colv(U, 2), colv(U, 3))
    P = madd((1, outer(E[0], E[0])), (1, outer(E[1], E[1])))
    Pc = mconj(P)
    I4 = mid(4)
    # operator-level identities (16x16)
    K = kmat_Q(4)
    Nb = bloch_N(E, 4, -1)
    Nd = design_N(E, 4, -1)
    design_eq_bloch = Nb.keys() == Nd.keys() and all(Nb[k] == Nd[k] for k in Nb)
    NM = N_as_matrix(Nb, 4)
    Po = kron2(P, I4)
    Pi = kron2(I4, Pc)
    lhs_out = mmul(mmul(Po, K), Po)
    rhs_out = madd((3, NM), (1, kron2(P, madd((1, I4), (-1, Pc)))))
    lhs_in = mmul(mmul(Pi, K), Pi)
    rhs_in = madd((3, NM), (1, kron2(madd((1, I4), (-1, P)), Pc)))
    op_ok = meq(lhs_out, rhs_out) and meq(lhs_in, rhs_in)
    psd_comp = ldl_psd(lhs_out)
    pos('lemma5_operator_identity_exact', unitary and design_eq_bloch and op_ok and psd_comp['psd'],
        U_unitary=unitary, octahedron_design_equals_bloch_moments=design_eq_bloch, out_and_in_identities=op_ok,
        compressed_K_2dim_leg_psd=psd_comp)
    # operator-level faults
    NM3 = N_as_matrix(bloch_N(E, 4, +1), 4)
    neg('lemma5_op_fault_weight2', not meq(lhs_out, madd((2, NM), (1, kron2(P, madd((1, I4), (-1, Pc)))))))
    neg('lemma5_op_fault_drop_perp', not meq(lhs_out, madd((3, NM),)))
    neg('lemma5_op_fault_u_for_uperp', not meq(lhs_out, madd((3, NM3), (1, kron2(P, madd((1, I4), (-1, Pc)))))))
    # 3-dim leg: compression of K is not PSD
    E3 = [[ONE if (a == b and a < 3) else ZERO for b in range(4)] for a in range(4)]
    lhs3 = mmul(mmul(kron2(E3, I4), K), kron2(E3, I4))
    neg('compressed_K_3dim_leg_not_psd', not ldl_psd(lhs3)['psd'])

    # end-to-end identities (5)/(6), every site, n = 2 and 3, both methods
    rows, ok_all = [], True
    for n, kinds in ((2, ('full', 'rank2')), (3, ('full', 'rank2'))):
        for i in range(n):
            for orient in ('out', 'in'):
                for kind in kinds:
                    Craw = rop(rng, n, 4) if kind == 'full' else rrank2(rng, n, 4)
                    C = left_site(P, Craw, i) if orient == 'out' else right_site(Craw, P, i)
                    leg_ok = op_eq(left_site(P, C, i), C) if orient == 'out' else op_eq(right_site(C, P, i), C)
                    q = qn(C, n)
                    rA = rhs_A(C, n, i, E, Ep, orient)
                    rB = rhs_B(C, n, i, E, Ep, orient, 4)
                    good = leg_ok and q == rA and rB == q
                    ok_all = ok_all and good
                    rows.append(dict(n=n, site=i + 1, orient=orient, kind=kind, q=fs(q), method_A=fs(rA),
                                     method_B=fs(rB.r) + ('' if rB.i == 0 else f'+{rB.i}i'), ok=good))
    pos('lemma5_identities_5_6_exact_all_sites', ok_all, E_basis='columns 0,1 of an exact Cayley unitary',
        cases=rows)
    # end-to-end faults (n=3, site 2)
    Craw = rrank2(rng, 3, 4)
    C = left_site(P, Craw, 1)
    q = qn(C, 3)
    f1 = rhs_A(C, 3, 1, E, Ep, 'out', weight=2)
    f2 = rhs_A(C, 3, 1, E, Ep, 'out', drop_perp=True)
    f3 = rhs_A(C, 3, 1, E, Ep, 'out', use_u=True)
    f4 = rhs_A(C, 3, 1, E, Ep, 'in')           # wrong orientation: C has its OUTPUT leg in E
    neg('lemma5_fault_weight2', f1 != q, q=fs(q), faulty=fs(f1))
    neg('lemma5_fault_drop_perp', f2 != q, q=fs(q), faulty=fs(f2))
    neg('lemma5_fault_u_for_uperp', f3 != q, q=fs(q), faulty=fs(f3))
    neg('lemma5_fault_wrong_orientation', f4 != q, q=fs(q), faulty=fs(f4))


def iterate(C, n, plan):
    """plan: list of (site_index_in_current_operator, E, Ep, orient). Returns list of (weight, X)."""
    cur = [(Fr(1), C)]
    m = n
    for (i, E, Ep, orient) in plan:
        nxt = []
        for w, X in cur:
            for w2, X2 in terms(X, i, E, Ep, orient):
                nxt.append((w * w2, X2))
        cur = nxt
        m -= 1
    return cur, m


def sec_ladder(R):
    rng = random.Random(16810)
    mk = lambda: cayley(rng, 4)
    def leg(U):
        E = (colv(U, 0), colv(U, 1))
        Ep = (colv(U, 2), colv(U, 3))
        P = madd((1, outer(E[0], E[0])), (1, outer(E[1], E[1])))
        return E, Ep, P
    out = {}
    # (i) one-leg stratum: exactly one 2-supported leg (output, site 3), rank 2
    E3, Ep3, P3 = leg(mk())
    a = [left_site_vec(P3, rvec(rng, 3, 4), 2) for _ in range(2)]
    b = [rvec(rng, 3, 4) for _ in range(2)]
    C = op_lin((1, ketbra(a[0], b[0])), (1, ketbra(a[1], b[1])))
    legs = all_legs(C, 3, 4)
    q = qn(C, 3)
    tl = terms(C, 2, E3, Ep3, 'out')
    rA = sum((w * qn(X, 2) for w, X in tl), Fr(0))
    ranks = sorted(set(op_rank(X, 2, 4) for _, X in tl))
    good1 = legs['out@3'] == 2 and sum(1 for v in legs.values() if v <= 2) == 1 and q == rA and max(ranks) <= 2
    out['one_leg'] = dict(legs=legs, rank=op_rank(C, 3, 4), q=fs(q), contraction_sum=fs(rA),
                          contraction_ranks=ranks, ok=good1,
                          note='q3 = positive combination of q2 on rank<=2 operators: needs T_2')
    # (ii) two distinct sites (output@1 in E1, input@2 in E2), rank 2 -> q1 terms, all >= 0
    E1, Ep1, P1 = leg(mk())
    E2, Ep2, P2 = leg(mk())
    a = [left_site_vec(P1, rvec(rng, 3, 4), 0) for _ in range(2)]
    b = [left_site_vec(P2, rvec(rng, 3, 4), 1) for _ in range(2)]
    C = op_lin((1, ketbra(a[0], b[0])), (1, ketbra(a[1], b[1])))
    legs2 = all_legs(C, 3, 4)
    q = qn(C, 3)
    lvl1 = terms(C, 0, E1, Ep1, 'out')
    pres = all(op_eq(right_site(X, P2, 0), X) for _, X in lvl1)
    tl, m = iterate(C, 3, [(0, E1, Ep1, 'out'), (0, E2, Ep2, 'in')])
    vals = [qn(X, 1) for _, X in tl]
    tot = sum((w * v for (w, _), v in zip(tl, vals)), Fr(0))
    good2 = (legs2['out@1'] == 2 and legs2['in@2'] == 2 and q == tot and all(v >= 0 for v in vals)
             and all(op_rank(X, 1, 4) <= 2 for _, X in tl) and pres and q >= 0)
    out['two_distinct_sites'] = dict(legs=legs2, q=fs(q), iterated_sum=fs(tot), n_terms=len(tl),
                                      min_q1_term=fs(min(vals)), legs_preserved_after_contraction=pres, ok=good2)
    # (iii) all three sites, any rank (out@1, in@2, out@3)
    E1, Ep1, P1 = leg(mk())
    E2, Ep2, P2 = leg(mk())
    E3, Ep3, P3 = leg(mk())
    C = right_site(left_site(P3, left_site(P1, rop(rng, 3, 4, 2), 0), 2), P2, 1)
    rk = op_rank(C, 3, 4)
    q = qn(C, 3)
    tl, m = iterate(C, 3, [(0, E1, Ep1, 'out'), (0, E2, Ep2, 'in'), (0, E3, Ep3, 'out')])
    tot = sum((w * qn(X, 0) for w, X in tl), Fr(0))
    good3 = rk > 2 and q == tot and q >= 0
    out['all_three_sites_any_rank'] = dict(rank=rk, q=fs(q), iterated_sum=fs(tot), n_terms=len(tl), ok=good3)
    # (iv) same-site input+output legs at site 1: NOT covered by Cor. 3 -- product witness shows class <=> T_2
    u, v = [rq(rng) for _ in range(4)], [rq(rng) for _ in range(4)]
    uv = op1(outer(u, v))
    Cp = rrank2(rng, 2, 4)
    C = tensor(uv, 1, Cp, 2)
    q1uv = qn(uv, 1)
    good4 = qn(C, 3) == q1uv * qn(Cp, 2) and q1uv > 0
    E1, Ep1, P1 = leg(mk())
    Cg = left_site(P1, right_site(rrank2(rng, 3, 4), P1, 0), 0)
    lg = all_legs(Cg, 3, 4)
    tl = terms(Cg, 0, E1, Ep1, 'out')
    contr_legs = [all_legs(X, 2, 4) for _, X in tl if X]
    generic = sum(1 for L in contr_legs if all(val >= 3 for val in L.values()))
    out['same_site_two_legs'] = dict(product_identity=good4, q1_uv=fs(q1uv), general_witness_legs=lg,
                                     contractions_with_all_legs_ge3=generic, n_contractions=len(contr_legs),
                                     note='positivity on this class implies T_2 (q1(|u><v|)>0) and its '
                                          'contractions are generic Z_2-type rank-2 operators')
    good4 = good4 and lg['out@1'] == 2 and lg['in@1'] == 2 and generic > 0
    out['same_site_two_legs']['ok'] = good4
    # (v) n=2 one-leg -> q1 terms >= 0 (T_2 <=> Z_2 direction)
    E1, Ep1, P1 = leg(mk())
    C = left_site(P1, rrank2(rng, 2, 4), 1)
    tl = terms(C, 1, E1, Ep1, 'out')
    vals = [qn(X, 1) for _, X in tl]
    tot = sum((w * val for (w, _), val in zip(tl, vals)), Fr(0))
    good5 = qn(C, 2) == tot and all(val >= 0 for val in vals)
    out['n2_one_leg_to_T1'] = dict(q=fs(qn(C, 2)), sum=fs(tot), min_term=fs(min(vals)), ok=good5)
    # (vi) generic rank-2 operator lies in the zero-leg class
    Cgen = rrank2(rng, 3, 4)
    lgen = all_legs(Cgen, 3, 4)
    good6 = all(val == 4 for val in lgen.values())
    out['generic_rank2_in_Z3'] = dict(legs=lgen, ok=good6)
    okall = good1 and good2 and good3 and good4 and good5 and good6
    pos('ladder_witnesses_exact', okall, detail=out)
    # negatives: 3-dim legs at all sites, any rank; rank 3 with two 2-supported legs
    e = lambda j: [ONE if t == j else ZERO for t in range(4)]
    P3m = op1(madd((1, outer(e(0), e(0))), (1, outer(e(1), e(1))), (1, outer(e(2), e(2)))))
    P2m = op1(madd((1, outer(e(0), e(0))), (1, outer(e(1), e(1)))))
    C3 = tensor(tensor(P3m, 1, P3m, 1), 2, P3m, 1)
    C2 = tensor(tensor(P2m, 1, P2m, 1), 2, P2m, 1)
    q3, q2 = qn(C3, 3), qn(C2, 3)
    pos('all_sites_2dim_any_rank_boundary', q2 == 0, q_P2_tensor3=fs(q2))
    neg('all_sites_3dim_legs_any_rank_fails', q3 < 0, q_P3_tensor3=fs(q3), expected='-27/8')
    E00 = op1(outer(e(0), e(0)))
    C = tensor(tensor(E00, 1, E00, 1), 2, P3m, 1)
    qr3 = qn(C, 3)
    neg('cor3_rank_hypothesis_needed_rank3_fails', qr3 < 0 and op_rank(C, 3, 4) == 3, q=fs(qr3), expected='-3/8')
    # T_1 and rank-3 negative
    rows = []
    okT1 = True
    for _ in range(5):
        X = rrank2(rng, 1, 4)
        q = qn(X, 1)
        okT1 = okT1 and q >= 0
        rows.append(fs(q))
    pos('T1_rank2_exact_instances', okT1, values=rows)
    neg('T1_fails_at_rank3', qn(P3m, 1) < 0, q=fs(qn(P3m, 1)))
    # (b)=>(c): T_3 => T_2 via C' (x) |u><u|
    Cp = rrank2(rng, 2, 4)
    u = rvec(rng, 1, 4)
    uu = ketbra(u, u)
    nu = sum((val.abs2() for val in u.values()), Fr(0))
    Cprod = tensor(Cp, 2, uu, 1)
    pos('T3_implies_T2_product_witness',
        qn(Cprod, 3) == qn(Cp, 2) * nu * nu / 2 and op_rank(Cprod, 3, 4) == op_rank(Cp, 2, 4),
        q3=fs(qn(Cprod, 3)), q2=fs(qn(Cp, 2)), norm_u_4_over_2=fs(nu * nu / 2))


def left_site_vec(M, a, i):
    """(M)_i applied to a vector given as dict x->Q."""
    R = {}
    d = len(M)
    for x, v in a.items():
        l = x[i]
        for k in range(d):
            m = M[k][l]
            if m.iz():
                continue
            key = x[:i] + (k,) + x[i + 1:]
            w = m * v
            R[key] = R[key] + w if key in R else w
    return clean(R)


def sec_rank1(R):
    rng = random.Random(16811)
    rows, ok = [], True
    for n in (1, 2, 2, 3):
        a, b = rvec(rng, n, 4), rvec(rng, n, 4)
        q = qn(ketbra(a, b), n)
        w = {}
        for x, va in a.items():
            for z, vb in b.items():
                val = va * vb      # |a> (x) |b>  (no conjugation)
                if not val.iz():
                    w[(x, z)] = val

        def swap(wd, i):
            return {(x[:i] + (z[i],) + x[i + 1:], z[:i] + (x[i],) + z[i + 1:]): v for (x, z), v in wd.items()}
        tot = Fr(0)
        for Rs in subsets(n):
            v = w
            for i in range(n):
                v = op_lin((Fr(1, 2), v), (Fr(-1 if i in Rs else 1, 2), swap(v, i)))
            tot += Fr(1, 2) ** (n - len(Rs)) * Fr(3, 2) ** len(Rs) * hs2(v)
        na = sum((v.abs2() for v in a.values()), Fr(0))
        nb = sum((v.abs2() for v in b.values()), Fr(0))
        good = q == tot and q >= Fr(1, 2 ** n) * na * nb
        ok = ok and good
        rows.append(dict(n=n, q=fs(q), swap_decomposition=fs(tot), lower_bound=fs(Fr(1, 2 ** n) * na * nb), ok=good))
    pos('rank1_positivity_exact_q_ge_2^-n', ok, cases=rows,
        note='q_n(|a><b|) = <a(x)b| (x)_i (I - F_i/2) |a(x)b> >= 2^-n ||a||^2 ||b||^2 (reviewer proof)')
    # intended-reason negative: the conjugated vector a (x) conj(b) does NOT reproduce q
    a, b = rvec(rng, 2, 4), rvec(rng, 2, 4)
    q = qn(ketbra(a, b), 2)
    w = {(x, z): va * vb.conj() for x, va in a.items() for z, vb in b.items() if not (va * vb.conj()).iz()}
    alt = hs2(w)
    for S in subsets(2)[1:]:
        v = w
        for i in S:
            v = {(x[:i] + (z[i],) + x[i + 1:], z[:i] + (x[i],) + z[i + 1:]): val for (x, z), val in v.items()}
        alt += HN ** len(S) * hsip(w, v).r
    neg('rank1_identity_needs_b_not_conj_b', alt != q, q=fs(q), conj_variant=fs(alt))


def kappa_def_vec(Fm, basis):
    Y = np.stack([(X @ Fm).reshape(-1) for X in basis], axis=1)
    H = Y @ Y.conj().T
    ev, V = np.linalg.eigh(H)
    c = Y.conj().T @ V[:, -1]
    c = c / np.linalg.norm(c)
    X = sum(ci * Xi for ci, Xi in zip(c, basis))
    return float(ev[-1]), X


def sec_maxcorr_and_converse_numeric(R):
    """(a) all-variable maximally-correlated families: reductions = sum_j w_j|j..j><j..j|,
    s(F) = n*max(w)/4 (+1/32 for n=3), min q >= 1-2s.  (b) Theorem 2 converse chain at a
    maximiser X of kappa(F): <X, X P_F> = ||X P_F||^2 = kappa and q(XP_F)/||XP_F||^2 <= 1-2kappa."""
    nrng = np.random.default_rng(16812)
    rows, ok = [], True
    for n in (2, 3):
        basis = wodd_basis(n)
        Dn = 4 ** n
        for t in range(4):
            raw = nrng.normal(size=(4, 2)) + 1j * nrng.normal(size=(4, 2))
            if t == 3:
                raw[:, 0] += 3 * np.array([1, 1, 0, 0])
                raw[:, 1] += 3 * np.array([0, 0, 1, 1])
            Qm, _ = np.linalg.qr(raw)
            alpha = Qm.T
            Fm = np.zeros((Dn, 2), complex)
            for r in range(2):
                for j in range(4):
                    Fm[idx((j,) * n, 4), r] = alpha[r, j]
            w = np.sum(np.abs(alpha) ** 2, axis=0)
            P = Fm @ Fm.conj().T
            red_ok = True
            for T in subsets(n):
                if len(T) != 1:
                    continue
                Rd = np_ptrace(P, n, T)
                Ex = np.zeros_like(Rd)
                for j in range(4):
                    Ex[idx((j,) * (n - 1), 4), idx((j,) * (n - 1), 4)] = w[j]
                red_ok = red_ok and float(np.max(np.abs(Rd - Ex))) < 1e-12
            s = spread(Fm, n)
            s_formula = n * float(w.max()) / 4 + (2 / 64 if n == 3 else 0.0)
            kd = kappa_def(Fm, basis)
            lmin = float(np.linalg.eigvalsh(q_gram(Fm, n))[0])
            good = (red_ok and abs(s - s_formula) < 1e-12 and kd <= s + TOL and lmin >= 1 - 2 * s - TOL
                    and abs((1 - lmin) / 2 - kd) < TOL and float(w.max()) <= 1 + 1e-12)
            ok = ok and good
            rows.append(dict(n=n, w=[float(v) for v in w], reductions_match=red_ok, spread=s,
                             spread_formula=s_formula, kappa=kd, min_q=lmin, bound_1_minus_2s=1 - 2 * s,
                             ok=good))
    pos('maxcorr_families_numeric_all_variable', ok, cases=rows)
    rows, ok = [], True
    for n in (2, 3):
        basis = wodd_basis(n)
        for t in range(2):
            Fm = rand_F(nrng, n)
            k, X = kappa_def_vec(Fm, basis)
            C = X @ Fm @ Fm.conj().T
            ip = complex(np.vdot(X, C))
            nC2 = float(np.vdot(C, C).real)
            qC = np_q(C, n) / nC2
            good = abs(ip.real - k) < TOL and abs(ip.imag) < TOL and abs(nC2 - k) < TOL and qC <= 1 - 2 * k + TOL
            ok = ok and good
            rows.append(dict(n=n, kappa=k, overlap=ip.real, normC2=nC2, q_over_norm2=qC, bound=1 - 2 * k, ok=good))
    pos('theorem2_converse_chain_numeric', ok, cases=rows)


def main():
    dry = '--dry' in sys.argv
    if not dry and os.path.exists(RESULTS):
        sys.exit('results file exists; refusing to overwrite')
    R = {'schema': 'f168rv-controls-v1', 'reviewer': 'ReviewF168WernerV2',
         'wave': 'f168-werner-stratified-source-independent-v2', 'clock_start': clock(),
         'script_sha256': hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
         'env': {'python': sys.version, 'numpy': np.__version__, 'mpmath': mp.__version__,
                 'platform': platform.platform()}}
    sec_inputs(R)
    sec_identity1(R)
    sec_dims(R)
    sec_theorem1(R)
    sec_theorem23(R)
    sec_maxcorr_and_converse_numeric(R)
    sec_certificates(R)
    sec_lemma4(R)
    sec_lemma5(R)
    sec_ladder(R)
    sec_rank1(R)
    R['positive_checks'] = POS
    R['negative_controls'] = NEG
    R['all_positive_pass'] = all(v['pass'] for v in POS.values())
    R['all_negatives_failed_as_intended'] = all(v['failed_as_intended'] for v in NEG.values())
    R['clock_end'] = clock()
    print('ALL_POSITIVE_PASS', R['all_positive_pass'], 'ALL_NEGATIVES_FAILED_AS_INTENDED',
          R['all_negatives_failed_as_intended'], 'n_pos', len(POS), 'n_neg', len(NEG))
    if not dry:
        with open(RESULTS, 'x', encoding='utf-8') as f:
            json.dump(R, f, indent=1, sort_keys=True, default=str)
            f.write('\n')
        print('wrote', RESULTS)
    else:
        print(json.dumps(R, indent=1, sort_keys=True, default=str))


if __name__ == '__main__':
    main()
