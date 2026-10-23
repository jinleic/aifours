#!/usr/bin/env python3
"""cert_to_seed.py -- extract a PC-SEED (README 1.5) from a strict POINT-CYCLIC-RESOLUTION certificate whose
classes are permuted by x -> x+1 (used for controls and round trips; it does not check the certificate).

Procedure (GENERAL-REDUCTION.md Lemmas 5-6): n = v/4, H = {0, n, 2n, 3n}. P_0 = the class containing H; t = the
length of its orbit under x -> x+1. The X blocks: one representative (lexicographically smallest sorted tuple) of
each <t>-orbit of full blocks of P_0. For every other class orbit (length s = 4k): its lexicographically smallest
class P, and one representative (smallest tuple) of each <s>-orbit of blocks of P. Output: X lines sorted, groups in
nonincreasing k (ties by their sorted line lists), Y lines sorted within a group.
Writes only the given output path; refuses to overwrite; never deletes anything.
Usage: cert_to_seed.py CERT OUT
"""
import os
import sys


def main(argv):
    if len(argv) != 3 or os.path.exists(argv[2]):
        print("usage: cert_to_seed.py CERT OUT (OUT must not exist)", file=sys.stderr)
        return 2
    lines = open(argv[1]).read().rstrip("\n").split("\n")
    v = int(lines[0].split()[1])
    n = v // 4
    byc = {}
    for line in lines[1:]:
        t = list(map(int, line.split()))
        byc.setdefault(t[0], []).append(tuple(t[1:]))
    classes = [frozenset(P) for P in byc.values()]
    cset = set(classes)

    def tr(B, d):
        return tuple(sorted((p + d) % v for p in B))

    def ctr(P, d):
        return frozenset(tr(B, d) for B in P)

    def orbit_len(P):
        d = 1
        while ctr(P, d) != P:
            d += 1
        return d

    H = (0, n, 2 * n, 3 * n)
    P0 = next(P for P in classes if H in P)
    t = orbit_len(P0)
    short = {tuple(sorted((a + h) % v for h in H)) for a in range(n)}

    def reps(P, s):
        out, seen = [], set()
        for B in sorted(P):
            if B in short or B in seen:
                continue
            orb = {tr(B, c) for c in range(0, v, s)}
            seen |= orb
            out.append(min(orb))
        return sorted(out)

    X = reps(P0, t) if t > 1 else []
    done = {ctr(P0, d) for d in range(t)}
    groups = []
    for P in sorted(classes, key=lambda P: sorted(P)):
        if P in done:
            continue
        s = orbit_len(P)
        orb = [ctr(P, d) for d in range(s)]
        rep = min(orb, key=lambda Q: sorted(Q))
        done |= set(orb)
        Y = reps(rep, s)
        assert len(Y) * 4 == s, (s, len(Y))
        groups.append((s // 4, Y))
    assert done == cset
    groups.sort(key=lambda g: (-g[0], g[1]))
    out = [f"PC-SEED {v}", f"SHORT {t}"] + ["X " + " ".join(map(str, B)) for B in X]
    for k, Y in groups:
        out.append(f"GROUP {k}")
        out += ["Y " + " ".join(map(str, B)) for B in Y]
    with open(argv[2], "x") as f:
        f.write("\n".join(out) + "\n")
    print(f"wrote {argv[2]}: v={v} t={t} K={[k for k, _ in groups]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
