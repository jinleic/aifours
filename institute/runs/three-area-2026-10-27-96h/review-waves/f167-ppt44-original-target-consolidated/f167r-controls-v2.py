#!/usr/bin/env python3
"""f167r-controls-v2.py -- independent exact controls by reviewer ReviewF167PPT44.

Review wave: f167-ppt44-original-target-consolidated (aifours three-area-2026-10-27-96h).
Author code is NOT imported, read or executed.  Every construction below is re-derived from
the candidate's displayed formulas and from the reviewer's own reconstruction.  Exact
arithmetic uses fractions.Fraction and a small Gaussian-rational class.  The only floating
computation is the supplementary mpmath sample in section B6, labelled NON-EXACT.

Usage: PYTHONDONTWRITEBYTECODE=1 /usr/bin/env python3 f167r-controls-v2.py OUT.json

v2 = v1 plus two boundary-biased generators (star_tight, matching_tight) and a tally of how many
decomposed instances are neither PSD nor coPSD (so both summands are genuinely needed).
"""
import json
import math
import random
import sys
import traceback
from fractions import Fraction as F

SEED = 20261029
OUT = {"script": "f167r-controls-v2.py", "seed": SEED, "sections": {}, "failures": []}


def put(section, name, ok, **info):
    OUT["sections"].setdefault(section, {})[name] = {"pass": bool(ok), **info}
    if not ok:
        OUT["failures"].append(f"{section}/{name}")


# ---------------------------------------------------------------------------
# exact Gaussian rationals
# ---------------------------------------------------------------------------
class C:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    @staticmethod
    def of(x):
        return x if isinstance(x, C) else C(x, 0)

    def __add__(self, o):
        o = C.of(o)
        return C(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = C.of(o)
        return C(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = C.of(o)
        return C(o.re - self.re, o.im - self.im)

    def __neg__(self):
        return C(-self.re, -self.im)

    def __mul__(self, o):
        o = C.of(o)
        return C(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = C.of(o)
        den = o.re * o.re + o.im * o.im
        return C((self.re * o.re + self.im * o.im) / den, (self.im * o.re - self.re * o.im) / den)

    def __rtruediv__(self, o):
        return C.of(o) / self

    def conj(self):
        return C(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __eq__(self, o):
        if not isinstance(o, (C, F, int)):
            return NotImplemented
        o = C.of(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def __repr__(self):
        return f"{self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i"


def cc(x):
    return x.conj() if isinstance(x, C) else x


def ab2(x):
    return x.abs2() if isinstance(x, C) else x * x


def iszero(x):
    return x.is_zero() if isinstance(x, C) else x == 0


# ---------------------------------------------------------------------------
# matrices
# ---------------------------------------------------------------------------
def zeros(n, m=None):
    m = n if m is None else m
    return [[F(0)] * m for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def madd(A, B):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def msub(A, B):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(A, B)]


def msc(s, A):
    return [[s * x for x in r] for r in A]


def meq(A, B):
    return len(A) == len(B) and all(
        len(ra) == len(rb) and all(x == y for x, y in zip(ra, rb)) for ra, rb in zip(A, B))


def proj(v):
    return [[x * cc(y) for y in v] for x in v]


def quad_real(M, x):
    n = len(x)
    tot = F(0)
    for i in range(n):
        if x[i] == 0:
            continue
        for j in range(n):
            if x[j] != 0 and M[i][j] != 0:
                tot += x[i] * M[i][j] * x[j]
    return tot


def herm_form(M, v):
    n = len(v)
    tot = C(0)
    for i in range(n):
        if iszero(v[i]):
            continue
        ci = cc(v[i])
        for j in range(n):
            if iszero(v[j]) or iszero(M[i][j]):
                continue
            tot = tot + ci * M[i][j] * v[j]
    assert tot.im == 0, "Hermitian form not real"
    return tot.re


def ldl_psd_real(M0):
    """Exact symmetric-pivoted LDL^T.  PSD: certificate M == sum_p d_p l_p l_p^T (d_p > 0) is
    re-multiplied and compared exactly.  Not PSD: explicit x with x^T M x < 0 (verified)."""
    n = len(M0)
    M = [[F(x) for x in row] for row in M0]
    for i in range(n):
        for j in range(i + 1, n):
            if M[i][j] != M[j][i]:
                raise ValueError("matrix not symmetric")
    Sm = [row[:] for row in M]
    remaining = list(range(n))
    pivots = []
    y = None
    while remaining:
        p = max(remaining, key=lambda i: Sm[i][i])
        dp = Sm[p][p]
        if dp <= 0:
            neg = [i for i in remaining if Sm[i][i] < 0]
            if neg:
                y = {neg[0]: F(1)}
                break
            off = [(i, j) for i in remaining for j in remaining if i != j and Sm[i][j] != 0]
            if off:
                i, j = off[0]
                y = {i: F(-1) if Sm[i][j] > 0 else F(1), j: F(1)}
            break
        col = {i: Sm[i][p] / dp for i in remaining}
        pivots.append((p, dp, col))
        remaining = [i for i in remaining if i != p]
        for i in remaining:
            ci = col[i]
            if ci == 0:
                continue
            for j in remaining:
                cj = col[j]
                if cj != 0:
                    Sm[i][j] -= ci * dp * cj
    if y is None:
        R = zeros(n)
        for p, dp, col in pivots:
            nz = [(i, v) for i, v in col.items() if v != 0]
            for i, vi in nz:
                for j, vj in nz:
                    R[i][j] += dp * vi * vj
        if not meq(R, M):
            raise AssertionError("LDL certificate reconstruction mismatch")
        return {"psd": True, "rank": len(pivots)}
    x = [F(0)] * n
    for i, v in y.items():
        x[i] = v
    for p, dp, col in reversed(pivots):
        x[p] = -sum((col[i] * x[i] for i in col if i != p), F(0))
    val = quad_real(M, x)
    if not val < 0:
        raise AssertionError("LDL witness not negative")
    return {"psd": False, "witness": x, "value": val}


def psd_herm(M):
    n = len(M)
    for i in range(n):
        for j in range(n):
            if not (C.of(M[i][j]) == C.of(M[j][i]).conj()):
                raise ValueError("not Hermitian")
    if all(C.of(M[i][j]).im == 0 for i in range(n) for j in range(n)):
        return ldl_psd_real([[C.of(M[i][j]).re for j in range(n)] for i in range(n)])
    E = zeros(2 * n)
    for i in range(n):
        for j in range(n):
            z = C.of(M[i][j])
            E[i][j] = z.re
            E[n + i][n + j] = z.re
            E[i][n + j] = -z.im
            E[n + i][j] = z.im
    r = ldl_psd_real(E)
    if r["psd"]:
        assert r["rank"] % 2 == 0
        return {"psd": True, "rank": r["rank"] // 2, "embedded_rank": r["rank"]}
    x = r["witness"]
    v = [C(x[i], x[n + i]) for i in range(n)]
    val = herm_form(M, v)
    assert val < 0
    return {"psd": False, "witness": v, "value": val}


def rank_exact(X):
    A = [[C.of(x) for x in row] for row in X]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if not A[i][c].is_zero()), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c] / A[r][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
        if r == rows:
            break
    return r


# ---------------------------------------------------------------------------
# bipartite C^n (x) C^n, basis |ij> -> index n*i+j ; Gamma = Bob partial transpose
# ---------------------------------------------------------------------------
def idx(i, j, n):
    return n * i + j


def ptB(M, n):
    N = n * n
    out = [[None] * N for _ in range(N)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    out[idx(i, j, n)][idx(k, l, n)] = M[idx(i, l, n)][idx(k, j, n)]
    return out


def vec(X, n):
    return [X[i][j] for i in range(n) for j in range(n)]


def pc_structure_ok(W, n):
    """Nonzero entries only at (|ij>,|ij>) or (|ii>,|kk>): equivalent to U(x)conj(U)
    invariance for all diagonal unitaries U."""
    N = n * n
    for r in range(N):
        for c in range(N):
            if not iszero(W[r][c]):
                i, j = divmod(r, n)
                k, l = divmod(c, n)
                if not (r == c or (i == j and k == l)):
                    return False
    return True


def build_pc(n, Hc, d):
    N = n * n
    W = zeros(N)
    for i in range(n):
        for k in range(n):
            W[idx(i, i, n)][idx(k, k, n)] = Hc[i][k]
    for (i, j), v in d.items():
        W[idx(i, j, n)][idx(i, j, n)] = F(v)
    return W


PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
MATCHINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def P(i, j):
    return (i, j) if i < j else (j, i)


def sqrt_exact(x):
    x = F(x)
    if x < 0:
        return None
    a, b = math.isqrt(x.numerator), math.isqrt(x.denominator)
    if a * a == x.numerator and b * b == x.denominator:
        return F(a, b)
    return None


def sqrt_approx(x, iters):
    x = F(x)
    e = sqrt_exact(x)
    if e is not None:
        return e
    y = F(math.sqrt(float(x))).limit_denominator(10 ** 9)
    if y <= 0:
        y = F(1, 10 ** 9)
    for _ in range(iters):
        y = (y + x / y) / 2
    return y


def W_params(a, k, d):
    Hc = zeros(4)
    for i in range(4):
        Hc[i][i] = F(a[i])
    for (i, j), v in k.items():
        Hc[i][j] = -F(v)
        Hc[j][i] = -F(v)
    return build_pc(4, Hc, d)


def add_B(Bm, i, j, c, q, d, phase=None, check=True):
    """Add (c/q) [[d_ij, -q*ph], [-q*conj(ph), d_ji]] on (|ij>,|ji>)  (candidate eq. (3); ph=1)."""
    c = F(c)
    q = F(q)
    if c == 0:
        return
    if check:
        assert q > 0 and 0 < c <= q, "B block outside 0<c<=q"
    r = c / q
    ph = F(1) if phase is None else phase
    Bm[idx(i, j, 4)][idx(i, j, 4)] = Bm[idx(i, j, 4)][idx(i, j, 4)] + r * d[(i, j)]
    Bm[idx(j, i, 4)][idx(j, i, 4)] = Bm[idx(j, i, 4)][idx(j, i, 4)] + r * d[(j, i)]
    Bm[idx(i, j, 4)][idx(j, i, 4)] = Bm[idx(i, j, 4)][idx(j, i, 4)] - c * ph
    Bm[idx(j, i, 4)][idx(i, j, 4)] = Bm[idx(j, i, 4)][idx(i, j, 4)] - c * cc(ph)


def comps_of(edges):
    parent = list(range(4))

    def f(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for i, j in edges:
        ri, rj = f(i), f(j)
        if ri != rj:
            parent[ri] = rj
    groups = {}
    for v in range(4):
        groups.setdefault(f(v), []).append(v)
    return sorted(groups.values())


def classify_edges(edges):
    comps = comps_of(edges)
    pms = [m for m in MATCHINGS if m[0] in edges and m[1] in edges]
    if len(comps) > 1:
        kind = "disconnected_3comp" if max(len(c) for c in comps) == 3 else "disconnected_le2"
        return {"kind": kind, "edges": edges, "comps": comps, "pms": pms}
    if pms:
        return {"kind": "matching", "edges": edges, "comps": comps, "pms": pms}
    common = set(range(4))
    for e in edges:
        common &= set(e)
    if not (len(edges) == 3 and len(common) == 1):
        return {"kind": "SPLIT_VIOLATION", "edges": edges}
    return {"kind": "star", "center": next(iter(common)), "edges": edges, "comps": comps, "pms": pms}


def classify(q, k):
    return classify_edges([e for e in PAIRS if q[e] < k[e]])


def fM(a, k, q, Mt, z):
    """Candidate eq. (2)."""
    v = sum((F(a[i]) * z[i] * z[i] for i in range(4)), F(0))
    for e in PAIRS:
        v -= 2 * k[e] * z[e[0]] * z[e[1]]
    for (i, j) in Mt:
        v += 2 * F(q[P(i, j)]) * z[i] * z[j]
    return v


def matching_X(Mt, z, d, iters):
    """Coefficient matrix with diagonal z and two disjoint rank-one 2x2 blocks on the pairs of Mt."""
    X = zeros(4)
    for i in range(4):
        X[i][i] = F(z[i])
    for (i, j) in Mt:
        w = z[i] * z[j]
        if w == 0:
            continue
        dij, dji = d[(i, j)], d[(j, i)]
        if dij > 0 and dji > 0:
            u = sqrt_approx(sqrt_approx(dji / dij, iters) * w, iters)
        elif dij == 0 and dji > 0:
            u = F(10) ** (3 * iters) * (1 + w)
        elif dji == 0 and dij > 0:
            u = w / (F(10) ** (3 * iters) * (1 + w))
        else:
            u = F(1)
        X[i][j] = u
        X[j][i] = w / u
    return X


def refute_matching(W, Mt, z, d):
    for iters in range(1, 9):
        X = matching_X(Mt, z, d, iters)
        val = quad_real(W, vec(X, 4))
        if val < 0:
            return {"value": val, "rank": rank_exact(X), "iters": iters}
    return None


# ---------------------------------------------------------------------------
# Claim A: graph split, recipe, and contrapositive refutation
# ---------------------------------------------------------------------------
def claimA_instance(a, k, d, rng, tag):
    q = {}
    for e in PAIRS:
        i, j = e
        qq = sqrt_exact(d[(i, j)] * d[(j, i)])
        assert qq is not None, "q not rational"
        q[e] = qq
    W = W_params(a, k, d)
    assert pc_structure_ok(W, 4)
    rec = {"tag": tag}
    for i in range(4):
        if F(a[i]) < 0:
            v = [F(0)] * 16
            v[idx(i, i, 4)] = F(1)
            assert quad_real(W, v) < 0
            rec.update(kind="pre", outcome="REFUTED_PRODUCT")
            return rec
    for e in PAIRS:
        i, j = e
        r2 = ldl_psd_real([[F(a[i]), -k[e]], [-k[e], F(a[j])]])
        if not r2["psd"]:
            x = r2["witness"]
            v = [F(0)] * 16
            v[idx(i, i, 4)] = x[0]
            v[idx(j, j, 4)] = x[1]
            assert quad_real(W, v) < 0
            rec.update(kind="pre", outcome="REFUTED_2x2")
            return rec
    cls = classify(q, k)
    rec["kind"] = cls["kind"]
    if cls["kind"] == "SPLIT_VIOLATION":
        rec["outcome"] = "SPLIT_VIOLATION"
        return rec
    if cls["kind"] == "disconnected_3comp":
        rec["outcome"] = "IMPORT_CASE_NOT_MACHINE_CHECKED"
        return rec
    routes = []
    if cls["kind"] == "disconnected_le2":
        routes.append("disconnected")
    if cls["pms"]:
        routes.append("matching")
    if cls["kind"] == "star":
        routes.append("star")
    rec["routes"] = {}
    for route in routes:
        try:
            rec["routes"][route] = run_route(route, W, a, k, d, q, cls, rng)
        except AssertionError as ex:
            rec["routes"][route] = {"route": route, "outcome": "ANOMALY_ASSERT", "error": repr(ex),
                                    "tb": traceback.format_exc()}
    rec["outcome"] = "/".join(sorted({r["outcome"] for r in rec["routes"].values()}))
    return rec


def run_route(route, W, a, k, d, q, cls, rng):
    Bm = zeros(16)
    out = {"route": route}
    star = None
    if route == "disconnected":
        comp_id = {}
        for ci, comp in enumerate(cls["comps"]):
            for v in comp:
                comp_id[v] = ci
        for e in PAIRS:
            i, j = e
            if comp_id[i] != comp_id[j]:
                assert q[e] >= k[e]
                if k[e] > 0:
                    add_B(Bm, i, j, k[e], q[e], d)
    elif route == "matching":
        Mt = cls["pms"][0]
        out["M"] = Mt
        for e in Mt:
            assert q[e] < k[e]
            if q[e] > 0:
                add_B(Bm, e[0], e[1], q[e], q[e], d)
    else:
        c0 = cls["center"]
        lv = [v for v in range(4) if v != c0]
        a0 = F(a[c0])
        t = {i: k[P(c0, i)] for i in lv}
        b = {i: t[i] - q[P(c0, i)] for i in lv}
        s = {P(i, j): q[P(i, j)] - k[P(i, j)] for i in lv for j in lv if i < j}
        assert a0 > 0
        for i in lv:
            assert t[i] > 0 and 0 < b[i] <= t[i]
            assert F(a[i]) >= t[i] ** 2 / a0
            if q[P(c0, i)] > 0:
                add_B(Bm, *P(c0, i), q[P(c0, i)], q[P(c0, i)], d)
        for e, se in s.items():
            assert se >= 0
            i, j = e
            cij = min(q[e], k[e] + b[i] * b[j] / a0)
            if cij > 0:
                add_B(Bm, i, j, cij, q[e], d)
        star = [c0, lv, a0, t, b, s]
    Bt = ptB(Bm, 4)
    A = msub(W, Bt)
    assert meq(madd(A, Bt), W)
    assert pc_structure_ok(A, 4)
    for i in range(4):
        for j in range(4):
            if i != j:
                assert A[idx(i, j, 4)][idx(i, j, 4)] >= 0
    Ac = [[A[idx(i, i, 4)][idx(j, j, 4)] for j in range(4)] for i in range(4)]
    rB = ldl_psd_real(Bm)
    assert rB["psd"]
    rA = ldl_psd_real(A)
    out["A_psd"] = rA["psd"]
    if route == "matching":
        for i in range(4):
            for j in range(4):
                if i != j:
                    assert Ac[i][j] <= 0, "matching residual not a Z-matrix"
        for _ in range(3):
            z = [F(rng.randint(0, 9), rng.randint(1, 5)) for _ in range(4)]
            assert quad_real(Ac, z) == fM(a, k, q, out["M"], z)
    if star is not None:
        c0, lv, a0, t, b, s = star
        R = [[Ac[i][j] - Ac[i][c0] * Ac[c0][j] / a0 for j in lv] for i in lv]
        for x_, i in enumerate(lv):
            assert Ac[i][c0] == -b[i]
            assert R[x_][x_] == F(a[i]) - b[i] ** 2 / a0
            for y_, j in enumerate(lv):
                if i < j:
                    e = (i, j)
                    assert Ac[i][j] == min(s[e], b[i] * b[j] / a0)
                    h = max(F(0), b[i] * b[j] / a0 - s[e])
                    assert R[x_][y_] == -h and R[y_][x_] == -h
        bad = [e for e in s if s[e] <= t[e[0]] * t[e[1]] / a0]
        out["bad_pairs"] = bad
        Cm = None
        if not bad:
            assert all(R[x_][y_] == 0 for x_ in range(3) for y_ in range(3) if x_ != y_)
        else:
            j, kk = bad[0]
            i = next(v for v in lv if v not in (j, kk))
            Cd = {
                (i, i): F(a[i]) - b[i] ** 2 / a0,
                (j, j): F(a[j]) - t[j] ** 2 / a0,
                (kk, kk): F(a[kk]) - t[kk] ** 2 / a0,
                P(i, j): -k[P(i, j)] - b[i] * t[j] / a0,
                P(i, kk): -k[P(i, kk)] - b[i] * t[kk] / a0,
                P(j, kk): s[P(j, kk)] - t[j] * t[kk] / a0,
            }
            assert Cd[P(j, kk)] <= 0
            Cm = [[Cd[(u, u)] if u == v else Cd[P(u, v)] for v in lv] for u in lv]
            for x_ in range(3):
                for y_ in range(3):
                    assert R[x_][y_] - Cm[x_][y_] >= 0, "R-C has a negative entry"
            Mt = [P(c0, i), P(j, kk)]
            for _ in range(3):
                zl = {v: F(rng.randint(0, 9), rng.randint(1, 5)) for v in lv}
                z = [None] * 4
                z[c0] = (b[i] * zl[i] + t[j] * zl[j] + t[kk] * zl[kk]) / a0
                for v in lv:
                    z[v] = zl[v]
                assert fM(a, k, q, Mt, z) == quad_real(Cm, [zl[v] for v in lv])
            out["star_branch"] = {"i": i, "jk": [j, kk]}
        star = star + [bad, Cm, R]
    if rA["psd"]:
        out["outcome"] = "DECOMPOSED"
        out["rank_A"], out["rank_B"] = rA["rank"], rB["rank"]
        return out
    if route == "disconnected":
        for comp in cls["comps"]:
            ids = [idx(i, j, 4) for i in comp for j in comp]
            sub = [[W[r][c] for c in ids] for r in ids]
            rs = ldl_psd_real(sub)
            if not rs["psd"]:
                v = [F(0)] * 16
                for pos, r in enumerate(ids):
                    v[r] = rs["witness"][pos]
                X = [[v[idx(i, j, 4)] for j in range(4)] for i in range(4)]
                val = quad_real(W, v)
                rk = rank_exact(X)
                if val < 0 and rk <= 2:
                    out.update(outcome="REFUTED", witness_value=str(val), witness_rank=rk)
                    return out
        out["outcome"] = "NEITHER"
        return out
    if route == "matching":
        rc = ldl_psd_real(Ac)
        assert not rc["psd"]
        z = [abs(x) for x in rc["witness"]]
        zv = quad_real(Ac, z)
        assert zv < 0 and zv == fM(a, k, q, out["M"], z)
        ref = refute_matching(W, out["M"], z, d)
    else:
        c0, lv, a0, t, b, s, bad, Cm, R = star
        rr = ldl_psd_real(R)
        assert not rr["psd"]
        if not bad:
            out["outcome"] = "ANOMALY_NO_BAD_PAIR"
            return out
        zl = [abs(x) for x in rr["witness"]]
        assert quad_real(R, zl) < 0
        assert quad_real(Cm, zl) <= quad_real(R, zl)
        j, kk = bad[0]
        i = next(v for v in lv if v not in (j, kk))
        zd = {v: zl[p] for p, v in enumerate(lv)}
        z = [None] * 4
        z[c0] = (b[i] * zd[i] + t[j] * zd[j] + t[kk] * zd[kk]) / a0
        for v in lv:
            z[v] = zd[v]
        Mt = [P(c0, i), P(j, kk)]
        fz = fM(a, k, q, Mt, z)
        assert fz == quad_real(Cm, zl) and fz < 0
        ref = refute_matching(W, Mt, z, d)
    if ref is not None and ref["rank"] <= 2 and ref["value"] < 0:
        out.update(outcome="REFUTED", witness_value=str(ref["value"]), witness_rank=ref["rank"],
                   newton_iters=ref["iters"])
    else:
        out["outcome"] = "NEITHER"
    return out


def rq(rng, lo, hi, den):
    return F(rng.randint(lo, hi), den)


RHOS = [F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3)]


def make_d(rng, q):
    d = {}
    for (i, j) in PAIRS:
        rho = rng.choice(RHOS)
        d[(i, j)] = q[(i, j)] * rho
        d[(j, i)] = q[(i, j)] / rho
    return d


def gen_general(rng):
    k = {e: rq(rng, 0, 40, 20) for e in PAIRS}
    q = {e: rq(rng, 0, 40, 20) for e in PAIRS}
    a = [rq(rng, 2, 60, 20) for _ in range(4)]
    return a, k, make_d(rng, q)


def gen_star(rng):
    c0 = rng.randrange(4)
    lv = [v for v in range(4) if v != c0]
    k, q = {}, {}
    for i in lv:
        e = P(c0, i)
        k[e] = rq(rng, 1, 40, 20)
        q[e] = k[e] * rq(rng, 0, 19, 20)
    for i in lv:
        for j in lv:
            if i < j:
                k[(i, j)] = rq(rng, 0, 30, 20)
                q[(i, j)] = k[(i, j)] + rq(rng, 0, 20, 20)
    a = [None] * 4
    a[c0] = rq(rng, 10, 60, 20)
    for i in lv:
        a[i] = k[P(c0, i)] ** 2 / a[c0] + rq(rng, -2, 40, 40)
    return a, k, make_d(rng, q)


def gen_matching(rng):
    Mt = rng.choice(MATCHINGS)
    k, q = {}, {}
    for e in PAIRS:
        if e in Mt:
            k[e] = rq(rng, 1, 40, 20)
            q[e] = k[e] * rq(rng, 0, 19, 20)
        else:
            k[e] = rq(rng, 0, 30, 20)
            q[e] = rq(rng, 0, 40, 20)
    a = [rq(rng, 4, 60, 20) for _ in range(4)]
    return a, k, make_d(rng, q)


def gen_disc(rng):
    Mt = rng.choice(MATCHINGS)
    low = set(Mt[:rng.choice([0, 1, 2])])
    k, q = {}, {}
    for e in PAIRS:
        if e in low:
            k[e] = rq(rng, 1, 40, 20)
            q[e] = k[e] * rq(rng, 0, 19, 20)
        else:
            k[e] = rq(rng, 0, 30, 20)
            q[e] = k[e] + rq(rng, 0, 20, 20)
    a = [rq(rng, 2, 60, 20) for _ in range(4)]
    return a, k, make_d(rng, q)


def gen_star_tight(rng):
    """Star instances that always pass the centre-leaf 2x2 tests, with b close to t and small s."""
    c0 = rng.randrange(4)
    lv = [v for v in range(4) if v != c0]
    k, q = {}, {}
    for i in lv:
        e = P(c0, i)
        k[e] = rq(rng, 10, 40, 20)
        q[e] = k[e] * rq(rng, 0, 6, 20)
    for i in lv:
        for j in lv:
            if i < j:
                k[(i, j)] = rq(rng, 0, 20, 20)
                q[(i, j)] = k[(i, j)] + rq(rng, 0, 8, 40)
    a = [None] * 4
    a[c0] = rq(rng, 10, 40, 20)
    for i in lv:
        a[i] = k[P(c0, i)] ** 2 / a[c0] + rq(rng, 0, 12, 40)
    return a, k, make_d(rng, q)


def gen_matching_tight(rng):
    """Perfect-matching instances that always pass every 2x2 test (a_i >= max_j k_ij)."""
    Mt = rng.choice(MATCHINGS)
    k, q = {}, {}
    for e in PAIRS:
        k[e] = rq(rng, 1, 20, 20)
        q[e] = k[e] * rq(rng, 0, 19, 20) if e in Mt else rq(rng, 0, 30, 20)
    a = [max(k[P(i, j)] for j in range(4) if j != i) + rq(rng, 0, 10, 40) for i in range(4)]
    return a, k, make_d(rng, q)


def graph_split_section():
    sec = "graph_split"
    kinds = {}
    for mask in range(64):
        edges = [PAIRS[bit] for bit in range(6) if mask >> bit & 1]
        c = classify_edges(edges)
        kinds[c["kind"]] = kinds.get(c["kind"], 0) + 1
    expected = {"disconnected_3comp": 16, "disconnected_le2": 10, "matching": 34, "star": 4}
    put(sec, "all_64_graphs_disconnected_or_PM_or_spanning_star", kinds == expected, kinds=kinds,
        expected=expected)


def claimA_random_section(rng):
    sec = "A_random"
    plan = [("general", gen_general, 400), ("star", gen_star, 300), ("matching", gen_matching, 200),
            ("disc_le2", gen_disc, 150), ("star_tight", gen_star_tight, 400),
            ("matching_tight", gen_matching_tight, 300)]
    tally = {}
    route_tally = {}
    mixed = {"decomposed_instances": 0, "W_psd": 0, "W_coPSD": 0, "W_neither_psd_nor_coPSD": 0}
    bad = []
    for name, g, cnt in plan:
        for t in range(cnt):
            a, k, d = g(rng)
            rec = claimA_instance(a, k, d, rng, f"{name}-{t}")
            key = f"{name}|{rec.get('kind')}|{rec['outcome']}"
            tally[key] = tally.get(key, 0) + 1
            for rname, r in rec.get("routes", {}).items():
                rk = f"{rname}|{r['outcome']}"
                route_tally[rk] = route_tally.get(rk, 0) + 1
            if any(r["outcome"] == "DECOMPOSED" for r in rec.get("routes", {}).values()):
                W = W_params(a, k, d)
                wp = ldl_psd_real(W)["psd"]
                wg = ldl_psd_real(ptB(W, 4))["psd"]
                mixed["decomposed_instances"] += 1
                mixed["W_psd"] += int(wp)
                mixed["W_coPSD"] += int(wg)
                mixed["W_neither_psd_nor_coPSD"] += int(not wp and not wg)
            if any(x in rec["outcome"] for x in ("NEITHER", "ANOMALY", "SPLIT_VIOLATION")):
                bad.append({"tag": rec["tag"], "a": [str(x) for x in a],
                            "k": {str(e): str(v) for e, v in k.items()},
                            "d": {str(e): str(v) for e, v in d.items()}, "rec": rec})
    put(sec, "dichotomy_decomposed_or_explicit_rank2_refutation", not bad,
        tally=dict(sorted(tally.items())), route_tally=dict(sorted(route_tally.items())),
        decomposed_mixedness=mixed, counterexample_candidates=bad[:5],
        note="each non-import instance is either decomposed by the candidate's recipe (exact PSD "
             "certificates for A and B, exact W == A + B^Gamma) or refuted by an explicit "
             "rank<=2 coefficient matrix X with <X|W|X> < 0; 3-vertex-component instances use the "
             "YLT import and are only counted")


def claimA_negative_section(rng):
    sec = "A_negative"
    a = [F(1)] * 4
    k = {(0, 1): F(1), (0, 2): F(1), (0, 3): F(1), (1, 2): F(0), (1, 3): F(0), (2, 3): F(0)}
    d = {}
    for (i, j) in PAIRS:
        val = F(0) if i == 0 else F(1, 2)
        d[(i, j)] = val
        d[(j, i)] = val
    rec = claimA_instance(a, k, d, rng, "hand-star")
    put(sec, "NEG_hand_star_passes_2x2_screens_but_recipe_fails_and_is_refuted",
        rec.get("kind") == "star" and rec.get("outcome") == "REFUTED", rec=rec)
    W = W_params(a, k, d)
    X = [[F(x) for x in row] for row in [[2, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]]
    val = quad_real(W, vec(X, 4))
    put(sec, "NEG_hand_star_explicit_X_rank2_value_minus1", val == F(-1) and rank_exact(X) == 2,
        value=val, rank=rank_exact(X))
    M = [[F(0), F(1)], [F(1), F(0)]]
    r = ldl_psd_real(M)
    put(sec, "NEG_Z_sign_needed_copositive_nonZ_matrix_not_psd", not r["psd"], value=r.get("value"),
        note="z^T M z = 2 z1 z2 >= 0 on R_+^2, yet x=(1,-1) gives -2")
    Mz = [[F(1), F(-1)], [F(-1), F(1)]]
    put(sec, "copositive_Z_matrix_psd_companion", ldl_psd_real(Mz)["psd"])


def liwu_choi(aa, cs, sigma):
    n = 4
    D = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = F(aa)
    for i in range(n):
        D[sigma[i]][i] += F(cs[i])
    Ch = zeros(16)
    for i in range(n):
        for j in range(n):
            Th = [[F(0)] * n for _ in range(n)]
            if i == j:
                for kk in range(n):
                    Th[kk][kk] += D[i][kk]
            Th[i][j] -= 1
            for r_ in range(n):
                for c_ in range(n):
                    Ch[idx(i, r_, n)][idx(j, c_, n)] += Th[r_][c_]
    return Ch


def example_section(rng):
    sec = "A5_example"
    I16 = eye(16)
    om = [F(0)] * 16
    for i in range(4):
        om[idx(i, i, 4)] = F(1)
    vv = [F(0)] * 16
    vv[idx(0, 0, 4)] = F(1)
    vv[idx(1, 1, 4)] = F(1)
    sum_ii = zeros(16)
    for i in range(4):
        sum_ii[idx(i, i, 4)][idx(i, i, 4)] = F(1)
    Pom = proj(om)
    W0 = msub(madd(msc(F(1, 2), I16), msc(F(3), sum_ii)), Pom)
    T1 = msub(msc(F(2), I16), Pom)
    T2 = msub(msc(F(4), sum_ii), Pom)
    put(sec, "W0_eq_quarter_(2I-[w])_plus_threequarters_(4sum[ii]-[w])",
        meq(W0, madd(msc(F(1, 4), T1), msc(F(3, 4), T2))))
    r = ldl_psd_real(T2)
    put(sec, "4sum[ii]-[w]_psd", r["psd"], rank=r.get("rank"))
    r = ldl_psd_real(T1)
    put(sec, "NEG_2I-[w]_not_psd_(only_2-block-positive)", not r["psd"], value=r.get("value"))
    Tv = msub(msc(F(2), I16), proj(vv))
    r = ldl_psd_real(Tv)
    put(sec, "2I-[v]_psd", r["psd"], rank=r.get("rank"))
    adds = [((1, 1), F(1, 10)), ((2, 2), F(1, 5)), ((3, 3), F(3, 10)), ((1, 2), F(11, 20)),
            ((2, 1), F(11, 20)), ((1, 3), F(3, 2)), ((3, 1), F(3, 2)), ((2, 3), F(5, 2)), ((3, 2), F(5, 2))]
    Wst = [row[:] for row in W0]
    for (i, j), c in adds:
        Wst[idx(i, j, 4)][idx(i, j, 4)] += c
    Wst = madd(Wst, msc(F(1, 100), Tv))
    put(sec, "Wstar_symmetric", meq(Wst, [list(r_) for r_ in zip(*Wst)]))
    put(sec, "Wstar_phase_covariant_structure", pc_structure_ok(Wst, 4))
    us = [C(1), C(F(3, 5), F(4, 5)), C(F(5, 13), F(12, 13)), C(F(8, 17), F(15, 17))]

    def invariant(Dg):
        return all(Dg[r_] * Wst[r_][c_] * Dg[c_].conj() == Wst[r_][c_] for r_ in range(16) for c_ in range(16))

    put(sec, "Wstar_invariant_under_U(x)conjU_rational_phases",
        invariant([us[i] * us[j].conj() for i in range(4) for j in range(4)]))
    put(sec, "NEG_Wstar_not_invariant_under_U(x)U", not invariant([us[i] * us[j] for i in range(4) for j in range(4)]))
    Nneg = madd(Pom, msc(F(1, 100), proj(vv)))
    put(sec, "negative_correlated_matrix_[w]+[v]/100_rank2", rank_exact(Nneg) == 2)
    val_om = quad_real(Wst, om)
    WstG = ptB(Wst, 4)
    v0220 = [F(0)] * 16
    v0220[idx(0, 2, 4)] = F(1)
    v0220[idx(2, 0, 4)] = F(1)
    val_pt = quad_real(WstG, v0220)
    put(sec, "<w|W*|w> = -34/25", val_om == F(-34, 25), value=val_om)
    put(sec, "<02+20|W*^Gamma|02+20> = -24/25", val_pt == F(-24, 25), value=val_pt)
    r1 = ldl_psd_real(Wst)
    r2 = ldl_psd_real(WstG)
    put(sec, "NEG_Wstar_not_psd", not r1["psd"], value=r1.get("value"))
    put(sec, "NEG_Wstar_not_coPSD", not r2["psd"], value=r2.get("value"))
    a = [Wst[idx(i, i, 4)][idx(i, i, 4)] for i in range(4)]
    k = {e: -Wst[idx(e[0], e[0], 4)][idx(e[1], e[1], 4)] for e in PAIRS}
    d = {(i, j): Wst[idx(i, j, 4)][idx(i, j, 4)] for i in range(4) for j in range(4) if i != j}
    q = {e: sqrt_exact(d[e] * d[(e[1], e[0])]) for e in PAIRS}
    cls = classify(q, k)
    put(sec, "low_graph_is_spanning_star_center_0", cls["kind"] == "star" and cls["center"] == 0,
        edges=cls["edges"])
    a0 = a[0]
    t = {i: k[(0, i)] for i in (1, 2, 3)}
    b = {i: t[i] - q[(0, i)] for i in (1, 2, 3)}
    s = {e: q[e] - k[e] for e in [(1, 2), (1, 3), (2, 3)]}
    Bm = zeros(16)
    for i in (1, 2, 3):
        add_B(Bm, 0, i, q[(0, i)], q[(0, i)], d)
    cv = {}
    for e in s:
        i, j = e
        cv[e] = min(q[e], k[e] + b[i] * b[j] / a0)
        add_B(Bm, i, j, cv[e], q[e], d)
    Bt = ptB(Bm, 4)
    A = msub(Wst, Bt)
    rA = ldl_psd_real(A)
    rB = ldl_psd_real(Bm)
    put(sec, "A_psd_rank_8", rA["psd"] and rA["rank"] == 8, rank=rA.get("rank"))
    put(sec, "B_psd_rank_6", rB["psd"] and rB["rank"] == 6, rank=rB.get("rank"))
    put(sec, "Wstar_eq_A_plus_B^Gamma", meq(madd(A, Bt), Wst))
    Ac = [[A[idx(i, i, 4)][idx(j, j, 4)] for j in range(4)] for i in range(4)]
    lv = [1, 2, 3]
    R = [[Ac[i][j] - Ac[i][0] * Ac[0][j] / a0 for j in lv] for i in lv]
    h = {e: max(F(0), b[e[0]] * b[e[1]] / a0 - s[e]) for e in s}
    formula_ok = all(R[x][x] == a[lv[x]] - b[lv[x]] ** 2 / a0 for x in range(3)) and all(
        R[lv.index(e[0])][lv.index(e[1])] == -h[e] for e in s)
    put(sec, "R_matches_eq4", formula_ok)
    put(sec, "deficit_h12_eq_119/5020_and_h13_h23_zero",
        h[(1, 2)] == F(119, 5020) and h[(1, 3)] == 0 and h[(2, 3)] == 0,
        h={str(e): str(v) for e, v in h.items()})
    badp = [e for e in s if s[e] <= t[e[0]] * t[e[1]] / a0]
    put(sec, "branch_pair_jk_is_12_third_leaf_3", badp == [(1, 2)], bad=badp)
    Cd = {(1, 1): a[1] - t[1] ** 2 / a0, (2, 2): a[2] - t[2] ** 2 / a0, (3, 3): a[3] - b[3] ** 2 / a0,
          (1, 3): -k[(1, 3)] - b[3] * t[1] / a0, (2, 3): -k[(2, 3)] - b[3] * t[2] / a0,
          (1, 2): s[(1, 2)] - t[1] * t[2] / a0}
    Cm = [[Cd[(u, u)] if u == v else Cd[P(u, v)] for v in lv] for u in lv]
    put(sec, "R_minus_C_entrywise_nonneg", all(R[x][y] - Cm[x][y] >= 0 for x in range(3) for y in range(3)))
    rR = ldl_psd_real(R)
    rC = ldl_psd_real(Cm)
    put(sec, "R_psd", rR["psd"], rank=rR.get("rank"))
    put(sec, "C_psd", rC["psd"], rank=rC.get("rank"))
    ok = True
    for _ in range(25):
        zl = {v: F(rng.randint(0, 12), rng.randint(1, 6)) for v in lv}
        z = [(b[3] * zl[3] + t[1] * zl[1] + t[2] * zl[2]) / a0, zl[1], zl[2], zl[3]]
        ok = ok and fM(a, k, q, [(0, 3), (1, 2)], z) == quad_real(Cm, [zl[1], zl[2], zl[3]])
    put(sec, "identity_f_M(z0*(z),z)_eq_zCz_25_random_points", ok)
    Bm2 = zeros(16)
    for i in (1, 2, 3):
        add_B(Bm2, 0, i, q[(0, i)], q[(0, i)], d)
    for e in s:
        add_B(Bm2, e[0], e[1], k[e] + b[e[0]] * b[e[1]] / a0, q[e], d, check=False)
    A2 = msub(Wst, ptB(Bm2, 4))
    r = ldl_psd_real(A2)
    put(sec, "NEG_min_clause_removed_gives_negative_|12>_diagonal_and_nonPSD_residual",
        (not r["psd"]) and A2[idx(1, 2, 4)][idx(1, 2, 4)] < 0 and ldl_psd_real(Bm2)["psd"],
        diag12=A2[idx(1, 2, 4)][idx(1, 2, 4)], value=r.get("value"))
    ok_t1 = True
    ok_w = True
    for _ in range(300):
        U = [[C(rq(rng, -4, 4, rng.randint(1, 3)), rq(rng, -4, 4, rng.randint(1, 3))) for _ in range(2)]
             for _ in range(4)]
        V = [[C(rq(rng, -4, 4, rng.randint(1, 3)), rq(rng, -4, 4, rng.randint(1, 3))) for _ in range(2)]
             for _ in range(4)]
        X = [[U[i][0] * V[j][0].conj() + U[i][1] * V[j][1].conj() for j in range(4)] for i in range(4)]
        tr = X[0][0] + X[1][1] + X[2][2] + X[3][3]
        fro = sum((x.abs2() for row in X for x in row), F(0))
        ok_t1 = ok_t1 and 2 * fro - tr.abs2() >= 0
        ok_w = ok_w and herm_form(Wst, vec(X, 4)) >= 0
    put(sec, "sanity_300_random_complex_rank2_X:_2|X|_F^2>=|trX|^2", ok_t1, note="sampling only, not a proof")
    put(sec, "sanity_300_random_complex_rank2_X:_<X|W*|X>>=0", ok_w, note="sampling only, not a proof")
    X3 = [[F(1) if (i == j and i < 3) else F(0) for j in range(4)] for i in range(4)]
    put(sec, "NEG_rank3_X_diag(1,1,1,0)_gives_<X|2I-[w]|X>=-3", quad_real(T1, vec(X3, 4)) == F(-3))
    OUT["sections"][sec]["_parameters"] = {
        "a": [str(x) for x in a], "k": {str(e): str(v) for e, v in k.items()},
        "d": {str(e): str(v) for e, v in d.items()}, "q": {str(e): str(v) for e, v in q.items()},
        "t": {str(i): str(v) for i, v in t.items()}, "b": {str(i): str(v) for i, v in b.items()},
        "s": {str(e): str(v) for e, v in s.items()}, "c_leaf": {str(e): str(v) for e, v in cv.items()},
        "R": [[str(x) for x in row] for row in R], "C": [[str(x) for x in row] for row in Cm]}


def sectionC_section():
    sec = "C_complex_disconnected"
    u1 = C(F(3, 5), F(4, 5))
    u2 = C(F(5, 13), F(12, 13))
    u3 = C(F(8, 17), F(15, 17))
    off = {(0, 1): u1, (2, 3): -u3, (0, 2): u2, (0, 3): C(0, F(1, 2)), (1, 2): C(-1),
           (1, 3): u1.conj() * F(1, 2)}
    mod = {(0, 1): F(1), (2, 3): F(1), (0, 2): F(1), (0, 3): F(1, 2), (1, 2): F(1), (1, 3): F(1, 2)}
    H = [[C(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        H[i][i] = C(1)
    for (i, j), v in off.items():
        assert v.abs2() == mod[(i, j)] ** 2
        H[i][j] = v
        H[j][i] = v.conj()
    d = {(0, 1): F(1, 2), (1, 0): F(1, 2), (2, 3): F(1, 4), (3, 2): F(1), (0, 2): F(2), (2, 0): F(1, 2),
         (0, 3): F(1), (3, 0): F(1), (1, 2): F(1), (2, 1): F(1), (1, 3): F(1, 2), (3, 1): F(2)}
    q = {e: sqrt_exact(d[e] * d[(e[1], e[0])]) for e in PAIRS}
    W = build_pc(4, H, d)
    low = [e for e in PAIRS if q[e] < mod[e]]
    cls = classify_edges(low)
    put(sec, "low_graph_components_{0,1}_{2,3}", cls["kind"] == "disconnected_le2" and cls["comps"] == [[0, 1], [2, 3]],
        low=low)
    rW = psd_herm(W)
    rWG = psd_herm(ptB(W, 4))
    put(sec, "W_not_psd", not rW["psd"], value=rW.get("value"))
    put(sec, "W_not_coPSD", not rWG["psd"], value=rWG.get("value"))
    comp = {0: 0, 1: 0, 2: 1, 3: 1}
    Bm = zeros(16)
    for e in PAIRS:
        i, j = e
        if comp[i] != comp[j]:
            add_B(Bm, i, j, mod[e], q[e], d, phase=-off[e] / mod[e])
    Bt = ptB(Bm, 4)
    A = msub(W, Bt)
    rA = psd_herm(A)
    rB = psd_herm(Bm)
    put(sec, "A_psd", rA["psd"], rank=rA.get("rank"))
    put(sec, "B_psd", rB["psd"], rank=rB.get("rank"))
    put(sec, "W_eq_A_plus_B^Gamma", meq(madd(A, Bt), W))
    put(sec, "cross_component_correlated_entries_cancelled",
        all(iszero(A[idx(i, i, 4)][idx(j, j, 4)]) for (i, j) in PAIRS if comp[i] != comp[j]))
    Bw = zeros(16)
    for e in PAIRS:
        i, j = e
        if comp[i] != comp[j]:
            add_B(Bw, i, j, mod[e], q[e], d, phase=off[e] / mod[e])
    Aw = msub(W, ptB(Bw, 4))
    resid = all(Aw[idx(i, i, 4)][idx(j, j, 4)] == off[(i, j)] * 2 for (i, j) in PAIRS if comp[i] != comp[j])
    rAw = psd_herm(Aw)
    put(sec, "NEG_wrong_phase_sign_leaves_2H_ij_and_nonPSD_residual", resid and not rAw["psd"],
        value=rAw.get("value"))
    Dg = [C(1), u3, C(0, 1), u2]
    HG = [[Dg[i] * H[i][j] * Dg[j].conj() for j in range(4)] for i in range(4)]

    def cyc(Hm):
        return (-Hm[0][1] / mod[(0, 1)]) * (-Hm[1][2] / mod[(1, 2)]) * (-Hm[2][0] / mod[(0, 2)])

    put(sec, "cycle_phase_product_gauge_invariant", cyc(HG) == cyc(H), value=repr(cyc(H)))
    put(sec, "triangle_012_frustrated_(product_ne_1)", not (cyc(H) == C(1)))
    ok = True
    for s0 in (1, -1):
        for s1 in (1, -1):
            for s2 in (1, -1):
                sg = [s0, s1, s2]
                gauged = [sg[0] * sg[1], sg[1] * sg[2], sg[2] * sg[0]]
                if all(x <= 0 for x in gauged):
                    ok = False
    put(sec, "real_triangle_all_+1_no_sign_gauge_makes_all_edges_nonpositive", ok)


def m_of(x):
    Ssum = sum(x, F(0))
    L = max(x)
    return Ssum * Ssum / 2 if 2 * L <= Ssum else L * L + (Ssum - L) ** 2


def fro2(Y):
    return sum((ab2(y) for row in Y for y in row), F(0))


def claimB_section(rng):
    sec = "B"
    ok = True
    mins = None
    for _ in range(3000):
        n = rng.choice([2, 3, 4, 5, 6])
        U = [[F(rng.randint(-6, 6), rng.randint(1, 4)) for _ in range(2)] for _ in range(n)]
        V = [[F(rng.randint(-6, 6), rng.randint(1, 4)) for _ in range(2)] for _ in range(n)]
        Y = [[U[i][0] * V[j][0] + U[i][1] * V[j][1] for j in range(n)] for i in range(n)]
        sl = fro2(Y) - m_of([abs(Y[i][i]) for i in range(n)])
        if sl < 0:
            ok = False
        mins = sl if mins is None or sl < mins else mins
    put(sec, "B1_exact_lower_bound_|Y|_F^2>=m(|diag|)_3000_real_rank2", ok, min_slack=mins)
    ok_id = ok_bd = ok_rk = True
    for _ in range(250):
        n = rng.choice([3, 4, 5])
        sr = [F(rng.randint(1, 5), rng.randint(1, 3)) for _ in range(n)]
        r = [x * x for x in sr]
        qq = F(rng.randint(0, 8), rng.randint(1, 4))
        Hs = zeros(n)
        for i in range(n):
            for j in range(i, n):
                v_ = F(rng.randint(-6, 6), rng.randint(1, 3))
                Hs[i][j] = v_
                Hs[j][i] = v_
        d = {(i, j): qq * r[i] / r[j] for i in range(n) for j in range(n) if i != j}
        W = build_pc(n, Hs, d)
        U = [[F(rng.randint(-6, 6), rng.randint(1, 4)) for _ in range(2)] for _ in range(n)]
        V = [[F(rng.randint(-6, 6), rng.randint(1, 4)) for _ in range(2)] for _ in range(n)]
        Y = [[U[i][0] * V[j][0] + U[i][1] * V[j][1] for j in range(n)] for i in range(n)]
        X = [[Y[i][j] * sr[j] / sr[i] for j in range(n)] for i in range(n)]
        z = [Y[i][i] for i in range(n)]
        val = quad_real(W, vec(X, n))
        zHz = quad_real(Hs, z)
        sz2 = sum((x * x for x in z), F(0))
        ok_id = ok_id and val == zHz + qq * (fro2(Y) - sz2)
        ok_bd = ok_bd and val >= zHz + qq * (m_of([abs(x) for x in z]) - sz2)
        ok_rk = ok_rk and rank_exact(X) <= 2
    put(sec, "B2_exact_T-similarity_identity_250_instances", ok_id)
    put(sec, "B2_exact_weighted_lower_bound_eq7_LHS_250_instances", ok_bd and ok_rk)

    def gram(rows):
        return [[sum((x * y for x, y in zip(ri, rj)), F(0)) for rj in rows] for ri in rows]

    Fr = lambda *xs: [F(x) for x in xs]
    configs = {
        "x=(1,1,1,1)_disjoint_blocks": [[F(1), F(1), F(0), F(0)], [F(1), F(1), F(0), F(0)],
                                        [F(0), F(0), F(1), F(1)], [F(0), F(0), F(1), F(1)]],
        "x=(1,1,1,1)_rotated_polygon": gram([Fr(1, 0), Fr(0, 1), Fr(F(3, 5), F(4, 5)), Fr(F(4, 5), F(-3, 5))]),
        "x=(3,1,1,0)_disjoint_blocks": [[F(3), F(0), F(0), F(0)], [F(0), F(1), F(1), F(0)],
                                        [F(0), F(1), F(1), F(0)], [F(0), F(0), F(0), F(0)]],
        "x=(1,65/32,65/32)_polygon_no_zero_offdiag": gram([Fr(1, 0), Fr(F(7, 8), F(9, 8)), Fr(F(7, 8), F(-9, 8))]),
        "x=(16,4,1,9)_L>=S/2": gram([Fr(4, 0), Fr(0, 2), Fr(0, 1), Fr(0, 3)]),
    }
    phases = [C(1), C(F(3, 5), F(4, 5)), C(F(5, 13), F(-12, 13)), C(F(-8, 17), F(15, 17)), C(0, 1)]
    assert all(p.abs2() == 1 for p in phases)
    att = {}
    all_ok = True
    for name, G in configs.items():
        n = len(G)
        x = [G[i][i] for i in range(n)]
        okg = rank_exact(G) <= 2 and fro2(G) == m_of(x)
        Y = [[phases[i] * G[i][j] for j in range(n)] for i in range(n)]
        z = [Y[i][i] for i in range(n)]
        oky = (rank_exact(Y) <= 2 and fro2(Y) == m_of(x) and all(z[i].abs2() == x[i] * x[i] for i in range(n)))
        sr = [F(i + 1, 2) for i in range(n)]
        r = [s_ * s_ for s_ in sr]
        qq = F(3, 2)
        Hh = [[C(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            Hh[i][i] = C(F(i + 2, 3))
            for j in range(i + 1, n):
                v_ = C(F(i - j, 3), F(i + j + 1, 4))
                Hh[i][j] = v_
                Hh[j][i] = v_.conj()
        d = {(i, j): qq * r[i] / r[j] for i in range(n) for j in range(n) if i != j}
        W = build_pc(n, Hh, d)
        X = [[Y[i][j] * sr[j] / sr[i] for j in range(n)] for i in range(n)]
        val = herm_form(W, vec(X, n))
        target = herm_form(Hh, z) + qq * (m_of(x) - sum((xx * xx for xx in x), F(0)))
        okw = val == target
        branch = "S^2/2" if 2 * max(x) <= sum(x, F(0)) else "L^2+(S-L)^2"
        att[name] = {"x": [str(v) for v in x], "m": str(m_of(x)), "branch": branch, "G_ok": okg,
                     "phased_Y_ok": oky, "weighted_value_equals_eq7_LHS": okw}
        all_ok = all_ok and okg and oky and okw
    put(sec, "B3_exact_attainment_constructions_with_rational_phases", all_ok, configs=att)
    I4 = eye(4)
    I3 = eye(3)
    put(sec, "NEG_rank4_identity_beats_m:_4<8", fro2(I4) == 4 and m_of([F(1)] * 4) == 8 and rank_exact(I4) == 4)
    put(sec, "NEG_rank3_identity_beats_m:_3<9/2", fro2(I3) == 3 and m_of([F(1)] * 3) == F(9, 2))
    rho = {(1, 2): F(2), (2, 3): F(2), (3, 1): F(2)}
    r1 = F(1)
    r2 = r1 / rho[(1, 2)]
    r3 = r2 / rho[(2, 3)]
    put(sec, "B5_equal_geometric_means_without_common_r:_cycle_product_8",
        rho[(1, 2)] * rho[(2, 3)] * rho[(3, 1)] == 8 and r3 / r1 != rho[(3, 1)],
        forced_r3_over_r1=str(r3 / r1), required=str(rho[(3, 1)]))


def mp_section(rng):
    sec = "B6_supplementary_NON_EXACT"
    import mpmath as mp
    mp.mp.dps = 50
    worst = None
    ok = True
    for _ in range(2000):
        n = rng.choice([3, 4, 5, 6])
        U = [[mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2)] for _ in range(n)]
        V = [[mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2)] for _ in range(n)]
        Y = [[U[i][0] * mp.conj(V[j][0]) + U[i][1] * mp.conj(V[j][1]) for j in range(n)] for i in range(n)]
        x = [abs(Y[i][i]) for i in range(n)]
        Ssum = mp.fsum(x)
        L = max(x)
        m = Ssum ** 2 / 2 if 2 * L <= Ssum else L ** 2 + (Ssum - L) ** 2
        fr = mp.fsum(abs(y) ** 2 for row in Y for y in row)
        rel = (fr - m) / fr
        if rel < mp.mpf("-1e-40"):
            ok = False
        worst = rel if worst is None or rel < worst else worst
    put(sec, "complex_rank2_lower_bound_2000_samples_50_digits", ok, min_relative_slack=mp.nstr(worst, 10),
        note="floating, supplementary only")


def priorart_section(rng):
    sec = "priorart"
    v = [F(1), F(-1), F(1), F(-1)]
    Ht = [[F(x) for x in row] for row in [[1, -1, 1, 1], [-1, 1, -1, 1], [1, -1, 1, -1], [1, 1, -1, 1]]]
    E = [[v[i] * v[j] for j in range(4)] for i in range(4)]
    E[0][3] += 2
    E[3][0] += 2
    put(sec, "GNP_Ex5.8_Htilde_eq_vv^T_plus_2(E03+E30)", meq(Ht, E))
    res = {}
    ok = True
    for lam in [F(1, 2), F(3, 4), F(99, 100)]:
        Am = [[F(1) if i == j else lam for j in range(4)] for i in range(4)]
        Bm = [[Ht[i][j] if i == j else Ht[i][j] - lam for j in range(4)] for i in range(4)]
        X1 = zeros(16)
        X2 = zeros(16)
        for i in range(4):
            for j in range(4):
                X1[idx(i, j, 4)][idx(i, j, 4)] += Am[i][j]
                X2[idx(i, j, 4)][idx(i, j, 4)] += Am[i][j]
                if i != j:
                    X1[idx(i, i, 4)][idx(j, j, 4)] += Bm[i][j]
                    X2[idx(i, j, 4)][idx(j, i, 4)] += Bm[i][j]
        w1 = [F(0)] * 16
        w1[idx(0, 0, 4)] = F(1)
        w1[idx(1, 1, 4)] = F(1)
        w2 = [F(0)] * 16
        w2[idx(0, 1, 4)] = F(1)
        w2[idx(1, 0, 4)] = F(1)
        e1 = quad_real(X1, w1)
        e2 = quad_real(X2, w2)
        res[str(lam)] = {"DUC_CLDUI_<00+11|.|00+11>": str(e1), "CDUC_LDUI_<01+10|.|01+10>": str(e2)}
        ok = ok and e1 == -2 * lam and e2 == -2
    put(sec, "GNP_Ex5.8_not_2-positive:_-2lambda_and_-2", ok, values=res)
    sigma = [1, 2, 3, 0]
    cs = [F(1), F(2), F(3), F(1, 2)]
    Ch4 = liwu_choi(4, cs, sigma)
    Ch35 = liwu_choi(F(7, 2), cs, sigma)
    struct = pc_structure_ok(Ch4, 4) and all(
        Ch4[idx(i, i, 4)][idx(j, j, 4)] == (F(3) if i == j else F(-1)) for i in range(4) for j in range(4))
    put(sec, "LiWu_Theta(4,4-cycle)_Choi_is_Z-correlated_single_projector", struct)
    put(sec, "LiWu_Choi_psd_at_a=4_not_psd_at_a=7/2", ldl_psd_real(Ch4)["psd"] and not ldl_psd_real(Ch35)["psd"])
    outs = {}
    for aa, Ch in ((F(4), Ch4), (F(7, 2), Ch35)):
        a = [Ch[idx(i, i, 4)][idx(i, i, 4)] for i in range(4)]
        k = {e: -Ch[idx(e[0], e[0], 4)][idx(e[1], e[1], 4)] for e in PAIRS}
        d = {(i, j): Ch[idx(i, j, 4)][idx(i, j, 4)] for i in range(4) for j in range(4) if i != j}
        outs[str(aa)] = claimA_instance(a, k, d, rng, f"liwu-a={aa}")["outcome"]
    put(sec, "LiWu_family_through_ClaimA_recipe:_a=4_DECOMPOSED_a=7/2_REFUTED",
        outs == {"4": "DECOMPOSED", "7/2": "REFUTED"}, outcomes=outs)


def choi_section(rng):
    """Exact identities behind 'a 2-block-positive 3x3 operator is the Choi matrix of a 2-positive
    map' and 'C_{Phi o T} = C_Phi^{T_A} = ((C_Phi)^T)^{T_B}' (used to transfer YLT's decomposition)."""
    sec = "choi_correspondence"
    n = 3

    def rc():
        return C(F(rng.randint(-5, 5), rng.randint(1, 3)), F(rng.randint(-5, 5), rng.randint(1, 3)))

    def ptA(M):
        N = n * n
        out = [[None] * N for _ in range(N)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        out[idx(i, j, n)][idx(k, l, n)] = M[idx(k, j, n)][idx(i, l, n)]
        return out

    ok_id = ok_tr = ok_pt = True
    for _ in range(30):
        blocks = {(i, j): [[rc() for _ in range(n)] for _ in range(n)] for i in range(n) for j in range(n)}

        def choi(bl):
            Ch = [[C(0)] * (n * n) for _ in range(n * n)]
            for (i, j), Bk in bl.items():
                for r_ in range(n):
                    for c_ in range(n):
                        Ch[idx(i, r_, n)][idx(j, c_, n)] = Bk[r_][c_]
            return Ch

        Ch = choi(blocks)

        def Phi(X):
            out = [[C(0)] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if X[i][j].is_zero():
                        continue
                    for r_ in range(n):
                        for c_ in range(n):
                            out[r_][c_] = out[r_][c_] + X[i][j] * blocks[(i, j)][r_][c_]
            return out

        ws = [[rc() for _ in range(n)] for _ in range(2)]
        ys = [[rc() for _ in range(n)] for _ in range(2)]
        lhs = C(0)
        for s_ in range(2):
            for t_ in range(2):
                Ph = Phi([[ws[s_][i] * ws[t_][j].conj() for j in range(n)] for i in range(n)])
                for r_ in range(n):
                    for c_ in range(n):
                        lhs = lhs + ys[s_][r_].conj() * Ph[r_][c_] * ys[t_][c_]
        v = [C(0)] * (n * n)
        for s_ in range(2):
            for i in range(n):
                for r_ in range(n):
                    v[idx(i, r_, n)] = v[idx(i, r_, n)] + ws[s_][i].conj() * ys[s_][r_]
        rhs = C(0)
        for a_ in range(n * n):
            for b_ in range(n * n):
                rhs = rhs + v[a_].conj() * Ch[a_][b_] * v[b_]
        ok_id = ok_id and lhs == rhs
        ChT = choi({(i, j): blocks[(j, i)] for i in range(n) for j in range(n)})
        ok_tr = ok_tr and meq(ChT, ptA(Ch))
        plainT = [[Ch[c_][r_] for c_ in range(n * n)] for r_ in range(n * n)]
        ok_pt = ok_pt and meq(ptA(Ch), ptB(plainT, n))
    put(sec, "<eta|(id2(x)Phi)(xi xi*)|eta> == <v|C_Phi|v> with v=sum_s conj(w_s)(x)y_s", ok_id, samples=30)
    put(sec, "C_(Phi o T) == C_Phi^(T_A)", ok_tr, samples=30)
    put(sec, "P^(T_A) == (P^T)^(T_B)", ok_pt, samples=30)


def run(name, fn, *args):
    try:
        fn(*args)
    except Exception as ex:
        put(name, "EXCEPTION", False, error=repr(ex), tb=traceback.format_exc())


def main():
    out_path = sys.argv[1]
    rng = random.Random(SEED)
    run("graph_split", graph_split_section)
    run("A5_example", example_section, rng)
    run("A_negative", claimA_negative_section, rng)
    run("A_random", claimA_random_section, rng)
    run("C_complex_disconnected", sectionC_section)
    run("B", claimB_section, rng)
    run("B6_supplementary_NON_EXACT", mp_section, rng)
    run("priorart", priorart_section, rng)
    run("choi_correspondence", choi_section, rng)
    OUT["all_pass"] = not OUT["failures"]
    with open(out_path, "w") as fh:
        json.dump(OUT, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")
    print(json.dumps({"all_pass": OUT["all_pass"], "failures": OUT["failures"]}, indent=1))
    return 0 if OUT["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
