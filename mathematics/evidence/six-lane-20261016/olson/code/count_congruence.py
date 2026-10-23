#!/usr/bin/env python3
"""Exploratory: distribution of N(w) = number of increasing-index n-subwords
with identity product, for random and structured words of length L.

Purpose: test whether N(w) satisfies a word-independent congruence (as it does
mod p for p-groups via the Dimitrov group-algebra identity), which would give
an algebraic proof route.  Output: residue histograms mod small integers.
"""
import json
import random
import sys
from collections import Counter


def read_table(path):
    with open(path) as f:
        n = int(f.readline())
        tab = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, tab


def count_identity(n, tab, w, K=None):
    K = K or n
    dp = [[0] * n for _ in range(K + 1)]
    dp[0][0] = 1
    for t, a in enumerate(w, 1):
        for k in range(min(K, t), 0, -1):
            src = dp[k - 1]
            dst = dp[k]
            for g in range(n):
                c = src[g]
                if c:
                    dst[tab[g][a]] += c
    return dp[K][0]


def main():
    path = sys.argv[1]
    trials = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 12345
    L = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != '-' else None
    n, tab = read_table(path)
    L = L or 2 * n - 1
    rng = random.Random(seed)
    mods = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]
    hist = {m: Counter() for m in mods}
    zero = 0
    vals = []
    for _ in range(trials):
        # mixture: uniform words and words over small random alphabets
        k = rng.choice([n, 2, 3, 4])
        alph = rng.sample(range(n), min(k, n))
        w = [rng.choice(alph) for _ in range(L)]
        N = count_identity(n, tab, w)
        vals.append(N)
        if N == 0:
            zero += 1
        for m in mods:
            hist[m][N % m] += 1
    out = {'table': path, 'n': n, 'L': L, 'trials': trials, 'seed': seed, 'zero_count': zero,
           'min': min(vals), 'residues': {m: dict(sorted(hist[m].items())) for m in mods}}
    print(json.dumps(out))


if __name__ == '__main__':
    main()
