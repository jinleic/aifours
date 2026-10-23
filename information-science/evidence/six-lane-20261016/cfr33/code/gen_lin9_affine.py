#!/usr/bin/env python3
"""Generate the 'lin9-mod9' family at n = 27 (lane cfr33): f(x) = 2x + 9 g0(x mod 9) with g0: Z_9 -> Z_3 odd
(g0(0) = 0, g0(9 - y) = -g0(y)); every such f is an odd orthomorphism (facts-v6 A1). Linear members (g0(y) = mu*y mod 3)
are dropped (facts-v3 E7). Usage: gen_lin9_affine.py C OUT  (C in {2, 5, 8} as the mod-9 slope)."""
import itertools, sys
n, M = 27, 13
C, out = int(sys.argv[1]), sys.argv[2]
res = []
for vals in itertools.product(range(3), repeat=4):
    g0 = [0] * 9
    for y in range(1, 5):
        g0[y] = vals[y - 1]; g0[9 - y] = (-vals[y - 1]) % 3
    full = [(C * x + 9 * g0[x % 9]) % n for x in range(n)]
    assert sorted(full) == list(range(n)), "not bijective"
    assert len({(full[x] - x) % n for x in range(n)}) == n, "f - id not bijective"
    assert all(full[(n - x) % n] == (n - full[x]) % n for x in range(n)), "not odd"
    lin = any(all(full[x] == (c * x) % n for x in range(n)) for c in range(n))
    if not lin:
        res.append(tuple(full[1:M + 1]))
with open(out, "x") as fh:
    fh.write("".join(" ".join(map(str, r)) + "\n" for r in res))
print("non-linear maps written:", len(res))
