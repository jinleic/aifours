"""Exploratory: fit r^2 along top families k = 2v - L as rational functions of v."""
import json
import sys
from collections import defaultdict

import sympy as sp

V = sp.symbols('v')
path = sys.argv[1]
kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
D = json.load(open(path))
fam = defaultdict(dict)
for r in D['rows']:
    v, L, e, Lp, ep = r['v'], r['L'], r['e'], r['Lp'], r['ep']
    k = 2 * v - L
    kp = 2 * (v - 1) - Lp
    fam[(k, e, kp, ep)][v] = (sp.Rational(r['r2']), r['sign'])


def ratfit(pts, maxdeg=8):
    """Find rational function N(v)/D(v) through points (exact), smallest total degree,
    requiring at least 3 spare points for validation."""
    xs = sorted(pts)
    for tot in range(0, 2 * maxdeg + 1):
        for dn in range(0, tot + 1):
            dd = tot - dn
            need = dn + dd + 1
            if len(xs) < need + 3:
                continue
            a = sp.symbols(f'a0:{dn + 1}')
            b = sp.symbols(f'b0:{dd + 1}')
            eqs = []
            for x in xs[:need + 1]:
                y = pts[x]
                eqs.append(sum(a[i] * x ** i for i in range(dn + 1)) - y * sum(b[i] * x ** i for i in range(dd + 1)))
            sol = sp.solve(eqs, list(a) + list(b), dict=True)
            if not sol:
                continue
            s = sol[0]
            num = sum(s.get(a[i], a[i]) * V ** i for i in range(dn + 1))
            den = sum(s.get(b[i], b[i]) * V ** i for i in range(dd + 1))
            free = (num.free_symbols | den.free_symbols) - {V}
            if free:
                num = num.subs({t: 1 for t in free})
                den = den.subs({t: 1 for t in free})
            if den == 0:
                continue
            fn = sp.cancel(num / den)
            if all(sp.simplify(fn.subs(V, x) - pts[x]) == 0 for x in xs):
                return sp.factor(fn)
    return None


for key in sorted(fam):
    k, e, kp, ep = key
    if k > kmax:
        continue
    pts = {v: val[0] for v, val in fam[key].items()}
    signs = {v: val[1] for v, val in fam[key].items()}
    vs = sorted(pts)
    # use only v in the stable range (exclude small v where structure changes)
    stable = {v: pts[v] for v in vs if v >= k + 3}
    fn = ratfit(stable) if len(stable) >= 5 else None
    sg = sorted(set(signs[v] for v in stable))
    print(f"k={k} e={e} -> k'={kp} e'={ep}: v in [{min(vs)},{max(vs)}] r2 = {fn}  signs={sg}")
    if fn is not None:
        bad = [v for v in vs if sp.simplify(fn.subs(V, v) - pts[v]) != 0]
        if bad:
            print(f"      formula fails at v = {bad}")
