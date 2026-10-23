#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v5: joint (alpha, alpha*) search with forward checking, adding T and Ppair (rules-k7-v1 L1, L4 with K2;
accepted) on every triangle, separately for alpha and for alpha*.

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
CAP = 200


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

    def rec(assigned, doms):
        chk()
        nodes[0] += 1
        un = [w for w in range(7) if w not in assigned]
        if not un:
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


def main():
    outp = sys.argv[1]
    classes = sys.argv[2].split(',')
    fh = open(outp, 'x')
    out = {'probe': 'lfc_inv_tri_joint_probe_v5', 'python': sys.version, 'classes': classes, 'items': []}
    status = 'COMPLETE'
    gens = {'K7': k7_profiles, 'K63': k63_profiles, 'K62': k62_profiles}
    jobs = []
    for cls in classes:
        for profs in gens[cls]():
            G = gmatrix(profs)
            if check_class(cls, G):
                jobs.append((cls, profs, G))
    for cls, profs, G in jobs:
        item = {'class': cls, 'profiles': [list(p) for p in profs]}
        if status != 'COMPLETE':
            item['evaluated'] = False
            out['items'].append(item)
            continue
        try:
            doms = domains(profs, G)
            item['joint_rows_per_vertex'] = [len(d) for d in doms]
            sols, capped, nodes = search(doms, profs)
            item['joint_solutions_first_vertex_symmetry_reduced'] = len(sols)
            item['capped'] = capped
            item['nodes'] = nodes
            item['examples'] = [[[list(x) if x else None for x in s[w]] for w in range(7)] for s in sols[:3]]
            item['evaluated'] = True
        except Budget:
            status = 'INCOMPLETE'
            item['evaluated'] = False
            item['note'] = 'self budget exhausted inside this item'
        out['items'].append(item)
    out['status'] = status
    out['seconds'] = round(time.monotonic() - T0, 3)
    json.dump(out, fh, indent=0)
    fh.write('\n')
    fh.flush()
    os.fsync(fh.fileno())
    fh.close()
    ev = [it for it in out['items'] if it.get('evaluated')]
    summ = {}
    for it in ev:
        k = it['class']
        summ.setdefault(k, [0, 0])
        summ[k][0] += 1
        summ[k][1] += 1 if it['joint_solutions_first_vertex_symmetry_reduced'] > 0 else 0
    print(json.dumps({'status': status, 'items': len(out['items']), 'evaluated': len(ev),
                      'per_class_evaluated_and_with_solutions': summ, 'seconds': out['seconds']}))


if __name__ == '__main__':
    main()
