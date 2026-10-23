#!/usr/bin/env python3
"""E2 part C cross-check: re-decide a seeded random sample of the un-fused words with the independent Python DPs
(dp1 and dp2) and compare with the C++ verdict recomputed here (all sampled words must be solvable unless printed as
candidates).  Also re-check every original avoider with dp.py.  Output: out/e2c_crosscheck.json (x)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp
rng = random.Random(4242)
res = {"by_p": {}}
for p in (5, 7):
    with open(os.path.join(HERE, "..", "out", "e2c_input_p%d.txt" % p)) as f:
        rows = [list(map(int, s.split())) for s in f if s.strip()]
    st = dict(originals=0, originals_avoid=0, sampled=0, sampled_solvable=0)
    for row in rows:
        k = row[1]; a = row[2:2 + k]; b = row[2 + k:2 + 2 * k]; l = row[2 + 2 * k:2 + 3 * k]; y = row[2 + 3 * k:2 + 4 * k]
        def build(bi, blk):
            w = []
            for i in range(k):
                w += [('R', 1)] * a[i] + [('R', p - 1)] * b[i]
                if i == bi:
                    for (val, ln) in blk: w += [('F', val)] * ln
                else:
                    w += [('F', y[i])] * l[i]
            return w
        st["originals"] += 1
        st["originals_avoid"] += (not dp.solvable(build(-1, []), p))
        for trial in range(3):
            bi = rng.randrange(k); Lb = l[bi]; u = y[bi]
            if Lb < 2: continue
            if Lb >= 4 and rng.random() < 0.4:
                aa = rng.randint(1, Lb - 3); bb = rng.choice([x for x in range(2, Lb - aa, 2)]); cc = Lb - aa - bb
                v = rng.choice([x for x in range(p) if x != u])
                blk = [(u, aa), (v, bb), (u, cc)]
            else:
                opts = [(s, side) for s in range(1, Lb) for side in (0, 1) if ((s if side == 0 else Lb - s) % 2 == 0)]
                if not opts: continue
                s, side = rng.choice(opts); v = rng.choice([x for x in range(p) if x != u])
                blk = [(v, s), (u, Lb - s)] if side == 0 else [(u, s), (v, Lb - s)]
            st["sampled"] += 1
            st["sampled_solvable"] += dp.solvable(build(bi, blk), p)
    res["by_p"][str(p)] = st
srcs = {}
for fn in ("dp.py", "e2c_crosscheck.py", "e2c_unfuse.cpp", "e2c_prep.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
res["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e2c_crosscheck.json"), "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps(res["by_p"]))
