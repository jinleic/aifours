"""Read-only verifier (v1.1, Codex finding 3): loads the FROZEN u2_dual_certificates.json and checks every stored
dual point exactly (Fractions): dimensions, signs (w, y, u, v >= 0), every dual inequality
  w_S + 3^{4-|S|} z + t_S y + sum_tau G_{tau S} (v_tau - u_tau) >= obj_S,  obj_S = C(|S|,2) 4 3^{4-|S|},
and bound = sum w/16 + k z + y + sum v/16 <= K_k(T_2), with K_k(T_2) recomputed from the spectrum
(6, 3x4, 1x6, 0x5). Writes nothing. Mutation control: the same check against K_k(T_2) - 1/1000 must fail.
"""
import itertools
import json
import sys
from fractions import Fraction as Fr
from math import comb, prod

subsets = [S for r in range(5) for S in itertools.combinations(range(4), r)]
taus = list(itertools.product((0, 1), repeat=4))


def g(inS, t):
    return (Fr(1, 2) if t == 0 else Fr(-1, 2)) if inS else (Fr(1, 2) if t == 0 else Fr(3, 2))


G = [[prod(g(l in S, t[l]) for l in range(4)) for S in subsets] for t in taus]
obj = [Fr(comb(len(S), 2) * 4 * 3 ** (4 - len(S))) for S in subsets]
tr = [Fr(3 ** (4 - len(S))) for S in subsets]
ts = [Fr(1, 2) ** len(S) * Fr(3, 2) ** (4 - len(S)) for S in subsets]
spec = sorted([comb(z, 2) for z in range(5) for _ in range(comb(4, z))], reverse=True)

path = sys.argv[1] if len(sys.argv) > 1 else "u2_dual_certificates.json"
data = json.load(open(path))
all_ok = True
for key, rec in sorted(data.items(), key=lambda kv: int(kv[0])):
    k = int(key)
    c = rec["certificate"]
    w = [Fr(x) for x in c["w"]]; u = [Fr(x) for x in c["u"]]; v = [Fr(x) for x in c["v"]]
    z, y = Fr(c["z"]), Fr(c["y"])
    dims = len(w) == 16 and len(u) == 16 and len(v) == 16
    signs = all(x >= 0 for x in w + u + v) and y >= 0
    ineq = all(w[j] + tr[j] * z + ts[j] * y + sum(G[i][j] * (v[i] - u[i]) for i in range(16)) >= obj[j]
               for j in range(16))
    bound = sum(w) / 16 + k * z + y + sum(v) / 16
    target = Fr(sum(spec[:k]))
    ok = dims and signs and ineq and bound <= target
    mutant = dims and signs and ineq and bound <= target - Fr(1, 1000)
    all_ok &= ok and not mutant
    print(f"k={k:2d} dims={dims} signs={signs} dual_ineqs={ineq} bound={bound} K_k(T2)={target} "
          f"VERIFIED={ok} mutant_passes={mutant}")
print("ALL_VERIFIED" if all_ok else "FAILURE")
