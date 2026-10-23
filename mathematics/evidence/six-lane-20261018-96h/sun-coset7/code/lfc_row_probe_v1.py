#!/usr/bin/env python3
"""sun-coset7 (96h lane) EXPLORATORY probe v1: exact LFC LP values of neighbour alpha-rows.

EXPLORATORY ONLY: never a premise of any claim.  Python standard library only.  Self wall budget 270 s,
checked between rows; on overrun the remaining scenarios are reported NOT_EVALUATED (status INCOMPLETE).
Writes exactly one output file (exclusive create) given by argv[1].

Definitions (K7-LFC-INV-v1.md, Lemma LFC (d)).  For a vertex v with neighbours j (g_vj, capped {2,3,5}
valuation triple (e_j, f_j, h_j) of n_j) and an alpha-row (alpha_vj in 1..g_vj-1):
  lab_j = {2,3,5}-part of n_j * alpha_vj / g_vj   (prime-to-30 parts are pairwise coprime: README P0(b));
  T allowed iff every T' subset T with |T'| >= 2 contains j != j' with gcd(lab_j, lab_j') >= |T'|;
  VAL = max sum_j y_j * alpha_vj / g_vj over y >= 0 with sum_{j in T} y_j <= 1 for every allowed T.
LFC kills the row iff VAL >= 1 (LFC gives VAL <= 1 - 1/n_v < 1 for actual configurations).
Capped profiles follow rules-k7-v1 section 4 (e <= 4, f <= 2, h <= 2).
"""
import itertools, json, math, os, sys, time
from fractions import Fraction as F

T0 = time.monotonic()
BUDGET = 270.0
CAPS = (4, 2, 2)


def lab(prof, alpha, g):
    e, f, h = prof
    a2 = e + v(2, alpha) - v(2, g)
    a3 = f + v(3, alpha) - v(3, g)
    a5 = h + v(5, alpha) - v(5, g)
    assert a2 >= 0 and a3 >= 0 and a5 >= 0
    return (2 ** a2) * (3 ** a3) * (5 ** a5)


def v(p, n):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c


def gn(p, q):
    """{2,3,5}-part of gcd(n_p, n_q) from capped profiles (pairwise minima are exact under CAP)."""
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
    """max c.y s.t. sum_{j in r} y_j <= 1 (r in rows), y >= 0; exact simplex, Bland's rule."""
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
        if best is None:
            raise RuntimeError('unbounded LP (impossible: singletons are constraints)')
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
    if key in LP_CACHE:
        return LP_CACHE[key]
    labels = [x[0] for x in items]
    c = [x[1] for x in items]
    val = lp_max(c, maximal_allowed(labels))
    LP_CACHE[key] = val
    return val


def scenarios_for(cls, profs):
    """Yield (v, sorted neighbour list) for every vertex; verify the class gcd matrix."""
    out = []
    n = len(profs)
    for vv in range(n):
        nb = []
        for j in range(n):
            if j == vv:
                continue
            g = gn(profs[vv], profs[j])
            nb.append((g, profs[j]))
        out.append((vv, tuple(sorted(nb))))
    return out


def k7_profiles():
    res = []
    for e2 in (None, 2, 3, 4):
        for f3 in (None, 2):
            for h5 in (None, 1, 2):
                # canonical placements: 2-marker on vertex 0; 3-marker on 0 or 1; 5-marker on 0, 1 or 2
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


def check_class(cls, profs):
    n = len(profs)
    for i in range(n):
        for j in range(i + 1, n):
            g = gn(profs[i], profs[j])
            if cls == 'K7':
                want = 6
            elif cls == 'K63':
                want = 3 if 6 in (i, j) else 6
            elif cls == 'K62':
                if 6 in (i, j):
                    want = 4 if 0 in (i, j) else 2
                else:
                    want = 6
            if g != want:
                return False
    return True


def main():
    outp = sys.argv[1]
    fh = open(outp, 'x')
    result = {'probe': 'lfc_row_probe_v1', 'status': None, 'classes': {}, 'python': sys.version}
    scen = {}
    for cls, gen in (('K7', k7_profiles), ('K63', k63_profiles), ('K62', k62_profiles)):
        profs_list = [p for p in gen() if check_class(cls, p)]
        result['classes'][cls] = {'profile_tuples': len(profs_list)}
        for profs in profs_list:
            for vv, nb in scenarios_for(cls, profs):
                key = (cls, nb)
                scen.setdefault(key, []).append((profs, vv))
    keys = sorted(scen, key=lambda k: (k[0], len([1 for g, p in k[1] if p != (1, 1, 0)]), str(k[1])))
    out_s = []
    status = 'COMPLETE'
    for (cls, nb) in keys:
        if time.monotonic() - T0 > BUDGET:
            status = 'INCOMPLETE'
            out_s.append({'class': cls, 'neighbours': nb, 'evaluated': False})
            continue
        groups = {}
        for idx, x in enumerate(nb):
            groups.setdefault(x, []).append(idx)
        gkeys = sorted(groups)
        choices = []
        for gk in gkeys:
            gval = gk[0]
            k = len(groups[gk])
            choices.append(list(itertools.combinations_with_replacement(range(1, gval), k)))
        surv = []
        total = 0
        for combo in itertools.product(*choices):
            nbl, al = [], []
            for gk, ms in zip(gkeys, combo):
                for a in ms:
                    nbl.append(gk)
                    al.append(a)
            total += 1
            val = row_val(nbl, al)
            if val < 1:
                surv.append({'row': [[gk[0], list(gk[1]), a] for gk, a in zip(nbl, al)], 'val': str(val)})
        out_s.append({'class': cls, 'neighbours': [[g, list(p)] for g, p in nb], 'evaluated': True,
                      'rows': total, 'survivors': len(surv), 'survivor_rows': surv,
                      'occurs_at': [[[list(x) for x in profs], vv] for profs, vv in scen[(cls, nb)][:3]],
                      'occurrences': len(scen[(cls, nb)])})
    result['status'] = status
    result['scenarios'] = out_s
    result['lp_cache'] = len(LP_CACHE)
    result['seconds'] = round(time.monotonic() - T0, 3)
    json.dump(result, fh, indent=0)
    fh.write('\n')
    fh.flush()
    os.fsync(fh.fileno())
    fh.close()
    print(json.dumps({'status': status, 'scenarios': len(out_s), 'seconds': result['seconds'],
                      'lp_cache': len(LP_CACHE)}))


if __name__ == '__main__':
    main()
