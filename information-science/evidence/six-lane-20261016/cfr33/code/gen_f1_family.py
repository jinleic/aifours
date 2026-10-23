#!/usr/bin/env python3
"""Random odd orthomorphisms of Z_27 from structured families, for f_1 surveys (lane cfr33).
Usage: gen_f1_family.py FAMILY COUNT SEED OUT
FAMILY: random   - any odd orthomorphism (randomized backtracking)
        pres3Z   - odd orthomorphism with f(3Z_27) = 3Z_27 (3Z part = random odd orthomorphism of Z_9)
        lin9:c   - odd orthomorphism with f(x) = c x (mod 9) for all x (c = 2 mod 3)
Values printed for a = 1..13, one map per line. Every output is re-checked (bijective, f - id bijective, odd).
"""
import random, sys
n, M = 27, 13
fam, count, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
rng = random.Random(seed)
cls = [min(v, n - v) for v in range(n)]
def allowed(a, v):
    if fam == "pres3Z":
        return (a % 3 == 0) == (v % 3 == 0)
    if fam.startswith("lin9:"):
        c = int(fam[5:])
        return (v - c * a) % 9 == 0
    return True
res = []
tries = 0
while len(res) < count:
    tries += 1
    g = [0] * (M + 1)
    order = list(range(1, M + 1)); rng.shuffle(order)
    def rec(k, u0, u1):
        if k == M:
            return True
        a = order[k]
        vals = [v for v in range(1, n) if allowed(a, v)]; rng.shuffle(vals)
        for v in vals:
            c0, c1 = cls[v], cls[(v - a) % n]
            if c1 == 0 or (u0 >> c0) & 1 or (u1 >> c1) & 1:
                continue
            g[a] = v
            if rec(k + 1, u0 | 1 << c0, u1 | 1 << c1):
                return True
        g[a] = 0
        return False
    if rec(0, 0, 0):
        full = [0] * n
        for a in range(1, M + 1):
            full[a] = g[a]; full[n - a] = (-g[a]) % n
        assert sorted(full) == list(range(n)) and len({(full[x] - x) % n for x in range(n)}) == n
        t = tuple(g[1:])
        if t not in res:
            res.append(t)
with open(out, "x") as fh:
    fh.write("".join(" ".join(map(str, r)) + "\n" for r in res))
print("family %s wrote %d maps (%d attempts)" % (fam, len(res), tries))
