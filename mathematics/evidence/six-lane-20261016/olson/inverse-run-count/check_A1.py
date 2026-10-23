#!/usr/bin/env python3
"""Aid only: Lemma A1 (proof-RUNS.md Sec. 11).  For random rho_1-only, all-odd words with
R = 2p-1 and kappa >= 1: every pattern with m* = floor(kappa/2)+1 intervals and
kappa <= R_P <= R - kappa has a full window, and such a pattern exists.
Usage: check_A1.py p trials seed
"""
import random, sys
from scl_closure import tables


def comps(P, k):
    return sum(1 for j in range(k) if (P >> j) & 1 and not (P >> ((j - 1) % k)) & 1)


def main():
    p, T, seed = map(int, sys.argv[1:4])
    rng = random.Random(seed); R = 2 * p - 1; N = 4 * p - 2
    bad = 0; noexist = 0; tested = 0; done = 0
    while done < T:
        kappa = rng.randint(1, min(p - 1, 8)); k = 2 * kappa + 1
        if k > R or k > 15:
            continue
        F = N - R; H = (F - k) // 2
        if p - 1 - H != kappa:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); a = [y - x for x, y in zip([0] + c, c + [R])]
        l = [1] * k
        for _ in range(H):
            l[rng.randrange(k)] += 2
        U, L = tables(a, [0] * k, l, p)
        ms = kappa // 2 + 1; found = False
        for P in range(1, (1 << k) - 1):
            if comps(P, k) != ms:
                continue
            x = sum(a[u] for u in range(k) if (P >> u) & 1)
            if kappa <= x <= R - kappa:
                tested += 1; found = True
                if U[P] + L[P] + 1 < p:
                    bad += 1
        if not found:
            noexist += 1
        done += 1
    print({'data': done, 'patterns_tested': tested, 'not_full': bad, 'no_pattern': noexist})


if __name__ == '__main__':
    main()
