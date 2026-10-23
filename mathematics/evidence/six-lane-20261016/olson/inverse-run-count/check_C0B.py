#!/usr/bin/env python3
"""Aid only: replay the proof of Theorem C0-B (proof-RUNS.md Sec. 10) on random data.
Data: constant rho_1 runs, all reflection runs odd, inherited, N = 4p-2, k >= p+1, R <= 2p-3.
For every interval-feasible phi (plus random phi) follow the proof; every claimed inequality is
checked numerically; any violation is reported as FAIL_<step>.
Usage: check_C0B.py p trials seed kmax
"""
import random, sys
from collections import Counter
from hw import windows
from scl_closure import tables


def comps(P, k):
    z = [(P >> i) & 1 for i in range(k)]
    return sum(1 for j in range(k) if z[j] and not z[j - 1])


def in_win(W, P, s, p):
    lo, hi = W[P]
    if lo > hi:
        return False
    if hi - lo + 1 >= p:
        return True
    return (s - lo) % p <= hi - lo


def base_lift(U, L, P, s, p):
    lo, hi = -L[P], U[P]
    return hi + 1 + ((s - (hi + 1)) % p)


def proof(p, a, l, phi, W, U, L):
    k = len(a); R = sum(a); full = (1 << k) - 1
    H = sum(v // 2 for v in l); kappa = p - 1 - H
    # Step 0/TL: chain lifts
    prev = 0; x = [0] * k
    for j in range(1, k + 1):
        P = (1 << j) - 1
        s = sum(phi[:j]) % p
        if j == k:
            cand = p
        else:
            if in_win(W, P, s, p):
                return 'prefix'
            if U[P] + L[P] < 0:
                return 'FAIL_empty_prefix'
            cand = base_lift(U, L, P, s, p)
        x[j - 1] = cand - prev; prev = cand
    bh = [2 * x[t] - a[t] for t in range(k)]
    Z = [t for t in range(k) if bh[t] <= 0]
    # Step 1: defects canonical, (9.2)
    for t in Z:
        T = 1 << t
        if in_win(W, T, phi[t], p):
            return 'single'
        if x[t] != base_lift(U, L, T, phi[t], p):
            return 'FAIL_step1_noncanonical'
        if -bh[t] > 2 * kappa - 2 - a[t]:
            return 'FAIL_9.2'
    if not Z:
        return 'ND_case'
    # Depth Lemma with pairs construction
    for t in Z:
        rt = a[t]
        m1 = -(-(2 * kappa - 1 - rt) // 4); m2 = -(-(R + 2 * k - 4 * p - 1 + rt) // 4)
        m = max(m1, m2, 1)
        if 3 * m > k - 2:
            return 'FAIL_room'
        P = 0
        for i in range(1, m + 1):
            P |= 1 << ((t + 3 * i - 1) % k); P |= 1 << ((t + 3 * i) % k)
        if comps(P, k) != m or P & ((1 << t) | (1 << ((t - 1) % k)) | (1 << ((t + 1) % k))):
            return 'FAIL_pairs_shape'
        rho = sum(a[u] for u in range(k) if (P >> u) & 1)
        T = 1 << t; Q = P | T
        Ept = rho + rt; EmP = R - rho
        if U[Q] != Ept // 2:
            return 'FAIL_F12'
        if L[P] != EmP // 2:
            return 'FAIL_F34'
        if U[P] + U[T] + L[Q] < -2:
            return 'FAIL_Aprime'
        if L[P] + L[T] + U[Q] < p - 2:
            return 'FAIL_Bprime'
        if U[P] + L[P] < 0 or U[Q] + L[Q] < 0:
            return 'FAIL_empty'
        # avoidance at P and Q (else kill found)
        sP = sum(phi[u] for u in range(k) if (P >> u) & 1) % p
        if in_win(W, P, sP, p):
            return 'P_killed'
        if in_win(W, Q, (sP + phi[t]) % p, p):
            return 'Q_killed'
        if -bh[t] > 2 * p - R - 2:
            return 'FAIL_depth_bound'
    # Step 4 greedy
    Zs = sorted(Z, key=lambda t: -bh[t])
    Pm = 0
    for idx, t in enumerate(Zs):
        Pm |= 1 << t
        mm = comps(Pm, k); rho = sum(a[u] for u in range(k) if (Pm >> u) & 1)
        dl = -sum(bh[u] for u in range(k) if (Pm >> u) & 1)
        if rho + 2 * mm + dl >= 2 * kappa + 2:
            if idx == 0:
                return 'FAIL_istar1'
            s = sum(x[u] for u in range(k) if (Pm >> u) & 1)
            lo, hi = -L[Pm], U[Pm]
            return 'greedy' if lo <= s <= hi else 'FAIL_greedy'
    return 'FAIL_noistar'


def main():
    from sample_famtest import inherited, has_full
    from chainlift_test import run
    p = int(sys.argv[1]); T = int(sys.argv[2]); seed = int(sys.argv[3]); kmax = int(sys.argv[4])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); fails = []; data = 0
    while data < T:
        k = rng.randint(p + 1, min(2 * p - 3, kmax)); R = rng.randint(k, 2 * p - 3); F = N - R
        if F < k or (F - k) % 2:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        l = [1] * k
        for _ in range((F - k) // 2):
            l[rng.randrange(k)] += 2
        a = list(r); b = [0] * k
        if not inherited(a, b, l, p) or has_full(a, b, l, p):
            continue
        data += 1
        W = windows(a, b, l, p); U, L = tables(a, b, l, p)
        sols = run(p, 1, a, b, l, 1500, 1500)
        rnd = []
        for _ in range(100):
            ph = [rng.randrange(p) for _ in range(k - 1)]; ph.append((-sum(ph)) % p); rnd.append(ph)
        for phi in sols + rnd:
            res = proof(p, a, l, phi, W, U, L)
            st[res] += 1
            if res.startswith('FAIL') and len(fails) < 5:
                fails.append((a, l, phi, res))
    print(dict(st))
    for f in fails:
        print(f)


if __name__ == '__main__':
    main()
