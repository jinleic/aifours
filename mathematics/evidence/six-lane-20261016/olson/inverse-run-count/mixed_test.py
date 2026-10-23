#!/usr/bin/env python3
"""Aid only: structure of kills for MIXED alphabets (B >= 1).  Random inherited data with
k >= p+1, A >= B >= 1, B <= kappa, no full window; interval-feasible phi (hwsingle) + random phi.
Chain lifts from start 0 (Lemma TL); defects Z = {bh <= 0}.  Reports which certificate kills:
prefix / Z / greedy (depth-ascending defects, stop at first killed prefix of the order) /
Z+fillers (Z plus up to 3 runs with bh = 1) / other subset / none.
Usage: mixed_test.py p trials seed allodd(0/1)
"""
import random, sys
from collections import Counter
from itertools import combinations
from scl_closure import tables
from sample_famtest import inherited
from chainlift_test import run as hws


def killed(U, L, P, X):
    return -L[P] <= X <= U[P]


def main():
    p, T, seed, allodd = map(int, sys.argv[1:5])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); ex = []
    done = 0
    while done < T:
        k = rng.randint(p + 1, 2 * p - 3)
        R = rng.randint(k, 3 * p - 2); F = N - R
        if F < k:
            continue
        if allodd and (F - k) % 2:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        if allodd:
            l = [1] * k
            for _ in range((F - k) // 2):
                l[rng.randrange(k)] += 2
        else:
            cl = sorted(rng.sample(range(1, F), k - 1)); l = [y - x for x, y in zip([0] + cl, cl + [F])]
        # random split with some rho_-1
        frac = rng.random() * 0.6
        b = [sum(1 for _ in range(x) if rng.random() < frac) for x in r]
        a = [x - y for x, y in zip(r, b)]
        A, B = sum(a), sum(b)
        if A < B:
            a, b = b, a; A, B = B, A
        if B < 1 or A >= 2 * p:
            continue
        H = sum(x // 2 for x in l); kappa = p - 1 - H
        if B > kappa or not inherited(a, b, l, p):
            continue
        U, L = tables(a, b, l, p)
        full = (1 << k) - 1
        if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
            continue
        done += 1
        d = [x - y for x, y in zip(a, b)]
        sols = hws(p, 1, a, b, l, 300, 300)
        rnd = []
        for _ in range(60):
            ph = [rng.randrange(p) for _ in range(k - 1)]; ph.append((-sum(ph)) % p); rnd.append(ph)
        for phi in sols + rnd:
            prev = 0; x = [0] * k; res = None
            for j in range(1, k + 1):
                P = (1 << j) - 1; s = sum(phi[:j]) % p
                if j == k:
                    cand = p
                else:
                    lo, hi = -L[P], U[P]
                    if lo <= hi and (s - lo) % p <= hi - lo:
                        res = 'prefix'; break
                    cand = hi + 1 + ((s - (hi + 1)) % p)
                x[j - 1] = cand - prev; prev = cand
            if res:
                st[res] += 1; continue
            bh = [2 * x[t] - d[t] for t in range(k)]
            Z = [t for t in range(k) if bh[t] <= 0]
            def X(P):
                return sum(x[u] for u in range(k) if (P >> u) & 1)
            Zm = sum(1 << t for t in Z)
            if not Z:
                st['noZ'] += 1; continue
            if Zm != full and killed(U, L, Zm, X(Zm)):
                st['Z'] += 1; continue
            order = sorted(Z, key=lambda t: -bh[t]); Pm = 0; g = False
            for t in order:
                Pm |= 1 << t
                if Pm != full and killed(U, L, Pm, X(Pm)):
                    g = True; break
            if g:
                st['greedy'] += 1; continue
            fill = [t for t in range(k) if bh[t] == 1]
            got = None
            for s in range(1, 4):
                for S in combinations(fill, s):
                    for base in [Zm] + [sum(1 << t for t in order[:i]) for i in range(1, len(order))]:
                        P = base | sum(1 << t for t in S)
                        if P != full and killed(U, L, P, X(P)):
                            got = s; break
                    if got: break
                if got: break
            if got:
                st['Z+fill%d' % got] += 1
                if len(ex) < 4:
                    ex.append(('fill', a, b, l, phi, bh))
                continue
            any_kill = None
            for P in range(1, full):
                if killed(U, L, P, X(P)):
                    any_kill = P; break
            st['other' if any_kill else 'NONE'] += 1
            if len(ex) < 8:
                ex.append(('other' if any_kill else 'NONE', a, b, l, phi, bh, [u for u in range(k) if any_kill and (any_kill >> u) & 1]))
    print(dict(st))
    for e in ex:
        print(e)


if __name__ == '__main__':
    main()
