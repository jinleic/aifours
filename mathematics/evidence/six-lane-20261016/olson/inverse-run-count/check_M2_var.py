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
            Z = [t for t in range(k) if bh[t] <= 0]
            if not Z:
                st['noZ(ND)'] += 1; continue
            flag = False
            for t in Z:
                T1 = 1 << t; lo, hi = -L[T1], U[T1]
                if lo <= hi and (phi[t] - lo) % p <= hi - lo:
                    st['single'] += 1; flag = True; break
                g = hi + 1 + ((phi[t] - (hi + 1)) % p)
                if g != x[t]:
                    st['STEP1_noncanon'] += 1
                if -bh[t] > 2 * kB - 2 - d[t]:
                    st['FAIL_9.2mixed'] += 1
                if -bh[t] > 2 * p - R - 2:
                    st['FAIL_depth'] += 1
            if flag:
                continue
            def X(P):
                return sum(x[u] for u in range(k) if (P >> u) & 1)
            def kil(P):
                return P not in (0, full) and -L[P] <= X(P) <= U[P]
            def comps(P):
                return sum(1 for j in range(k) if (P >> j) & 1 and not (P >> ((j - 1) % k)) & 1)
            def Phi(P):
                return sum(d[u] for u in range(k) if (P >> u) & 1) + 2 * comps(P) - sum(bh[u] for u in range(k) if (P >> u) & 1)
            target = 2 * kB + 2
            def fill(P):
                for f in [t for t in range(k) if bh[t] == 1 and d[t] > 0]:
                    if P and Phi(P) >= target:
                        break
                    if (P >> f) & 1 or (P >> ((f + 1) % k)) & 1 or (P >> ((f - 1) % k)) & 1:
                        continue
                    P |= 1 << f
                return P
            def greedy(P, seq):
                for t in seq:
                    if P and Phi(P) >= target:
                        break
                    P |= 1 << t
                return P
            Zp = sorted([t for t in Z if d[t] > 0], key=lambda t: -bh[t])
            Zall = sorted(Z, key=lambda t: -bh[t])
            neg = sum(1 << t for t in range(k) if d[t] <= 0)
            variants = {
                'V1_allneg': fill(greedy(neg, Zp)),
                'V2_Zfill': fill(sum(1 << t for t in Z)),
                'V3_greedyall': fill(greedy(0, Zall)),
                'V4_negdef': fill(greedy(sum(1 << t for t in Z if d[t] <= 0), Zp)),
            }
            for nm, P in variants.items():
                ok = P and Phi(P) >= target and kil(P)
                st[nm + ('_ok' if ok else '_FAIL')] += 1
    print(dict(st))
    for e in ex:
        print(e)


if __name__ == '__main__':
    main()
