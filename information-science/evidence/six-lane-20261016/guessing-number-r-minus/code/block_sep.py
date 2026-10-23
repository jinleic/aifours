"""Separation oracle for copy-lemma blocks (exploratory floats).

Given a base entropy vector h* (masks over the 10 base variables) and a copy chain, decide whether h*
extends to the chain's variables while satisfying the chain's Shannon and copy constraints.
depth = min t such that every block row is satisfied up to t, with the base fixed to h*.
depth > 0 means the block cuts h*.  Then the block is added to the master LP (copy_lp.Model).
"""
import sys, os, json, itertools, time
import numpy as np
import highspy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks
from copy_lp import Model

N = 10
NBM = nbmasks(R_MINUS_EDGES)
SIG = [7, 9, 6, 5, 8, 2, 3, 0, 1, 4]   # (1 8)(2 10 5 9)(3 7 4 6) in 0-based images
TAU = [0, 4, 5, 6, 1, 2, 3, 7, 8, 9]   # (2 5)(3 6)(4 7)

def group():
    G = {tuple(range(N))}; frontier = [tuple(range(N))]
    while frontier:
        g = frontier.pop(); 
        for s in (SIG, TAU):
            h = tuple(s[g[i]] for i in range(N))
            if h not in G: G.add(h); frontier.append(h)
    return sorted(G)
AUT = group()

def closure(T):
    T = set(T); ch = True
    while ch:
        ch = False
        for v in range(N):
            if v not in T and all(((NBM[v] >> u) & 1) == 0 or u in T for u in range(N)):
                T.add(v); ch = True
    return T

def canon(X, Y):
    return min((tuple(sorted(g[x] for x in X)), tuple(sorted(g[y] for y in Y))) for g in AUT)

def separation_depth(hbase, copies):
    m = Model(NBM); m.add_block(copies)
    cols = {}; starts = []; idx = []; val = []; rl = []; ru = []
    inf = highspy.kHighsInf
    def add(row, eq):
        const = 0.0; acc = {}
        for b, mk, c in row:
            if mk == 0: continue
            if mk >> N == 0: const += c * hbase[mk]
            else:
                k = cols.setdefault(mk, len(cols)); acc[k] = acc.get(k, 0) + c
        acc = {k: v for k, v in acc.items() if v}
        if not acc:
            return const
        # sum acc*x + const + t >= 0   (and for eq also  -(sum acc*x + const) + t >= 0)
        for sgn in ((1,) if not eq else (1, -1)):
            starts.append(len(idx))
            for k, v in acc.items(): idx.append(k); val.append(float(sgn * v))
            idx.append(-1); val.append(1.0)          # t column placeholder
            rl.append(-sgn * const); ru.append(inf)
        return None
    worst = 0.0
    for r in m.ge:
        c = add(r, False)
        if c is not None: worst = max(worst, -c)
    for r in m.eq:
        c = add(r, True)
        if c is not None: worst = max(worst, abs(c))
    tcol = len(cols); ncol = tcol + 1
    idx = [tcol if k == -1 else k for k in idx]
    cost = np.zeros(ncol); cost[tcol] = 1.0
    h = highspy.Highs(); h.silent()
    lp = highspy.HighsLp(); lp.num_col_ = ncol; lp.num_row_ = len(starts)
    lp.col_cost_ = cost; lp.col_lower_ = np.zeros(ncol); lp.col_upper_ = np.full(ncol, inf)
    lp.row_lower_ = np.array(rl); lp.row_upper_ = np.array(ru)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_ = np.array(starts + [len(idx)], dtype=np.int32)
    lp.a_matrix_.index_ = np.array(idx, dtype=np.int32)
    lp.a_matrix_.value_ = np.array(val)
    lp.sense_ = highspy.ObjSense.kMinimize
    h.passModel(lp); h.run()
    st = h.modelStatusToString(h.getModelStatus())
    return st, max(h.getInfo().objective_function_value, worst)

def single_candidates(sizes=(1,)):
    seen = set(); out = []
    for k in sizes:
        for X in itertools.combinations(range(N), k):
            rest = [v for v in range(N) if v not in X]
            for r in range(len(rest) + 1):
                for Y in itertools.combinations(rest, r):
                    if all(x in closure(Y) for x in X): continue     # copy would equal original
                    c = canon(X, Y)
                    if c in seen: continue
                    seen.add(c); out.append(c)
    return out

GURPINAR = [
    [([1], [0, 3, 4, 5, 6, 7, 8, 9])],
    [([3, 4], [0, 1, 2, 5, 6, 7, 8]), ([6], [0, 1, 2, 3, 11, 5, 7, 8])],
    [([5, 6], [0, 1, 2, 3, 4, 7, 8, 9]), ([7], [0, 1, 2, 3, 4, 5, 10, 8, 9])],
]

def master(blocks, options=None):
    m = Model(NBM)
    for b in blocks: m.add_block(b)
    t0 = time.time()
    st, val, nc, nr = m.solve(sym_perms=[SIG, TAU], options=options)
    return st, val, m.last_hbase, round(time.time() - t0, 1), nc, nr
