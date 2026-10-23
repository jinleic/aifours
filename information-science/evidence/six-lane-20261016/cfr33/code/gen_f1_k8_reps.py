#!/usr/bin/env python3
"""Regenerate the K = <8>-equivariant odd orthomorphism candidates for f_1 at n = 27 and their orbit representatives
(lane cfr33).  Usage: gen_f1_k8_reps.py OUT_REPS_TXT
K = <8> = {1, 8, 10, 17, 19, 26} <= Z_27^*. A K-equivariant odd orthomorphism maps units to units (f(u) must be a unit
since |uK| = 6) and 3Z_27 to itself; the units part is fixed by f(1), f(2), f(4) (coset representatives), the 3Z part
is 3*h(y) with h an odd orthomorphism of Z_9. Linear maps c*x are excluded (facts-v3 E7). Orbits are taken under
conjugation by Z_27^*, f -> id - f and f -> f^-1 (facts-v4 R1). Output: one line per orbit (lexicographically smallest
member), values f(1..13) separated by spaces.
"""
import itertools, sys
n, M = 27, 13
U = [x for x in range(n) if x % 3]
K = [1, 8, 10, 17, 19, 26]
cos = {u: frozenset((u * k) % n for k in K) for u in U}
reps = sorted({min(c) for c in cos.values()})
units_parts = []
for vals in itertools.product(U, repeat=3):
    if len({cos[v] for v in vals}) != 3:
        continue
    d = [(v - u) % n for u, v in zip(reps, vals)]
    if any(x % 3 == 0 for x in d) or len({cos[x] for x in d}) != 3:
        continue
    units_parts.append(dict(zip(reps, vals)))
odd9 = []
for perm in itertools.permutations(range(1, 9)):
    h = [0] + list(perm)
    if any(h[(9 - y) % 9] != (9 - h[y]) % 9 for y in range(9)):
        continue
    if len({(h[y] - y) % 9 for y in range(9)}) != 9:
        continue
    odd9.append(h)
cands = set()
for up in units_parts:
    for h in odd9:
        full = [0] * n
        for r, v in up.items():
            for k in K:
                full[(r * k) % n] = (v * k) % n
        for y in range(9):
            full[3 * y] = 3 * h[y]
        assert sorted(full) == list(range(n)) and len({(full[x] - x) % n for x in range(n)}) == n
        assert all(full[(n - x) % n] == (n - full[x]) % n for x in range(n))
        cands.add(tuple(full[1:M + 1]))
lin = {tuple((c * a) % n for a in range(1, M + 1)) for c in range(n) if c % 3 == 2}
nonlin = sorted(cands - lin)


def full_from(c):
    fl = [0] * n
    for a in range(1, M + 1):
        fl[a] = c[a - 1]; fl[n - a] = (-c[a - 1]) % n
    return fl


def conj(fl, u):
    ui = pow(u, -1, n)
    return [(u * fl[(ui * x) % n]) % n for x in range(n)]


seen, out = set(), []
for c in nonlin:
    if c in seen:
        continue
    orb, stack = {c}, [c]
    while stack:
        fl = full_from(stack.pop())
        inv = [0] * n
        for x in range(n):
            inv[fl[x]] = x
        for g in [conj(fl, u) for u in U] + [[(x - fl[x]) % n for x in range(n)], inv]:
            p = tuple(g[1:M + 1])
            if p not in orb:
                orb.add(p); stack.append(p)
    assert orb <= set(nonlin)
    seen |= orb
    out.append(c)
print("units parts %d, odd orthomorphisms of Z_9 %d, candidates %d, non-linear %d, orbits %d"
      % (len(units_parts), len(odd9), len(cands), len(nonlin), len(out)))
with open(sys.argv[1], "x") as fh:
    fh.write("".join(" ".join(map(str, c)) + "\n" for c in out))
