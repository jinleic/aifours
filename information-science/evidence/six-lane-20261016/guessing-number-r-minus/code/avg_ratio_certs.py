"""Exact certificates for the 9-vertex screen of avg_ratio_subgraphs.py:
for every w, on R^- - w (W = V - w):  h(W) <= (2/3) sum_{v in W} h(v)  for all FD-consistent polymatroids.
Identity checked coefficient-wise in Fractions:
   h(W) = (2/3) sum_v h(v) - sum_k y_k g_k(h) + sum_e z_e f_e(h) - sum_S c_S h(S),   y, c >= 0,
g_k elemental Shannon rows, f_e FD rows h(N[v]&W) - h(N(v)&W).  (floats only propose multipliers)."""
import sys, os, json
from fractions import Fraction as F
from collections import Counter
import numpy as np, highspy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES
from copy_lp import elemental_rows
NB = {v: set() for v in range(1, 11)}
for a, b in R_MINUS_EDGES: NB[a].add(b); NB[b].add(a)

def certify_W(W, maxden=10**6):
    W = sorted(W); k = len(W); pos = {v: i for i, v in enumerate(W)}
    G = [{m: c for m, c in r if m} for r in elemental_rows(k)]
    Fd = []
    for v in W:
        N = sum(1 << pos[u] for u in NB[v] if u in pos); r = {N | 1 << pos[v]: 1}
        if N: r[N] = -1
        Fd.append(r)
    norm = {1 << i: 1 for i in range(k)}
    rows = G + Fd + [norm]; lo = [0.0] * len(G) + [0.0] * len(Fd) + [1.0]
    hi = [highspy.kHighsInf] * len(G) + [0.0] * len(Fd) + [1.0]
    ncol = (1 << k) - 1; starts, idx, val = [], [], []
    for r in rows:
        starts.append(len(idx))
        for mk, c in r.items(): idx.append(mk - 1); val.append(float(c))
    h = highspy.Highs(); h.silent(); lp = highspy.HighsLp()
    lp.num_col_ = ncol; lp.num_row_ = len(rows); cost = np.zeros(ncol); cost[ncol - 1] = 1.0
    lp.col_cost_ = cost; lp.col_lower_ = np.zeros(ncol); lp.col_upper_ = np.full(ncol, highspy.kHighsInf)
    lp.row_lower_ = np.array(lo); lp.row_upper_ = np.array(hi)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts + [len(idx)], dtype=np.int32)
    lp.a_matrix_.index_ = np.array(idx, dtype=np.int32); lp.a_matrix_.value_ = np.array(val)
    lp.sense_ = highspy.ObjSense.kMaximize; h.passModel(lp); h.run()
    sol = h.getSolution(); rd = np.array(sol.row_dual); cd = np.array(sol.col_dual)
    q = lambda x: F(float(x)).limit_denominator(maxden)
    y = [max(F(0), -q(t)) for t in rd[:len(G)]]
    z = [q(t) for t in rd[len(G):len(G) + len(Fd)]]
    lam = q(rd[-1]); c = [max(F(0), -q(t)) for t in cd]
    acc = Counter(); acc[(1 << k) - 1] += 1
    for i in range(k): acc[1 << i] -= lam
    for t, r in zip(y, G):
        if t:
            for mk, x in r.items(): acc[mk] += t * x
    for t, r in zip(z, Fd):
        if t:
            for mk, x in r.items(): acc[mk] -= t * x
    for j, t in enumerate(c):
        if t: acc[j + 1] += t
    resid = {m: x for m, x in acc.items() if x}
    return dict(W=W, lam=str(lam), identity_exact=(not resid) and lam == F(2, 3), residual_terms=len(resid),
                nnz_y=sum(1 for t in y if t), nnz_c=sum(1 for t in c if t),
                y={str(i): str(t) for i, t in enumerate(y) if t}, z={str(i): str(t) for i, t in enumerate(z) if t},
                c={str(j + 1): str(t) for j, t in enumerate(c) if t})

if __name__ == "__main__":
    out = {}
    for w in range(1, 11):
        r = certify_W([u for u in range(1, 11) if u != w]); out[f"minus{w}"] = r
        print("minus", w, "lam", r["lam"], "identity_exact", r["identity_exact"], "residual", r["residual_terms"], flush=True)
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "certs", "avg-ratio-9vertex.json"), "w"))
    sys.exit(0 if all(r["identity_exact"] for r in out.values()) else 1)
