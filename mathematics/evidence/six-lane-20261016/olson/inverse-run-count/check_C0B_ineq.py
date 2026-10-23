#!/usr/bin/env python3
"""Aid only: phi-independent inequalities of the proof of Theorem C0-B' (Secs. 9-11) on random
data with b = 0, all l odd, kappa >= 1 and a chosen R range (no inherited filter).
Checked for every chain start 0 and every run t:
  Step 0: prefix windows nonempty;  Step 1: L^t = floor((R - r_t)/2) and (9.1) S >= p-1 at every
  chain position;  Depth Lemma: room 3m <= k-2, U_{P+t} = floor((rho+r_t)/2), L_P = floor((R-rho)/2),
  (A') for defect-type runs (U^t = r_t - kappa), (B'), windows of P and P+t nonempty;
  greedy arithmetic: k + r_t + 1 <= 2p (K3 bound) and k <= 2p.
Windows that are full are reported separately (they kill outright).
Usage: check_C0B_ineq.py p trials seed Rmin Rmax
"""
import random, sys
from collections import Counter
from scl_closure import tables


def comps(P, k):
    return sum(1 for j in range(k) if (P >> j) & 1 and not (P >> ((j - 1) % k)) & 1)


def main():
    p, T, seed, Rmin, Rmax = map(int, sys.argv[1:6])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); fails = []
    done = 0
    while done < T:
        R = rng.randint(Rmin, Rmax); F = N - R
        k = rng.randint(5, min(R, F))
        if (F - k) % 2:
            continue
        H = (F - k) // 2; kappa = p - 1 - H
        if kappa < 1:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); a = [y - x for x, y in zip([0] + c, c + [R])]
        l = [1] * k
        for _ in range(H):
            l[rng.randrange(k)] += 2
        b = [0] * k
        done += 1
        U, L = tables(a, b, l, p)
        full = (1 << k) - 1
        def isfull(P):
            return U[P] + L[P] + 1 >= p
        bad = []
        # Step 0
        for j in range(1, k):
            P = (1 << j) - 1
            if isfull(P):
                st['prefix_full'] += 1
            elif U[P] + L[P] < 0:
                bad.append('step0_empty')
        # Step 1
        for t in range(k):
            T1 = 1 << t
            if L[T1] != (R - a[t]) // 2:
                bad.append('Lt_formula')
        for j in range(2, k):
            Pj = (1 << j) - 1; Pj1 = (1 << (j - 1)) - 1; t = j - 1
            S = U[Pj] + L[Pj1] + L[1 << t]
            if S < p - 1:
                bad.append('9.1')
        # Depth lemma for runs with U^t = r_t - kappa < floor(r_t/2)
        for t in range(k):
            rt = a[t]
            if U[1 << t] != rt - kappa or rt - kappa >= rt // 2:
                continue
            m1 = -(-(2 * kappa - 1 - rt) // 4); m2 = -(-(R + 2 * k - 4 * p - 1 + rt) // 4)
            m = max(1, m1, m2)
            if 3 * m > k - 2:
                bad.append('room'); continue
            P = 0
            for i in range(1, m + 1):
                P |= 1 << ((t + 3 * i - 1) % k); P |= 1 << ((t + 3 * i) % k)
            rho = sum(a[u] for u in range(k) if (P >> u) & 1); Q = P | (1 << t)
            if isfull(P) or isfull(Q):
                st['depth_full'] += 1; continue
            if U[Q] != (rho + rt) // 2: bad.append('F12')
            if L[P] != (R - rho) // 2: bad.append('F34')
            if U[P] + U[1 << t] + L[Q] < -2: bad.append('Aprime')
            if L[P] + L[1 << t] + U[Q] < p - 2: bad.append('Bprime')
            if U[P] + L[P] < 0 or U[Q] + L[Q] < 0: bad.append('empty')
            if k + rt + 1 > 2 * p: bad.append('K3bound')
        for x in set(bad):
            st['FAIL_' + x] += 1
        if bad and len(fails) < 4:
            fails.append((a, l, sorted(set(bad))))
        st['data'] += 1
    print(dict(st))
    for f in fails:
        print(f)


if __name__ == '__main__':
    main()
