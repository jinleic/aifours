"""Exploratory: fit r^2 along bottom families (fixed L, lambda; v = 3e + lambda) as rational functions of v."""
import json
import sys
from collections import defaultdict

import sympy as sp

V = sp.symbols('v')


def ratfit(pts, maxdeg=6):
    xs = sorted(pts)
    for tot in range(0, 2 * maxdeg + 1):
        for dn in range(0, tot + 1):
            dd = tot - dn
            need = dn + dd + 1
            if len(xs) < need + 3:
                continue
            a = sp.symbols(f'a0:{dn + 1}')
            b = sp.symbols(f'b0:{dd + 1}')
            eqs = [sum(a[i] * x ** i for i in range(dn + 1)) - pts[x] * sum(b[i] * x ** i for i in range(dd + 1))
                   for x in xs[:need + 1]]
            sol = sp.solve(eqs, list(a) + list(b), dict=True)
            if not sol:
                continue
            s = sol[0]
            num = sum(s.get(a[i], a[i]) * V ** i for i in range(dn + 1))
            den = sum(s.get(b[i], b[i]) * V ** i for i in range(dd + 1))
            free = (num.free_symbols | den.free_symbols) - {V}
            num = num.subs({t: 1 for t in free})
            den = den.subs({t: 1 for t in free})
            if den == 0:
                continue
            fn = sp.cancel(num / den)
            if all(fn.subs(V, x) == pts[x] for x in xs):
                return sp.factor(fn)
    return None


D = json.load(open(sys.argv[1]))
Lmax = int(sys.argv[2]) if len(sys.argv) > 2 else 5
fam = defaultdict(dict)
for r in D['rows']:
    v, L, e, Lp, ep = r['v'], r['L'], r['e'], r['Lp'], r['ep']
    if L > Lmax:
        continue
    lam, lamp = v - 3 * e, v - 1 - 3 * ep
    fam[(L, lam, Lp, lamp)][v] = (sp.Rational(r['r2']), r['sign'])
for key in sorted(fam):
    pts = {v: x[0] for v, x in fam[key].items()}
    sg = sorted(set(x[1] for x in fam[key].values()))
    vs = sorted(pts)
    stable = {v: pts[v] for v in vs if v >= 7}
    fn = ratfit(stable) if len(stable) >= 4 else None
    print(f"L={key[0]} lam={key[1]} -> L'={key[2]} lam'={key[3]}: v in [{vs[0]}..{vs[-1]}] ({len(vs)} pts)  r2={fn}  signs={sg}")
