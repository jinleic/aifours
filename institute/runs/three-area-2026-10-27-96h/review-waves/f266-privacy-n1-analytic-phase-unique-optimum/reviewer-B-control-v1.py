#!/usr/bin/env python3
"""Reviewer B's bounded exact control for f266. No author code, network or third-party libraries.
Finite identities/signs/root counts only: this script does NOT test any universal optimality claim.
Usage: python3 reviewer-B-control-v1.py receipt-path 'native clock before execution'
"""
import hashlib
import json
import os
import platform
import signal
import sys
import time
from fractions import Fraction as F
from math import factorial

signal.alarm(120)
started = time.monotonic()
checks = []

def check(name, result, detail=''):
    checks.append({'name': name, 'pass': bool(result), 'detail': str(detail)})
    print(('PASS ' if result else 'FAIL ') + name + (': ' + str(detail) if detail else ''))

# Independent sparse-polynomial implementation: rational coefficients, simultaneous powers
# represented by exponent tuples; differentiation, substitution and definite integration.
variables = ('x', 'm', 't', 'd', 'y', 'v', 'i1', 'i2', 'i3', 'iy', 'lam')
dimension = len(variables)

class Poly:
    def __init__(self, terms=None):
        self.terms = {a: F(c) for a, c in (terms or {}).items() if c}

    @staticmethod
    def constant(c):
        return Poly({(0,) * dimension: F(c)}) if c else Poly()

    @staticmethod
    def variable(name):
        a = [0] * dimension
        a[variables.index(name)] = 1
        return Poly({tuple(a): F(1)})

    def convert(self, q):
        return q if isinstance(q, Poly) else Poly.constant(q)

    def __add__(self, q):
        result = dict(self.terms)
        for a, c in self.convert(q).terms.items():
            result[a] = result.get(a, F(0)) + c
        return Poly(result)
    __radd__ = __add__

    def __neg__(self):
        return Poly({a: -c for a, c in self.terms.items()})

    def __sub__(self, q):
        return self + (-self.convert(q))

    def __rsub__(self, q):
        return self.convert(q) - self

    def __mul__(self, q):
        result = {}
        for a, c in self.terms.items():
            for b, e in self.convert(q).terms.items():
                exponent = tuple(ai + bi for ai, bi in zip(a, b))
                result[exponent] = result.get(exponent, F(0)) + c * e
        return Poly(result)
    __rmul__ = __mul__

    def __truediv__(self, c):
        return self * F(1, 1) / c if isinstance(c, Poly) else self * (F(1) / F(c))

    def __pow__(self, n):
        result = Poly.constant(1)
        for unused in range(n):
            result = result * self
        return result

    def __eq__(self, q):
        return self.terms == self.convert(q).terms

    def derivative(self, name):
        index = variables.index(name)
        result = {}
        for a, c in self.terms.items():
            if a[index]:
                b = list(a)
                b[index] -= 1
                result[tuple(b)] = c * a[index]
        return Poly(result)

    def substitute(self, name, q):
        index = variables.index(name)
        q = self.convert(q)
        result = Poly()
        for a, c in self.terms.items():
            b = list(a)
            exponent = b[index]
            b[index] = 0
            result = result + Poly({tuple(b): c}) * q ** exponent
        return result

    def integral(self, name, lower, upper):
        index = variables.index(name)
        lower, upper = self.convert(lower), self.convert(upper)
        result = Poly()
        for a, c in self.terms.items():
            b = list(a)
            exponent = b[index] + 1
            b[index] = 0
            result = result + Poly({tuple(b): c / exponent}) * (upper ** exponent - lower ** exponent)
        return result

    def univariate(self, name):
        index = variables.index(name)
        degree = max((a[index] for a in self.terms), default=0)
        result = [F(0)] * (degree + 1)
        for a, c in self.terms.items():
            if any(a[i] for i in range(dimension) if i != index):
                raise ValueError('Not univariate')
            result[a[index]] += c
        return result

x, m, t, d, y, free_v, i1, i2, i3, iy, lam = (Poly.variable(s) for s in variables)
one = Poly.constant(1)

# Exact univariate Sturm implementation, ascending coefficient order.
def evaluate(p, point):
    result = F(0)
    for coefficient in reversed(p):
        result = result * point + coefficient
    return result

def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p

def remainder(p, q):
    p, q = trim(p), trim(q)
    while p and len(p) >= len(q):
        ratio, shift = p[-1] / q[-1], len(p) - len(q)
        for j, c in enumerate(q):
            p[j + shift] -= ratio * c
        p = trim(p)
    return p

def sturm(p):
    sequence = [trim(p), trim([j * p[j] for j in range(1, len(p))])]
    while sequence[-1]:
        r = remainder(sequence[-2], sequence[-1])
        if not r:
            break
        sequence.append([-c for c in r])
    return [q for q in sequence if q]

def sign(c):
    return (c > 0) - (c < 0)

def variations(sequence, point):
    signs = []
    for q in sequence:
        s = sign(q[-1]) if point == '+inf' else sign(evaluate(q, point))
        if s:
            signs.append(s)
    return sum(a != b for a, b in zip(signs, signs[1:]))

def root_count(p, lower, upper):
    sequence = sturm(p)
    return variations(sequence, lower) - variations(sequence, upper)

# 1. Geometric moments derived from factorial moments and Stirling conversion.
S = [[0] * 5 for unused in range(5)]
S[0][0] = 1
for n in range(1, 5):
    for k in range(1, n + 1):
        S[n][k] = S[n - 1][k - 1] + k * S[n - 1][k]

def raw_moment(n):
    return sum((S[n][k] * factorial(k) * m ** k for k in range(1, n + 1)), Poly())

T2 = m + 2 * m ** 2
T3 = m + 6 * m ** 2 + 6 * m ** 3
T4 = m + 14 * m ** 2 + 36 * m ** 3 + 24 * m ** 4
v, tau = m + m ** 2, one + 2 * m
check('Geometric T2,T3,T4 via falling-factorial moments', all(raw_moment(n) == q for n, q in [(2, T2), (3, T3), (4, T4)]))
check('T2-m^2=v and T4=T2(1+12m+12m^2)', T2 - m ** 2 == v and T4 == T2 * (one + 12 * m + 12 * m ** 2))

# 2. Diamond quintic/centered identities: finite checks, not universal root isolation.
M2 = x ** 2 + 2 * m * x + T2
M4 = x ** 4 + 4 * m * x ** 3 + 6 * T2 * x ** 2 + 4 * T3 * x + T4
P = x ** 5 + 5 * m * x ** 4 + (2 * m + 12 * m ** 2) * x ** 3 + (12 * m ** 3 - 2 * m) * x ** 2 - m * (one + 2 * m) * (one + 6 * m) * x + m ** 2 * (one + 2 * m)
check('M4 prime M2 - M4 M2 prime = 2P', M4.derivative('x') * M2 - M4 * M2.derivative('x') == 2 * P)
Pc = x ** 5 + 2 * v * x ** 3 - 2 * v * tau * x ** 2 - v * (one + 3 * v) * x + 2 * v ** 2 * tau
M2c, M4c = M2.substitute('x', x - m), M4.substitute('x', x - m)
check('Centered quintic and moments', P.substitute('x', x - m) == Pc and M2c == x ** 2 + v and M4c == x ** 4 + 6 * v * x ** 2 + 4 * v * tau * x + v + 9 * v ** 2)
G = 2 * x ** 4 - 4 * v * tau * x - v - 6 * v ** 2
check('M4-3M2^2=-G and identity (13a)', M4c - 3 * M2c ** 2 == -G and 2 * x * Pc + (v - x ** 2) * G == 6 * v * (x ** 2 + v) * (x ** 2 - v - F(1, 6)))
check('P(0), P(1) and (g+m)^2+v=M2(g)', P.substitute('x', 0) == m ** 2 * (one + 2 * m) and P.substitute('x', 1) == (one + m) ** 2 * (one + 2 * m) and (x + m) ** 2 + v == M2)
reduced = Poly()
for exponent, coefficient in Pc.terms.items():
    a = exponent[0]
    b = list(exponent)
    b[0] = a % 2
    reduced = reduced + Poly({tuple(b): coefficient}) * v ** (a // 2)
check('Centered P modulo x^2-v equals -vx', reduced == -v * x)
A = (one - 12 * free_v) * (one + 6 * free_v) / 18
check('Screen identity (13c), using independent free v', A ** 2 - 16 * free_v ** 2 * (one + 4 * free_v) * (free_v + F(1, 6)) == (one + 6 * free_v) * (one - 18 * free_v - 864 * free_v ** 2 - 2592 * free_v ** 3) / 324)
check('G at x_c: 2(v+1/6)^2-v-6v^2=A', 2 * (free_v + F(1, 6)) ** 2 - free_v - 6 * free_v ** 2 == A)

# 3. Trial, threshold and epsilon localization; this is the interface bound V<=1/2.
M2h, M4h = M2.substitute('x', F(1, 2)), M4.substitute('x', F(1, 2))
check('One-half diamond M2/M4 expansions', M2h == F(1, 4) + 2 * m + 2 * m ** 2 and M4h == F(1, 16) + 5 * m + 29 * m ** 2 + 48 * m ** 3 + 24 * m ** 4)
Delta = M4h - F(3, 2) * M2h
check('Trial J<=1/2 iff Delta<=0', Delta == 24 * m ** 4 + 48 * m ** 3 + 26 * m ** 2 + 2 * m - F(5, 16))
check('Delta derivative has strictly positive coefficients', Delta.derivative('m') == 96 * m ** 3 + 144 * m ** 2 + 52 * m + 2)
Dcoeff = Delta.univariate('m')
check('Exact Delta signs at 1/14 and 1/13', evaluate(Dcoeff, F(1, 14)) == F(-725, 38416) and evaluate(Dcoeff, F(1, 13)) == F(8171, 456976))
check('Sturm Delta: one positive root; that root lies in (1/14,1/13)', root_count(Dcoeff, F(0), '+inf') == 1 and root_count(Dcoeff, F(1, 14), F(1, 13)) == 1)
check('Epsilon bracket and v bound: (1+m)/m=15,14 at endpoints; 14/169<1/12', (1 + F(1, 14)) / F(1, 14) == 15 and (1 + F(1, 13)) / F(1, 13) == 14 and F(14, 169) < F(1, 12))

# 4. Compare formula (5) to f261 (12),(B2), treating profile integrals as formal atoms.
Z = 8 * (i1 - t ** 2 / 2) + 8 * t * m + 2 * T2
N = F(2, 3) * T4 + F(16, 3) * t * T3 + 4 * t ** 2 * T2 + 8 * (T2 * i1 + m * (i2 + t ** 3 / 3) + i3 / 3 + iy - t ** 4 / 3)
area = 8 * (i1 - t ** 2 / 2)
core_moment = 8 * ((i3 - t ** 4 / 4) / 3 + iy - t ** 4 / 4)
parallel_coefficient = 8 * (i2 + t ** 3 / 3)
check('Formula (5) equals f261 tail mass/moment at N=1', Z == area + 8 * t * m + 2 * T2 and N == core_moment + parallel_coefficient * m + (area + 8 * t ** 2) * T2 + F(16, 3) * t * T3 + F(2, 3) * T4)
H = N - lam * Z
check('F-dependent coefficients equal 8 integral G_lambda(F,y)', H.derivative('i1') == 8 * (T2 - lam) and H.derivative('i2') == 8 * m and H.derivative('i3') == Poly.constant(F(8, 3)) and H.derivative('iy') == Poly.constant(8))

def profile_substitution(expression, profile):
    values = {'i1': profile.integral('y', 0, t), 'i2': (profile ** 2).integral('y', 0, t), 'i3': (profile ** 3).integral('y', 0, t), 'iy': (y ** 2 * profile).integral('y', 0, t)}
    for name, value in values.items():
        expression = expression.substitute(name, value)
    return expression

square = profile_substitution(N - T2 * Z, t)
check('Square/clip h_T2 expansion', square == F(2, 3) * T4 - 2 * T2 ** 2 + (F(16, 3) * T3 - 8 * m * T2) * t + 8 * T2 * t ** 2 + F(32, 3) * m * t ** 3 + F(8, 3) * t ** 4)
check('h_T2 positive constant and linear coefficients', F(2, 3) * T4 - 2 * T2 ** 2 == F(2, 3) * m + F(22, 3) * m ** 2 + 16 * m ** 3 + 8 * m ** 4 and F(16, 3) * T3 - 8 * m * T2 == F(16, 3) * m + 24 * m ** 2 + 16 * m ** 3)
check('Diamond profile yields Z=2M2 and N=(2/3)M4', profile_substitution(Z, 2 * t - y).substitute('t', x / 2) == 2 * M2 and profile_substitution(N, 2 * t - y).substitute('t', x / 2) == F(2, 3) * M4)

# 5. Rounded junction/envelope algebra; the analytic convexity proof remains written.
junction_lam = 2 * t ** 2 + 2 * d ** 2 + 2 * m * (t + d) + T2
P3 = F(4, 3) * d ** 3 + 2 * m * d ** 2 + m ** 2 * d
C0 = T3 / 3 - m * T2 / 2
check('Arc/facet junction lam-v-(t-d)^2=(t+d+m)^2', junction_lam - v - (t - d) ** 2 == (t + d + m) ** 2)
check('P3 derivative and C0 expansion', P3.derivative('d') == (2 * d + m) ** 2 and C0 == m / 3 + F(3, 2) * m ** 2 + m ** 3)
# Derivative before junction substitution, derived from endpoint and upper-facet terms.
envelope = F(16, 3) * T3 + 16 * t * T2 + 16 * m * t ** 2 - 8 * m * junction_lam - F(64, 3) * d ** 3 - 16 * m * d ** 2
check('Rounded signed-functional derivative equals 16(C0+tv-P3)', envelope == 16 * (C0 + t * v - P3))
check('R regime membership from t>d>0: lambda-(2t^2+2mt+T2)>0 and (2t+m)^2-(t+d+m)^2>0', junction_lam - (2 * t ** 2 + 2 * m * t + T2) == 2 * d ** 2 + 2 * m * d and (2 * t + m) ** 2 - (t + d + m) ** 2 == (t - d) * (3 * t + d + 2 * m))

# 6. Cubic and finite root-count controls: no prior v241 input is accessed.
cubic = [F(-1), F(18), F(864), F(2592)]
check('Cubic signs at 1/50,1/40', evaluate(cubic, F(1, 50)) < 0 < evaluate(cubic, F(1, 40)), (evaluate(cubic, F(1, 50)), evaluate(cubic, F(1, 40))))
check('Sturm cubic: exactly one positive root', root_count(cubic, F(0), '+inf') == 1)
check('Epsilon transition rational brackets', F(64, 3969) < F(1, 50) < F(1, 40) < F(15, 196) < F(1, 12))
for mm in (F(1, 14), F(1, 20), F(1, 100), F(1, 1000)):
    coefficients = P.substitute('m', mm).univariate('x')
    counts = root_count(coefficients, F(0), F(1)), root_count(coefficients, F(1), '+inf')
    check('Instance Sturm P_m roots, m=' + str(mm), counts == (2, 0), counts)

# Two finite rational root brackets cross-check (13d); they are not a proof for all m.
for mm in (F(1, 14), F(1, 100)):
    coefficients = P.substitute('m', mm).univariate('x')
    lower, upper = F(0), F(1)
    for unused in range(50):
        midpoint = (lower + upper) / 2
        if root_count(coefficients, midpoint, upper):
            lower = midpoint
        else:
            upper = midpoint
    vv = mm * (1 + mm)
    a, b = lower + mm, upper + mm
    Gcoeff = G.substitute('m', mm).univariate('x')
    signs_G = sign(-evaluate(Gcoeff, a)), sign(-evaluate(Gcoeff, b))
    signs_Q = sign(a ** 2 - vv - F(1, 6)), sign(b ** 2 - vv - F(1, 6))
    cubic_sign = sign(evaluate(cubic, vv))
    check('Instance (13d) screen sign, m=' + str(mm), signs_G[0] == signs_G[1] == signs_Q[0] == signs_Q[1] == cubic_sign and a ** 2 > vv and evaluate(coefficients, lower) < 0 < evaluate(coefficients, upper), 'g bracket=[' + str(lower) + ',' + str(upper) + ']; sign=' + str(cubic_sign))

source = open(sys.argv[0], 'rb').read()
ok = all(item['pass'] for item in checks)
receipt = {
    'kind': 'reviewer-owned-bounded-exact-control-receipt',
    'wave': 'f266-privacy-n1-analytic-phase-unique-optimum',
    'reviewer_slice': 'B',
    'script': {'path': os.path.abspath(sys.argv[0]), 'sha256': hashlib.sha256(source).hexdigest(), 'bytes': len(source), 'LF': source.count(b'\n')},
    'observed_native_clock_before_run': sys.argv[2],
    'python_version': platform.python_version(),
    'wall_seconds': round(time.monotonic() - started, 3),
    'alarm_seconds': 120,
    'stdlib_only': True,
    'author_code_executed': False,
    'network_used': False,
    'mathematical_arithmetic': 'Fraction/integer only; clock measurement is not mathematical evidence',
    'scope': 'Finite identities, rational signs, Sturm counts and two rational root brackets ONLY; not f261 or any universal claim, geometric, attainment, optimality or uniqueness proof',
    'checks': checks,
    'n_checks': len(checks),
    'all_passed': ok,
    'exit_code': 0 if ok else 1
}
with open(sys.argv[1], 'x') as output:
    json.dump(receipt, output, indent=2)
    output.write('\n')
print(('ALL ' + str(len(checks)) + ' CHECKS PASSED') if ok else 'SOME CHECKS FAILED')
print('SCRIPT_SHA256=' + receipt['script']['sha256'])
print('WALL_SECONDS=' + str(receipt['wall_seconds']))
sys.exit(receipt['exit_code'])
