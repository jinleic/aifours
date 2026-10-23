"""Real SDP over the 8-parameter genus-2 family: maximize a uniform normalized margin tau such that
(i) every pair count x = c + V s is >= tau * rowscale  (AMH Eq. (34) nonnegativity, relaxed to reals)
(ii) every AMH block D^{-1/2} B_(a,k)(s) D^{-1/2} - tau I >= 0  (AMH Eq. (31)), D = |diag B| at the LP center.
Variables s = s_c + w * u around the LP center s_c (family_lp_center.json); floating point exploration only.
"""
import json
import pickle

import cvxpy as cp
import numpy as np

from g2_polytope import load_space

if __name__ == "__main__":
    keys, piv, free, c, V = load_space()
    nf = len(free)
    cf = np.array([float(x) for x in c])
    Vf = np.array([[float(x) for x in row] for row in V])
    rng = json.load(open("../evidence/g2_polytope_ranges.json"))
    lo = np.array([(rng[str(keys[f])][1] or 0.0) for f in free])
    hi = np.array([rng[str(keys[f])][3] for f in free])
    w = np.maximum(hi - lo, 1.0)
    sc = np.array(json.load(open("../evidence/family_lp_center.json"))["s"])
    rs = np.abs(cf + Vf @ sc) + np.abs(Vf) @ w + 1.0
    u = cp.Variable(nf)
    tau = cp.Variable()
    Vu = (Vf * w[None, :]) / rs[:, None]
    x0 = (cf + Vf @ sc) / rs
    cons = [x0 + Vu @ u >= tau, u >= -sc / w]
    blk = pickle.load(open("../evidence/amh_blocks24_exact.pkl", "rb"))
    nblk = 0
    report = []
    for b in blk["blocks"]:
        if not b["nonzero"]:
            continue
        Bs = [np.array([[float(v) for v in row] for row in M]) for M in b["B"]]
        Bc = Bs[0] + sum(sc[f] * Bs[f + 1] for f in range(nf))
        d = np.abs(np.diag(Bc))
        d = np.where(d > 0, d, np.max(d) if np.max(d) > 0 else 1.0)
        Dm = 1.0 / np.sqrt(d)
        A0 = Dm[:, None] * Bc * Dm[None, :]
        Af = [Dm[:, None] * (w[f] * Bs[f + 1]) * Dm[None, :] for f in range(nf)]
        report.append((b["a"], b["k"], float(np.linalg.eigvalsh((A0 + A0.T) / 2).min())))
        expr = A0 + sum(u[f] * Af[f] for f in range(nf))
        m = A0.shape[0]
        Sv = cp.Variable((m, m), symmetric=True)
        cons += [Sv == (expr + expr.T) / 2 - tau * np.eye(m), Sv >> 0]
        nblk += 1
    report.sort(key=lambda r: r[2])
    print("most negative normalized block eigenvalues at LP center:", report[:6])
    cons.append(tau <= 1)
    prob = cp.Problem(cp.Maximize(tau), cons)
    prob.solve(solver="CLARABEL")
    sv = None if u.value is None else (sc + w * u.value)
    print(json.dumps({"n_blocks": nblk, "status": prob.status,
                      "tau": None if tau.value is None else float(tau.value),
                      "s": None if sv is None else [float(v) for v in sv]}))
    if sv is not None:
        json.dump({"s": [float(v) for v in sv], "tau": float(tau.value)},
                  open("../evidence/family_sdp_center.json", "w"))
