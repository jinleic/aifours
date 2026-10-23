"""Certified branch-and-bound for the DUAL sufficient test on the far region F (spec JSON in argv[2]).

Charts (all with s in [0,1], mu = s/(1-s)):
  C  corner : (s, delta, w) boxes, test_corner(s, dh, wh)            [delta in [0,dh], w in (0,wh]]
  B  bedge  : (s, delta, w) boxes, test_bedge(s, dl, dh, wh)         [delta in [dl,dh], w in (0,wh]]
  G  general: (s, delta, w) boxes, test_general; boxes inside the primal valley V are SKIPPED
              (V = {w in [w_lo, w_hi], delta <= r_V * w}, handled by the primal certificate)
  LD large-delta: (s, d, beta) boxes, test_largedelta
  LW large-w   : (s, delta, nu) boxes, test_largew
argv[1] = run directory; argv[2] = spec path; optional argv[3] = chart name to run only that chart.
Writes dual_<chart>.json (exclusive create).
"""
import sys
import json
import time
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import me3dual_v2 as D  # noqa: E402

RUN = sys.argv[1]
spec = json.load(open(sys.argv[2]))
only = sys.argv[3] if len(sys.argv) > 3 else None
flint.ctx.prec = spec.get("prec", 128)


def Q(x):
    x = str(x)
    if "/" in x:
        a, b = x.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(x))


T = Q(spec["T"])
kap = arb(1 / (1 + T))
V = {k: Q(v) for k, v in spec["valley"].items()}
maxdepth = spec["max_depth"]
beta_top = Q(spec["beta_top"])


def inside_valley(box):
    (sl, sh), (dl, dh), (wl, wh) = box
    return wl >= V["w_lo"] and wh <= V["w_hi"] and dh <= V["r_V"] * wl


def run_chart(name, cs):
    ranges = [(Q(a), Q(b)) for a, b in cs["ranges"]]
    splits = cs["initial_split"]
    kind = cs["kind"]
    init = []

    def grid(lo, hi, n):
        return [(lo + (hi - lo) * i / n, lo + (hi - lo) * (i + 1) / n) for i in range(n)]
    for a in grid(*ranges[0], splits[0]):
        for b in grid(*ranges[1], splits[1]):
            for c in grid(*ranges[2], splits[2]):
                init.append((a, b, c))
    counts = {"CERT": 0, "SKIP": 0, "FAIL": 0}
    reasons = {}
    fails = []
    depth_hist = {}
    hasher = hashlib.sha256()
    stack = [(bx, 0) for bx in reversed(init)]
    t0 = time.time()
    evals = 0
    while stack:
        box, dpt = stack.pop()
        (sl, sh), (xl, xh), (yl, yh) = box
        evals += 1
        if kind == "G" and inside_valley(box):
            counts["SKIP"] += 1
            hasher.update(("SKIP " + " ".join(f"{p} {q}" for p, q in box) + "\n").encode())
            continue
        sb = arb(sl).union(arb(sh))
        if kind == "C":
            ok, why = D.test_corner(sb, xh, yh, kap)
        elif kind == "B":
            ok, why = D.test_bedge(sb, xl, xh, yh, kap)
        elif kind == "G":
            ok, why = D.test_general(sb, xl, xh, yl, yh, kap)
        elif kind == "LD":
            ok, why = D.test_largedelta(sb, xl, xh, yl, yh, kap, beta_top)
        elif kind == "LW":
            ok, why = D.test_largew(sb, xl, xh, yl, yh, kap)
        else:
            raise SystemExit("unknown chart kind")
        if ok:
            counts["CERT"] += 1
            depth_hist[dpt] = depth_hist.get(dpt, 0) + 1
            hasher.update(("CERT " + " ".join(f"{p} {q}" for p, q in box) + "\n").encode())
            continue
        reasons[why] = reasons.get(why, 0) + 1
        if dpt >= maxdepth:
            counts["FAIL"] += 1
            if len(fails) < 40:
                fails.append({"box": [[str(p), str(q)] for p, q in box], "why": why})
            hasher.update(("FAIL " + " ".join(f"{p} {q}" for p, q in box) + "\n").encode())
            continue
        widths = [(box[i][1] - box[i][0]) / (ranges[i][1] - ranges[i][0]) for i in range(3)]
        i = max(range(3), key=lambda j: widths[j])
        lo, hi = box[i]
        mid = (lo + hi) / 2
        b1, b2 = list(box), list(box)
        b1[i], b2[i] = (lo, mid), (mid, hi)
        stack.append((tuple(b2), dpt + 1))
        stack.append((tuple(b1), dpt + 1))
        if evals % 50000 == 0:
            print(name, "progress", evals, counts, round(time.time() - t0, 1), flush=True)
    res = {"chart": name, "kind": kind, "ranges": cs["ranges"], "counts": counts, "evaluations": evals,
           "fail_reasons_before_split": reasons, "fails_first40": fails,
           "depth_histogram": {str(k): v for k, v in sorted(depth_hist.items())},
           "leaf_list_sha256": hasher.hexdigest(), "certificate_ok": counts["FAIL"] == 0,
           "elapsed_seconds": round(time.time() - t0, 2)}
    with lane_guard.xopen(f"{RUN}/dual_{name}.json") as fh:
        json.dump(res, fh, indent=1)
    print("CHART", name, json.dumps({k: res[k] for k in ("counts", "evaluations", "certificate_ok", "elapsed_seconds")}),
          flush=True)
    return res


allres = {}
for name, cs in spec["charts"].items():
    if only and name != only:
        continue
    allres[name] = run_chart(name, cs)
print("ALL", json.dumps({k: v["certificate_ok"] for k, v in allres.items()}))
