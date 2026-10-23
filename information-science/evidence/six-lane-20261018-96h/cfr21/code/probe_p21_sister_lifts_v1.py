#!/usr/bin/env python3
"""probe_p21_sister_lifts_v1.py (ContinueCFR21; frozen before execution; stdlib only; self wall budget).
Calibration of the CRT/fibre-orthogonality representation on GENERIC known positives (the 96 pinned P21 DM6):
for each DM take its mod-7 image beta (row0 = 0), solve the EXACT F3 lift system (fibre triple-sum equations +
nowhere-zero inequalities; gauge alpha_0 = 0 and alpha_x(col 0) = 0), enumerate ALL nowhere-zero lifts up to the
global sign z -> -z (cap per DM), rebuild each Z21 matrix by CRT, verify it directly as a DM, and classify its 20
row triples by a canonical form under <unit conjugation C_u, A: f(x)->f(-x)+x, I: f->f^-1, T_a: f(x)->f(x+a)-f(a)>
against the triple classes of the 96 P21 DMs themselves.  Output: one JSON object.
Args: p21-detail.json sha256 budget_seconds cap_per_dm"""
import sys, json, time, hashlib, itertools
T0 = time.monotonic()
path, want, BUD, CAP = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
raw = open(path, 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
d = json.loads(raw); n = 21; q = 7
UNITS = [u for u in range(1, n) if all(u % p for p in (3, 7))]
def over(): return time.monotonic() - T0 > BUD
def is_dm(D):
    return all(sorted((D[i][c] - D[j][c]) % n for c in range(n)) == list(range(n)) for i in range(len(D)) for j in range(len(D)) if i != j)
def lift_system(beta):
    kk = len(beta); var = {}
    for x in range(1, kk):
        for c in range(1, n): var[(x, c)] = len(var)
    nv = len(var); eqs = []; forms = []
    for x in range(kk):
        for xp in range(x + 1, kk):
            fib = {}
            for c in range(n): fib.setdefault((beta[x][c] - beta[xp][c]) % q, []).append(c)
            if len(fib) != q or any(len(v) != 3 for v in fib.values()): return None
            for F in fib.values():
                e = [0] * nv
                for c in F:
                    if (x, c) in var: e[var[(x, c)]] = (e[var[(x, c)]] + 1) % 3
                    if (xp, c) in var: e[var[(xp, c)]] = (e[var[(xp, c)]] - 1) % 3
                eqs.append(e)
                f = [0] * nv
                for c, s in ((F[0], 1), (F[1], -1)):
                    if (x, c) in var: f[var[(x, c)]] = (f[var[(x, c)]] + s) % 3
                    if (xp, c) in var: f[var[(xp, c)]] = (f[var[(xp, c)]] - s) % 3
                forms.append(f)
    M = [e[:] for e in eqs]; piv = []; r = 0
    for col in range(nv):
        p = next((i for i in range(r, len(M)) if M[i][col]), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        if M[r][col] == 2: M[r] = [(2 * v) % 3 for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][col]:
                fct = M[i][col]; M[i] = [(a - fct * b) % 3 for a, b in zip(M[i], M[r])]
        piv.append(col); r += 1
        if r == len(M): break
    pivset = set(piv); free = [c for c in range(nv) if c not in pivset]
    basis = []
    for fc in free:
        v = [0] * nv; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = (-M[i][fc]) % 3
        basis.append(v)
    return var, basis, forms, len(eqs), r
def nowhere_zero_all(basis, forms, cap):
    dd = len(basis); red = []
    for f in forms:
        co = [sum(a * b for a, b in zip(f, bv)) % 3 for bv in basis]
        if not any(co): return [], True, "ZERO_FORM"
        red.append((max(i for i in range(dd) if co[i]), co))
    bylast = [[] for _ in range(dd)]
    for last, co in red: bylast[last].append(co)
    sols = []; z = [0] * dd; capped = [False]
    def dfs(i, started):
        if len(sols) >= cap: capped[0] = True; return
        if i == dd:
            sols.append(z[:]); return
        for val in ((0, 1) if not started else (0, 1, 2)):
            z[i] = val
            if all(sum(a * b for a, b in zip(co, z[:i + 1])) % 3 for co in bylast[i]):
                dfs(i + 1, started or val != 0)
            if capped[0]: break
        z[i] = 0
    dfs(0, False)
    return sols, capped[0], "OK"
def build(var, basis, z, beta):
    kk = len(beta); alpha = [[0] * n for _ in range(kk)]
    for (x, c), idx in var.items(): alpha[x][c] = sum(z[j] * basis[j][idx] for j in range(len(basis))) % 3
    return [[(7 * alpha[x][c] + 15 * beta[x][c]) % n for c in range(n)] for x in range(kk)]
# 7*a: 7 = 1 mod 3, 0 mod 7 ; 15*b: 15 = 0 mod 3, 1 mod 7
def inverse(f):
    g = [0] * n
    for x in range(n): g[f[x]] = x
    return tuple(g)
def gens(f):
    yield tuple((f[(-x) % n] + x) % n for x in range(n))
    yield inverse(f)
    for u in UNITS:
        ui = pow(u, -1, n); yield tuple((u * f[(ui * x) % n]) % n for x in range(n))
    for a in range(1, n):
        yield tuple((f[(x + a) % n] - f[a]) % n for x in range(n))
canon_cache = {}
def canon(f):
    f = tuple(f)
    if f in canon_cache: return canon_cache[f]
    seen = {f}; frontier = [f]
    while frontier:
        nf = []
        for g in frontier:
            for h in gens(g):
                if h not in seen: seen.add(h); nf.append(h)
        frontier = nf
    m = min(seen)
    for g in seen: canon_cache[g] = m
    return m
def triple_canons(D):
    out = []
    for a, b, c in itertools.combinations(range(len(D)), 3):
        E = [[(D[x][col] - D[a][col]) % n for col in range(n)] for x in range(len(D))]
        colof = {E[b][col]: col for col in range(n)}
        f = [(E[c][colof[s]] - E[c][colof[0]]) % n for s in range(n)]
        out.append(canon(f))
    return out
ref = set(); ref_orbit_sizes = {}
for dm in d["dms"]:
    for t in triple_canons(dm["rows"]): ref.add(t)
res = {"status": "OK", "input_sha256": got, "p21_triple_classes": len(ref), "per_dm": []}
new_classes = {}; sister_profiles = {}; incomplete = False; total_sisters = 0; nonp21_sisters = 0
for dm in d["dms"]:
    if over(): incomplete = True; break
    R = dm["rows"]; beta = [[(R[i][c] - R[0][c]) % q for c in range(n)] for i in range(len(R))]
    sysr = lift_system(beta)
    var, basis, forms, neq, rk = sysr
    sols, capped, st = nowhere_zero_all(basis, forms, CAP)
    rec = {"sol": dm["sol"], "equations": neq, "rank": rk, "kernel_dim_after_gauge": len(basis),
           "nowhere_zero_up_to_sign": len(sols), "capped": capped}
    nvalid = 0; nnew = 0
    for z in sols:
        if over(): incomplete = True; break
        D = build(var, basis, z, beta)
        if not is_dm(D): continue
        nvalid += 1; total_sisters += 1
        tc = triple_canons(D)
        newt = [t for t in tc if t not in ref]
        prof = tuple(sorted(tc))
        sister_profiles.setdefault(prof, {"count": 0, "example_dm": D, "from_sol": dm["sol"]})
        sister_profiles[prof]["count"] += 1
        if newt:
            nnew += 1; nonp21_sisters += 1
            for t in newt: new_classes.setdefault(t, 0); new_classes[t] += 1
    rec["sisters_verified_dm"] = nvalid; rec["sisters_with_triple_outside_p21_classes"] = nnew
    res["per_dm"].append(rec)
    if incomplete: break
res.update({"incomplete_budget": incomplete, "dms_processed": len(res["per_dm"]), "total_sisters": total_sisters,
            "sisters_with_new_triple_class": nonp21_sisters, "new_triple_classes": len(new_classes),
            "distinct_sister_triple_profiles": len(sister_profiles),
            "new_triple_class_list": [list(t) for t in sorted(new_classes)][:400],
            "profile_examples": [{"count": v["count"], "from_sol": v["from_sol"], "dm": v["example_dm"]} for v in list(sister_profiles.values())[:60]],
            "wall_s": round(time.monotonic() - T0, 3)})
print(json.dumps(res, sort_keys=True))
