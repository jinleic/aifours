import sys, collections
sys.path.insert(0,'.')
from km2 import KM2
from g513_groups import *
for tag, bases in [("gamma", [(P27, []), (F57, [gamma(1,1)])]), ("plain", [(P27, []), (F57, [])])]:
    M = KM2(N, G_GENS, bases, names=["S0","B"])
    cnt = collections.Counter()
    for j, U, cols in M.rows:
        if j != 1: continue
        t = M.trip[U[0]]
        lay = len({int(p)//19 for p in t})
        cnt[lay] += 1
    print(tag, "B rows by #layers of first triple:", dict(cnt), "total", sum(cnt.values()))
