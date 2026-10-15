"""Exact Hirota multi-soliton tests for bilinear equations and two-function bilinear systems.

Conventions
-----------
Coordinates z = (x, y, t).  A bilinear polynomial B(D_x, D_y, D_t) is stored as a dict
{(a, b, c): coeff} meaning sum coeff * D_x^a D_y^b D_t^c.  The only analytic fact used is

    B(D) exp(p.z) . exp(q.z) = B(p - q) exp((p + q).z),

so for F = sum_S F_S exp(eta_S), G = sum_S G_S exp(eta_S) with eta_S = sum_{i in S} eta_i,
eta_i = kappa_i . z + const, the coefficient of exp(sum_i n_i eta_i), n in {0,1,2}^N, in B(D)F.G is

    C_B(n) = sum_{mu + nu = n} F_mu G_nu B(kappa_mu - kappa_nu).

All arithmetic is generic: it works for fractions.Fraction (exact rational witnesses) and for
elements of a sympy rational-function field (symbolic identities).  No floating point is used.

Two constructions are provided.

* two_function_solution: the N-soliton ansatz of a two-function system B_1 F.G = B_2 F.G = 0
  with free one-soliton amplitudes (a_i, b_i).  For every subset S with |S| >= 2 the two
  equations C_{B_1}(1_S) = C_{B_2}(1_S) = 0 are linear in the unknowns (F_S, G_S) with matrix
  [[B_1(k_S), B_1(-k_S)], [B_2(k_S), B_2(-k_S)]]; they are solved exactly.  The ansatz is a
  solution iff every remaining coefficient C_{B_j}(n) (n with some entry 2) vanishes.

* hirota_product_solution: the classical single-function ansatz
  f = sum_S prod_{i in S} e^{eta_i} prod_{i<j in S} A_ij,  A_ij = -B(k_i - k_j)/B(k_i + k_j),
  for B(D) f.f = 0 (B even).  It solves the equation iff all coefficients C_B(n) vanish
  (for N = 3 this is Hirota's three-soliton condition).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import sympy as sp

DX, DY, DT = sp.symbols("Dx Dy Dt")


# ---------------------------------------------------------------- bilinear polynomials
def bpoly(expr) -> dict:
    """sympy expression in Dx, Dy, Dt (rational coefficients) -> {(a,b,c): Fraction}."""
    poly = sp.Poly(sp.expand(sp.sympify(expr)), DX, DY, DT)
    out = {}
    for (a, b, c), co in poly.terms():
        co = sp.Rational(co)
        out[(a, b, c)] = Fraction(int(co.p), int(co.q))
    return out


def bmul(P: dict, Q: dict) -> dict:
    out: dict = {}
    for (a1, b1, c1), x1 in P.items():
        for (a2, b2, c2), x2 in Q.items():
            key = (a1 + a2, b1 + b2, c1 + c2)
            out[key] = out.get(key, 0) + x1 * x2
    return {k: v for k, v in out.items() if v != 0}


def beval(B: dict, v):
    """Evaluate B at the vector v = (kx, ky, kt) (field elements)."""
    s = 0
    for (a, b, c), co in B.items():
        term = co
        if a:
            term = term * v[0] ** a
        if b:
            term = term * v[1] ** b
        if c:
            term = term * v[2] ** c
        s = s + term
    return s


def parity(B: dict) -> str:
    degs = {sum(k) % 2 for k in B}
    if degs == {0}:
        return "even"
    if degs == {1}:
        return "odd"
    return "mixed"


# ---------------------------------------------------------------- subset helpers
def _vec_sub(u, v):
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def _kappa_table(waves):
    """kappa_S for every bitmask S."""
    N = len(waves)
    zero = waves[0][0] * 0
    tab = [(zero, zero, zero)] * (1 << N)
    for S in range(1, 1 << N):
        low = S & (-S)
        i = low.bit_length() - 1
        prev = tab[S ^ low]
        w = waves[i]
        tab[S] = (prev[0] + w[0], prev[1] + w[1], prev[2] + w[2])
    return tab


def _submasks(S):
    """All submasks T of S (including 0 and S)."""
    T = S
    while True:
        yield T
        if T == 0:
            return
        T = (T - 1) & S


class DegenerateSystem(Exception):
    pass


def _sym(B, kap, A, C):
    """Value of the bilinear symbol B on kappa_A - kappa_C.

    B is either a polynomial dict (evaluated on the difference vector) or a callable B(A, C) taking the
    two bitmasks; the callable form is used for non-polynomial multipliers and for abstract symbols.
    """
    if callable(B):
        return B(A, C)
    return beval(B, _vec_sub(kap[A], kap[C]))


# ---------------------------------------------------------------- two-function ansatz
def two_function_solution(Bs, waves, a, b):
    """Return (F, G) coefficient lists indexed by bitmask for the system Bs[0] F.G = Bs[1] F.G = 0.

    waves: list of N wave vectors (k_i, l_i, w_i); a, b: lists of N one-soliton amplitudes.
    The caller is responsible for the one-soliton conditions B_j(k_i) a_i + B_j(-k_i) b_i = 0
    (they are reported by residuals() at n = e_i anyway).
    """
    assert len(Bs) == 2
    N = len(waves)
    kap = _kappa_table(waves)
    one = waves[0][0] ** 0
    F = [None] * (1 << N)
    G = [None] * (1 << N)
    F[0] = one
    G[0] = one
    for i in range(N):
        F[1 << i] = a[i]
        G[1 << i] = b[i]
    order = sorted(range(1, 1 << N), key=lambda m: bin(m).count("1"))
    for S in order:
        if bin(S).count("1") < 2:
            continue
        rhs = []
        for B in Bs:
            r = 0
            for T in _submasks(S):
                if T == 0 or T == S:
                    continue
                U = S ^ T
                r = r + F[T] * G[U] * _sym(B, kap, T, U)
            rhs.append(r)
        m11, m12 = _sym(Bs[0], kap, S, 0), _sym(Bs[0], kap, 0, S)
        m21, m22 = _sym(Bs[1], kap, S, 0), _sym(Bs[1], kap, 0, S)
        det = m11 * m22 - m12 * m21
        if det == 0:
            raise DegenerateSystem(f"singular 2x2 system at subset mask {S:b}")
        # solve [[m11, m12], [m21, m22]] [F_S, G_S]^T = -[rhs0, rhs1]^T
        F[S] = (-rhs[0] * m22 + rhs[1] * m12) / det
        G[S] = (-rhs[1] * m11 + rhs[0] * m21) / det
    return F, G


def coefficient(B, kap, F, G, n):
    """C_B(n) for n in {0,1,2}^N given as a tuple."""
    S2 = 0
    S1 = 0
    for i, ni in enumerate(n):
        if ni == 2:
            S2 |= 1 << i
        elif ni == 1:
            S1 |= 1 << i
    s = 0
    for A in _submasks(S1):
        mu = S2 | A
        nu = S2 | (S1 ^ A)
        s = s + F[mu] * G[nu] * _sym(B, kap, A, S1 ^ A)
    return s


def residuals(Bs, waves, F, G, only_nonzero=True):
    """Map n -> [C_{B_j}(n)] over all n in {0,1,2}^N."""
    N = len(waves)
    kap = _kappa_table(waves)
    out = {}
    for n in product((0, 1, 2), repeat=N):
        vals = [coefficient(B, kap, F, G, n) for B in Bs]
        if not only_nonzero or any(v != 0 for v in vals):
            out[n] = vals
    return out


# ---------------------------------------------------------------- single-function (Hirota) ansatz
def hirota_product_solution(B, waves, amps=None):
    """f-coefficients (by bitmask) of f = sum_S prod a_i prod A_ij exp(eta_S)."""
    N = len(waves)
    one = waves[0][0] ** 0
    if amps is None:
        amps = [one] * N
    A = {}
    for i in range(N):
        for j in range(i + 1, N):
            ki, kj = waves[i], waves[j]
            num = beval(B, _vec_sub(ki, kj))
            den = beval(B, (ki[0] + kj[0], ki[1] + kj[1], ki[2] + kj[2]))
            if den == 0:
                raise DegenerateSystem(f"B(k_{i}+k_{j}) = 0")
            A[(i, j)] = -num / den
    f = [None] * (1 << N)
    for S in range(1 << N):
        val = one
        idx = [i for i in range(N) if S >> i & 1]
        for i in idx:
            val = val * amps[i]
        for p in range(len(idx)):
            for q in range(p + 1, len(idx)):
                val = val * A[(idx[p], idx[q])]
        f[S] = val
    return f, A


# ---------------------------------------------------------------- rational helpers
def Q(x) -> Fraction:
    return Fraction(x)


def dispersion_D_t_plus(pcoeffs, k):
    """w for P = D_t + sum_j c_j D_x^j, i.e. w = -sum c_j k^j (exact)."""
    return -sum(Fraction(c) * k ** j for j, c in pcoeffs.items())
