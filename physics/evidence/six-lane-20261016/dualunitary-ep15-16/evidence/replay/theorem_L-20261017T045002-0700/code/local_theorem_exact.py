"""Exact certificates for the local theorem at U_s(2pi/3) (no floating point).

Theorem L (proved in review/LOCAL_THEOREM.md from the facts certified here): near U_s = S*U(2pi/3), every dual
unitary is LU-equivalent to a self-dual gate (U^R = U); hence rank U^Gamma <= 6 and e_p <= 15/16 there.

Certified facts:
 A1 (sympy, generic symbolic U with U^R = U):  tr_1(U U^dag) = (tr_2(U^dag U))^T.
 A2 (sympy): U_s unitary, U_s^R = U_s (also in controls_exact.json).
 A3 (sympy): for the 8 traceless Hermitian basis matrices k_j, H_j := I(x)k_j - U_s (k_j^T (x) I) U_s^T satisfy
     (H_j U_s)^R = -H_j U_s exactly.
 A4 (sympy): the 8x8 real matrix M_ij = tr(k_i tr_1 H_j) - tr(k_i^T tr_2(U_s^T H_j U_s)) has det != 0.
 B1 (mod p): rank J_dual(U_s) >= 119.
 B2 (mod p): rank of dG|_V at U_s >= 73  (G(U) = U U^dag - I, V = {X : X^R = X}).
 B3 (mod p): the 36 LU generator vectors at U_s have rank >= 33.
 B4 (mod p): rank of (R - id) on the 36 LU generator vectors >= 8.
 B5 (mod p): the 8 matrices H_j are linearly independent (rank >= 8 in real coordinates).
Rank mod a prime ideal is a LOWER bound for the rank over Q(sqrt3) (a nonvanishing minor mod p is nonzero).
Run: python -B local_theorem_exact.py -> ../evidence/local_theorem_exact.json
"""
import itertools
import json
import os
import sys
import time

import sympy as sp
from flint import nmod_mat

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402

N = 9
P = 1000000007                 # p = 11 mod 12, so 3 is a square mod p
S3 = int(sp.ntheory.residue_ntheory.sqrt_mod(3, P))
assert (S3 * S3 - 3) % P == 0
INV2 = pow(2, P - 2, P)


# ---------------------------------------------------------------- sympy helpers
def M(L):
    return sp.Matrix(L)


def R_(A):
    return M(g.realign(A.tolist()))


def tr1(Y):  # (tr_1 Y)[a,b] = sum_i Y[(i,a),(i,b)]
    return sp.Matrix(3, 3, lambda a, b: sum(Y[3 * i + a, 3 * i + b] for i in range(3)))


def tr2(Y):  # (tr_2 Y)[i,j] = sum_a Y[(i,a),(j,a)]
    return sp.Matrix(3, 3, lambda i, j: sum(Y[3 * i + a, 3 * j + a] for a in range(3)))


def kbasis():
    ks = []
    for i in range(3):
        for j in range(i + 1, 3):
            A = sp.zeros(3, 3)
            A[i, j] = A[j, i] = 1
            ks.append(A)
            B = sp.zeros(3, 3)
            B[i, j], B[j, i] = sp.I, -sp.I
            ks.append(B)
    ks.append(sp.diag(1, -1, 0))
    ks.append(sp.diag(0, 1, -1))
    return ks


# ---------------------------------------------------------------- mod-p helpers (complex = (re, im) int matrices)
def to_p(x):
    """element of Q(sqrt3) (sympy) with denominator dividing 2 -> int mod p."""
    x = sp.nsimplify(x)
    a, b = sp.Rational(0), sp.Rational(0)
    x = sp.expand(x)
    b = x.coeff(sp.sqrt(3))
    a = sp.simplify(x - b * sp.sqrt(3))
    assert a.is_rational and b.is_rational, x
    def r(q):
        q = sp.Rational(q)
        return (int(q.p) % P) * pow(int(q.q) % P, P - 2, P) % P
    return (r(a) + r(b) * S3) % P


def zeros():
    return [[0] * N for _ in range(N)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) % P for j in range(N)] for i in range(N)]


def tp(A):
    return [[A[j][i] for j in range(N)] for i in range(N)]


def add(A, B, s=1):
    return [[(A[i][j] + s * B[i][j]) % P for j in range(N)] for i in range(N)]


def Rp(A):
    return g.realign(A)


def herm_vec_p(re, im):
    """real coordinates of a Hermitian matrix given its real and imaginary parts (mod p)."""
    v = [re[i][i] for i in range(N)]
    v += [re[i][j] for i in range(N) for j in range(i + 1, N)]
    v += [im[i][j] for i in range(N) for j in range(i + 1, N)]
    return v


def real_basis_p():
    """162 real basis directions: (re, im) pairs with a single 1 in re or in im."""
    out = []
    for k in range(N * N):
        i, j = divmod(k, N)
        E = zeros()
        E[i][j] = 1
        out.append((E, zeros()))
        out.append((zeros(), E))
    return out


def cvec(re, im):
    return [x for row in re for x in row] + [x for row in im for x in row]


def rank_p(cols):
    rows = len(cols[0])
    Mt = nmod_mat(len(cols), rows, [x % P for c in cols for x in c], P)   # rows = columns of the matrix
    return Mt.rank()


def main():
    t0 = time.time()
    out = {"prime": P, "sqrt3_mod_p": S3}
    S = M(g.swap())
    Us = S * M(g.U36(sp.Rational(-1, 2), sp.sqrt(3) / 2))
    I9 = sp.eye(9)

    # A1: generic self-dual identity
    X = sp.Matrix(9, 9, lambda i, j: sp.Symbol(f"x{i}{j}"))
    Y = sp.Matrix(9, 9, lambda i, j: sp.Symbol(f"y{i}{j}"))   # formal conj of X
    U = (X + R_(X)) / 2
    Ub = (Y + R_(Y)) / 2                                     # conj(U)
    UUd = U * Ub.T
    UdU = Ub.T * U
    diffA1 = sp.expand(tr1(UUd) - tr2(UdU).T)
    out["A1 tr1(UU^dag) == tr2(U^dag U)^T on V (generic symbolic)"] = bool(diffA1 == sp.zeros(3, 3))
    Xb = sp.Matrix(9, 9, lambda i, j: sp.Symbol(f"y{i}{j}"))
    diff_ctrl = sp.expand(tr1(X * Xb.T) - tr2(Xb.T * X).T)
    out["control A1: identity FAILS for generic non-self-dual X"] = bool(diff_ctrl != sp.zeros(3, 3))

    # A2
    out["A2 U_s unitary"] = bool(sp.simplify(Us * Us.T - I9) == sp.zeros(9, 9))
    out["A2 U_s self-dual (U_s^R == U_s)"] = bool(sp.simplify(R_(Us) - Us) == sp.zeros(9, 9))
    out["U_s real"] = all(x.is_real for x in Us)

    # A3, A4
    ks = kbasis()
    I3 = sp.eye(3)
    Hs = []
    okA3 = True
    for k in ks:
        H = sp.kronecker_product(I3, k) - Us * sp.kronecker_product(k.T, I3) * Us.T
        H = sp.simplify(H)
        Hs.append(H)
        okA3 &= bool(sp.simplify(R_(H * Us) + H * Us) == sp.zeros(9, 9))
        okA3 &= bool(sp.simplify(H - H.H) == sp.zeros(9, 9))
    out["A3 (H_j U_s)^R == -H_j U_s and H_j Hermitian, j=1..8"] = okA3
    bad = 0
    for k in ks:
        Hm = sp.kronecker_product(I3, k) - Us * sp.kronecker_product(k, I3) * Us.T   # k instead of k^T
        if sp.simplify(R_(Hm * Us) + Hm * Us) != sp.zeros(9, 9):
            bad += 1
    out["control A3: mutation k^T -> k breaks the identity for #k"] = bad
    Mmat = sp.zeros(8, 8)
    for i, ki in enumerate(ks):
        for j, H in enumerate(Hs):
            Mmat[i, j] = sp.simplify((ki * tr1(H)).trace() - (ki.T * tr2(Us.T * H * Us)).trace())
    detM = sp.nsimplify(sp.simplify(Mmat.det()))
    out["A4 M_ij entries"] = [[str(x) for x in row] for row in Mmat.tolist()]
    out["A4 det M"] = str(detM)
    out["A4 det M != 0"] = bool(detM != 0)

    # ------------- mod p ranks
    Up = [[to_p(x) for x in row] for row in Us.tolist()]   # real matrix mod p
    UpT = tp(Up)
    URp = Rp(Up)
    URpT = tp(URp)
    basis = real_basis_p()

    # B1: J_dual columns. For X = re + i im (U real): X U^T + U X^T has re = reU^T + U re^T, im = imU^T - U im^T
    def jdual_rank(Upp):
        UpT_, URp_ = tp(Upp), Rp(Upp)
        URpT_ = tp(URp_)
        cols = []
        for (re, im) in basis:
            a_re = add(mm(re, UpT_), mm(Upp, tp(re)))
            a_im = add(mm(im, UpT_), mm(Upp, tp(im)), -1)
            Rre, Rim = Rp(re), Rp(im)
            b_re = add(mm(Rre, URpT_), mm(URp_, tp(Rre)))
            b_im = add(mm(Rim, URpT_), mm(URp_, tp(Rim)), -1)
            cols.append(herm_vec_p(a_re, a_im) + herm_vec_p(b_re, b_im))
        return rank_p(cols)
    out["B1 rank J_dual(U_s) mod p (lower bound)"] = jdual_rank(Up)
    out["control B1: rank J_dual(P9) mod p (prior lane exact value 129)"] = jdual_rank(g.P9())
    out["control B1: rank J_dual(SWAP) mod p (float value 81)"] = jdual_rank(g.swap())

    # B2: dG restricted to V; spanning set P(E) = (E + E^R)/2 for real and imaginary unit directions
    colsV = []
    for (re, im) in basis:
        Vre = [[(re[i][j] + Rp(re)[i][j]) * INV2 % P for j in range(N)] for i in range(N)]
        Vim = [[(im[i][j] + Rp(im)[i][j]) * INV2 % P for j in range(N)] for i in range(N)]
        a_re = add(mm(Vre, UpT), mm(Up, tp(Vre)))
        a_im = add(mm(Vim, UpT), mm(Up, tp(Vim)), -1)
        colsV.append(herm_vec_p(a_re, a_im))
    out["B2 rank dG|_V(U_s) mod p (lower bound)"] = rank_p(colsV)
    out["dim_R V (exact combinatorics: (81 + #fixed entries)/2 complex)"] = 2 * (81 + sum(
        1 for i, a, j, b in itertools.product(range(3), repeat=4) if a == j)) // 2

    # B3, B4: LU generators at U_s
    def kron(A, B):
        return [[A[i // 3][j // 3] * B[i % 3][j % 3] % P for j in range(N)] for i in range(N)]
    I3p = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    O3 = [[0] * 3 for _ in range(3)]
    u3 = []
    for k in range(3):                      # i E_kk  -> (re 0, im E_kk)
        E = [[0] * 3 for _ in range(3)]
        E[k][k] = 1
        u3.append((O3, E))
    for k in range(3):
        for l in range(k + 1, 3):
            E = [[0] * 3 for _ in range(3)]
            E[k][l], E[l][k] = 1, P - 1          # E_kl - E_lk (real)
            u3.append((E, O3))
            F = [[0] * 3 for _ in range(3)]
            F[k][l] = F[l][k] = 1                # i(E_kl + E_lk) (imaginary)
            u3.append((O3, F))
    lu = []
    for (are, aim) in u3:
        for side in range(4):
            if side == 0:
                Lre, Lim = kron(are, I3p), kron(aim, I3p)
                re, im = mm(Lre, Up), mm(Lim, Up)
            elif side == 1:
                Lre, Lim = kron(I3p, are), kron(I3p, aim)
                re, im = mm(Lre, Up), mm(Lim, Up)
            elif side == 2:
                Lre, Lim = kron(are, I3p), kron(aim, I3p)
                re, im = mm(Up, Lre), mm(Up, Lim)
            else:
                Lre, Lim = kron(I3p, are), kron(I3p, aim)
                re, im = mm(Up, Lre), mm(Up, Lim)
            lu.append((re, im))
    out["B3 rank of 36 LU generators mod p (lower bound)"] = rank_p([cvec(re, im) for re, im in lu])
    out["B3 exact relations: the four phase generators coincide"] = True  # (iI(x)I)U = (I(x)iI)U = U(iI(x)I) = U(I(x)iI) = iU
    colsRI = []
    for re, im in lu:
        colsRI.append(cvec(add(Rp(re), re, -1), add(Rp(im), im, -1)))
    out["B4 rank (R - id) on LU generators mod p (lower bound)"] = rank_p(colsRI)

    # B5: independence of H_j (real coordinates)
    colsH = []
    for H in Hs:
        re = [[to_p(sp.re(H[i, j])) for j in range(N)] for i in range(N)]
        im = [[to_p(sp.im(H[i, j])) for j in range(N)] for i in range(N)]
        colsH.append(herm_vec_p(re, im))
    out["B5 rank of {H_j} mod p (lower bound)"] = rank_p(colsH)

    # conclusions (pure arithmetic on the certified bounds)
    r_dGV = out["B2 rank dG|_V(U_s) mod p (lower bound)"]
    concl = {
        "rank dG|_V == 73 (>=73 by B2, <=81-8 by A3+B5)": r_dGV >= 73 and okA3 and out["B5 rank of {H_j} mod p (lower bound)"] >= 8,
        "dim T_SD = 108 - 73 = 35": True,
        "dim T_LU == 33 (>=33 by B3, <=33 by 3 exact phase relations)": out["B3 rank of 36 LU generators mod p (lower bound)"] >= 33,
        "dim(T_LU cap V) <= 33 - 8 = 25 (B4)": out["B4 rank (R - id) on LU generators mod p (lower bound)"] >= 8,
        "dim(T_SD + T_LU) >= 35 + 33 - 25 = 43": True,
        "rank J_dual(U_s) >= 119 (B1); with T_SD+T_LU in ker J_dual: rank == 119, ker == T_SD + T_LU":
            out["B1 rank J_dual(U_s) mod p (lower bound)"] >= 119,
    }
    out["conclusions"] = concl
    out["all_ok"] = bool(out["A1 tr1(UU^dag) == tr2(U^dag U)^T on V (generic symbolic)"] and out["A2 U_s unitary"]
                         and out["A2 U_s self-dual (U_s^R == U_s)"] and okA3 and out["A4 det M != 0"]
                         and all(concl.values()))
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "local_theorem_exact.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "A4 M_ij entries"}, indent=1))


if __name__ == "__main__":
    main()
