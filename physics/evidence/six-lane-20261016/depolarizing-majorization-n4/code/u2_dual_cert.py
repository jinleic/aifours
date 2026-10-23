"""Exact dual certificates for the twirled PPT LP of U2(n=4):  K_k(sum_{|I|=2} rho_I (x) 1) <= K_k(sum_{|I|=2} P_I)
for every 4-qubit state, at k in {1..5, 11..15}.  (LP data as in twirl_lp_exact.py.)

Dual of  max obj.c  s.t. c <= 1/16 [w], sum_S 3^{4-|S|} c_S = k [z free], sum_S t_S c_S <= 1 [y],
         -G c <= 0 [u], G c <= 1/16 [v], c >= 0:
  min (1/16) sum w + k z + y + (1/16) sum v   s.t.  w_S + 3^{4-|S|} z + t_S y + sum_tau G_{tau S}(v_tau - u_tau) >= obj_S,
  w, y, u, v >= 0.
Weak duality (all c feasible, c >= 0) makes any exactly feasible dual point an upper bound on the LP, hence on
sup_{rho, Pi} Tr[Pi X_2(rho)] = max_rho K_k(X_2(rho)). Floats from HiGHS are rationalized and re-checked EXACTLY.
Mutation control: the same check with the target lowered by 1/1000 must fail.
"""
import itertools
import json
from fractions import Fraction as Fr
from math import comb

import numpy as np
from scipy.optimize import linprog

n = 4
subsets = [S for r in range(n + 1) for S in itertools.combinations(range(n), r)]
taus = list(itertools.product((0, 1), repeat=n))


def g(inS, tau):
    return (Fr(1, 2) if tau == 0 else Fr(-1, 2)) if inS else (Fr(1, 2) if tau == 0 else Fr(3, 2))


obj = [Fr(comb(len(S), 2) * 4 * 3 ** (n - len(S))) for S in subsets]
tr = [Fr(3 ** (n - len(S))) for S in subsets]
ts = [Fr(1, 2) ** len(S) * Fr(3, 2) ** (n - len(S)) for S in subsets]
G = [[np.prod([g(l in S, t[l]) for l in range(n)]) for S in subsets] for t in taus]
eig = sorted([comb(z, 2) for z in range(n + 1) for _ in range(comb(n, z))], reverse=True)


def certificate(k):
    # variables: w(16), z+(1), z-(1), y(1), u(16), v(16)
    nv = 16 + 2 + 1 + 16 + 16
    cost = np.array([1 / 16] * 16 + [k, -k, 1] + [0] * 16 + [1 / 16] * 16, dtype=float)
    A, b = [], []
    for j in range(16):
        row = [0.0] * nv
        row[j] = 1
        row[16], row[17], row[18] = float(tr[j]), -float(tr[j]), float(ts[j])
        for i in range(16):
            row[19 + i] = -float(G[i][j])
            row[35 + i] = float(G[i][j])
        A.append([-x for x in row]); b.append(-float(obj[j]))
    r = linprog(cost, A_ub=np.array(A), b_ub=np.array(b), bounds=[(0, None)] * nv, method="highs")
    x = [Fr(v).limit_denominator(10 ** 6) for v in r.x]
    x = [max(v, Fr(0)) for v in x]
    w, z, y, u, v = x[:16], x[16] - x[17], x[18], x[19:35], x[35:51]
    ok = all(w[j] + tr[j] * z + ts[j] * y + sum(G[i][j] * (v[i] - u[i]) for i in range(16)) >= obj[j]
             for j in range(16))
    bound = Fr(1, 16) * sum(w) + k * z + y + Fr(1, 16) * sum(v)
    return ok, bound, {"w": [str(t) for t in w], "z": str(z), "y": str(y), "u": [str(t) for t in u],
                       "v": [str(t) for t in v]}


if __name__ == "__main__":
    out = {}
    for k in list(range(1, 6)) + list(range(11, 16)):
        target = Fr(sum(eig[:k]))
        ok, bound, cert = certificate(k)
        proved = ok and bound <= target
        mutant = ok and bound <= target - Fr(1, 1000)          # must be False
        out[k] = {"dual_feasible_exact": ok, "dual_bound": str(bound), "target": str(target),
                  "PROVED": proved, "mutation_control_lowered_target_passes": mutant, "certificate": cert}
        print(f"k={k:2d} dual feasible={ok} bound={bound} target={target} PROVED={proved} mutant_passes={mutant}")
    json.dump(out, open("../evidence/u2_dual_certificates.json", "w"), indent=1)
