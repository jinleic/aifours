#!/usr/bin/env python3
"""Enumerate odd orthomorphisms f of Z_27 that respect the cosets of 9Z_27, i.e. f(x) = h(x mod 9) (mod 9) for an odd
orthomorphism h of Z_9 (lane cfr33; facts-v6). For each h (21 odd orthomorphisms of Z_9) all lifts f = htilde + 9 g,
g odd with values in Z_3, are tested (bijective, f - id bijective). Linear f (c x) are dropped (facts-v3 E7).
Output: OUTDIR/Fh-<index>.txt (all members) and OUTDIR/Fh-<index>-conjreps.txt (one per conjugation orbit under Z_27^*),
plus OUTDIR/summary.json. Usage: enum_Fh.py OUTDIR (created; must not exist)."""
import itertools, json, os, sys
n, M = 27, 13
out = sys.argv[1]
os.mkdir(out)
odd9 = []
for perm in itertools.permutations(range(1, 9)):
    h = [0] + list(perm)
    if any(h[(9 - y) % 9] != (9 - h[y]) % 9 for y in range(9)):
        continue
    if len({(h[y] - y) % 9 for y in range(9)}) != 9:
        continue
    odd9.append(h)
U = [u for u in range(1, n) if u % 3]
lin = {tuple((c * a) % n for a in range(1, M + 1)) for c in range(n) if c % 3 == 2}
summary = []
for idx, h in enumerate(odd9):
    members = []
    for g in itertools.product(range(3), repeat=M):
        full = [0] * n
        for a in range(1, M + 1):
            v = (h[a % 9] + 9 * g[a - 1]) % n
            full[a] = v; full[n - a] = (-v) % n
        if len(set(full)) != n or len({(full[x] - x) % n for x in range(n)}) != n:
            continue
        t = tuple(full[1:M + 1])
        if t not in lin:
            members.append(t)
    S = set(members); seen = set(); reps = []
    for s in sorted(members):
        if s in seen:
            continue
        fl = [0] * n
        for a in range(1, M + 1):
            fl[a] = s[a - 1]; fl[n - a] = (-s[a - 1]) % n
        orb = set()
        for u in U:
            ui = pow(u, -1, n)
            orb.add(tuple((u * fl[(ui * a) % n]) % n for a in range(1, M + 1)))
        seen |= orb & S
        reps.append(s)
    with open(os.path.join(out, "Fh-%02d.txt" % idx), "x") as fh:
        fh.write("".join(" ".join(map(str, s)) + "\n" for s in members))
    with open(os.path.join(out, "Fh-%02d-conjreps.txt" % idx), "x") as fh:
        fh.write("".join(" ".join(map(str, s)) + "\n" for s in reps))
    summary.append({"index": idx, "h": h, "members": len(members), "conj_reps": len(reps),
                    "h_linear": any(all(h[y] == (c * y) % 9 for y in range(9)) for c in range(9))})
    print(idx, h, len(members), len(reps), flush=True)
with open(os.path.join(out, "summary.json"), "x") as fh:
    json.dump(summary, fh, indent=1)
