#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v13: v12 plus RPLP (both orientations) at SECONDARY centres (argv[7], JSON list) as soon as
their rows are complete, with exact data for decided pairs and the sound relaxation (union over values admissible by
T/Ppair through z and through the secondary centre) for undecided pairs; pairs incident to secondary centres are
branched first.  formerly v12/v11/v6b/v6a: as v5 (LFC + INV + T + Ppair(K2) on both alpha and alpha*), but for SELECTED profile tuples
only (argv[3] = JSON list of item indices in the class job list), with a larger solution cap and canonical
deduplication of solutions under all permutations of vertices preserving the labelled profiles.

EXPLORATORY ONLY; never a premise.  Python standard library only; self wall budget 270 s.
argv: OUT CLASSES  (CLASSES = comma list from K7,K63,K62).  Writes OUT (exclusive create).
Rules used: Lemma LFC (row value < 1 at every vertex, for alpha AND alpha*), Lemma INV (alpha + alpha* <= g
entrywise, same labelled profiles), and T + Ppair with K2 on every triangle for alpha and for alpha*.
Search: domains of joint rows per vertex; minimum-remaining-values vertex choice; forward checking of every
unassigned vertex's domain against each new assignment; symmetry breaking only at the first assigned vertex
(entries non-decreasing over neighbours of identical profile), valid because permuting identical-profile
vertices that fixes the first vertex maps joint solutions to joint solutions.
"""
import itertools, json, math, os, sys, time
from fractions import Fraction as F

T0 = time.monotonic()
BUDGET = 270.0
CAP = 60000


class Budget(Exception):
    pass


def chk():
    if time.monotonic() - T0 > BUDGET:
        raise Budget()


def v(p, n):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def lab(prof, alpha, g):
    e, f, h = prof
    a2 = e + v(2, alpha) - v(2, g)
    a3 = f + v(3, alpha) - v(3, g)
    a5 = h + v(5, alpha) - v(5, g)
    assert a2 >= 0 and a3 >= 0 and a5 >= 0
    return (2 ** a2) * (3 ** a3) * (5 ** a5)


def gn(p, q):
    return (2 ** min(p[0], q[0])) * (3 ** min(p[1], q[1])) * (5 ** min(p[2], q[2]))


ALLOWED_CACHE = {}


def maximal_allowed(labels):
    key = tuple(labels)
    if key in ALLOWED_CACHE:
        return ALLOWED_CACHE[key]
    n = len(labels)
    good = {}
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            if r == 1:
                good[S] = True
                continue
            ok = all(good[T] for T in itertools.combinations(S, r - 1))
            if ok:
                ok = max(math.gcd(labels[a], labels[b]) for a, b in itertools.combinations(S, 2)) >= r
            good[S] = ok
    allowed = [S for S, ok in good.items() if ok]
    sets = set(allowed)
    maximal = [S for S in allowed
               if not any(tuple(sorted(S + (x,))) in sets for x in range(n) if x not in S)]
    ALLOWED_CACHE[key] = maximal
    return maximal


def lp_max(c, rows):
    n, m = len(c), len(rows)
    tab = []
    for i, r in enumerate(rows):
        row = [F(1) if j in r else F(0) for j in range(n)] + [F(0)] * m + [F(1)]
        row[n + i] = F(1)
        tab.append(row)
    obj = [-x for x in c] + [F(0)] * m + [F(0)]
    basis = [n + i for i in range(m)]
    while True:
        e = next((j for j in range(n + m) if obj[j] < 0), None)
        if e is None:
            return obj[-1]
        best = None
        for i in range(m):
            a = tab[i][e]
            if a > 0:
                ratio = tab[i][-1] / a
                if best is None or ratio < best[0] or (ratio == best[0] and basis[i] < basis[best[1]]):
                    best = (ratio, i)
        i = best[1]
        piv = tab[i][e]
        tab[i] = [x / piv for x in tab[i]]
        for k in range(m):
            if k != i and tab[k][e] != 0:
                fac = tab[k][e]
                tab[k] = [a - fac * b for a, b in zip(tab[k], tab[i])]
        fac = obj[e]
        obj = [a - fac * b for a, b in zip(obj, tab[i])]
        basis[i] = e


LP_CACHE = {}


def row_val(nbrs, alphas):
    items = sorted((lab(p, a, g), F(a, g)) for (g, p), a in zip(nbrs, alphas))
    key = tuple(items)
    r = LP_CACHE.get(key)
    if r is None:
        r = lp_max([x[1] for x in items], maximal_allowed([x[0] for x in items]))
        LP_CACHE[key] = r
    return r


def vals(prof):
    return prof  # capped (e, f, h)


def nv(P):
    return P


def gval(P, Q):
    return tuple(min(a, b) for a, b in zip(P, Q))


def num(vv):
    return (2 ** vv[0]) * (3 ** vv[1]) * (5 ** vv[2])


def vp_int(n):
    return (v(2, n), v(3, n), v(5, n))


TRI_CACHE = {}


def tri_ok(Px, Py, Pz, axy, axz, ayz):
    """T and Ppair (rules-k7-v1 L1, L4 with K2) on triangle {x,y,z}; True iff not killed."""
    key = (Px, Py, Pz, axy, axz, ayz)
    r = TRI_CACHE.get(key)
    if r is not None:
        return r
    P = {'x': Px, 'y': Py, 'z': Pz}
    A = {frozenset('xy'): axy, frozenset('xz'): axz, frozenset('yz'): ayz}
    G = {frozenset('xy'): gval(Px, Py), frozenset('xz'): gval(Px, Pz), frozenset('yz'): gval(Py, Pz)}

    def g(a, b):
        return num(G[frozenset(a + b)])

    def al(a, b):
        return A[frozenset(a + b)]

    def gamma(y):
        others = [t for t in 'xyz' if t != y]
        return num(tuple(max(G[frozenset(y + others[0])][i], G[frozenset(y + others[1])][i]) for i in range(3)))

    def ell_val(z):
        gz = vp_int(gamma(z))
        return tuple(P[z][i] - gz[i] for i in range(3))

    def gcd_alpha_ell(a, z):
        le = ell_val(z)
        va = vp_int(a)
        return num(tuple(min(va[i], le[i]) for i in range(3)))
    tmin = 1
    for e in ('xy', 'xz', 'yz'):
        z = [t for t in 'xyz' if t not in e][0]
        a = al(e[0], e[1])
        term = a // gcd_alpha_ell(a, z)
        tmin = tmin * term // math.gcd(tmin, term)
    tmax = None
    for y in 'xyz':
        x, z = [t for t in 'xyz' if t != y]
        bound = gamma(y) * al(x, z) * min(F(al(x, y), g(x, y)), F(al(y, z), g(y, z)))
        b = math.floor(bound)
        tmax = b if tmax is None else min(tmax, b)
    if tmin > tmax:
        TRI_CACHE[key] = False
        return False
    for vv in 'xyz':
        j, k = [t for t in 'xyz' if t != vv]
        mj = F(al(vv, j), g(vv, j))
        mk = F(al(vv, k), g(vv, k))
        ajk = al(j, k)
        vj, vk, vvv = P[j], P[k], P[vv]
        vajk = vp_int(ajk)
        gexp = tuple(min(vvv[i], max(vj[i], vk[i]) + vajk[i]) for i in range(3))
        u = F(1, num(gexp))
        Lb = max(F(tmin, gamma(vv) * ajk), mj + mk - 1, F(0))
        lo = u * math.ceil(Lb / u)
        m = min(mj, mk)
        hi = u * math.floor(m / u)
        if hi == m:
            barj = mj + F(ajk, g(j, k)) >= 1   # X_j subset X_k barred by K2
            bark = mk + F(ajk, g(j, k)) >= 1   # X_k subset X_j barred by K2
            if mj < mk:
                barred = barj
            elif mk < mj:
                barred = bark
            else:
                barred = barj or bark
            if barred:
                hi -= u
        if lo > hi:
            TRI_CACHE[key] = False
            return False
    TRI_CACHE[key] = True
    return True


def simplex_min(c, A_eq, b_eq, eps=1e-9):
    """Float two-phase simplex (Bland). minimize c.x s.t. A_eq x = b_eq, x >= 0. Returns (status, value)."""
    m = len(A_eq)
    n = len(c)
    A = [row[:] for row in A_eq]
    b = b_eq[:]
    for i in range(m):
        if b[i] < 0:
            A[i] = [-x for x in A[i]]
            b[i] = -b[i]
    # phase 1 tableau with artificials
    T = [A[i] + [1.0 if k == i else 0.0 for k in range(m)] + [b[i]] for i in range(m)]
    basis = [n + i for i in range(m)]
    ncols = n + m

    def pivot(r, col):
        pv = T[r][col]
        T[r] = [x / pv for x in T[r]]
        for k in range(m):
            if k != r and abs(T[k][col]) > 0:
                f = T[k][col]
                rowr = T[r]
                T[k] = [a - f * bb for a, bb in zip(T[k], rowr)]
        basis[r] = col

    def run(cost, allowed_cols):
        while True:
            # reduced costs
            best = None
            for col in allowed_cols:
                if col in basis:
                    continue
                rc = cost[col] - sum(cost[basis[i]] * T[i][col] for i in range(m))
                if rc < -eps:
                    best = col
                    break
            if best is None:
                return 'optimal'
            col = best
            r = None
            for i in range(m):
                if T[i][col] > eps:
                    ratio = T[i][-1] / T[i][col]
                    if r is None or ratio < r[0] - 1e-12 or (abs(ratio - r[0]) <= 1e-12 and basis[i] < basis[r[1]]):
                        r = (ratio, i)
            if r is None:
                return 'unbounded'
            pivot(r[1], col)
    cost1 = [0.0] * n + [1.0] * m
    run(cost1, list(range(ncols)))
    val1 = sum(cost1[basis[i]] * T[i][-1] for i in range(m))
    if val1 > 1e-7:
        return 'infeasible', None
    # drive artificials out of basis where possible
    for i in range(m):
        if basis[i] >= n:
            for col in range(n):
                if abs(T[i][col]) > 1e-9:
                    pivot(i, col)
                    break
    cost2 = list(c) + [0.0] * m
    st = run(cost2, list(range(n)))
    if st == 'unbounded':
        return 'unbounded', None
    val = sum(cost2[basis[i]] * T[i][-1] for i in range(m))
    return 'optimal', val


def tri_tmin(Pv, Pa, Pb, a_va, a_vb, a_ab):
    """tau_min of triangle {v,a,b} (rules-k7-v1 L1)."""
    P = {'v': Pv, 'a': Pa, 'b': Pb}
    A = {frozenset('va'): a_va, frozenset('vb'): a_vb, frozenset('ab'): a_ab}
    G = {frozenset('va'): gval(Pv, Pa), frozenset('vb'): gval(Pv, Pb), frozenset('ab'): gval(Pa, Pb)}

    def gamma_vals(y):
        o = [t for t in 'vab' if t != y]
        return tuple(max(G[frozenset(y + o[0])][i], G[frozenset(y + o[1])][i]) for i in range(3))
    t = 1
    for e in ('va', 'vb', 'ab'):
        z = [s for s in 'vab' if s not in e][0]
        al = A[frozenset(e)]
        gz = gamma_vals(z)
        le = tuple(P[z][i] - gz[i] for i in range(3))
        va = vp_int(al)
        gg = num(tuple(min(va[i], le[i]) for i in range(3)))
        term = al // gg
        t = t * term // math.gcd(t, term)
    return t


def pair_bounds(Pv, Pj, Pk, a_vj, a_vk, a_jk):
    """(lo, hi) for mu(X_j cap X_k) at apex v (rules-k7-addendum A1 (F6) = L4 with K2)."""
    gvj = num(gval(Pv, Pj)); gvk = num(gval(Pv, Pk)); gjk = num(gval(Pj, Pk))
    mj = F(a_vj, gvj); mk = F(a_vk, gvk)
    tmin = tri_tmin(Pv, Pj, Pk, a_vj, a_vk, a_jk)
    gam = num(tuple(max(gval(Pv, Pj)[i], gval(Pv, Pk)[i]) for i in range(3)))
    vajk = vp_int(a_jk)
    gexp = tuple(min(Pv[i], max(Pj[i], Pk[i]) + vajk[i]) for i in range(3))
    u = F(1, num(gexp))
    Lb = max(F(tmin, gam * a_jk), mj + mk - 1, F(0))
    lo = u * math.ceil(Lb / u)
    m = min(mj, mk)
    hi = u * math.floor(m / u)
    if hi == m:
        barj = mj + F(a_jk, gjk) >= 1
        bark = mk + F(a_jk, gjk) >= 1
        barred = barj if mj < mk else (bark if mk < mj else (barj or bark))
        if barred:
            hi -= u
    return lo, hi


RPLP_CACHE = {}
killed = [0]


def rplp_kills(vv, profs, AL, Q):
    """RPLP-k7 at vertex vv for the pattern AL (alpha) with the TRUE q-row Q[vv] (INV: q = alpha*).
    Returns True iff the LP {E1, E2, B, columns} has no solution with total < 1 (float, exploratory)."""
    N = [j for j in range(7) if j != vv]
    key = (vv, tuple(profs), tuple(tuple(r) for r in AL), tuple(Q[vv][j] for j in N))
    if key in RPLP_CACHE:
        return RPLP_CACHE[key]
    Pv = profs[vv]
    g = {j: num(gval(Pv, profs[j])) for j in N}
    labels = [lab(profs[j], Q[vv][j], g[j]) for j in N]
    idx = {j: t for t, j in enumerate(N)}
    allowed = set()
    for r in range(0, 7):
        for S in itertools.combinations(N, r):
            ok = True
            for rr in range(2, len(S) + 1):
                for T in itertools.combinations(S, rr):
                    if max(math.gcd(labels[idx[a]], labels[idx[b]]) for a, b in itertools.combinations(T, 2)) < rr:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                allowed.add(S)
    forced = []
    for a in N:
        for b in N:
            if a == b:
                continue
            tmin = tri_tmin(Pv, profs[a], profs[b], AL[vv][a], AL[vv][b], AL[a][b])
            gam = num(tuple(max(gval(Pv, profs[a])[i], gval(Pv, profs[b])[i]) for i in range(3)))
            if tmin * g[a] >= gam * AL[a][b] * AL[vv][a]:
                forced.append((a, b))
    tight = {j for j in N if AL[vv][j] + Q[vv][j] == g[j]}
    cols = []
    for r in range(1, 7):
        for Aset in itertools.combinations(N, r):
            As = set(Aset)
            if any((b in As) and (a not in As) for a, b in forced):
                continue
            for S in allowed:
                if not set(S) <= As:
                    continue
                if any((j in As) and (j not in S) for j in tight):
                    continue
                cols.append((As, set(S)))
    rows, rhs = [], []
    for j in N:
        rows.append([1.0 if j in S else 0.0 for A_, S in cols]); rhs.append(float(F(Q[vv][j], g[j])))
    for j in N:
        rows.append([1.0 if j in A_ else 0.0 for A_, S in cols]); rhs.append(float(1 - F(AL[vv][j], g[j])))
    nslack = 0
    ineq = []
    for j, k in itertools.combinations(N, 2):
        lo, hi = pair_bounds(Pv, profs[j], profs[k], AL[vv][j], AL[vv][k], AL[j][k])
        mj = F(AL[vv][j], g[j]); mk = F(AL[vv][k], g[k])
        ylo = 1 - mj - mk + lo
        yhi = 1 - mj - mk + hi
        if yhi < 0:
            RPLP_CACHE[key] = True
            return True
        coef = [1.0 if (j in A_ and k in A_) else 0.0 for A_, S in cols]
        ineq.append((coef, float(yhi), +1))
        if ylo > 0:
            ineq.append((coef, float(ylo), -1))
    ncol = len(cols)
    tot = len(ineq)
    Aeq = []
    beq = []
    for row, r_ in zip(rows, rhs):
        Aeq.append(row + [0.0] * tot); beq.append(r_)
    for t, (coef, bound, sgn) in enumerate(ineq):
        sl = [0.0] * tot
        sl[t] = 1.0 if sgn > 0 else -1.0
        Aeq.append(coef + sl); beq.append(bound)
    cost = [1.0] * ncol + [0.0] * tot
    st, val = simplex_min(cost, Aeq, beq)
    kill = (st == 'infeasible') or (st == 'optimal' and val >= 1 - 1e-9)
    RPLP_CACHE[key] = kill
    return kill


SURV = {}


def survivors(nbrs):
    key = tuple(nbrs)
    if key not in SURV:
        res = []
        for al in itertools.product(*[range(1, g) for g, p in nbrs]):
            chk()
            if row_val(nbrs, al) < 1:
                res.append(al)
        SURV[key] = res
    return SURV[key]


def k7_profiles():
    res = []
    for e2 in (None, 2, 3, 4):
        for f3 in (None, 2):
            for h5 in (None, 1, 2):
                p2 = [None] if e2 is None else [0]
                p3 = [None] if f3 is None else [0, 1]
                p5 = [None] if h5 is None else [0, 1, 2]
                for a in p2:
                    for b in p3:
                        for c in p5:
                            pr = [[1, 1, 0] for _ in range(7)]
                            if a is not None:
                                pr[a][0] = e2
                            if b is not None:
                                pr[b][1] = f3
                            if c is not None:
                                pr[c][2] = h5
                            res.append(tuple(tuple(x) for x in pr))
    return sorted(set(res))


def k63_profiles():
    res = []
    for e2 in (None, 2, 3, 4):
        for f3pos in (None, 'd', 0, 1):
            for h5 in (None, 1, 2):
                for h5pos in ((None,) if h5 is None else ('d', 0, 1, 2)):
                    pr = [[1, 1, 0] for _ in range(6)] + [[0, 1, 0]]
                    if e2 is not None:
                        pr[0][0] = e2
                    if f3pos is not None:
                        pr[6 if f3pos == 'd' else f3pos][1] = 2
                    if h5pos is not None:
                        pr[6 if h5pos == 'd' else h5pos][2] = h5
                    res.append(tuple(tuple(x) for x in pr))
    return sorted(set(res))


def k62_profiles():
    res = []
    for es, ed in ((2, 2), (2, 3), (2, 4), (3, 2), (4, 2)):
        for f3pos in (None, 0, 1):
            for h5 in (None, 1, 2):
                for h5pos in ((None,) if h5 is None else ('d', 0, 1, 2)):
                    pr = [[1, 1, 0] for _ in range(6)] + [[ed, 0, 0]]
                    pr[0][0] = es
                    if f3pos is not None:
                        pr[f3pos][1] = 2
                    if h5pos is not None:
                        pr[6 if h5pos == 'd' else h5pos][2] = h5
                    res.append(tuple(tuple(x) for x in pr))
    return sorted(set(res))


def gmatrix(profs):
    return [[gn(profs[i], profs[j]) if i != j else 0 for j in range(7)] for i in range(7)]


def check_class(cls, G):
    for i in range(7):
        for j in range(i + 1, 7):
            if cls == 'K7':
                want = 6
            elif cls == 'K63':
                want = 3 if 6 in (i, j) else 6
            else:
                want = (4 if 0 in (i, j) else 2) if 6 in (i, j) else 6
            if G[i][j] != want:
                return False
    return True


def domains(profs, G):
    doms = []
    for w in range(7):
        nb = [j for j in range(7) if j != w]
        nbrs = [(G[w][j], profs[j]) for j in nb]
        S = survivors(nbrs)
        gs = [G[w][j] for j in nb]
        d = []
        for s in S:
            for t in S:
                if all(a + b <= g for a, b, g in zip(s, t, gs)):
                    row = [None] * 7
                    for j, a, b in zip(nb, s, t):
                        row[j] = (a, b)
                    d.append(tuple(row))
        chk()
        doms.append(d)
    return doms


def symmetric_ok(row, w, profs):
    """first-vertex symmetry breaking: over neighbours of identical profile, entries non-decreasing."""
    groups = {}
    for j in range(7):
        if j != w:
            groups.setdefault(profs[j], []).append(j)
    for js in groups.values():
        vals = [row[j] for j in js]
        if any(vals[i] > vals[i + 1] for i in range(len(vals) - 1)):
            return False
    return True


def search(doms, profs):
    sols = []
    nodes = [0]
    killed[0] = 0

    def rec(assigned, doms):
        chk()
        nodes[0] += 1
        un = [w for w in range(7) if w not in assigned]
        if not un:
            AL = [[assigned[i][j][0] if i != j else 0 for j in range(7)] for i in range(7)]
            AS = [[assigned[i][j][1] if i != j else 0 for j in range(7)] for i in range(7)]
            for x in range(7):
                if rplp_kills(x, profs, AL, AS) or rplp_kills(x, profs, AS, AL):
                    killed[0] += 1
                    return
            sols.append({w: assigned[w] for w in range(7)})
            if len(sols) >= CAP:
                raise OverflowError()
            return
        w = min(un, key=lambda x: len(doms[x]))
        cands = doms[w]
        if not assigned:
            cands = [r for r in cands if symmetric_ok(r, w, profs)]
        for r in cands:
            # triangles {w, x, y} with x already assigned are fully determined now
            ok = True
            for x in assigned:
                for y in range(7):
                    if y == w or y == x:
                        continue
                    a_wx, a_wy, a_xy = r[x], r[y], assigned[x][y]
                    if not (tri_ok(profs[w], profs[x], profs[y], a_wx[0], a_wy[0], a_xy[0]) and
                            tri_ok(profs[w], profs[x], profs[y], a_wx[1], a_wy[1], a_xy[1])):
                        ok = False
                        break
                if not ok:
                    break
            if not ok:
                continue
            nd = list(doms)
            for u in un:
                if u == w:
                    continue
                need = r[u]
                f = []
                for xr in nd[u]:
                    if xr[w] != need:
                        continue
                    good = True
                    for y in range(7):
                        if y == u or y == w:
                            continue
                        a_uw, a_uy, a_wy = xr[w], xr[y], r[y]
                        if not (tri_ok(profs[u], profs[w], profs[y], a_uw[0], a_uy[0], a_wy[0]) and
                                tri_ok(profs[u], profs[w], profs[y], a_uw[1], a_uy[1], a_wy[1])):
                            good = False
                            break
                    if good:
                        f.append(xr)
                if not f:
                    ok = False
                    break
                nd[u] = f
            if ok:
                assigned[w] = r
                rec(assigned, nd)
                del assigned[w]
    capped = False
    try:
        rec({}, doms)
    except OverflowError:
        capped = True
    return sols, capped, nodes[0]



def rplp_kills_pd(vv, profs, rowA, rowQ, pairdata):
    """RPLP-k7 at vv: rowA[j] = alpha_vj, rowQ[j] = q_j (true q = alpha* or alpha), pairdata[(j,k)] (j<k) =
    (lo, hi, forced_jk, forced_kj) for mu(X_j cap X_k) and F7.  Returns True iff no x with total < 1 (float)."""
    N = [j for j in range(7) if j != vv]
    Pv = profs[vv]
    g = {j: num(gval(Pv, profs[j])) for j in N}
    labels = {j: lab(profs[j], rowQ[j], g[j]) for j in N}
    allowed = set()
    for r in range(0, 7):
        for S in itertools.combinations(N, r):
            ok = True
            for rr in range(2, len(S) + 1):
                for T in itertools.combinations(S, rr):
                    if max(math.gcd(labels[a], labels[b]) for a, b in itertools.combinations(T, 2)) < rr:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                allowed.add(S)
    forced = []
    for (j, k), (lo, hi, fjk, fkj) in pairdata.items():
        if fjk:
            forced.append((j, k))
        if fkj:
            forced.append((k, j))
    tight = {j for j in N if rowA[j] + rowQ[j] == g[j]}
    cols = []
    for r in range(1, 7):
        for Aset in itertools.combinations(N, r):
            As = set(Aset)
            if any((b in As) and (a not in As) for a, b in forced):
                continue
            for S in allowed:
                if not set(S) <= As:
                    continue
                if any((j in As) and (j not in S) for j in tight):
                    continue
                cols.append((As, set(S)))
    rows, rhs = [], []
    for j in N:
        rows.append([1.0 if j in S else 0.0 for A_, S in cols]); rhs.append(float(F(rowQ[j], g[j])))
    for j in N:
        rows.append([1.0 if j in A_ else 0.0 for A_, S in cols]); rhs.append(float(1 - F(rowA[j], g[j])))
    ineq = []
    for (j, k), (lo, hi, fjk, fkj) in pairdata.items():
        mj = F(rowA[j], g[j]); mk = F(rowA[k], g[k])
        ylo = 1 - mj - mk + lo
        yhi = 1 - mj - mk + hi
        if yhi < 0:
            return True
        coef = [1.0 if (j in A_ and k in A_) else 0.0 for A_, S in cols]
        ineq.append((coef, float(yhi), +1))
        if ylo > 0:
            ineq.append((coef, float(ylo), -1))
    tot = len(ineq)
    Aeq, beq = [], []
    for row, r_ in zip(rows, rhs):
        Aeq.append(row + [0.0] * tot); beq.append(r_)
    for t, (coef, bound, sgn) in enumerate(ineq):
        sl = [0.0] * tot
        sl[t] = 1.0 if sgn > 0 else -1.0
        Aeq.append(coef + sl); beq.append(bound)
    cost = [1.0] * len(cols) + [0.0] * tot
    st, val = simplex_min(cost, Aeq, beq)
    return (st == 'infeasible') or (st == 'optimal' and val >= 1 - 1e-9)


def pair_info(Pz, Pj, Pk, a_zj, a_zk, a_jk):
    lo, hi = pair_bounds(Pz, Pj, Pk, a_zj, a_zk, a_jk)
    gzj = num(gval(Pz, Pj)); gzk = num(gval(Pz, Pk))
    gam = num(tuple(max(gval(Pz, Pj)[i], gval(Pz, Pk)[i]) for i in range(3)))
    t = tri_tmin(Pz, Pj, Pk, a_zj, a_zk, a_jk)
    fjk = t * gzj >= gam * a_jk * a_zj
    fkj = t * gzk >= gam * a_jk * a_zk
    return lo, hi, fjk, fkj


def full_leaf_dead(profs, G, AL, AS):
    """Full checks on a complete joint pattern: LFC rows (both sides), T/Ppair on all triangles (both sides),
    RPLP at every vertex (both orientations). True iff some rule kills."""
    for v in range(7):
        nb = [j for j in range(7) if j != v]
        nbrs = [(G[v][j], profs[j]) for j in nb]
        if row_val(nbrs, [AL[v][j] for j in nb]) >= 1:
            return 'LFC'
        if row_val(nbrs, [AS[v][j] for j in nb]) >= 1:
            return 'LFC*'
    for a, b, c in itertools.combinations(range(7), 3):
        if not tri_ok(profs[a], profs[b], profs[c], AL[a][b], AL[a][c], AL[b][c]):
            return 'T/Ppair'
        if not tri_ok(profs[a], profs[b], profs[c], AS[a][b], AS[a][c], AS[b][c]):
            return 'T/Ppair*'
    for v in range(7):
        N = [j for j in range(7) if j != v]
        pdA = {}
        pdQ = {}
        for j, k in itertools.combinations(N, 2):
            pdA[(j, k)] = pair_info(profs[v], profs[j], profs[k], AL[v][j], AL[v][k], AL[j][k])
            pdQ[(j, k)] = pair_info(profs[v], profs[j], profs[k], AS[v][j], AS[v][k], AS[j][k])
        if rplp_kills_pd(v, profs, {j: AL[v][j] for j in N}, {j: AS[v][j] for j in N}, pdA):
            return 'RPLP@%d' % v
        if rplp_kills_pd(v, profs, {j: AS[v][j] for j in N}, {j: AL[v][j] for j in N}, pdQ):
            return 'RPLP*@%d' % v
    return None


SECONDARY = []


def vertex_domains(profs, G):
    doms = {}
    for w in range(7):
        nb = [j for j in range(7) if j != w]
        nbrs = [(G[w][j], profs[j]) for j in nb]
        S = survivors(nbrs)
        gs = [G[w][j] for j in nb]
        d = []
        for s in S:
            for t in S:
                if all(a + b <= g for a, b, g in zip(s, t, gs)):
                    d.append({j: (a, b) for j, a, b in zip(nb, s, t)})
        doms[w] = d
    return doms


def centre_search(profs, G, z, deadline, leaf_cap):
    U = [j for j in range(7) if j != z]
    VD = vertex_domains(profs, G)
    nbrs = [(G[z][j], profs[j]) for j in U]
    S = survivors(nbrs)
    gs = [G[z][j] for j in U]
    zrows = []
    for s in S:
        for t in S:
            if all(a + b <= gg for a, b, gg in zip(s, t, gs)):
                jr = list(zip(s, t))
                ok = True
                for i1 in range(len(U)):
                    for i2 in range(i1 + 1, len(U)):
                        if profs[U[i1]] == profs[U[i2]] and jr[i1] > jr[i2]:
                            ok = False
                if ok:
                    zrows.append(jr)
    stats = {'centre': z, 'z_joint_rows_reduced': len(zrows), 'nodes': 0, 'zstar_leaves': 0,
             'leaf_kills': {}, 'full_survivors': 0, 'zrow_killed_at_root': 0, 'complete': False}
    examples = []
    for jr in zrows:
        if time.monotonic() > deadline:
            return stats, examples
        A_z = {j: jr[i][0] for i, j in enumerate(U)}
        Q_z = {j: jr[i][1] for i, j in enumerate(U)}
        pairs = [(j, k) for j, k in itertools.combinations(U, 2)]
        adm = {}
        dead = False
        for (j, k) in pairs:
            gjk = G[j][k]
            vals = []
            for a in range(1, gjk):
                for b in range(1, gjk):
                    if a + b > gjk:
                        continue
                    if not tri_ok(profs[z], profs[j], profs[k], A_z[j], A_z[k], a):
                        continue
                    if not tri_ok(profs[z], profs[j], profs[k], Q_z[j], Q_z[k], b):
                        continue
                    vals.append((a, b))
            if not vals:
                dead = True
                break
            adm[(j, k)] = vals
        if dead:
            stats['zrow_killed_at_root'] += 1
            continue
        infoA, infoQ = {}, {}
        for pk, vals in adm.items():
            j, k = pk
            for a, b in vals:
                if (pk, a) not in infoA:
                    infoA[(pk, a)] = pair_info(profs[z], profs[j], profs[k], A_z[j], A_z[k], a)
                if (pk, b) not in infoQ:
                    infoQ[(pk, b)] = pair_info(profs[z], profs[j], profs[k], Q_z[j], Q_z[k], b)
        Fset = [j for j in U if 2 * A_z[j] > G[z][j]]
        SEC = [c for c in SECONDARY if c != z]
        order = sorted(pairs, key=lambda p: (0 if (p[0] in SEC or p[1] in SEC) else 1,
                                             0 if ((p[0] in Fset) != (p[1] in Fset)) else 1, len(adm[p])))

        def relaxed(fixed, info, comp):
            pdat = {}
            for pk in pairs:
                if pk in fixed:
                    pdat[pk] = info[(pk, fixed[pk][comp])]
                else:
                    vs = sorted(set(v[comp] for v in adm[pk]))
                    ds = [info[(pk, x)] for x in vs]
                    pdat[pk] = (min(d[0] for d in ds), max(d[1] for d in ds), all(d[2] for d in ds), all(d[3] for d in ds))
            return pdat

        SECINFO = {}

        def sec_killed(c, fixed):
            # row of c complete?
            rowA = {}; rowQ = {}
            for j in range(7):
                if j == c:
                    continue
                if j == z:
                    rowA[j], rowQ[j] = A_z[c], Q_z[c]
                else:
                    pk = (min(c, j), max(c, j))
                    if pk not in fixed:
                        return False
                    rowA[j], rowQ[j] = fixed[pk]
            Nc = [j for j in range(7) if j != c]
            pdA, pdQ = {}, {}
            for j, k in itertools.combinations(Nc, 2):
                if z in (j, k):
                    o = k if j == z else j
                    cand = [(A_z[o], Q_z[o])]
                else:
                    pk = (j, k)
                    cand = [fixed[pk]] if pk in fixed else adm[pk]
                cand = [v for v in cand
                        if tri_ok(profs[c], profs[j], profs[k], rowA[j], rowA[k], v[0])
                        and tri_ok(profs[c], profs[j], profs[k], rowQ[j], rowQ[k], v[1])]
                if not cand:
                    return True
                dsA = []
                dsQ = []
                for v in cand:
                    keyA = (c, j, k, rowA[j], rowA[k], v[0])
                    if keyA not in SECINFO:
                        SECINFO[keyA] = pair_info(profs[c], profs[j], profs[k], rowA[j], rowA[k], v[0])
                    dsA.append(SECINFO[keyA])
                    keyQ = (c, j, k, rowQ[j], rowQ[k], v[1])
                    if keyQ not in SECINFO:
                        SECINFO[keyQ] = pair_info(profs[c], profs[j], profs[k], rowQ[j], rowQ[k], v[1])
                    dsQ.append(SECINFO[keyQ])
                pdA[(j, k)] = (min(d[0] for d in dsA), max(d[1] for d in dsA), all(d[2] for d in dsA), all(d[3] for d in dsA))
                pdQ[(j, k)] = (min(d[0] for d in dsQ), max(d[1] for d in dsQ), all(d[2] for d in dsQ), all(d[3] for d in dsQ))
            if rplp_kills_pd(c, profs, rowA, rowQ, pdA):
                return True
            return rplp_kills_pd(c, profs, rowQ, rowA, pdQ)

        def killed(fixed):
            rowA = {j: A_z[j] for j in U}; rowQ = {j: Q_z[j] for j in U}
            if rplp_kills_pd(z, profs, rowA, rowQ, relaxed(fixed, infoA, 0)):
                return True
            if rplp_kills_pd(z, profs, rowQ, rowA, relaxed(fixed, infoQ, 1)):
                return True
            for c in SEC:
                if sec_killed(c, fixed):
                    stats['secondary_kills'] = stats.get('secondary_kills', 0) + 1
                    return True
            return False

        dom0 = {}
        for u in U:
            dom0[u] = [r for r in VD[u] if r[z] == (A_z[u], Q_z[u])]
            if not dom0[u]:
                dead = True
        if dead:
            stats['zrow_killed_by_domains'] = stats.get('zrow_killed_by_domains', 0) + 1
            continue
        DOM = [dom0]

        def rec(depth, fixed):
            if time.monotonic() > deadline:
                raise TimeoutError()
            stats['nodes'] += 1
            if killed(fixed):
                return
            if depth == len(order):
                stats['zstar_leaves'] += 1
                AL = [[0] * 7 for _ in range(7)]
                AS = [[0] * 7 for _ in range(7)]
                for j in U:
                    AL[z][j] = AL[j][z] = A_z[j]
                    AS[z][j] = AS[j][z] = Q_z[j]
                for (j, k), (a, b) in fixed.items():
                    AL[j][k] = AL[k][j] = a
                    AS[j][k] = AS[k][j] = b
                why = full_leaf_dead(profs, G, AL, AS)
                if why is None:
                    stats['full_survivors'] += 1
                    if len(examples) < 5:
                        examples.append({'alpha': AL, 'alpha_star': AS})
                else:
                    stats['leaf_kills'][why] = stats['leaf_kills'].get(why, 0) + 1
                if stats['zstar_leaves'] >= leaf_cap:
                    raise TimeoutError()
                return
            pk = order[depth]
            j, k = pk
            cur = DOM[-1]
            for v in adm[pk]:
                nj = [r for r in cur[j] if r[k] == v]
                if not nj:
                    continue
                nk = [r for r in cur[k] if r[j] == v]
                if not nk:
                    continue
                # T/Ppair on triangles {j, k, l} (l != z) whose other two pairs are decided
                okt = True
                for l in U:
                    if l in (j, k):
                        continue
                    p1 = (min(j, l), max(j, l)); p2 = (min(k, l), max(k, l))
                    if p1 in fixed and p2 in fixed:
                        a1 = fixed[p1]; a2 = fixed[p2]
                        if not (tri_ok(profs[j], profs[k], profs[l], v[0], a1[0], a2[0]) and
                                tri_ok(profs[j], profs[k], profs[l], v[1], a1[1], a2[1])):
                            okt = False
                            break
                if not okt:
                    continue
                nd = dict(cur)
                nd[j] = nj
                nd[k] = nk
                DOM.append(nd)
                fixed[pk] = v
                rec(depth + 1, fixed)
                del fixed[pk]
                DOM.pop()
        try:
            rec(0, {})
        except TimeoutError:
            return stats, examples
    stats['complete'] = True
    return stats, examples


def main():
    outp = sys.argv[1]
    cls = sys.argv[2]
    sel = json.loads(sys.argv[3])
    centres = json.loads(sys.argv[4])
    per_centre = float(sys.argv[5])
    leaf_cap = int(sys.argv[6])
    SECONDARY[:] = json.loads(sys.argv[7])
    gens = {'K7': k7_profiles, 'K63': k63_profiles, 'K62': k62_profiles}
    jobs = []
    for profs in gens[cls]():
        G = gmatrix(profs)
        if check_class(cls, G):
            jobs.append((profs, G))
    fh = open(outp, 'x')
    out = {'probe': 'two_centre_rplp_probe_v13', 'class': cls, 'items': []}
    status = 'COMPLETE'
    for ix in sel:
        if time.monotonic() - T0 > BUDGET:
            status = 'INCOMPLETE'
            out['items'].append({'index': ix, 'evaluated': False})
            continue
        profs, G = jobs[ix]
        item = {'index': ix, 'profiles': [list(p) for p in profs], 'attempts': []}
        for z in centres:
            dl = min(time.monotonic() + per_centre, T0 + BUDGET)
            try:
                stats, ex = centre_search(profs, G, z, dl, leaf_cap)
            except Budget:
                stats, ex = {'centre': z, 'note': 'budget'}, []
            stats['examples'] = ex
            item['attempts'].append(stats)
            if stats.get('complete') and stats.get('full_survivors') == 0:
                item['closed_by_centre'] = z
                break
        item['evaluated'] = True
        out['items'].append(item)
    out['status'] = status
    out['seconds'] = round(time.monotonic() - T0, 3)
    json.dump(out, fh, indent=0, default=str)
    fh.write('\n')
    fh.flush()
    os.fsync(fh.fileno())
    fh.close()
    print(json.dumps({'status': status, 'seconds': out['seconds'], 'items': [{'index': it['index'], 'closed_by': it.get('closed_by_centre'), 'attempts': [{k: a.get(k) for k in ('centre', 'z_joint_rows_reduced', 'nodes', 'zstar_leaves', 'full_survivors', 'complete', 'leaf_kills')} for a in it.get('attempts', [])]} for it in out['items']]}))


if __name__ == '__main__':
    main()
