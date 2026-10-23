#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v2: full 7-vertex alpha-patterns passing LFC at every vertex,
and pairs (alpha, alpha*) of such patterns with alpha + alpha* <= g entrywise (Lemma INV).

EXPLORATORY ONLY; never a premise.  Python standard library only; self wall budget 270 s checked inside the
search loops; on overrun the current item is reported INCOMPLETE and the rest NOT_EVALUATED.
Writes one output file (exclusive create) given by argv[1].  Uses ONLY Lemma LFC (row values, as in
lfc_row_probe_v1) and Lemma INV (pairing); no T, Ppair, K, RPLP, TWIN, Q or BLOCK rule is applied.
"""
import itertools, json, math, os, sys, time
from fractions import Fraction as F

T0 = time.monotonic()
BUDGET = 270.0


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
    n = len(profs)
    return [[gn(profs[i], profs[j]) if i != j else 0 for j in range(n)] for i in range(n)]


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


def vertex_tables(profs, G):
    """For each v: dict key (alpha_vj for j<v) -> list of (alpha_vj for j>v) with LFC value < 1."""
    tabs = []
    nsurv = []
    for vv in range(7):
        nb = [j for j in range(7) if j != vv]
        nbrs = [(G[vv][j], profs[j]) for j in nb]
        ranges = [range(1, G[vv][j]) for j in nb]
        tab = {}
        cnt = 0
        for al in itertools.product(*ranges):
            chk()
            if row_val(nbrs, al) < 1:
                cnt += 1
                lo = tuple(a for j, a in zip(nb, al) if j < vv)
                hi = tuple(a for j, a in zip(nb, al) if j > vv)
                tab.setdefault(lo, []).append(hi)
        tabs.append(tab)
        nsurv.append(cnt)
    return tabs, nsurv


EDGES = [(i, j) for i in range(7) for j in range(i + 1, 7)]
EIDX = {e: k for k, e in enumerate(EDGES)}


def patterns(tabs, limit):
    out = []
    A = [[0] * 7 for _ in range(7)]

    def rec(vv):
        chk()
        if vv == 7:
            out.append(tuple(A[i][j] for i, j in EDGES))
            if len(out) > limit:
                raise OverflowError()
            return
        lo = tuple(A[vv][j] for j in range(vv))
        for hi in tabs[vv].get(lo, ()):
            for j, a in zip(range(vv + 1, 7), hi):
                A[vv][j] = a
                A[j][vv] = a
            rec(vv + 1)
        for j in range(vv + 1, 7):
            A[vv][j] = 0
            A[j][vv] = 0
    rec(0)
    return out


def pairs(pats, G):
    gv = [G[i][j] for i, j in EDGES]
    # index patterns by first few coordinates for pruning
    res = []
    S = pats
    for P in S:
        chk()
        cap = [g - a for g, a in zip(gv, P)]
        for Q in S:
            ok = True
            for q, c in zip(Q, cap):
                if q > c:
                    ok = False
                    break
            if ok:
                res.append((P, Q))
                break
    return res


def main():
    fh = open(sys.argv[1], 'x')
    out = {'probe': 'lfc_inv_pattern_probe_v2', 'python': sys.version, 'items': []}
    status = 'COMPLETE'
    jobs = []
    for cls, gen in (('K7', k7_profiles), ('K63', k63_profiles), ('K62', k62_profiles)):
        for profs in gen():
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
            tabs, ns = vertex_tables(profs, G)
            item['row_survivors_per_vertex'] = ns
            try:
                pats = patterns(tabs, 2000000)
                item['lfc_patterns'] = len(pats)
                pr = pairs(pats, G)
                item['patterns_with_inv_partner'] = len(pr)
                item['examples'] = [[list(P), list(Q)] for P, Q in pr[:5]]
                item['evaluated'] = True
            except OverflowError:
                item['evaluated'] = False
                item['note'] = 'more than 2,000,000 LFC patterns; pairing skipped'
        except Budget:
            status = 'INCOMPLETE'
            item['evaluated'] = False
            item['note'] = 'self budget exhausted inside this item'
        out['items'].append(item)
    out['status'] = status
    out['edges'] = EDGES
    out['seconds'] = round(time.monotonic() - T0, 3)
    out['lp_cache'] = len(LP_CACHE)
    json.dump(out, fh, indent=0)
    fh.write('\n')
    fh.flush()
    os.fsync(fh.fileno())
    fh.close()
    ev = [it for it in out['items'] if it.get('evaluated')]
    print(json.dumps({'status': status, 'items': len(out['items']), 'evaluated': len(ev),
                      'with_pairs': sum(1 for it in ev if it['patterns_with_inv_partner'] > 0),
                      'seconds': out['seconds']}))


if __name__ == '__main__':
    main()
