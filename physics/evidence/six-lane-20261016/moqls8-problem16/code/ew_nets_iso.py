"""Direct isomorphism test (networkx VF2++) of point-line incidence graphs for the pairs of E–W 5-nets that the
invariants of ew_nets_inv3.py do not separate. Incidence graph: 64 point nodes + 40 line nodes, node attribute
'kind' preserved; a type-preserving isomorphism is exactly a net isomorphism (parallel classes are recovered as
the classes of pairwise disjoint lines). Positive control: each net against a randomly relabelled copy of itself
(points permuted, lines of each class permuted, classes permuted) must be isomorphic.
python -B ew_nets_iso.py --nets ../evidence/k2_fixed/ew_nets.json --inv3 ../evidence/k2_fixed/ew_nets_inv3.json \\
       --out ../evidence/k2_fixed/ew_nets_iso.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random

import networkx as nx

N = 8


def incidence(sqs, perm_points=None, perm_classes=None, perm_lines=None):
    cells = [(i, j) for i in range(N) for j in range(N)]
    cls = [lambda c: c[0], lambda c: c[1]] + [(lambda L: (lambda c: L[c[0]][c[1]]))(L) for L in sqs]
    G = nx.Graph()
    for c in cells:
        pc = perm_points[c] if perm_points else c
        G.add_node(("p", pc), kind="p")
    for k in range(5):
        for x in range(N):
            kk = perm_classes[k] if perm_classes else k
            xx = perm_lines[k][x] if perm_lines else x
            G.add_node(("l", kk, xx), kind="l")
    for c in cells:
        pc = perm_points[c] if perm_points else c
        for k in range(5):
            kk = perm_classes[k] if perm_classes else k
            xx = perm_lines[k][cls[k](c)] if perm_lines else cls[k](c)
            G.add_edge(("p", pc), ("l", kk, xx))
    return G


def iso(G1, G2):
    return nx.vf2pp_is_isomorphic(G1, G2, node_label="kind")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--inv3", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = {x["tag"]: x["squares"] for x in json.load(open(a.nets))["nets"]}
    coll = json.load(open(a.inv3))["collisions"]
    rng = random.Random(20261017)
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "networkx": nx.__version__,
           "pairs": [], "controls": []}
    for group in coll:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                t1, t2 = group[i], group[j]
                r = iso(incidence(d[t1]), incidence(d[t2]))
                res["pairs"].append({"a": t1, "b": t2, "isomorphic": r})
                print(json.dumps(res["pairs"][-1]), flush=True)
    for t in sorted({t for g in coll for t in g}):
        cells = [(i, j) for i in range(N) for j in range(N)]
        sh = cells[:]
        rng.shuffle(sh)
        pp = dict(zip(cells, sh))
        pc = list(range(5))
        rng.shuffle(pc)
        pl = []
        for _ in range(5):
            q = list(range(N))
            rng.shuffle(q)
            pl.append(q)
        r = iso(incidence(d[t]), incidence(d[t], pp, pc, pl))
        res["controls"].append({"net": t, "isomorphic_to_relabelled_self": r})
        print(json.dumps(res["controls"][-1]), flush=True)
    res["all_pairs_nonisomorphic"] = not any(p["isomorphic"] for p in res["pairs"])
    res["all_controls_isomorphic"] = all(c["isomorphic_to_relabelled_self"] for c in res["controls"])
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("all_pairs_nonisomorphic", "all_controls_isomorphic")}))


if __name__ == "__main__":
    main()
