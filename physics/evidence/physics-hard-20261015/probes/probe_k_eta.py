# <=5 min probe (floating point, NOT a certificate): single-rate trial, y fixed large (optimum sat at y-grid max), eta golden search.
import numpy as np, math, sys
sys.path.insert(0, '/tmp/ai4s-hard/phys')
from probe_k_lib import Phi
def best(k, a, y=60.0):
    D = int(k*a/2 + 10*math.sqrt(k*a/2) + 15)
    lo, hi = 0.35, 0.75; g = (math.sqrt(5)-1)/2
    x1, x2 = hi-g*(hi-lo), lo+g*(hi-lo); f1, f2 = Phi(k,a,y,x1,D), Phi(k,a,y,x2,D)
    for _ in range(18):
        if f1 < f2: hi, x2, f2 = x2, x1, f1; x1 = hi-g*(hi-lo); f1 = Phi(k,a,y,x1,D)
        else: lo, x1, f1 = x1, x2, f2; x2 = lo+g*(hi-lo); f2 = Phi(k,a,y,x2,D)
    return min((f1,x1),(f2,x2))
k = int(sys.argv[1])
for a in [float(x) for x in sys.argv[2:]]:
    f, e = best(k, a); print(f"k={k} a={a} Phi~{f:+.6f} eta={e:.4f}", flush=True)
