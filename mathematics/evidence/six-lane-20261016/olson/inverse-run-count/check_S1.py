#!/usr/bin/env python3
"""Aid only: replay the proof of Theorem S1 (proof-RUNS.md Sec. 9) on random data and random phi.
For each (data, phi): follow the proof; every step either produces an explicit killed pattern
(certificate checked by the HW window test) or the final constructed pattern must be killed.
Report any instance where the proof's claimed kill fails (would be a bug in the proof).
Usage: check_S1.py p trials seed [mode]   mode: S1 (default) = sample S1 data only; any = all regime-B
"""
import random, sys
from collections import Counter
from hw import windows


def in_win(W, P, s, p):
    lo, hi = W[P]
    if lo > hi:
        return False
    if hi - lo + 1 >= p:
        return True
    return (s - lo) % p <= hi - lo


def comps(P, k):
    """number of maximal cyclic intervals of bitmask P over k runs (P proper nonempty)."""
    z = [(P >> i) & 1 for i in range(k)]
    return sum(1 for j in range(k) if z[j] and not z[j - 1])


def proof_S1(p, a, l, phi, W):
    """returns (status, pattern) ; status in {'prefix','single','ND','greedy','FAIL...'}"""
    k = len(a); R = sum(a); full = (1 << k) - 1
    # chain lifts along prefixes {0..j-1}
    prev = 0; x = [0] * k
    for j in range(1, k + 1):
        P = (1 << j) - 1
        s = sum(phi[:j]) % p
        if j == k:
            cand = p
        else:
            if in_win(W, P, s, p):
                return 'prefix', P
            lo, hi = W[P]
            if lo > hi:
                return 'FAIL_empty_prefix', P
            cand = hi + 1 + ((s - (hi + 1)) % p)
        x[j - 1] = cand - prev; prev = cand
    assert sum(x) == p
    bh = [2 * x[t] - a[t] for t in range(k)]
    Z = [t for t in range(k) if bh[t] <= 0]
    for t in Z:
        lo, hi = W[1 << t]
        if lo <= x[t] <= hi:
            return 'single', 1 << t
        if x[t] < lo:
            return 'FAIL_deep_singleton', 1 << t
    if not Z:
        # ND: some run with 1 <= d_t <= 2D+1 (constant: d = r = a, D = R)
        D = R
        cands = [t for t in range(k) if 1 <= a[t] <= 2 * D + 1]
        for t in cands:
            if lo_hi_contains(W, 1 << t, x[t], p):
                return 'ND', 1 << t
        return 'FAIL_ND', None
    H = sum(v // 2 for v in l); kappa = p - 1 - H
    for t in Z:
        if -bh[t] > 2 * kappa - 2 - a[t]:
            return 'FAIL_9.2', 1 << t
    Z.sort(key=lambda t: -bh[t])  # depth ascending (depth = -bh)
    P = 0
    for t in Z:
        P |= 1 << t
        m = comps(P, k)
        rho = sum(a[u] for u in range(k) if (P >> u) & 1)
        dl = -sum(bh[u] for u in range(k) if (P >> u) & 1)
        if rho + 2 * m + dl >= 2 * kappa + 2:
            if R + 2 * k <= 4 * p - 3 and (dl > 4 * kappa - 5 or rho + 2 * m + dl > 4 * kappa + 1):
                return 'FAIL_step4bound', P
            s = sum(x[u] for u in range(k) if (P >> u) & 1)
            Q = P if not (P >> (k - 1)) & 1 else full ^ P
            ss = s if Q == P else -s
            lo, hi = W[Q]
            ok = (lo <= ss <= hi)
            return ('greedy' if ok else 'FAIL_greedy'), P
    return 'FAIL_noistar', None


def lo_hi_contains(W, P, v, p):
    lo, hi = W[P]
    return lo <= v <= hi


def main():
    from sample_famtest import inherited, has_full
    p = int(sys.argv[1]); T = int(sys.argv[2]); seed = int(sys.argv[3]); mode = sys.argv[4] if len(sys.argv) > 4 else 'S1'
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); fails = []
    data = 0
    while data < T:
        k = rng.randint(p + 1, min(2 * p - 3, 14))
        R = rng.randint(k, 2 * p - 3)
        if mode == 'S1' and R + 2 * k > 4 * p - 3:
            continue
        F = N - R
        if F < k:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        # odd reflection runs summing to F with k parts
        if (F - k) % 2:
            continue
        extra = (F - k) // 2
        l = [1] * k
        for _ in range(extra):
            l[rng.randrange(k)] += 2
        a = list(r); b = [0] * k
        if not inherited(a, b, l, p) or has_full(a, b, l, p):
            continue
        data += 1
        W = windows(a, b, l, p)
        from chainlift_test import run
        sols = run(p, 1, a, b, l, 2000, 2000)
        rnd = []
        for _ in range(100):
            ph = [rng.randrange(p) for _ in range(k - 1)]; ph.append((-sum(ph)) % p); rnd.append(ph)
        for phi in sols + rnd:
            stt, P = proof_S1(p, a, l, phi, W)
            st[stt] += 1
            if stt.startswith('FAIL') and len(fails) < 5:
                fails.append((a, l, phi, stt))
    print(dict(st))
    for f in fails:
        print(f)


if __name__ == '__main__':
    main()
