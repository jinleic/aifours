#!/usr/bin/env python3
"""Aid only: end-to-end replay of Corollary B0 (proof-RUNS.md Sec. 11) on random rho_1-only words
with ANY reflection parities, k >= p+1, no inherited filter.  For each phi (interval-feasible for w
plus random): merge segments (Lemma OR) to w~, map phi to phi~ (segment sums), find a kill of w~
by the C0-B' route (full window, else the proof replay of check_C0B.proof), map the kill pattern
back to w (union of segments) and confirm phi(P) lies in the window of P in w.
Usage: check_B0_pipeline.py p trials seed
"""
import random, sys
from collections import Counter
from scl_closure import tables
from hw import windows
from check_C0B import proof as c0b_proof


def merge(a, l):
    k = len(a); odd = [j for j in range(k) if l[j] % 2]
    if not odd:
        return None
    # segment = runs strictly after an odd reflection run up to and including the run before the next
    # odd reflection run; run t is followed by reflection run S_t.
    segs = []
    for i, j0 in enumerate(odd):
        j1 = odd[(i + 1) % len(odd)]
        runs = []; t = (j0 + 1) % k
        while True:
            runs.append(t)
            if t == j1:
                break
            t = (t + 1) % k
        segs.append(runs)
    a2 = [sum(a[t] for t in s) for s in segs]
    l2 = [sum(l[t] for t in s if l[t] % 2 == 0) + l[s[-1]] for s in segs]
    return segs, a2, l2


def main():
    p, T, seed = map(int, sys.argv[1:4])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); done = 0
    while done < T:
        k = rng.randint(p + 1, 2 * p - 2)
        R = rng.randint(k, 2 * p - 2); F = N - R
        if F < k:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); a = [y - x for x, y in zip([0] + c, c + [R])]
        cl = sorted(rng.sample(range(1, F), k - 1)); l = [y - x for x, y in zip([0] + cl, cl + [F])]
        mg = merge(a, l)
        if mg is None:
            continue
        segs, a2, l2 = mg
        k2 = len(a2); H = sum(x // 2 for x in l); kappa = p - 1 - H
        if kappa < 1 or k2 < 2:
            continue
        b = [0] * k; b2 = [0] * k2
        U, L = tables(a, b, l, p)
        full = (1 << k) - 1
        if any(U[P] + L[P] + 1 >= p for P in range(1, full)):
            continue
        done += 1
        W2 = windows(a2, b2, l2, p); U2, L2 = tables(a2, b2, l2, p)
        for _ in range(60):
            ph = [rng.randrange(p) for _ in range(k - 1)]; ph.append((-sum(ph)) % p)
            phi2 = [sum(ph[t] for t in s) % p for s in segs]
            full2 = (1 << k2) - 1
            killP2 = None
            for P2 in range(1, full2):
                if U2[P2] + L2[P2] + 1 >= p:
                    killP2 = P2; break
            how = 'full~'
            if killP2 is None:
                res = c0b_proof(p, a2, l2, phi2, W2, U2, L2)
                if res.startswith('FAIL'):
                    st['C0B_' + res] += 1; continue
                # find the kill pattern explicitly (any killed pattern of w~)
                how = res
                for P2 in range(1, full2):
                    s2 = sum(phi2[j] for j in range(k2) if (P2 >> j) & 1) % p
                    lo, hi = -L2[P2], U2[P2]
                    if lo <= hi and (s2 - lo) % p <= hi - lo:
                        killP2 = P2; break
            if killP2 is None:
                st['NO_KILL_IN_W~'] += 1; continue
            P = sum(1 << t for j in range(k2) if (killP2 >> j) & 1 for t in segs[j])
            s = sum(ph[t] for t in range(k) if (P >> t) & 1) % p
            lo, hi = -L[P], U[P]
            same = (U[P], L[P]) == (U2[killP2], L2[killP2])
            inw = lo <= hi and (hi - lo + 1 >= p or (s - lo) % p <= hi - lo)
            st[how + ('_transfers' if inw and same else '_TRANSFER_FAIL')] += 1
    print(dict(st))


if __name__ == '__main__':
    main()
