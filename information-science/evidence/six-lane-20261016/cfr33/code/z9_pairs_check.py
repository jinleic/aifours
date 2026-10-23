#!/usr/bin/env python3
"""Exhaustive check (lane cfr33): number of normalized orthomorphisms of Z_n (f(0)=0, f and f-id bijective) and
number of orthogonal pairs (f-g bijective) among them. For n = 9 a zero pair count means no CFR(3,9), i.e. no
(Z_9,4;1)-DM, so kmax(Z_9) = 3 (rows 0, x, 2x give k = 3).  Usage: z9_pairs_check.py N"""
import sys
n = int(sys.argv[1])
orth = []
def rec(a, f, used, dused):
    if a == n:
        orth.append(tuple(f)); return
    for v in range(1, n):
        d = (v - a) % n
        if not used[v] and not dused[d]:
            used[v] = dused[d] = True; f.append(v)
            rec(a + 1, f, used, dused)
            f.pop(); used[v] = dused[d] = False
used = [False] * n; dused = [False] * n
used[0] = dused[0] = True
rec(1, [0], used, dused)
pairs = 0
for i in range(len(orth)):
    for j in range(i + 1, len(orth)):
        if len({(orth[i][x] - orth[j][x]) % n for x in range(n)}) == n:
            pairs += 1
print("n %d normalized orthomorphisms %d orthogonal pairs %d" % (n, len(orth), pairs))
