#!/usr/bin/env python3
"""README E10: explicit Tan–Zhou Construction 2.3 (lines 444–541; transcription in
sources/construction-2.3-transcription.md) for (m, g, n, s) = (8, 4, 4, 0), standard library only.

Inputs: FG.json (1-FG(3,({4},{5}),16) of type 4^4: groups, B, T on points 0..15), a GCDCQS 32 4 8
certificate (gcDCQS(8^4:0), groups 0..7 | 8..15 | 16..23 | 24..31) and an FDH 5 8 certificate
(groups 0..7 | … | 32..39, Kirkman frames at every point).
Labels: a 1-FG point p has group u(p) (index of its group in FG.json) and position w(p) (rank in
its group); the big point (p, i), i in I_8, gets label 32·u(p) + 8·w(p) + i, so the big groups are
G_u × I_8 = {32u, …, 32u + 31}.
A_B (B in B): the gcDCQS point 8t + i ↦ (B_t, i), B_t = the point of B in group t (B meets each group
once).  D_T (T in T, sorted T = (a_0 < … < a_4)): the FDH point 8s + i ↦ (a_s, i).
Colouring at (x, i) (lines 495–531): F^{y,j} (y ≠ x, j = 0..3) and F^j (j = 0..3) exactly as in the
source; label bijections: the non-avoiding classes of A_B at (x, i), in index order, are assigned
to y ∈ B ∖ {x} in increasing label order, 4 each; the avoiding classes keep index order; the FDH
frame classes missing the group of y keep index order.  Output: GCDCQS certificate (exclusive create).
Usage: build_c23.py FG.json GCDCQS8.txt FDH.txt OUT.txt"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import read_cert  # noqa: E402
from check_ingredients import read_fdh  # noqa: E402


def main():
    fgp, gcp, fdhp, out = sys.argv[1:5]
    fg = json.load(open(fgp))
    groups = [sorted(g) for g in fg["groups"]]
    u = {p: gi for gi, g in enumerate(groups) for p in g}
    w = {p: g.index(p) for g in groups for p in g}
    lab = lambda p, i: 32 * u[p] + 8 * w[p] + i
    Bs = [sorted(b) for b in fg["B"]]
    Ts = [sorted(t) for t in fg["T"]]
    header, head, ggroups, gblocks, gcol = read_cert(gcp)
    assert head["GCDCQS"] == [32, 4, 8] and [list(x) for x in ggroups] == [list(range(8 * t, 8 * t + 8)) for t in range(4)]
    fgroups, fblocks, fcol = read_fdh(fdhp)
    assert [list(x) for x in fgroups] == [list(range(8 * s, 8 * s + 8)) for s in range(5)]
    blocks = set()
    # A_B
    Bmap = []
    for B in Bs:
        Bt = {u[p]: p for p in B}
        assert sorted(Bt) == [0, 1, 2, 3], "a B-block does not meet every group once"
        mp = {8 * t + i: lab(Bt[t], i) for t in range(4) for i in range(8)}
        Bmap.append((B, Bt, mp))
        for b in gblocks:
            blocks.add(tuple(sorted(mp[q] for q in b)))
    Tmap = []
    for T in Ts:
        mp = {8 * s + i: lab(T[s], i) for s in range(5) for i in range(8)}
        Tmap.append((T, mp))
        for b in fblocks:
            blocks.add(tuple(sorted(mp[q] for q in b)))
    assert len(blocks) == 16 * len(gblocks) + 48 * len(fblocks) == 80384, len(blocks)
    col = {}
    for x in range(16):
        for i in range(8):
            P = lab(x, i)
            Fyj = {(y, j): [] for y in range(16) if y != x for j in range(4)}
            Fj = {j: [] for j in range(4)}
            for B, Bt, mp in Bmap:
                if x not in B:
                    continue
                c = 8 * u[x] + i
                hole = {8 * u[x] + k for k in range(8)} - {c}
                classes = gcol[c]
                avoid = [C for C in classes if not any(q in hole for t in C for q in t)]
                non = [C for C in classes if any(q in hole for t in C for q in t)]
                assert len(avoid) == 4 and len(non) == 12
                others = sorted(p for p in B if p != x)
                for k, C in enumerate(non):
                    y, j = others[k // 4], k % 4
                    Fyj[(y, j)] += [tuple(sorted(mp[q] for q in t)) for t in C]
                for j, C in enumerate(avoid):
                    Fj[j] += [tuple(sorted(mp[q] for q in t)) for t in C]
            for T, mp in Tmap:
                if x not in T:
                    continue
                s = T.index(x)
                c = 8 * s + i
                seen = {}
                for C in fcol[c]:
                    gs = {q // 8 for t in C for q in t}
                    smiss = ({0, 1, 2, 3, 4} - gs - {s}).pop()
                    y = T[smiss]
                    j = seen.get(y, 0)
                    seen[y] = j + 1
                    Fyj[(y, j)] += [tuple(sorted(mp[q] for q in t)) for t in C]
                assert sorted(seen.values()) == [4, 4, 4, 4]
            ordered = [sorted(Fyj[(y, j)]) for y in sorted({k[0] for k in Fyj}) for j in range(4)]
            ordered += [sorted(Fj[j]) for j in range(4)]
            col[P] = ordered
    assert sorted(col) == list(range(128))
    certsha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
    L = [f"# gcDCQS(32^4:0) by Tan-Zhou Construction 2.3 (m,g,n,s)=(8,4,4,0) from 1-FG {certsha(fgp)}, "
         f"gcDCQS(8^4:0) {certsha(gcp)}, FDH(5,8,4,3) {certsha(fdhp)}",
         "GCDCQS 128 4 32", "COLOURS 64", "HOLEFREE 16", "GROUPS"]
    L += [" ".join(str(32 * g + k) for k in range(32)) for g in range(4)]
    L.append("BLOCKS")
    L += [" ".join(map(str, b)) for b in sorted(blocks)]
    for P in range(128):
        L.append(f"POINT {P}")
        for j, C in enumerate(col[P]):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in C]
    text = "\n".join(L) + "\n"
    with xopen(out) as fh:
        fh.write(text)
    print(out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "blocks", len(blocks))


if __name__ == "__main__":
    main()
