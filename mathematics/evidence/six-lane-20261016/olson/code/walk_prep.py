#!/usr/bin/env python3
"""Prepare inputs for avoider_walk: automorphism text file and seed avoiders
a^{n-1} b^{n-1} for every 'complementary' pair (<a> cap <b> = 1,
lcm(ord a, ord b) = n), each seed checked by an independent Python DP.
Usage: python3 code/walk_prep.py GROUP [max_seeds]
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
GDIR = os.path.join(LANE, 'evidence', 'groups')


def read_table(path):
    with open(path) as f:
        n = int(f.readline())
        return n, [list(map(int, f.readline().split())) for _ in range(n)]


def avoids(n, tab, w, K):
    S = [set() for _ in range(K + 1)]
    S[0].add(0)
    for a in w:
        for k in range(K, 0, -1):
            S[k] |= {tab[g][a] for g in S[k - 1]}
    return 0 not in S[K]


def main():
    g = sys.argv[1]
    maxs = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    n, tab = read_table(os.path.join(GDIR, g + '.tab'))
    aut = json.load(open(os.path.join(GDIR, g + '.aut.json')))
    with open(os.path.join(GDIR, g + '.aut.txt'), 'w') as f:
        f.write(f"{n} {len(aut['automorphisms'])}\n")
        for phi in aut['automorphisms']:
            f.write(' '.join(map(str, phi)) + '\n')
        f.write(' '.join(map(str, aut['inverse'])) + '\n')
    ords = aut['element_orders']

    def cyc(a):
        s, x = {0}, a
        while x != 0:
            s.add(x)
            x = tab[x][a]
        return s
    seeds = []
    for a in range(1, n):
        for b in range(1, n):
            if a == b:
                continue
            if cyc(a) & cyc(b) != {0}:
                continue
            if ords[a] * ords[b] // math.gcd(ords[a], ords[b]) != n:
                continue
            w = [a] * (n - 1) + [b] * (n - 1)
            if avoids(n, tab, w, n):
                seeds.append(w)
            if len(seeds) >= maxs:
                break
        if len(seeds) >= maxs:
            break
    with open(os.path.join(GDIR, g + '.seeds.txt'), 'w') as f:
        for w in seeds:
            f.write(' '.join(map(str, w)) + '\n')
    print(g, 'n', n, '|Aut|', len(aut['automorphisms']), 'seeds', len(seeds))


if __name__ == '__main__':
    main()
