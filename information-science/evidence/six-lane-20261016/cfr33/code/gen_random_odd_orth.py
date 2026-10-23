#!/usr/bin/env python3
"""Generate random odd orthomorphisms of Z_n (seeded randomized backtracking), one per line (values at a = 1..M).
Usage: gen_random_odd_orth.py N COUNT SEED OUT   (lane cfr33; validation inputs only)"""
import random, sys
n, count, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
M = (n - 1) // 2
cls = [min(v, n - v) for v in range(n)]
rng = random.Random(seed)
res = []
while len(res) < count:
    g = [0] * (M + 1)
    def rec(a, u0, u1):
        if a > M:
            return True
        vals = list(range(1, n)); rng.shuffle(vals)
        for v in vals:
            c0, c1 = cls[v], cls[(v - a) % n]
            if c1 == 0 or (u0 >> c0) & 1 or (u1 >> c1) & 1:
                continue
            g[a] = v
            if rec(a + 1, u0 | 1 << c0, u1 | 1 << c1):
                return True
        return False
    if rec(1, 0, 0):
        res.append(tuple(g[1:]))
with open(out, "x") as fh:
    fh.write("".join(" ".join(map(str, r)) + "\n" for r in res))
print("wrote", len(res))
