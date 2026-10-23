#!/usr/bin/env python3
"""identities_v4_I15.py -- third addendum for I15 (moments of the control members f0 and h0), without sympy.integrate.

r03/r04 showed sympy.integrate returns exp_polar/branch artefacts for the k = 0 cosine integral (k = 1, 2 and the h0
formula were already confirmed).  Here, for z = 1 + delta - i omega and k = 0, 1, 2, an explicit antiderivative
F_k(t) = -e^{-zt} * sum_{j=0}^{k} k!/(j!) t^j / z^{k-j+1} of t^k e^{-zt} is checked by exact differentiation, with
F_k(0) = -k!/z^{k+1} and F_k(t) -> 0 (Re z > 0), so int_0^oo t^k e^{-zt} dt = k!/z^{k+1}.  Taking real parts (the
integrals converge absolutely) gives m_k(f0) = k!(1 - Re zeta^{k+1}) and m_k(h0) = k!(1 - Re((1 - i r) zeta^{k+1})),
zeta = 1/z, because cos(omega t) = Re e^{i omega t} and cos + r sin = Re((1 - i r) e^{i omega t}).
Writes OUT (exclusive).  Usage: python -I -B identities_v4_I15.py OUT.json
"""
import sys
import json
import sympy as sp

OUT = sys.argv[1]
t = sp.symbols("t", positive=True)
zr, zi = sp.symbols("zr zi", real=True)
z = zr + sp.I * zi
res = {}
ok = True
for k in range(3):
    F = -sp.exp(-z * t) * sum(sp.factorial(k) / sp.factorial(j) * t ** j / z ** (k - j + 1) for j in range(k + 1))
    ok = ok and sp.simplify(sp.diff(F, t) - t ** k * sp.exp(-z * t)) == 0
    ok = ok and sp.simplify(F.subs(t, 0) + sp.factorial(k) / z ** (k + 1)) == 0
res["antiderivative_t^k_e^{-zt}_k0..2"] = bool(ok)
dl, om, r = sp.symbols("delta omega r", positive=True)
res["cos(wt) = Re e^{iwt}"] = sp.simplify(sp.re(sp.expand_complex(sp.exp(sp.I * om * t))) - sp.cos(om * t)) == 0
res["cos + r sin = Re((1 - i r) e^{iwt})"] = sp.simplify(
    sp.re(sp.expand_complex((1 - sp.I * r) * sp.exp(sp.I * om * t))) - (sp.cos(om * t) + r * sp.sin(om * t))) == 0
res["e^{-(1+delta)t} e^{i omega t} = e^{-(1+delta - i omega) t}"] = sp.simplify(
    sp.exp(-(1 + dl) * t) * sp.exp(sp.I * om * t) - sp.exp(-(1 + dl - sp.I * om) * t)) == 0
res["all_true"] = all(v is True for v in res.values())
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps(res))
