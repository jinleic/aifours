#!/usr/bin/env python3
"""E7 (plan-E7.md): words realising the lift data on which a G-version of S1' Step 2 fails (B = 0, all blocks odd, k <= p,
3g = 2 kappa, every nonempty run odd with theta_t = r_t + 1, every empty run with theta_t = -2).  Raw DP decides each word.
Output: out/e7_failing_lifts.json (exclusive create)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(7070)

def g1(p, kap, E):
    return min(p - 1, E - kap, E // 2)

out = {"cases": [], "candidates": []}
for (p, kap, g) in ((11, 3, 2), (13, 3, 2), (17, 3, 2), (17, 6, 4), (19, 6, 4)):
    H = p - 1 - kap
    for k in range(2 * kap + 2, p + 1):
        R = 2 * p - k + 2 * kap
        st = dict(p=p, kappa=kap, g=g, k=k, words=0, solvable=0, lifts_realised=0, adjacent_empty=0)
        for trial in range(40):
            # positions of empty runs
            if rng.random() < 0.5:
                s = rng.randrange(k); emp = {(s + i) % k for i in range(g)}       # consecutive empty runs
            else:
                emp = set(rng.sample(range(k), g))
            if len(emp) != g: continue
            ne = [i for i in range(k) if i not in emp]
            # odd run lengths summing to R
            if R < len(ne) or (R - len(ne)) % 2: continue
            r = [0] * k
            for i in ne: r[i] = 1
            for _ in range((R - len(ne)) // 2): r[rng.choice(ne)] += 2
            a = r; b = [0] * k
            l = [1] * k; l[rng.randrange(k)] += 2 * H
            theta = [(r[i] + 1) % p if r[i] > 0 else (-2) % p for i in range(k)]
            assert sum(theta) % p == 0
            y = [0] * k
            # y_i = y_(i-1) - theta_i, y_(k-1) = 0
            prev = 0
            for i in range(k):
                y[i] = (prev - theta[i]) % p; prev = y[i]
            assert y[k - 1] == 0
            assert all(y[(i - 1) % k] != y[i] for i in emp)
            assert gwin.kappa_of(l, p) == kap and sum(a) + sum(l) == 4 * p - 2
            # do the prefix lifts (chain 0..k-1 starting after block k-1) realise x_t = (r_t+1)/2, resp. -1 ?
            x = [(r[i] + 1) // 2 if r[i] > 0 else -1 for i in range(k)]
            V = 0; rho = 0; ok = True
            for j in range(k - 1):
                V += x[j]; rho += r[j]
                lo = g1(p, kap, rho) + 1; hi = p - g1(p, kap, R - rho) - 1
                if not (lo <= V <= hi): ok = False
            st["lifts_realised"] += ok
            st["adjacent_empty"] += any(((i + 1) % k) in emp for i in emp)
            w = gwin.word_of(a, b, l, y, p)
            st["words"] += 1
            sv = dp.dp1(w, p)
            if not sv:
                sv = dp.dp2(w, p)
                if not sv:
                    out["candidates"].append(dict(p=p, kappa=kap, k=k, a=a, l=l, y=y))
            st["solvable"] += sv
        out["cases"].append(st)
srcs = {}
for fn in ("dp.py", "gwin.py", "e7_failing_lifts.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "plan-E7.md"), "rb") as f:
    srcs["plan-E7.md"] = hashlib.sha256(f.read()).hexdigest()
out["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e7_failing_lifts.json"), "x") as f:
    json.dump(out, f, indent=0)
tw = sum(c["words"] for c in out["cases"]); ts = sum(c["solvable"] for c in out["cases"]); tl = sum(c["lifts_realised"] for c in out["cases"])
print("words", tw, "solvable", ts, "lifts_realised", tl, "candidates", len(out["candidates"]))
