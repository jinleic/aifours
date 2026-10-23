#!/usr/bin/env python3
"""btd_cnf_a.py -- CNF encoding A of BTD(V,B;p1,p2,R;K,L) (lane btd12-15, README 1.6 item A).  Python stdlib.

Variables (thermometer): a[i][j] = [m_ij >= 1], b[i][j] = [m_ij = 2]; clause (-b v a).  Then m_ij = a_ij + b_ij.
Constraints:
  (D2) row i: exactly p1 + p2 of a[i][*] and exactly p2 of b[i][*]   (so exactly p1 ones and p2 twos);
  (D3) column j: exactly K of the 2V literals {a_ij, b_ij : i};
  (D4) rows i < k: exactly L of the 4B products {a_ij a_kj, a_ij b_kj, b_ij a_kj, b_ij b_kj : j}; each product is a
       fully defined AND variable p <-> x & y.  The count equals sum_j m_ij m_kj because m = a + b.
  Every "exactly n" is a Sinz-style unary counter: s[t][c] <-> (at least c of the first t literals), c = 1..n+1,
  defined in both directions; then s[T][n] and not s[T][n+1].
Symmetry (S1, README 1.3): rows lexicographically nondecreasing and columns lexicographically nondecreasing, compared
  through the order-preserving pair map 0 -> (0,0), 1 -> (1,0), 2 -> (1,1) of (a, b), interleaved per entry; every
  adjacent pair X <=lex Y uses "equal-so-far" variables e_t: e_0 = true, e_{t+1} <-> e_t & (X_t <-> Y_t),
  e_t -> (X_t -> Y_t).  Row 0 = 0^z 1^p1 2^p2 (S0, implied by S1) is added as unit clauses.
  --no-symmetry: neither S1 nor S0 (used for counting controls).  --s0-only: S0 units only.
--strengthen (target parameters only): (C1) at most two 2s per column, as all 3-subset clauses on b[*][j].
--lemmas 2|3 (target parameters only; implies --strengthen; README amendment 1.8, proofs in notes/nonexistence-proof.md):
  column-pair counters G_jk[c] <-> g_jk >= c (c = 1..7) over the 4V products of thermometer bits of columns j, k, and
  type indicators d_j <-> (column j has >= 2 twos), o_j <-> (exactly one 2).  Level 2 adds
    (C3) d_j & d_k -> 4 <= g_jk <= 5;  (C4) d_j & o_k -> g_jk >= 4  (Step 2(b));
    (Step 4) d_j -> for every k != j: 3 <= g_jk <= 6, and with c_x = #{k != j : g_jk = x}:
             (c3, c4, c6) = (0, 4, 2) or (1, 1, 1);
    (Step 5) d_j & d_k & g_jk = 4 -> g_jl = g_kl for every other column l.
  Level 3 adds (Steps 6-7, Lemma D) no three type-2 columns with pairwise g = 5.
--fix FILE: add unit clauses fixing every a, b to the matrix in FILE (strict format, same parameters).
--fix-flip i j v: with --fix, replace entry (i, j) of the fixed matrix by v before fixing (mutation control).
Usage: btd_cnf_a.py V B p1 p2 R K L OUT.cnf [options]
Writes OUT.cnf (exclusive) and OUT.cnf.map.json (exclusive: variable numbers of a and b, generator SHA-256, options).
"""
import hashlib
import itertools
import json
import sys


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, *lits):
        self.clauses.append(lits)

    def AND(self, x, y):
        p = self.new()
        self.add(-p, x)
        self.add(-p, y)
        self.add(p, -x, -y)
        return p

    def counter(self, lits, cap):
        """unary counter: r[c] <-> (at least c of lits are true), 1 <= c <= cap; r[c] is None when c > len(lits)"""
        prev = None
        for t, x in enumerate(lits, start=1):
            cur = [None] * (cap + 1)
            for c in range(1, min(t, cap) + 1):
                s = self.new()
                cur[c] = s
                ps = prev[c] if prev is not None else None
                pm = (prev[c - 1] if c - 1 >= 1 else "T") if prev is not None else ("T" if c == 1 else None)
                if ps is not None:
                    self.add(-ps, s)
                if pm == "T":
                    self.add(-x, s)
                elif pm is not None:
                    self.add(-x, -pm, s)
                self.add(*([-s, x] + ([ps] if ps is not None else [])))
                if pm != "T":
                    self.add(*([-s] + ([ps] if ps is not None else []) + ([pm] if pm is not None else [])))
            prev = cur
        return prev if prev is not None else [None] * (cap + 1)

    def exactly(self, lits, n):
        """unary counter over lits; enforce exactly n true"""
        T = len(lits)
        if n > T:
            self.add()  # empty clause: impossible
            return
        prev = None  # prev[c] for c = 1..n+1 (None = constant false); c = 0 is constant true
        for t, x in enumerate(lits, start=1):
            cur = [None] * (n + 2)
            for c in range(1, min(t, n + 1) + 1):
                s = self.new()
                cur[c] = s
                ps = prev[c] if prev is not None else None          # s[t-1][c]
                pm = (prev[c - 1] if c - 1 >= 1 else "T") if prev is not None else ("T" if c == 1 else None)
                # s <-> ps | (x & pm)
                if ps is not None:
                    self.add(-ps, s)
                if pm == "T":
                    self.add(-x, s)
                elif pm is not None:
                    self.add(-x, -pm, s)
                # s -> ps | x ; s -> ps | pm
                c1 = [-s, x] + ([ps] if ps is not None else [])
                self.add(*c1)
                if pm != "T":
                    c2 = [-s] + ([ps] if ps is not None else []) + ([pm] if pm is not None else [])
                    self.add(*c2)
            prev = cur
        if n >= 1:
            if prev[n] is None:
                self.add()
            else:
                self.add(prev[n])
        if n + 1 <= T and prev[n + 1] is not None:
            self.add(-prev[n + 1])

    def lex_leq(self, X, Y):
        e = None  # None = constant true
        for t in range(len(X)):
            x, y = X[t], Y[t]
            if e is None:
                self.add(-x, y)
            else:
                self.add(-e, -x, y)
            if t == len(X) - 1:
                break
            f = self.new()
            # f <-> e & (x <-> y)
            if e is not None:
                self.add(-f, e)
            self.add(-f, x, -y)
            self.add(-f, -x, y)
            base = [] if e is None else [-e]
            self.add(*(base + [x, y, f]))
            self.add(*(base + [-x, -y, f]))
            e = f


def read_matrix(path, params):
    lines = open(path).read().split("\n")
    head = [int(x) for x in lines[0].split()[1:]]
    assert tuple(head) == tuple(params), "fixed matrix parameters differ"
    V, B = params[0], params[1]
    rows = [[int(t) for t in lines[1 + i].split(" ")] for i in range(V)]
    assert all(len(r) == B for r in rows)
    return rows

TRUE, FALSE = "T", "F"


def add_lemmas(F, a, b, V, B, level):
    """implied constraints of README amendment 1.8 (target parameters, (C1) present)."""
    def ge(r, c):
        if c <= 0:
            return TRUE
        if c >= len(r) or r[c] is None:
            return FALSE
        return r[c]

    def neg(x):
        return FALSE if x == TRUE else (TRUE if x == FALSE else -x)

    def cl(*lits):
        out = []
        for x in lits:
            if x == TRUE:
                return
            if x == FALSE:
                continue
            out.append(x)
        F.add(*out)

    d, o = [], []
    for j in range(B):
        r = F.counter([b[i][j] for i in range(V)], 2)
        d.append(r[2])
        o.append(F.AND(r[1], -r[2]))
    G = {}
    for j, k in itertools.combinations(range(B), 2):
        prods = [F.AND(x, y) for i in range(V) for x in (a[i][j], b[i][j]) for y in (a[i][k], b[i][k])]
        G[(j, k)] = F.counter(prods, 7)

    def g(j, k):
        return G[(min(j, k), max(j, k))]

    for j, k in itertools.combinations(range(B), 2):
        r = g(j, k)
        cl(-d[j], -d[k], ge(r, 4))
        cl(-d[j], -d[k], neg(ge(r, 6)))
    for j in range(B):
        for k in range(B):
            if j != k:
                cl(-d[j], -o[k], ge(g(j, k), 4))
    for j in range(B):
        e3, e4, e6 = [], [], []
        for k in range(B):
            if k == j:
                continue
            r = g(j, k)
            cl(-d[j], ge(r, 3))
            cl(-d[j], neg(ge(r, 7)))
            e3.append(F.AND(r[3], -r[4]))
            e4.append(F.AND(r[4], -r[5]))
            e6.append(F.AND(r[6], -r[7]))
        c3, c4, c6 = F.counter(e3, 2), F.counter(e4, 5), F.counter(e6, 3)
        z = c3[1]
        cl(-d[j], -c3[2])
        cl(-d[j], z, c4[4])
        cl(-d[j], z, -c4[5])
        cl(-d[j], z, c6[2])
        cl(-d[j], z, -c6[3])
        cl(-d[j], -z, c4[1])
        cl(-d[j], -z, -c4[2])
        cl(-d[j], -z, c6[1])
        cl(-d[j], -z, -c6[2])
    for j, k in itertools.combinations(range(B), 2):
        for l in range(B):
            if l in (j, k):
                continue
            for c in range(1, 8):
                cl(-d[j], -d[k], ge(g(j, k), 5), neg(ge(g(j, l), c)), ge(g(k, l), c))
                cl(-d[j], -d[k], ge(g(j, k), 5), neg(ge(g(k, l), c)), ge(g(j, l), c))
    if level >= 3:
        for j, k, l in itertools.combinations(range(B), 3):
            cl(-d[j], -d[k], -d[l], neg(ge(g(j, k), 5)), neg(ge(g(j, l), 5)), neg(ge(g(k, l), 5)))



def main(argv):
    args = argv[1:]
    if len(args) < 8:
        print(__doc__, file=sys.stderr)
        return 2
    params = tuple(int(x) for x in args[:7])
    V, B, p1, p2, R, K, L = params
    out = args[7]
    opts = args[8:]
    sym, strengthen, fix, flip, lemmas, lemma_test = "S1", False, None, None, 0, False
    while opts:
        o = opts.pop(0)
        if o == "--no-symmetry":
            sym = "none"
        elif o == "--s0-only":
            sym = "S0"
        elif o == "--strengthen":
            strengthen = True
        elif o == "--lemmas":
            lemmas = int(opts.pop(0))
            strengthen = True
            if lemmas not in (2, 3):
                print("--lemmas must be 2 or 3", file=sys.stderr)
                return 2
        elif o == "--lemma-test":
            lemma_test = True
            sym = "none"
        elif o == "--fix":
            fix = opts.pop(0)
        elif o == "--fix-flip":
            flip = (int(opts.pop(0)), int(opts.pop(0)), int(opts.pop(0)))
        else:
            print(f"bad option {o}", file=sys.stderr)
            return 2
    if R != p1 + 2 * p2:
        print("R != p1 + 2 p2", file=sys.stderr)
        return 2
    if strengthen and params != (12, 15, 6, 2, 10, 8, 6):
        print("--strengthen is proved only for the target parameters", file=sys.stderr)
        return 2
    F = CNF()
    a = [[F.new() for j in range(B)] for i in range(V)]
    b = [[F.new() for j in range(B)] for i in range(V)]
    for i in range(V):
        for j in range(B):
            F.add(-b[i][j], a[i][j])
    if not lemma_test:  # --lemma-test (controls only): omit (D2)-(D4); keep b -> a, (C1) and the lemma clauses
        for i in range(V):
            F.exactly([a[i][j] for j in range(B)], p1 + p2)
            F.exactly([b[i][j] for j in range(B)], p2)
        for j in range(B):
            F.exactly([lit for i in range(V) for lit in (a[i][j], b[i][j])], K)
        for i in range(V):
            for k in range(i + 1, V):
                prods = []
                for j in range(B):
                    for x in (a[i][j], b[i][j]):
                        for y in (a[k][j], b[k][j]):
                            prods.append(F.AND(x, y))
                F.exactly(prods, L)
    if sym in ("S1", "S0"):
        z = B - p1 - p2
        row0 = [0] * z + [1] * p1 + [2] * p2
        for j in range(B):
            F.add(a[0][j] if row0[j] >= 1 else -a[0][j])
            F.add(b[0][j] if row0[j] == 2 else -b[0][j])
    if sym == "S1":
        for i in range(V - 1):
            F.lex_leq([v for j in range(B) for v in (a[i][j], b[i][j])],
                      [v for j in range(B) for v in (a[i + 1][j], b[i + 1][j])])
        for j in range(B - 1):
            F.lex_leq([v for i in range(V) for v in (a[i][j], b[i][j])],
                      [v for i in range(V) for v in (a[i][j + 1], b[i][j + 1])])
    if strengthen:
        for j in range(B):
            for t in itertools.combinations(range(V), 3):
                F.add(*[-b[i][j] for i in t])
    if lemmas:
        add_lemmas(F, a, b, V, B, lemmas)
    if fix is not None:
        rows = read_matrix(fix, params)
        if flip is not None:
            rows[flip[0]][flip[1]] = flip[2]
        for i in range(V):
            for j in range(B):
                F.add(a[i][j] if rows[i][j] >= 1 else -a[i][j])
                F.add(b[i][j] if rows[i][j] == 2 else -b[i][j])
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    with open(out, "x") as f:
        f.write(f"c btd_cnf_a.py sha256 {me}\nc params {' '.join(map(str, params))} symmetry {sym} "
                f"strengthen {int(strengthen)} fix {fix} flip {flip}" + (f" lemmas {lemmas}" if lemmas else "")
                + (" LEMMA-TEST-ONLY" if lemma_test else "") + "\n")
        f.write(f"p cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
    with open(out + ".map.json", "x") as f:
        json.dump({"generator": "btd_cnf_a.py", "generator_sha256": me, "params": list(params), "symmetry": sym,
                   "strengthen": strengthen, "lemmas": lemmas, "lemma_test": lemma_test, "fix": fix, "flip": flip,
                   "a": a, "b": b, "vars": F.nv,
                   "clauses": len(F.clauses)}, f)
        f.write("\n")
    print(f"{out}: vars {F.nv} clauses {len(F.clauses)} symmetry {sym} strengthen {strengthen} lemmas {lemmas}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
