#!/usr/bin/env python3
"""k62-followon EXPLORATORY probe v1: survivor map for the K6.2* residue e_d >= 4, e* = 2, GENERIC sub-case
(no 3-marker in O, no 5-marker anywhere; f* arbitrary). EXPLORATORY ONLY; never a premise; proves nothing.
Universe: joint O-O values (alpha, alpha*) in {1,2,4}^2 with sum <= 6; joint i*-O values in {1..4}^2 with sum <= 6
(5 excluded by the T rule on {d, i*, c} with h_d = 0); alpha = alpha* = 1 on all d-edges (K62-E3 Lemma 1, no t).
Filters (each a written candidate or accepted rule; see the plan file):
 R  rows at every O-vertex, both orientations: LFC/VFC optimum <= 5 (units 1/6; Corollary 5/6-62, candidate);
 I  i*-rows, both orientations: optimum <= 11/2 (granularity 11/12 at i*), and separately < 6 (plain LFC);
 T  T rule (L1) on all O-triangles and {i*,u,v}-triangles, both orientations;
 C  shadow |Odd| <= 2 both orientations (K62-SH (i),(iii)); C2 n4 >= 2 n1 + 2 both (K62-E3); chain upper bound
    u(O) >= 4 and u(Q) >= 3 for all 4-subsets Q, both families (K62-E3 step 4 and C1).
Counts are over S5-canonical patterns of O. Stdlib only, exact Fractions; writes one JSON (exclusive) at argv[1]."""
import itertools, json, sys, time
from fractions import Fraction as Fr
from math import gcd

T0 = time.monotonic()
BUDGET = 250.0
MAXBYTES = 1 << 20


class Budget(Exception):
    pass


def chk():
    if time.monotonic() - T0 > BUDGET:
        raise Budget()


def v2(n):
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def maximal_allowed(types):
    n = len(types)
    g = [[gcd(types[i], types[j]) for j in range(n)] for i in range(n)]
    ok = [False] * (1 << n)
    for m in range(1, 1 << n):
        idx = [i for i in range(n) if m >> i & 1]
        if len(idx) == 1:
            ok[m] = True
            continue
        if not all(ok[m & ~(1 << i)] for i in idx):
            continue
        ok[m] = any(g[i][j] >= len(idx) for i, j in itertools.combinations(idx, 2))
    al = [m for m in range(1, 1 << n) if ok[m]]
    mx = [m for m in al if not any(ok[m | (1 << i)] for i in range(n) if not m >> i & 1)]
    return [[i for i in range(n) if m >> i & 1] for m in mx]


def simplex_max(c, rows):
    n, m = len(c), len(rows)
    A = [[Fr(1) if j in row else Fr(0) for j in range(n)] for row in rows]
    T = [A[r] + [Fr(1) if s == r else Fr(0) for s in range(m)] + [Fr(1)] for r in range(m)]
    obj = [Fr(-x) for x in c] + [Fr(0)] * m + [Fr(0)]
    basis = [n + r for r in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            break
        best = None
        for r in range(m):
            if T[r][enter] > 0:
                ratio = T[r][-1] / T[r][enter]
                if best is None or ratio < best[0] or (ratio == best[0] and basis[r] < basis[best[1]]):
                    best = (ratio, r)
        r = best[1]
        piv = T[r][enter]
        T[r] = [x / piv for x in T[r]]
        for rr in range(m):
            if rr != r and T[rr][enter] != 0:
                f = T[rr][enter]
                T[rr] = [a - f * b for a, b in zip(T[rr], T[r])]
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[r])]
        basis[r] = enter
    opt = obj[-1]
    y = [Fr(0)] * n
    for r, bv in enumerate(basis):
        if bv < n:
            y[bv] = T[r][-1]
    u = obj[n:n + m]
    assert all(t >= 0 for t in y) and all(sum(y[j] for j in row) <= 1 for row in rows)
    assert sum(c[j] * y[j] for j in range(n)) == opt
    assert all(t >= 0 for t in u) and sum(u) == opt
    assert all(sum(u[r] * A[r][j] for r in range(m)) >= c[j] for j in range(n))
    return opt


LPC = {}


def lp(types, loads):
    key = tuple(sorted(zip(types, loads)))
    if key not in LPC:
        LPC[key] = simplex_max([k[1] for k in key], maximal_allowed([k[0] for k in key]))
    return LPC[key]


JO = [(a, b) for a in (1, 2, 4) for b in (1, 2, 4) if a + b <= 6]
JI = [(a, b) for a in (1, 2, 3, 4) for b in (1, 2, 3, 4) if a + b <= 6]


def orow_ok(ovals, ival):
    for k in (0, 1):
        xs = [o[k] for o in ovals]
        xi = ival[k]
        types = xs + [2 ** (1 + v2(xi)), 8]
        loads = [Fr(x) for x in xs] + [Fr(xi), Fr(3)]
        if lp(types, loads) > 5:
            return False
    return True


ROWOK = {}


def row_valid(ovals, ival):
    key = (tuple(sorted(ovals)), ival)
    if key not in ROWOK:
        ROWOK[key] = orow_ok(list(ovals), ival)
    return ROWOK[key]


EDGES = [(i, j) for i in range(5) for j in range(i + 1, 5)]


def canon(E, I):
    best = None
    for p in itertools.permutations(range(5)):
        e2 = tuple(E[tuple(sorted((p[i], p[j])))] for (i, j) in EDGES)
        # relabel: new vertex p[i] gets old vertex i's data
        inv = [0] * 5
        for i in range(5):
            inv[p[i]] = i
        e3 = tuple(E[tuple(sorted((inv[a], inv[b])))] for (a, b) in EDGES)
        i3 = tuple(I[inv[a]] for a in range(5))
        cand = (e3, i3)
        if best is None or cand < best:
            best = cand
    return best


def tau_ok(a_uv_red, a_uv, b, c):
    # triangle with O-edge value a_uv (reduced a_uv_red for tau_min), other two edges b, c (all g = gamma = 6)
    tmin = a_uv_red
    for x in (b, c):
        tmin = tmin * x // gcd(tmin, x)
    tmax = min(a_uv * min(b, c), b * min(a_uv, c), c * min(a_uv, b))
    return tmin <= tmax


def T_ok(E, I):
    for k in (0, 1):
        for (u, v, w) in itertools.combinations(range(5), 3):
            a, b, c = E[(u, v)][k], E[(u, w)][k], E[(v, w)][k]
            if not tau_ok(a, a, b, c):
                return False
        for (u, v) in itertools.combinations(range(5), 2):
            a = E[(u, v)][k]
            if not tau_ok(a // gcd(a, 2), a, I[u][k], I[v][k]):
                return False
    return True


def istar_opt(I, k):
    xs = [I[c][k] for c in range(5)]
    return lp(xs + [4], [Fr(x) for x in xs] + [Fr(3, 2)])


def uQ(E, k, Q):
    best = None
    for perm in itertools.permutations(Q):
        s = 1
        for m in range(1, len(perm)):
            s += v2(min(E[tuple(sorted((perm[m], perm[j])))][k] for j in range(m)))
        best = s if best is None else min(best, s)
    return best


def C_ok(E, I):
    for k in (0, 1):
        if sum(1 for c in range(5) if I[c][k] in (1, 3)) > 2:
            return False
        vals = [E[e][k] for e in EDGES]
        if vals.count(4) < 2 * vals.count(1) + 2:
            return False
        if uQ(E, k, tuple(range(5))) < 4:
            return False
        for Q in itertools.combinations(range(5), 4):
            if uQ(E, k, Q) < 3:
                return False
    return True


def main():
    out = sys.argv[1]
    res = {'probe': 'k62_residue_survivor_map_v1', 'python': sys.version, 'status': 'INCOMPLETE'}
    seen = {}
    stats = {'row_consistent': 0, 'pass_I_g': 0, 'pass_I_plain': 0, 'pass_T': 0, 'pass_C': 0}
    E = {}
    I = [None] * 5

    def rec(v):
        chk()
        if v == 5:
            key = canon(E, I)
            if key not in seen:
                seen[key] = None
            return
        free = [(v, j) for j in range(v + 1, 5)]
        fixed = [E[(i, v)] for i in range(v)]
        for combo in itertools.product(JO, repeat=len(free)):
            if v == 0 and list(combo) != sorted(combo):
                continue
            for iv in JI:
                if not row_valid(fixed + list(combo), iv):
                    continue
                for e, val in zip(free, combo):
                    E[e] = val
                I[v] = iv
                rec(v + 1)
        for e in free:
            E.pop(e, None)
        I[v] = None

    try:
        rec(0)
        surv = []
        for key in seen:
            chk()
            e3, i3 = key
            Ed = {e: e3[n] for n, e in enumerate(EDGES)}
            Id = list(i3)
            stats['row_consistent'] += 1
            og = [istar_opt(Id, 0), istar_opt(Id, 1)]
            if max(og) < 6:
                stats['pass_I_plain'] += 1
            if max(og) > Fr(11, 2):
                continue
            stats['pass_I_g'] += 1
            if not T_ok(Ed, Id):
                continue
            stats['pass_T'] += 1
            if not C_ok(Ed, Id):
                continue
            stats['pass_C'] += 1
            if len(surv) < 200:
                surv.append({'O_edges_alpha_alphastar': [list(Ed[e]) for e in EDGES],
                             'istar_alpha_alphastar': [list(x) for x in Id], 'istar_opts': [str(o) for o in og]})
        # positive control: P_ob
        Pe = {}
        for (i, j) in EDGES:
            cyc = (j - i) % 5 in (1, 4)
            Pe[(i, j)] = (4, 2) if cyc else (2, 4)
        Pi = [(4, 2), (2, 4), (2, 4), (4, 2), (1, 2)]
        pk = canon(Pe, Pi)
        ctrl = {'P_ob_row_consistent': pk in seen,
                'P_ob_rows_valid': all(row_valid([Pe[tuple(sorted((v, j)))] for j in range(5) if j != v], Pi[v])
                                       for v in range(5)),
                'P_ob_pass_I_g': max(istar_opt(Pi, 0), istar_opt(Pi, 1)) <= Fr(11, 2),
                'P_ob_pass_T': T_ok(Pe, Pi), 'P_ob_pass_C': C_ok(Pe, Pi)}
        # negative control: an O-row with three entries 4 in both orientations is impossible by INV, and a row
        # (1,1,1,2 | 1) must be rejected by the row LP
        ctrl['neg_row_1112_rejected'] = not row_valid([(1, 1), (1, 1), (1, 1), (2, 2)], (1, 1))
        res.update({'status': 'COMPLETE', 'stats': stats, 'survivors_listed': surv, 'controls': ctrl,
                    'distinct_lps': len(LPC), 'valid_row_keys': sum(1 for x in ROWOK.values() if x),
                    'row_keys': len(ROWOK)})
    except Budget:
        res.update({'status': 'STOPPED_BUDGET', 'stats': stats, 'partial_row_consistent': len(seen)})
    res['seconds'] = round(time.monotonic() - T0, 3)
    data = json.dumps(res, indent=1)
    if len(data) > MAXBYTES:
        data = json.dumps({'status': 'OUTPUT_CAP', 'stats': stats})
    with open(out, 'x') as f:
        f.write(data)
    print(res['status'], json.dumps(stats), res['seconds'])


if __name__ == '__main__':
    main()
