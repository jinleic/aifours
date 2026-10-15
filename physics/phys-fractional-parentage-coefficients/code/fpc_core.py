"""Exact rational engine for one-body coefficients of fractional parentage (CFPs)
of N identical spin-f bosons in total-spin (and seniority) eigenstates.

Representation (all arithmetic exact, python-flint fmpq):
  * single-boson orbitals eps_m = u^(f+m) v^(f-m), m = -f..f (unnormalised SU(2)
    polynomial basis).  Their squared norms (scaled by 1/(2f)!) are
    w_m = 1/binom(2f, f+m), so S+ eps_m = (f-m) eps_(m+1) has rational entries.
  * an N-boson state is a homogeneous polynomial of degree N in commuting
    variables z_m (z_m creates eps_m), stored as {exponent tuple: fmpq}.
  * Fock inner product: <z^a, z^b> = delta_ab * prod_m a_m! w_m^(a_m).
  * normalised operators: a+_m = z_m / sqrt(w_m),  a_m = sqrt(w_m) d/dz_m.
  * SO(2f+1)-invariant pair: P+ = sum_m (-1)^m a+_m a+_(-m) = sum_m (-1)^m z_m z_-m / w_m,
    P = sum_m (-1)^m a_m a_-m = sum_m (-1)^m w_m d_m d_-m;  [P, P+] = 4 N + 2 D.

CFP convention (Bao & Li 2005 ordering, particle first):
  |N; G L M> = sum_G' cfp(G L; G' L') [ chi(particle N) x |N-1; G' L'> ]_{L M},
  so cfp = (1/sqrt N) <N; G L L | [a+ x |N-1; G' L'>]_{L L}>
         = <N; G L L| a+_mu |N-1; G' L' L'> / (sqrt(N) <f mu; L' L' | L L>),  mu = L - L'.
Squared CFPs are rational; signs are reported separately.
"""
from __future__ import annotations

from math import comb, factorial

from flint import fmpq, fmpz_mat


def _add(d, k, c):
    v = d.get(k)
    if v is None:
        d[k] = c
    else:
        v = v + c
        if v == 0:
            del d[k]
        else:
            d[k] = v


def clean(p):
    return {k: c for k, c in p.items() if c != 0}


def cg_stretched(j1, m1, j2, m2, J):
    """<j1 m1; j2 m2 | J J> for integer spins with m1 + m2 = J.

    Returns (sign, square) with square an fmpq.  Closed formula for the
    stretched component (Varshalovich 8.5); cross-checked against sympy in
    tests (code/selftest.py).
    """
    assert m1 + m2 == J and abs(m1) <= j1 and abs(m2) <= j2
    assert abs(j1 - j2) <= J <= j1 + j2
    sq = fmpq(factorial(2 * J + 1) * factorial(j1 + j2 - J),
              factorial(j1 + j2 + J + 1) * factorial(J + j1 - j2) * factorial(J - j1 + j2))
    sq *= fmpq(factorial(j1 + m1) * factorial(j2 + m2), factorial(j1 - m1) * factorial(j2 - m2))
    sign = -1 if (j1 - m1) % 2 else 1
    return sign, sq


class SpinBosons:
    """Symmetric N-boson states of spin-f particles (D = 2f+1 orbitals)."""

    def __init__(self, f: int):
        assert f >= 1
        self.f = f
        self.D = 2 * f + 1
        self.w = tuple(fmpq(1, comb(2 * f, f + m)) for m in range(-f, f + 1))
        self._mono = {}
        self._mnorm = {}

    # ----- monomial bookkeeping -------------------------------------------------
    def monomials(self, n, M):
        """Sorted exponent tuples of degree n and total S_z weight M."""
        key = (n, M)
        if key in self._mono:
            return self._mono[key]
        f, D = self.f, self.D
        out = []

        def rec(i, rem, wt, acc):
            m = i - f
            if i == D - 1:
                if wt + f * rem == M:
                    out.append(tuple(acc + [rem]))
                return
            for a in range(rem, -1, -1):
                r = rem - a
                wt2 = wt + m * a
                if wt2 + (m + 1) * r <= M <= wt2 + f * r:
                    rec(i + 1, r, wt2, acc + [a])

        if n >= 0:
            rec(0, n, 0, [])
        out.sort()
        self._mono[key] = out
        return out

    def mono_norm(self, a):
        v = self._mnorm.get(a)
        if v is None:
            v = fmpq(1)
            for ai, wi in zip(a, self.w):
                if ai:
                    v *= factorial(ai) * wi ** ai
            self._mnorm[a] = v
        return v

    def inner(self, p, q):
        if len(p) > len(q):
            p, q = q, p
        s = fmpq(0)
        for a, c in p.items():
            d = q.get(a)
            if d is not None:
                s += c * d * self.mono_norm(a)
        return s

    def norm2(self, p):
        return self.inner(p, p)

    # ----- operators --------------------------------------------------------------
    def mul_var(self, p, m):
        i = m + self.f
        out = {}
        for a, c in p.items():
            b = list(a)
            b[i] += 1
            out[tuple(b)] = c
        return out

    def mul(self, p, q):
        out = {}
        for a, c in p.items():
            for b, d in q.items():
                _add(out, tuple(x + y for x, y in zip(a, b)), c * d)
        return out

    def splus(self, p):
        f = self.f
        out = {}
        for a, c in p.items():
            for i in range(self.D - 1):
                ai = a[i]
                if ai:
                    b = list(a)
                    b[i] -= 1
                    b[i + 1] += 1
                    _add(out, tuple(b), c * (ai * (f - (i - f))))
        return out

    def sminus(self, p):
        f = self.f
        out = {}
        for a, c in p.items():
            for i in range(1, self.D):
                ai = a[i]
                if ai:
                    b = list(a)
                    b[i] -= 1
                    b[i - 1] += 1
                    _add(out, tuple(b), c * (ai * (f + (i - f))))
        return out

    def pair_ann(self, p):
        f, w = self.f, self.w
        out = {}
        for a, c in p.items():
            i0 = f
            if a[i0] >= 2:
                b = list(a)
                b[i0] -= 2
                _add(out, tuple(b), c * w[i0] * (a[i0] * (a[i0] - 1)))
            for m in range(1, f + 1):
                ip, im = f + m, f - m
                if a[ip] and a[im]:
                    b = list(a)
                    b[ip] -= 1
                    b[im] -= 1
                    _add(out, tuple(b), c * w[ip] * (2 * (-1) ** m * a[ip] * a[im]))
        return out

    def pair_cre(self, p):
        f, w = self.f, self.w
        out = {}
        for a, c in p.items():
            b = list(a)
            b[f] += 2
            _add(out, tuple(b), c / w[f])
            for m in range(1, f + 1):
                ip, im = f + m, f - m
                b = list(a)
                b[ip] += 1
                b[im] += 1
                _add(out, tuple(b), c * (2 * (-1) ** m) / w[ip])
        return out

    def pair_cre_pow(self, p, n):
        for _ in range(n):
            p = self.pair_cre(p)
        return p

    # ----- harmonic (seniority) projection -----------------------------------------
    def harm_proj(self, p, n):
        """Orthogonal projection of a degree-n polynomial onto ker P (seniority n).

        H(p) = sum_k (-1)^k (P+)^k P^k p / (2^k k! prod_{i=1..k} (D + 2n - 2 - 2i)).
        """
        D = self.D
        out = dict(p)
        q = p
        coef = fmpq(1)
        k = 0
        while True:
            k += 1
            if 2 * k > n:
                break
            q = self.pair_ann(q)
            if not q:
                break
            coef = coef * fmpq(-1, 2 * k * (D + 2 * n - 2 - 2 * k))
            t = self.pair_cre_pow(q, k)
            for a, c in t.items():
                _add(out, a, c * coef)
        return out

    # ----- highest-weight spaces --------------------------------------------------
    def hw_harmonic_basis(self, v, L):
        """Integer basis of {h in Sym^v : weight L, S+ h = 0, P h = 0}."""
        cols = self.monomials(v, L)
        if not cols:
            return []
        rows_sp = {a: i for i, a in enumerate(self.monomials(v, L + 1))}
        rows_p = {a: i for i, a in enumerate(self.monomials(v - 2, L))} if v >= 2 else {}
        nr = len(rows_sp) + len(rows_p)
        if nr == 0:
            return [{a: fmpq(1)} for a in cols]
        # integer matrix: S+ rows (integer) and P rows scaled by binom(2f,f)*binom(2f,f+1)... use lcm
        from math import lcm
        scale = 1
        for wi in self.w:
            scale = lcm(scale, int(wi.q))
        M = [[0] * len(cols) for _ in range(nr)]
        for j, a in enumerate(cols):
            for b, c in self.splus({a: fmpq(1)}).items():
                M[rows_sp[b]][j] = int(c)
            if rows_p:
                for b, c in self.pair_ann({a: fmpq(1)}).items():
                    cc = c * scale
                    assert cc.q == 1
                    M[len(rows_sp) + rows_p[b]][j] = int(cc.p)
        X, nullity = fmpz_mat(M).nullspace()
        basis = []
        for k in range(nullity):
            vec = {}
            for j, a in enumerate(cols):
                x = X[j, k]
                if x != 0:
                    vec[a] = fmpq(int(x))
            basis.append(vec)
        return basis

    # ----- CFP -------------------------------------------------------------------------
    def cfp_sq_sign(self, parent, N, L, daughter, Lp):
        """Squared one-body CFP (fmpq) and sign for unnormalised highest-weight states.

        parent: degree-N polynomial with S_z = L, S+ parent = 0 (total spin L)
        daughter: degree-(N-1) polynomial with S_z = Lp, S+ daughter = 0.
        Returns (0, 0) when (f, Lp, L) violates the triangle rule.
        """
        mu = L - Lp
        if not (abs(mu) <= self.f <= L + Lp):
            return fmpq(0), 0
        x = self.inner(parent, self.mul_var(daughter, mu))
        cgs, cg2 = cg_stretched(self.f, mu, Lp, Lp, L)
        val = x * x / (self.w[mu + self.f] * self.norm2(parent) * self.norm2(daughter) * N * cg2)
        sgn = 0 if x == 0 else (1 if x > 0 else -1) * cgs
        return val, sgn


def frac_str(q):
    q = fmpq(q)
    return str(q.p) if q.q == 1 else f"{q.p}/{q.q}"
