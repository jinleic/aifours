#!/usr/bin/env python3
"""core56_checkB_v1 -- second, separately coded checker for Core5(6) (rules-k6-v1 + rules-k6-v2).

A lane SELF-REPORT: same author as the engine, so it is not parent-independent. It differs from
core56_engine_v1/v2 deliberately:
  * edge order is lexicographic (0,1),(0,2),...,(4,5), not the engine's (j,i) order;
  * no canonical forms: every labelled leaf of the 8 special-placement types is checked;
  * tau, links, K, P and the fibre rule are coded afresh from the rules text;
  * the Lemma R LP is solved in PRIMAL covering form, min sum mu s.t. M mu >= c, with a dense
    two-phase simplex (exact Fractions, Bland's rule), instead of the engine's dual packing simplex;
  * hereditary Sun (rules-k6-v2 L9) is used in both RLP supports and fibre cosets.
Usage: python3 core56_checkB_v1.py OUTDIR      (writes summary.json, exclusive create)
"""
import hashlib
import itertools
import json
import os
import sys
import time
from fractions import Fraction as Fr
from math import gcd

K6 = 6
EDGES = [(i, j) for i in range(K6) for j in range(i + 1, K6)]
POS = {e: n for n, e in enumerate(EDGES)}
HUGE = 40
TYPES = [(None, 0, None), (None, 0, 0), (0, 1, None), (0, 1, 0), (0, 1, 1), (0, 2, None), (0, 2, 0), (0, 2, 1)]


def val2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def val3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


def val5(n):
    c = 0
    while n % 5 == 0:
        n //= 5
        c += 1
    return c


def rgcd(alpha, z, e2, c2, e3):
    """gcd(alpha, r_z) for alpha in 1..4 (rules-k6-v1 L1)."""
    if alpha == 2 and z == e2:
        return 2
    if alpha == 3 and z == e3:
        return 3
    if alpha == 4 and z == e2:
        return 2 if c2 == 1 else 4
    return 1


class Pat:
    def __init__(self, a, typ):
        self.a = a  # dict (i,j)->alpha with i<j
        self.e2, self.c2, self.e3 = typ

    def al(self, i, j):
        return self.a[(i, j)] if i < j else self.a[(j, i)]

    def tmin(self, x, y, z):
        t = 1
        for p, q, opp in ((x, y, z), (x, z, y), (y, z, x)):
            A = self.al(p, q)
            need = A // rgcd(A, opp, self.e2, self.c2, self.e3)
            t = t * need // gcd(t, need)
        return t

    def tmax(self, x, y, z):
        p, q, r = self.al(x, y), self.al(x, z), self.al(y, z)
        return min(p * q, p * r, q * r)


def k_rule(P):
    for v in range(K6):
        others = [w for w in range(K6) if w != v]
        for size in range(2, 6):
            for S in itertools.combinations(others, size):
                if sum(P.al(i, v) for i in S) < 5:
                    continue
                if all(P.tmin(i, v, j) == P.al(i, v) * P.al(v, j) for i, j in itertools.combinations(S, 2)):
                    return ("K", v, S)
    return None


def hered(members, g):
    for size in range(2, len(members) + 1):
        for T in itertools.combinations(members, size):
            if max(g(x, y) for x, y in itertools.combinations(T, 2)) < size:
                return False
    return True


def primal_cover_min(sets, n, c):
    """min sum_S mu_S  s.t. sum_{S ni j} mu_S >= c_j, mu >= 0.  Two-phase dense simplex (Bland)."""
    m = len(sets)
    # variables: mu_0..mu_{m-1}, surplus s_0..s_{n-1}, artificial a_0..a_{n-1}
    nv = m + 2 * n
    rows = []
    for j in range(n):
        row = [Fr(0)] * nv
        for t, S in enumerate(sets):
            if j in S:
                row[t] = Fr(1)
        row[m + j] = Fr(-1)
        row[m + n + j] = Fr(1)
        rows.append(row + [Fr(c[j])])
    basis = [m + n + j for j in range(n)]

    def solve(cost):
        # reduced costs z_j - c_j style: we minimise cost . x
        while True:
            # compute reduced costs
            cb = [cost[b] for b in basis]
            best = None
            for col in range(nv):
                if col in basis:
                    continue
                red = cost[col] - sum(cb[i] * rows[i][col] for i in range(n))
                if red < 0:
                    best = col
                    break
            if best is None:
                return sum(cb[i] * rows[i][-1] for i in range(n))
            leave = None
            ratio = None
            for i in range(n):
                if rows[i][best] > 0:
                    rt = rows[i][-1] / rows[i][best]
                    if ratio is None or rt < ratio or (rt == ratio and basis[i] < basis[leave]):
                        ratio, leave = rt, i
            if leave is None:
                raise RuntimeError("unbounded")
            pv = rows[leave][best]
            rows[leave] = [x / pv for x in rows[leave]]
            for i in range(n):
                if i != leave and rows[i][best] != 0:
                    f = rows[i][best]
                    rows[i] = [x - f * y for x, y in zip(rows[i], rows[leave])]
            basis[leave] = best
    phase1 = [Fr(0)] * (m + n) + [Fr(1)] * n
    if solve(phase1) != 0:
        raise RuntimeError("infeasible")  # cannot happen: singletons are allowed
    # drive artificials out is unnecessary for optimality value since they are 0; block them
    cost2 = [Fr(1)] * m + [Fr(0)] * n + [Fr(10 ** 9)] * n
    return solve(cost2)


_CACHE = {}


def lp_total(qs, st):
    key = (qs, st)
    if key in _CACHE:
        return _CACHE[key]
    n = len(qs)
    ex = []
    for x in range(n):
        two = val2(qs[x]) + (0 if st[x][0] == 0 else (1 if st[x][0] == 1 else HUGE))
        three = val3(qs[x]) + (HUGE if st[x][1] else 0)
        ex.append((two, three))

    def g(x, y):
        return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1]))
    supp = [S for size in range(1, n + 1) for S in itertools.combinations(range(n), size) if size == 1 or hered(S, g)]
    val = primal_cover_min([set(S) for S in supp], n, [Fr(q, 5) for q in qs])
    _CACHE[key] = val
    return val


def st_of(j, P):
    return ((P.c2 if j == P.e2 else 0), (1 if j == P.e3 else 0))


def rlp_rule(P):
    for v in range(K6):
        nb = [w for w in range(K6) if w != v]
        st = tuple(st_of(j, P) for j in nb)
        ok_any = False
        for qs in itertools.product(*[range(1, 6 - P.al(v, j)) for j in nb]):
            if lp_total(qs, st) < 1:
                ok_any = True
                break
        if not ok_any:
            return ("RLP", v)
    return None


def p_rule(P):
    for v in range(K6):
        nb = [w for w in range(K6) if w != v]
        size = {j: Fr(P.al(v, j), 5) for j in nb}
        top = {}
        for j, k in itertools.combinations(nb, 2):
            unit = Fr(1, 5 * rgcd(P.al(j, k), v, P.e2, P.c2, P.e3))
            low = max(Fr(P.tmin(v, j, k), 5 * P.al(j, k)), size[j] + size[k] - 1, Fr(0))
            nlow = -((-low) // unit)
            low = nlow * unit
            small = min(size[j], size[k])
            hi = (small // unit) * unit
            if hi == small:
                cj = P.al(v, j) + P.al(k, j) <= 4  # U_vU_j <= U_vU_k allowed
                ck = P.al(v, k) + P.al(j, k) <= 4  # U_vU_k <= U_vU_j allowed
                if size[j] < size[k]:
                    allow = cj
                elif size[k] < size[j]:
                    allow = ck
                else:
                    allow = cj and ck
                if not allow:
                    hi -= unit
            if low > hi:
                return ("Ppair", v, (j, k))
            top[(j, k)] = hi
        for sz in range(2, 6):
            for S in itertools.combinations(nb, sz):
                lhs = sum(1 - size[j] for j in S) - sum(1 - size[j] - size[k] + top[(j, k)] for j, k in itertools.combinations(S, 2))
                if lhs >= 1:
                    return ("PB", v, S)
    return None


def fib_ex(l, t, P, e5):
    two, three, five = val2(t), val3(t), val5(t)
    if l == P.e2:
        two += 1 if P.c2 == 1 else HUGE
    if l == P.e3:
        three += HUGE
    if l == e5:
        five += HUGE
    return two, three, five


def fibre_ok(P, e5, inside, forced):
    choices = []
    for l in range(K6):
        if l == inside[0]:
            choices.append([(1, frozenset([0]))])
            continue
        if l in inside:
            ts = [1]
        elif l in forced:
            ts = [forced[l]]
        else:
            ts = [1, 2, 3, 4, 5]
        choices.append([(t, frozenset(M)) for t in ts for M in itertools.combinations(range(5), t)])
    for pick in itertools.product(*choices):
        tt = [p[0] for p in pick]
        if any(tt[i] == 1 and P.al(i, l) > tt[l] for i in range(K6) for l in range(K6) if l != i):
            continue
        ex = [fib_ex(l, tt[l], P, e5) for l in range(K6)]

        def g(x, y):
            return (2 ** min(ex[x][0], ex[y][0])) * (3 ** min(ex[x][1], ex[y][1])) * (5 ** min(ex[x][2], ex[y][2]))
        good = True
        for cst in range(5):
            mem = [l for l in range(K6) if cst in pick[l][1]]
            if len(mem) >= 2 and not hered(mem, g):
                good = False
                break
        if good:
            return True
    return False


def fh_rule(P):
    for a, b in itertools.combinations(range(K6), 2):
        if P.al(a, b) != 1:
            continue
        Vs = {v: P.al(v, a) for v in range(K6) if v not in (a, b) and P.al(v, a) == P.al(v, b)}
        if not Vs:
            continue
        inside = [a, b] + sorted(v for v in Vs if Vs[v] == 1)
        forced = {v: c for v, c in Vs.items() if c > 1}
        if not any(fibre_ok(P, e5, inside, forced) for e5 in [None] + list(range(K6))):
            return ("FH5", (a, b))
    return None


def main():
    out = sys.argv[1]
    os.makedirs(out, exist_ok=False)
    with open(os.path.abspath(__file__), "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    t0 = time.time()
    # triangles completed at each lexicographic edge position
    tri_done = {}
    for (x, y, z) in itertools.combinations(range(K6), 3):
        last = max(POS[(x, y)], POS[(x, z)], POS[(y, z)])
        tri_done.setdefault(last, []).append((x, y, z))
    res = {}
    surv = []
    for typ in TYPES:
        tt = time.time()
        a = {}
        cnt = {}
        nleaf = 0

        def go(pos):
            nonlocal nleaf
            if pos == len(EDGES):
                nleaf += 1
                P = Pat(a, typ)
                w = k_rule(P) or rlp_rule(P) or p_rule(P) or fh_rule(P)
                key = w[0] if w else "SURVIVE"
                cnt[key] = cnt.get(key, 0) + 1
                if w is None and len(surv) < 200:
                    surv.append([list(typ), [a[e] for e in EDGES]])
                return
            e = EDGES[pos]
            for v in (1, 2, 3, 4):
                a[e] = v
                P = Pat(a, typ)
                if all(P.tmin(*tr) <= P.tmax(*tr) for tr in tri_done.get(pos, [])):
                    go(pos + 1)
            del a[e]
        go(0)
        res[str(typ)] = {"labelled_T_consistent_leaves": nleaf, "first_rule_counts": cnt, "seconds": round(time.time() - tt, 1)}
        print(typ, res[str(typ)], flush=True)
    summ = {"checker": "core56_checkB_v1", "sha256": sha, "python": sys.version, "by_type": res,
            "survivors_first_200": surv, "total_survivors": sum(v["first_rule_counts"].get("SURVIVE", 0) for v in res.values()),
            "lp_cache": len(_CACHE), "seconds": round(time.time() - t0, 1)}
    with open(os.path.join(out, "summary.json"), "x") as f:
        json.dump(summ, f, indent=1)
    print(json.dumps({"total_survivors": summ["total_survivors"], "seconds": summ["seconds"]}))


if __name__ == "__main__":
    main()
