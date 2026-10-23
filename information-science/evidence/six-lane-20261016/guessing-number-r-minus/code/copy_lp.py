"""Entropy LP with copy-lemma extensions (valid for all entropic vectors), HiGHS float solve.

Base variables 0..9 (vertices 1..10).  A copy step (X, Y): new variables X' (one per element of X);
constraints h(S'+T) = h(S+T) for all S subset X, T subset Y, and I(X'; rest | Y) = 0, i.e.
h(all_base + X') - h(all_base) - h(X'+Y) + h(Y) = 0.  Several independent blocks may share the base:
each block has its own copies; the LP couples them only through base-subset entropies.
Elemental Shannon inequalities are imposed on every block's full variable set.
"""
import numpy as np
import highspy

def elemental_rows(n):
    """Yield elemental inequalities on n variables as lists of (mask, coeff)."""
    full = (1 << n) - 1
    rows = []
    for i in range(n):
        rows.append(((full, 1), (full ^ (1 << i), -1)))
    for i in range(n):
        for j in range(i + 1, n):
            rest = full ^ (1 << i) ^ (1 << j)
            K = rest
            while True:
                r = [(K | 1 << i, 1), (K | 1 << j, 1), (K | 1 << i | 1 << j, -1)]
                if K: r.append((K, -1))
                rows.append(tuple(r))
                if K == 0: break
                K = (K - 1) & rest
    return rows

class Model:
    def __init__(self, nbm, base_n=10):
        self.base_n = base_n; self.nbm = nbm
        self.var = {}  # (block, mask) -> column; base masks shared under block None
        self.ge = []; self.eq = []
        self.blocks = []

    def col(self, block, mask, nb):
        # masks within a block use bits 0..base_n-1 for base and base_n.. for copies
        if mask >> self.base_n == 0:
            key = (None, mask)
        else:
            key = (block, mask)
        if key not in self.var:
            self.var[key] = len(self.var)
        return self.var[key]

    def add_block(self, copies):
        """copies: list of (X_list, Y_list) applied sequentially within this block (later steps may copy
        earlier copies: elements are indices into the block's current variable list)."""
        b = len(self.blocks); n = self.base_n
        nvars = n
        allbase = (1 << n) - 1
        for X, Y in copies:
            Xm = sum(1 << x for x in X); Ym = sum(1 << y for y in Y)
            newbits = {}
            for x in X:
                newbits[x] = nvars; nvars += 1
            # distribution equality: for S subset X, T subset Y
            Xs = list(X)
            for s in range(1 << len(Xs)):
                S = sum(1 << Xs[t] for t in range(len(Xs)) if s >> t & 1)
                Sp = sum(1 << newbits[Xs[t]] for t in range(len(Xs)) if s >> t & 1)
                T = Ym
                while True:
                    if S | T and Sp:
                        self.eq.append(((b, Sp | T, 1), (b, S | T, -1)))
                    if T == 0: break
                    T = (T - 1) & Ym
            # conditional independence of the copy from everything else (current variables) given Y
            cur_all = (1 << (nvars - len(Xs))) - 1  # variables existing before this copy
            Xp = sum(1 << newbits[x] for x in Xs)
            row = [(b, cur_all | Xp, 1), (b, cur_all, -1), (b, Xp | Ym, -1)]
            if Ym: row.append((b, Ym, 1))
            self.eq.append(tuple(row))
        self.blocks.append(nvars)
        for r in elemental_rows(nvars):
            self.ge.append(tuple((b, m, c) for m, c in r))

    def solve(self, singleton_cap=1.0, extra_ge=(), sym_perms=(), options=None):
        n = self.base_n
        for v in range(n):  # FD on base
            Nv = self.nbm[v]
            row = [(None, Nv | 1 << v, 1)]
            if Nv: row.append((None, Nv, -1))
            self.eq.append(tuple(row))
        for p in sym_perms:  # base symmetry h(S) = h(pS); p: list mapping base index -> base index
            for S in range(1, 1 << n):
                pS = 0
                for i in range(n):
                    if S >> i & 1: pS |= 1 << p[i]
                if pS != S:
                    self.eq.append(((None, S, 1), (None, pS, -1)))
        cols = {}
        def cid(b, m):
            key = (None, m) if m >> n == 0 else (b, m)
            if key not in cols: cols[key] = len(cols)
            return cols[key]
        starts = []; idx = []; val = []; rl = []; ru = []
        inf = highspy.kHighsInf
        def emit(row, lo, hi):
            acc = {}
            for b, m, c in row:
                if m == 0: continue
                k = cid(b, m); acc[k] = acc.get(k, 0) + c
            acc = {k: v for k, v in acc.items() if v}
            if not acc: return
            starts.append(len(idx))
            for k, v in acc.items(): idx.append(k); val.append(float(v))
            rl.append(lo); ru.append(hi)
        for r in self.ge: emit(r, 0.0, inf)
        for r in extra_ge: emit(r, 0.0, inf)
        for r in self.eq: emit(r, 0.0, 0.0)
        full = (1 << n) - 1
        objc = cid(None, full)
        ncol = len(cols)
        cost = np.zeros(ncol); cost[objc] = 1.0
        lower = np.zeros(ncol); upper = np.full(ncol, inf)
        for v in range(n):
            upper[cid(None, 1 << v)] = singleton_cap
        h = highspy.Highs(); h.silent()
        for k, v in (options or {}).items(): h.setOptionValue(k, v)
        lp = highspy.HighsLp(); lp.num_col_ = ncol; lp.num_row_ = len(starts)
        lp.col_cost_ = cost; lp.col_lower_ = lower; lp.col_upper_ = upper
        lp.row_lower_ = np.array(rl); lp.row_upper_ = np.array(ru)
        lp.a_matrix_.format_ = highspy.MatrixFormat.kRowwise
        lp.a_matrix_.start_ = np.array(starts + [len(idx)], dtype=np.int32)
        lp.a_matrix_.index_ = np.array(idx, dtype=np.int32)
        lp.a_matrix_.value_ = np.array(val)
        lp.sense_ = highspy.ObjSense.kMaximize
        h.passModel(lp); h.run()
        st = h.modelStatusToString(h.getModelStatus())
        xs = np.array(h.getSolution().col_value)
        hbase = np.zeros(1 << n)
        for (b, m), k in cols.items():
            if b is None: hbase[m] = xs[k]
        self.last_hbase = hbase
        return st, h.getInfo().objective_function_value, ncol, len(starts)
