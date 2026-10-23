"""2-dimensional Weisfeiler–Leman colour refinement on the point set of a 5-net (class labels NOT used, so the colour
multiset is invariant under every net isomorphism, including class permutations). Initial colour of an ordered point
pair (p,q): 0 if p = q, 1 if p, q are collinear, 2 otherwise. Refinement: colour(p,q) <- (colour(p,q), multiset over
r of (colour(p,r), colour(r,q))). Signatures are canonicalised through one dictionary shared by all nets in a round,
so equal final multisets are comparable across nets. Different stable multisets certify non-isomorphism.
python -B ew_nets_wl.py --nets ../evidence/k2_fixed/ew_nets.json --tags max00,max02,... --out ../evidence/k2_fixed/wl.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter

N = 8


def initial(sqs):
    cells = [(i, j) for i in range(N) for j in range(N)]
    lab = [lambda c: c[0], lambda c: c[1]] + [(lambda L: (lambda c: L[c[0]][c[1]]))(L) for L in sqs]
    P = len(cells)
    col = [[0] * P for _ in range(P)]
    for a in range(P):
        for b in range(P):
            if a == b:
                col[a][b] = 0
            else:
                col[a][b] = 1 if any(f(cells[a]) == f(cells[b]) for f in lab) else 2
    return col


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--tags", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rounds", type=int, default=4)
    a = ap.parse_args()
    nets = {x["tag"]: x["squares"] for x in json.load(open(a.nets))["nets"]}
    tags = a.tags.split(",")
    cols = {t: initial(nets[t]) for t in tags}
    P = N * N
    history = []
    for rnd in range(a.rounds):
        table = {}
        new = {}
        for t in tags:
            c = cols[t]
            nc = [[0] * P for _ in range(P)]
            for p in range(P):
                cp = c[p]
                for q in range(P):
                    sig = (c[p][q], tuple(sorted(Counter((cp[r], c[r][q]) for r in range(P)).items())))
                    if sig not in table:
                        table[sig] = len(table)
                    nc[p][q] = table[sig]
            new[t] = nc
        cols = new
        summary = {t: sorted(Counter(v for row in cols[t] for v in row).items()) for t in tags}
        history.append({"round": rnd + 1, "colours": len(table),
                        "multisets": {t: hashlib.sha256(json.dumps(summary[t]).encode()).hexdigest()[:16]
                                      for t in tags}})
        print(json.dumps(history[-1]), flush=True)
    final = history[-1]["multisets"]
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "tags": tags, "history": history,
           "pairs": []}
    pairs = [tuple(x.split(":")) for x in []]
    for i in range(0, len(tags), 2):
        if i + 1 < len(tags):
            res["pairs"].append({"a": tags[i], "b": tags[i + 1], "separated": final[tags[i]] != final[tags[i + 1]]})
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res["pairs"]))


if __name__ == "__main__":
    main()
