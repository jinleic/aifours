"""Independent coverage audit for a leaf record (leaves.txt.gz) produced by a certified branch-and-bound run.

Uses ONLY the spec geometry (region, initial_split, split rule) and the leaf lines; does not evaluate any test.
Checks, per initial cell, that the leaf paths (in file order) are exactly the leaves of a depth-first traversal of a
binary tree in which every internal node has both children, i.e. the leaf boxes tile the cell with disjoint interiors.
Also checks: every cell appears, outcomes are in the allowed set, no FAIL. Rebuilds exact rational boxes for a
deterministic sample (every k-th leaf) and writes them for independent re-evaluation.
argv[1] = run directory (output), argv[2] = spec, argv[3] = leaves.txt.gz, argv[4] = comma-separated allowed outcomes,
argv[5] = variable names in order (comma-separated, matching spec["region"] keys), argv[6] = sample stride.
Writes cover.json and sample_boxes.txt (exclusive create).
"""
import sys
import json
import gzip
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
from fractions import Fraction  # noqa: E402

RUN, specp, leafp = sys.argv[1], sys.argv[2], sys.argv[3]
allowed = set(sys.argv[4].split(","))
names = sys.argv[5].split(",")
stride = int(sys.argv[6])
spec = json.load(open(specp))


def F(x):
    return Fraction(str(x))


reg = [(F(spec["region"][k][0]), F(spec["region"][k][1])) for k in names]
nsplit = [spec["initial_split"][k] for k in names]
wts = [F(w) for w in spec["split_weights"]]
ncells = nsplit[0] * nsplit[1] * nsplit[2]


def cell_box(ci):
    i, rem = divmod(ci, nsplit[1] * nsplit[2])
    j, k = divmod(rem, nsplit[2])
    idx = (i, j, k)
    return tuple((reg[d][0] + (reg[d][1] - reg[d][0]) * idx[d] / nsplit[d],
                  reg[d][0] + (reg[d][1] - reg[d][0]) * (idx[d] + 1) / nsplit[d]) for d in range(3))


def split_dim(box):
    sc = [(box[i][1] - box[i][0]) * wts[i] for i in range(3)]
    best = 0
    for i in (1, 2):
        if sc[i] > sc[best]:
            best = i
    return best


def box_of(ci, path):
    box = list(cell_box(ci))
    for ch in path:
        i = split_dim(tuple(box))
        lo, hi = box[i]
        mid = (lo + hi) / 2
        box[i] = (lo, mid) if ch == "0" else (mid, hi)
    return tuple(box)


errors = []
counts = {}
cur_cell = -1
expected = []
seen_cells = 0
n = 0
sample = []
volume = {}
with gzip.open(leafp, "rt") as fh:
    for line in fh:
        ci_s, path, out = line.split()
        ci = int(ci_s)
        path = "" if path == "-" else path
        if out not in allowed:
            errors.append(f"outcome {out} not allowed at cell {ci} path {path}")
        counts[out] = counts.get(out, 0) + 1
        if ci != cur_cell:
            if cur_cell >= 0 and expected:
                errors.append(f"cell {cur_cell} incomplete: {len(expected)} open nodes")
            if ci != cur_cell + 1:
                errors.append(f"cell order jump {cur_cell} -> {ci}")
            cur_cell = ci
            seen_cells += 1
            expected = [""]
        if not expected:
            errors.append(f"cell {ci}: extra leaf {path}")
            continue
        e = expected.pop()
        while e != path:
            if not path.startswith(e) or len(path) <= len(e):
                errors.append(f"cell {ci}: leaf {path} does not match expected node {e}")
                break
            expected.append(e + "1")
            e = e + "0"
        n += 1
        if n % stride == 0:
            b = box_of(ci, path)
            sample.append(f"{out} " + " ".join(f"{lo} {hi}" for lo, hi in b))
        if len(errors) > 50:
            break
if expected:
    errors.append(f"cell {cur_cell} incomplete at end: {len(expected)} open nodes")
if seen_cells != ncells:
    errors.append(f"cells seen {seen_cells} != {ncells}")
res = {"leaves": n, "counts": counts, "cells_expected": ncells, "cells_seen": seen_cells,
       "errors_first50": errors[:50], "tiling_ok": not errors, "sample_stride": stride, "sample_size": len(sample)}
with lane_guard.xopen(RUN + "/cover.json") as fh:
    json.dump(res, fh, indent=1)
with lane_guard.xopen(RUN + "/sample_boxes.txt") as fh:
    fh.write("\n".join(sample) + "\n")
print(json.dumps(res, indent=1))
