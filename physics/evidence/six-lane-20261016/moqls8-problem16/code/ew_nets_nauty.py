"""Canonical certificates (nauty via pynauty, lane venv env/venv8) of the point-line incidence graphs of the 39 E–W
5-nets: vertices 0..63 points, 64..103 lines (colour classes: points | lines). Equal certificates <=> isomorphic
incidence structures <=> isomorphic nets (parallel classes are recovered from disjointness, so class permutations
are included). Positive controls: randomly relabelled copies (points, lines within classes, classes) of every net
must reproduce its certificate. Also reports automorphism group orders.
env/venv8/bin/python -B ew_nets_nauty.py --nets ../evidence/k2_fixed/ew_nets.json --out ../evidence/k2_fixed/nauty.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random

import pynauty

N = 8


def graph(sqs, rng=None):
    cells = [(i, j) for i in range(N) for j in range(N)]
    lab = [lambda c: c[0], lambda c: c[1]] + [(lambda L: (lambda c: L[c[0]][c[1]]))(L) for L in sqs]
    pid = list(range(64))
    cperm = list(range(5))
    lperm = [list(range(N)) for _ in range(5)]
    if rng:
        rng.shuffle(pid)
        rng.shuffle(cperm)
        for q in lperm:
            rng.shuffle(q)
    adj = {v: [] for v in range(104)}
    for k, c in enumerate(cells):
        p = pid[k]
        for cl in range(5):
            line = 64 + cperm[cl] * N + lperm[cl][lab[cl](c)]
            adj[p].append(line)
            adj[line].append(p)
    g = pynauty.Graph(104, directed=False, adjacency_dict=adj,
                      vertex_coloring=[set(range(64)), set(range(64, 104))])
    return g


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    nets = json.load(open(a.nets))["nets"]
    rng = random.Random(1017)
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "pynauty": pynauty.__version__, "nets": {}}
    certs = {}
    for item in nets:
        g = graph(item["squares"])
        cert = pynauty.certificate(g)
        aut = pynauty.autgrp(g)
        g2 = graph(item["squares"], rng)
        ctrl = pynauty.certificate(g2) == cert
        certs[item["tag"]] = cert
        res["nets"][item["tag"]] = {"cert_sha256": hashlib.sha256(cert).hexdigest(), "aut_order": aut[1] * 10 ** aut[2],
                                    "relabelled_copy_same_cert": ctrl}
        print(json.dumps({"net": item["tag"], **res["nets"][item["tag"]]}), flush=True)
    res["distinct_certificates"] = len(set(certs.values()))
    res["all_controls_ok"] = all(v["relabelled_copy_same_cert"] for v in res["nets"].values())
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("distinct_certificates", "all_controls_ok")}))


if __name__ == "__main__":
    main()
