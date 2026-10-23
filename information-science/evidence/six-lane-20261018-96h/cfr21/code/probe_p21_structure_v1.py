#!/usr/bin/env python3
"""probe_p21_structure_v1.py  (ContinueCFR21, frozen before execution)
Stdlib-only, read-only analysis of the 96 pinned P21 six-row (Z21,6;1)-DMs.
Self wall budget 280 s. Prints one JSON object to stdout.
Checks: DM property; mod-3 triple-sum types (must be multiples of 3); constant
characters of the mod-3 image over all translation-invariant characters chi in F3^6
(sum chi = 0); affine rank of the mod-3 image; mod-7 blocks (7-column subsets on which
every row pair difference is a permutation of Z7) and three-block decompositions.
"""
import sys, json, time, hashlib, itertools
T0 = time.monotonic(); BUDGET = 280.0
def budget():
    if time.monotonic() - T0 > BUDGET:
        print(json.dumps({"status": "SELF_BUDGET_EXCEEDED"})); sys.exit(3)
path, want = sys.argv[1], sys.argv[2]
raw = open(path, 'rb').read()
got = hashlib.sha256(raw).hexdigest()
if got != want:
    print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
d = json.loads(raw)
n = 21
def is_perm(v): return sorted(v) == list(range(n))
out = {"status": "OK", "input_sha256": got, "n_dms": len(d["dms"])}
type_hist = {}; rank_hist = {}; const_hist = {}; block_hist = {}; dec_hist = {}
per = []
# all translation-invariant characters chi in F3^6 (rows 0..5) up to sign, nonzero
chars = []
for chi in itertools.product(range(3), repeat=6):
    if sum(chi) % 3 or not any(chi): continue
    # canonical up to sign: first nonzero coordinate == 1
    fnz = next(c for c in chi if c)
    if fnz != 1: continue
    chars.append(chi)
def chartype(chi):
    return (sum(1 for c in chi if c == 1), sum(1 for c in chi if c == 2))
def f3rank(rows):
    rows = [list(r) for r in rows]; r = 0; m = len(rows[0]) if rows else 0
    for col in range(m):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][col] % 3: piv = i; break
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = 1 if rows[r][col] % 3 == 1 else 2
        rows[r] = [(x * inv) % 3 for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] % 3:
                f = rows[i][col] % 3
                rows[i] = [(a - f * b) % 3 for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
for dm in d["dms"]:
    budget()
    R = dm["rows"]; k = len(R)
    ok = all(is_perm([(R[i][c] - R[j][c]) % n for c in range(n)]) for i in range(k) for j in range(k) if i != j)
    rec = {"sol": dm["sol"], "dm_ok": ok}
    A = [[x % 3 for x in r] for r in R]
    B = [[x % 7 for x in r] for r in R]
    types = []
    for (a, b, c) in itertools.combinations(range(k), 3):
        cnt = [0, 0, 0]
        for col in range(n): cnt[(A[a][col] + A[b][col] + A[c][col]) % 3] += 1
        assert all(x % 3 == 0 for x in cnt), (dm["sol"], a, b, c, cnt)
        t = tuple(sorted((x // 3 for x in cnt), reverse=True)); types.append(t)
        type_hist[str(t)] = type_hist.get(str(t), 0) + 1
    rec["triple_types"] = sorted(str(t) for t in types)
    consts = []
    for chi in chars:
        vals = set((sum(chi[i] * A[i][col] for i in range(k))) % 3 for col in range(n))
        if len(vals) == 1: consts.append(chartype(chi))
    rec["constant_characters"] = sorted(str(t) for t in consts)
    for t in consts: const_hist[str(t)] = const_hist.get(str(t), 0) + 1
    diffs = [[(A[i][col] - A[0][col]) % 3 for col in range(n)] for i in range(1, k)]
    pts = list(zip(*diffs))
    rk = f3rank([[ (p[i] - pts[0][i]) % 3 for i in range(k - 1)] for p in pts[1:]]) if len(pts) > 1 else 0
    rec["mod3_affine_rank"] = rk; rank_hist[rk] = rank_hist.get(rk, 0) + 1
    # mod-7 compatibility graph and 7-cliques (blocks)
    comp = [[False] * n for _ in range(n)]
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            v = [(B[i][c1] - B[i][c2]) % 7 for i in range(k)]
            comp[c1][c2] = comp[c2][c1] = (len(set(v)) == k)
    blocks = []
    def ext(cl, cand):
        if len(cl) == 7: blocks.append(tuple(cl)); return
        for idx, c in enumerate(cand):
            nc = [x for x in cand[idx + 1:] if comp[c][x]]
            if len(cl) + 1 + len(nc) >= 7: ext(cl + [c], nc)
    ext([], list(range(n)))
    rec["mod7_blocks"] = len(blocks); block_hist[len(blocks)] = block_hist.get(len(blocks), 0) + 1
    decs = 0
    bs = [set(b) for b in blocks]
    for i in range(len(bs)):
        for j in range(i + 1, len(bs)):
            if bs[i] & bs[j]: continue
            for l in range(j + 1, len(bs)):
                if not (bs[l] & bs[i]) and not (bs[l] & bs[j]): decs += 1
    rec["three_block_decompositions"] = decs; dec_hist[decs] = dec_hist.get(decs, 0) + 1
    per.append(rec)
out["all_dm_ok"] = all(r["dm_ok"] for r in per)
out["triple_type_hist"] = type_hist
out["constant_character_hist"] = const_hist
out["mod3_affine_rank_hist"] = {str(a): b for a, b in rank_hist.items()}
out["mod7_block_count_hist"] = {str(a): b for a, b in block_hist.items()}
out["three_block_decomposition_hist"] = {str(a): b for a, b in dec_hist.items()}
# representatives (0,id,f) triple types
reps = []
for r in d["representatives"]:
    f = [0] + r["f"]
    cnt = [0, 0, 0]
    for x in range(n): cnt[(x + f[x]) % 3] += 1
    reps.append({"line": r["line"], "orbit_size": r["orbit_size"], "sum_counts": cnt})
out["representatives_triple_sum_counts"] = reps
out["per_dm"] = per
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
