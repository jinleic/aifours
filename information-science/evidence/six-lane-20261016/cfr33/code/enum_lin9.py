#!/usr/bin/env python3
"""Enumerate all odd orthomorphisms f of Z_27 with f(x) = C x (mod 9) (lane cfr33), their conjugation orbits under
Z_27^*, and write one representative per orbit. Usage: enum_lin9.py C OUT_ALL OUT_REPS"""
import itertools, sys
n, M = 27, 13
C, out_all, out_reps = int(sys.argv[1]), sys.argv[2], sys.argv[3]
U = [u for u in range(1, n) if u % 3]
sols = []
for vals in itertools.product(range(3), repeat=M):
    full = [0] * n
    for a in range(1, M + 1):
        v = (C * a + 9 * vals[a - 1]) % n
        full[a] = v; full[n - a] = (-v) % n
    if len(set(full)) != n:
        continue
    if len({(full[x] - x) % n for x in range(n)}) != n:
        continue
    sols.append(tuple(full[1:M + 1]))
lin = {tuple((c * a) % n for a in range(1, M + 1)) for c in range(n) if c % 3 == 2}
nonlin = [s for s in sols if s not in lin]
def full_of(s):
    fl = [0] * n
    for a in range(1, M + 1):
        fl[a] = s[a - 1]; fl[n - a] = (-s[a - 1]) % n
    return fl
seen, reps = set(), []
S = set(nonlin)
for s in sorted(nonlin):
    if s in seen:
        continue
    fl = full_of(s)
    orb = set()
    for u in U:
        ui = pow(u, -1, n)
        g = [(u * fl[(ui * x) % n]) % n for x in range(n)]
        orb.add(tuple(g[1:M + 1]))
    assert orb <= S
    seen |= orb
    reps.append(s)
with open(out_all, "x") as fh:
    fh.write("".join(" ".join(map(str, s)) + "\n" for s in nonlin))
with open(out_reps, "x") as fh:
    fh.write("".join(" ".join(map(str, s)) + "\n" for s in reps))
print("C %d: odd orthomorphisms = C x mod 9: %d (linear %d, non-linear %d); conjugation orbits %d" % (C, len(sols), len(sols) - len(nonlin), len(nonlin), len(reps)))
