#!/usr/bin/env python3
"""Check exact positive-coefficient quadratic bound for the two-omission block.

Uses the stdlib Fraction polynomial arithmetic and characteristic identity
from the pinned previous checker; this replay is not an independent audit.
"""
from fractions import Fraction as F
from pathlib import Path
from runpy import run_path

ns = run_path(str(Path(__file__).with_name('frontier-20261028-ph7-nine-edge-log-derivative-fraction-check.py')))
Poly, variable = ns['Poly'], ns['variable']
r, T, U = variable(0), variable(1), variable(2)
cut = F(21, 8)
t, u, z = T+cut, U+cut, F(8, 9)
n, norm = ns['characteristic_parts'](r, t, u, Poly.value(1), z)
vt, vu = (t-1)**2+z, (u-1)**2+z
m1 = n*vt*vu - norm*(vt+vu)
assert all(key[0] <= 2 and key[3:] == (0, 0) for key in m1.terms)
by_power = [{(key[1],key[2]):v for key,v in m1.terms.items() if key[0] == k} for k in range(3)]
constants = [p.get((0,0),F(0)) for p in by_power]
assert constants == [F(17082424681921,110075314176), -F(34168631,524288), F(4084297,589824)]
assert all(value >= 0 for p in by_power for ex,value in p.items() if ex != (0,0))
a,b,c = constants
assert a > 0 and b < 0 and c > 0
assert 4*a*c-b*b == F(51891455549006353,1014454095446016) > 0
print('PASS: cut=21/8; all 3 coefficient polynomials bounded by constants; bounding quadratic strictly positive')
