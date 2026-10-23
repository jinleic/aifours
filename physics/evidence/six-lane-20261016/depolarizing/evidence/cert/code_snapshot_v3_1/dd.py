"""Vectorized double-double (DD) arithmetic on numpy float64 arrays, IEEE binary64 round-to-nearest.

A DD number is a pair (hi, lo) of float64 arrays representing hi + lo.  Only error-free transformations
(TwoSum, Dekker split/TwoProd) and correctly rounded +,-,*,/ are used, so the code is deterministic and
platform independent (numpy float64 ops are IEEE correctly rounded; no FMA is used anywhere).

Rigorous error model used by cert.py (u = 2^-53, all magnitudes far from overflow/underflow; cert.py asserts
the exponent range at runtime):
  * add(a, b)  : |res - (a+b)| <= EPS_ADD * (|a| + |b|)
  * mul(a, b)  : |res - a*b|   <= EPS_MUL * |a| * |b|
  * mul_d(a, d): |res - a*d|   <= EPS_MUL * |a| * |d|        (d a float64)
  * Inputs carry their own absolute error bounds; cert.py propagates bounds with a separate float64
    magnitude recursion inflated by safety factors (see cert.py).
Derivation sketch (proved in review/PROOFS.md): TwoSum and TwoProd are exact; for add, the neglected
rounding errors are fl(a.lo+b.lo) (<= u|a.lo+b.lo| <= u^2(|a|+|b|)(1+u)) and fl(e + t) (<= u(|e|+|t|) <=
u(u+u^2)(|a|+|b|)*2), and the final quick_two_sum is exact when |s| >= |e|, giving < 4u^2(|a|+|b|).
For mul, neglected terms are a.lo*b.lo (<= u^2|ab|(1+u)^2), and roundings of the two cross products and of
two sums, each <= u * (2u + u^2)|ab|(1+u)^2, giving < 8u^2|a||b|.  We use EPS_ADD = EPS_MUL = 2^-100
(~ 7.9e-31 = 64.5 u^2), a factor > 8 above the derived constants.
"""
from __future__ import annotations

import numpy as np

U = 2.0 ** -53
EPS_ADD = 2.0 ** -100
EPS_MUL = 2.0 ** -100
_SPLIT = 134217729.0  # 2^27 + 1


def two_sum(a, b):
    s = a + b
    bb = s - a
    e = (a - (s - bb)) + (b - bb)
    return s, e


def quick_two_sum(a, b):
    s = a + b
    e = b - (s - a)
    return s, e


def split(a):
    t = _SPLIT * a
    hi = t - (t - a)
    lo = a - hi
    return hi, lo


def two_prod(a, b):
    p = a * b
    ah, al = split(a)
    bh, bl = split(b)
    e = ((ah * bh - p) + ah * bl + al * bh) + al * bl
    return p, e


class DD:
    __slots__ = ("hi", "lo")

    def __init__(self, hi, lo=None):
        self.hi = np.asarray(hi, dtype=np.float64)
        self.lo = np.zeros_like(self.hi) if lo is None else np.asarray(lo, dtype=np.float64)

    def copy(self):
        return DD(self.hi.copy(), self.lo.copy())

    def __getitem__(self, idx):
        return DD(self.hi[idx], self.lo[idx])

    def __setitem__(self, idx, val):
        self.hi[idx] = val.hi
        self.lo[idx] = val.lo

    @property
    def shape(self):
        return self.hi.shape

    def to_float(self):
        return self.hi + self.lo


def add(a: DD, b: DD) -> DD:
    s, e = two_sum(a.hi, b.hi)
    t = a.lo + b.lo
    e = e + t
    hi, lo = quick_two_sum(s, e)
    return DD(hi, lo)


def mul(a: DD, b: DD) -> DD:
    p, e = two_prod(a.hi, b.hi)
    e = e + (a.hi * b.lo + a.lo * b.hi)
    hi, lo = quick_two_sum(p, e)
    return DD(hi, lo)


def mul_d(a: DD, d) -> DD:
    """DD times float64 (array or scalar)."""
    d = np.asarray(d, dtype=np.float64)
    p, e = two_prod(a.hi, d)
    e = e + a.lo * d
    hi, lo = quick_two_sum(p, e)
    return DD(hi, lo)


def outer(a: DD, b: DD) -> DD:
    """outer product of two DD vectors (one DD multiplication per entry)."""
    A = DD(np.broadcast_to(a.hi[:, None], (a.hi.shape[0], b.hi.shape[0])),
           np.broadcast_to(a.lo[:, None], (a.hi.shape[0], b.hi.shape[0])))
    B = DD(np.broadcast_to(b.hi[None, :], (a.hi.shape[0], b.hi.shape[0])),
           np.broadcast_to(b.lo[None, :], (a.hi.shape[0], b.hi.shape[0])))
    return mul(A, B)


def sqrt_int(m) -> DD:
    """DD enclosure-quality sqrt of nonnegative integers m < 2^52 (exactly representable).

    s = fl(sqrt(m)); r = m - s^2 computed exactly via two_prod; correction c = r/(2s).
    Relative error <= 3u^2 (Newton step from a correctly rounded seed); m = 0 -> 0.
    """
    m = np.asarray(m, dtype=np.float64)
    s = np.sqrt(m)
    p, e = two_prod(s, s)
    r = (m - p) - e  # exact: m - p is exact (Sterbenz, p within 1 ulp of m); then one rounding
    with np.errstate(divide="ignore", invalid="ignore"):
        c = np.where(s > 0, r / (2.0 * s), 0.0)
    hi, lo = quick_two_sum(s, c)
    return DD(hi, lo)


def recip_int(m) -> DD:
    """DD approximation of 1/m for positive integers m < 2^52; relative error <= 3u^2."""
    m = np.asarray(m, dtype=np.float64)
    x = 1.0 / m
    p, e = two_prod(m, x)
    r = (1.0 - p) - e
    c = r * x
    hi, lo = quick_two_sum(x, c)
    return DD(hi, lo)
