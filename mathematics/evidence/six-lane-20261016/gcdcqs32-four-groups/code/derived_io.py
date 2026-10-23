#!/usr/bin/env python3
"""Export / assemble helpers for unrestricted colourings (README E3).

export  GROUP SUMMARY.json:SAMPLE X OUT.tri   -> derived design at X of the recorded KM solution:
        "V NTRIPLES R S" then "a b c holeflag" (original point labels; X itself unused)
assemble GROUP SUMMARY.json:SAMPLE X COLOURING OUT.cert
        -> reads "a b c colour" lines (colour 0..R-1; colours < S used only by hole-free triples),
           verifies the good colouring, transports it by the group (transitive groups only) and
           writes a GCDCQS certificate; then runs code/check_gcdcqs.py on it.
All writes are exclusive-create.
"""
import lane_guard  # noqa: F401

import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import xopen
from lanelib import closure, gcsts_params
from cqs_km import CQSKM
import colour_model as cm
import groups as grp
from pipeline import certificate_text, derived


def load_design(group, rows_from):
    path, idx = rows_from.rsplit(":", 1)
    src = json.load(open(path))
    g = src["g"]
    spec = grp.build(group, 4, g)
    assert src["group"] == group
    v = 4 * g
    km = CQSKM(v, spec["group_of"], spec["gens"])
    rows = src["samples"][int(idx)]["rows"]
    return spec, v, g, km.blocks_of(rows)


def main():
    mode = sys.argv[1]
    group, rows_from, x = sys.argv[2], sys.argv[3], int(sys.argv[4])
    spec, v, g, blocks = load_design(group, rows_from)
    r, s = gcsts_params(v - 1, g - 1)
    group_of = spec["group_of"]
    hole = {q for q in range(v) if group_of[q] == group_of[x] and q != x}
    der = derived(blocks, x)
    if mode == "export":
        with xopen(sys.argv[5]) as fh:
            fh.write(f"{v} {len(der)} {r} {s}\n")
            for t in der:
                fh.write(f"{t[0]} {t[1]} {t[2]} {1 if set(t) & hole else 0}\n")
        print("exported", len(der), "triples at", x)
        return
    assert mode == "assemble"
    colouring, out = sys.argv[5], sys.argv[6]
    classes = [[] for _ in range(r)]
    for line in open(colouring):
        a, b, c, k = map(int, line.split())
        classes[k].append(tuple(sorted((a, b, c))))
    classes = [sorted(C) for C in classes]
    pts = [q for q in range(v) if q != x]
    cm.verify_good_colouring(der, pts, sorted(hole), classes, r, s)
    G = closure(spec["gens"], v)
    col = {}
    for e in G:
        y = e[x]
        if y not in col:
            col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in classes]
    assert sorted(col) == list(range(v)), "group is not transitive (assemble supports transitive groups only)"
    text = certificate_text(v, 4, g, r, s, spec["groups"], blocks, col,
                            f"gcDCQS({g}^4:0) candidate: group {group} (order {len(G)}), design {rows_from}, "
                            f"unrestricted colouring at {x} from {os.path.basename(colouring)}")
    with xopen(out) as fh:
        fh.write(text)
    chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), out], capture_output=True, text=True)
    print("certificate", out, "sha256", hashlib.sha256(text.encode()).hexdigest(), "checker", json.loads(chk.stdout)["result"])


if __name__ == "__main__":
    main()
