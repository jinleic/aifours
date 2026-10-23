#!/usr/bin/env python3
"""README E10: explicit mcDSQS(80) by Tan–Zhou Construction 2.1 (g = 20, n = 4, s = 0) from a
GCDCQS certificate and the transcribed Shi–Xia–Krotov Prop. 3 mcDSQS(20) (standard library only).
* SQS(20): the 16 transcribed base blocks and all cyclic shifts mod 20; checked to be an SQS(20);
* its derived STS(19) at 0 is checked to be partitioned by the 10 transcribed cells into partial
  parallel classes; the colouring at a is cells + a (checked against the derived design at a);
* blocks: the 19400 GCDCQS blocks + the SQS(20) on every group G_i (a -> 20i + a);
* at x = 20i + a: the k-th hole-avoiding class of the GCDCQS colouring at x (index order) gets the
  k-th SQS(20) class at a (mapped into G_i); the other classes are kept; indices unchanged.
Writes the MCDSQS certificate (exclusive create) and prints its sha256.
Usage: build_mcdsqs80.py GCDCQS_CERT TRANSCRIPTION.json OUT.txt"""
import hashlib
import json
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import read_cert  # noqa: E402


def sqs20_from_transcription(tr):
    base = [tuple(b) for b in tr["base_blocks"]]
    blocks = {tuple(sorted((p + i) % 20 for p in b)) for b in base for i in range(20)}
    assert len(blocks) == 20 * 19 * 18 // 24, f"{len(blocks)} blocks, expected 285"
    cover = {}
    for b in blocks:
        for t in combinations(b, 3):
            cover[t] = cover.get(t, 0) + 1
    assert set(cover) == set(combinations(range(20), 3)) and set(cover.values()) == {1}, "not an SQS(20)"
    return sorted(blocks)


def derived(blocks, x):
    return {tuple(p for p in b if p != x) for b in blocks if x in b}


def check_colouring(der, classes, k):
    seen = set()
    for C in classes:
        pts = [p for t in C for p in t]
        assert len(pts) == len(set(pts)), "class is not a partial parallel class"
        for t in C:
            assert t in der and t not in seen, "cell triple not derived or repeated"
            seen.add(t)
    assert seen == der and len(classes) == k, "cells do not partition the derived design"


def main():
    certp, trp, out = sys.argv[1:4]
    tr = json.load(open(trp))
    S = sqs20_from_transcription(tr)
    cells = [[tuple(sorted(t)) for t in C] for C in tr["cells"]]
    check_colouring(derived(S, 0), cells, 10)
    Q = {}
    for a in range(20):
        Q[a] = [[tuple(sorted((p + a) % 20 for p in t)) for t in C] for C in cells]
        check_colouring(derived(S, a), Q[a], 10)
    header, head, groups, blocks, col = read_cert(certp)
    v, n, g = head["GCDCQS"]
    assert (v, n, g) == (80, 4, 20) and head["COLOURS"] == [40] and head["HOLEFREE"] == [10]
    assert [list(G) for G in groups] == [list(range(20 * i, 20 * i + 20)) for i in range(4)]
    allblocks = sorted(set(blocks) | {tuple(20 * i + p for p in b) for i in range(4) for b in S})
    assert len(allblocks) == 19400 + 4 * 285
    certsha = hashlib.sha256(open(certp, "rb").read()).hexdigest()
    trsha = hashlib.sha256(open(trp, "rb").read()).hexdigest()
    L = [f"# mcDSQS(80) by Tan-Zhou Construction 2.1 (g=20, n=4, s=0) from GCDCQS sha256 {certsha}",
         f"# and the Shi-Xia-Krotov Prop. 3 cyclic SQS(20) II.A.1 with its 10-colouring (transcription sha256 {trsha})",
         "MCDSQS 80", "COLOURS 40", "BLOCKS"]
    L += [" ".join(map(str, b)) for b in allblocks]
    for x in range(80):
        i, a = divmod(x, 20)
        hole = set(range(20 * i, 20 * i + 20)) - {x}
        classes = [list(C) for C in col[x]]
        avoid = [j for j, C in enumerate(classes) if not any(set(t) & hole for t in C)]
        assert len(avoid) == 10, f"point {x}: {len(avoid)} hole-avoiding classes"
        for k, j in enumerate(avoid):
            classes[j] = classes[j] + [tuple(20 * i + p for p in t) for t in Q[a][k]]
        L.append(f"POINT {x}")
        for j, C in enumerate(classes):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in sorted(tuple(sorted(t)) for t in C)]
    text = "\n".join(L) + "\n"
    with xopen(out) as fh:
        fh.write(text)
    print(out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "blocks", len(allblocks))


if __name__ == "__main__":
    main()
