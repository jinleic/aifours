#!/usr/bin/env python3
"""Independent enumerator (lane cfr33): all odd orthomorphisms g of Z_n orthogonal to a given odd f (i.e. the set L2 of
cfr_odd_search_v6), plus the number of orthogonal pairs inside L2. Written separately from the C code (fixed point
order a = 1..M, plain recursion, no DLX). Usage: l2_enum_py.py N "f(1) ... f(M)" [--pairs]
Prints the count, the sha256 of the sorted list (one line per map, values space-separated) and optionally the pair count.
"""
import hashlib, sys

n = int(sys.argv[1]); M = (n - 1) // 2
f = [0] + [int(x) for x in sys.argv[2].split()]
assert len(f) == M + 1
cls = [min(v, n - v) for v in range(n)]
sols = []
g = [0] * (M + 1)


def rec(a, u0, u1, u2):
    if a > M:
        sols.append(tuple(g[1:]))
        return
    for v in range(1, n):
        c0 = cls[v]; c1 = cls[(v - a) % n]; c2 = cls[(v - f[a]) % n]
        if c1 == 0 or c2 == 0:
            continue
        b0, b1, b2 = 1 << c0, 1 << c1, 1 << c2
        if (u0 & b0) or (u1 & b1) or (u2 & b2):
            continue
        g[a] = v
        rec(a + 1, u0 | b0, u1 | b1, u2 | b2)
    g[a] = 0


rec(1, 0, 0, 0)
sols.sort()
text = "".join(" ".join(map(str, s)) + "\n" for s in sols)
print("count", len(sols), "sha256", hashlib.sha256(text.encode()).hexdigest())
if "--pairs" in sys.argv:
    full = (1 << (M + 1)) - 2
    pairs = 0
    for i in range(len(sols)):
        si = sols[i]
        for j in range(i + 1, len(sols)):
            sj = sols[j]
            m = 0
            ok = True
            for a in range(M):
                c = cls[(si[a] - sj[a]) % n]
                b = 1 << c
                if c == 0 or (m & b):
                    ok = False
                    break
                m |= b
            if ok:
                pairs += 1
    print("pairs", pairs)
