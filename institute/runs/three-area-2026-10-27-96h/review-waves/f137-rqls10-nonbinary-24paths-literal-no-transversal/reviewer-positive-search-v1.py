#!/usr/bin/env python3
"""reviewer-positive-search-v1.py  (review f137, reviewer-written, exploratory)

Searches for Fourier-product QLSs WITH an orthogonal transversal, to serve as positive controls for the
half-graph / row-obstruction machinery.  Fourier-product QLS of an n x n Hadamard K with physical order sigma:
cell (r,d) has vector v_{r,d}(t) = zeta_n^{r t} K[sigma(t)][d].  A transversal is a permutation pi with
{v_{r,pi(r)}} orthonormal.  WLOG sigma(0)=0 (coordinate shift) and pi(0)=0 (row shift).
Families searched (all exact, in Z[zeta_m] power bases):
  order 4 : K = Klein character table F2(x)F2 in coordinates t -> (t mod 2, t div 2), and K = F4;
  order 6 : K = Tao's BH(6,3) S6, and K = F6;
  order 10: K[t][r] = zeta10^{rho(t) tau(r) - t r} for bijections rho, tau (then W = F (.) K is the permuted F10 and
            the DIAGONAL {(r,r)} with sigma = id is a transversal iff K is Hadamard); random rho, backtracked tau.
Prints what it finds; writes reviewer-positive-search-result-v1.json.
"""
import importlib.util, json, subprocess, time, random, sys
from itertools import permutations, combinations
from pathlib import Path
HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rc", HERE / "reviewer-cyclo-v1.py")
rc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rc)
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()
T0 = clock(); t0 = time.monotonic()
out = {"clock_start": T0}

def is_hadamard(K, m, C):
    n = len(K)
    return all(C.vanishes([K[t][c] - K[t][d] for t in range(n)]) for c, d in combinations(range(n), 2))

def transversals(K, m, C, limit=5):
    """K: n x n exponent matrix over zeta_m (m multiple of n so zeta_n = zeta_m^{m/n}); returns normalized (sigma, pi) list"""
    n = len(K); f = m // n
    found = []
    rows = list(range(1, n))
    for sig_rest in permutations(rows):
        sigma = (0,) + sig_rest
        # orthogonality of cells (r,c) and (r',c'): sum_t zeta_m^{f (r'-r) t + K[sigma(t)][c'] - K[sigma(t)][c]} == 0
        def ok(r, c, r2, c2):
            return C.vanishes([f * (r2 - r) * t + K[sigma[t]][c2] - K[sigma[t]][c] for t in range(n)])
        # backtrack pi with pi(0)=0
        pi = [0] + [None] * (n - 1)
        def rec(r):
            if r == n:
                found.append((sigma, tuple(pi))); return len(found) >= limit
            used = set(pi[:r])
            for c in range(n):
                if c in used: continue
                if all(ok(r2, pi[r2], r, c) for r2 in range(r)):
                    pi[r] = c
                    if rec(r + 1): return True
                    pi[r] = None
            return False
        if rec(1) and len(found) >= limit:
            break
    return found

# ---------- order 4 ----------
C4 = rc.Cyclo(4)
klein = [[2 * (((t & 1) * (d & 1) + (t >> 1) * (d >> 1)) % 2) for d in range(4)] for t in range(4)]   # exponents of zeta4 (so 0 or 2 => +-1)
f4 = [[(t * d) % 4 for d in range(4)] for t in range(4)]
res4 = {}
for name, K in (("klein_F2xF2", klein), ("F4", f4)):
    assert is_hadamard(K, 4, C4)
    tr = transversals(K, 4, C4)
    res4[name] = {"n_found_up_to_limit": len(tr), "examples": [[list(s), list(p)] for s, p in tr[:3]]}
    print("order4", name, res4[name], flush=True)
out["order4"] = res4

# ---------- order 6 ----------
C6 = rc.Cyclo(6)
w = 2  # omega = zeta6^2
tao = [[0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 2, 2], [0, 1, 0, 2, 2, 1], [0, 1, 2, 0, 1, 2], [0, 2, 2, 1, 0, 1], [0, 2, 1, 2, 1, 0]]
tao6 = [[w * x for x in row] for row in tao]
f6 = [[(t * d) % 6 for d in range(6)] for t in range(6)]
res6 = {}
for name, K in (("tao_BH63", tao6), ("F6", f6)):
    assert is_hadamard(K, 6, C6), name
    tr = transversals(K, 6, C6)
    res6[name] = {"n_found_up_to_limit": len(tr), "examples": [[list(s), list(p)] for s, p in tr[:3]]}
    print("order6", name, res6[name], flush=True)
out["order6"] = res6

# ---------- order 10: K = zeta10^{rho(t)tau(r) - t r} ----------
C10 = rc.Cyclo(10)
def zero_set(rho):
    Z = set()
    for b in range(10):
        for a in range(10):
            if C10.vanishes([a * rho[t] - b * t for t in range(10)]):
                Z.add((b, a))
    return Z
def find_tau(rho, Z):
    tau = [0] + [None] * 9
    def rec(r):
        if r == 10: return True
        for v in range(10):
            if v in tau[:r]: continue
            if all(((r - r2) % 10, (v - tau[r2]) % 10) in Z for r2 in range(r)):
                tau[r] = v
                if rec(r + 1): return True
                tau[r] = None
        return False
    return tuple(tau) if rec(1) else None
rng = random.Random(20261028)
found10 = None; tried = 0; deadline = time.monotonic() + float(sys.argv[1]) if len(sys.argv) > 1 else time.monotonic() + 240
while time.monotonic() < deadline:
    rest = list(range(1, 10)); rng.shuffle(rest); rho = (0,) + tuple(rest)
    tried += 1
    Z = zero_set(rho)
    if sum(1 for (b, a) in Z if b) < 9:   # need at least the 9 differences b=1..9 to be realizable at all
        continue
    tau = find_tau(rho, Z)
    if tau:
        K = [[(rho[t] * tau[r] - t * r) % 10 for r in range(10)] for t in range(10)]
        assert is_hadamard(K, 10, C10)
        found10 = {"rho": list(rho), "tau": list(tau), "K_exponents_mod10": K}
        print("order10 FOUND", found10, flush=True)
        break
out["order10"] = {"family": "zeta10^{rho(t)tau(r)-tr}", "rho_tried": tried, "found": found10}
print("order10 tried", tried, "found" if found10 else "none", flush=True)
out["elapsed_seconds"] = time.monotonic() - t0; out["clock_end"] = clock()
(HERE / "reviewer-positive-search-result-v1.json").write_text(json.dumps(out, indent=1) + "\n")
