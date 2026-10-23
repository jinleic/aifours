#!/usr/bin/env python3
"""Read-only structure statistics of the colouring at POINT x of a GCDCQS certificate (stdlib):
per class: avoiding?, size, vertical / skew hole triples, transversal / 2+1 hole-free triples,
number of missed non-hole points and the groups of the missed points; aggregated counts.
Usage: colouring_structure.py CERT [X] [OUT.json]"""
import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import read_cert  # noqa: E402


def main():
    cert = sys.argv[1]
    x = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    header, head, groups, blocks, col = read_cert(cert)
    v, n, g = head["GCDCQS"]
    gof = {p: i for i, G in enumerate(groups) for p in G}
    hole = {p for p in groups[gof[x]] if p != x}
    nonhole = [p for p in range(v) if gof[p] != gof[x]]
    rows = []
    for j, C in enumerate(col[x]):
        cov = {p for t in C for p in t}
        vert = skew = trans = tw = 0
        for t in C:
            hs = [p for p in t if p in hole]
            rest = [gof[p] for p in t if p not in hole]
            if hs:
                if rest[0] == rest[1]:
                    vert += 1
                else:
                    skew += 1
            elif len(set(rest)) == 3:
                trans += 1
            else:
                tw += 1
        missed = [p for p in nonhole if p not in cov]
        rows.append({"class": j, "avoiding": not (cov & hole), "size": len(C), "vertical": vert, "skew": skew,
                     "transversal": trans, "two_one": tw, "missed": len(missed),
                     "missed_groups": sorted(collections.Counter(gof[p] for p in missed).values(), reverse=True)})
    agg = collections.Counter()
    for r in rows:
        key = ("A" if r["avoiding"] else "N") + f" size{r['size']} v{r['vertical']} s{r['skew']} t{r['transversal']} w{r['two_one']} miss{r['missed']}"
        agg[key] += 1
    rec = {"certificate": cert, "x": x, "classes": rows, "patterns": dict(sorted(agg.items()))}
    if len(sys.argv) > 3:
        with xopen(sys.argv[3]) as fh:
            json.dump(rec, fh, indent=1)
    for k, c in sorted(agg.items()):
        print(c, "x", k)


if __name__ == "__main__":
    main()
