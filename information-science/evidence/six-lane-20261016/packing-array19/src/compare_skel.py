#!/usr/bin/env python3
"""Case-for-case comparison of the two A2 skeleton generators (gen_skel vs gen_skel_b):
each skeleton is turned into a bicoloured graph (P0 quads vs rows in >= 2 quads, plus the
number of rows in no quad as a graph attribute); the two lists must be in bijection under
isomorphism, and each list must be internally duplicate-free.
Usage (research venv): compare_skel.py MS_INDEX SKELDIR_A SKELDIR_B OUT_JSON
"""
import json
import os
import sys

import networkx as nx


def graph(c0, types, empty):
    G = nx.Graph()
    G.graph["empty"] = empty
    for v in range(c0):
        G.add_node(("q", v), kind="q")
    for j, t in enumerate(types):
        G.add_node(("r", j), kind="r%d" % len(t))
        for v in t:
            G.add_edge(("r", j), ("q", v))
    return G


def key(G):
    return (G.graph["empty"], G.number_of_edges(), G.number_of_nodes(),
            nx.weisfeiler_lehman_graph_hash(G, node_attr="kind", iterations=4))


def main():
    mi, da, db, out = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
    A = json.load(open(os.path.join(da, "skeletons-ms%02d.json" % mi)))
    B = json.load(open(os.path.join(db, "skeletons-b-ms%02d.json" % mi)))
    assert [list(p) for p in A["profiles"]] == [list(p) for p in B["profiles"]] or \
        sorted(map(tuple, A["profiles"])) == sorted(map(tuple, B["profiles"]))
    c0 = A["c0"]
    ga = [graph(c0, [tuple(e) for e in s["edges"]] + [tuple(h) for h in s["hyper"]], s["empty"])
          for s in A["skeletons"]]
    gb = [graph(c0, [tuple(t) for t in s["types"]], s["empty"]) for s in B["skeletons"]]
    nm = lambda x, y: x["kind"] == y["kind"]  # noqa: E731
    buckets = {}
    for i, G in enumerate(gb):
        buckets.setdefault(key(G), []).append(i)
    hits_b = [0] * len(gb)
    hits_a = []
    mapping = []
    for G in ga:
        h = [i for i in buckets.get(key(G), []) if nx.is_isomorphic(G, gb[i], node_match=nm)]
        hits_a.append(len(h))
        mapping.append(h[0] if len(h) == 1 else None)
        for i in h:
            hits_b[i] += 1
    res = {"multiset_index": mi, "count_a": len(ga), "count_b": len(gb),
           "a_each_matched_once": all(x == 1 for x in hits_a),
           "b_each_matched_once": all(x == 1 for x in hits_b)}
    res["bijection"] = res["count_a"] == res["count_b"] and res["a_each_matched_once"] and res["b_each_matched_once"]
    res["a_to_b"] = mapping
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "a_to_b"}))


if __name__ == "__main__":
    main()
