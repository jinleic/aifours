#!/usr/bin/env python3
"""E1: finite checks of the move lemmas of proof-K0star-r1.md Sec. 2 (aids only).
 (1) spectra of two-block segments by full subset enumeration: SL equality, FUS inclusion, and mutations
     (one-letter slide; FUS with the absorbed block odd) that must FAIL;
 (2) TR, PM0, FUS on explicit words: raw-DP avoidance transfer (TR both directions, PM0/FUS one direction), with
     near-avoider inputs so that NO instances occur.
Output: out/e1_moves.json (exclusive create)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin

def spec(seg, p):
    n = len(seg)
    out = set()
    for mask in range(1 << n):
        g = (0, 1); c = 0
        for i in range(n):
            if (mask >> i) & 1:
                g = dp.mult(g, dp.letter(*seg[i], p), p); c += 1
        out.add((c, g))
    return out

res = {"spectra": {}, "moves": {}, "failures": []}
def fail(msg, **kw):
    res["failures"].append(dict(msg=msg, **kw))

# (1) spectra
cnt = dict(sl=0, fus=0, mut_slide_detected=0, mut_slide_total=0, mut_fus_detected=0, mut_fus_total=0)
for p in (5, 7, 11):
    for (u, v) in ((0, 1), (0, 2), (3, 1)):
        S = {}
        for a in range(1, 12):
            for b in range(1, 13 - a):
                S[(a, b)] = spec([('F', u)] * a + [('F', v)] * b, p)
        for (a, b), s in S.items():
            if (a + 2, b - 2) in S:
                cnt["sl"] += 1
                if S[(a + 2, b - 2)] != s:
                    fail("SL", p=p, u=u, v=v, a=a, b=b)
            if (a + 1, b - 1) in S:
                cnt["mut_slide_total"] += 1
                if S[(a + 1, b - 1)] != s:
                    cnt["mut_slide_detected"] += 1
            n = a + b
            yu = spec([('F', u)] * n, p); yv = spec([('F', v)] * n, p)
            if b % 2 == 0:
                cnt["fus"] += 1
                if not yu <= s:
                    fail("FUS_even_after", p=p, a=a, b=b)
            else:
                cnt["mut_fus_total"] += 1
                if not yu <= s:
                    cnt["mut_fus_detected"] += 1
            if a % 2 == 0:
                cnt["fus"] += 1
                if not yv <= s:
                    fail("FUS_even_before", p=p, a=a, b=b)
res["spectra"] = cnt

# (2) moves on explicit words
rng = random.Random(1018)
def near_word(p, n):
    """random G-representation biased toward avoiding: few blocks, constant-ish rotation runs"""
    while True:
        k = rng.randint(2, 7)
        F = rng.randint(k, n - 2)
        l = [1] * k
        for _ in range(F - k):
            l[rng.randrange(k)] += 1
        Rr = n - F
        empty = [rng.random() < 0.3 for _ in range(k)]
        if all(empty):
            continue
        ne = [i for i in range(k) if not empty[i]]
        if Rr < len(ne):
            continue
        cnt_ = [0] * k
        for i in ne: cnt_[i] = 1
        for _ in range(Rr - len(ne)):
            cnt_[rng.choice(ne)] += 1
        a = [0] * k; b = [0] * k
        for i in range(k):
            r = rng.random()
            if r < 0.55: a[i] = cnt_[i]
            elif r < 0.75: b[i] = cnt_[i]
            else:
                a[i] = rng.randint(0, cnt_[i]); b[i] = cnt_[i] - a[i]
        y = [rng.randrange(p) for _ in range(k)]
        bad = False
        for i in range(k):
            if empty[i] and y[i - 1] == y[i]:
                y[i] = (y[i] + 1 + rng.randrange(p - 1)) % p
        for i in range(k):
            if empty[i] and y[i - 1] == y[i]:
                bad = True
        if not bad:
            return a, b, l, y

stats = dict(tr_pairs=0, tr_no=0, tr_mismatch=0, pm0=0, pm0_no_before=0, pm0_violation=0,
             fus=0, fus_no_before=0, fus_violation=0)
for trial in range(6000):
    p = rng.choice((5, 7))
    n = rng.choice((4 * p - 6, 4 * p - 5, 4 * p - 4, 4 * p - 3, 4 * p - 2))
    a, b, l, y = near_word(p, n)
    k = len(a)
    w = gwin.word_of(a, b, l, y, p)
    before = dp.solvable(w, p)
    # TR
    donors = [s for s in range(k) if a[s] >= 1 and b[s] >= 1]
    if donors:
        s = rng.choice(donors); t = rng.choice([i for i in range(k) if i != s])
        a2 = list(a); b2 = list(b)
        a2[s] -= 1; b2[s] -= 1; a2[t] += 1; b2[t] += 1
        w2 = gwin.word_of(a2, b2, l, y, p)
        after = dp.solvable(w2, p)
        stats["tr_pairs"] += 1; stats["tr_no"] += (not before)
        if after != before:
            stats["tr_mismatch"] += 1
            fail("TR", p=p, a=a, b=b, l=l, y=y, s=s, t=t)
    # PM0 across an even block S_j (any neighbours)
    ev = [j for j in range(k) if l[j] % 2 == 0 and k >= 2]
    if ev:
        j = rng.choice(ev)
        jn = (j + 1) % k
        # merge R_j and R_{j+1}: new run = R_j + R_{j+1}; S_j's letters appended to S_{j+1}
        a2 = []; b2 = []; l2 = []; y2 = []
        for i in range(k):
            if i == jn:
                continue
            if i == j:
                a2.append(a[j] + a[jn]); b2.append(b[j] + b[jn]); l2.append(l[jn] + l[j]); y2.append(y[jn])
            else:
                a2.append(a[i]); b2.append(b[i]); l2.append(l[i]); y2.append(y[i])
        # representation order: run i is followed by block i; merged run j followed by enlarged S_{j+1}
        w2 = gwin.word_of(a2, b2, l2, y2, p)
        after = dp.solvable(w2, p)
        stats["pm0"] += 1; stats["pm0_no_before"] += (not before)
        if (not before) and after:
            stats["pm0_violation"] += 1
            fail("PM0", p=p, a=a, b=b, l=l, y=y, j=j)
    # FUS at an empty run with an even neighbour
    cand = []
    for t in range(k):
        if a[t] + b[t] == 0:
            if l[t] % 2 == 0: cand.append((t, 'after'))
            if l[t - 1] % 2 == 0: cand.append((t, 'before'))
    if cand:
        t, side = rng.choice(cand)
        y2 = list(y)
        if side == 'after': y2[t] = y[t - 1]
        else: y2[t - 1] = y[t]
        w2 = gwin.word_of(a, b, l, y2, p)
        after = dp.solvable(w2, p)
        stats["fus"] += 1; stats["fus_no_before"] += (not before)
        if (not before) and after:
            stats["fus_violation"] += 1
            fail("FUS", p=p, a=a, b=b, l=l, y=y, t=t, side=side)
res["moves"] = stats
srcs = {}
for fn in ("dp.py", "gwin.py", "e1_moves.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
res["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e1_moves.json"), "x") as f:
    json.dump(res, f, indent=1)
print(json.dumps({"spectra": cnt, "moves": stats, "nfail": len(res["failures"])}))
