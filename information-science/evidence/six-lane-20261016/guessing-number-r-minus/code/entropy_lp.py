"""Entropy LP bounds for guessing games (Shannon / +extra linear inequality rows), HiGHS float solve.

Variables h[S] for nonempty S subset [n] (bitmask), h[0]=0 implicit.  Constraints:
  elemental Shannon: h(V)-h(V-i) >= 0 ; h(K+i)+h(K+j)-h(K+i+j)-h(K) >= 0 (i<j, K subset V-{i,j})
  game: h(N[v]) - h(N(v)) = 0 for each v ; h({v}) <= 1
Objective: max h(V).  Extra rows are dicts {mask: coeff} meaning sum coeff*h[mask] >= 0.
Exact certification is done separately (certify.py) from the returned dual values.
"""
import numpy as np
import highspy

def elemental(n):
    full = (1 << n) - 1
    rows = []
    for i in range(n):
        rows.append({full: 1, full ^ (1 << i): -1})
    for i in range(n):
        for j in range(i + 1, n):
            rest = full ^ (1 << i) ^ (1 << j)
            K = rest
            while True:
                r = {}
                for m, c in ((K | 1 << i, 1), (K | 1 << j, 1), (K | 1 << i | 1 << j, -1), (K, -1)):
                    if m: r[m] = r.get(m, 0) + c
                rows.append({k: v for k, v in r.items() if v})
                if K == 0: break
                K = (K - 1) & rest
    return rows

def game_rows(nbm, n):
    eq = []
    for v in range(n):
        Nv = nbm[v]
        r = {Nv | (1 << v): 1}
        if Nv: r[Nv] = r.get(Nv, 0) - 1
        eq.append(r)
    return eq

def solve(nbm, n=10, extra_ge=(), want_duals=True, singleton_cap=1.0):
    full = (1 << n) - 1
    nvar = full  # variable index = mask-1
    ge = elemental(n) + list(extra_ge)
    eq = game_rows(nbm, n)
    h = highspy.Highs(); h.silent()
    inf = highspy.kHighsInf
    lp = highspy.HighsLp()
    lp.num_col_ = nvar
    cost = np.zeros(nvar); cost[full - 1] = 1.0
    lower = np.zeros(nvar); upper = np.full(nvar, inf)
    for v in range(n):
        upper[(1 << v) - 1] = singleton_cap
    lp.col_cost_ = cost; lp.col_lower_ = lower; lp.col_upper_ = upper
    starts = []; idx = []; val = []; rl = []; ru = []
    for r in ge:
        starts.append(len(idx))
        for m, c in r.items(): idx.append(m - 1); val.append(float(c))
        rl.append(0.0); ru.append(inf)
    for r in eq:
        starts.append(len(idx))
        for m, c in r.items(): idx.append(m - 1); val.append(float(c))
        rl.append(0.0); ru.append(0.0)
    lp.num_row_ = len(starts)
    lp.row_lower_ = np.array(rl); lp.row_upper_ = np.array(ru)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts + [len(idx)], dtype=np.int32)
    lp.a_matrix_.index_ = np.array(idx, dtype=np.int32)
    lp.a_matrix_.value_ = np.array(val)
    lp.sense_ = highspy.ObjSense.kMaximize
    h.passModel(lp); h.run()
    st = h.modelStatusToString(h.getModelStatus())
    sol = h.getSolution()
    out = dict(status=st, value=h.getInfo().objective_function_value,
               x=np.array(sol.col_value), row_dual=np.array(sol.row_dual), col_dual=np.array(sol.col_dual),
               ge=ge, eq=eq)
    return out
