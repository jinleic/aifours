#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v3: joint search over pairs (alpha, alpha*) of 7-vertex patterns.

EXPLORATORY ONLY; never a premise.  Python standard library only; self wall budget 270 s.
Writes one output file (exclusive create) given by argv[1].
Rules used: Lemma LFC (row value < 1 at every vertex, for alpha AND for alpha*) and Lemma INV
(alpha_ij + alpha*_ij <= g_ij on every edge; alpha* has the same labelled profiles).  Nothing else
(no T, Ppair, K, RPLP, TWIN, Q, BLOCK).  For every class/profile tuple the probe counts joint solutions
(capped) and records up to 3 examples.
"""
import itertools, json, math, os, sys, time
from fractions import Fraction as F

T0 = time.monotonic()
BUDGET = 270.0
CAP = 1000


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


SCEN_CACHE = {}


def survivors(nbrs):
    """All alpha-sequences (in the given neighbour order) with LFC value < 1."""
    key = tuple(nbrs)
    if key in SCEN_CACHE:
        return SCEN_CACHE[key]
    res = []
    for al in itertools.product(*[range(1, g) for g, p in nbrs]):
        chk()
        if row_val(nbrs, al) < 1:
            res.append(al)
    SCEN_CACHE[key] = res
    return res


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


def joint_tables(profs, G):
    tabs = []
    counts = []
    for vv in range(7):
        nb = [j for j in range(7) if j != vv]
        nbrs = [(G[vv][j], profs[j]) for j in nb]
        S = survivors(nbrs)
        gs = [G[vv][j] for j in nb]
        tab = {}
        cnt = 0
        for s in S:
            for t in S:
                chk()
                if all(a + b <= g for a, b, g in zip(s, t, gs)):
                    cnt += 1
                    lo = tuple((a, b) for j, a, b in zip(nb, s, t) if j < vv)
                    hi = tuple((a, b) for j, a, b in zip(nb, s, t) if j > vv)
                    tab.setdefault(lo, []).append(hi)
        tabs.append(tab)
        counts.append((len(S), cnt))
    return tabs, counts


def search(tabs, cap):
    sols = []
    A = [[None] * 7 for _ in range(7)]
    nodes = [0]

    def rec(vv):
        chk()
        nodes[0] += 1
        if vv == 7:
            sols.append([[A[i][j] for j in range(7)] for i in range(7)])
            if len(sols) >= cap:
                raise OverflowError()
            return
        lo = tuple(A[vv][j] for j in range(vv))
        for hi in tabs[vv].get(lo, ()):
            for j, ab in zip(range(vv + 1, 7), hi):
                A[vv][j] = ab
                A[j][vv] = ab
            rec(vv + 1)
        for j in range(vv + 1, 7):
            A[vv][j] = None
            A[j][vv] = None
    capped = False
    try:
        rec(0)
    except OverflowError:
        capped = True
    return sols, capped, nodes[0]


def main():
    fh = open(sys.argv[1], 'x')
    out = {'probe': 'lfc_inv_joint_probe_v3', 'python': sys.version, 'items': []}
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
            tabs, counts = joint_tables(profs, G)
            item['alpha_survivors_and_joint_rows_per_vertex'] = counts
            sols, capped, nodes = search(tabs, CAP)
            item['joint_solutions'] = len(sols)
            item['capped'] = capped
            item['nodes'] = nodes
            item['examples'] = sols[:3]
            item['evaluated'] = True
        except Budget:
            status = 'INCOMPLETE'
            item['evaluated'] = False
            item['note'] = 'self budget exhausted inside this item'
        out['items'].append(item)
    out['status'] = status
    out['seconds'] = round(time.monotonic() - T0, 3)
    out['lp_cache'] = len(LP_CACHE)
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
        summ[k][1] += 1 if it['joint_solutions'] > 0 else 0
    print(json.dumps({'status': status, 'items': len(out['items']), 'evaluated': len(ev),
                      'per_class_evaluated_and_with_solutions': summ, 'seconds': out['seconds']}))


if __name__ == '__main__':
    main()
