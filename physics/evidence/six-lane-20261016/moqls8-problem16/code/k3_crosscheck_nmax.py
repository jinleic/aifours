"""Cross-check (parent item 7): deleting one class from each of the 39 E–W 5-nets (3-MOLS(8)) gives 195 4-nets
(2-MOLS(8) after regridding); their nauty canonical classes must be exactly the 38 non-maximal 2-MOLS(8) classes of
nmaxMOLS8.2.txt (a 2-MOLS set is non-maximal iff its 4-net is a 4-subnet of some 5-net). Incidence graphs: points and
lines, only the two vertex classes {points}, {lines} distinguished.
env/venv8/bin/python -B k3_crosscheck_nmax.py --nets3 ../evidence/k2_fixed/ew_nets.json --out ../evidence/k3_fixed/crosscheck_nmax.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os

import pynauty

HERE = os.path.dirname(os.path.abspath(__file__))
N = 8


def incidence_cert(classes):
    """classes: list of dicts cell -> line index (one dict per parallel class)."""
    cells = sorted(classes[0])
    K = len(classes)
    V = 64 + K * N
    adj = {v: [] for v in range(V)}
    for idx, c in enumerate(cells):
        for k, cl in enumerate(classes):
            line = 64 + k * N + cl[c]
            adj[idx].append(line)
            adj[line].append(idx)
    g = pynauty.Graph(V, directed=False, adjacency_dict=adj, vertex_coloring=[set(range(64)), set(range(64, V))])
    return hashlib.sha256(pynauty.certificate(g)).hexdigest()


def net_classes(sqs):
    cells = [(i, j) for i in range(N) for j in range(N)]
    cls = [{c: c[0] for c in cells}, {c: c[1] for c in cells}]
    for L in sqs:
        cls.append({c: L[c[0]][c[1]] for c in cells})
    return cls


def parse(path):
    lines = open(path).read().split("\n")
    n, k, m = (int(x) for x in lines[0].split()[:3])
    sq, cur = [], []
    for line in lines[1:]:
        s = line.strip()
        if not s:
            if cur:
                sq.append(cur)
                cur = []
            continue
        if len(s) != n or not all("a" <= ch <= "h" for ch in s):
            break
        cur.append([ord(ch) - 97 for ch in s])
    if cur:
        sq.append(cur)
    assert len(sq) == m
    return sq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets3", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    nets3 = json.load(open(a.nets3))["nets"]
    sub = {}
    for item in nets3:
        cls = net_classes(item["squares"])
        for d in range(5):
            cert = incidence_cert([c for k, c in enumerate(cls) if k != d])
            sub.setdefault(cert, []).append("%s-del%d" % (item["tag"], d))
    nmax = parse(os.path.join(HERE, "..", "sources", "ew_data", "nmaxMOLS8.2.txt"))
    cat = {}
    for s in range(len(nmax) // 2):
        cert = incidence_cert(net_classes(nmax[2 * s:2 * s + 2]))
        cat.setdefault(cert, []).append("nmax%04d" % s)
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "subnets_total": sum(len(v) for v in sub.values()), "subnet_classes": len(sub),
           "catalogue_nmax_classes": len(cat), "catalogue_nmax_entries": sum(len(v) for v in cat.values()),
           "sets_equal": set(sub) == set(cat),
           "subnet_classes_not_in_catalogue": [sub[k][:3] for k in set(sub) - set(cat)],
           "catalogue_classes_not_from_subnets": [cat[k] for k in set(cat) - set(sub)]}
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))
    if not res["sets_equal"] or res["subnet_classes"] != 38:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
