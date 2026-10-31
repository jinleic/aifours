#!/usr/bin/env python3
"""reviewer-positive-search2-v1.py  (review f137, reviewer-written, exploratory)

Second positive-control search for Fourier-product QLSs with a transversal:
  (a) order 4, the complete one-parameter family F4(x) = [[1,1,1,1],[1,x,-1,-x],[1,-1,1,-1],[1,-x,-1,x]], |x|=1
      (every 4x4 complex Hadamard is equivalent to one of these; the transversal property is equivalence-invariant),
      numeric grid over x = e^{i theta}, all 4!*4! (sigma,pi); report min over (theta,sigma,pi) of the max |inner product|.
  (b) order 10, K = F2 (x) F5 in BLOCK coordinates t -> (t div 5, t mod 5) (not the CRT isomorphism), exact search in
      Q(zeta10) with sigma(0)=0, pi(0)=0, backtracking on pi for every sigma (9! sigmas), bounded by a time budget.
  (c) order 5 (odd) sanity: K = F5, the diagonal is a transversal (control that the finder works).
"""
import importlib.util, json, subprocess, time, sys
from itertools import permutations, combinations
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("rc", HERE / "reviewer-cyclo-v1.py")
rc = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rc)
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()
T0 = clock(); t0 = time.monotonic(); out = {"clock_start": T0}

# (a) F4(x) numeric
perms4 = list(permutations(range(4)))
best = (9.0, None)
F4char = np.exp(2j * np.pi * np.outer(np.arange(4), np.arange(4)) / 4)      # [t, r] = i^{rt}
for k in range(720):
    th = 2 * np.pi * k / 720; x = np.exp(1j * th)
    K = np.array([[1, 1, 1, 1], [1, x, -1, -x], [1, -1, 1, -1], [1, -x, -1, x]])
    assert np.allclose(K.conj().T @ K, 4 * np.eye(4))
    for sig in perms4:
        Ks = K[list(sig), :]
        for pi in perms4:
            W = F4char * Ks[:, list(pi)]            # W[t, r] = i^{rt} K[sigma(t)][pi(r)]
            G = W.conj().T @ W
            off = np.max(np.abs(G - np.diag(np.diag(G))))
            if off < best[0]:
                best = (float(off), {"theta_deg": 360 * k / 720, "sigma": list(sig), "pi": list(pi)})
out["order4_F4x_grid720"] = {"min_max_offdiag": best[0], "argmin": best[1], "transversal_found": best[0] < 1e-9}
print("order4 F4(x) grid:", out["order4_F4x_grid720"], flush=True)

# (c) odd order 5 sanity
C5 = rc.Cyclo(5)
F5 = [[(t * d) % 5 for d in range(5)] for t in range(5)]
sigma = tuple(range(5)); pi = tuple(range(5))
ok = all(C5.vanishes([(r2 - r) * t + F5[sigma[t]][pi[r2]] - F5[sigma[t]][pi[r]] for t in range(5)]) for r, r2 in combinations(range(5), 2))
out["order5_F5_diagonal_is_transversal"] = ok
print("order5 F5 diagonal transversal:", ok, flush=True)

# (b) order 10 block F2 x F5, exact
C10 = rc.Cyclo(10)
K = [[(5 * ((t // 5) * (r // 5)) + 2 * ((t % 5) * (r % 5))) % 10 for r in range(10)] for t in range(10)]
assert all(C10.vanishes([K[t][c] - K[t][d] for t in range(10)]) for c, d in combinations(range(10), 2))
budget = float(sys.argv[1]) if len(sys.argv) > 1 else 300.0
deadline = time.monotonic() + budget
found = None; sigmas_tried = 0
for rest in permutations(range(1, 10)):
    if time.monotonic() > deadline: break
    sigma = (0,) + rest; sigmas_tried += 1
    # half-graph necessary condition first: E = sigma(even) must have a perfect matching in the half graph
    E = [sigma[t] for t in range(0, 10, 2)]
    edges = [(c, d) for c, d in rc.PAIRS if C10.vanishes([K[t][d] - K[t][c] for t in E])]
    if not rc.has_pm(rc.edges_to_mask(edges)):
        continue
    pi = [0] + [None] * 9
    def ok_pair(r, c, r2, c2):
        return C10.vanishes([(r2 - r) * t + K[sigma[t]][c2] - K[sigma[t]][c] for t in range(10)])
    def rec(r):
        if r == 10: return True
        for c in range(10):
            if c in pi[:r]: continue
            if all(ok_pair(r2, pi[r2], r, c) for r2 in range(r)):
                pi[r] = c
                if rec(r + 1): return True
                pi[r] = None
        return False
    if rec(1):
        found = {"sigma": list(sigma), "pi": list(pi)}
        print("order10 block F2xF5 FOUND", found, flush=True)
        break
out["order10_block_F2xF5"] = {"sigmas_tried_of_362880": sigmas_tried, "found": found, "time_budget_s": budget}
print("order10 block F2xF5:", out["order10_block_F2xF5"], flush=True)
out["elapsed_seconds"] = time.monotonic() - t0; out["clock_end"] = clock()
(HERE / "reviewer-positive-search2-result-v1.json").write_text(json.dumps(out, indent=1) + "\n")
