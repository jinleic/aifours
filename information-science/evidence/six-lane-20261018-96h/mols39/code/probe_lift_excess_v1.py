#!/usr/bin/env python3
"""probe_lift_excess_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; no search, no candidate).
For each pinned orbit-model JSON (format of models/*_orb.json: n, k, gens [[mu, perm]], orbit_types [{name, stab_gens,
mult, fixed_coords}]) with n = 3q, gcd(3,q) = 1, computes exact counts for the G-EQUIVARIANT mod-3 lift system:
  E  = number of G-orbits on Phi = {(x,y,t): x<y, t in Z_q}, where g = (mu, pi) maps (x,y,t) to (pi x, pi y, mu t) and a
       reversed pair is identified via (y,x,t) ~ (x,y,-t)   [one fibre-sum equation per orbit];
  U  = sum over orbit types of mult * dim_F3{a in F_3^k : a_x = 0 for x in fixed_coords, a_(pi_h x) = (mu_h mod 3) a_x
       for every stabiliser generator h}   [equivariant lift unknowns of one representative per column orbit];
  C0 = dim_F3{e in F_3^k : e_x = 0 for x in Z, e_(pi_g x) = (mu_g mod 3) e_x for all generators g}, Z = rows forced to 0
       in EVERY orbit type (normalised zero rows)   [equivariant row constants, always solutions];
  excess = U - C0 - E  (negative: the generic in-model skeleton has only trivial equivariant lifts).
Exactness caveat recorded in the output: E and U are exact counts; 'generic rank' reasoning from them is heuristic.
Args: models_json_list_path list_sha budget_s"""
import sys, json, hashlib, time
T0 = time.monotonic()
lp, lsha, BUD = sys.argv[1], sys.argv[2], float(sys.argv[3])
lb = open(lp, 'rb').read()
if hashlib.sha256(lb).hexdigest() != lsha: print(json.dumps({"status": "INPUT_PIN_MISMATCH"})); sys.exit(2)
def nullity_f3(rows, ncols):
    piv = []
    m = [list(r) for r in rows]
    rank = 0; col = 0
    while rank < len(m) and col < ncols:
        p = next((i for i in range(rank, len(m)) if m[i][col] % 3), None)
        if p is None: col += 1; continue
        m[rank], m[p] = m[p], m[rank]
        inv = 1 if m[rank][col] % 3 == 1 else 2
        m[rank] = [(v * inv) % 3 for v in m[rank]]
        for i in range(len(m)):
            if i != rank and m[i][col] % 3:
                f = m[i][col]
                m[i] = [(a - f * b) % 3 for a, b in zip(m[i], m[rank])]
        rank += 1; col += 1
    return ncols - rank
def constraints(k, zero_rows, gens):
    rows = []
    for x in zero_rows:
        r = [0] * k; r[x] = 1; rows.append(r)
    for (mu, perm) in gens:
        e = mu % 3
        for x in range(k):
            r = [0] * k
            r[perm[x]] = (r[perm[x]] + 1) % 3
            r[x] = (r[x] - e) % 3
            if any(r): rows.append(r)
    return rows
out = {"status": "OK", "results": []}
for item in json.loads(lb):
    raw = open(item["path"], 'rb').read()
    if hashlib.sha256(raw).hexdigest() != item["sha256"]:
        out["results"].append({"name": item["path"], "status": "INPUT_PIN_MISMATCH"}); continue
    M = json.loads(raw); n, k = M["n"], M["k"]
    res = {"model": M.get("name"), "n": n, "k": k}
    if n % 3 or (n // 3) % 3 == 0:
        res["status"] = "SKIP_NOT_3_PARALLEL_N"; out["results"].append(res); continue
    q = n // 3
    gens = [(g[0] % n, list(g[1])) for g in M["gens"]]
    # orbits on Phi by BFS
    def canon(x, y, t):
        return (x, y, t % q) if x < y else (y, x, (-t) % q)
    seen = set(); E = 0; orbit_sizes = {}
    for x in range(k):
        for y in range(x + 1, k):
            for t in range(q):
                s = canon(x, y, t)
                if s in seen: continue
                E += 1; stack = [s]; seen.add(s); sz = 0
                while stack:
                    a, b, tt = stack.pop(); sz += 1
                    for (mu, perm) in gens:
                        nx = canon(perm[a], perm[b], mu * tt)
                        if nx not in seen: seen.add(nx); stack.append(nx)
                orbit_sizes[sz] = orbit_sizes.get(sz, 0) + 1
    U = 0; per_type = []
    zero_rows_all = None
    for ot in M["orbit_types"]:
        fz = sorted(int(x) for x, v in ot.get("fixed_coords", {}).items() if int(v) == 0)
        sg = [(g[0] % n, list(g[1])) for g in ot.get("stab_gens", [])]
        d = nullity_f3(constraints(k, fz, sg), k)
        per_type.append({"type": ot["name"], "mult": ot["mult"], "dim": d, "fixed_zero_rows": fz})
        U += ot["mult"] * d
        zs = set(fz) if ot["name"] != "zero" else None
        if zs is not None:
            zero_rows_all = zs if zero_rows_all is None else (zero_rows_all & zs)
    Z = sorted(zero_rows_all or [])
    C0 = nullity_f3(constraints(k, Z, gens), k)
    ncols = sum(ot["mult"] * 1 for ot in M["orbit_types"])
    res.update({"status": "OK", "q": q, "E": E, "phi_orbit_size_hist": orbit_sizes, "U": U, "C0": C0, "zero_rows_in_all_types": Z,
                "excess": U - C0 - E, "per_type": per_type, "column_orbits": ncols,
                "caveat": "E, U, C0 exact; any generic-rank conclusion is heuristic"})
    out["results"].append(res)
    if time.monotonic() - T0 > BUD: out["status"] = "INCOMPLETE_BUDGET"; break
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
