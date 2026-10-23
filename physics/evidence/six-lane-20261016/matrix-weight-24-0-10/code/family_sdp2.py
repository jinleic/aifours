"""Full real AMH-SDP over the 8-parameter genus-2 family, well-conditioned formulation:
u-variables (s = sref + w*u) from lp_rank1.py; linear rows = pair-count nonnegativity + 84 rank-1 block
functionals (row-normalized); the 41 general blocks as PSD constraints, each congruence-scaled by
D = |diag B(s_lp)|^{-1/2} at the LP center. Maximize the common margin t. Floating point exploration only.
"""
import json
import pickle

import cvxpy as cp
import numpy as np

from lp_rank1 import rows_and_funcs

if __name__ == "__main__":
    keys, piv, free, c, V, funcs = rows_and_funcs()
    nf = len(free)
    cf = np.array([float(x) for x in c])
    Vf = np.array([[float(x) for x in row] for row in V])
    ctr = json.load(open("../evidence/lp_rank1_center.json"))
    w = np.array(ctr["w"]); sref = np.array(ctr["sref"]); slp = np.array(ctr["s"])
    Arows, brows = [], []
    for i in range(len(cf)):
        a = Vf[i] * w
        bb = cf[i] + Vf[i] @ sref
        if np.abs(a).max() == 0:
            continue
        nrm = max(np.abs(a).max(), abs(bb))
        Arows.append(a / nrm); brows.append(bb / nrm)
    for blkid, k0, kv in funcs:
        kvf = np.array([float(q) for q in kv])
        a = kvf * w
        bb = float(k0) + kvf @ sref
        if np.abs(a).max() == 0:
            continue
        nrm = max(np.abs(a).max(), abs(bb))
        Arows.append(a / nrm); brows.append(bb / nrm)
    A = np.array(Arows); b = np.array(brows)
    u = cp.Variable(nf)
    t = cp.Variable()
    cons = [A @ u + b >= t, sref + cp.multiply(w, u) >= 0, t <= 1]
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    st = json.load(open("../evidence/block_structure.json"))
    general = {tuple(g["block"]) for g in st["general"]}
    nblk = 0
    for bb_ in blk["blocks"]:
        if (bb_["a"], bb_["k"]) not in general:
            continue
        Bs = bb_["B"]
        m = len(bb_["idx"])
        nz = [r for r in range(m) if any(Bs[0][r]) or any(any(Bf[r]) for Bf in Bs[1:])]
        comps = [np.array([[float(M[r][cc]) for cc in nz] for r in nz]) for M in Bs]
        A0 = comps[0] + sum(sref[f] * comps[f + 1] for f in range(nf))
        Af = [w[f] * comps[f + 1] for f in range(nf)]
        Blp = A0 + sum(((slp[f] - sref[f]) / w[f]) * Af[f] for f in range(nf))
        d = np.abs(np.diag(Blp))
        d = np.where(d > 0, d, d.max())
        Dm = 1.0 / np.sqrt(d)
        A0n = Dm[:, None] * A0 * Dm[None, :]
        Afn = [Dm[:, None] * M * Dm[None, :] for M in Af]
        expr = A0n + sum(u[f] * Afn[f] for f in range(nf))
        mm = len(nz)
        S = cp.Variable((mm, mm), symmetric=True)
        cons += [S == (expr + expr.T) / 2 - t * np.eye(mm), S >> 0]
        nblk += 1
    prob = cp.Problem(cp.Maximize(t), cons)
    prob.solve(solver="CLARABEL")
    print(json.dumps({"general_blocks": nblk, "status": prob.status,
                      "t": None if t.value is None else float(t.value)}))
    if u.value is not None:
        s = sref + w * u.value
        json.dump({"s": s.tolist(), "t": float(t.value), "status": prob.status},
                  open("../evidence/family_sdp2_center.json", "w"))
        print("s* =", s.tolist())
