"""Further structured ansatzes (STS-level KM feasibility only):
  phiB : B2 = phi(B1), phi = multiplication by a fixed non-square n on both copies
         (phi normalizes G; tie x[B1,U] = x[B2,phi(U)]).
  sigS : S additionally invariant under sigma:(x,0)->(x,1),(x,1)->(n x,0) (not in G).
  both : phiB and sigS together."""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from km2 import KM2
from satlib import solve

def order_mod(a, q):
    k, x = 1, a % q
    while x != 1:
        x = x * a % q; k += 1
    return k

q = int(sys.argv[1]); mode = sys.argv[2]; out = sys.argv[3]
m = (q - 1) // 2
g = next(a for a in range(2, q) if order_mod(a, q) == m)
n0 = next(a for a in range(2, q) if pow(a, m, q) == q - 1)
n = 2 * q + 1; inf = 2 * q
def P(f):
    o = [0] * n
    for j in range(2):
        for x in range(q):
            x2, j2 = f(x, j)
            o[q * j + x] = q * j2 + (x2 % q)
    o[inf] = inf
    return tuple(o)
tau = P(lambda x, j: (x + 1, j)); mg = P(lambda x, j: (g * x, j))
phi = P(lambda x, j: (n0 * x, j))
sigma = P(lambda x, j: (x, 1) if j == 0 else (n0 * x, 0))
bases = [([mg], [sigma] if mode in ("sigS", "both") else []), ([tau], []), ([tau], [])]
M = KM2(n, [tau, mg], bases, names=["S0", "B1", "B2"])
cnf, rv = M.cnf()
if mode in ("phiB", "both"):
    idx = {}
    for i, (j, U, c) in enumerate(M.rows):
        idx[(j, frozenset(U))] = i
    trip = M.trip; tid = M.tid
    import numpy as np
    ties = 0
    for i, (j, U, c) in enumerate(M.rows):
        if j != 1: continue
        img = frozenset(int(tid[phi[trip[t][0]], phi[trip[t][1]], phi[trip[t][2]]]) for t in U)
        k = idx.get((2, img))
        if k is None:
            cnf.add([-rv[i]])
        else:
            cnf.add([-rv[i], rv[k]]); cnf.add([rv[i], -rv[k]]); ties += 1
os.makedirs(out, exist_ok=True)
p = os.path.join(out, f"km_{mode}_q{q}.cnf"); sha = cnf.write(p)
st, model, dt = solve(p, "kissat", timeout=900, seed=0)
print(json.dumps({"q": q, "mode": mode, **M.summary(), "status": st, "seconds": round(dt, 3), "cnf_sha256": sha}))
