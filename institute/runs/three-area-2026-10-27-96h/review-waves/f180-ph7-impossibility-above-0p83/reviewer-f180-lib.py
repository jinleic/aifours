"""Reviewer-authored exact library for the f180 review (z3 = 83/100).

Independent of the author's generator/replay: sparse dict polynomials with
Fraction/int coefficients, elementary symmetric functions by the product
recurrence, all definitions written from the theorem packet text, per-leaf
DIRECT Bernstein coefficients (no subdivision of parent tensors), and
prefix/Kraft coverage proofs.  Standard library + numpy object arrays only;
no floating point anywhere.
"""
import hashlib, itertools, json, math
from fractions import Fraction as Fr

# ---------------- sparse polynomials ----------------
def clean(p):
    return {k: v for k, v in p.items() if v != 0}

def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, 0) + v
    return clean(o)

def pscale(p, c):
    return clean({k: v * c for k, v in p.items()}) if c != 0 else {}

def psub(a, b):
    return padd(a, pscale(b, -1))

def pmul(a, b):
    o = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(x + y for x, y in zip(k1, k2))
            o[k] = o.get(k, 0) + v1 * v2
    return clean(o)

def pmuls(*ps):
    out = ps[0]
    for p in ps[1:]:
        out = pmul(out, p)
    return out

def var(i, n):
    e = [0] * n; e[i] = 1
    return {tuple(e): 1}

def const(c, n):
    return {tuple([0] * n): c} if c != 0 else {}

def esyms(vs, n, kmax):
    """[e_0..e_kmax] of the polynomials vs via prod (1 + t v)."""
    E = [const(1, n)] + [{} for _ in range(kmax)]
    for v in vs:
        for k in range(kmax, 0, -1):
            E[k] = padd(E[k], pmul(v, E[k - 1]))
    return E

def coef_in(P, i, d):
    """coefficient of var_i^d, var_i kept in the tuple with exponent 0"""
    return clean({k[:i] + (0,) + k[i + 1:]: v for k, v in P.items() if k[i] == d})

def deg_in(P, i):
    return max((k[i] for k in P), default=0)

def drop_var(P, i):
    assert all(k[i] == 0 for k in P)
    return clean({k[:i] + k[i + 1:]: v for k, v in P.items()})

def is_zero(P):
    return not clean(P)

def subst_const(P, i, val):
    """substitute var_i := val (a constant)"""
    o = {}
    for k, v in P.items():
        kk = k[:i] + (0,) + k[i + 1:]
        o[kk] = o.get(kk, 0) + v * (val ** k[i])
    return clean(o)

def integerize(P):
    L = 1
    for v in P.values():
        L = math.lcm(L, Fr(v).denominator)
    Q = {k: Fr(v) * L for k, v in P.items()}
    assert all(v.denominator == 1 for v in Q.values())
    return {k: int(v) for k, v in Q.items()}, L

def digest(P):
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()

# ---------------- coverage (prefix-free + Kraft) ----------------
def coverage_proof(paths):
    """Return (ok, info).  ok iff every path is a 0/1 string, the set has no
    duplicates, is prefix-free, and sum 2^-len == 1 exactly (then the leaf
    cylinders partition Cantor space, so the leaf boxes cover the cube)."""
    if any(set(p) - {'0', '1'} for p in paths):
        return False, 'non-binary path'
    if len(set(paths)) != len(paths):
        return False, 'duplicate path'
    sp = sorted(paths)
    for a, b in zip(sp, sp[1:]):
        if b.startswith(a):
            return False, 'prefix violation %r < %r' % (a, b)
    m = max(len(p) for p in paths)
    tot = sum(1 << (m - len(p)) for p in paths)
    if tot != (1 << m):
        return False, 'Kraft sum %s' % Fr(tot, 1 << m)
    return True, 'prefix-free, Kraft sum exactly 1, %d leaves, max depth %d' % (len(paths), m)

def path_intervals(path, naxes):
    """per axis (n, l): interval [n/2^l, (n+1)/2^l] in [0,1]; char t splits axis t mod naxes,
    '0' lower half, '1' upper half."""
    n = [0] * naxes; l = [0] * naxes
    for t, ch in enumerate(path):
        a = t % naxes
        n[a] = 2 * n[a] + (1 if ch == '1' else 0); l[a] += 1
    return tuple(zip(n, l))

# ---------------- per-axis integer matrices ----------------
def lcm_binoms(d):
    L = 1
    for j in range(d + 1):
        L = math.lcm(L, math.comb(d, j))
    return L

def conv_matrix(d):
    """monomial (t^j) -> Bernstein (index m) on [0,1], scaled by lcm C(d,j) (integer, >=0)"""
    L = lcm_binoms(d)
    return [[(L * math.comb(m, j)) // math.comb(d, j) if j <= m else 0 for j in range(d + 1)] for m in range(d + 1)]

def shift_matrix(d, n, l):
    """s = (n + t)/2^l ; maps monomial coeffs in s (index k) to monomial coeffs in t
    (index j), multiplied by 2^(l d) (positive)."""
    return [[math.comb(k, j) * n ** (k - j) * (1 << (l * (d - k))) if j <= k else 0 for k in range(d + 1)]
            for j in range(d + 1)]

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def leaf_matrix(d, n, l):
    """integer matrix taking monomial coefficients in s (on [0,1]) to positive multiples of the
    Bernstein coefficients on the dyadic sub-interval [n/2^l,(n+1)/2^l]"""
    return matmul(conv_matrix(d), shift_matrix(d, n, l))

def compact_axis_matrix(n, l):
    """Degree-2 compactified axis: column k is x^k (1-x)^(2-k), row m the Bernstein coefficient
    (blossom at (a,a),(a,b),(b,b)) on [a,b]=[n/2^l,(n+1)/2^l], all times 2*N^2 with N=2^l."""
    N = 1 << l
    pts = [(n, n), (n, n + 1), (n + 1, n + 1)]
    M = []
    for (t1, t2) in pts:
        M.append([2 * (N - t1) * (N - t2), t1 * (N - t2) + t2 * (N - t1), 2 * t1 * t2])
    return M
