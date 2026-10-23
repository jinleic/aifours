#!/usr/bin/env python3
"""All odd normalised orthomorphisms of Z_n and one representative per R1-orbit (sub-lane cfr21, worker InfoCFR27Lift).

Usage: gen_odd_reps_c21v1.py N OUT.txt          (OUT written with mode 'x'; one line per orbit representative, the values
                                                f(1) .. f(M), M = (N-1)/2, i.e. the f1file format of cfr_odd_search_v7)
Written independently of keq_clique_c21v1.c (different algorithm): odd f is given on half-columns a = 1..M by values
v in 1..N-1 (f(-a) = -f(a)); f is an orthomorphism iff the +- classes of the M values f(a) are distinct and the +- classes
of the M values f(a) - a are distinct and nonzero. Plain DFS in the order a = 1..M. R1 group (facts-v4 R1): conjugation
f -> u f(u^-1 .) by units u, f -> id - f, f -> f^-1. Orbits are formed explicitly (every member marked), the
representative is the lexicographically smallest member (full array f(0..N-1)). Prints the number of maps and orbits.
"""
import sys
from math import gcd


def main():
    n, out = int(sys.argv[1]), sys.argv[2]
    m = (n - 1) // 2
    cls = [min(v % n, (-v) % n) for v in range(n)]
    maps = []
    val = [0] * (m + 1)
    used1 = [False] * (m + 1)
    used2 = [False] * (m + 1)

    def rec(a):
        if a > m:
            maps.append(tuple(val[1:]))
            return
        for v in range(1, n):
            c1, c2 = cls[v], cls[(v - a) % n]
            if c2 == 0 or used1[c1] or used2[c2]:
                continue
            used1[c1] = used2[c2] = True
            val[a] = v
            rec(a + 1)
            used1[c1] = used2[c2] = False

    rec(1)

    def full(h):
        f = [0] * n
        for a in range(1, m + 1):
            f[a] = h[a - 1]
            f[n - a] = (-h[a - 1]) % n
        return f

    def half(f):
        return tuple(f[1:m + 1])

    units = [u for u in range(1, n) if gcd(u, n) == 1]
    uinv = {u: pow(u, -1, n) for u in units}
    index = {h: i for i, h in enumerate(maps)}
    seen = bytearray(len(maps))
    reps = []
    for i, h in enumerate(maps):
        if seen[i]:
            continue
        orbit = {h}
        frontier = [h]
        while frontier:
            new = []
            for g in frontier:
                f = full(g)
                imgs = [half([(x - f[x]) % n for x in range(n)])]          # id - f
                inv = [0] * n
                for x in range(n):
                    inv[f[x]] = x
                imgs.append(half(inv))                                       # f^-1
                for u in units:
                    ui = uinv[u]
                    imgs.append(half([(u * f[(ui * x) % n]) % n for x in range(n)]))
                for im in imgs:
                    if im not in orbit:
                        if im not in index:
                            raise SystemExit("INTERNAL: image is not an odd orthomorphism in the list")
                        orbit.add(im)
                        new.append(im)
            frontier = new
        for g in orbit:
            seen[index[g]] = 1
        reps.append(min(orbit, key=lambda g: full(g)))
    reps.sort(key=lambda g: full(g))
    with open(out, "x") as fh:
        for g in reps:
            fh.write(" ".join(map(str, g)) + "\n")
    print("N %d odd normalised orthomorphisms %d R1-orbits %d" % (n, len(maps), len(reps)))


if __name__ == "__main__":
    main()
