#!/usr/bin/env python3
"""Mutation controls for checker B's outer replay (cells_iv.py), applied IN MEMORY to a copy of
one tree JSON (no mutated files are written).  Usage:

  mutants_iv.py TREE.json --baseline evidence/cells_iv_coneXX.json --which y_min,y_first,mu_far,lstar,del,r0
                [--out evidence/mutants_coneXX.json]

Mutations (each must be rejected, or a harmless perturbation explained):
  y_min   : the D leaf with the baseline minimum margin; its largest |y_e| multiplied by 1.1
  y_first : the first D leaf in preorder; its largest |y_e| multiplied by 1.1
  mu_far  : the first D leaf; mu0^u of the class u with the largest min-vertex n^u replaced by
            the far point (2^10, 2^-10, 2^-10, 2^10)
  lstar   : no tree change; L* replaced by L* - 1/50
  del     : the subtree rooted at the S node with subtree size 3 nearest the middle of the list
            is deleted
  r0      : the tree's 'r0' replaced by '1/20000' (C leaves would still lie in the certified box,
            but the trusted constant must match exactly)
"""
import argparse
import copy
import itertools
import json
import os
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cb_common as cb  # noqa: E402
import cells_iv as cv  # noqa: E402
from mpmath import iv, mp  # noqa: E402


def subtree_end(tree, p):
    need, q = 1, p
    while need:
        node = tree[q]
        q += 1
        need -= 1
        if node[0] == "S":
            need += 2
    return q


def leaf_positions(tree):
    return [p for p, n in enumerate(tree) if n[0] in ("C", "D")]


def vertices_at(data, target):
    """Exact vertices of the cell of node position `target` (structure walk only)."""
    fi, fj = data["facet"]
    root = [(Fr(1, 9),) * 4]
    for sig in itertools.permutations(range(3)):
        if sig[fi] != fj:
            root.append(tuple(Fr(int(x), 3) for x in (sig[0] == 0, sig[0] == 1, sig[1] == 0, sig[1] == 1)))
    tree, pos, stack = data["tree"], 0, [root]
    while stack:
        verts = stack.pop()
        node = tree[pos]
        if pos == target:
            return verts
        pos += 1
        if node[0] == "S":
            i, j = node[1], node[2]
            mid = tuple((a + b) / 2 for a, b in zip(verts[i], verts[j]))
            c1, c2 = list(verts), list(verts)
            c1[i], c2[j] = mid, mid
            stack.append(c2)
            stack.append(c1)
    raise ValueError("target not reached")


def scale_largest_y(node, factor):
    ys = [float.fromhex(s) for s in node[1]]
    e = max(range(18), key=lambda i: abs(ys[i]))
    old = ys[e]
    node[1][e] = float.hex(old * factor)
    return {"edge": e, "old": float.hex(old), "new": node[1][e]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tree")
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--which", default="y_min,y_first,mu_far,lstar,del,r0")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    iv.prec = 128
    mp.prec = 128
    assert cb.check_spectra() and cv.check_closed_forms()
    cand, _ = cv.convex_certificate()
    cv.verify_vertex_set(cand)
    with open(a.tree) as f:
        data = json.load(f)
    with open(a.baseline) as f:
        base = json.load(f)
    bres = [r for r in base["results"] if os.path.basename(r["file"]) == os.path.basename(a.tree)][0]
    tree = data["tree"]
    leaves = leaf_positions(tree)
    d_leaves = [p for p in leaves if tree[p][0] == "D"]
    out = {"tree": a.tree, "sha256": cv.sha256(a.tree), "baseline_min_margin": bres["min_margin"],
           "baseline_min_margin_leaf_index": bres["min_margin_leaf_index"], "mutants": []}
    for which in a.which.split(","):
        t0 = time.time()
        mdata = {k: v for k, v in data.items() if k != "tree"}
        mtree = list(tree)          # shallow copy; mutated nodes are deep-copied below
        shift = Fr(0)
        info = {}
        if which in ("y_min", "y_first", "mu_far"):
            p = leaves[bres["min_margin_leaf_index"]] if which == "y_min" else d_leaves[0]
            node = copy.deepcopy(tree[p])
            info["node_pos"] = p
            if which.startswith("y_"):
                info.update(scale_largest_y(node, 1.1))
            else:
                verts = vertices_at(data, p)
                nv = [cb.nine_values(v) for v in verts]
                u = max(range(9), key=lambda c: min(x[c] for x in nv))
                info.update({"class": u, "old": node[2][u],
                             "min_vertex_n_u": str(min(x[u] for x in nv))})
                node[2][u] = [float.hex(2.0 ** 10), float.hex(2.0 ** -10), float.hex(2.0 ** -10), float.hex(2.0 ** 10)]
                info["new"] = node[2][u]
            mtree[p] = node
        elif which == "lstar":
            shift = Fr(1, 50)
            info["lstar_shift"] = "1/50"
        elif which == "del":
            sizes = [(abs(p - len(tree) // 2), p) for p, n in enumerate(tree)
                     if n[0] == "S" and subtree_end(tree, p) - p == 3]
            p = min(sizes)[1]
            q = subtree_end(tree, p)
            info.update({"deleted_nodes": [p, q], "deleted": tree[p:q][:1] + [tree[x][0] for x in range(p + 1, q)]})
            mtree = tree[:p] + tree[q:]
        elif which == "r0":
            mdata["r0"] = "1/20000"
            info["r0"] = {"old": data["r0"], "new": "1/20000"}
        else:
            raise SystemExit(f"unknown mutation {which}")
        mdata["tree"] = mtree
        rep = cv.Replayer(cand, shift)
        r = rep.replay(mdata)
        summary = {"mutation": which, "info": info, "PASS": r["PASS"], "rejected": not r["PASS"],
                   "structure_error": r["structure_error"], "failed_leaves": r["failed_leaves"],
                   "invalid_leaves": r["invalid_leaves"], "min_margin": r["min_margin"],
                   "min_margin_leaf_index": r["min_margin_leaf_index"], "first_failures": r["failures"][:5],
                   "nodes_read": r["nodes"], "runtime_s": round(time.time() - t0, 2)}
        print(json.dumps(summary), flush=True)
        out["mutants"].append(summary)
    if a.out:
        with open(a.out, "w") as f:
            f.write(json.dumps(out, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
