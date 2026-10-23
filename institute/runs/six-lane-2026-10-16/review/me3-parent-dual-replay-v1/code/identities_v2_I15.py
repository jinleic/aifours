#!/usr/bin/env python3
"""identities_v2_I15.py -- addendum to identities_v1.py (run r02, all items True except I15).

r02 reported I15 False because sympy left exp_polar(0) (= 1) unsimplified in the k = 0 integral (diagnosed by a
throw-away sympy session; not evidence).  This script re-checks I15 with sympy.unpolarify, adds the moment formula of
the second control member h0 = 1 - e^{-delta t}(cos(omega t) + r sin(omega t)), r = delta/omega, and the derivative
identity behind h0 >= 0.  Writes OUT (exclusive).  Usage: python -I -B identities_v2_I15.py OUT.json
"""
import sys
import json
import sympy as sp

OUT = sys.argv[1]
t, dl, om, u, r = sp.symbols("t delta omega u r", positive=True)
I = sp.I
res = {}


def zero(e):
    e = sp.unpolarify(e)
    return sp.simplify(sp.expand(sp.together(e))) == 0


ok_f0, ok_h0 = True, True
rr = dl / om
for kk in range(3):
    mf = sp.integrate(t ** kk * (sp.exp(-t) - sp.exp(-(1 + dl) * t) * sp.cos(om * t)), (t, 0, sp.oo), conds="none")
    cf = sp.factorial(kk) * (1 - sp.re(sp.expand_complex((1 / (1 + dl - I * om)) ** (kk + 1))))
    ok_f0 = ok_f0 and zero(mf - cf)
    mh = sp.integrate(t ** kk * (sp.exp(-t) - sp.exp(-(1 + dl) * t) * (sp.cos(om * t) + rr * sp.sin(om * t))),
                      (t, 0, sp.oo), conds="none")
    ch = sp.factorial(kk) * (1 - sp.re(sp.expand_complex((1 - I * rr) * (1 / (1 + dl - I * om)) ** (kk + 1))))
    ok_h0 = ok_h0 and zero(mh - ch)
res["I15_f0_moments (unpolarified)"] = ok_f0
res["I15b_h0_moments"] = ok_h0
k_u = sp.exp(-r * u) * (sp.cos(u) + r * sp.sin(u))
res["I15c_d/du e^{-ru}(cos u + r sin u) = -(1+r^2) e^{-ru} sin u"] = zero(sp.diff(k_u, u) + (1 + r ** 2) * sp.exp(-r * u) * sp.sin(u))
res["all_true"] = all(v is True for v in res.values())
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res))
