"""Quick STS-level feasibility tests of extra-symmetry ansatzes in the 2q+1 framework.
modes: twistB1 (only B1 twisted by psi of order m/3), sE1/sE2 (S additionally invariant
under an order-3 element g commuting with Q that cycles three of the four Q-orbits
Q0,N0,Q1,N1 and acts as omega on the fourth).  Prints KM status only (no resolution)."""
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
om = next(a for a in range(2, q) if order_mod(a, q) == 3)
n = 2 * q + 1; inf = 2 * q
Qs = {pow(g, k, q) for k in range(m)}
def P(f):
    o = [0] * n
    for j in range(2):
        for x in range(q):
            x2, j2 = f(x, j)
            o[q * j + x] = q * j2 + (x2 % q)
    o[inf] = inf
    return tuple(o)
tau = P(lambda x, j: (x + 1, j)); mg = P(lambda x, j: (g * x, j))
inv = lambda a: pow(a, q - 2, q)
def cyc(orbs_cycle, fourth):
    # orbs: (j, cls) with cls in {'Q','N'}; cycle A->B->C->A by multipliers; fourth gets omega
    def cls(x): return 'Q' if x in Qs else 'N'
    A, B, C = orbs_cycle
    # multipliers: A->B by c1, B->C by c2, C->A by c3, with c1 c2 c3 = 1 and classes matching
    def mult_for(src, dst):
        return 1 if src[1] == dst[1] else n0
    c1 = mult_for(A, B); c2 = mult_for(B, C); c3 = inv(c1 * c2 % q)
    def f(x, j):
        if x == 0: return (x, j)
        o = (j, cls(x))
        if o == A: return (c1 * x, B[0])
        if o == B: return (c2 * x, C[0])
        if o == C: return (c3 * x, A[0])
        return (om * x, j)
    return P(f)
bases = [([mg], []), ([tau], []), ([tau], [])]
if mode == "sE1":
    bases[0] = ([mg], [cyc(((0,'Q'),(0,'N'),(1,'Q')), (1,'N'))])
elif mode == "sE2":
    bases[0] = ([mg], [cyc(((0,'Q'),(1,'Q'),(1,'N')), (0,'N'))])
elif mode == "sE3":
    bases[0] = ([mg], [cyc(((0,'Q'),(1,'N'),(0,'N')), (1,'Q'))])
elif mode == "twistB1":
    mp = m // 3
    lam = next(a for a in range(2, q) if order_mod(a, q) == mp)
    bases[1] = ([tau], [P(lambda x, j: (lam * x, 0) if j == 0 else (lam * (x - 1) + 1, 1))])
M = KM2(n, [tau, mg], bases, names=["S0", "B1", "B2"])
cnf, rv = M.cnf()
os.makedirs(out, exist_ok=True)
p = os.path.join(out, f"km_{mode}_q{q}.cnf"); sha = cnf.write(p)
st, model, dt = solve(p, "kissat", timeout=600, seed=0)
print(json.dumps({"q": q, "mode": mode, **M.summary(), "status": st, "seconds": round(dt, 3), "cnf_sha256": sha}))
