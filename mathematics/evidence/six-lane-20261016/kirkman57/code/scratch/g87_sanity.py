import sys, collections, time
sys.path.insert(0,'.')
from lkts_core import *
from g87_groups import *
t0=time.time()
G = closure(G_GENS, N); print("order", len(G))
st = collections.Counter((perm_order(g), len(fixed_points(g))) for g in G)
print(sorted(st.items()))
trip, tid = triple_index_tables(N)
img = triple_images(G, trip, tid)
rep = img.min(axis=0)
sizes = collections.Counter(collections.Counter(rep.tolist()).values())
print("triple orbits by size", sorted(sizes.items()), round(time.time()-t0,1))
