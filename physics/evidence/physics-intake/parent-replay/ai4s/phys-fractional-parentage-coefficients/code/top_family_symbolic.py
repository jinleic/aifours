"""Symbolic-in-v derivation of seniority-reduced one-body CFPs along the top families
L = f*v - k of N identical spin-f bosons (independent re-implementation in "deficit"
coordinates; exact rational-function arithmetic with sympy).

A degree-n monomial with S_z = f*n - k is z_f^(n-|d|) prod_{j>=1} z_(f-j)^(d_j) with
sum_j j d_j = k (the deficit partition d; |d| = sum_j d_j).  For n >= k every partition
occurs, so a highest-weight vector is a vector of coefficients indexed by the (finitely
many, n-independent) partitions d.  In these coordinates
  S+ : z_(f-j) -> j z_(f-j+1)                          (n-independent, f-independent)
  P  : pairs (z_m, z_-m) have deficits (j, 2f-j)       (only acts when k >= 2f)
  <z^a, z^a> = (n-|d|)! prod_j d_j! w_(f-j)^(d_j),  w_(f-j) = 1/binom(2f, j).
CG: <f mu; L' L' | L L>^2 = prod_{i<j} (2L'-i)/(2L+2+i), j = f - mu = k - k'.
Hence every reduced CFP r^2(v) is a rational function of v (and of f when k < 2f).

Usage:
  $PY code/top_family_symbolic.py f KMAX         # integer f, e.g. "2 8"
  $PY code/top_family_symbolic.py general KMAX   # symbolic f, families with k < 2f
"""
from __future__ import annotations

import itertools
import json
import os
import sys

import sympy as sp

v = sp.Symbol('v', positive=True)
fs = sp.Symbol('f', positive=True)


def partitions_weighted(k, J):
    """Tuples (d_1..d_J) with sum j d_j = k."""
    out = []

    def rec(j, rem, acc):
        if j == 0:
            if rem == 0:
                out.append(tuple(reversed(acc)))
            return
        for dj in range(rem // j, -1, -1):
            rec(j - 1, rem - j * dj, acc + [dj])

    rec(J, k, [])
    return sorted(out)


class Deficit:
    def __init__(self, f, J):
        """f: int or sympy Symbol; J: number of deficit slots kept (2f for integer f)."""
        self.f = f
        self.J = J
        self.symbolic = not isinstance(f, int)

    def w(self, j):
        """Squared norm weight of orbital m = f - j (w_f = 1)."""
        if j == 0:
            return sp.Integer(1)
        return sp.factorial(j) / sp.ff(2 * self.f, j)

    # ---- operators on {d: coeff} at degree n, deficit k ----
    def splus(self, p):
        out = {}
        for d, c in p.items():
            for j in range(1, self.J + 1):
                if d[j - 1]:
                    nd = list(d)
                    nd[j - 1] -= 1
                    if j >= 2:
                        nd[j - 2] += 1
                    nd = tuple(nd)
                    out[nd] = out.get(nd, 0) + c * j * d[j - 1]
        return {d: sp.expand(c) for d, c in out.items() if sp.expand(c) != 0}

    def pair_ann(self, p, n):
        """P on degree-n polynomial (integer f only)."""
        assert not self.symbolic
        f = self.f
        out = {}
        for d, c in p.items():
            a_f = n - sum(d)
            for j in range(0, f + 1):
                m = f - j
                jj = 2 * f - j
                if j == 0:
                    if d[jj - 1] == 0:
                        continue
                    coef = 2 * (-1) ** m * self.w(0) * a_f * d[jj - 1]
                    nd = list(d)
                    nd[jj - 1] -= 1
                elif j == f:
                    if d[j - 1] < 2:
                        continue
                    coef = self.w(j) * d[j - 1] * (d[j - 1] - 1)
                    nd = list(d)
                    nd[j - 1] -= 2
                else:
                    if d[j - 1] == 0 or d[jj - 1] == 0:
                        continue
                    coef = 2 * (-1) ** m * self.w(j) * d[j - 1] * d[jj - 1]
                    nd = list(d)
                    nd[j - 1] -= 1
                    nd[jj - 1] -= 1
                nd = tuple(nd)
                out[nd] = out.get(nd, 0) + c * coef
        return {d: sp.expand(c) for d, c in out.items() if sp.expand(c) != 0}

    def pair_cre(self, p):
        assert not self.symbolic
        f = self.f
        out = {}
        for d, c in p.items():
            for j in range(0, f + 1):
                m = f - j
                jj = 2 * f - j
                nd = list(d)
                if j == 0:
                    coef = 2 * (-1) ** m / self.w(0)
                    nd[jj - 1] += 1
                elif j == f:
                    coef = 1 / self.w(j)
                    nd[j - 1] += 2
                else:
                    coef = 2 * (-1) ** m / self.w(j)
                    nd[j - 1] += 1
                    nd[jj - 1] += 1
                nd = tuple(nd)
                out[nd] = out.get(nd, 0) + c * coef
        return {d: sp.expand(c) for d, c in out.items() if sp.expand(c) != 0}

    def mul(self, p, q):
        out = {}
        for d, c in p.items():
            for e, b in q.items():
                nd = tuple(x + y for x, y in zip(d, e))
                out[nd] = out.get(nd, 0) + c * b
        return {d: sp.expand(c) for d, c in out.items() if sp.expand(c) != 0}

    def mul_z(self, p, j):
        """Multiply by z_(f-j)."""
        if j == 0:
            return dict(p)
        out = {}
        for d, c in p.items():
            nd = list(d)
            nd[j - 1] += 1
            out[tuple(nd)] = c
        return out

    def inner(self, p, q, n, k):
        """<p, q> / (n-k)! for degree-n, deficit-k polynomials (exact rational function)."""
        s = 0
        for d, c in p.items():
            b = q.get(d)
            if b is None:
                continue
            wt = sp.rf(n - k + 1, k - sum(d))
            for j, dj in enumerate(d, start=1):
                if dj:
                    wt *= sp.factorial(dj) * self.w(j) ** dj
            s += c * b * wt
        return sp.factor(sp.expand(s))

    # ---- states ----
    def hw_kernel(self, n, k, harmonic=True, max_parts=None):
        """Basis (over Q(v)) of highest-weight (and harmonic if requested) deficit-k vectors.

        max_parts: for a fixed small integer degree n, keep only partitions with |d| <= n."""
        cols = [d for d in partitions_weighted(k, self.J) if max_parts is None or sum(d) <= max_parts]
        rows = {}
        for i, d in enumerate(cols):
            for nd, c in self.splus({d: sp.Integer(1)}).items():
                rows.setdefault(('S', nd), len(rows))
        if harmonic and not self.symbolic and k >= 2 * self.f:
            for i, d in enumerate(cols):
                for nd, c in self.pair_ann({d: sp.Integer(1)}, n).items():
                    rows.setdefault(('P', nd), len(rows))
        M = sp.zeros(len(rows), len(cols))
        for i, d in enumerate(cols):
            for nd, c in self.splus({d: sp.Integer(1)}).items():
                M[rows[('S', nd)], i] += c
            if harmonic and not self.symbolic and k >= 2 * self.f:
                for nd, c in self.pair_ann({d: sp.Integer(1)}, n).items():
                    M[rows[('P', nd)], i] += c
        ns = M.nullspace(simplify=True) if M.rows else [sp.eye(len(cols))[:, i] for i in range(len(cols))]
        out = []
        for vec in ns:
            vec = sp.Matrix([sp.factor(x) for x in vec])
            den = sp.lcm([sp.fraction(sp.together(x))[1] for x in vec])
            vec = [sp.factor(sp.cancel(x * den)) for x in vec]
            out.append({d: c for d, c in zip(cols, vec) if c != 0})
        return out


def cg2(f, L, Lp, j):
    """<f mu; L' L' | L L>^2 with j = f - mu."""
    r = sp.Integer(1)
    for i in range(j):
        r *= (2 * Lp - i) / (2 * L + 2 + i)
    return r


def large_sign(expr):
    """Sign of a rational function of (v, f) for large v and f (asymptotic sign; callers
    check separately that no factor changes sign on the integer domain used)."""
    val = sp.sympify(expr).subs({v: 10 ** 9, fs: 10 ** 6})
    return int(sp.sign(val))


def leading_sign_fix(p):
    """Phase rule: coefficient of the partition with lexicographically largest
    (d_J, ..., d_1) is positive (for large v)."""
    key = max(p, key=lambda d: tuple(reversed(d)))
    return {d: -x for d, x in p.items()} if large_sign(p[key]) < 0 else p


def reduced_cfp2(D, psi, k, phi, kp, f):
    """r^2 for parent psi (degree v, deficit k) and daughter phi (degree v-1, deficit kp)."""
    j = k - kp
    if not (0 <= j <= 2 * f if not D.symbolic else 0 <= j):
        return sp.Integer(0), 0
    L = f * v - k
    Lp = f * (v - 1) - kp
    X = D.inner(psi, D.mul_z(phi, j), v, k)
    Np = D.inner(psi, psi, v, k)
    Nd = D.inner(phi, phi, v - 1, kp)
    shift = kp + 1 - k   # (v-k)!/(v-1-kp)!
    fac = sp.ff(v - k, shift) if shift >= 0 else 1 / sp.ff(v - 1 - kp, -shift)
    val = sp.factor(sp.cancel(X ** 2 * fac / (D.w(j) * Np * Nd * v * cg2(f, L, Lp, j))))
    sgn_cg = -1 if (j % 2) else 1   # (-1)^(f - mu) = (-1)^j
    return val, large_sign(X) * sgn_cg, sp.factor(X)


def run_general(kmax):
    """Symbolic f: families k < 2f (no harmonic constraint), multiplicity-free ones."""
    D = Deficit(fs, kmax)
    states = {}
    for k in range(0, kmax + 1):
        ker = D.hw_kernel(v, k, harmonic=False)
        states[k] = [leading_sign_fix(p) for p in ker]
    res = {}
    for k in range(1, kmax + 1):
        if len(states[k]) != 1:
            continue
        for kp in range(max(0, k - 2 * kmax), k + 1):
            if kp not in states or len(states[kp]) != 1:
                continue
            val, sg, X = reduced_cfp2(D, states[k][0], k, states[kp][0], kp, fs)
            if X != 0:   # sign certified on v >= max(k, k'+1), f >= k//2 + 1 (so k < 2f)
                assert certified_sign(X, max(k, kp + 1), k // 2 + 1) == large_sign(X), (k, kp)
            res[(k, kp)] = (val, sg)
    return states, res


def pair_first_k4(D, n):
    """Spin f >= 3, deficit 4 (two states, both seniority n): Gram-Schmidt at degree n of
    phi_A = z_f^(n-2) Q4 then phi_B = z_f^(n-4) H2^2, where Q4 = z_f z_(f-4) - 4 z_(f-1) z_(f-3)
    + 3 z_(f-2)^2 and H2 = z_f z_(f-2) - z_(f-1)^2 (degree-2 highest-weight pairs of spin 2f-4,
    2f-2; phases by leading_sign_fix).  Returns [A, B - t A] with t = (f-1)(2f-3)/g(n),
    g(n) = f(2f-1)n + 3(4f^2-10f+5); the residual keeps its inherited sign (no re-phasing),
    and both are normalised later with positive factors."""
    (Q4,) = D.hw_kernel(2, 4, harmonic=False, max_parts=2)
    (H2,) = D.hw_kernel(2, 2, harmonic=False, max_parts=2)
    A = leading_sign_fix(Q4)
    H2 = leading_sign_fix(H2)
    Bv = D.mul(H2, H2)
    cf = sp.cancel(D.inner(A, Bv, n, 4) / D.inner(A, A, n, 4))
    B2 = {d: sp.factor(sp.cancel(Bv.get(d, 0) - cf * A.get(d, 0))) for d in set(A) | set(Bv)}
    B2 = {d: c for d, c in B2.items() if c != 0}
    return [A, B2]

def certified_sign(expr, v0, f0):
    """Sign of a rational function of (v, f) on the domain v >= v0, f >= f0 (reals), certified
    factor by factor.  Every irreducible factor must be of degree <= 1 in v: p = a(f) v + b(f),
    where a(f) and p(v0, f) have no real root >= f0 and agree in sign (or a = 0).  Raises
    AssertionError otherwise.  Returns +1 or -1."""
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    sign = 1

    def const_sign(g):
        g = sp.Poly(g, fs)
        if g.degree() <= 0:
            return int(sp.sign(g.as_expr()))
        assert all(r < f0 for r in g.real_roots()), ("root in domain", g)
        return int(sp.sign(g.as_expr().subs(fs, f0)))

    for poly in (num, den):
        c, facs = sp.factor_list(sp.Poly(poly, v, fs))
        sign *= int(sp.sign(c))
        for fac, m in facs:
            p = fac.as_expr()
            assert sp.Poly(p, v).degree() <= 1, ("non-linear in v", p)
            a = sp.Poly(p, v).coeff_monomial(v)
            sb = const_sign(sp.expand(p.subs(v, v0)))
            if a != 0:
                assert const_sign(a) == sb, ("factor may change sign", p)
            sign *= sb ** m
    return sign



def run_general_k4():
    """Symbolic (v, f), f >= 3: all reduced CFPs of the k = 4 family (multiplicity 2) in the
    pair-first basis, into the daughters k' = 0, 2, 3 and the k' = 4 pair-first states."""
    D = Deficit(fs, 4)
    states = {k: [leading_sign_fix(p) for p in D.hw_kernel(v, k, harmonic=False)] for k in (0, 2, 3)}
    parents = pair_first_k4(D, v)
    daughters = {0: states[0], 2: states[2], 3: states[3], 4: pair_first_k4(D, v - 1)}
    res = {}
    for i, psi in enumerate(parents, start=1):
        for kp, ds in daughters.items():
            for jd, phi in enumerate(ds, start=1):
                val, sg, X = reduced_cfp2(D, psi, 4, phi, kp, fs)
                if X != 0:   # sign of X certified on v >= 5, f >= 3 (not just asymptotically)
                    assert certified_sign(X, 5, 3) == large_sign(X), (i, kp, jd)
                res[(i, kp, jd if kp == 4 else 0)] = (val, sg)
    for i in (1, 2):   # symbolic completeness of each parent row
        assert sp.simplify(sum(val for key, (val, _) in res.items() if key[0] == i) - 1) == 0, i
    return res


def integer_roots(expr, v0):
    """Integer roots >= v0 of numerator or denominator of a rational function of v."""
    bad = set()
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    for poly in (num, den):
        for fac, _ in sp.factor_list(sp.Poly(poly, v))[1]:
            if fac.degree() == 1:
                a, b = fac.all_coeffs()
                root = sp.Rational(-b, a)
                if root.q == 1 and root >= v0:
                    bad.add(int(root))
    return bad


def max_real_root(expr):
    """Largest real root (exact) of numerator or denominator of a rational function of v,
    or None.  The sign of expr is constant on (max_real_root, oo)."""
    roots = []
    num, den = sp.fraction(sp.factor(sp.together(expr)))
    for poly in (num, den):
        P = sp.Poly(poly, v)
        if P.degree() > 0:
            roots += P.real_roots()
    return max(roots) if roots else None


# ---------------------------------------------------------------- spin 2 ------------
def f2_labels(k):
    """Missing-label values e for the family L = 2v - k (v >= k): e <= k/6, k - 6e != 1."""
    return [e for e in range(k // 6 + 1) if k - 6 * e != 1]


class Spin2Families:
    def __init__(self):
        self.D = Deficit(2, 4)
        D = self.D
        (H,) = D.hw_kernel(2, 2, max_parts=2)
        (T,) = D.hw_kernel(3, 3, max_parts=3)
        (J,) = D.hw_kernel(3, 6, max_parts=3)
        self.H, self.T, self.J = (leading_sign_fix(p) for p in (H, T, J))
        self._basis = {}

    def harm_proj(self, p, n, k):
        D = self.D
        out = dict(p)
        q = p
        coef = sp.Integer(1)
        i = 0
        while 4 * (i + 1) <= k:
            i += 1
            q = D.pair_ann(q, n - 2 * (i - 1))
            if not q:
                break
            coef = coef * sp.Integer(-1) / (2 * i * (5 + 2 * n - 2 - 2 * i))
            t = q
            for _ in range(i):
                t = D.pair_cre(t)
            for d, c in t.items():
                out[d] = out.get(d, 0) + coef * c
        return {d: sp.factor(sp.cancel(c)) for d, c in out.items() if sp.cancel(c) != 0}

    def covariant(self, k, e):
        """Deficit polynomial of H^b T^c J^e for the family k (the f^a factor is implicit)."""
        c = (k - 6 * e) % 2
        b = (k - 6 * e - 3 * c) // 2
        p = {(0, 0, 0, 0): sp.Integer(1)}
        for _ in range(b):
            p = self.D.mul(p, self.H)
        if c:
            p = self.D.mul(p, self.T)
        for _ in range(e):
            p = self.D.mul(p, self.J)
        return p

    def basis(self, k, n, order="asc"):
        """[(e, psi_e)] Gram-Schmidt of projected covariants, degree n; order "asc" (e = 0
        first, the convention of spin2_basis.py) or "desc" (largest e, i.e. most trios, first)."""
        key = (k, n, order)
        if key in self._basis:
            return self._basis[key]
        D = self.D
        out = []
        labs = f2_labels(k)
        for e in (labs if order == "asc" else labs[::-1]):
            w = self.harm_proj(self.covariant(k, e), n, k)
            for _, u in out:
                cf = sp.cancel(D.inner(u, w, n, k) / D.inner(u, u, n, k))
                for d, x in u.items():
                    w[d] = sp.cancel(w.get(d, 0) - cf * x)
                w = {d: sp.factor(x) for d, x in w.items() if x != 0}
            # certify: highest weight and harmonic identically in v
            assert not {d: c for d, c in D.splus(w).items() if sp.cancel(c) != 0}, (k, e)
            assert not {d: c for d, c in D.pair_ann(w, n).items() if sp.cancel(c) != 0}, (k, e)
            out.append((e, w))
        self._basis[key] = out
        return out


def run_f2(kmax, table_path=None, order="asc"):
    S = Spin2Families()
    D = S.D
    res = []
    for k in range(0, kmax + 1):
        if not f2_labels(k):
            continue
        for e, psi in S.basis(k, v, order):
            for kp in range(max(0, k - 4), k + 1):
                if not f2_labels(kp):
                    continue
                for ep, phi in S.basis(kp, v - 1, order):
                    val, sg, X = reduced_cfp2(D, psi, k, phi, kp, 2)
                    v0 = max(k, kp + 1, 1)
                    divisors = [D.inner(psi, psi, v, k), D.inner(phi, phi, v - 1, kp),
                                cg2(2, 2 * v - k, 2 * (v - 1) - kp, k - kp)]
                    bad = set()
                    for dv in divisors:
                        bad |= integer_roots(dv, v0)
                    bad |= integer_roots(X, v0) if X != 0 else set()
                    mr = max_real_root(X) if X != 0 else None
                    sign_from = v0 if (mr is None or mr < v0) else int(sp.floor(mr)) + 1
                    res.append(dict(k=k, e=e, kp=kp, ep=ep, r2=val, sign=sg, v0=v0, bad=sorted(bad),
                                    sign_from=sign_from))
    checked = 0
    if table_path:
        tab = {}
        for r in json.load(open(table_path))["rows"]:
            tab[(r["v"], 2 * r["v"] - r["L"], r["e"], 2 * (r["v"] - 1) - r["Lp"], r["ep"])] = (
                sp.Rational(r["r2"]), r["sign"])
        vmax = max(key[0] for key in tab)
        for row in res:
            for vv in range(row["v0"], vmax + 1):
                if vv in row["bad"]:
                    continue
                key = (vv, row["k"], row["e"], row["kp"], row["ep"])
                num = row["r2"].subs(v, vv)
                ref = tab.get(key, (sp.Integer(0), 0))
                assert num == ref[0], (key, num, ref)
                if num != 0:
                    assert row["sign"] == ref[1], (key, row["sign"], ref)
                checked += 1
    return res, checked


if __name__ == "__main__":
    mode = sys.argv[1]
    kmax = int(sys.argv[2])
    if mode == "general":
        states, res = run_general(kmax)
        for k, st in states.items():
            print(f"k={k}: dim of highest-weight space (generic v, f > k/2) = {len(st)}")
        for (k, kp), (val, sg) in sorted(res.items()):
            print(f"  r^2(k={k} -> k'={kp}) = {val}   sign {sg:+d}")
    elif mode == "2":
        table = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3] != "-" else None
        order = sys.argv[4] if len(sys.argv) > 4 else "asc"
        res, checked = run_f2(kmax, table, order)
        for row in res:
            print(f"k={row['k']} e={row['e']} -> k'={row['kp']} e'={row['ep']}: r^2 = {row['r2']}"
                  f"   sign {row['sign']:+d}   valid v >= {row['v0']}"
                  + (f"  (excluded integer v: {row['bad']})" if row['bad'] else "")
                  + (f"  (sign constant only for v >= {row['sign_from']})"
                     if row['sign_from'] > row['v0'] else ""))
        if table:
            print(f"cross-check vs exact numeric table: {checked} (v, family) values agree exactly")
