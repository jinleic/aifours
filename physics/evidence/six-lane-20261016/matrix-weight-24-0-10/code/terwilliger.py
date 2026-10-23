"""Nonbinary Terwilliger-algebra block diagonalization (Gijswijt-Schrijver-Tanaka 2006),
as used by Angles Munne-Huber (arXiv:2603.19901, Eqs. (27)-(31), (41)-(42)).

Orbit variables x[i,j,t,p]: pairs (u,v) of words in F_q^n with |S(u)|=i, |S(v)|=j,
|S(u) & S(v)|=t, #{l: u_l = v_l != 0} = p.

gamma(i,j,t,p) = number of ordered pairs in the orbit.
Block theorem: sum x M_{ij}^{tp} >= 0  iff for all 0<=a<=k<=n+a-k,
   ( sum_{t,p} alpha(i,j,t,p,a,k) x[i,j,t,p] )_{i,j=k..n+a-k} >= 0.
"""
from functools import lru_cache
from math import comb as _comb, factorial


def C(a, b):
    if a < 0 or b < 0 or b > a:
        return 0
    return _comb(a, b)


def I_set(n):
    return [(i, j, t, p) for i in range(n + 1) for j in range(n + 1)
            for t in range(min(i, j) + 1) for p in range(t + 1) if i + j <= t + n]


def gamma(i, j, t, p, n, q=4):
    return ((q - 1) ** (i + j - t) * (q - 2) ** (t - p) * factorial(n)
            // (factorial(p) * factorial(t - p) * factorial(i - t) * factorial(j - t)
                * factorial(n - i - j + t)))


@lru_cache(maxsize=None)
def beta(m, t, i, j, k):
    s = 0
    for u in range(0, m + 1):
        s += (-1) ** ((t - u) % 2) * C(u, t) * C(m - 2 * k, m - k - u) * C(m - k - u, i - u) * C(m - k - u, j - u)
    return s


def alpha(i, j, t, p, a, k, n, q=4):
    """Returns (integer_part, sqrt_power_flag): value = integer_part * (q-1)**((i+j)/2 - t).
    We return a float and also the exact pieces (rational coefficient, exponent of sqrt(q-1))."""
    b = beta(n - a, t - a, i - a, j - a, k - a)
    if b == 0:
        return 0.0, 0, 0
    s = 0
    for g in range(0, p + 1):
        s += (-1) ** ((a - g) % 2) * C(a, g) * C(t - a, p - g) * (q - 2) ** (t - a - p + g)
    coeff = b * s
    # (q-1)^((i+j)/2 - t): exponent in half-units
    half_exp = (i + j) - 2 * t   # exponent of sqrt(q-1)
    val = coeff * (q - 1) ** (half_exp / 2.0)
    return val, coeff, half_exp


def blocks_index(n):
    out = []
    for a in range(0, n + 1):
        for k in range(a, n + 1):
            if k <= n + a - k:
                out.append((a, k))
    return out
