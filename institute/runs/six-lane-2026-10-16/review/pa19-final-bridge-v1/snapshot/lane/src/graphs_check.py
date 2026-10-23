#!/usr/bin/env python3
"""Independent check of the geng list for the E0 split: all simple graphs on 8 vertices
with max degree <= 4 and 13..16 edges, up to isomorphism, generated from the networkx
graph atlas (all graphs on 7 vertices) by adding an 8th vertex in every possible way,
deduplicated with nx.is_isomorphic. Then matched one-to-one against the geng file.
Usage (research venv python): graphs_check.py GENG_FILE OUT_JSON
"""
import itertools
import json
import sys

import networkx as nx


def parse_g6(s):
    return nx.from_graph6_bytes(s.strip().encode())


def main():
    geng = [parse_g6(l) for l in open(sys.argv[1]) if l.strip()]
    reps = {}
    ncand = 0
    for H in nx.graph_atlas_g():
        if H.number_of_nodes() != 7 or (H.number_of_edges() and max(d for _, d in H.degree()) > 4):
            continue
        for k in range(0, 5):
            for S in itertools.combinations(range(7), k):
                if any(H.degree(v) + 1 > 4 for v in S):
                    continue
                m = H.number_of_edges() + k
                if not 13 <= m <= 16:
                    continue
                G = H.copy()
                G.add_node(7)
                G.add_edges_from((7, v) for v in S)
                ncand += 1
                key = (m, tuple(sorted(d for _, d in G.degree())),
                       nx.weisfeiler_lehman_graph_hash(G, iterations=3))
                bucket = reps.setdefault(key, [])
                if not any(nx.is_isomorphic(G, R) for R in bucket):
                    bucket.append(G)
    allreps = [R for b in reps.values() for R in b]
    by_edges = {}
    for R in allreps:
        by_edges[R.number_of_edges()] = by_edges.get(R.number_of_edges(), 0) + 1
    matched = [0] * len(geng)
    rep_hits = []
    for R in allreps:
        hits = [i for i, G in enumerate(geng) if G.number_of_edges() == R.number_of_edges()
                and nx.is_isomorphic(G, R)]
        rep_hits.append(len(hits))
        for i in hits:
            matched[i] += 1
    bij = (len(allreps) == len(geng) and all(x == 1 for x in matched)
           and all(h == 1 for h in rep_hits))
    out = {"candidates": ncand, "atlas_classes": len(allreps), "by_edges": by_edges,
           "geng_count": len(geng), "geng_each_matched_once": all(x == 1 for x in matched),
           "atlas_each_matched_once": all(h == 1 for h in rep_hits), "bijection": bij}
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
