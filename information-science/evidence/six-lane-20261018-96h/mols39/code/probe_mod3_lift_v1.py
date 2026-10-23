#!/usr/bin/env python3
"""probe_mod3_lift_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; self budget; analysis of
KNOWN difference matrices only: it cannot produce a new DM row and makes no existence claim).
For a (Z_n,k;1)-DM D with n = 3q, gcd(3,q) = 1, normalised at row r (D'_x = D_x - D_r): beta = D' mod q, alpha = D' mod 3.
By CRT, D' is a DM iff for every pair x<y and t in Z_q the fibre T_xy(t) = {c : beta_x(c)-beta_y(c) = t} has 3 columns
and alpha_x - alpha_y is a bijection on it ('rainbow'). Three elements of Z_3 are pairwise distinct iff their sum is 0 and
two given ones differ. Hence the alpha-lifts of the skeleton beta are exactly the points A of the GF(3)-space
  V(beta) = {A : A_r = 0, sum_{c in T_xy(t)} (A_x(c) - A_y(c)) = 0 for all x<y, t}
with (A_x(c1)-A_y(c1)) != (A_x(c2)-A_y(c2)) for the first two columns c1<c2 of every fibre. Row constants (A_x = e_x) lie
in V and preserve rainbow. The probe reports dim V, m = dim V - (k-1) (dimension modulo row constants), checks that the
true alpha lies in V and is rainbow (sanity), counts fibre functionals that vanish identically on V, and if m <= MMAX
enumerates V / constants and counts rainbow points (= number of mod-3 lifts of beta up to row constants; >= 1).
Inputs: a JSON list of jobs [{name, raw, sha256, n, rows (optional subset of row indices), r}] or the built-in 'singer57'
(8 x 57 DM from the planar difference set B = (1,6,7,9,19,38,42,49) and an OA(8,8) over GF(8) built here:
rows (u,v) in GF(8)^2, entries u + a v for the 8 elements a; non-constant rows only; plus the zero column).
Args: jobs_json_path jobs_sha budget_s mmax"""
import sys, json, hashlib, time
T0 = time.monotonic()
jp, jsha, BUD, MMAX = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
jb = open(jp, 'rb').read()
if hashlib.sha256(jb).hexdigest() != jsha: print(json.dumps({"status": "INPUT_PIN_MISMATCH"})); sys.exit(2)
jobs = json.loads(jb)
def gf8_mul(a, b):
    r = 0
    for i in range(3):
        if (b >> i) & 1: r ^= a << i
    for i in (4, 3):
        if (r >> i) & 1: r ^= 0b1011 << (i - 3)
    return r
def singer57():
    B = (1, 6, 7, 9, 19, 38, 42, 49); cols = []
    for u in range(8):
        for v in range(8):
            R = [u ^ gf8_mul(a, v) for a in range(8)]
            if len(set(R)) == 1: continue
            cols.append([B[x] for x in R])
    cols.append([0] * 8)
    return [[c[x] for c in cols] for x in range(8)]
def is_dm(rows, n):
    k = len(rows)
    return all(len({(rows[i][c] - rows[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
def rank_nullspace(eqs, U):
    # Gaussian elimination over GF(3); eqs: list of dicts {var: coef}; returns rank, pivot rows (reduced), pivot cols
    piv = {}            # col -> reduced row (dict)
    for e in eqs:
        row = {v: c % 3 for v, c in e.items() if c % 3}
        while row:
            col = min(row)
            if col in piv:
                pr = piv[col]; f = row[col] * pow(pr[col], -1, 3) % 3
                for v, c in pr.items():
                    nv = (row.get(v, 0) - f * c) % 3
                    if nv: row[v] = nv
                    else: row.pop(v, None)
            else:
                inv = pow(row[col], -1, 3)
                row = {v: (c * inv) % 3 for v, c in row.items()}
                piv[col] = row; break
    # back-substitute to reduced echelon form
    cols = sorted(piv)
    for col in reversed(cols):
        pr = piv[col]
        for col2 in cols:
            if col2 >= col: break
            r2 = piv[col2]
            if col in r2:
                f = r2[col]
                for v, c in pr.items():
                    nv = (r2.get(v, 0) - f * c) % 3
                    if nv: r2[v] = nv
                    else: r2.pop(v, None)
    free = [v for v in range(U) if v not in piv]
    basis = []
    for fv in free:
        vec = [0] * U; vec[fv] = 1
        for col, pr in piv.items():
            c = pr.get(fv, 0)
            if c: vec[col] = (-c) % 3
        basis.append(vec)
    return len(piv), basis
def analyse(name, rows, n, r):
    q = n // 3; k = len(rows)
    res = {"name": name, "n": n, "k": k, "r": r, "dm_ok": is_dm(rows, n)}
    if not res["dm_ok"] or n % 3 or q % 3 == 0: res["status"] = "SKIP"; return res
    Dp = [[(rows[x][c] - rows[r][c]) % n for c in range(n)] for x in range(k)]
    beta = [[v % q for v in R] for R in Dp]; alpha = [[v % 3 for v in R] for R in Dp]
    others = [x for x in range(k) if x != r]; idx = {x: i for i, x in enumerate(others)}; U = (k - 1) * n
    var = lambda x, c: idx[x] * n + c
    eqs = []; fibres = []
    for i in range(k):
        for j in range(i + 1, k):
            fib = {}
            for c in range(n): fib.setdefault((beta[i][c] - beta[j][c]) % q, []).append(c)
            assert all(len(v) == 3 for v in fib.values()) and len(fib) == q
            for t in range(q):
                T = fib[t]; e = {}
                for c in T:
                    if i != r: e[var(i, c)] = e.get(var(i, c), 0) + 1
                    if j != r: e[var(j, c)] = e.get(var(j, c), 0) - 1
                eqs.append(e); fibres.append((i, j, T))
    rank, basis = rank_nullspace(eqs, U)
    d = U - rank
    res.update({"unknowns": U, "equations": len(eqs), "rank": rank, "dim_V": d, "m_mod_constants": d - (k - 1), "fibres": len(fibres)})
    def val(A, x, c): return 0 if x == r else A[var(x, c)]
    A0 = [0] * U
    for x in others:
        for c in range(n): A0[var(x, c)] = alpha[x][c]
    res["true_alpha_in_V"] = all(sum(v * A0[u] for u, v in e.items()) % 3 == 0 for e in eqs)
    res["true_alpha_rainbow"] = all(len({(val(A0, i, c) - val(A0, j, c)) % 3 for c in T}) == 3 for (i, j, T) in fibres)
    # fibre functionals on V: phi(A) = (A_i(c1)-A_j(c1)) - (A_i(c2)-A_j(c2)), as coefficient vectors over the basis
    def coeffs(vec_of_basis):
        return vec_of_basis
    fun = []
    for (i, j, T) in fibres:
        c1, c2 = T[0], T[1]
        f = []
        for bvec in basis:
            v = (val(bvec, i, c1) - val(bvec, j, c1) - val(bvec, i, c2) + val(bvec, j, c2)) % 3
            f.append(v)
        fun.append(f)
    res["identically_zero_fibre_functionals"] = sum(1 for f in fun if not any(f))
    res["distinct_fibre_functionals_up_to_sign"] = len({tuple(f) if next((x for x in f if x), 1) == 1 else tuple((-x) % 3 for x in f) for f in fun if any(f)})
    m = d - (k - 1)
    if m <= MMAX and time.monotonic() - T0 < BUD:
        # quotient by row constants: choose basis vectors spanning a complement of the constant subspace by evaluating
        # functionals (which vanish on constants); count points z in GF(3)^d with all functionals nonzero, divide by 3^(k-1)
        # restricted to the subspace where functionals depend: enumerate over coordinates of a reduced basis
        # reduce: functional matrix F (fibres x d); its rank equals m if constants span the kernel exactly
        Fcols = list(zip(*fun)) if fun else []
        # find independent columns of F (as vectors in GF(3)^fibres)
        piv = {}; keep = []
        for ci, col in enumerate(Fcols):
            v = {ii: x for ii, x in enumerate(col) if x}
            while v:
                p0 = min(v)
                if p0 in piv:
                    pr = piv[p0]; f = v[p0] * pow(pr[p0], -1, 3) % 3
                    for ii, x in pr.items():
                        nv = (v.get(ii, 0) - f * x) % 3
                        if nv: v[ii] = nv
                        else: v.pop(ii, None)
                else:
                    piv[p0] = v; keep.append(ci); break
        res["functional_rank"] = len(keep)
        if len(keep) <= MMAX:
            # every point of V/ker(F) corresponds to z over the kept coordinates (others set to 0 give all values of F)
            sub = [[f[ci] for ci in keep] for f in fun]
            cnt = 0; tot = 0
            L = len(keep)
            import itertools
            for z in itertools.product(range(3), repeat=L):
                tot += 1
                ok = True
                for f in sub:
                    s = 0
                    for a, b in zip(f, z):
                        if a: s += a * b
                    if s % 3 == 0: ok = False; break
                if ok: cnt += 1
                if (tot & 4095) == 0 and time.monotonic() - T0 > BUD: res["enum_status"] = "INCOMPLETE_BUDGET"; break
            else:
                res["enum_status"] = "COMPLETE"
            res["enum_points"] = tot; res["rainbow_points_mod_kernel"] = cnt
    res["status"] = "OK"
    return res
out = {"status": "OK", "results": []}
for jobd in jobs:
    if time.monotonic() - T0 > BUD: out["status"] = "INCOMPLETE_BUDGET"; break
    if jobd.get("builtin") == "singer57":
        rows = singer57(); n = 57
        if "rows" in jobd: rows = [rows[x] for x in jobd["rows"]]
    else:
        rb = open(jobd["raw"], 'rb').read()
        if hashlib.sha256(rb).hexdigest() != jobd["sha256"]:
            out["results"].append({"name": jobd["name"], "status": "INPUT_PIN_MISMATCH"}); continue
        n = jobd["n"]; rows = [[int(t) % n for t in ln.split()] for ln in rb.decode().splitlines() if ln.strip()]
        if "rows" in jobd: rows = [rows[x] for x in jobd["rows"]]
    out["results"].append(analyse(jobd["name"], rows, n, jobd.get("r", 0)))
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
