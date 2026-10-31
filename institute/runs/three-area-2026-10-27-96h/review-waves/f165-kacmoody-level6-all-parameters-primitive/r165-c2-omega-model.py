#!/usr/bin/env python3
# r165 reviewer-authored model (independent; no author code imported or executed).
# Free-Levi model of the positive part of A(r,s)=[[2,-1,-1],[-1,2,-1],[-r,-s,2]]:
#   level-one module M = sl3-adjoint with basis u0..u7 = v,Xv,Yv,Zv,XYv,ZXv,ZYv,Z^2v
#   (matrix images E31,-E32,E21,E11-E33,E11-E22,-E12,-E23,-2E13 as written in the descent file),
#   M^- basis w_j = -theta(u_j), bracket [w_j,u_k] in g0 = sl3 + C*c3 derived here by
#   sl3-equivariance from [f3,e3] = -h3 (c3 = centraliser component of h3, acting by n(2-r-s) on level n).
# Positive part = free Lie algebra L(M) realised inside the tensor algebra T(M) (words = base-8 codes).
# The action of w in M^- on L(M) is the induced-module recursion
#   F_w(y1...yn) = sum_k y1..y_{k-1} ( [w,y_k] |> y_{k+1}..y_n ),   ( |> = derivation action of g0 ).
# Everything is exact integer/Fraction arithmetic; float64 BLAS is used only for integer
# products whose exactness is asserted by an explicit 2^53 bound.
import sys
sys.dont_write_bytecode = True
import subprocess
from fractions import Fraction as Fr
import numpy as np

def clock():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()

# ---------------- finite sl3 data ----------------
def Z3():
    return [[Fr(0)] * 3 for _ in range(3)]

def Em(i, j):
    m = Z3(); m[i - 1][j - 1] = Fr(1); return m

def lin(*pairs):
    R = Z3()
    for c, M in pairs:
        for i in range(3):
            for j in range(3):
                R[i][j] += Fr(c) * M[i][j]
    return R

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def comm(A, B):
    return lin((1, mul(A, B)), (-1, mul(B, A)))

def tr(A):
    return A[0][0] + A[1][1] + A[2][2]

def tp(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]

BM = [Em(3, 1), lin((-1, Em(3, 2))), Em(2, 1), lin((1, Em(1, 1)), (-1, Em(3, 3))),
      lin((1, Em(1, 1)), (-1, Em(2, 2))), lin((-1, Em(1, 2))), lin((-1, Em(2, 3))), lin((-2, Em(1, 3)))]
E1, E2, F1, F2 = Em(1, 2), Em(2, 3), Em(2, 1), Em(3, 2)
H1 = lin((1, Em(1, 1)), (-1, Em(2, 2)))
H2 = lin((1, Em(2, 2)), (-1, Em(3, 3)))
LET = [(0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2)]

def coords(X):
    if tr(X) != 0:
        raise ValueError('not traceless')
    c = [X[2][0], -X[2][1], X[1][0], -X[2][2], -X[1][1], -X[0][1], -X[1][2], -X[0][2] / 2]
    if lin(*[(c[k], BM[k]) for k in range(8)]) != X:
        raise ValueError('reconstruction failed')
    return c

def rho(Z):
    cols = [coords(comm(Z, BM[k])) for k in range(8)]
    return [[cols[k][l] for k in range(8)] for l in range(8)]   # rho[l][k]: coeff of u_l in Z.u_k

def inv8(G):
    n = len(G)
    A = [[Fr(G[i][j]) for j in range(n)] + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]

GRAM = [[tr(mul(BM[i], tp(BM[j]))) for j in range(8)] for i in range(8)]
GINV = inv8(GRAM)

def bracket_pencil(j, k):
    """Letter-action matrix of [w_j,u_k] on M as (G0,Gr,Gs): G = G0 + r Gr + s Gs (Fractions)."""
    W, U = tp(BM[j]), BM[k]
    C = comm(W, U)
    S = lin((1, mul(W, U)), (1, mul(U, W)))
    t = tr(mul(W, U))
    rC, rS = rho(C), rho(S)
    G0 = [[(-2 * t if l == m else Fr(0)) for m in range(8)] for l in range(8)]
    Gr = [[(rC[l][m] + rS[l][m]) / 2 + (t if l == m else 0) for m in range(8)] for l in range(8)]
    Gs = [[(rC[l][m] - rS[l][m]) / 2 + (t if l == m else 0) for m in range(8)] for l in range(8)]
    return G0, Gr, Gs

PENCIL = {(j, k): bracket_pencil(j, k) for j in range(8) for k in range(8)}

def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

SIGMA = 1
for (j, k), comps in PENCIL.items():
    for M in comps:
        for row in M:
            for x in row:
                SIGMA = lcm(SIGMA, x.denominator)

def contraction_weights(G_inverse):
    # Omega' = LAMBDA*Omega = sum_ij KW_ij [u_i, F_j^{SIGMA*G}] with integer KW_ij = LAMBDA*Ginv_ij/SIGMA
    lam = 1
    for i in range(8):
        for j in range(8):
            q = Fr(G_inverse[i][j]) / SIGMA
            lam = lcm(lam, q.denominator)
    KW = {}
    for i in range(8):
        for j in range(8):
            q = Fr(G_inverse[i][j]) * lam / SIGMA
            if q != 0:
                assert q.denominator == 1
                KW[(i, j)] = int(q)
    return lam, KW

LAMBDA, KW = contraction_weights(GINV)

def int_sparse_cols(M, scale):
    cols = []
    for k in range(8):
        lst = []
        for l in range(8):
            x = M[l][k] * scale
            if x != 0:
                assert x.denominator == 1
                lst.append((l, int(x)))
        cols.append(lst)
    return cols

# pencil columns scaled by SIGMA: PC[j][k][m] = list of (l, v0, vr, vs) for source letter m
PC = {}
for j in range(8):
    for k in range(8):
        G0, Gr, Gs = PENCIL[(j, k)]
        cols = []
        for m in range(8):
            lst = []
            for l in range(8):
                v = tuple(int(X[l][m] * SIGMA) for X in (G0, Gr, Gs))
                for X in (G0, Gr, Gs):
                    assert (X[l][m] * SIGMA).denominator == 1
                if any(v):
                    lst.append((l,) + v)
            cols.append(lst)
        PC[(j, k)] = cols

RHO_F1 = int_sparse_cols(rho(F1), 1)
RHO_F2 = int_sparse_cols(rho(F2), 1)
RHO_E1 = int_sparse_cols(rho(E1), 2)   # NOTE: e1,e2 have half-integer entries in this basis; stored as 2*e1, 2*e2
RHO_E2 = int_sparse_cols(rho(E2), 2)

# ---------------- words ----------------
def letters(code, n):
    return [(code >> (3 * (n - 1 - i))) & 7 for i in range(n)]

def encode(ls):
    c = 0
    for x in ls:
        c = (c << 3) | x
    return c

def words_of_degree(n, a, b):
    out = []
    def rec(prefix, k, ra, rb):
        if k == n:
            if ra == 0 and rb == 0:
                out.append(encode(prefix))
            return
        left = n - k - 1
        for x, (da, db) in enumerate(LET):
            na, nb = ra - da, rb - db
            if 0 <= na <= 2 * left and 0 <= nb <= 2 * left:
                prefix.append(x); rec(prefix, k + 1, na, nb); prefix.pop()
    rec([], 0, a, b)
    return sorted(out)

def is_lyndon(t):
    return all(t < t[i:] for i in range(1, len(t)))

_EXP = {}
def expand(t):
    """Standard Lyndon bracketing of tuple t as dict code->int (length len(t))."""
    if t in _EXP:
        return _EXP[t]
    if len(t) == 1:
        res = {t[0]: 1}
    else:
        i = min(range(1, len(t)), key=lambda i: t[i:])
        u, v = t[:i], t[i:]
        A, B = expand(u), expand(v)
        lu, lv = len(u), len(v)
        res = {}
        for a, ca in A.items():
            for b, cb in B.items():
                k1 = (a << (3 * lv)) | b
                k2 = (b << (3 * lu)) | a
                res[k1] = res.get(k1, 0) + ca * cb
                res[k2] = res.get(k2, 0) - ca * cb
        res = {k: c for k, c in res.items() if c}
    _EXP[t] = res
    return res

def lyndon_basis(n, a, b):
    ws = words_of_degree(n, a, b)
    lw = [w for w in ws if is_lyndon(tuple(letters(w, n)))]
    return ws, lw

# ---------------- operators on words ----------------
def der_scalar(cols, code, L, coef, out):
    """Derivation action of an integer letter matrix (columns) on a word of length L; accumulate coef*image into out (dict)."""
    for m in range(L):
        sh = 3 * (L - 1 - m)
        c = (code >> sh) & 7
        for (l, v) in cols[c]:
            key = code + ((l - c) << sh)
            out[key] = out.get(key, 0) + coef * v

def F_pencil(j, code, n, out, coef=1):
    """out[code'] += coef * (SIGMA * F_{w_j})(word) as [c0,cr,cs] lists (level n-1)."""
    for k in range(n):
        L = n - 1 - k
        letter = (code >> (3 * L)) & 7
        prefix = code >> (3 * (L + 1))
        suffix = code & ((1 << (3 * L)) - 1)
        cols = PC[(j, letter)]
        base = prefix << (3 * L)
        for m in range(L):
            sh = 3 * (L - 1 - m)
            c = (suffix >> sh) & 7
            for (l, v0, vr, vs) in cols[c]:
                key = base | (suffix + ((l - c) << sh))
                e = out.get(key)
                if e is None:
                    out[key] = [coef * v0, coef * vr, coef * vs]
                else:
                    e[0] += coef * v0; e[1] += coef * vr; e[2] += coef * vs

def F_numeric(j, x, n, r, s):
    """(SIGMA*F_{w_j}) applied to a dict-Lie element x of length n at numeric (r,s)."""
    tmp = {}
    for code, c in x.items():
        F_pencil(j, code, n, tmp, c)
    out = {}
    for k, (a0, ar, as_) in tmp.items():
        v = a0 + r * ar + s * as_
        if v:
            out[k] = v
    return out

def der_dict(cols, x, n):
    out = {}
    for code, c in x.items():
        der_scalar(cols, code, n, c, out)
    return {k: v for k, v in out.items() if v}

def bracket_dict(x, nx, y, ny):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            k1 = (a << (3 * ny)) | b
            k2 = (b << (3 * nx)) | a
            out[k1] = out.get(k1, 0) + ca * cb
            out[k2] = out.get(k2, 0) - ca * cb
    return {k: v for k, v in out.items() if v}

def add_dicts(*pairs):
    out = {}
    for c, x in pairs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + c * v
    return {k: v for k, v in out.items() if v}

def lie_coordinates(x, n, lw_sorted):
    """Exact Lyndon coordinates of dict x (length n); returns (coords dict, residual dict)."""
    rem = dict(x)
    co = {}
    for w in lw_sorted:
        c = rem.get(w, 0)
        if c:
            co[w] = c
            for k, v in expand(tuple(letters(w, n))).items():
                rem[k] = rem.get(k, 0) - c * v
    return co, {k: v for k, v in rem.items() if v}

# ---------------- dense exact matrices for a type ----------------
def build_type(n, a, b, want_omega=True, want_d3=True, alt_weights=None, log=print):
    """Exact integer matrices for the degree (a,b,n) Lie component in Lyndon coordinates.
    Returns dict with T, F1Y, F2Y, R (3 comps), D3 (3 comps), optional R_alt."""
    ws, lw = lyndon_basis(n, a, b)
    widx = {w: i for i, w in enumerate(ws)}
    NL, NW = len(lw), len(ws)
    X = np.zeros((NW, NL), dtype=np.float64)
    for jcol, w in enumerate(lw):
        e = expand(tuple(letters(w, n)))
        assert min(e) == w and e[w] == 1, 'Lyndon triangularity fails'
        for k, v in e.items():
            X[widx[k], jcol] = v
    Lpos = [widx[w] for w in lw]
    T = X[Lpos, :].copy()
    res = {'NW': NW, 'NL': NL, 'lw': lw}
    res['T'] = T.astype(np.int64)
    maxX = float(np.abs(X).max())
    def restricted(target_lw, op):
        tidx = {w: i for i, w in enumerate(target_lw)}
        mats = None
        for col, w in enumerate(ws):
            img = op(w)
            for key, val in img.items():
                row = tidx.get(key)
                if row is None:
                    continue
                if mats is None:
                    ncomp = len(val) if isinstance(val, list) else 1
                    mats = [np.zeros((len(target_lw), NW), dtype=np.float64) for _ in range(ncomp)]
                if isinstance(val, list):
                    for q in range(len(val)):
                        mats[q][row, col] += val[q]
                else:
                    mats[0][row, col] += val
        if mats is None:
            return [np.zeros((len(target_lw), NL), dtype=np.int64) for _ in range(3)]
        out = []
        for Mq in mats:
            bound = float(np.abs(Mq).sum(axis=1).max()) * maxX
            assert bound < 2.0 ** 52, bound
            P = Mq @ X
            Pr = np.rint(P)
            assert np.array_equal(P, Pr)
            out.append(Pr.astype(np.int64))
        return out
    # f1, f2 targets
    _, lw1 = lyndon_basis(n, a - 1, b) if a >= 1 else ([], [])
    _, lw2 = lyndon_basis(n, a, b - 1) if b >= 1 else ([], [])
    def f_op(cols):
        def op(w):
            o = {}
            der_scalar(cols, w, n, 1, o)
            return o
        return op
    res['F1Y'] = restricted(lw1, f_op(RHO_F1))[0] if lw1 else np.zeros((0, NL), dtype=np.int64)
    res['F2Y'] = restricted(lw2, f_op(RHO_F2))[0] if lw2 else np.zeros((0, NL), dtype=np.int64)
    log(f'  built f1/f2 restricted: {res["F1Y"].shape} {res["F2Y"].shape} at {clock()}')
    if want_d3:
        _, lw5 = lyndon_basis(n - 1, a, b)
        def d3_op(w):
            o = {}
            F_pencil(0, w, n, o)
            return o
        res['D3'] = restricted(lw5, d3_op)
        res['NL5'] = len(lw5)
        log(f'  built D3 restricted: {res["D3"][0].shape} at {clock()}')
    def omega_op_factory(weights):
        def op(w):
            Fj = {}
            for j in range(8):
                d = {}
                F_pencil(j, w, n, d)
                Fj[j] = d
            o = {}
            for (i, j), kw in weights.items():
                for y, (c0, cr, cs) in Fj[j].items():
                    k1 = (i << (3 * (n - 1))) | y
                    k2 = (y << 3) | i
                    for key, sg in ((k1, kw), (k2, -kw)):
                        e = o.get(key)
                        if e is None:
                            o[key] = [sg * c0, sg * cr, sg * cs]
                        else:
                            e[0] += sg * c0; e[1] += sg * cr; e[2] += sg * cs
            return o
        return op
    if want_omega:
        res['R'] = restricted(lw, omega_op_factory(KW))
        log(f'  built Omega restricted: {res["R"][0].shape} at {clock()}')
    if alt_weights is not None:
        res['R_alt'] = restricted(lw, omega_op_factory(alt_weights))
        log(f'  built ALT Omega restricted at {clock()}')
    return res

# ---------------- modular linear algebra ----------------
def rref_kernel_mod(A, p):
    """Kernel basis K (ncols x k) of A mod p with K[free,:] = I; returns K, free indices, rank."""
    A = np.array(A % p, dtype=np.int64)
    nr, nc = A.shape
    piv_cols = []
    row = 0
    for col in range(nc):
        if row >= nr:
            break
        nzr = np.nonzero(A[row:, col])[0]
        if nzr.size == 0:
            continue
        pr = row + nzr[0]
        if pr != row:
            A[[row, pr]] = A[[pr, row]]
        inv = pow(int(A[row, col]), p - 2, p)
        A[row] = (A[row] * inv) % p
        colv = A[:, col].copy()
        colv[row] = 0
        nzrows = np.nonzero(colv)[0]
        if nzrows.size:
            A[nzrows, col:] = (A[nzrows, col:] - (colv[nzrows, None] * A[row, col:][None, :]) % p) % p
        piv_cols.append(col)
        row += 1
    rank = len(piv_cols)
    ps = set(piv_cols)
    free = [c for c in range(nc) if c not in ps]
    K = np.zeros((nc, len(free)), dtype=np.int64)
    if free:
        K[free, np.arange(len(free))] = 1
        if rank:
            K[np.array(piv_cols)[:, None], np.arange(len(free))[None, :]] = (-A[:rank][:, free]) % p
    return K, free, rank

def matmul_mod(A, B, p):
    """Exact (A @ B) mod p for int64 matrices with entries in [0,p), p < 2^25, via float64 BLAS."""
    assert p < 2 ** 25
    A = np.asarray(A % p, dtype=np.float64)
    B = np.asarray(B % p, dtype=np.int64)
    n = A.shape[1]
    assert n < 2 ** 14
    Bh = (B >> 13).astype(np.float64)
    Bl = (B & ((1 << 13) - 1)).astype(np.float64)
    Ph = np.rint(A @ Bh).astype(np.int64) % p
    Pl = np.rint(A @ Bl).astype(np.int64) % p
    return ((Ph << 13) % p + Pl) % p

def lower_unit_solve_mod(T, Y, p):
    """Solve T Z = Y mod p for unit lower-triangular integer T (exact)."""
    T = np.asarray(T % p, dtype=np.int64)
    Z = np.array(Y % p, dtype=np.int64)
    n = T.shape[0]
    assert np.all(np.diag(T) == 1) and not np.any(np.triu(T, 1))
    for i in range(n):
        row = T[i, :i]
        nz = np.nonzero(row)[0]
        if nz.size:
            Z[i] = (Z[i] - (row[nz, None] * Z[nz]).sum(axis=0) % p) % p
    return Z

def det_mod(M, p):
    M = np.array(M % p, dtype=np.int64)
    n = M.shape[0]
    det = 1
    for c in range(n):
        nz = np.nonzero(M[c:, c])[0]
        if nz.size == 0:
            return 0
        pr = c + nz[0]
        if pr != c:
            M[[c, pr]] = M[[pr, c]]
            det = -det
        pv = int(M[c, c])
        det = (det * pv) % p
        inv = pow(pv, p - 2, p)
        f = (M[c + 1:, c] * inv) % p
        M[c + 1:, c:] = (M[c + 1:, c:] - (f[:, None] * M[c, c:][None, :]) % p) % p
    return det % p

def rank_mod(M, p):
    _, _, rk = rref_kernel_mod(M, p)
    return rk

def batch_det_mod(M0, Mr, Ms, pts, p):
    """det(M0 + r Mr + s Ms) mod p for a list of (r,s) points, batched elimination."""
    m = M0.shape[0]
    res = []
    B = 256
    for st in range(0, len(pts), B):
        chunk = pts[st:st + B]
        rr = np.array([q[0] % p for q in chunk], dtype=np.int64)[:, None, None]
        ss = np.array([q[1] % p for q in chunk], dtype=np.int64)[:, None, None]
        A = (M0[None] % p + (rr * (Mr[None] % p)) % p + (ss * (Ms[None] % p)) % p) % p
        nb = A.shape[0]
        det = np.ones(nb, dtype=np.int64)
        alive = np.ones(nb, dtype=bool)
        ar = np.arange(nb)
        for c in range(m):
            col = A[:, c:, c]
            nzm = col != 0
            has = nzm.any(axis=1)
            alive &= has
            first = np.argmax(nzm, axis=1)
            swap = (first != 0) & has
            if swap.any():
                bi = ar[swap]
                src = c + first[swap]
                tmp = A[bi, c, :].copy()
                A[bi, c, :] = A[bi, src, :]
                A[bi, src, :] = tmp
                det[bi] = (-det[bi]) % p
            pv = A[:, c, c].copy()
            pv[~has] = 1
            det = (det * pv) % p
            # modular inverse by Fermat, vectorised
            inv = np.ones(nb, dtype=np.int64)
            base = pv % p
            e = p - 2
            while e:
                if e & 1:
                    inv = (inv * base) % p
                base = (base * base) % p
                e >>= 1
            f = (A[:, c + 1:, c] * inv[:, None]) % p
            A[:, c + 1:, c:] = (A[:, c + 1:, c:] - (f[:, :, None] * A[:, c, None, c:]) % p) % p
        det[~alive] = 0
        res.extend(int(x) for x in det)
    return res

def primes_below(limit, count):
    out = []
    x = limit - 1
    while len(out) < count:
        if x % 2 and all(x % d for d in range(3, int(x ** 0.5) + 1, 2)):
            out.append(x)
        x -= 2 if x % 2 else 1
    return out
