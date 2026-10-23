"""Certified branch-and-bound for Lemma M on the primal valley region (spec: code/spec_valley_v1.json).

argv[1] = run directory; argv[2] = spec path. Deterministic depth-first processing in a fixed order.
Writes valley.json and dpos_leaves.txt (exclusive create).
"""
import sys
import json
import time
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import me3lib_v1 as L  # noqa: E402

RUN = sys.argv[1]
spec = json.load(open(sys.argv[2]))
flint.ctx.prec = 128


def Q(s):
    if "/" in s:
        a, b = s.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(s))


T = arb(Q(spec["T"]))
reg = {k: (Q(v[0]), Q(v[1])) for k, v in spec["region"].items()}
dims = ["r", "w", "phi"]
PI = arb.pi()
maxdepth = spec["max_depth"]


def ball(lo, hi):
    return arb(lo).union(arb(hi))


def classify(box):
    (rl, rh), (wl, wh), (pl, ph) = box
    # INFEAS
    if arb(pl) > PI and rl > 0:
        if L.g_feas(arb(rl), arb(pl)) > 1:
            return "INFEAS"
    rb, wb, pb = ball(rl, rh), ball(wl, wh), ball(pl, ph)
    a0, a1, a2, G, D = L.primal_G_D(rb, wb, pb, T)
    if a1 > 0 and G > 0:
        return "SGE"
    if a0 > 0 and a1 > 0 and a2 > 0 and D > 0:
        return "DPOS"
    return None


def split(box):
    widths = [box[i][1] - box[i][0] for i in range(3)]
    i = max(range(3), key=lambda j: widths[j])
    lo, hi = box[i]
    mid = (lo + hi) / 2
    b1 = list(box)
    b2 = list(box)
    b1[i] = (lo, mid)
    b2[i] = (mid, hi)
    return tuple(b1), tuple(b2)


t0 = time.time()
init = []
n = spec["initial_split"]
for i in range(n["r"]):
    r0 = reg["r"][0] + (reg["r"][1] - reg["r"][0]) * i / n["r"]
    r1 = reg["r"][0] + (reg["r"][1] - reg["r"][0]) * (i + 1) / n["r"]
    for j in range(n["w"]):
        w0 = reg["w"][0] + (reg["w"][1] - reg["w"][0]) * j / n["w"]
        w1 = reg["w"][0] + (reg["w"][1] - reg["w"][0]) * (j + 1) / n["w"]
        for k in range(n["phi"]):
            p0 = reg["phi"][0] + (reg["phi"][1] - reg["phi"][0]) * k / n["phi"]
            p1 = reg["phi"][0] + (reg["phi"][1] - reg["phi"][0]) * (k + 1) / n["phi"]
            init.append(((r0, r1), (w0, w1), (p0, p1)))

counts = {"INFEAS": 0, "SGE": 0, "DPOS": 0, "FAIL": 0}
depth_hist = {}
fails = []
hasher = hashlib.sha256()
dpos_lines = []
dpos_bb = None
evals = 0
stack = [(b, 0) for b in reversed(init)]
while stack:
    box, d = stack.pop()
    out = classify(box)
    evals += 1
    if out is None:
        if d >= maxdepth:
            counts["FAIL"] += 1
            if len(fails) < 50:
                fails.append([[str(x) for x in iv] for iv in box])
            hasher.update(("FAIL " + repr([[str(x) for x in iv] for iv in box]) + "\n").encode())
            continue
        b1, b2 = split(box)
        stack.append((b2, d + 1))
        stack.append((b1, d + 1))
        continue
    counts[out] += 1
    depth_hist[d] = depth_hist.get(d, 0) + 1
    line = out + " " + " ".join(f"{iv[0]} {iv[1]}" for iv in box)
    hasher.update((line + "\n").encode())
    if out == "DPOS":
        dpos_lines.append(line)
        lo = [float(iv[0]) for iv in box]
        hi = [float(iv[1]) for iv in box]
        if dpos_bb is None:
            dpos_bb = [lo, hi]
        else:
            dpos_bb = [[min(a, b) for a, b in zip(dpos_bb[0], lo)], [max(a, b) for a, b in zip(dpos_bb[1], hi)]]
    if evals % 20000 == 0:
        print("progress", evals, counts, round(time.time() - t0, 1), flush=True)

summary = {"spec": spec["name"], "counts": counts, "evaluations": evals, "initial_boxes": len(init),
           "depth_histogram": {str(k): v for k, v in sorted(depth_hist.items())}, "fails_first50": fails,
           "dpos_bounding_box_float": dpos_bb, "leaf_list_sha256": hasher.hexdigest(),
           "certificate_ok": counts["FAIL"] == 0, "elapsed_seconds": round(time.time() - t0, 2)}
with lane_guard.xopen(RUN + "/valley.json") as fh:
    json.dump(summary, fh, indent=1)
with lane_guard.xopen(RUN + "/dpos_leaves.txt") as fh:
    fh.write("\n".join(dpos_lines) + "\n")
print("SUMMARY", json.dumps(summary))
