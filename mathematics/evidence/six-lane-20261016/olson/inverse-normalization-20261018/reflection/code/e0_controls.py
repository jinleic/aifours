#!/usr/bin/env python3
"""E0: controls for the raw DPs and the G-word window formulas (README Sec. 5, E0).  Output: out/e0_controls.json (x)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
OLSON_CODE = os.path.normpath(os.path.join(HERE, "..", "..", "..", "code"))
sys.path.insert(1, OLSON_CODE)
import was_verify  # read-only import of the unchanged olson/code/was_verify.py (dp_has only)

out = {"checks": [], "failures": 0}
def rec(name, ok, **kw):
    out["checks"].append(dict(name=name, ok=bool(ok), **kw))
    if not ok:
        out["failures"] += 1

R = lambda x: ('R', x)
S = lambda y: ('F', y)

# Positive controls: must AVOID.
for p in (5, 7, 11, 13):
    for v in (0, 1, p - 1):
        w = [S(v - 2)] + [R(1)] * (2 * p - 3) + [S(v)] * (2 * p - 1)
        a1, a2 = dp.dp1(w, p), dp.dp2(w, p)
        rec("sharpness_avoids", (not a1) and (not a2), p=p, v=v, n=len(w))
        # three extensions: must be solvable, explicit witness re-multiplied
        exts = [[S(v - 2)] + [R(1)] * (2 * p - 2) + [S(v)] * (2 * p - 1),
                [S(v - 2)] + [R(1)] * (2 * p - 3) + [S(v)] * (2 * p),
                [S(v - 2)] * 2 + [R(1)] * (2 * p - 3) + [S(v)] * (2 * p - 1)]
        for j, e in enumerate(exts):
            wi = dp.witness(e, p)
            rec("sharpness_ext_solvable", wi is not None and dp.dp2(e, p), p=p, v=v, ext=j + 1, n=len(e))
    w = [R(1)] * (2 * p - 1) + [S(0)] * (2 * p - 1)
    rec("rho^(2p-1)sigma^(2p-1)_avoids", (not dp.dp1(w, p)) and (not dp.dp2(w, p)), p=p, n=len(w))
    # explicit index sets of proof-sharpness.md, multiplied directly
    v = 0
    e1 = [S(v - 2)] + [R(1)] * (2 * p - 2) + [S(v)] * (2 * p - 1)
    idx1 = list(range(0, 2 * p - 1)) + [2 * p - 1]     # sigma_(v-2), all 2p-2 rho_1, one sigma_v
    rec("ext1_explicit", dp.product(e1, idx1, p) == (0, 1) and len(idx1) == 2 * p, p=p)
    e2 = [S(v - 2)] + [R(1)] * (2 * p - 3) + [S(v)] * (2 * p)
    idx2 = list(range(2 * p - 2, 4 * p - 2))
    rec("ext2_explicit", dp.product(e2, idx2, p) == (0, 1) and len(idx2) == 2 * p, p=p)
    e3 = [S(v - 2)] * 2 + [R(1)] * (2 * p - 3) + [S(v)] * (2 * p - 1)
    idx3 = [0, 1] + list(range(2 * p - 1, 4 * p - 3))
    rec("ext3_explicit", dp.product(e3, idx3, p) == (0, 1) and len(idx3) == 2 * p, p=p)

# FILL counter-example of README Sec. 3 (p = 5, N = 17): sigma_y^2 rho_1^9 sigma_(y+3)^6
p = 5
for yv in range(p):
    w = [S(yv)] * 2 + [R(1)] * 9 + [S(yv + 3)] * 6
    rec("fill_example_avoids", (not dp.dp1(w, p)) and (not dp.dp2(w, p)), p=p, y=yv)
    for x in (1, p - 1):
        wf = w + [R(x)]
        wi = dp.witness(wf, p)
        rec("fill_example_filled_solvable", wi is not None, p=p, y=yv, x=x, witness=wi)

# Cross-check dp1, dp2, was_verify.dp_has on random words (all letter types, including rho_0)
rng = random.Random(20261018)
agree = 0; nos = 0
for trial in range(3000):
    p = rng.choice((5, 7))
    n = rng.choice((4 * p - 3, 4 * p - 2, 4 * p - 1))
    mode = rng.random()
    w = []
    for _ in range(n):
        if rng.random() < 0.5:
            w.append(R(rng.choice((1, p - 1)) if mode < 0.7 else rng.randrange(p)))
        else:
            w.append(S(rng.randrange(min(p, 1 + int(mode * 4)))))
    a1 = dp.dp1(w, p); a2 = dp.dp2(w, p); a3 = was_verify.dp_has(w, p)
    if a1 == a2 == a3:
        agree += 1
    else:
        rec("dp_disagree", False, p=p, word=w)
    nos += (not a1)
rec("dp_crosscheck", agree == 3000, agree=agree, no_instances=nos)

# GR0 (any representation) and H0 (length 4p-2) versus raw DP on random G-words with empty runs
def rand_gword(p, n, rng, kmax):
    while True:
        k = rng.randint(2, kmax)
        l = [1] * k
        a = [0] * k; b = [0] * k
        F = rng.randint(k, n - 1)
        for _ in range(F - k):
            l[rng.randrange(k)] += 1
        Rr = n - F
        empty = [rng.random() < 0.35 for _ in range(k)]
        if all(empty):
            empty[rng.randrange(k)] = False
        ne = [i for i in range(k) if not empty[i]]
        if Rr < len(ne):
            continue
        cnt = [0] * k
        for i in ne:
            cnt[i] = 1
        for _ in range(Rr - len(ne)):
            cnt[rng.choice(ne)] += 1
        for i in range(k):
            if rng.random() < 0.6:
                a[i] = cnt[i]
            else:
                a[i] = rng.randint(0, cnt[i]); b[i] = cnt[i] - a[i]
        y = [rng.randrange(p) for _ in range(k)]
        for i in range(k):  # genuine: empty run i separates y[i-1] != y[i]
            if empty[i] and y[i - 1] == y[i]:
                y[i] = (y[i] + 1) % p
        if any(empty[i] and y[i - 1] == y[i] for i in range(k)):
            continue
        return a, b, l, y

g_agree = 0; g_total = 0; g_no = 0; h_agree = 0; h_total = 0; h_no = 0
for trial in range(1500):
    p = rng.choice((5, 7))
    n = rng.choice((4 * p - 3, 4 * p - 2))
    a, b, l, y = rand_gword(p, n, rng, 8)
    # random order inside rotation runs
    order = []
    for i in range(len(a)):
        s = [1] * a[i] + [p - 1] * b[i]
        rng.shuffle(s)
        order.append(s)
    w = gwin.word_of(a, b, l, y, p, order)
    truth = dp.solvable(w, p)
    g = gwin.gr0_solvable(a, b, l, y, p)
    g_total += 1; g_agree += (g == truth); g_no += (not truth)
    if g != truth:
        rec("gr0_mismatch", False, p=p, a=a, b=b, l=l, y=y)
    if n == 4 * p - 2:
        h = gwin.h0_solvable(a, b, l, y, p)
        h_total += 1; h_agree += (h == truth); h_no += (not truth)
        if h != truth:
            rec("h0_mismatch", False, p=p, a=a, b=b, l=l, y=y)
rec("gr0_vs_dp", g_agree == g_total, total=g_total, agree=g_agree, no_instances=g_no)
rec("h0_vs_dp", h_agree == h_total, total=h_total, agree=h_agree, no_instances=h_no)

srcs = {}
for fn in ("dp.py", "gwin.py", "e0_controls.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(OLSON_CODE, "was_verify.py"), "rb") as f:
    srcs["olson/code/was_verify.py"] = hashlib.sha256(f.read()).hexdigest()
out["sources_sha256"] = srcs
path = os.path.join(HERE, "..", "out", "e0_controls.json")
with open(path, "x") as f:
    json.dump(out, f, indent=1)
print("failures", out["failures"], "checks", len(out["checks"]))
for c in out["checks"]:
    if c["name"] in ("dp_crosscheck", "gr0_vs_dp", "h0_vs_dp") or not c["ok"]:
        print(c)
