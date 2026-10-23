import sys
sys.path.insert(0,'.')
from lkts_core import closure, compose, inverse, perm_order, fixed_points
from g513_groups import *
G = set(closure(G_GENS, N))
F = set(closure(F57, N)); Fp = set(closure(F57P, N))
for e, FF, name in [(1, F, "F57"), (-1, Fp, "F57'")]:
    for c in [1, 2]:
        g = gamma(c, e)
        ok = all(compose(compose(g, h), inverse(g)) in FF for h in FF)
        K = closure(list(F57 if e==1 else F57P) + [g], N)
        print(name, "c", c, "order", perm_order(g), "fix", len(fixed_points(g)), "normalizes", ok,
              "in G", g in G, "|K|", len(K), "|K∩G|", len(set(K) & G),
              "f3-elements in K", sum(1 for k in K if perm_order(k)==3 and len(fixed_points(k))==3))
