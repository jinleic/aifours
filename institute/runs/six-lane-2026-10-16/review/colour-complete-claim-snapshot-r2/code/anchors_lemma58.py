#!/usr/bin/env python3
"""anchors_lemma58.py -- exact non-hypothesis anchors of Sections 5.2 and 2 of

    J. Diaz, A.C. Kaporis, G.D. Kemkes, L.M. Kirousis, X. Perez, N. Wormald,
    "On the chromatic number of a random 5-regular graph", J. Graph Theory 61 (2009) 157-191
    (preprint sources/diaz2009-3col-preprint.pdf; text sources/diaz2009-3col-preprint.layout.txt).

Items (lane random5reg-colour, task prefix "anchors_"):
  1. Lemma 5.7: the 24 equations have rank 23; the 18 pairing equations are exactly the
     constraints (4.3); an explicit parametrisation d_B = L(d_F, 1/6) with integer coefficients.
  2. A Z-basis P (324 x 301) of Lambda = ker(M) cap Z^324 with saturation proofs, plus an
     independent HNF-derived basis of the same lattice.
  3. Hessian of f at b; det(P^T Hf P) exactly over Q, factorised; exact negative definiteness.
  4. g(b) and prod_s w_s.
  5. (2.2)-(2.5), Lemma 5.1's h(n), Lemma 5.9's constant, E(Y^2)/(EY)^2 vs exp(sum lambda_k delta_k^2).

Every claimed equality uses exact integer/rational arithmetic (python-flint, fractions, sympy).
Floating point (numpy, mpmath) appears only in fields named "numeric_cross_check*".
The Maximum Hypothesis is NOT checked here; items that depend on it are flagged as conditional.

Run from the lane root:   .venv/bin/python code/anchors_lemma58.py
Writes evidence/anchors_lemma58.json and evidence/anchors_lemma57_parametrisation.json.
Single thread (BLAS and FLINT pinned to 1 thread).
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import hashlib
import itertools
import json
import math
import platform
import random
import resource
import subprocess
import sys
import time
from fractions import Fraction
from pathlib import Path

import flint
import mpmath
import numpy as np
import scipy
import sympy as sp

flint.ctx.threads = 1

LANE = Path(__file__).resolve().parent.parent
OUT_MAIN = LANE / "evidence" / "anchors_lemma58.json"
OUT_PARAM = LANE / "evidence" / "anchors_lemma57_parametrisation.json"
SRC_PDF = LANE / "sources" / "diaz2009-3col-preprint.pdf"
SRC_TXT = LANE / "sources" / "diaz2009-3col-preprint.layout.txt"

NVAR = 324     # 9 classes x 36 spectra
NFREE = 301    # 324 - rank 23
SEED = 20261016

# Values printed in the paper (read from the rendered PDF pages 6, 11, 14, 23-25).
PAPER = {
    "detH_sign": -1,
    "detH": {2: 175, 3: 1078, 5: 310, 7: 12, 11: 14, 13: 1, 17: 1, 79: 4},          # Lemma 5.8
    "g_b": {2: 90, 3: 558, 5: 171},                                                  # Lemma 5.8
    # (2.4): EY ~ sqrt(2^2 3^6 5^3 / 11^3) (2 pi n)^-1 (25/24)^(n/2)
    "EY_const_sq": {2: 2, 3: 6, 5: 3, 11: -3},
    # (2.5) / Thm 5.1: E(Y^2) ~ 2^2 3^19 5^16 / (7^6 11^7 79^2 sqrt(13*17)) (2 pi n)^-2 (25/24)^n
    "EY2_const_sq": {2: 4, 3: 38, 5: 32, 7: -12, 11: -14, 13: -1, 17: -1, 79: -4},
    # Lemma 5.9: 2^3 3^19 5^16 (2 pi n)^(301/2) / (7^6 11^7 79^2 sqrt(2*13*17)) (25/24)^n 5^(5n/2)
    "L59_const_sq": {2: 5, 3: 38, 5: 32, 7: -12, 11: -14, 13: -1, 17: -1, 79: -4},
    # (2.3) and the ratio in Section 2: 3^13 5^13 / (7^6 11^4 79^2 sqrt(13*17))
    "ratio_const_sq": {3: 26, 5: 26, 7: -12, 11: -8, 13: -1, 17: -1, 79: -4},
    # (5.1): h(n) = 2^(-1/2) (2 pi n)^(-305/2) 5^(-5n/2)
    "h_two_pi_n_exp": Fraction(-305, 2),
}


# ----------------------------------------------------------------------------------------------
# small utilities
# ----------------------------------------------------------------------------------------------
def host_date():
    plain = subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()
    iso = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S%z"], capture_output=True, text=True,
                         check=True).stdout.strip()
    return {"date": plain, "iso": iso}


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verdict(ok):
    return "MATCH" if ok else "MISMATCH"


def factor_int(n):
    """{p: e} with prod p^e == |n| (n != 0); FLINT factorisation, multiplied back as a check."""
    n = abs(int(n))
    assert n != 0
    if n == 1:
        return {}
    fac = {int(p): int(e) for p, e in flint.fmpz(n).factor()}
    back = 1
    for p, e in fac.items():
        assert flint.fmpz(p).is_prime()
        back *= p ** e
    assert back == n
    return dict(sorted(fac.items()))


def factor_frac(q):
    q = Fraction(q)
    fac = dict(factor_int(q.numerator))
    for p, e in factor_int(q.denominator).items():
        fac[p] = fac.get(p, 0) - e
    return {p: e for p, e in sorted(fac.items()) if e != 0}


def fac_mul(a, b, k=1):
    out = dict(a)
    for p, e in b.items():
        out[p] = out.get(p, 0) + k * e
    return {p: e for p, e in sorted(out.items()) if e != 0}


def fac_scale(a, k):
    return {p: e * k for p, e in a.items() if e * k != 0}


def fac_eq(a, b):
    return fac_mul(a, b, -1) == {}


def fac_str(fac, sign=1):
    parts = []
    for p, e in sorted(fac.items()):
        e = Fraction(e)
        if e == 1:
            parts.append(f"{p}")
        elif e.denominator == 1:
            parts.append(f"{p}^{e.numerator}")
        else:
            parts.append(f"{p}^({e})")
    return ("-" if sign < 0 else "") + (" * ".join(parts) if parts else "1")


def fac_json(fac):
    return {str(p): str(Fraction(e)) for p, e in sorted(fac.items())}


def frac_from_fac(fac):
    num, den = 1, 1
    for p, e in fac.items():
        e = Fraction(e)
        assert e.denominator == 1
        if e > 0:
            num *= p ** int(e)
        else:
            den *= p ** int(-e)
    return Fraction(num, den)


def zmat(rows):
    return flint.fmpz_mat([[int(x) for x in r] for r in rows])


def zmat_rows(M):
    return [[int(x) for x in r] for r in M.tolist()]


# ----------------------------------------------------------------------------------------------
# spectra and indexing (Section 4)
# ----------------------------------------------------------------------------------------------
OFF = [(-1, -1), (-1, 1), (1, -1), (1, 1)]   # entry order (s_{-1,-1}, s_{-1,1}, s_{1,-1}, s_{1,1})


def eidx(r, t):
    return OFF.index((r, t))


ALL56 = [s for s in itertools.product(range(6), repeat=4) if sum(s) == 5]
S = [s for s in ALL56
     if s[0] + s[1] >= 1 and s[2] + s[3] >= 1      # row sums >= 1 (C1 locally rainbow)
     and s[0] + s[2] >= 1 and s[1] + s[3] >= 1]    # column sums >= 1 (C2 locally rainbow)
W = [math.factorial(5) // math.prod(math.factorial(x) for x in s) for s in S]   # w_s = (5 choose s)


def cls(i, j):
    return 3 * (i % 3) + (j % 3)


def var(i, j, k):
    """index of d^{i,j}_s for s = S[k]"""
    return 36 * cls(i, j) + k


def label(v):
    c, k = divmod(v, 36)
    i, j = divmod(c, 3)
    return f"d^({i},{j})_{S[k]}"


def lemma57_system():
    """The 24 equations of Lemma 5.7.  Rows are integer coefficient vectors, rhs exact.

    The paper writes the pairing equations as sum_s s^t_1 d^{i,j}_s - sum_s s^{-t}_{-1} d^{i+1,j+t}_s = 0;
    s^t_1 is read as s_{1,t} (row index 1, column index t), which is (4.3) with r = 1:
    m^{i,j}_{1,t} = m^{i+1,j+t}_{-1,-t}.  (The other reading s_{t,1} would compare m^{i,j}_{t,1} with
    m^{i+1,j+t}_{-t,-1}, which is not of the form (4.3).)"""
    rows, rhs, names = [], [], []
    for i in range(3):
        for j in range(3):
            for t in (-1, 1):
                row = [0] * NVAR
                for k, s in enumerate(S):
                    row[var(i, j, k)] += s[eidx(1, t)]
                    row[var(i + 1, j + t, k)] -= s[eidx(-1, -t)]
                rows.append(row)
                rhs.append(Fraction(0))
                names.append(f"pair(i={i},j={j},t={t})")
    for i in range(3):
        row = [0] * NVAR
        for j in range(3):
            for k in range(36):
                row[var(i, j, k)] = 1
        rows.append(row)
        rhs.append(Fraction(1, 3))
        names.append(f"rowsum(i={i})")
    for j in range(3):
        row = [0] * NVAR
        for i in range(3):
            for k in range(36):
                row[var(i, j, k)] = 1
        rows.append(row)
        rhs.append(Fraction(1, 3))
        names.append(f"colsum(j={j})")
    return rows, rhs, names


def form43(i, j, r, t):
    """(4.3) as a linear form in d: m^{i,j}_{r,t} - m^{i+r,j+t}_{-r,-t}."""
    row = [0] * NVAR
    for k, s in enumerate(S):
        row[var(i, j, k)] += s[eidx(r, t)]
        row[var(i + r, j + t, k)] -= s[eidx(-r, -t)]
    return row


def integral_gauss_jordan(rows, rhs):
    """Gauss-Jordan elimination over Q that keeps every coefficient row integral.

    Pivots are always +-1 entries, so eliminating with them keeps the rows integral.  When no
    remaining row has a +-1 entry, every remaining nonzero row is divided by its content (gcd of its
    coefficients); this exact rational rescaling does not change the solution set and is recorded.
    The rhs is carried as exact Fractions.  Returns (rows, rhs, pivots [(row, col)], leftover rows,
    content divisions [(row, divisor)])."""
    R = [list(r) for r in rows]
    c = [Fraction(x) for x in rhs]
    nr, nc = len(R), len(rows[0])
    used, pivcols, pivots, divisions = set(), set(), [], []
    while True:
        best = None
        for r in range(nr):
            if r in used:
                continue
            Rr = R[r]
            for col in range(nc):
                if col in pivcols or abs(Rr[col]) != 1:
                    continue
                fill = sum(1 for q in range(nr) if q != r and R[q][col] != 0)
                key = (fill, col, r)
                if best is None or key < best[0]:
                    best = (key, r, col)
        if best is None:
            progressed = False
            for r in range(nr):
                if r in used or not any(R[r]):
                    continue
                g = math.gcd(*R[r])
                if g > 1:
                    R[r] = [x // g for x in R[r]]
                    c[r] = c[r] / g
                    divisions.append((r, g))
                    progressed = True
            if progressed:
                continue
            break
        _, r, col = best
        if R[r][col] == -1:
            R[r] = [-x for x in R[r]]
            c[r] = -c[r]
        Rr, cr = R[r], c[r]
        for q in range(nr):
            if q != r and R[q][col] != 0:
                fq = R[q][col]
                R[q] = [a - fq * b for a, b in zip(R[q], Rr)]
                c[q] = c[q] - fq * cr
        used.add(r)
        pivcols.add(col)
        pivots.append((r, col))
    leftover = [r for r in range(nr) if r not in used]
    return R, c, pivots, leftover, divisions


def bareiss_symmetric_leading_minors(G):
    """Fraction-free (Bareiss) elimination without pivoting on a symmetric integer matrix.

    Returns the list of leading principal minors Delta_1..Delta_n (stops at a zero pivot).
    Every division is asserted exact.  Trailing blocks stay symmetric, so only j >= i is updated.
    The LDL^T pivots over Q are D_k = Delta_k / Delta_{k-1}."""
    n = len(G)
    Amat = [list(r) for r in G]
    prev = 1
    minors = []
    for k in range(n):
        Ak = Amat[k]
        piv = Ak[k]
        minors.append(piv)
        if piv == 0:
            break
        for i in range(k + 1, n):
            Ai = Amat[i]
            aik = Ak[i]                  # = A[i][k] by symmetry of the trailing block
            for j in range(i, n):
                q, rem = divmod(Ai[j] * piv - aik * Ak[j], prev)
                if rem:
                    raise ArithmeticError("inexact Bareiss division")
                Ai[j] = q
        prev = piv
    return minors


# ----------------------------------------------------------------------------------------------
# asymptotic bookkeeping:  const * pi^a * n^b * base^n * n^(c n) * e^(e n)
# ----------------------------------------------------------------------------------------------
class Asym:
    def __init__(self, const=None, pi_e=0, n_e=0, base=None, nlogn=0, e_coef=0):
        self.const = {p: Fraction(e) for p, e in sorted((const or {}).items()) if e != 0}
        self.pi_e = Fraction(pi_e)
        self.n_e = Fraction(n_e)
        self.base = {p: Fraction(e) for p, e in sorted((base or {}).items()) if e != 0}
        self.nlogn = Fraction(nlogn)
        self.e_coef = Fraction(e_coef)

    def __mul__(self, o):
        return Asym(fac_mul(self.const, o.const), self.pi_e + o.pi_e, self.n_e + o.n_e,
                    fac_mul(self.base, o.base), self.nlogn + o.nlogn, self.e_coef + o.e_coef)

    def __pow__(self, k):
        k = Fraction(k)
        return Asym(fac_scale(self.const, k), self.pi_e * k, self.n_e * k,
                    fac_scale(self.base, k), self.nlogn * k, self.e_coef * k)

    def __truediv__(self, o):
        return self * (o ** -1)

    def __eq__(self, o):
        return (fac_eq(self.const, o.const) and self.pi_e == o.pi_e and self.n_e == o.n_e
                and fac_eq(self.base, o.base) and self.nlogn == o.nlogn and self.e_coef == o.e_coef)

    def normalised(self):
        """If pi and n carry the same exponent k, write as C (2 pi n)^k B^n; return (C, k, B) as dicts."""
        assert self.pi_e == self.n_e and self.nlogn == 0 and self.e_coef == 0
        k = self.pi_e
        return fac_mul(self.const, {2: -k}), k, self.base

    def describe(self):
        if self.pi_e == self.n_e and self.nlogn == 0 and self.e_coef == 0:
            C, k, B = self.normalised()
            return f"[{fac_str(C)}] * (2 pi n)^({k}) * [{fac_str(B)}]^n"
        return (f"[{fac_str(self.const)}] pi^({self.pi_e}) n^({self.n_e}) [{fac_str(self.base)}]^n "
                f"n^({self.nlogn} n) e^({self.e_coef} n)")


def a_const(q, k=1):
    return Asym(const=fac_scale(factor_frac(q), Fraction(k)))


def a_base(q, k=1):
    """q^(k n)"""
    return Asym(base=fac_scale(factor_frac(q), Fraction(k)))


def a_two_pi_n(k):
    """(2 pi n)^k"""
    return Asym(const={2: Fraction(k)}, pi_e=k, n_e=k)


def a_n_over_e(c):
    """(n/e)^(c n)"""
    return Asym(nlogn=c, e_coef=-Fraction(c))


def a_stirling(a):
    """(a n)! ~ sqrt(2 pi a n) (a n / e)^(a n) = (2 pi n)^(1/2) a^(1/2) a^(a n) (n/e)^(a n)"""
    a = Fraction(a)
    return a_two_pi_n(Fraction(1, 2)) * a_const(a, Fraction(1, 2)) * a_base(a, a) * a_n_over_e(a)


# ----------------------------------------------------------------------------------------------
def main():
    t_start = time.perf_counter()
    date_start = host_date()
    timings = {}
    res = {
        "task": "anchors_lemma58: exact non-hypothesis anchors of Diaz et al. (2009) Sections 5.2 and 2",
        "lane": str(LANE),
        "date_start": date_start,
        "conventions": {
            "spectrum_entry_order": "(s_{-1,-1}, s_{-1,1}, s_{1,-1}, s_{1,1})",
            "variable_index": "v = 36*(3*i+j) + k, s = S[k], S in lexicographic order of the 4-tuple",
            "lemma57_pairing_reading": "s^t_1 := s_{1,t}, s^{-t}_{-1} := s_{-1,-t}  ((4.3) with r = 1)",
            "exact_vs_float": "all equalities exact (python-flint/fractions/sympy); floats only in "
                              "fields named numeric_cross_check*",
        },
    }

    # ------------------------------------------------------------------ item 0: spectra
    t0 = time.perf_counter()
    assert len(ALL56) == 56 and len(S) == 36
    res["spectra"] = {
        "count_all_sum5": len(ALL56),
        "count_S": len(S),
        "count_S_match_paper_36": verdict(len(S) == 36),
        "w_multiset": {str(wv): W.count(wv) for wv in sorted(set(W))},
        "sum_w": sum(W),
        "sum_w_equals_Phi(1,1,1,1)=4^5-4*2^5+4": sum(W) == 4 ** 5 - 4 * 2 ** 5 + 4,
    }
    timings["spectra_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ item 1: Lemma 5.7
    t0 = time.perf_counter()
    rows, rhs, names = lemma57_system()
    pair_rows = rows[:18]
    forms = {}
    for i in range(3):
        for j in range(3):
            for r in (-1, 1):
                for t in (-1, 1):
                    forms[(i, j, r, t)] = form43(i, j, r, t)
    # r = 1 forms coincide with the 18 pairing rows of Lemma 5.7 (same order i, j, t)
    r1_equal = all(forms[(i, j, 1, t)] == pair_rows[6 * i + 2 * j + (0 if t == -1 else 1)]
                   for i in range(3) for j in range(3) for t in (-1, 1))
    # r = -1 forms are the negatives of r = 1 forms: m^{ij}_{-1,t} - m^{i-1,j+t}_{1,-t}
    #   = -(m^{i',j'}_{1,t'} - m^{i'+1,j'+t'}_{-1,-t'}) with i' = i-1, j' = j+t, t' = -t
    rm1_neg = all(forms[(i, j, -1, t)] == [-x for x in forms[((i - 1) % 3, (j + t) % 3, 1, -t)]]
                  for i in range(3) for j in range(3) for t in (-1, 1))
    set43 = {tuple(rw) for rw in forms.values()} | {tuple(-x for x in rw) for rw in forms.values()}
    setpair = {tuple(rw) for rw in pair_rows} | {tuple(-x for x in rw) for rw in pair_rows}
    distinct_pair = len({tuple(rw) for rw in pair_rows}) == 18 and all(any(rw) for rw in pair_rows)
    rank_pair = zmat(pair_rows).rank()
    rank_43 = zmat(list(forms.values())).rank()
    Mz = zmat(rows)
    rank_M = Mz.rank()
    # augmented matrix (rows scaled by 3 to clear the 1/3): rank must stay 23 (consistency)
    aug = [[3 * x for x in rw] + [int(3 * c)] for rw, c in zip(rows, rhs)]
    rank_aug = zmat(aug).rank()
    rank_pair_rows = zmat(rows[:21]).rank()
    rank_pair_cols = zmat(rows[:18] + rows[21:]).rank()
    # left kernel of M (dependencies among the 24 equations)
    X, nullity = Mz.transpose().nullspace()
    dep = None
    if nullity >= 1:
        dep = [int(X[q, 0]) for q in range(24)]
        gd = math.gcd(*dep)
        dep = [x // gd for x in dep]
    dep_expected = [0] * 18 + [1, 1, 1, -1, -1, -1]
    dep_ok = (nullity == 1 and dep is not None
              and (dep == dep_expected or dep == [-x for x in dep_expected]))
    dep_annihilates_rhs = dep is not None and sum(Fraction(c) * r for c, r in zip(dep, rhs)) == 0
    res["item1_lemma57"] = {
        "n_equations": len(rows),
        "n_variables": NVAR,
        "rank_M": rank_M,
        "rank_M_match_paper_23": verdict(rank_M == 23),
        "rank_augmented": rank_aug,
        "system_consistent": rank_aug == rank_M,
        "rank_pairing_18_rows": rank_pair,
        "rank_pairing_plus_rowsums": rank_pair_rows,
        "rank_pairing_plus_colsums": rank_pair_cols,
        "left_kernel_dimension": int(nullity),
        "unique_dependency": "sum_i rowsum(i) - sum_j colsum(j) = 0 (coefficients "
                             "(0^18, 1,1,1, -1,-1,-1)); rhs 1/3*3 - 1/3*3 = 0",
        "unique_dependency_verified": bool(dep_ok and dep_annihilates_rhs),
        "pairing_equals_(4.3)": {
            "r=+1_forms_equal_the_18_Lemma57_rows": r1_equal,
            "r=-1_forms_are_negatives_of_r=+1_forms": rm1_neg,
            "set_of_36_(4.3)_forms_equals_18_pairing_rows_up_to_sign": set43 == setpair,
            "18_pairing_rows_distinct_nonzero": distinct_pair,
            "rank_of_all_36_(4.3)_forms": rank_43,
            "verdict": verdict(r1_equal and rm1_neg and set43 == setpair and rank_43 == 18
                               and rank_pair == 18),
        },
    }

    # explicit parametrisation of Lemma 5.7 type: Gauss-Jordan over Q with integral rows and +-1 pivots
    R, cred, pivots, leftover, divisions = integral_gauss_jordan(rows, rhs)
    leftover_zero = all(all(x == 0 for x in R[r]) and cred[r] == 0 for r in leftover)
    B = [c for _, c in pivots]
    Bset = set(B)
    F = [c for c in range(NVAR) if c not in Bset]
    piv_rows_ok = all(R[r][c] == 1 and all(R[r][c2] == 0 for _, c2 in pivots if c2 != c)
                      for r, c in pivots)
    assert len(pivots) == 23 and len(F) == NFREE and leftover_zero and piv_rows_ok
    # reduced (equivalent over Q) system:  d_c + sum_{f in F} R[r][f] d_f = cred[r]  for each pivot (r, c)
    R_red = [R[r] for r, _ in pivots]                       # 23 integral rows, identity on B
    rank_with_red = zmat(rows + R_red).rank()               # R_red lies in the Q-row space of M
    const = {c: cred[r] for r, c in pivots}
    const6_integral = all((6 * v).denominator == 1 for v in const.values())
    assert const6_integral
    const6 = {c: int(6 * v) for c, v in const.items()}
    P0 = [[0] * NFREE for _ in range(NVAR)]
    for p, f in enumerate(F):
        P0[f][p] = 1
    for r, c in pivots:
        for p, f in enumerate(F):
            P0[c][p] = -R[r][f]
    # particular solution (d_F = 0) solves the inhomogeneous system exactly
    dpart = [Fraction(0)] * NVAR
    for c, v in const.items():
        dpart[c] = v
    part_ok = all(sum(a * x for a, x in zip(rw, dpart)) == c for rw, c in zip(rows, rhs))
    # the centre b (b^{ij}_s = w_s/8100) satisfies the system and the parametrisation
    b = [Fraction(W[v % 36], 8100) for v in range(NVAR)]
    b_solves = all(sum(a * x for a, x in zip(rw, b)) == c for rw, c in zip(rows, rhs))
    b_param = all(b[c] == const[c] - sum(R[r][f] * b[f] for f in F) for r, c in pivots)
    # 23 independent original rows (drop colsum(j=2)); their minor on B measures the index of the
    # original row lattice in its saturation (M' = T R_red with T integral, M'_B = T)
    Mp_rows = rows[:23]
    Mp = zmat(Mp_rows)
    rank_Mp = Mp.rank()
    minorB = int(zmat([[rw[c] for c in B] for rw in Mp_rows]).det())
    maxcoef = max(abs(P0[c][p]) for c in B for p in range(NFREE))
    nnz_C = sum(1 for c in B for p in range(NFREE) if P0[c][p] != 0)
    moreover_ok = (part_ok and b_solves and b_param and const6_integral and leftover_zero
                   and piv_rows_ok and rank_Mp == 23 and rank_with_red == 23)
    res["item1_lemma57"]["parametrisation"] = {
        "method": "Gauss-Jordan over Q keeping rows integral: +-1 pivots only, plus exact division of a "
                  "remaining row by its content when no +-1 entry is left; free coordinates F (301), "
                  "dependent coordinates B (23)",
        "content_divisions": [{"row_origin": names[r], "divisor": g} for r, g in divisions],
        "n_free": len(F),
        "n_dependent": len(B),
        "dependent_variables": [label(c) for c in B],
        "constants_in_units_of_1/6": {label(c): const6[c] for c in B},
        "constants_need_1/6_not_just_1/3": any(v.denominator == 6 for v in const.values()),
        "lcm_of_constant_denominators": math.lcm(*[v.denominator for v in const.values()]),
        "integer_points_exist_iff_lcm_divides_n": (
            "scaled system x = n d: x_B = C x_F + n*const with C integral, so an integer solution exists iff "
            "n*const is integral (x_F = 0 works; conversely n*const = x_B - C x_F), i.e. iff lcm | n. With "
            "lcm = 6 this matches the paper's L_k(., 1/6) and its assumption n = 0 mod 6."),
        "all_coefficients_integer": True,
        "max_abs_coefficient": maxcoef,
        "nonzero_coefficients": nnz_C,
        "reduced_rows_in_Q_rowspace_of_M (rank of [M; R_red])": rank_with_red,
        "particular_solution_dF0_solves_system_exactly": part_ok,
        "centre_b_solves_system_exactly": b_solves,
        "centre_b_satisfies_parametrisation_exactly": b_param,
        "rank_of_23_rows_without_colsum2": rank_Mp,
        "det_of_original_23x23_minor_on_B": minorB,
        "index_of_original_row_lattice_in_its_saturation": abs(minorB),
        "lemma57_moreover_form_reproduced": verdict(moreover_ok),
        "file": str(OUT_PARAM.relative_to(LANE)),
    }
    timings["item1_lemma57_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ item 2: lattice basis
    # Lambda = { v in Z^324 : M v = 0 }.
    # P0 = [I_F ; C_B] (rows of F carry the identity, rows of B carry C = -R_red[.][F]) is a Z-basis:
    #   * its columns are integral and M P0 = 0 (checked);
    #   * the 301x301 minor of P0 on the rows F is det(I) = 1, so the gcd of the maximal minors
    #     of P0 is 1 (P0 is saturated: P0 Q^301 cap Z^324 = P0 Z^301);
    #   * completeness: the reduced system (R_red, cred) is equivalent over Q to the original one
    #     (Gauss-Jordan steps and content divisions are invertible over Q).  For v in Lambda the
    #     homogeneous reduced equations give v_B = -C v_F, i.e. v = P0 v_F with v_F in Z^301.
    #   Note: the Z-span of the original 23 independent rows is NOT saturated (index |det M'_B|);
    #   its saturation has basis R_red (identity on B).  Covolume duality for primitive lattices
    #   therefore reads det(P0^T P0) = det(R_red R_red^T), and det(M'M'^T) = det(M'_B)^2 det(R_red R_red^T).
    #
    # Why det(P^T Hf P) is basis independent and equals the paper's det H~:
    #   (a) two Z-bases of the same lattice differ by U in GL_301(Z): P' = P U, det U = +-1, so
    #       det(P'^T Hf P') = det(U)^2 det(P^T Hf P) = det(P^T Hf P).
    #   (b) a parametrisation of the Lemma 5.7 type (d_1..d_301 free, d_k = L_k(d_1..d_301, 1/6),
    #       L_k with integer coefficients, valid for ALL solutions) is affine with linear part
    #       P_L = [I ; C_L], C_L integral.  Its columns are integral kernel vectors, the identity
    #       block makes them independent and saturated, and every v in Lambda equals P_L v_F
    #       (v - P_L v_F is a homogeneous solution with zero free part, hence zero because the
    #       parametrisation covers all solutions).  So P_L is a Z-basis of Lambda.
    #   (c) f~ = f o (affine map with linear part P_L), hence the Hessian of f~ at b~ is
    #       H~ = P_L^T Hf(b) P_L, and by (a)-(b) det H~ = det(P^T Hf P) for every Z-basis P,
    #       whichever unimodular parametrisation the paper used.  This is also the normalisation
    #       that Lemma 5.9 needs: J = Q cap (1/n)Z^324 is a translate of (1/n)Lambda, whose cells
    #       have volume n^-301 in P-coordinates, which gives the factor n^301 in (5.26).
    t0 = time.perf_counter()
    P0z = zmat(P0)
    MP0_zero = (Mz * P0z).is_zero()
    P0F = zmat([P0[f] for f in F])
    P0F_is_identity = P0F.is_one()
    ones_P0_zero = all(sum(P0[v][p] for v in range(NVAR)) == 0 for p in range(NFREE))
    # Gram/covolume duality check for primitive lattices: det(Lambda) = det(Lambda^perp)
    R_red_z = zmat(R_red)
    gram_ker = (P0z.transpose() * P0z).det()
    gram_red = (R_red_z * R_red_z.transpose()).det()
    gram_row = (Mp * Mp.transpose()).det()
    R_red_B_identity = zmat([[rw[c] for c in B] for rw in R_red]).is_one()
    # independent basis: HNF of [M^T | I_324]; rows with zero left block give Lambda
    Xhnf = flint.fmpz_mat([[rows[q][k] for q in range(24)] + [1 if kk == k else 0 for kk in range(NVAR)]
                           for k in range(NVAR)])
    t_h = time.perf_counter()
    H = Xhnf.hnf()
    t_hnf = time.perf_counter() - t_h
    Hl = zmat_rows(H)
    zero_rows = [r for r in range(NVAR) if all(Hl[r][c] == 0 for c in range(24))]
    hnf_rows_ok = zero_rows == list(range(23, NVAR))
    PB_T = [Hl[r][24:] for r in zero_rows]
    PBz = zmat(PB_T).transpose()
    MPB_zero = (Mz * PBz).is_zero()
    rank_PB = PBz.rank()
    T = zmat([[PB_T[p][f] for p in range(len(PB_T))] for f in F])     # rows F of P_B
    detT = int(T.det())
    same_lattice = abs(detT) == 1 and (P0z * T) == PBz
    maxabs_PB = max(abs(x) for rw in PB_T for x in rw)
    # control: FLINT's raw rational-kernel basis (scaled to integers) spans ker(M) over Q but in general
    # only a sublattice of Lambda; its index is |det of its F-rows| (X_K = P0 X_K[F])
    Xn, nul = Mz.nullspace()
    XK = [[int(Xn[v, p]) for p in range(nul)] for v in range(NVAR)]
    XKz = zmat(XK)
    idx_raw = abs(int(zmat([XK[f] for f in F]).det()))
    XK_in_lattice = nul == NFREE and (Mz * XKz).is_zero() and (P0z * zmat([XK[f] for f in F])) == XKz
    res["item2_lattice_basis"] = {
        "P0_shape": [NVAR, NFREE],
        "P0_integral": True,
        "M_P0_is_zero": MP0_zero,
        "P0_rows_F_is_identity (maximal minor = 1, gcd of maximal minors = 1)": P0F_is_identity,
        "P0_completeness_argument": "reduced system equivalent over Q with identity on B: "
                                    "v in Lambda => v_B = -C v_F => v = P0 v_F, v_F in Z^301",
        "det_M'_B (original 23 rows, pivot columns)": minorB,
        "R_red_restricted_to_B_is_identity": R_red_B_identity,
        "ones_vector_orthogonal_to_Lambda (1^T P0 = 0)": ones_P0_zero,
        "gram_det_P0TP0": str(gram_ker),
        "gram_det_RredRredT": str(gram_red),
        "gram_det_M'M'T": str(gram_row),
        "covolume_duality det(P0^T P0) == det(R_red R_red^T)": gram_ker == gram_red,
        "det(M'M'^T) == det(M'_B)^2 det(R_red R_red^T)": gram_row == minorB ** 2 * gram_red,
        "control_raw_nullspace_basis": {
            "what": "flint fmpz_mat.nullspace() basis X_K (integral, spans ker M over Q)",
            "X_K_columns_in_Lambda_and_X_K == P0 X_K[F]": XK_in_lattice,
            "index_[Lambda : X_K Z^301] = |det X_K[F]|": str(idx_raw),
            "note": "a non-saturated basis multiplies det(P^T Hf P) by index^2 (checked in item 3)",
        },
        "basis_independence_justification": (
            "Two Z-bases of Lambda differ by U in GL_301(Z), so det(P'^T Hf P') = det(U)^2 det(P^T Hf P) = "
            "det(P^T Hf P). A Lemma-5.7-type parametrisation (301 free coordinates, the other 23 integer-linear "
            "in them plus multiples of 1/6, valid for all solutions) has linear part [I; C] with C integral, "
            "which is a Z-basis of Lambda (integral kernel vectors, identity block => saturated, and every "
            "v in Lambda equals [I; C] v_F). The Hessian of f~ = f o (that affine map) at b~ is "
            "[I; C]^T Hf(b) [I; C], so det H~ = det(P^T Hf P) for every Z-basis P, whichever such "
            "parametrisation the paper used; it is also the normalisation required by (5.26), since "
            "J = Q cap (1/n)Z^324 is a translate of (1/n)Lambda."),
        "independent_basis_PB": {
            "method": "flint HNF of [M^T | I_324] (324 x 348); rows 23..323 have zero left block, "
                      "their right blocks form a Z-basis of Lambda (rows of a unimodular transform)",
            "hnf_seconds": round(t_hnf, 3),
            "zero_left_block_rows_are_23..323": hnf_rows_ok,
            "M_PB_is_zero": MPB_zero,
            "rank_PB": rank_PB,
            "max_abs_entry_PB": maxabs_PB,
            "det_of_rows_F_of_PB": detT,
            "PB_equals_P0_times_PB[F]_with_unimodular_PB[F]": same_lattice,
        },
        "lattice_basis_check": "PASS" if (MP0_zero and P0F_is_identity and R_red_B_identity
                                          and gram_ker == gram_red and gram_row == minorB ** 2 * gram_red
                                          and hnf_rows_ok and MPB_zero and rank_PB == NFREE
                                          and same_lattice) else "FAIL",
    }
    timings["item2_lattice_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ item 3: Hessian
    # f(d) = sum_v d_v (ln w_v - ln d_v) + (1/2) sum_e m_e ln m_e,   m = A d  (A: 36 x 324, A[e][v] = s_e)
    # df/dd_v       = ln w_v - ln d_v - 1 + (1/2) sum_e A[e][v] (ln m_e + 1)
    # d2f/dd_v dd_u = -delta_{vu}/d_v + (1/2) sum_e A[e][v] A[e][u] / m_e
    # => Hf = -diag(1/d) + (1/2) A^T diag(1/m) A.
    t0 = time.perf_counter()
    A = [[0] * NVAR for _ in range(36)]
    for i in range(3):
        for j in range(3):
            for k, s in enumerate(S):
                for e in range(4):
                    A[4 * cls(i, j) + e][var(i, j, k)] = s[e]
    m = [sum(A[e][v] * b[v] for v in range(NVAR)) for e in range(36)]
    m_ok = all(me == Fraction(5, 36) for me in m)
    nij_ok = all(sum(b[var(i, j, k)] for k in range(36)) == Fraction(1, 9)
                 for i in range(3) for j in range(3))
    colsumA_5 = all(sum(A[e][v] for e in range(36)) == 5 for v in range(NVAR))
    wb_ratio = all(Fraction(W[v % 36]) / b[v] == 8100 for v in range(NVAR))
    # K5 = -5 Hf(b) from the general formula (sum over e restricted to the support of column v of A);
    # assert integrality and the block structure
    supp = [[e for e in range(36) if A[e][v]] for v in range(NVAR)]
    K5 = [[0] * NVAR for _ in range(NVAR)]
    for v in range(NVAR):
        for u in range(NVAR):
            h = Fraction(1, 2) * sum(Fraction(A[e][v] * A[e][u]) / m[e] for e in supp[v] if A[e][u])
            if u == v:
                h -= 1 / b[v]
            val = -5 * h
            assert val.denominator == 1
            K5[v][u] = int(val)
    block_diag = all(K5[v][u] == 0 for v in range(NVAR) for u in range(NVAR) if v // 36 != u // 36)
    K5z = zmat(K5)
    G0 = P0z.transpose() * K5z * P0z          # G0 = -5 P0^T Hf P0 = -5 H~ (P0 coordinates)
    GB = PBz.transpose() * K5z * PBz
    detG0 = int(G0.det())
    detGB = int(GB.det())
    # control 1: the raw (non-saturated) nullspace basis gives det * index^2
    detG_raw = int((XKz.transpose() * K5z * XKz).det())
    raw_ratio_is_index_sq = detG_raw == idx_raw ** 2 * detG0
    # control 2: without the constraints the Hessian is indefinite: K5 has a positive diagonal but
    # b^T K5 b = -5 (-sum b + (1/2) sum m) = -5 (-1 + 5/2) = -15/2 < 0
    bK5b = sum(b[v] * K5[v][u] * b[u] for v in range(NVAR) for u in range(36 * (v // 36), 36 * (v // 36) + 36))
    K5_diag_pos = all(K5[v][v] > 0 for v in range(NVAR))
    timings["item3_det_s"] = time.perf_counter() - t0
    # det H~ = det(-G/5) = (-1)^301 det(G) / 5^301
    detH = Fraction((-1) ** NFREE * detG0, 5 ** NFREE)
    detH_sign = 1 if detH > 0 else -1
    detH_fac = factor_frac(abs(detH))
    det_match = detH_sign == PAPER["detH_sign"] and fac_eq(detH_fac, PAPER["detH"])
    det_ratio_to_paper = fac_mul(detH_fac, PAPER["detH"], -1)
    # exact definiteness: Bareiss leading principal minors of G0 (Sylvester); LDL^T pivots D_k
    t1 = time.perf_counter()
    G0_int = zmat_rows(G0)
    sym_ok = all(G0_int[a][c] == G0_int[c][a] for a in range(NFREE) for c in range(a))
    minors = bareiss_symmetric_leading_minors(G0_int)
    t_bareiss = time.perf_counter() - t1
    all_pos = len(minors) == NFREE and all(x > 0 for x in minors)
    last_eq_det = minors[-1] == detG0
    t1 = time.perf_counter()
    Pf, Lf, Df, Uf = G0.fflu()
    fflu_noperm = Pf.is_one()
    fflu_diag = [int(Uf[q, q]) for q in range(NFREE)]
    fflu_agree = fflu_noperm and fflu_diag == minors
    t_fflu = time.perf_counter() - t1
    ldl_pivots = [Fraction(minors[0])] + [Fraction(minors[q], minors[q - 1]) for q in range(1, NFREE)]
    min_piv = min(ldl_pivots)
    timings["item3_definiteness_s"] = time.perf_counter() - t0 - timings["item3_det_s"]

    # numeric cross-checks (float64 / mpmath; NOT part of any exact claim)
    G0f = np.array(G0_int, dtype=float)
    ev_G0 = np.linalg.eigvalsh(G0f)
    Hf_f = -np.array(K5, dtype=float) / 5.0
    Q, _ = np.linalg.qr(np.array(P0, dtype=float))
    ev_restricted = np.linalg.eigvalsh(Q.T @ Hf_f @ Q)
    sign_ld, logabs = np.linalg.slogdet(G0f)
    mpmath.mp.dps = 80
    rng = random.Random(SEED)
    fd_checks = []
    logw = [mpmath.log(wv) for wv in W]

    def f_mp(dv):
        tot = mpmath.mpf(0)
        for v in range(NVAR):
            tot += dv[v] * (logw[v % 36] - mpmath.log(dv[v]))
        for e in range(36):
            c0 = 36 * (e // 4)
            me = mpmath.fsum(A[e][v] * dv[v] for v in range(c0, c0 + 36))
            tot += me * mpmath.log(me) / 2
        return tot

    bm = [mpmath.mpf(x.numerator) / x.denominator for x in b]
    f_b = f_mp(bm)
    eps = mpmath.mpf("1e-25")
    for _trial in range(3):
        z = [rng.randint(-2, 2) for _ in range(NFREE)]
        vdir = [sum(P0[v][p] * z[p] for p in range(NFREE) if P0[v][p]) for v in range(NVAR)]
        exact_q = Fraction(-sum(vdir[a] * K5[a][c] * vdir[c] for a in range(NVAR) if vdir[a]
                               for c in range(36 * (a // 36), 36 * (a // 36) + 36) if vdir[c]), 5)
        fp = f_mp([bm[v] + eps * vdir[v] for v in range(NVAR)])
        fm = f_mp([bm[v] - eps * vdir[v] for v in range(NVAR)])
        fd = (fp - 2 * f_b + fm) / eps ** 2
        fd_checks.append({"vT_Hf_v_exact": str(exact_q),
                          "second_difference_mpmath": mpmath.nstr(fd, 25),
                          "rel_err": mpmath.nstr(abs(fd - mpmath.mpf(exact_q.numerator) / exact_q.denominator)
                                                 / abs(mpmath.mpf(exact_q.numerator) / exact_q.denominator), 5)})
    res["item3_hessian"] = {
        "derivation": "f(d) = sum d ln(w/d) + (1/2) sum m ln m, m = A d  =>  "
                      "Hf = -diag(1/d) + (1/2) A^T diag(1/m) A",
        "centre_checks": {
            "all_m_equal_5/36": m_ok,
            "all_n_ij_equal_1/9": nij_ok,
            "w_v/b_v_equals_8100": wb_ratio,
            "sum_e A[e][v] = 5": colsumA_5,
            "gradient_at_b_is_constant_vector_so_b_is_stationary_on_the_affine_slice":
                bool(m_ok and wb_ratio and colsumA_5 and ones_P0_zero),
        },
        "Hf_at_b": "Hf = -diag(8100/w_s) + (18/5) blockdiag_9(S S^T);  K5 := -5 Hf is integral",
        "K5_block_diagonal": block_diag,
        "detG_P0 (G = -5 P0^T Hf P0)": str(detG0),
        "detG_PB (independent basis)": str(detGB),
        "det_basis_independent (P0 vs PB)": detG0 == detGB,
        "control_raw_nullspace_basis_det_equals_index^2_times_detG": raw_ratio_is_index_sq,
        "control_raw_nullspace_basis_index": str(idx_raw),
        "control_unconstrained_hessian_indefinite": {
            "K5_diagonal_positive": K5_diag_pos,
            "b^T K5 b (exact)": str(bK5b),
            "indefinite_on_R^324": K5_diag_pos and bK5b < 0,
            "meaning": "negative definiteness holds only on the constraint lattice; the Sylvester test "
                       "on G = P^T K5 P is therefore not vacuous",
        },
        "detH_tilde_exact": {
            "formula": "det H~ = det(P^T Hf P) = (-1)^301 det(G) / 5^301",
            "sign": detH_sign,
            "factorisation": fac_str(detH_fac, detH_sign),
            "factorisation_json": fac_json(detH_fac),
            "decimal_digits_of_|numerator|": len(str(abs(detH.numerator))),
            "is_integer": detH.denominator == 1,
        },
        "paper_detH": fac_str(PAPER["detH"], PAPER["detH_sign"]),
        "detH_vs_paper": verdict(det_match),
        "computed_over_paper": fac_str(det_ratio_to_paper),
        "negative_definiteness_exact": {
            "method": "Sylvester: Bareiss fraction-free elimination (no pivoting) of G = -5 H~ "
                      "(P0 coordinates); leading principal minors Delta_k; LDL^T pivots D_k = "
                      "Delta_k/Delta_(k-1); cross-checked against flint fflu",
            "G_symmetric": sym_ok,
            "all_301_leading_minors_positive": all_pos,
            "last_minor_equals_det": last_eq_det,
            "flint_fflu_no_permutation_and_same_minors": fflu_agree,
            "min_LDL_pivot_of_G_(float_display)": float(min_piv),
            "min_LDL_pivot_of_G_exact": str(min_piv) if len(str(min_piv)) < 200 else
            f"{float(min_piv)!r} (exact fraction has {len(str(min_piv))} chars)",
            "bareiss_seconds": round(t_bareiss, 2),
            "fflu_seconds": round(t_fflu, 2),
            "H_tilde_negative_definite": all_pos and last_eq_det and fflu_agree,
            "verdict_vs_paper": verdict(all_pos and last_eq_det and fflu_agree),
        },
        "numeric_cross_check_float64": {
            "eig_G_P0_min": float(ev_G0.min()),
            "eig_G_P0_max": float(ev_G0.max()),
            "restricted_Hf_orthonormal_basis_eig_max (basis independent)": float(ev_restricted.max()),
            "restricted_Hf_orthonormal_basis_eig_min": float(ev_restricted.min()),
            "slogdet_G_P0_sign": float(sign_ld),
            "slogdet_G_P0_log": float(logabs),
            "log_detG_exact_(display)": float(mpmath.log(mpmath.mpf(detG0))),
        },
        "numeric_cross_check_hessian_formula_mpmath_dps80": {
            "method": "central second difference of f along b +- eps*P0 z, eps=1e-25, z in [-2,2]^301 "
                      f"(seed {SEED}) vs exact v^T Hf v",
            "f(b)_mpmath": mpmath.nstr(f_b, 30),
            "trials": fd_checks,
        },
    }
    timings["item3_total_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ item 4: g(b), prod w
    t0 = time.perf_counter()
    prod_w = math.prod(W)
    prod_w_fac = factor_int(prod_w)
    # g(b)^2 = prod_e m_e^(1/2) / prod_v b_v = (5/36)^18 * 8100^324 / (prod_s w_s)^9
    g_sq = Fraction(5, 36) ** 18 * Fraction(8100) ** 324 / Fraction(prod_w) ** 9
    # independent direct evaluation from the 36 m_e and 324 b_v: g^4 = prod_e m_e / prod_v b_v^2
    prod_m = Fraction(1)
    for me in m:
        prod_m *= me
    prod_b = Fraction(1)
    for x in b:
        prod_b *= x
    g4_direct = prod_m / prod_b ** 2
    g_sq_fac = factor_frac(g_sq)
    g_is_rational = all(e % 2 == 0 for e in g_sq_fac.values())
    g_fac = fac_scale(g_sq_fac, Fraction(1, 2))
    g_match = fac_eq(g_fac, PAPER["g_b"])
    res["item4_g_and_w"] = {
        "prod_s_w_s": str(prod_w),
        "prod_s_w_s_factorisation": fac_str(prod_w_fac),
        "g_b_definition": "g(b) = prod_{ij,rt} m^(1/4) / prod_{ij,s} b^(1/2), m = 5/36, b = w_s/8100",
        "g_b_squared_formula": "(5/36)^18 * 8100^324 / (prod_s w_s)^9",
        "g_b_fourth_power_direct_equals_formula": g4_direct == g_sq ** 2,
        "g_b_is_rational": g_is_rational,
        "g_b_factorisation": fac_str(g_fac),
        "paper_g_b": fac_str(PAPER["g_b"]),
        "g_b_vs_paper": verdict(g_match),
        "g_tilde_equals_g_at_b": "g~(b~) = g(b) because the parametrisation maps b~ to b "
                                 "(centre_b_satisfies_parametrisation_exactly)",
        "f_b_exact": {
            "f(b)": "ln 8100 + (5/2) ln(5/36)  (sum b = 1, sum m = 5)",
            "exp(2 f(b)) == (5^(5/2) * 25/24)^2": Fraction(8100) ** 2 * Fraction(5, 36) ** 5
            == Fraction(5 ** 5) * Fraction(25, 24) ** 2,
            "exp_f_b_float": float(mpmath.exp(f_b)),
            "paper_value": "25/24 * 5^(5/2) ~ 58.2309",
            "verdict": verdict(Fraction(8100) ** 2 * Fraction(5, 36) ** 5
                               == Fraction(5 ** 5) * Fraction(25, 24) ** 2
                               and abs(float(mpmath.exp(f_b)) - 58.2309) < 5e-5),
        },
    }
    timings["item4_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ item 5: constants
    t0 = time.perf_counter()
    item5 = {}
    # (a) delta_k from the transition matrix of Section 3 (matrix rebuilt from the state rule)
    states = [(1, 2), (2, 1), (3, 1), (1, 3), (2, 3), (3, 2)]
    c_alpha = Fraction((1 + 1) ** 3, (1 + 1) ** 5 - 1 - 1)             # 8/30
    c_beta = Fraction((1 + 1) ** 3 - 1, (1 + 1) ** 5 - 1 - 1)          # 7/30
    Mtr = [[Fraction(0)] * 6 for _ in range(6)]
    for x, (a1, b1) in enumerate(states):
        for y, (b2, c2) in enumerate(states):
            if b2 == b1:
                Mtr[x][y] = c_alpha if a1 != c2 else c_beta
    paper_pattern = [[0, "b", 0, 0, "a", 0], ["b", 0, 0, "a", 0, 0], ["a", 0, 0, "b", 0, 0],
                     [0, 0, "b", 0, 0, "a"], [0, 0, "a", 0, 0, "b"], [0, "a", 0, 0, "b", 0]]
    paper_M = [[c_alpha if x == "a" else c_beta if x == "b" else Fraction(0) for x in rw]
               for rw in paper_pattern]
    Msp = sp.Matrix(6, 6, lambda a, c: sp.Rational(Mtr[a][c].numerator, Mtr[a][c].denominator))
    lam = sp.Symbol("x")
    charpoly = sp.factor(Msp.charpoly(lam).as_expr())
    eig = {str(k): v for k, v in Msp.eigenvals().items()}

    def delta(k):
        return Fraction(1, 15 ** k) + 2 * Fraction(1, (-5) ** k) + 2 * Fraction(1, (-3) ** k)

    def lam_k(k):
        return Fraction(4 ** k, 2 * k)

    trace_ok = True
    Mk = [[Fraction(int(a == c)) for c in range(6)] for a in range(6)]
    for k in range(1, 31):
        Mk = [[sum(Mk[a][q] * Mtr[q][c] for q in range(6)) for c in range(6)] for a in range(6)]
        tr = sum(Mk[a][a] for a in range(6))
        if tr != Fraction(1, 2 ** k) * (1 + delta(k)):
            trace_ok = False
        # E(Y X_k)/EY -> (1/2k) 8^k Tr(M^k) = lambda_k (1 + delta_k)
        if Fraction(8 ** k, 2 * k) * tr != lam_k(k) * (1 + delta(k)):
            trace_ok = False
    bound = Fraction(1, 225) + Fraction(2, 25) + Fraction(2, 9)
    item5["a_delta_k_(2.2)"] = {
        "source": "transition matrix rebuilt here from the state rule (Section 3) with "
                  "c_alpha=(1+1)^3/30, c_beta=((1+1)^3-1)/30 (generating functions at the saddle x=1, "
                  "taken from the paper's derivation); lambda_k = 4^k/(2k) taken from the paper/[17]",
        "c_alpha": str(c_alpha), "c_beta": str(c_beta),
        "matrix_equals_paper_printed_matrix": Mtr == paper_M,
        "charpoly_factored": str(charpoly),
        "eigenvalues_with_multiplicity": eig,
        "Tr(M^k) == 2^-k (1+delta_k) and 8^k Tr(M^k)/(2k) == lambda_k (1+delta_k), k=1..30": trace_ok,
        "delta_1": str(delta(1)),
        "max_|delta_k|_k>=2_bound": str(bound),
        "|delta_k|<=bound<1 for k=2..60": all(abs(delta(k)) <= bound for k in range(2, 61)) and bound < 1,
        "verdict": verdict(Mtr == paper_M and trace_ok and delta(1) == -1 and bound < 1),
    }
    # (b) (2.3): exp(sum lambda_k delta_k^2) closed form
    terms = [(Fraction(4, 225), 1), (Fraction(-4, 45), 4), (Fraction(-4, 75), 4),
             (Fraction(4, 9), 4), (Fraction(4, 15), 8), (Fraction(4, 25), 4)]
    expand_ok = all(lam_k(k) * delta(k) ** 2
                    == Fraction(1, 2 * k) * sum(c * x ** k for x, c in terms) for k in range(1, 41))
    prod_terms = Fraction(1)
    for x, c in terms:
        prod_terms *= (1 - x) ** c
    paper_inner = (Fraction(221, 225) * Fraction(49, 45) ** 4 * Fraction(79, 75) ** 4 * Fraction(5, 9) ** 4
                   * Fraction(11, 15) ** 8 * Fraction(21, 25) ** 4)
    # exp(sum) = prod (1-x)^(-c/2)  =>  exp(2 sum) = 1/prod_terms
    exp2sum_fac = factor_frac(1 / prod_terms)
    closed_match = fac_eq(exp2sum_fac, PAPER["ratio_const_sq"])
    mpmath.mp.dps = 50
    partial = mpmath.fsum(mpmath.mpf(4) ** k / (2 * k) * (mpmath.mpf(15) ** -k + 2 * mpmath.mpf(-5) ** -k
                                                          + 2 * mpmath.mpf(-3) ** -k) ** 2
                          for k in range(1, 401))
    closed_val = mpmath.log(mpmath.mpf(3) ** 13 * mpmath.mpf(5) ** 13
                            / (mpmath.mpf(7) ** 6 * mpmath.mpf(11) ** 4 * mpmath.mpf(79) ** 2
                               * mpmath.sqrt(13 * 17)))
    item5["b_sum_lambda_delta_sq_(2.3)"] = {
        "source": "recomputed: series expansion, -1/2 ln(1-x) identity, exact product",
        "lambda_k_delta_k^2 == (1/2k) sum c x^k (6 geometric terms), k=1..40": expand_ok,
        "paper_intermediate_product_equals_prod_(1-x)^c": paper_inner == prod_terms,
        "prod_(1-x)^c_factorisation": fac_str(factor_frac(prod_terms)),
        "exp(2*sum)_factorisation": fac_str(exp2sum_fac),
        "paper_(2.3)_squared": fac_str(PAPER["ratio_const_sq"]),
        "verdict": verdict(expand_ok and paper_inner == prod_terms and closed_match),
        "numeric_cross_check_mpmath": {
            "partial_sum_k<=400": mpmath.nstr(partial, 30),
            "ln(3^13 5^13/(7^6 11^4 79^2 sqrt(221)))": mpmath.nstr(closed_val, 30),
            "abs_diff": mpmath.nstr(abs(partial - closed_val), 5),
            "exp_value": mpmath.nstr(mpmath.exp(closed_val), 20),
        },
    }
    # (c) (2.4) from Lemma 3.1 via Stirling (recomputed), saddle-point variance recomputed
    coeffs = {1: 5, 2: 10, 3: 10, 4: 5}                 # (x+1)^5 - x^5 - 1
    tot = sum(coeffs.values())
    mean = Fraction(sum(k * c for k, c in coeffs.items()), tot)
    var2 = Fraction(sum(k * k * c for k, c in coeffs.items()), tot) - mean ** 2
    # N ~ 30^(n/3) / sqrt(2 pi (n/3) var2) = c_N (pi n)^(-1/2) 30^(n/3) with c_N^2 = 3/(2 var2)
    cN_sq = Fraction(3) / (2 * var2)
    multinom = a_stirling(1) / a_stirling(Fraction(1, 3)) ** 3
    P_size = a_stirling(5) / (a_base(2, Fraction(5, 2)) * a_stirling(Fraction(5, 2)))
    A_n = (a_const(3) * a_const(2, Fraction(1, 2)) * a_const(11, Fraction(-1, 2))
           * Asym(pi_e=Fraction(-1, 2), n_e=Fraction(-1, 2)) * a_base(30, Fraction(1, 3))) ** 3
    EY = multinom * a_stirling(Fraction(5, 6)) ** 3 / P_size * A_n
    C1, k1, B1 = EY.normalised()
    EY_match = (fac_eq(fac_scale(C1, 2), PAPER["EY_const_sq"]) and k1 == -1
                and fac_eq(fac_scale(B1, 2), factor_frac(Fraction(25, 24))))
    # exact finite-n EY (Lemma 3.1 proof, exact formula) vs (2.4): ratio -> 1 (numeric)
    # N = [x^(5n/6)] (5x(1+x)(1+x+x^2))^(n/3) = 5^a sum_k C(a, n/2-k) [x^k](1+x+x^2)^a,  a = n/3
    def coeff_N(n):
        a = n // 3
        binp = flint.fmpz_poly([1, 1]) ** a
        trip = flint.fmpz_poly([1, 1, 1]) ** a
        return 5 ** a * sum(int(binp[n // 2 - kk]) * int(trip[kk])
                            for kk in range(max(0, n // 2 - a), min(2 * a, n // 2) + 1))

    mpmath.mp.dps = 60
    finite = []
    for n in (60, 600, 6000, 24000):
        a = n // 3
        Nn = coeff_N(n)
        logEY = (mpmath.loggamma(n + 1) - 3 * mpmath.loggamma(a + 1) + 3 * mpmath.loggamma(5 * n // 6 + 1)
                 + 3 * mpmath.log(mpmath.mpf(Nn))
                 - (mpmath.loggamma(5 * n + 1) - mpmath.mpf(5 * n) / 2 * mpmath.log(2)
                    - mpmath.loggamma(mpmath.mpf(5 * n) / 2 + 1)))
        logasym = (mpmath.log(mpmath.sqrt(mpmath.mpf(2 ** 2 * 3 ** 6 * 5 ** 3) / 11 ** 3))
                   - mpmath.log(2 * mpmath.pi * n) + mpmath.mpf(n) / 2 * mpmath.log(mpmath.mpf(25) / 24))
        ratio = mpmath.exp(logEY - logasym)
        finite.append({"n": n, "EY_exact/EY_(2.4)": mpmath.nstr(ratio, 15),
                       "n*(ratio-1)": mpmath.nstr(n * (ratio - 1), 10)})
    # check the coefficient extraction identity once exactly at small n
    n_small = 60
    direct = (flint.fmpz_poly([0, 5, 10, 10, 5]) ** (n_small // 3))[5 * n_small // 6]
    via = coeff_N(n_small)
    item5["c_EY_(2.4)"] = {
        "source": "recomputed from Lemma 3.1 (statement and exact formula EY = multinomial (5n/6)!^3 N^3/|P_n5|) "
                  "with Stirling; saddle-point variance recomputed",
        "saddle_mean_per_vertex": str(mean),
        "saddle_variance_per_vertex": str(var2),
        "c_N^2 = 3/(2 var) (paper: (3 sqrt2/sqrt11)^2 = 18/11)": str(cN_sq),
        "c_N_matches_paper": cN_sq == Fraction(18, 11),
        "EY_asymptotic_recomputed": EY.describe(),
        "EY_const_squared": fac_str(fac_scale(C1, 2)),
        "paper_(2.4)_const_squared": fac_str(PAPER["EY_const_sq"]),
        "verdict": verdict(EY_match and cN_sq == Fraction(18, 11)),
        "coefficient_identity_N_(n=60)_exact": int(direct) == via,
        "numeric_cross_check_exact_finite_n": finite,
    }
    # (d) h(n) of Lemma 5.1 from (4.7) via Stirling (d-independent part; sum d = 1, sum m = 5)
    h_rec = (a_base(2, Fraction(5, 2)) * a_stirling(Fraction(5, 2)) / a_stirling(5) * a_stirling(1)
             * a_two_pi_n(-162) * a_n_over_e(-1)          # 1/prod_324 (d n)!: d-independent part
             * a_two_pi_n(9) * a_n_over_e(Fraction(5, 2)))  # prod_36 ((m n)!)^(1/2): d-independent part
    h_paper = a_const(2, Fraction(-1, 2)) * a_two_pi_n(PAPER["h_two_pi_n_exp"]) * a_base(5, Fraction(-5, 2))
    item5["d_h(n)_Lemma_5.1"] = {
        "source": "recomputed from (4.7): Stirling for n!, (5n/2)!, (5n)!, 324 factorials (d n)! and "
                  "36 factorials (m n)!^(1/2); the d-dependent leftovers are exactly g(d) e^(n f(d))",
        "h_recomputed": h_rec.describe(),
        "h_paper": h_paper.describe(),
        "verdict": verdict(h_rec == h_paper),
    }
    # (e) Lemma 5.9 constant and (2.5) from the exact det and g (Laplace + Euler-Maclaurin, method
    #     taken from the paper, constants recomputed); conditional on the Maximum Hypothesis.
    absdet_fac = detH_fac
    lap = Asym(const={2: Fraction(NFREE, 2)}, pi_e=Fraction(NFREE, 2), n_e=Fraction(NFREE, 2))  # n^301 (2pi/n)^(301/2)
    L59 = (lap * Asym(const=g_fac) * Asym(const=fac_scale(absdet_fac, Fraction(-1, 2)))
           * a_base(5, Fraction(5, 2)) * a_base(Fraction(25, 24)))
    L59_paper = (Asym(const=fac_scale(PAPER["L59_const_sq"], Fraction(1, 2))) * a_two_pi_n(Fraction(NFREE, 2))
                 * a_base(Fraction(25, 24)) * a_base(5, Fraction(5, 2)))
    EY2 = h_rec * L59
    C2, k2, B2 = EY2.normalised()
    EY2_paper_fac = fac_scale(PAPER["EY2_const_sq"], Fraction(1, 2))
    EY2_match = fac_eq(C2, EY2_paper_fac) and k2 == -2 and fac_eq(B2, factor_frac(Fraction(25, 24)))
    ratio = EY2 / (EY ** 2)
    Cr, kr, Br = ratio.normalised()
    ratio_match_paper = fac_eq(fac_scale(Cr, 2), PAPER["ratio_const_sq"]) and kr == 0 and Br == {}
    ratio_eq_exp_sum = fac_eq(fac_scale(Cr, 2), exp2sum_fac) and kr == 0 and Br == {}
    item5["e_Lemma_5.9_and_(2.5)"] = {
        "source": "Laplace/Euler-Maclaurin structure (5.25)-(5.27) taken from the paper; g(b), |det H~| "
                  "recomputed above; CONDITIONAL on the Maximum Hypothesis (not checked here)",
        "L59_recomputed": L59.describe(),
        "L59_paper": L59_paper.describe(),
        "L59_verdict": verdict(L59 == L59_paper),
        "EY2_recomputed": EY2.describe(),
        "EY2_const_squared": fac_str(fac_scale(C2, 2)),
        "paper_(2.5)_const_squared": fac_str(PAPER["EY2_const_sq"]),
        "EY2_verdict": verdict(EY2_match),
    }
    item5["f_ratio_E(Y^2)/(EY)^2"] = {
        "source": "ratio of the recomputed (2.5) and (2.4) asymptotics vs recomputed exp(sum lambda_k delta_k^2)",
        "ratio_recomputed": ratio.describe(),
        "ratio_const_squared": fac_str(fac_scale(Cr, 2)),
        "paper_ratio_squared_3^26_5^26/(7^12_11^8_79^4_13_17)": fac_str(PAPER["ratio_const_sq"]),
        "ratio_vs_paper": verdict(ratio_match_paper),
        "ratio_equals_exp(sum_lambda_k_delta_k^2)_(condition_(iv)_with_equality)": verdict(ratio_eq_exp_sum),
        "ratio_float": float(mpmath.exp(closed_val)),
    }
    res["item5_constants"] = item5
    timings["item5_s"] = time.perf_counter() - t0

    # ------------------------------------------------------------------ summary
    res["summary"] = {
        "1_rank_23": res["item1_lemma57"]["rank_M_match_paper_23"],
        "1_pairing_equals_(4.3)": res["item1_lemma57"]["pairing_equals_(4.3)"]["verdict"],
        "1_lemma57_integer_parametrisation": res["item1_lemma57"]["parametrisation"]["lemma57_moreover_form_reproduced"],
        "2_lattice_basis": res["item2_lattice_basis"]["lattice_basis_check"],
        "3_detH": res["item3_hessian"]["detH_vs_paper"],
        "3_detH_computed": res["item3_hessian"]["detH_tilde_exact"]["factorisation"],
        "3_negative_definite": res["item3_hessian"]["negative_definiteness_exact"]["verdict_vs_paper"],
        "4_g_b": res["item4_g_and_w"]["g_b_vs_paper"],
        "4_g_b_computed": res["item4_g_and_w"]["g_b_factorisation"],
        "4_prod_w": res["item4_g_and_w"]["prod_s_w_s_factorisation"],
        "4_e^f(b)": res["item4_g_and_w"]["f_b_exact"]["verdict"],
        "5_delta_k_(2.2)": item5["a_delta_k_(2.2)"]["verdict"],
        "5_sum_lambda_delta^2_(2.3)": item5["b_sum_lambda_delta_sq_(2.3)"]["verdict"],
        "5_EY_(2.4)": item5["c_EY_(2.4)"]["verdict"],
        "5_h(n)_(5.1)": item5["d_h(n)_Lemma_5.1"]["verdict"],
        "5_Lemma_5.9_constant": item5["e_Lemma_5.9_and_(2.5)"]["L59_verdict"],
        "5_EY2_(2.5)": item5["e_Lemma_5.9_and_(2.5)"]["EY2_verdict"],
        "5_ratio_vs_paper": item5["f_ratio_E(Y^2)/(EY)^2"]["ratio_vs_paper"],
        "5_ratio_equals_exp_sum": item5["f_ratio_E(Y^2)/(EY)^2"][
            "ratio_equals_exp(sum_lambda_k_delta_k^2)_(condition_(iv)_with_equality)"],
        "controls": {
            "raw_nullspace_basis_det_is_index^2_times_lattice_det": raw_ratio_is_index_sq,
            "raw_nullspace_basis_index_decimal_digits": len(str(idx_raw)),
            "unconstrained_hessian_indefinite": K5_diag_pos and bK5b < 0,
            "original_row_lattice_index_in_saturation": abs(minorB),
            "lcm_of_parametrisation_constant_denominators": math.lcm(*[v.denominator for v in const.values()]),
        },
        "scope_note": "Non-hypothesis anchors only; (2.5), Lemma 5.9 and condition (iv) are conditional on "
                      "the Maximum Hypothesis, which this script does not test.",
    }

    # ------------------------------------------------------------------ parametrisation file
    param = {
        "description": "Lemma 5.7 parametrisation: d_B = const/6 + sum_F coeff * d_F, integer coefficients. "
                       "Variable index v = 36*(3i+j)+k with s = S[k] (entry order s_{-1,-1}, s_{-1,1}, "
                       "s_{1,-1}, s_{1,1}).",
        "S": [list(s) for s in S],
        "free_indices": F,
        "dependent": [{"index": c, "label": label(c), "const_sixths": const6[c],
                       "coeffs": {str(F[p]): P0[c][p] for p in range(NFREE) if P0[c][p] != 0}}
                      for c in B],
        "generated_by": "code/anchors_lemma58.py",
    }
    OUT_PARAM.write_text(json.dumps(param, indent=1) + "\n")
    res["item1_lemma57"]["parametrisation"]["file_sha256"] = sha256_file(OUT_PARAM)

    res["timings_seconds"] = {k: round(v, 3) for k, v in timings.items()}
    res["runtime_seconds_total"] = round(time.perf_counter() - t_start, 3)
    res["peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on macOS
    res["versions"] = {
        "python": sys.version.split()[0],
        "python-flint": flint.__version__,
        "sympy": sp.__version__,
        "mpmath": mpmath.__version__,
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "platform": platform.platform(),
        "flint_threads": flint.ctx.threads,
    }
    res["hashes"] = {
        "script_sha256": sha256_file(__file__),
        "source_pdf_sha256": sha256_file(SRC_PDF),
        "source_layout_txt_sha256": sha256_file(SRC_TXT),
    }
    res["date_end"] = host_date()
    OUT_MAIN.write_text(json.dumps(res, indent=1, default=str) + "\n")
    print(json.dumps(res["summary"], indent=1))
    print("runtime_s", res["runtime_seconds_total"], "peak_rss_bytes", res["peak_rss_bytes"])


if __name__ == "__main__":
    main()
