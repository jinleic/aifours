#!/usr/bin/env python3
"""Independent exact checks of the f61 PH spectral/graph identities.

Only the Python standard library is used. This checks polynomial algebra and
specific controls, not Perron theory, the extremal theorem, or existence.
"""
from fractions import Fraction as Q
from itertools import permutations


class Poly:
    """Sparse bivariate polynomial over Q; exponent order is (x, y)."""
    def __init__(self, terms=0):
        if not isinstance(terms, dict):
            terms = {(0, 0): Q(terms)}
        self.terms = {k: Q(v) for k, v in terms.items() if v}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly(value)

    def __add__(self, other):
        result = dict(self.terms)
        for key, value in self.coerce(other).terms.items():
            result[key] = result.get(key, Q(0)) + value
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + -self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        result = {}
        for (i, j), a in self.terms.items():
            for (k, l), b in self.coerce(other).terms.items():
                key = (i + k, j + l)
                result[key] = result.get(key, Q(0)) + a * b
        return Poly(result)

    __rmul__ = __mul__

    def __truediv__(self, value):
        return self * (Q(1) / Q(value))

    def __pow__(self, power):
        if not isinstance(power, int) or power < 0:
            raise ValueError('power must be a nonnegative integer')
        result = Poly(1)
        for _ in range(power):
            result = result * self
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def value(self, x, y):
        return sum((c * Q(x) ** i * Q(y) ** j
                    for (i, j), c in self.terms.items()), Q(0))

    def __repr__(self):
        if not self.terms:
            return '0'
        return ' + '.join(f'({v})*x^{i}*y^{j}'
                          for (i, j), v in sorted(self.terms.items(), reverse=True))


def require(label, condition):
    if not condition:
        raise RuntimeError('FAIL: ' + label)
    print('PASS:', label)


def trace(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))), Q(0))


def matmul(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), Q(0))
             for j in range(n)] for i in range(n)]


def matadd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))]
            for i in range(len(a))]


def scale(a, value):
    return [[value * cell for cell in row] for row in a]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def centered_traces(u, z):
    h = (u + 4) / 6
    return (h**2 + (h-u)**2 + 4*((h-1)**2-z),
            h**3 + (h-u)**3 + 4*((h-1)**3-3*(h-1)*z))


x, y = Poly({(1, 0): 1}), Poly({(0, 1): 1})
# Spectral sums for the n=3 and n=5 cases; x=r and y=z.
for n, k in ((3, 1), (5, 2)):
    trace_gap = n*(x**2 + 2*k*(1-y)) - (x+2*k)**2
    claimed = 2*k*((1-x)**2 - n*y)
    require(f'{n}-state trace-square identity', trace_gap == claimed)
    print('  expanded:', trace_gap)

# Derive centered moments directly from the conjugate spectral pairs.
tau2, tau3 = centered_traces(x, y)
expect2 = (5*x**2 - 8*x + 8 - 24*y)/6
expect3 = -(x-2)*(5*x**2 - 2*x + 18*y + 2)/9
require('six-state centered square identity', tau2 == expect2)
require('six-state centered cube identity', tau3 == expect3)
print('  tau2:', tau2)
print('  tau3:', tau3)

# Recompute with x=s=u-2 and y=delta=Z-1/2.
sub2, sub3 = centered_traces(x+2, y+Q(1, 2))
tau20 = x*(5*x+12)/6
tau30 = -x*(5*x**2+18*x+27)/9
require('delta shift in square', sub2 == tau20-4*y)
require('delta shift in cube', sub3 == tau30-2*x*y)
gap = Q(8, 15)*tau20**3 - tau30**2
negative = -x**2*(30*x**2+116*x+135)/15
require('strict negative zero-delta polynomial identity', gap == negative)
print('  zero-delta gap:', gap)

# Numeric rational nonvacuity point: square is positive but cubic obstruction fails.
q = tau2.value(3, Q(3, 4))
p = tau3.value(3, Q(3, 4))
witness_gap = Q(8, 15)*q**3-p**2
require('u=3, Z=3/4: square positive and necessary inequality violated',
        q > 0 and p < 0 and witness_gap < 0)
print(f'  tau2={q}; tau3={p}; (8/15)tau2^3-tau3^2={witness_gap}')

# Non-diagonalizable conjugate-pair Jordan control. M is NOT claimed Metzler.
m = [[Q(0) for _ in range(6)] for _ in range(6)]
m[1][1] = Q(-3)
for i in (2, 4):
    m[i][i] = m[i+1][i+1] = Q(-1)
    m[i][i+1] = Q(-1)
    m[i+1][i] = Q(1)
m[2][4] = m[3][5] = Q(1)
h = Q(7, 6)
centered = matadd(m, scale(identity(6), h))
centered2 = matmul(centered, centered)
require('nondiagonalizable real control reproduces centered traces',
        trace(centered2) == tau2.value(3, 1) and
        trace(matmul(centered2, centered)) == tau3.value(3, 1))
j = [[m[i][k] for k in range(2, 6)] for i in range(2, 6)]
annihilator = matadd(matadd(matmul(j, j), scale(j, 2)), scale(identity(4), 2))
require('conjugate-pair control has nontrivial nilpotent Jordan coupling',
        any(cell != 0 for row in annihilator for cell in row) and
        all(cell == 0 for row in matmul(annihilator, annihilator) for cell in row))
print(f'  Jordan tau2={trace(centered2)}; tau3={trace(matmul(centered2, centered))}')

# Directed 3-cycle AM-GM control with rational square roots, embedded in 6x6.
a = [[Q(0) for _ in range(6)] for _ in range(6)]
for i, v in enumerate((-5, -3, -2, 1, 3, 6)):
    a[i][i] = Q(v)
a[0][1], a[1][2], a[2][0] = Q(4), Q(9), Q(16)
a[1][0] = a[2][1] = a[0][2] = Q(1)
sym = [[a[i][j] if i == j else Q(0) for j in range(6)] for i in range(6)]
for i, j, v in ((0, 1, 2), (1, 2, 3), (0, 2, 4)):
    sym[i][j] = sym[j][i] = Q(v)
a2, s2 = matmul(a, a), matmul(sym, sym)
a3, s3 = matmul(a2, a), matmul(s2, sym)
require('symmetric replacement preserves trace and trace-square',
        trace(a) == trace(sym) == 0 and trace(a2) == trace(s2))
require('cycle AM-GM gap equals 3*(sqrt(576)-sqrt(1))^2',
        trace(a3)-trace(s3) == 3*(24-1)**2)
print(f'  common square={trace(a2)}; cube gap={trace(a3)-trace(s3)}')

# Sharp equality control for the symmetric six-eigenvalue bound.
diag = (-5, 1, 1, 1, 1, 1)
q0, p0 = sum(v*v for v in diag), sum(v**3 for v in diag)
require('symmetric-trace-cube bound has equality at (-5,1,1,1,1,1)',
        sum(diag) == 0 and p0 < 0 and Q(8, 15)*q0**3 == p0**2)

# Independent determinant permutation calculation for a seven-vertex cycle.
u = (-3, -2, -1, 0, 1, 2, 4)
w = (2, 1, 3, 1, 2, 1, 2)
entries = [[Poly(0) for _ in range(7)] for _ in range(7)]
for i in range(7):
    entries[i][i] = x+u[i]
    entries[i][(i+1) % 7] = Poly(-w[i])
det = Poly(0)
nonzero = 0
for perm in permutations(range(7)):
    term = Poly(1)
    for i in range(7):
        term = term*entries[i][perm[i]]
    if not term.terms:
        continue
    nonzero += 1
    inversions = sum(perm[i] > perm[j] for i in range(7) for j in range(i+1, 7))
    det += (-1 if inversions % 2 else 1)*term
prod, weight = Poly(1), 1
for ui, wi in zip(u, w):
    prod *= x+ui
    weight *= wi
require('cycle determinant: exactly two permutation terms and product-minus-K',
        nonzero == 2 and det == prod-weight)
print(f'  n=7 cycle K={weight}; P(x)={det}')

# Negative controls prove the identity comparator is capable of rejecting errors.
require('negative control rejects a changed six-state coefficient', tau2 != expect2+y)
require('negative control rejects a changed cycle weight', det != prod-(weight+1))
print('RESULT: exact identities and targeted controls completed; not a formal proof')
