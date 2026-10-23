#!/usr/bin/env python3
"""Aid only: test candidate steps for mixed all-odd words (Sec. 12 programme).
Data: all reflection runs odd; rotation runs pure (rho_1^r or rho_-1^r) or (1,1)-pairs;
A >= B >= 1, B <= kappa, A <= 2p-1, k >= kmin; no window full; no inherited filter.
phi: interval-feasible (hwsingle fam 1) + random.  For each phi: chain lifts (start 0),
then report: Step 1 (defects canonical, x_t = singleton-gap lift), mixed (9.2)
delta_t <= 2kappa_B - 2 - d_t, depth delta_t <= 2p - R - 2, and which certificate kills:
Z / greedy (depth-ascending prefixes of Z) / greedy+fillers (bh = 1 runs, aligned first).
Usage: check_M2.py p trials seed kmin
"""
import random, sys
from collections import Counter
from itertools import combinations
from scl_closure import tables
from chainlift_test import run as hws


def main():
    p, T, seed, kmin = map(int, sys.argv[1:5])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); ex = []; done = 0
    while done < T:
        k = rng.randint(kmin, 2 * p - 3)
        R = rng.randint(k, 3 * p - 2); F = N - R
        if F < k or (F - k) % 2:
            continue
        H = (F - k) // 2; kappa = p - 1 - H
        if kappa < 1:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        a = []; b = []
        for x in r:
            u = rng.random()
            if x == 2 and u < 0.15:
                a.append(1); b.append(1)
            elif u < 0.3:
                a.append(0); b.append(x)
            else:
                a.append(x); b.append(0)
        A, B = sum(a), sum(b)
        if A < B:
            a, b = b, a; A, B = B, A
        if B < 1 or B > kappa or A >= 2 * p:
            continue
        l = [1] * k
        for _ in range(H):
            l[rng.randrange(k)] += 2
        U, L = tables(a, b, l, p)
        full = (1 << k) - 1
        if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
            continue
        done += 1
        d = [x - y for x, y in zip(a, b)]; kB = kappa - B
        sols = hws(p, 1, a, b, l, 300, 300)
        rnd = []
        for _ in range(40):
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
            xc = []
            for t in range(k):
                T1 = 1 << t; lo, hi = -L[T1], U[T1]
                xc.append(hi + 1 + ((phi[t] - (hi + 1)) % p))
            S = sum(xc)
            st['sumcanon=%d p' % (S // p) if S % p == 0 else 'sumcanon_nonmult'] += 1
            nonc = [t for t in range(k) if xc[t] != x[t]]
            st['chain_noncanon_runs=%d' % min(len(nonc), 3)] += 1
            if nonc:
                tt = [('al' if d[t] > 0 else 'anti' if d[t] < 0 else 'bal', 'def' if bh[t] <= 0 else 'nd') for t in nonc]
                for q in tt:
                    st['nc_' + q[0] + '_' + q[1]] += 1
    print(dict(st))
    for e in ex:
        print(e)


if __name__ == '__main__':
    main()
