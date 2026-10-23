#!/usr/bin/env python3
"""README C: explicit mcDSQS(74) by Tan–Zhou Construction 2.1 (LF 292–335, ≡ 2 mod 6 branch) with
(g, n, s) = (18, 4, 2), from a Format S gcDCQS(18^4 : 2) and the transcribed Shi–Xia–Krotov cyclic mcDSQS(20)
(sources/sxk/sxk_prop3_transcription.json: 16 base blocks under Z20 and 10 cells partitioning the derived
STS(19) at 0).  Standard library only; every intermediate claim is asserted, and the output is checked by the
copied definition-first mcDSQS checkers, not by this script.
* SQS(20): base blocks + all shifts mod 20, checked to be an SQS(20); at EVERY a in Z20 the 10 cells + a are
  checked to be partial parallel classes partitioning the derived STS(19) at a;
* local copies: for each group G_k (GROUPS order) the map t -> G_k[t] (t < 18), 18 -> first stem point,
  19 -> second stem point; the image of the SQS(20) is an SQS(20) on G_k ∪ S;
* blocks: the gcDCQS blocks + the four local copies (16206 = C(74,3)/4 blocks);
* group point x = G_k[t]: the 10 classes of the gcDCQS colouring at x avoiding (G_k ∪ S)∖{x} (index order) are
  merged with the 10 local classes (cells + t) in order, the other 27 classes are kept;
* stem point α: for each k, the 9 frame classes missing G_k (listed order) are merged with the 9 local classes at α
  in copy k that contain the other stem point (cells order); the remaining local class of each copy (which avoids
  the other stem point, a partial parallel class of G_k) is united over k into one class: 36 + 1 = 37 classes.
Writes the MCDSQS certificate (exclusive create) and prints its sha256.
Usage: build_mcdsqs74.py GCDCQS_S_CERT SXK_TRANSCRIPTION.json OUT.txt"""
import hashlib
import json
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402


def read_s(path):
    lines = [l.split("#", 1)[0].split() for l in open(path)]
    lines = [l for l in lines if l]
    head = lines[0]
    assert head[0] == "GCDCQS" and [int(z) for z in head[1:]] == [74, 4, 18, 2]
    assert lines[1] == ["COLOURS", "37"] and lines[2] == ["HOLEFREE", "10"] and lines[3] == ["GROUPS"]
    groups = [[int(z) for z in lines[4 + i]] for i in range(4)]
    assert lines[8] == ["STEM"]
    stem = [int(z) for z in lines[9]]
    assert lines[10] == ["BLOCKS"]
    pos, blocks = 11, []
    while lines[pos][0] not in ("POINT", "STEMPOINT"):
        blocks.append(tuple(sorted(int(z) for z in lines[pos])))
        pos += 1
    col, frames, cur, kind = {}, {}, None, None
    for tk in lines[pos:]:
        if tk[0] == "POINT":
            cur, kind = int(tk[1]), "P"
            col[cur] = []
        elif tk[0] == "STEMPOINT":
            cur, kind = int(tk[1]), "S"
            frames[cur] = []
        elif tk[0] == "CLASS":
            col[cur].append([])
        elif tk[0] == "FRAME":
            frames[cur].append((int(tk[1]), []))
        elif kind == "P":
            col[cur][-1].append(tuple(sorted(int(z) for z in tk)))
        else:
            frames[cur][-1][1].append(tuple(sorted(int(z) for z in tk)))
    return groups, stem, blocks, col, frames


def main():
    certp, trp, out = sys.argv[1:4]
    tr = json.load(open(trp))
    base = [tuple(b) for b in tr["base_blocks"]]
    S20 = sorted({tuple(sorted((p + i) % 20 for p in b)) for b in base for i in range(20)})
    assert len(S20) == 285, f"{len(S20)} blocks, expected 285"
    cover = {}
    for b in S20:
        for t in combinations(b, 3):
            cover[t] = cover.get(t, 0) + 1
    assert set(cover) == set(combinations(range(20), 3)) and set(cover.values()) == {1}, "not an SQS(20)"
    cells = [[tuple(sorted(t)) for t in C] for C in tr["cells"]]
    loc = {}
    for a in range(20):
        der = {tuple(p for p in b if p != a) for b in S20 if a in b}
        Q = [[tuple(sorted((p + a) % 20 for p in t)) for t in C] for C in cells]
        seen = set()
        for C in Q:
            pts = [p for t in C for p in t]
            assert len(pts) == len(set(pts)), "cell is not a partial parallel class"
            for t in C:
                assert t in der and t not in seen, "cell triple not derived or repeated"
                seen.add(t)
        assert seen == der and len(Q) == 10, "cells do not partition the derived STS(19)"
        loc[a] = Q
    groups, stem, blocks, col, frames = read_s(certp)
    assert len(blocks) == 15066 and sorted(p for G in groups for p in G) + sorted(stem) == sorted(range(74))
    maps = []
    for G in groups:
        mp = {t: G[t] for t in range(18)}
        mp[18], mp[19] = stem[0], stem[1]
        maps.append(mp)
    local = set()
    for mp in maps:
        local |= {tuple(sorted(mp[p] for p in b)) for b in S20}
    allblocks = sorted(set(blocks) | local)
    assert len(allblocks) == 16206 == 74 * 73 * 72 // 24, f"{len(allblocks)} blocks"
    newcol = {}
    for k, G in enumerate(groups):
        mp = maps[k]
        hole_base = set(G) | set(stem)
        for t, x in enumerate(G):
            classes = [list(C) for C in col[x]]
            assert len(classes) == 37
            hole = hole_base - {x}
            avoid = [j for j, C in enumerate(classes) if not any(set(tr_) & hole for tr_ in C)]
            assert len(avoid) == 10, f"point {x}: {len(avoid)} hole-avoiding classes"
            for i, j in enumerate(avoid):
                classes[j] = classes[j] + [tuple(sorted(mp[p] for p in tr_)) for tr_ in loc[t][i]]
            newcol[x] = classes
    for si, al in enumerate(stem):
        other = stem[1 - si]
        lab_al = 18 + si
        fr = frames[al]
        assert len(fr) == 36
        merged, last = [], []
        for k in range(4):
            mp = maps[k]
            Fk = [C for kk, C in fr if kk == k]
            assert len(Fk) == 9, f"stem {al}: {len(Fk)} frame classes missing group {k}"
            Lk = [[tuple(sorted(mp[p] for p in tr_)) for tr_ in C] for C in loc[lab_al]]
            with_other = [C for C in Lk if any(other in tr_ for tr_ in C)]
            without = [C for C in Lk if not any(other in tr_ for tr_ in C)]
            assert len(with_other) == 9 and len(without) == 1, "local colouring at the stem: other stem not missed exactly once"
            for F, C in zip(Fk, with_other):
                merged.append(list(F) + list(C))
            last += without[0]
        newcol[al] = merged + [last]
    certsha = hashlib.sha256(open(certp, "rb").read()).hexdigest()
    trsha = hashlib.sha256(open(trp, "rb").read()).hexdigest()
    L = [f"# mcDSQS(74) by Tan-Zhou Construction 2.1 (g=18, n=4, s=2) from gcDCQS(18^4:2) sha256 {certsha}",
         f"# and the Shi-Xia-Krotov Prop. 3 cyclic mcDSQS(20) (transcription sha256 {trsha}) on every G_k ∪ S",
         "MCDSQS 74", "COLOURS 37", "BLOCKS"]
    L += [" ".join(map(str, b)) for b in allblocks]
    prof = set()
    for x in range(74):
        L.append(f"POINT {x}")
        cl = newcol[x]
        assert len(cl) == 37
        prof.add(tuple(sorted((len(C) for C in cl), reverse=True)))
        for j, C in enumerate(cl):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in sorted(tuple(sorted(t)) for t in C)]
    text = "\n".join(L) + "\n"
    with xopen(out) as fh:
        fh.write(text)
    print(out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "blocks", len(allblocks),
          "profiles", sorted(" ".join(f"{z}^{p.count(z)}" for z in sorted(set(p), reverse=True)) for p in prof))


if __name__ == "__main__":
    main()
