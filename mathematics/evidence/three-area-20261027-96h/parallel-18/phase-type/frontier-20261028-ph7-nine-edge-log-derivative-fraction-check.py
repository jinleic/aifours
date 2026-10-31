#!/usr/bin/env python3
"""Stdlib rational coefficient replay for the three block derivative identities.

This verifies algebraic identities as multivariate coefficient dictionaries;
it does not search graphs, generators, or numerical PH states, and is not a
formal proof assistant or an independent mathematical review.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

NVAR = 5
ZERO = (0,) * NVAR


class Poly:
    def __init__(self, terms=None):
        self.terms = {k: F(v) for k, v in (terms or {}).items() if v}

    @staticmethod
    def value(x):
        return x if isinstance(x, Poly) else Poly({ZERO: F(x)})

    def __add__(self, other):
        out = dict(self.terms)
        for key, value in self.value(other).terms.items():
            out[key] = out.get(key, F(0)) + value
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.terms.items()})

    def __sub__(self, other):
        return self + -self.value(other)

    def __rsub__(self, other):
        return self.value(other) - self

    def __mul__(self, other):
        out = {}
        for a, b in product(self.terms.items(), self.value(other).terms.items()):
            key = tuple(x + y for x, y in zip(a[0], b[0]))
            out[key] = out.get(key, F(0)) + a[1] * b[1]
        return Poly(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        out = self.value(1)
        for _ in range(exponent):
            out = out * self
        return out

    def __eq__(self, other):
        return self.terms == self.value(other).terms


def variable(index):
    key = tuple(int(i == index) for i in range(NVAR))
    return Poly({key: 1})


def characteristic_parts(a, b, c, theta, z):
    # For y=-1+i*sqrt(z), C=cre+i*sqrt(z)*cim and
    # C'=dre+i*sqrt(z)*dim.  No square root is evaluated.
    x, y, w = a - 1, b - 1, c - 1
    cre = x*y*w - z*(x+y+w) - theta*a*b*c
    cim = x*y + x*w + y*w - z
    dre = x*y + x*w + y*w - 3*z
    dim = 2*(x+y+w)
    n = dre*cim - dim*cre       # -Im(C' conjugate(C))/sqrt(z)
    norm = cre**2 + z*cim**2
    return n, norm


a, b, c, z, theta = [variable(i) for i in range(NVAR)]
n, norm = characteristic_parts(a, b, c, theta, z)
va, vb, vc = (a-1)**2+z, (b-1)**2+z, (c-1)**2+z
assert n == va*vb + va*vc + vb*vc + 2*theta*a*b*c*(a+b+c-3)

# One omitted vertex: the displayed identity is valid for all real variables.
x, y, w = a-1, b-1, c-1
m_two = n*vc - norm
rhs_two = (x**2+y**2+2*z)*vc**2 + 2*theta*a*b*c*w*(w+x)*(w+y) - theta**2*a**2*b**2*c**2
assert m_two == rhs_two

# Two omitted vertices: concavity in theta, for arbitrary z.
m_one = n*vb*vc - norm*(vb+vc)
m_zero = vb**2*vc**2
n1, norm1 = characteristic_parts(a, b, c, Poly.value(1), z)
m_at_one = n1*vb*vc - norm1*(vb+vc)
assert m_one == (1-theta)*m_zero + theta*m_at_one + theta*(1-theta)*a**2*b**2*c**2*(vb+vc)

# Exact nonnegative-coefficient decomposition at z=8/9 and b,c>=3.
r, T, U = variable(0), variable(1), variable(2)
t, u, zz = T+3, U+3, F(8, 9)
n1, norm1 = characteristic_parts(r, t, u, Poly.value(1), zz)
vt, vu = (t-1)**2+zz, (u-1)**2+zz
m_one_at_one = n1*vt*vu - norm1*(vt+vu)
H, V = T+U, T*U
p1 = 162*H**3 + 243*H**2*V + 1296*H**2 + 81*H*V**2 + 1620*H*V + 2240*H + 405*V**2 + 1800*V + 528
p2 = 81*H**3 + 81*H**2*V + 891*H**2 + 810*H*V + 3060*H + 2250*V + 1672
assert m_one_at_one == vt**2*vu**2 + F(2, 81)*r*t*u*p1 + F(1, 81)*r**2*t*u*p2
assert all(x >= 0 for x in p1.terms.values())
assert all(x >= 0 for x in p2.terms.values())

# Five degree-four Bernstein coefficients from the full-block lemma, z=3/4.
s = variable(0)
quartic = 3*((1-s)**2 + F(3,4))**2 - 6*s**3*(1-s)
coefficients = [quartic.terms.get((j,0,0,0,0), F(0)) for j in range(5)]
bernstein = [sum(coefficients[j]*F(comb(k,j),comb(4,j)) for j in range(k+1)) for k in range(5)]
assert bernstein == [F(147,16),F(63,16),F(39,16),F(3,16),F(27,16)]
assert all(c > 0 for c in bernstein)
print('PASS: full-block, one-omitted, two-omitted and concavity identities; exact positive decomposition and Bernstein coefficients')
