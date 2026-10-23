"""Certified branch-and-bound for Lemma M on the primal valley region, VERSION 2 (spec: argv[2]).

v1 (cert_valley_v1.py, run c01-valley) used naive ball evaluation only and was stopped by SIGTERM after
38.8M evaluations (box explosion from the dependency effect; no FAIL up to that point; no conclusion).
v2 adds mean-value-form (MVF) enclosures via first-order jets (me3jet_v1) for G and D, tried after the naive test.

Per box (exact rational endpoints): INFEAS (phi_lo > pi, r_lo > 0, g_{r_lo}(phi_lo) > 1)  |  SGE (a1 > 0 and
G > 0, naive or MVF)  |  DPOS (a0, a1, a2 > 0 and D > 0, naive or MVF)  |  split widest dimension.
G = 2 a0 a2 - (1+T) a1^2 (S > T), D = a0' a1 a2 + a0 a1 a2' - 2 a0 a1' a2 (dS/dr > 0 at fixed w, phi).
argv[1] = run directory. Writes valley.json (+ dpos_leaves.txt only if <= 300000 DPOS leaves).
"""
import sys
import json
import time
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3lib_v1 as L  # noqa: E402
from me3jet_v1 import EXP, RE, mvf  # noqa: E402

RUN = sys.argv[1]
spec = json.load(open(sys.argv[2]))
flint.ctx.prec = spec.get("prec", 128)


def Q(s):
    s = str(s)
    if "/" in s:
        a, b = s.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(s))


T = Q(spec["T"])
Tb = arb(T)
reg = {k: (Q(v[0]), Q(v[1])) for k, v in spec["region"].items()}
PI = arb.pi()
maxdepth = spec["max_depth"]
I = acb(0, 1)


def primal_GD_generic(R, Wv, Ph):
    c = (1 - I * R) * EXP((R - I) * Ph)
    zeta = 1 / (1 + R * Wv - I * Wv)
    shift = Ph + (R - I) / (1 + R * R)
    a = []
    da = []
    zp = zeta
    for k in range(3):
        P = c * zp
        a.append(1 - RE(P))
        dP = P * (shift - (k + 1) * Wv * zeta)
        da.append(-RE(dP))
        zp = zp * zeta
    G = 2 * a[0] * a[2] - (1 + Tb) * a[1] * a[1]
    D = da[0] * a[1] * a[2] + a[0] * a[1] * da[2] - 2 * a[0] * da[1] * a[2]
    return (G, D)


def ball(lo, hi):
    return arb(lo).union(arb(hi))


stats = {"naive_SGE": 0, "mvf_SGE": 0, "naive_DPOS": 0, "mvf_DPOS": 0}


def classify(box):
    (rl, rh), (wl, wh), (pl, ph) = box
    if arb(pl) > PI and rl > 0:
        if L.g_feas(arb(rl), arb(pl)) > 1:
            return "INFEAS"
    rb, wb, pb = ball(rl, rh), ball(wl, wh), ball(pl, ph)
    a0, a1, a2, G, D = L.primal_G_D(rb, wb, pb, Tb)
    apos = a0 > 0 and a1 > 0 and a2 > 0
    if a1 > 0 and G > 0:
        stats["naive_SGE"] += 1
        return "SGE"
    if apos and D > 0:
        stats["naive_DPOS"] += 1
        return "DPOS"
    mids = [arb((rl + rh) / 2), arb((wl + wh) / 2), arb((pl + ph) / 2)]
    hb = [ball(-(rh - rl) / 2, (rh - rl) / 2), ball(-(wh - wl) / 2, (wh - wl) / 2), ball(-(ph - pl) / 2, (ph - pl) / 2)]
    Gm, Dm = mvf(primal_GD_generic, mids, [rb, wb, pb], hb)
    if a1 > 0 and Gm > 0:
        stats["mvf_SGE"] += 1
        return "SGE"
    if apos and Dm > 0:
        stats["mvf_DPOS"] += 1
        return "DPOS"
    return None


def split(box):
    widths = [box[i][1] - box[i][0] for i in range(3)]
    i = max(range(3), key=lambda j: widths[j])
    lo, hi = box[i]
    mid = (lo + hi) / 2
    b1, b2 = list(box), list(box)
    b1[i], b2[i] = (lo, mid), (mid, hi)
    return tuple(b1), tuple(b2)


t0 = time.time()
n = spec["initial_split"]
init = []
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
            hasher.update(("FAIL " + " ".join(f"{iv[0]} {iv[1]}" for iv in box) + "\n").encode())
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
        if len(dpos_lines) <= 300000:
            dpos_lines.append(line)
        lo = [float(iv[0]) for iv in box]
        hi = [float(iv[1]) for iv in box]
        dpos_bb = [lo, hi] if dpos_bb is None else [[min(a, b) for a, b in zip(dpos_bb[0], lo)],
                                                     [max(a, b) for a, b in zip(dpos_bb[1], hi)]]
    if evals % 100000 == 0:
        print("progress", evals, counts, stats, round(time.time() - t0, 1), flush=True)
    if evals > spec["eval_cap"]:
        print("EVAL CAP REACHED; stopping without conclusion", flush=True)
        break

summary = {"spec": spec["name"], "counts": counts, "stats": stats, "evaluations": evals, "initial_boxes": len(init),
           "stack_remaining": len(stack), "depth_histogram": {str(k): v for k, v in sorted(depth_hist.items())},
           "fails_first50": fails, "dpos_bounding_box_float": dpos_bb, "leaf_list_sha256": hasher.hexdigest(),
           "certificate_ok": counts["FAIL"] == 0 and len(stack) == 0, "elapsed_seconds": round(time.time() - t0, 2)}
with lane_guard.xopen(RUN + "/valley.json") as fh:
    json.dump(summary, fh, indent=1)
if counts["DPOS"] <= 300000:
    with lane_guard.xopen(RUN + "/dpos_leaves.txt") as fh:
        fh.write("\n".join(dpos_lines) + "\n")
print("SUMMARY", json.dumps(summary))
