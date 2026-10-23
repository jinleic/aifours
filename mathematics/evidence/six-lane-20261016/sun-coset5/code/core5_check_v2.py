#!/usr/bin/env python3
"""core5_check_v2 -- second, independently written checker for the Core(5) case analysis.

Differences from core5_engine_v1 (on purpose):
  * enumerates ALL labelled patterns (alpha in {1,2,3}^10, E2, E3 in {none,0..4}); no symmetry reduction;
  * Core(5)-specific symbolic formulas (special status only); no representative integers;
  * adds rule RSD (proof-v1.md, Lemma R as used for S-D, in general form):
      vertex v, vertex w with alpha_vw = 1, alpha_vj = 3 for the other three j, and the containments
      U_vU_w <= U_vU_j forced by (T3), i.e. tau_min(v,w,j) >= alpha_vw*alpha_wj for each j.
Rule order: T, K, P, N2, FH2, RSD; a pattern survives only if no rule fires.
Usage: python3 core5_check_v2.py OUTDIR       (writes summary.json, exclusive create)
"""
import hashlib
import itertools
import json
import os
import sys
import time
from fractions import Fraction as Fr
from math import gcd

V = range(5)
E = list(itertools.combinations(V, 2))
BIG = 10


def lcm(a, b):
    return a * b // gcd(a, b)


class Pat:
    def __init__(self, al, e2, e3):
        self.A = [[0] * 5 for _ in V]
        for (i, j), x in zip(E, al):
            self.A[i][j] = self.A[j][i] = x
        self.e2, self.e3 = e2, e3
        self.tm = {}
        for tri in itertools.combinations(V, 3):
            self.tm[tri] = self._taumin(tri)

    def div(self, alpha, z):  # alpha | r_z ?
        return alpha == 1 or (alpha == 2 and z == self.e2) or (alpha == 3 and z == self.e3)

    def _taumin(self, tri):
        t = 1
        for x, y in itertools.combinations(tri, 2):
            z = [w for w in tri if w not in (x, y)][0]
            a = self.A[x][y]
            if not self.div(a, z):
                t = lcm(t, a)
        return t

    def taumin(self, a, b, c):
        return self.tm[tuple(sorted((a, b, c)))]


def r_T(p):
    for tri in itertools.combinations(V, 3):
        x, y, z = tri
        a, b, c = p.A[x][y], p.A[x][z], p.A[y][z]
        if p.tm[tri] > min(a * b, a * c, b * c):
            return ("T", tri)
    return None


def linked(p, v, i, j):
    return p.taumin(i, v, j) == p.A[i][v] * p.A[v][j]


def r_K(p):
    for v in V:
        oth = [w for w in V if w != v]
        for r in (2, 3, 4):
            for S in itertools.combinations(oth, r):
                if sum(p.A[i][v] for i in S) >= 4 and all(linked(p, v, i, j) for i, j in itertools.combinations(S, 2)):
                    return ("K", v, S)
    return None


def k2ok(p, v, j, k):  # U_vU_j <= U_vU_k allowed?
    return p.A[v][j] + p.A[k][j] <= 3


def pb(p, v, j, k):
    a_jk = p.A[j][k]
    gam = a_jk if (a_jk > 1 and p.div(a_jk, v)) else 1
    u = Fr(1, 4 * gam)
    Xj, Xk = Fr(p.A[v][j], 4), Fr(p.A[v][k], 4)
    lo = max(Fr(p.taumin(v, j, k), 4 * a_jk), Xj + Xk - 1, Fr(0))
    q = lo / u
    lo = (-((-q.numerator) // q.denominator)) * u
    m = min(Xj, Xk)
    q = m / u
    hi = (q.numerator // q.denominator) * u
    if hi == m:
        if Xj < Xk:
            ok = k2ok(p, v, j, k)
        elif Xk < Xj:
            ok = k2ok(p, v, k, j)
        else:
            ok = k2ok(p, v, j, k) and k2ok(p, v, k, j)
        if not ok:
            hi -= u
    return lo, hi


def r_P(p):
    for v in V:
        oth = [w for w in V if w != v]
        H = {}
        for j, k in itertools.combinations(oth, 2):
            lo, hi = pb(p, v, j, k)
            if lo > hi:
                return ("Ppair", v, (j, k))
            H[(j, k)] = hi
        for r in (2, 3, 4):
            for S in itertools.combinations(oth, r):
                tot = Fr(0)
                for j in S:
                    tot += 1 - Fr(p.A[v][j], 4)
                for j, k in itertools.combinations(S, 2):
                    tot -= 1 - Fr(p.A[v][j], 4) - Fr(p.A[v][k], 4) + H[(j, k)]
                if tot >= 1:
                    return ("PB", v, S)
    return None


def r_N2(p):
    if all(p.A[i][j] == 2 for i, j in E):
        return ("N2",)
    return None


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def fibre_ok(p, m, inside, fixed):
    """True if some fibre assignment satisfies (F1)-(F3) (symbolic maximal gcds)."""
    opts = []
    for l in V:
        if l in inside:
            ts = [1]
        elif l in fixed:
            ts = [fixed[l]]
        else:
            ts = range(1, m + 1)
        o = []
        for t in ts:
            for M in itertools.combinations(range(m), t):
                o.append((t, frozenset(M)))
        if l == inside[0]:
            o = [(1, frozenset([0]))]
        opts.append(o)
    base2 = v2(4 // m)
    for combo in itertools.product(*opts):
        t = [c[0] for c in combo]
        bad = False
        for i in V:
            if t[i] == 1:
                for l in V:
                    if l != i and p.A[i][l] * m > 4 * t[l]:
                        bad = True
                        break
            if bad:
                break
        if bad:
            continue
        a = [base2 + v2(t[l]) + (BIG if l == p.e2 else 0) for l in V]
        b = [v3(t[l]) + (BIG if l == p.e3 else 0) for l in V]
        for c in range(m):
            S = [l for l in V if c in combo[l][1]]
            s = len(S)
            if s >= 2 and not any(2 ** min(a[x], a[y]) * 3 ** min(b[x], b[y]) >= s for x, y in itertools.combinations(S, 2)):
                bad = True
                break
        if not bad:
            return True
    return False


def r_FH2(p):
    for x, y in E:
        if p.A[x][y] != 1:
            continue
        V2 = [v for v in V if v not in (x, y) and p.A[v][x] == 2 and p.A[v][y] == 2]
        if not V2:
            continue
        if not fibre_ok(p, 4, [x, y], {v: 2 for v in V2}) and not fibre_ok(p, 2, [x, y] + V2, {}):
            return ("FH2", (x, y))
    return None


def r_RSD(p):
    for v in V:
        for w in V:
            if w == v or p.A[v][w] != 1:
                continue
            J = [j for j in V if j not in (v, w)]
            if all(p.A[v][j] == 3 for j in J) and all(p.taumin(v, w, j) >= p.A[v][w] * p.A[w][j] for j in J):
                return ("RSD", v, w)
    return None


RULES = (r_T, r_K, r_P, r_N2, r_FH2, r_RSD)


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    with open(os.path.abspath(__file__), "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    t0 = time.time()
    counts = {}
    surv = []
    rsd_needed = []  # labelled patterns whose first firing rule is RSD
    n = 0
    for al in itertools.product((1, 2, 3), repeat=10):
        for e2 in (None, 0, 1, 2, 3, 4):
            for e3 in (None, 0, 1, 2, 3, 4):
                n += 1
                p = Pat(al, e2, e3)
                w = None
                for f in RULES:
                    w = f(p)
                    if w is not None:
                        break
                if w is None:
                    counts["SURVIVE"] = counts.get("SURVIVE", 0) + 1
                    surv.append(["".join(map(str, al)), e2, e3])
                else:
                    counts[w[0]] = counts.get(w[0], 0) + 1
                    if w[0] == "RSD" and len(rsd_needed) < 50:
                        rsd_needed.append(["".join(map(str, al)), e2, e3, list(w[1:])])
    res = {"checker": "core5_check_v2", "sha256": sha, "python": sys.version, "labelled_patterns": n,
           "first_rule_counts": counts, "survivors": surv, "first_50_RSD_patterns": rsd_needed,
           "seconds": round(time.time() - t0, 1)}
    with open(os.path.join(out, "summary.json"), "x") as f:
        json.dump(res, f, indent=1)
    print(json.dumps({"n": n, "counts": counts, "survivors": len(surv), "seconds": res["seconds"]}))


if __name__ == "__main__":
    main()
