#!/usr/bin/env python3
"""reviewer-q3-product-control-v1.py  (f153 review; reviewer-authored, pure stdlib)

Independent exact control for the claim that, on products C = X1 (x) X2 (x) X3 of complex 4x4
matrices, the ORIGINAL unnormalized q3 of the dossier v3 Section 1,

    q3(C) = ||C||^2 - (1/2) sum_i ||Tr_i C||^2 + (1/4) sum_{i<j} ||Tr_ij C||^2 - (1/8) |Tr C|^2 ,

factors as prod_i g(X_i) with g(X) = ||X||^2 - |Tr X|^2 / 2, and for the stated equality class.

Nothing here imports, reads or executes author code.  All arithmetic is exact over the Gaussian
rationals Q(i), represented as pairs of fractions.Fraction.  Partial traces are evaluated literally
on the explicit 64x64 matrix (index x = 16 x1 + 4 x2 + x3), never through the product structure,
so Check B is an independent concrete test of the whole chain
    (partial trace of a product) -> (HS multiplicativity) -> (8-term bookkeeping).

Checks
  A  formal 8-monomial identity in the six variables n_i = ||X_i||^2, t_i = |Tr X_i|^2, plus two
     intended-reason negative controls (wrong single-trace sign; wrong pair coefficient) that must FAIL.
  B  direct-definition q3 on explicit 64x64 Kronecker products versus prod_i g(X_i); equality
     operators (q3 == 0, rank == 2 exactly, ||C||^2 > 0); non-equality controls that each break
     exactly one hypothesis of the classification (oblique idempotent, unequal singular values,
     eigenvalue-phase mismatch, all factors rank 1); a rank-3 factor outside the domain giving
     q3 < 0; and a deliberately corrupted evaluator that must disagree with the product formula.
  C  rank-pattern enumeration: (r1,r2,r3) in {1..4}^3 with r1 r2 r3 <= 2.
Exit status 0 iff every expectation holds.
"""
from fractions import Fraction as F
import itertools, json, sys

# ----------------------------------------------------------------------------- Gaussian rationals
class GQ:
    __slots__ = ("re", "im")
    def __init__(self, re=0, im=0):
        self.re = F(re); self.im = F(im)
    def __add__(self, o): return GQ(self.re + o.re, self.im + o.im)
    def __sub__(self, o): return GQ(self.re - o.re, self.im - o.im)
    def __mul__(self, o): return GQ(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    def __neg__(self): return GQ(-self.re, -self.im)
    def conj(self): return GQ(self.re, -self.im)
    def abs2(self): return self.re * self.re + self.im * self.im          # exact |z|^2 in Q
    def is_zero(self): return self.re == 0 and self.im == 0
    def inv(self):
        d = self.abs2(); return GQ(self.re / d, -self.im / d)
    def __eq__(self, o): return self.re == o.re and self.im == o.im
    def __repr__(self): return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"

Z = GQ(0, 0); ONE = GQ(1, 0); I = GQ(0, 1)

def mat(rows):                       # rows of Python complex / int / Fraction / GQ -> GQ matrix
    out = []
    for r in rows:
        rr = []
        for v in r:
            if isinstance(v, GQ): rr.append(v)
            elif isinstance(v, complex): rr.append(GQ(F(v.real), F(v.imag)))
            else: rr.append(GQ(F(v), 0))
        out.append(rr)
    return out

def zeros(n, m): return [[Z for _ in range(m)] for _ in range(n)]
def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0]); C = zeros(n, m)
    for i in range(n):
        for j in range(m):
            s = Z
            for l in range(k): s = s + A[i][l] * B[l][j]
            C[i][j] = s
    return C
def madd(A, B): return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]
def dagger(A): return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]
def scal(c, A): return [[c * v for v in r] for r in A]
def outer(u, v):                     # |u><v| : entries u_x conj(v_y)
    return [[u[x] * v[y].conj() for y in range(len(v))] for x in range(len(u))]
def kron(A, B):
    n, m, p, q = len(A), len(A[0]), len(B), len(B[0]); C = zeros(n * p, m * q)
    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(q): C[i * p + k][j * q + l] = A[i][j] * B[k][l]
    return C
def hs2(A):                          # ||A||_HS^2 exactly
    s = F(0)
    for r in A:
        for v in r: s += v.abs2()
    return s
def trace(A):
    s = Z
    for i in range(len(A)): s = s + A[i][i]
    return s
def g(X): return hs2(X) - trace(X).abs2() / 2

def rank(A):                         # exact Gaussian elimination over Q(i)
    M = [r[:] for r in A]; n, m = len(M), len(M[0]); rk = 0; row = 0
    for col in range(m):
        piv = next((r for r in range(row, n) if not M[r][col].is_zero()), None)
        if piv is None: continue
        M[row], M[piv] = M[piv], M[row]
        inv = M[row][col].inv()
        M[row] = [v * inv for v in M[row]]
        for r in range(n):
            if r != row and not M[r][col].is_zero():
                f = M[r][col]; M[r] = [a - f * b for a, b in zip(M[r], M[row])]
        row += 1; rk += 1
        if row == n: break
    return rk

# ------------------------------------------------- literal partial trace on the 64x64 matrix
D = 4; SITES = (0, 1, 2)
def idx(t): return 16 * t[0] + 4 * t[1] + t[2]
def partial_trace(C, S):
    """Unnormalized Tr_S C on the 4^3-dimensional space; returns matrix on the sites not in S
    (a 1x1 matrix when S = all three sites).  Evaluated entry-by-entry from the definition."""
    keep = [s for s in SITES if s not in S]
    out_dim = D ** len(keep); R = zeros(out_dim, out_dim)
    for a in itertools.product(range(D), repeat=len(keep)):
        for b in itertools.product(range(D), repeat=len(keep)):
            s = Z
            for tr in itertools.product(range(D), repeat=len(S)):
                x = [0, 0, 0]; y = [0, 0, 0]
                for site, v in zip(keep, a): x[site] = v
                for site, v in zip(keep, b): y[site] = v
                for site, v in zip(S, tr): x[site] = v; y[site] = v
                s = s + C[idx(x)][idx(y)]
            ra = sum(v * D ** (len(keep) - 1 - k) for k, v in enumerate(a))
            rb = sum(v * D ** (len(keep) - 1 - k) for k, v in enumerate(b))
            R[ra][rb] = s
    return R

def q3_direct(C, coef=(F(1), F(-1, 2), F(1, 4), F(-1, 8))):
    c0, c1, c2, c3 = coef
    val = c0 * hs2(C)
    for i in SITES: val += c1 * hs2(partial_trace(C, (i,)))
    for i, j in itertools.combinations(SITES, 2): val += c2 * hs2(partial_trace(C, (i, j)))
    val += c3 * hs2(partial_trace(C, SITES))        # 1x1 matrix: |Tr C|^2
    return val

# ------------------------------------------------------------------- Check A: formal polynomials
# polynomial = dict{exponent 6-tuple (n1,n2,n3,t1,t2,t3): Fraction}
def pmono(e, c=F(1)): return {tuple(e): F(c)}
def padd(P, Q):
    R = dict(P)
    for k, v in Q.items():
        R[k] = R.get(k, F(0)) + v
        if R[k] == 0: del R[k]
    return R
def pscale(c, P): return {k: F(c) * v for k, v in P.items()} if c != 0 else {}
def pmul(P, Q):
    R = {}
    for k1, v1 in P.items():
        for k2, v2 in Q.items():
            k = tuple(a + b for a, b in zip(k1, k2)); R[k] = R.get(k, F(0)) + v1 * v2
    return {k: v for k, v in R.items() if v != 0}
def var(name):
    e = [0] * 6; e[{"n1": 0, "n2": 1, "n3": 2, "t1": 3, "t2": 4, "t3": 5}[name]] = 1; return pmono(e)
n = [var("n1"), var("n2"), var("n3")]; t = [var("t1"), var("t2"), var("t3")]
def term_for_subset(S):              # ||Tr_S (X1 x X2 x X3)||^2 -> prod_{i in S} t_i prod_{i not in S} n_i
    P = pmono([0] * 6)
    for i in SITES: P = pmul(P, t[i] if i in S else n[i])
    return P
def q3_formal(coef=(F(1), F(-1, 2), F(1, 4), F(-1, 8))):
    c0, c1, c2, c3 = coef; P = pscale(c0, term_for_subset(()))
    for i in SITES: P = padd(P, pscale(c1, term_for_subset((i,))))
    for i, j in itertools.combinations(SITES, 2): P = padd(P, pscale(c2, term_for_subset((i, j))))
    return padd(P, pscale(c3, term_for_subset(SITES)))
def product_formal():
    P = pmono([0] * 6)
    for i in SITES: P = pmul(P, padd(n[i], pscale(F(-1, 2), t[i])))
    return P

results = {"checks": [], "all_ok": True}
def record(name, ok, **info):
    results["checks"].append({"name": name, "ok": bool(ok), **{k: str(v) for k, v in info.items()}})
    if not ok: results["all_ok"] = False
    print(("PASS " if ok else "FAIL ") + name + ("  " + json.dumps({k: str(v) for k, v in info.items()}) if info else ""))

prod = product_formal(); q3f = q3_formal()
record("A1 formal: q3_formal == prod_i (n_i - t_i/2), 8 monomials", q3f == prod and len(prod) == 8,
       monomials=len(prod), coefficients=sorted(str(v) for v in prod.values()))
bad_sign = q3_formal((F(1), F(1, 2), F(1, 4), F(-1, 8)))      # wrong single-trace sign
record("A2 negative control (wrong single-trace sign) must differ", bad_sign != prod,
       differing_monomials=len({k for k in set(bad_sign) | set(prod) if bad_sign.get(k) != prod.get(k)}))
bad_pair = q3_formal((F(1), F(-1, 2), F(1, 2), F(-1, 8)))     # wrong pair coefficient
record("A3 negative control (pair coefficient 1/2 instead of 1/4) must differ", bad_pair != prod,
       differing_monomials=len({k for k in set(bad_pair) | set(prod) if bad_pair.get(k) != prod.get(k)}))

# --------------------------------------------------------------------- Check B: explicit operators
e = [[ONE if k == j else Z for k in range(4)] for j in range(4)]
E = lambda a, b: outer(e[a], e[b])                   # matrix unit |a><b|
P12 = mat([[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,0]])  # orthogonal rank-2 projection
# rational unitary mixing coordinates 1 and 2 (one inside ran P12, one outside): U = (1/5)[[3,4i],[4i,3]]
U = mat([[1,0,0,0],[0,F(3,5),GQ(0,F(4,5)),0],[0,GQ(0,F(4,5)),F(3,5),0],[0,0,0,1]])
assert matmul(U, dagger(U)) == mat([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
Pu = matmul(matmul(U, P12), dagger(U))               # non-diagonal orthogonal rank-2 projection
assert matmul(Pu, Pu) == Pu and dagger(Pu) == Pu and rank(Pu) == 2
lam = GQ(1, 2)                                       # nonzero complex scalar 1+2i
X_proj = scal(lam, Pu)
X_r1a = E(0, 1)                                      # |e0><e1|, non-normal rank 1
u = [GQ(1), GQ(2), GQ(0, 1), GQ(0)]; v = [GQ(1), GQ(-1), GQ(0), GQ(0, 3)]
X_r1b = outer(u, v)                                  # generic rank 1 with complex entries
X_r1c = scal(GQ(F(2,3), F(-1,7)), E(2, 2))           # scaled rank-1 projection
X_obl = madd(madd(E(0, 0), E(0, 1)), E(2, 2))        # oblique idempotent E00+E01+E22 (rank 2, not Hermitian)
assert matmul(X_obl, X_obl) == X_obl and rank(X_obl) == 2 and dagger(X_obl) != X_obl
X_uneq = mat([[1,0,0,0],[0,F(1,2),0,0],[0,0,0,0],[0,0,0,0]])  # rank 2, unequal singular values
X_phase = mat([[1,0,0,0],[0,1j,0,0],[0,0,0,0],[0,0,0,0]])     # rank 2, equal moduli, phases differ
X_rank3 = mat([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,0]])      # rank 3: outside the domain
# generic rank-2 non-normal complex factor  |u1><v1| + |u2><v2|
u1 = [GQ(1, 1), GQ(0), GQ(2), GQ(0, -1)]; v1 = [GQ(0, 1), GQ(1), GQ(0), GQ(3)]
u2 = [GQ(0), GQ(1, -2), GQ(1), GQ(0)];    v2 = [GQ(1), GQ(0), GQ(0, 2), GQ(-1)]
X_gen2 = madd(outer(u1, v1), outer(u2, v2))
assert rank(X_gen2) == 2
X_gen4 = mat([[1,1j,2,0],[0,3,1,-1j],[2j,0,1,1],[1,0,0,5]])   # generic rank-4 complex factor (outside domain)
assert rank(X_gen4) == 4

def run_case(name, Xs, expect_zero=None, expect_rank=None, expect_sign=None, corrupt=False):
    C = kron(kron(Xs[0], Xs[1]), Xs[2])
    direct = q3_direct(C) if not corrupt else q3_direct(C, (F(1), F(-1, 2), F(1, 2), F(-1, 8)))
    prodv = g(Xs[0]) * g(Xs[1]) * g(Xs[2]); norm2 = hs2(C); rk = rank(C)
    ok = True; info = dict(q3_direct=direct, prod_g=prodv, norm2=norm2, rank=rk, gs=[g(X) for X in Xs])
    if corrupt: ok &= (direct != prodv)
    else: ok &= (direct == prodv)
    if expect_zero is True: ok &= (direct == 0 and norm2 > 0)
    if expect_zero is False: ok &= (direct != 0)
    if expect_rank is not None: ok &= (rk == expect_rank)
    if expect_sign == "+": ok &= (direct > 0)
    if expect_sign == "-": ok &= (direct < 0)
    record(name, ok, **info)
    return direct, norm2

# equality operators (positive cases): exactly one factor = scalar * rank-2 orthogonal projection
run_case("B1 equality: diag P12 (x) E00 (x) E00", [P12, E(0,0), E(0,0)], expect_zero=True, expect_rank=2)
run_case("B2 equality: (1+2i) U P12 U^dag (x) |e0><e1| (x) generic rank-1", [X_proj, X_r1a, X_r1b], expect_zero=True, expect_rank=2)
run_case("B3 equality: projection factor on site 3", [X_r1b, X_r1c, X_proj], expect_zero=True, expect_rank=2)
run_case("B4 equality: projection factor on site 2", [X_r1a, X_proj, X_r1c], expect_zero=True, expect_rank=2)
# intended-reason non-equality controls, each breaking exactly one hypothesis
run_case("B5 non-equality: oblique (non-orthogonal) rank-2 idempotent factor", [X_obl, X_r1a, X_r1b], expect_zero=False, expect_rank=2, expect_sign="+")
run_case("B6 non-equality: rank-2 factor with unequal singular values", [X_uneq, E(0,0), X_r1b], expect_zero=False, expect_rank=2, expect_sign="+")
run_case("B7 non-equality: rank-2 normal factor diag(1,i) with phase mismatch", [X_phase, X_r1a, E(0,0)], expect_zero=False, expect_rank=2, expect_sign="+")
run_case("B8 non-equality: all three factors rank 1 (strictly positive)", [X_r1a, X_r1b, X_r1c], expect_zero=False, expect_rank=1, expect_sign="+")
run_case("B9 outside domain: rank-3 factor gives q3 < 0 (rank hypothesis load-bearing)", [X_rank3, E(0,0), E(0,0)], expect_rank=3, expect_sign="-")
run_case("B10 generic rank-2 non-normal complex factor (x) rank-1 (x) rank-1: factorization exact, q3 > 0", [X_gen2, X_r1a, X_r1b], expect_zero=False, expect_rank=2, expect_sign="+")
run_case("B11 outside domain: generic rank-4 factor, factorization identity still exact", [X_gen4, X_gen2, X_r1b], expect_rank=8)
run_case("B12 negative control: corrupted evaluator (pair coef 1/2) must disagree", [X_obl, X_proj, X_r1b], corrupt=True)
# explicit normalized ratio for the B1 operator
Cb1 = kron(kron(P12, E(0,0)), E(0,0)); r = q3_direct(Cb1) / hs2(Cb1)
record("B13 normalized ratio q3/||C||^2 of B1 operator equals 0 exactly", r == 0, ratio=r, norm2=hs2(Cb1))
# the all-rank-1 bound q3 >= ||C||^2/8 on B8
Cb8 = kron(kron(X_r1a, X_r1b), X_r1c)
record("B14 all-rank-1 product satisfies q3 >= ||C||^2 / 8", q3_direct(Cb8) >= hs2(Cb8) / 8, q3=q3_direct(Cb8), norm2_over_8=hs2(Cb8) / 8)

# ------------------------------------------------------------------- Check C: rank patterns
pats = sorted(p for p in itertools.product(range(1, 5), repeat=3) if p[0] * p[1] * p[2] <= 2)
record("C1 rank patterns with r1 r2 r3 <= 2 are exactly (1,1,1),(1,1,2),(1,2,1),(2,1,1)",
       pats == [(1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)], patterns=pats)

print(json.dumps({"all_ok": results["all_ok"], "n_checks": len(results["checks"]),
                  "n_pass": sum(c["ok"] for c in results["checks"])}))
sys.exit(0 if results["all_ok"] else 1)
