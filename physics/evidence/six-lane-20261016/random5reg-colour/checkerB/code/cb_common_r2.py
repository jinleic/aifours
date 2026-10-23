"""Shared exact objects for checker B, r2 HARDENED COPY of cb_common.py (pinned, sha256
9d3ad5abb52c3ac9ad1bc1027ae9618040d01b3f7e6266f48651ca91ba183726).  Only change: every assert
(and the unguarded next() in inv) is replaced by an explicit require(...) check that raises
CheckFailed (not removed by python -O); the caller turns it into verdict FAIL + nonzero exit.
Check ids "cb_common.py:<line>" name the pinned line that held the replaced assert.

Original provenance: written from README section 1 + the format
spec + sources/diaz2009-3col-preprint.layout.txt only; nothing under code/ or
outer/code/ was read or imported.

Conventions (README frozen scheme / format spec):
  * entries of a 2x2 matrix are indexed by k = 0..3 <-> (r,t) = (-1,-1), (-1,1), (1,-1), (1,1)
    (paper: rows/columns indexed by -1, 1, with -1 first);
  * class u = 3i + j for (i,j) in Z3 x Z3;
  * n = (n00, n01, n10, n11); the nine n^u by (7.2): n^{02} = 1/3 - n00 - n01,
    n^{12} = 1/3 - n10 - n11, n^{20} = 1/3 - n00 - n10, n^{21} = 1/3 - n01 - n11,
    n^{22} = n00 + n01 + n10 + n11 - 1/3;
  * pairing (7.5): m^{ij}_{r,t} = m^{i+r,j+t}_{-r,-t}; EDGES in the loop order of the spec;
    C_u[k][e] = +1 if (u,k) is the first end of edge e, -1 if it is the second end.
"""
from fractions import Fraction as Fr
import itertools
import math


class CheckFailed(Exception):
    """A certificate-critical explicit check failed."""


CHECK_COUNTS = {}   # check id -> number of times the check was executed and held


def require(cond, cid, reason):
    """Explicit replacement for assert: raise CheckFailed unless cond; count successes."""
    if not cond:
        raise CheckFailed(f"{cid}: {reason}")
    CHECK_COUNTS[cid] = CHECK_COUNTS.get(cid, 0) + 1


KRT = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
KIDX = {rt: k for k, rt in enumerate(KRT)}

# Spectra (paper section 4 / (7.x)): 2x2 nonnegative integer matrices, entry sum 5,
# both row sums >= 1 and both column sums >= 1.  Row -1 = (k0,k1), row 1 = (k2,k3),
# column -1 = (k0,k2), column 1 = (k1,k3).
SPECTRA = [s for s in itertools.product(range(6), repeat=4)
           if sum(s) == 5 and s[0] + s[1] >= 1 and s[2] + s[3] >= 1
           and s[0] + s[2] >= 1 and s[1] + s[3] >= 1]
WEIGHT = [math.factorial(5) // math.prod(math.factorial(x) for x in s) for s in SPECTRA]


def phi_closed_form(x, y, z, w):
    """(7.7): Phi = (x+y+z+w)^5-(x+y)^5-(x+z)^5-(y+w)^5-(z+w)^5+x^5+y^5+z^5+w^5."""
    return ((x + y + z + w) ** 5 - (x + y) ** 5 - (x + z) ** 5 - (y + w) ** 5 - (z + w) ** 5
            + x ** 5 + y ** 5 + z ** 5 + w ** 5)


def phi_sum(mu):
    return sum(wt * mu[0] ** s[0] * mu[1] ** s[1] * mu[2] ** s[2] * mu[3] ** s[3]
               for s, wt in zip(SPECTRA, WEIGHT))


def check_spectra():
    """|S| = 36 and sum_s w_s mu^s == (7.7) as polynomials.  Both sides have degree <= 5
    in each variable, so equality on the grid {0..5}^4 implies identity."""
    require(len(SPECTRA) == 36, "cb_common.py:45", f"|S| = {len(SPECTRA)}, expected 36")
    for p in itertools.product(range(6), repeat=4):
        require(phi_sum(p) == phi_closed_form(*p), "cb_common.py:47",
                f"sum_s w_s mu^s differs from (7.7) at mu = {p}")
    return True


def build_edges():
    edges, seen = [], set()
    for u in range(9):
        i, j = divmod(u, 3)
        for k, (r, t) in enumerate(KRT):
            if (u, k) in seen:
                continue
            v = 3 * ((i + r) % 3) + (j + t) % 3
            kv = KIDX[(-r, -t)]
            edges.append((u, k, v, kv))
            seen.add((u, k))
            seen.add((v, kv))
    require(len(edges) == 18 and len(seen) == 36, "cb_common.py:63",
            f"pairing edges: {len(edges)} edges / {len(seen)} ends, expected 18 / 36")
    return edges


EDGES = build_edges()

# C[u][k][e]
CMAT = [[[0] * 18 for _ in range(4)] for _ in range(9)]
for _e, (_u, _k, _v, _kv) in enumerate(EDGES):
    CMAT[_u][_k][_e] += 1
    CMAT[_v][_kv][_e] -= 1

# n^u = 1/9 + A[u] . eta, eta = (n00, n01, n10, n11) - 1/9   (from (7.2))
AROWS = [[1, 0, 0, 0], [0, 1, 0, 0], [-1, -1, 0, 0],
         [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, -1, -1],
         [-1, 0, -1, 0], [0, -1, 0, -1], [1, 1, 1, 1]]


def nine_values(n):
    """(7.2) on a 4-tuple of Fractions."""
    n1, n2, n3, n4 = n
    third = Fr(1, 3)
    return [n1, n2, third - n1 - n2,
            n3, n4, third - n3 - n4,
            third - n1 - n3, third - n2 - n4, n1 + n2 + n3 + n4 - third]


def check_arows():
    """A[u] reproduces (7.2) and every n^u equals 1/9 at n*."""
    nstar = (Fr(1, 9),) * 4
    for eta in itertools.product([Fr(0), Fr(1, 7), Fr(-2, 11)], repeat=4):
        n = tuple(Fr(1, 9) + e for e in eta)
        nv = nine_values(n)
        for u in range(9):
            require(nv[u] == Fr(1, 9) + sum(a * e for a, e in zip(AROWS[u], eta)), "cb_common.py:97",
                    f"AROWS[{u}] does not reproduce (7.2) at eta = {eta}")
    require(nine_values(nstar) == [Fr(1, 9)] * 9, "cb_common.py:98", "n^u(n*) != 1/9 for some u")
    return True


# ---- small exact linear algebra over Fractions -------------------------------------------
def T(M):
    return [list(r) for r in zip(*M)]


def mm(A, B):
    Bt = T(B)
    return [[sum(a * b for a, b in zip(r, c)) for c in Bt] for r in A]


def madd(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def msc(c, A):
    return [[c * a for a in r] for r in A]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def outer(a, b):
    return [[x * y for y in b] for x in a]


def inv(M):
    n = len(M)
    aug = [[Fr(x) for x in r] + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for col in range(n):
        piv = next((r for r in range(col, n) if aug[r][col] != 0), None)
        require(piv is not None, "cb_common.py:132(next)", f"singular matrix in exact inverse (column {col})")
        aug[col], aug[piv] = aug[piv], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col] != 0:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [r[n:] for r in aug]


def det(M):
    """Exact determinant by fraction Gaussian elimination."""
    a = [[Fr(x) for x in r] for r in M]
    n, d = len(a), Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if a[r][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            a[col], a[piv] = a[piv], a[col]
            d = -d
        d *= a[col][col]
        for r in range(col + 1, n):
            f = a[r][col] / a[col][col]
            if f:
                a[r] = [x - f * y for x, y in zip(a[r], a[col])]
    return d


def leading_minors(M):
    return [det([row[:k] for row in M[:k]]) for k in range(1, len(M) + 1)]


def is_pos_def_exact(M):
    """Sylvester's criterion on a symmetric rational matrix."""
    require(all(M[i][j] == M[j][i] for i in range(len(M)) for j in range(len(M))), "cb_common.py:168",
            "Sylvester test called on a non-symmetric matrix")
    return all(x > 0 for x in leading_minors(M))
