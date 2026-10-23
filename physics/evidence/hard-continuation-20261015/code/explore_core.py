"""Non-rigorous high-precision evaluator used ONLY for candidate exploration.

Nothing in this module is a premise of a certified inequality. It evaluates

    Psi_T(rho, alpha) = -sum_{j=1}^T mu_j^2/j - (k-1) alpha E log(1 - R_1...R_k)

with mu_j = sum_i (-1)^i binom(j,i) M_i, M_i = exp(lambda(nu_i - 1)),
nu_i = E(1-Q)^i, Q = R_2...R_k, lambda = k alpha/2, in nearest-rounded
fixed-point integer arithmetic with T+guard bits, so the alternating sums do
not lose the answer to cancellation. Rounding is not directed here.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial, log1p
from collections import Counter

import mpmath


def multinomial_law(rates, weights, arity):
    """Return dict value->mass for the product of `arity` iid draws (floats)."""
    out = {}
    m = len(rates)
    for combo in combinations_with_replacement(range(m), arity):
        cnt = Counter(combo)
        mass = factorial(arity)
        val = 1.0
        for idx, c in cnt.items():
            mass /= factorial(c)
            mass *= weights[idx] ** c
            val *= rates[idx] ** c
        out[val] = out.get(val, 0.0) + mass
    return out


def multinomial_law_exact(rates, weights, arity):
    out = {}
    m = len(rates)
    for combo in combinations_with_replacement(range(m), arity):
        cnt = Counter(combo)
        mass = Fraction(factorial(arity))
        val = Fraction(1)
        for idx, c in cnt.items():
            mass /= factorial(c)
            mass *= weights[idx] ** c
            val *= rates[idx] ** c
        out[val] = out.get(val, Fraction(0)) + mass
    return out


class Evaluator:
    def __init__(self, k, T, guard=160):
        self.k = k
        self.T = T
        self.P = T + guard
        self.ONE = 1 << self.P
        mpmath.mp.prec = self.P + 40

    def fx(self, x):
        """Float/Fraction -> fixed point integer (nearest)."""
        f = Fraction(x)
        return (f.numerator * self.ONE * 2 + f.denominator) // (2 * f.denominator)

    def site_mu(self, rates, weights, alpha, exact=False):
        k, T, P, ONE = self.k, self.T, self.P, self.ONE
        if exact:
            qlaw = multinomial_law_exact([Fraction(r) for r in rates], [Fraction(w) for w in weights], k - 1)
        else:
            qlaw = multinomial_law(rates, weights, k - 1)
        qs = [(self.fx(1 - Fraction(q)), self.fx(w)) for q, w in qlaw.items()]
        lam = mpmath.mpf(k) * mpmath.mpf(Fraction(alpha).numerator) / mpmath.mpf(Fraction(alpha).denominator) / 2
        powers = [ONE for _ in qs]
        M = []
        for i in range(T + 1):
            nu = sum(w * p for (_, w), p in zip(qs, powers)) >> P
            x = lam * (mpmath.mpf(nu) / ONE - 1)
            M.append(int(mpmath.nint(mpmath.exp(x) * ONE)))
            powers = [(p * b) >> P for (b, _), p in zip(qs, powers)]
        # forward differences: mu_j = ((1-E)^j M)_0
        row = M[:]
        mus = [ONE]
        for j in range(1, T + 1):
            row = [row[i] - row[i + 1] for i in range(len(row) - 1)]
            mus.append(row[0])
        return mus

    def psi(self, rates, weights, alpha, T=None, return_parts=False, exact=False):
        k = self.k
        T = self.T if T is None else T
        mus = self.site_mu(rates, weights, alpha, exact=exact)
        ONE = self.ONE
        site = 0.0
        acc = Fraction(0)
        # accumulate in mpmath for accuracy
        s = mpmath.mpf(0)
        partial = []
        for j in range(1, min(T, self.T) + 1):
            mu = mpmath.mpf(mus[j]) / ONE
            s += mu * mu / j
            partial.append(s)
        clause_law = multinomial_law([float(r) for r in rates], [float(w) for w in weights], k)
        d = 0.0
        for z, w in clause_law.items():
            d += w * log1p(-z)
        a = float(Fraction(alpha))
        corr = -(k - 1) * a * d
        val = float(-s) + corr
        if return_parts:
            return val, float(s), corr, [m / ONE for m in mus], partial
        return val
