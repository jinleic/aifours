#!/usr/bin/env python3
"""probe_lift_rank_census_v1.py (ContinueCFR21; frozen before execution; stdlib only; self wall budget 280 s).
Generic-construction calibration of the exact F3 lift system of 7-row mod-7 images beta (q=7, n=21):
  rank of the 147 x 120 gauge-fixed system E(beta), lift-space dim = 120 - rank, nowhere-zero lift existence,
  versus structure: number of collinear row-point triples ("affine triples", constant mod-7 characters of support 3)
  and the largest collinear row set (Lemma B forbids 4).
Families (seeded, sampled, NOT exhaustive):
  A common-slope   beta_i(t,c) = i*c + f_t(i), f_0 = 0, f_1,f_2 uniform in F7^7
  B affine blocks  beta_i(t,c) = a_t(i)*c + b_t(i), a_0 = id, a_1,a_2 uniform permutations, b_t uniform (b_0 = 0)
Args: seed samples_per_family. Prints one JSON object."""
import sys, json, time, random, itertools
T0 = time.monotonic(); BUD = 270.0
seed = int(sys.argv[1]); NS = int(sys.argv[2]); rng = random.Random(seed)
q = 7; n = 21; K = 7
def over(): return time.monotonic() - T0 > BUD
def lift_rank(beta):
    var = {}
    for x in range(1, K):
        for c in range(1, n): var[(x, c)] = len(var)
    nv = len(var); rows = []; forms = []
    for x in range(K):
        for xp in range(x + 1, K):
            fib = {}
            for c in range(n): fib.setdefault((beta[x][c] - beta[xp][c]) % q, []).append(c)
            if len(fib) != q or any(len(v) != 3 for v in fib.values()): return None
            for F in fib.values():
                e = [0] * nv
                for c in F:
                    if (x, c) in var: e[var[(x, c)]] = (e[var[(x, c)]] + 1) % 3
                    if (xp, c) in var: e[var[(xp, c)]] = (e[var[(xp, c)]] - 1) % 3
                rows.append(e)
                f = [0] * nv
                for c, s in ((F[0], 1), (F[1], -1)):
                    if (x, c) in var: f[var[(x, c)]] = (f[var[(x, c)]] + s) % 3
                    if (xp, c) in var: f[var[(xp, c)]] = (f[var[(xp, c)]] - s) % 3
                forms.append(f)
    M = rows; piv = []; r = 0
    for col in range(nv):
        p = None
        for i in range(r, len(M)):
            if M[i][col]: p = i; break
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        if M[r][col] == 2: M[r] = [(2 * v) % 3 for v in M[r]]
        pr = M[r]
        for i in range(len(M)):
            if i != r:
                fct = M[i][col]
                if fct: M[i] = [(a - fct * b) % 3 for a, b in zip(M[i], pr)]
        piv.append(col); r += 1
    pivset = set(piv); free = [c for c in range(nv) if c not in pivset]
    basis = []
    for fc in free:
        v = [0] * nv; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % 3
        basis.append(v)
    d = len(basis)
    nz = None
    if d == 0: nz = False
    elif d <= 14:
        red = []
        ok = True
        for f in forms:
            co = [sum(a * b for a, b in zip(f, bv)) % 3 for bv in basis]
            if not any(co): ok = False; break
            red.append((max(i for i in range(d) if co[i]), co))
        if not ok: nz = False
        else:
            bylast = [[] for _ in range(d)]
            for last, co in red: bylast[last].append(co)
            z = [0] * d; found = [False]
            def dfs(i, started):
                if found[0]: return
                if i == d: found[0] = True; return
                for val in ((0, 1) if not started else (0, 1, 2)):
                    z[i] = val
                    if all(sum(a * b for a, b in zip(co, z[:i + 1])) % 3 for co in bylast[i]): dfs(i + 1, started or val != 0)
                    if found[0]: return
                z[i] = 0
            dfs(0, False); nz = found[0]
    return {"rank": r, "lift_dim": d, "nowhere_zero_lift": nz}
def collinear_stats(points):
    # points: list of K row points in F7^3 ; collinear triples and max collinear set
    trip = 0; lines = {}
    for a, b, c in itertools.combinations(range(K), 3):
        u = [(points[b][t] - points[a][t]) % q for t in range(3)]
        v = [(points[c][t] - points[a][t]) % q for t in range(3)]
        cross = [(u[1] * v[2] - u[2] * v[1]) % q, (u[2] * v[0] - u[0] * v[2]) % q, (u[0] * v[1] - u[1] * v[0]) % q]
        if not any(cross): trip += 1
    mx = 2
    for size in (4, 5, 6, 7):
        for S in itertools.combinations(range(K), size):
            a = S[0]; ok = True
            u = None
            for b in S[1:]:
                w = [(points[b][t] - points[a][t]) % q for t in range(3)]
                if u is None: u = w; continue
                cross = [(u[1] * w[2] - u[2] * w[1]) % q, (u[2] * w[0] - u[0] * w[2]) % q, (u[0] * w[1] - u[1] * w[0]) % q]
                if any(cross): ok = False; break
            if ok: mx = size; break
    if trip and mx < 3: mx = 3
    return trip, mx
def fam_A():
    f = [[0] * K] + [[rng.randrange(q) for _ in range(K)] for _ in range(2)]
    beta = [[(i * c + f[t][i]) % q for t in range(3) for c in range(q)] for i in range(K)]
    beta = [[(beta[i][col] - beta[0][col]) % q for col in range(n)] for i in range(K)]
    pts = [(i, f[1][i], f[2][i]) for i in range(K)]
    return beta, pts
def fam_B():
    a = [list(range(K))] + [rng.sample(range(K), K) for _ in range(2)]
    b = [[0] * K] + [[rng.randrange(q) for _ in range(K)] for _ in range(2)]
    beta = [[(a[t][i] * c + b[t][i]) % q for t in range(3) for c in range(q)] for i in range(K)]
    beta = [[(beta[i][col] - beta[0][col]) % q for col in range(n)] for i in range(K)]
    return beta, None
out = {"seed": seed, "samples_per_family": NS, "A": [], "B": []}
for name, gen in (("A", fam_A), ("B", fam_B)):
    for s in range(NS):
        if over(): out["status"] = "INCOMPLETE_BUDGET"; break
        beta, pts = gen()
        res = lift_rank(beta)
        if res is None: out[name].append({"valid": False}); continue
        rec = dict(res)
        if pts is not None:
            tr, mx = collinear_stats(pts); rec["affine_triples"] = tr; rec["max_collinear"] = mx
        out[name].append(rec)
def summ(lst, key):
    h = {}
    for r in lst:
        k = json.dumps({kk: r.get(kk) for kk in key}, sort_keys=True); h[k] = h.get(k, 0) + 1
    return h
out["A_summary"] = summ(out["A"], ["affine_triples", "max_collinear", "lift_dim", "nowhere_zero_lift"])
out["B_summary"] = summ(out["B"], ["lift_dim", "nowhere_zero_lift"])
out.setdefault("status", "OK")
out["wall_s"] = round(time.monotonic() - T0, 3)
del out["A"]; del out["B"]
print(json.dumps(out, sort_keys=True))
