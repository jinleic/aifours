"""Ansatzes allowed by Proposition C (framework-2q1.md):
  sN   : S invariant under multiplication by a non-square n (so under all of F_q^*).
  bInv : B1 invariant under the twisted involution x_0 -> -x_0, x_1 -> -(x_1 - 1) + 1 (center d=1).
  bInv2: both B1 (center 1) and B2 (center n) invariant under their twisted involutions.
STS-level KM feasibility only."""
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
            x2, j2 = f(x, j); o[q * j + x] = q * j2 + (x2 % q)
    o[inf] = inf; return tuple(o)
tau = P(lambda x, j: (x + 1, j)); mg = P(lambda x, j: (g * x, j))
phi = P(lambda x, j: (n0 * x, j))
inv1 = P(lambda x, j: (-x, 0) if j == 0 else (-(x - 1) + 1, 1))
invn = P(lambda x, j: (-x, 0) if j == 0 else (-(x - n0) + n0, 1))
bases = [([mg], [phi] if mode == "sN" else []), ([tau], [inv1] if mode in ("bInv", "bInv2") else []),
         ([tau], [invn] if mode == "bInv2" else [])]
M = KM2(n, [tau, mg], bases, names=["S0", "B1", "B2"])
cnf, rv = M.cnf()
os.makedirs(out, exist_ok=True)
p = os.path.join(out, f"km_{mode}_q{q}.cnf"); sha = cnf.write(p)
st, model, dt = solve(p, "kissat", timeout=900, seed=0)
print(json.dumps({"q": q, "mode": mode, **M.summary(), "status": st, "seconds": round(dt, 3), "cnf_sha256": sha}))
