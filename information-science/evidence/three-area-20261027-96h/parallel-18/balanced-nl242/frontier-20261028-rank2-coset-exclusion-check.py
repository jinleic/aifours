#!/opt/homebrew/bin/python3
"""Finite inputs and solver cross-checks for the rank-two coset exclusion.

The written proof is in frontier-20261028-rank2-coset-exclusion-v1.md.  This
script (i) enumerates the 81 local four-point ternary types, (ii) recomputes
the e=2 family and e=4 Walsh histograms exactly, (iii) checks the affine-flat
intersection lemma in F2^5, and (iv) records Z3 cross-checks.  Solver UNSAT is a
cross-check only, not the proof.
"""
import argparse
import collections
import itertools
import json
import pathlib
import z3


def par(x):
    return bin(x).count('1') & 1


def local_walsh(u):
    return tuple(sum(u[z] * (-1 if par(a & z) else 1) for z in range(4)) for a in range(4))


def fw6(v):
    a = list(v); s = 1
    while s < 64:
        for i in range(0, 64, 2 * s):
            for j in range(i, i + s):
                x, y = a[j], a[j + s]; a[j] = x + y; a[j + s] = x - y
        s *= 2
    return a


def even_codes(e):
    words = [w for w in range(1, 1 << e) if par(w) == 0 and bin(w).count('1') >= 4]
    seen = {frozenset([0])}; frontier = [frozenset([0])]
    while frontier:
        nxt = []
        for sp in frontier:
            for w in words:
                if w in sp: continue
                new = frozenset(sp | {x ^ w for x in sp})
                if min(bin(x).count('1') for x in new if x) < 4: continue
                if new not in seen: seen.add(new); nxt.append(new)
        frontier = nxt
    return [sp for sp in seen if len(sp).bit_length() - 1 >= max(0, e - 7)]


def histograms(e):
    out = set()
    for sp in even_codes(e):
        dual = [y for y in range(1 << e) if all(par(x & y) == 0 for x in sp)]
        for eps in range(1 << e):
            cnt = collections.Counter()
            for b in dual:
                cnt[abs(sum((-1 if (eps >> i) & 1 else 1) * (-1 if (b >> i) & 1 else 1) for i in range(e)))] += 1
            assert all(64 * cnt[k] % len(dual) == 0 for k in range(e + 1))
            out.add(tuple(64 * cnt[k] // len(dual) for k in range(e + 1)))
    return out


def main():
    p = argparse.ArgumentParser(); p.add_argument('--output', type=pathlib.Path, required=True); a = p.parse_args()
    if a.output.exists(): raise FileExistsError(a.output)
    types = [(u, local_walsh(u), sum(abs(x) for x in u)) for u in itertools.product((-1, 0, 1), repeat=4)]
    assert len(types) == 81
    # Parseval on each coset and the class table.
    for u, U, n in types:
        assert sum(x * x for x in U) == 4 * n and all((x - n) % 2 == 0 for x in U)
    classes = collections.Counter()
    for u, U, n in types:
        classes[(n, tuple(abs(x) for x in U))] += 1
    table = {f'n{n}:{"/".join(map(str, U))}': c for (n, U), c in sorted(classes.items())}
    assert sum(classes.values()) == 81
    # n=3 types: exactly one |U|=3 and U0*U1*U2*U3 = -3.
    for u, U, n in types:
        if n == 3:
            assert sorted(map(abs, U)) == [1, 1, 1, 3] and U[0] * U[1] * U[2] * U[3] == -3
    # e=2 family: allowed (|U|,t,W) rows and all nonnegative integer solutions.
    rows = {0: (0, 0), 1: (-2, 4), 2: (2, 12), 3: (0, 16), 4: (-2, 20)}
    fam = []
    for n1 in range(65):
        for n2 in range(65 - n1):
            for n3 in range(65 - n1 - n2):
                for n4 in range(65 - n1 - n2 - n3):
                    n0 = 64 - n1 - n2 - n3 - n4
                    N = [n0, n1, n2, n3, n4]
                    if sum(N[k] * k * k for k in range(5)) != 140: continue
                    if sum(N[k] * rows[k][0] ** 2 for k in range(5)) != 128: continue
                    if sum(N[k] * rows[k][1] ** 2 for k in range(5)) != 4096: continue
                    if sum(N[k] * rows[k][0] * rows[k][1] for k in range(5)) != 128: continue
                    fam.append(N)
    assert sorted(fam) == sorted([24 + 2 * k, 20 - 2 * k, 12 + k, 8 - 2 * k, k] for k in range(5))
    # Per-|U| unique t for e=2 from t == U (mod 3), t in {-2,0,2}.
    for U in range(-4, 5):
        opts = [t for t in (-2, 0, 2) if (U - t) % 3 == 0]
        assert len(opts) == 1 and (16 * U + 2 * opts[0]) % 3 == 0
    hist4 = histograms(4); hist2 = histograms(2)
    assert hist2 == {(32, 0, 32)} and hist4 == {(0, 0, 64, 0, 0), (24, 0, 32, 0, 8), (48, 0, 0, 0, 16)}
    # Affine 3-flats in F2^5 intersect in 0,2,4,8 points.
    subs = set()
    for comb in itertools.combinations(range(1, 32), 3):
        S = {0}
        for v in comb: S |= {x ^ v for x in S}
        if len(S) == 8: subs.add(frozenset(S))
    flats = {frozenset(x ^ t for x in S) for S in subs for t in range(32)}
    assert len(subs) == 155 and len(flats) == 620
    masks = [sum(1 << x for x in F) for F in flats]
    inter = collections.Counter(bin(x & y).count('1') for x in masks for y in masks)
    assert set(inter) == {0, 2, 4, 8}
    # Geometry of a general-position four-point tau: zero set = hyperplane minus 3-flat.
    rng = __import__('random').Random(20261029)
    checked = 0
    while checked < 400:
        pts = rng.sample(range(64), 4)
        if pts[0] ^ pts[1] ^ pts[2] ^ pts[3] == 0: continue
        eps = [rng.choice((-1, 1)) for _ in pts]; d = [0] * 64
        for x, e in zip(pts, eps): d[x] = e
        F = fw6(d); zero = {c for c in range(64) if F[c] == 0}; four = {c for c in range(64) if abs(F[c]) == 4}
        two = {c for c in range(64) if abs(F[c]) == 2}
        rho = pts[0] ^ pts[1] ^ pts[2] ^ pts[3]; sign = eps[0] * eps[1] * eps[2] * eps[3]
        hyp = {c for c in range(64) if (-1 if par(rho & c) else 1) == sign}
        assert zero | four == hyp and two == set(range(64)) - hyp and len(four) == 8
        base = min(four); assert len({x ^ base for x in four}) == 8
        spanv = {0}
        for v in four: 
            w = v ^ base
            if w not in spanv: spanv |= {x ^ w for x in spanv}
        assert len(spanv) == 8
        checked += 1
    # Z3 cross-checks of the class-count reductions, with and without geometry.
    def refined(m, Z, es, timeout=20000, transversal=False, region=None):
        s = z3.Solver(); s.set(timeout=timeout); regvars = collections.defaultdict(list)
        N = [z3.Int(f'N{i}') for i in range(81)]; s.add(*[x >= 0 for x in N])
        s.add(z3.Sum(N) == 64, z3.Sum([N[i] * types[i][2] for i in range(81)]) == m,
              z3.Sum([N[i] * types[i][1][0] for i in range(81)]) == 0,
              z3.Sum([N[i] * types[i][1][0] ** 2 for i in range(81)]) == 64 - Z)
        TH = {2: hist2, 4: hist4}
        for j in (1, 2, 3):
            e = es[j - 1]; s.add(z3.Sum([N[i] * types[i][1][j] ** 2 for i in range(81)]) == 144 - 2 * e)
            if e == 0:
                for i in range(81):
                    if types[i][1][j] % 3: s.add(N[i] == 0)
                continue
            W2 = []; Wt = []; H = {k: [] for k in range(e + 1)}
            for i in range(81):
                U = types[i][1][j]; vs = []
                for t in range(-e, e + 1, 2):
                    if (U - t) % 3: continue
                    x = z3.Int(f'X{j}_{i}_{t}'); s.add(x >= 0); vs.append(x); W = (16 * U + 2 * t) // 3
                    W2.append(x * W * W); Wt.append(x * W * t); H[abs(t)].append(x)
                    if region is not None and j == 3:
                        key = (int(types[i][1][1] % 3 == 0), int(types[i][1][2] % 3 == 0), 0 if t == 0 else (1 if abs(t) == 4 else 2))
                        regvars[key].append(x)
                s.add(z3.Sum(vs) == N[i]) if vs else s.add(N[i] == 0)
            s.add(z3.Sum(W2) == 4096, z3.Sum(Wt) == 64 * e)
            s.add(z3.Or(*[z3.And(*[(z3.Sum(H[k]) if H[k] else z3.IntVal(0)) == h[k] for k in range(e + 1)]) for h in TH[e]]))
        if transversal:
            for h1 in (0, 1):
                for h2 in (0, 1):
                    s.add(z3.Sum([N[i] for i in range(81) if int(types[i][1][1] % 3 == 0) == h1 and int(types[i][1][2] % 3 == 0) == h2]) == 16)
        if region is not None:
            for key, val in region.items():
                s.add((z3.Sum(regvars[key]) if regvars[key] else z3.IntVal(0)) == val)
        return str(s.check())
    cross = {}
    for D, m, Z in ((12, 118, 8), (12, 118, 12), (12, 118, 16), (12, 118, 20), (12, 118, 24), (16, 120, 8), (16, 120, 12), (16, 120, 16), (20, 122, 8)):
        E2 = (7936 - 16 * Z - 64 * m) // 32
        for es in sorted({tuple(sorted(t)) for t in itertools.product(range(E2 + 1), repeat=3) if sum(t) == E2 and all(x % 2 == 0 for x in t) and max(t) <= 4}):
            for perm in sorted(set(itertools.permutations(es))):
                cross[f'D{D}/m{m}/Z{Z}/e{perm}'] = refined(m, Z, perm)
    cross['D12/m118/Z8/e(2,2,4)/transversal'] = refined(118, 8, (2, 2, 4), transversal=True)
    # All 29 region vectors of (Hyp1,Hyp2 transversal; Hyp3 and 3-flat F3 in Hyp3).
    H1 = {c for c in range(64) if not c & 1}; H2 = {c for c in range(64) if not c & 2}
    regions = collections.Counter()
    for rho in range(1, 64):
        for b in (0, 1):
            H3 = {c for c in range(64) if par(rho & c) == b}; base = min(H3); dirs = sorted({c ^ base for c in H3} - {0})
            sp3 = set()
            for comb in itertools.combinations(dirs, 3):
                S = {0}
                for v in comb: S |= {x ^ v for x in S}
                if len(S) == 8: sp3.add(frozenset(S))
            for S in sp3:
                for t0 in H3:
                    F3 = frozenset(t0 ^ v for v in S); Z3s = H3 - F3; vec = {}
                    for h1 in (1, 0):
                        for h2 in (1, 0):
                            Q = {c for c in range(64) if (c in H1) == bool(h1) and (c in H2) == bool(h2)}
                            vec[(h1, h2, 0)] = len(Q & Z3s); vec[(h1, h2, 1)] = len(Q & F3); vec[(h1, h2, 2)] = len(Q - H3)
                    regions[tuple(sorted(vec.items()))] += 1
    region_status = collections.Counter(refined(118, 8, (2, 2, 4), transversal=True, region=dict(r)) for r in regions)
    assert len(regions) == 29
    cross['D12/m118/Z8/e(2,2,4)/all29regions'] = dict(region_status)
    out = {'scope': 'finite lemma inputs and Z3 cross-checks; not a Boolean witness or solver-only proof',
           'local_type_classes': table, 'e2_family': fam, 'e2_histogram': sorted(hist2), 'e4_histograms': sorted(hist4),
           'affine_3flat_intersections_F2_5': sorted(inter), 'random_general_position_checks': checked,
           'z3_class_count_crosschecks': cross}
    with a.output.open('x', encoding='utf-8') as dst: json.dump(out, dst, indent=2, sort_keys=True); dst.write('\n')
    print('types, e2 family, e4 histograms, flat lemma and', len(cross), 'cross-checks recorded')


if __name__ == '__main__':
    main()
