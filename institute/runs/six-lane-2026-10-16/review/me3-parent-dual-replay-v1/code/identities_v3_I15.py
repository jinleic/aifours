#!/usr/bin/env python3
"""identities_v3_I15.py -- second addendum for I15 (f0 moments).  r03 (identities_v2_I15.py) confirmed the h0 moments
and the h0 >= 0 derivative identity but still reported the f0 check False: sympy.unpolarify did not remove the
exp_polar(0) factors.  Here every exp_polar(x) is replaced by exp(x) (exp_polar(0) = 1) before simplification, and
the k = 0..2 identities are additionally checked by exact substitution at three rational points.
Writes OUT (exclusive).  Usage: python -I -B identities_v3_I15.py OUT.json
"""
import sys
import json
import sympy as sp

OUT = sys.argv[1]
t, dl, om = sp.symbols("t delta omega", positive=True)
I = sp.I
res = {}
ok_sym, ok_pts = True, True
for kk in range(3):
    mf = sp.integrate(t ** kk * (sp.exp(-t) - sp.exp(-(1 + dl) * t) * sp.cos(om * t)), (t, 0, sp.oo), conds="none")
    mf = mf.replace(sp.exp_polar, sp.exp)
    cf = sp.factorial(kk) * (1 - sp.re(sp.expand_complex((1 / (1 + dl - I * om)) ** (kk + 1))))
    diff = sp.simplify(sp.expand(sp.together(mf - cf)))
    ok_sym = ok_sym and diff == 0
    for a, b in ((sp.Rational(1, 3), sp.Rational(2, 7)), (sp.Rational(5, 2), sp.Rational(9, 4)), (sp.Integer(64), sp.Integer(10))):
        ok_pts = ok_pts and sp.simplify((mf - cf).subs({dl: a, om: b})) == 0
res["I15_f0_moments_symbolic (exp_polar->exp)"] = bool(ok_sym)
res["I15_f0_moments_at_rational_points"] = bool(ok_pts)
res["all_true"] = bool(ok_sym and ok_pts)
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res))
