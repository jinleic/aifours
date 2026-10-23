import sys, collections
sys.path.insert(0, '..')
sys.path.insert(0, '.')
from lkts_core import *
import numpy as np
n=57
def P(f):
    return tuple(19*i2+x2 for (x2,i2) in (f(x,i) for i in range(3) for x in range(19)))
# note ordering: index = 19*i + x, iterate i then x
tau = P(lambda x,i: ((x+1)%19, i))
nu  = P(lambda x,i: ((4*x)%19, (i+1)%3))
rho = P(lambda x,i: (x, (i+1)%3))
G = closure([tau,nu,rho], n)
print("order", len(G))
stats = collections.Counter()
for g in G:
    stats[(perm_order(g), len(fixed_points(g)))] += 1
for k in sorted(stats): print("order,fix", k, stats[k])
trip, tid = triple_index_tables(n)
img = triple_images(G, trip, tid)
rep = orbits_from_images(img)
orbs = orbit_lists(rep)
sizes = collections.Counter(len(v) for v in orbs.values())
print("triple orbits", len(orbs), "by size", sorted(sizes.items()))
