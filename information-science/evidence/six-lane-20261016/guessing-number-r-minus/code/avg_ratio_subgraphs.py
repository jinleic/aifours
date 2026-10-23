"""Product/time-sharing factors need Phi = Ing + 3S < 0, i.e. (exactly, by the certificate identity on
codes) H(V) > (2/3) * sum_v H(X_v).  Which vertex sets can host such a factor even at the Shannon level?

For every induced subgraph R^-[W] (vertices outside W constant), solve the float LP
    max h(W)  s.t.  Shannon on W, FD h(N[v] & W) = h(N(v) & W) for v in W, sum_{v in W} h(v) = 1,
and compare with 2/3.  A value <= 2/3 means that no distribution supported on W, even a non-uniform
one, has an average-vertex ratio above 20/3.  This is a float LP screen; any positive finding needs an
exact certificate before use.
"""
import sys, os, json, itertools
import numpy as np, highspy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES
from copy_lp import elemental_rows
NB = {v: set() for v in range(1, 11)}
for a, b in R_MINUS_EDGES: NB[a].add(b); NB[b].add(a)

def solve(W):
    W = sorted(W); k = len(W); pos = {v: i for i, v in enumerate(W)}
    rows = []; lo = []; hi = []
    for r in elemental_rows(k):
        rows.append({m: c for m, c in r if m}); lo.append(0.0); hi.append(highspy.kHighsInf)
    for v in W:
        N = sum(1 << pos[u] for u in NB[v] if u in pos); Nc = N | 1 << pos[v]
        r = {Nc: 1}
        if N: r[N] = -1
        rows.append(r); lo.append(0.0); hi.append(0.0)
    rows.append({1 << i: 1 for i in range(k)}); lo.append(1.0); hi.append(1.0)
    ncol = (1 << k) - 1        # column m-1 for mask m
    starts, idx, val = [], [], []
    for r in rows:
        starts.append(len(idx))
        for mk, c in r.items(): idx.append(mk - 1); val.append(float(c))
    h = highspy.Highs(); h.silent()
    lp = highspy.HighsLp(); lp.num_col_ = ncol; lp.num_row_ = len(rows)
    cost = np.zeros(ncol); cost[ncol - 1] = 1.0
    lp.col_cost_ = cost; lp.col_lower_ = np.zeros(ncol); lp.col_upper_ = np.full(ncol, highspy.kHighsInf)
    lp.row_lower_ = np.array(lo); lp.row_upper_ = np.array(hi)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts + [len(idx)], dtype=np.int32)
    lp.a_matrix_.index_ = np.array(idx, dtype=np.int32); lp.a_matrix_.value_ = np.array(val)
    lp.sense_ = highspy.ObjSense.kMaximize
    h.passModel(lp); h.run()
    return h.modelStatusToString(h.getModelStatus()), h.getInfo().objective_function_value

if __name__ == "__main__":
    res = {}
    full = list(range(1, 11))
    st, v = solve(full); res["all10"] = dict(status=st, value=v, times_10=10 * v)
    print("all 10", st, round(v, 6), "x10 =", round(10 * v, 6), flush=True)
    for w in full:
        W = [u for u in full if u != w]
        st, v = solve(W); res[f"minus{w}"] = dict(status=st, value=v)
        print("minus", w, st, round(v, 6), "(2/3 = 0.666667)", flush=True)
    json.dump(res, open(os.path.join(os.path.dirname(__file__), "..", "evidence", "avg-ratio-subgraphs-float.json"), "w"), indent=1)
