"""Delsarte (Lovasz-theta-type) LP upper bound for the guessing game on a graph G with alphabet Z_q.

Winning set C (all players correct) <=> no two words of C differ by z with some v in supp(z) having
supp(z) cap N(v) empty.  So C is independent in Cay(Z_q^n, S),
S = {z : exists v in supp z with N(v) cap supp z = empty}.
For phi = 1_C * 1_{-C} / |C|: phi(0)=1, phi=0 on S, phi>=0, phi-hat>=0, sum phi = |C|.  Averaging over
coordinate scalings (Z_q^*)^n makes phi depend only on P = supp(z); with psi(P) = sum_{supp z = P} phi(z):
  max sum_P psi(P)  s.t. psi(empty)=1, psi>=0, psi(P)=0 unless G[P] has no isolated vertex,
  for every Q:  sum_P psi(P) * (-1/(q-1))^{|P cap Q|} >= 0.
Then |C| <= LP value, so gn(G,q) <= log_q(LP).  Floating HiGHS here; exact certification separately.
"""
import sys, os, json, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks

def isolate_free_patterns(nbm, n=10):
    out = []
    for P in range(1 << n):
        ok = True
        for v in range(n):
            if (P >> v) & 1 and (nbm[v] & P) == 0:
                ok = False; break
        if ok: out.append(P)
    return out  # includes 0

def solve(edges, q, n=10):
    import highspy
    nbm = nbmasks(edges, n)
    pats = isolate_free_patterns(nbm, n)
    pc = [bin(P).count("1") for P in range(1 << n)]
    r = -1.0 / (q - 1)
    h = highspy.Highs(); h.silent()
    inf = highspy.kHighsInf
    nv = len(pats)
    lower = np.zeros(nv); upper = np.full(nv, inf)
    i0 = pats.index(0); lower[i0] = upper[i0] = 1.0
    cost = np.ones(nv)
    # constraint rows for each Q
    rows_start = []; idx = []; val = []
    for Q in range(1 << n):
        rows_start.append(len(idx))
        for j, P in enumerate(pats):
            idx.append(j); val.append(r ** pc[P & Q])
    lp = highspy.HighsLp()
    lp.num_col_ = nv; lp.num_row_ = 1 << n
    lp.col_cost_ = cost; lp.col_lower_ = lower; lp.col_upper_ = upper
    lp.row_lower_ = np.zeros(1 << n); lp.row_upper_ = np.full(1 << n, inf)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(rows_start + [len(idx)], dtype=np.int32)
    lp.a_matrix_.index_ = np.array(idx, dtype=np.int32)
    lp.a_matrix_.value_ = np.array(val)
    lp.sense_ = highspy.ObjSense.kMaximize
    h.passModel(lp); h.run()
    st = h.modelStatusToString(h.getModelStatus())
    obj = h.getInfo().objective_function_value
    sol = np.array(h.getSolution().col_value)
    return st, obj, dict(zip(pats, sol)), len(pats)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "Rminus"
    edges = R_MINUS_EDGES if which == "Rminus" else R_EDGES
    res = []
    for q in [2, 3, 4, 5, 7, 8, 9, 16, 27, 32, 64, 81, 256, 1024, 4096, 65536, 2 ** 20]:
        st, obj, sol, npat = solve(edges, q)
        res.append(dict(q=q, status=st, theta=obj, exponent=math.log(obj) / math.log(q), patterns=npat))
        print(json.dumps(res[-1])); sys.stdout.flush()
