#!/usr/bin/env python3
"""README E11b: explicit mcDSQS(128) by Tan-Zhou Construction 2.1 (g = 32, n = 4, s = 0) from the
gcDCQS(32^4 : 0) certificate and the transcribed Tan-Zhou Appendix B cyclic mcDSQS(32) of Lemma 3.4
(standard library only; modelled on the gcdcqs20 lane's code/build_mcdsqs80.py).
* SQS(32): the transcribed base blocks and all their shifts mod 32; checked to be an SQS(32);
* at EVERY a in Z32 the 16 transcribed parts + a are checked to be partial parallel classes that
  partition the derived STS(31) of this SQS(32) at a (no reliance on the cyclic symmetry);
* blocks: the 80384 GCDCQS blocks + the SQS(32) on every group G_i (a -> 32i + a);
* at x = 32i + a: the classes of the GCDCQS colouring at x that contain no point of G_i \\ {x}
  (exactly 16, asserted), in index order; the k-th gets parts_k + a (mapped into G_i); the other 48
  classes are kept; class indices unchanged (Construction 2.1, s = 0).
Writes the MCDSQS certificate (exclusive create) and prints its sha256.
Usage: build_mcdsqs128.py GCDCQS_CERT TRANSCRIPTION.json OUT.txt"""
import hashlib
import json
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import read_cert  # noqa: E402

G, N = 32, 4
V = G * N


def sqs32_from_transcription(tr):
    base = [tuple(b) for b in tr["base_blocks"]]
    assert all(len(set(b)) == 4 and all(0 <= p < G for p in b) for b in base), "bad base block"
    blocks = {tuple(sorted((p + i) % G for p in b)) for b in base for i in range(G)}
    assert len(blocks) == G * (G - 1) * (G - 2) // 24, f"{len(blocks)} blocks, expected 1240"
    cover = {}
    for b in blocks:
        for t in combinations(b, 3):
            cover[t] = cover.get(t, 0) + 1
    assert set(cover) == set(combinations(range(G), 3)) and set(cover.values()) == {1}, "not an SQS(32)"
    return sorted(blocks)


def derived(blocks, x):
    return {tuple(p for p in b if p != x) for b in blocks if x in b}


def check_colouring(der, classes, k):
    seen = set()
    for C in classes:
        pts = [p for t in C for p in t]
        assert len(pts) == len(set(pts)), "class is not a partial parallel class"
        for t in C:
            assert t in der and t not in seen, "part triple not derived or repeated"
            seen.add(t)
    assert seen == der and len(classes) == k, "parts do not partition the derived design"


def main():
    certp, trp, out = sys.argv[1:4]
    tr = json.load(open(trp))
    S = sqs32_from_transcription(tr)
    parts = [[tuple(sorted(t)) for t in C] for C in tr["parts"]]
    Q = {}
    for a in range(G):
        Q[a] = [[tuple(sorted((p + a) % G for p in t)) for t in C] for C in parts]
        check_colouring(derived(S, a), Q[a], G // 2)
    header, head, groups, blocks, col = read_cert(certp)
    assert head.get("GCDCQS") == [V, N, G] and head.get("COLOURS") == [V // 2] and head.get("HOLEFREE") == [G // 2], \
        f"GCDCQS header {head}"
    assert [list(Gi) for Gi in groups] == [list(range(G * i, G * i + G)) for i in range(N)], "groups"
    local = {tuple(G * i + p for p in b) for i in range(N) for b in S}
    allblocks = sorted(set(blocks) | local)
    assert len(blocks) == 80384 and len(allblocks) == 80384 + N * len(S), f"{len(allblocks)} blocks"
    certsha = hashlib.sha256(open(certp, "rb").read()).hexdigest()
    trsha = hashlib.sha256(open(trp, "rb").read()).hexdigest()
    L = [f"# mcDSQS(128) by Tan-Zhou Construction 2.1 (g=32, n=4, s=0) from GCDCQS sha256 {certsha}",
         f"# and the Tan-Zhou arXiv:2503.11934v1 Appendix B (Lemma 3.4) cyclic mcDSQS(32) (transcription sha256 {trsha})",
         f"MCDSQS {V}", f"COLOURS {V // 2}", "BLOCKS"]
    L += [" ".join(map(str, b)) for b in allblocks]
    profiles = set()
    for x in range(V):
        i, a = divmod(x, G)
        hole = set(range(G * i, G * i + G)) - {x}
        classes = [list(C) for C in col[x]]
        assert len(classes) == V // 2, f"point {x}: {len(classes)} classes"
        avoid = [j for j, C in enumerate(classes) if not any(set(t) & hole for t in C)]
        assert len(avoid) == G // 2, f"point {x}: {len(avoid)} hole-avoiding classes"
        for k, j in enumerate(avoid):
            classes[j] = classes[j] + [tuple(G * i + p for p in t) for t in Q[a][k]]
        profiles.add(tuple(sorted((len(C) for C in classes), reverse=True)))
        L.append(f"POINT {x}")
        for j, C in enumerate(classes):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in sorted(tuple(sorted(t)) for t in C)]
    text = "\n".join(L) + "\n"
    with xopen(out) as fh:
        fh.write(text)
    print(out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "blocks", len(allblocks),
          "class_size_profiles", [" ".join(f"{s}^{p.count(s)}" for s in sorted(set(p), reverse=True)) for p in sorted(profiles)])


if __name__ == "__main__":
    main()
