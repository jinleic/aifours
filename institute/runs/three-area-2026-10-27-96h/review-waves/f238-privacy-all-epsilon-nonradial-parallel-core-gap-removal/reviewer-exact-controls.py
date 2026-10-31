#!/usr/bin/env python3
"""Reviewer-owned exact arithmetic checks; no author code is imported."""
from collections import defaultdict
from fractions import Fraction as Q
from math import comb, factorial

# Coefficients of a polynomial in (t, radius, mean, I).
class P:
    def __init__(self, terms=None):
        self.c = {e: Q(a) for e, a in (terms or {}).items() if a}

    @staticmethod
    def scalar(a):
        return P({(0, 0, 0, 0): Q(a)})

    @staticmethod
    def basis(k):
        e = [0] * 4
        e[k] = 1
        return P({tuple(e): Q(1)})

    def __add__(self, other):
        other = other if isinstance(other, P) else P.scalar(other)
        z = defaultdict(Q, self.c)
        for e, a in other.c.items():
            z[e] += a
        return P(z)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -a for e, a in self.c.items()})

    def __sub__(self, other):
        return self + (-other if isinstance(other, P) else -Q(other))

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = other if isinstance(other, P) else P.scalar(other)
        z = defaultdict(Q)
        for e, a in self.c.items():
            for f, b in other.c.items():
                z[tuple(x + y for x, y in zip(e, f))] += a * b
        return P(z)

    __rmul__ = __mul__

    def __pow__(self, n):
        out = P.scalar(1)
        for _ in range(n):
            out = out * self
        return out

    def derivative_radius(self):
        z = {}
        for (a, b, c, d), v in self.c.items():
            if b:
                z[(a, b - 1, c, d)] = b * v
        return P(z)

    def translate_radius(self, shift):
        z = defaultdict(Q)
        for (a, b, c, d), v in self.c.items():
            for k in range(b + 1):
                z[(a, k, c, d)] += v * comb(b, k) * Q(shift) ** (b - k)
        return P(z)

    def mean_zero(self):
        return P({e: v for e, v in self.c.items() if e[2] == 0})


def stirling(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def raw_geometric_moment(n, mean):
    # E[(G)_k] = k! mean^k; convert powers using Stirling numbers.
    return sum(stirling(n, k) * factorial(k) * mean ** k for k in range(n + 1))


def shifted_moment(n, radius, mean):
    return sum(comb(n, k) * radius ** (n - k) * raw_geometric_moment(k, mean)
               for k in range(n + 1))


def positive_coefficients(poly):
    bad = [(e, v) for e, v in poly.c.items() if v <= 0]
    if bad:
        raise ValueError('nonpositive coefficient at ' + repr(bad[0]))


t, r, m, I = (P.basis(k) for k in range(4))
H = [shifted_moment(n, r, m) for n in range(5)]
Z = 4*t*t + I + 8*t*H[1] + 2*H[2]


def lower_derivative(endpoint):
    u = endpoint * t * I
    k = t * u
    n = (Q(8, 3)*t**4 + k + (Q(32, 3)*t**3 + u)*H[1]
         + (12*t*t + I)*H[2] + Q(16, 3)*t*H[3] + Q(2, 3)*H[4])
    d = n.derivative_radius()*Z - n*Z.derivative_radius()
    if endpoint == 3:
        d -= Q(4, 3)*t**3*(4*t*t - I)
    return d


certificates = {}
for endpoint in (2, 3):
    original = lower_derivative(endpoint)
    certificates[('tail', endpoint)] = original.translate_radius(1)
    certificates[('uniform', endpoint)] = original.mean_zero()

expected = {('tail', 2): 76, ('tail', 3): 75,
            ('uniform', 2): 12, ('uniform', 3): 11}
for key, p in certificates.items():
    positive_coefficients(p)
    assert len(p.c) == expected[key], (key, len(p.c))
    if key[0] == 'tail':
        assert p.c[(0, 0, 0, 0)] == Q(8, 3)
    else:
        assert p.c[(5, 0, 0, 0)] > 0
        assert p.c[(0, 5, 0, 0)] == Q(8, 3)
    print('POSITIVE', key, 'terms', len(p.c),
          'witness', p.c[(0, 0, 0, 0)] if key[0] == 'tail'
          else (p.c[(5, 0, 0, 0)], p.c[(0, 5, 0, 0)]))

# A deliberately corrupted constant must fail for that exact reason.
try:
    positive_coefficients(certificates[('tail', 2)] - Q(11, 3))
except ValueError as exc:
    assert '(0, 0, 0, 0)' in str(exc) and 'Fraction(-1, 1)' in str(exc)
    print('INTENDED_NEGATIVE constant corruption:', exc)
else:
    raise AssertionError('corrupted coefficient was not detected')

# Independent rational square computations from polynomial coefficients.
a = [Q(1), Q(4), Q(2)]
mu = [Q(1, 6), Q(4, 3), Q(3), Q(8, 3), Q(2, 3)]
b = Q(1, 2)
mean = b / (1 - b)
delta = Q(1, 10)

def at(coeffs, x):
    return sum(v*x**n for n, v in enumerate(coeffs))


def expected_at(coeffs, offset):
    return sum(v*shifted_moment(n, offset, mean) for n, v in enumerate(coeffs))


first_a = at(a, 1 + delta) - at(a, 1)
first_mu = at(mu, 1 + delta) - at(mu, 1)
assert (first_a, first_mu) == (Q(41, 50), Q(9777, 5000))
lower_v = Q(17, 4)
first_upper = first_mu - lower_v*first_a
assert first_upper == -Q(956, 625)
comparator_cost = expected_at(mu, Q(0)) / expected_at(a, Q(0))
assert comparator_cost == Q(571, 66)
weighted_a = b/(1-b) * (expected_at(a, 1+delta) - expected_at(a, 1))
weighted_mu = b/(1-b) * (expected_at(mu, 1+delta) - expected_at(mu, 1))
assert (weighted_a, weighted_mu) == (Q(61, 50), Q(202571, 15000))
weighted_lower = weighted_mu - comparator_cost*weighted_a
assert weighted_lower == Q(486731, 165000) > 0
print('SQUARE', 'first-area', first_a, 'first-moment', first_mu,
      'first-upper', first_upper, 'comparator', comparator_cost,
      'weighted-area', weighted_a, 'weighted-moment', weighted_mu,
      'weighted-lower', weighted_lower)

# A false weaker lower bound is unable to establish the claimed sign.
try:
    false_bound_upper = first_mu - Q(2)*first_a
    if false_bound_upper >= 0:
        raise ValueError('first-shell bound is nonnegative: ' + str(false_bound_upper))
except ValueError as exc:
    assert str(exc).endswith('1577/5000')
    print('INTENDED_NEGATIVE insufficient V bound:', exc)
else:
    raise AssertionError('incorrect first-shell sign was accepted')

# Concrete nonconvex canonical profile and two in-core endpoints.
f = lambda y: Q(1) + (Q(1)-y)**2/2
mid_x, mid_y = Q(5, 4), Q(1, 2)
assert f(Q(0)) == Q(3, 2) and f(Q(1)) == Q(1)
assert f(mid_y) == Q(9, 8) and mid_x > f(mid_y)
print('NONCONVEX midpoint', mid_x, mid_y, 'outside bound', f(mid_y))
print('ALL_REVIEWER_CONTROLS_COMPLETE')
