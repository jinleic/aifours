#!/usr/bin/env python3
"""w8_flat_planes_couples_v2: float stdlib EXPLORATION (evidence only, never a proof premise) for the W8 decision note.

Supersedes the classification step of z5_flat_rank2_projectors_v1 (whose MUB-pair test used a 1e-6 block-norm threshold;
at the degenerate MUB-pair zeros LM stops at residual ~1e-12 with displacements ~1e-6, so that test mislabelled them).

Stage S (search, ~110 s): LM on P = (2/5) I + sum_k sum_m (a_{k,m}/5) psi^k_m psi^k_m^* (flat in Z, X, T by
construction; psi^k_m(t) = zeta^(3 k t^2 + m t)/sqrt5, k = 1, 2, 3), residual P^2 - P, random starts. Endpoint with
residual < 1e-11: MUB-pair if within 1e-3 (Frobenius) of one of the 30 projectors onto two vectors of one psi^k basis;
otherwise polished (LM, 300 iterations, tol 1e-14) and kept as EXOTIC if residual < 1e-13 and rank-2 projector
(trace 2, ||P^2 - P|| < 1e-12); exotic endpoints clustered at 1e-7.
Stage O: closure of the exotic list under conjugation by the 25 Weyl-Heisenberg operators X^a Z^c.
Stage C (couples): for every flat plane S_r (orbit representative under WH translations) and every listed plane S_s and
basis b in {Z, X, T}: the W8 couple condition needs V in U(2) with (e^* F_r) V (e^* F_s)^* = 0 for all e in b
(F = orthonormal frame). M = 5 x 4 matrix of these linear forms; compatible iff smallest eigenvalue of M^* M < 1e-18
(relative) and its kernel vector is proportional to a unitary (defect < 1e-6); kernel dimension >= 2 flagged.
Stage K (K4): all assignments of listed planes to the representatives 00, 01, 10, 11 with all six couples compatible
(Z: 00-01, 10-11; X: 00-10, 01-11; T: 00-11, 01-10), plane(00) an orbit representative (WH translation symmetry);
for each, frames U_r from the kernels at 00 and the remaining three couples tested; any survivor is verified on the
full 10 x 10 configuration (rows, columns, Cayley classes of Z_5 x Z_2) and its rays counted.
Standard library only; self budget 280 s; output JSON (exclusive) argv[1]; seed fixed.
"""
import cmath, json, math, random, sys, time

T0 = time.monotonic()
BUDGET = 280.0
OUT = sys.argv[1]
N = 5
Z5 = cmath.exp(2j * math.pi / 5)
R5 = math.sqrt(5.0)


def zp(e):
    return Z5 ** (e % 5)


def vec_k(k, m):
    return [zp(3 * k * t * t + m * t) / R5 for t in range(N)]


BASES = {"Z": [[1.0 + 0j if t == s else 0j for t in range(N)] for s in range(N)],
         "X": [[zp(n * t) / R5 for t in range(N)] for n in range(N)],
         "T": [vec_k(4, m) for m in range(N)]}
COMP = {k: [vec_k(k, m) for m in range(N)] for k in (1, 2, 3)}


def outer(u):
    return [[u[i] * u[j].conjugate() for j in range(N)] for i in range(N)]


def mm(A, B):
    return [[sum(A[i][l] * B[l][j] for l in range(N)) for j in range(N)] for i in range(N)]


def madd(A, B, s=1.0):
    return [[A[i][j] + s * B[i][j] for j in range(N)] for i in range(N)]


def mdist(A, B):
    return math.sqrt(sum(abs(A[i][j] - B[i][j]) ** 2 for i in range(N) for j in range(N)))


def dag(A):
    return [[A[j][i].conjugate() for j in range(N)] for i in range(N)]


def herm_reals(M):
    out = [M[i][i].real for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            out.append(M[i][j].real)
            out.append(M[i][j].imag)
    return out


PROJ = {k: [outer(COMP[k][m]) for m in range(N)] for k in (1, 2, 3)}
GEN = []
for k in (1, 2, 3):
    for i in range(4):
        GEN.append([[x / 5.0 for x in row] for row in madd(PROJ[k][i], PROJ[k][4], -1.0)])
I5 = [[1.0 + 0j if i == j else 0j for j in range(N)] for i in range(N)]


def P_of(c):
    P = [[0.4 * I5[i][j] for j in range(N)] for i in range(N)]
    for ci, G in zip(c, GEN):
        for i in range(N):
            for j in range(N):
                P[i][j] += ci * G[i][j]
    return P


def resid(c):
    P = P_of(c)
    return P, herm_reals(madd(mm(P, P), P, -1.0))


def jac(P):
    return [list(r) for r in zip(*[herm_reals(madd(madd(mm(G, P), mm(P, G)), G, -1.0)) for G in GEN])]


def solve(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(M[r][col]))
        if abs(M[piv][col]) < 1e-300:
            return None
        M[col], M[piv] = M[piv], M[col]
        for r in range(n):
            if r != col:
                f = M[r][col] / M[col][col]
                if f != 0.0:
                    for cc in range(col, n + 1):
                        M[r][cc] -= f * M[col][cc]
    return [M[i][n] / M[i][i] for i in range(n)]


def lm(c, iters=150, tol=1e-12):
    lam = 1e-3
    P, r = resid(c)
    nr = sum(x * x for x in r)
    for it in range(1, iters + 1):
        if math.sqrt(nr) < tol:
            return c, math.sqrt(nr), it, "CONVERGED"
        J = jac(P)
        A = [[sum(J[k][i] * J[k][j] for k in range(25)) for j in range(12)] for i in range(12)]
        g = [sum(J[k][i] * r[k] for k in range(25)) for i in range(12)]
        while True:
            Ad = [[A[i][j] + (lam * (A[i][i] + 1e-12) if i == j else 0.0) for j in range(12)] for i in range(12)]
            step = solve(Ad, [-x for x in g])
            if step is not None:
                c2 = [c[i] + step[i] for i in range(12)]
                P2, r2 = resid(c2)
                n2 = sum(x * x for x in r2)
                if n2 < nr:
                    c, P, r, nr = c2, P2, r2, n2
                    lam = max(lam / 3.0, 1e-15)
                    break
            lam *= 4.0
            if lam > 1e12:
                return c, math.sqrt(nr), it, "STALL"
    return c, math.sqrt(nr), iters, ("CONVERGED" if math.sqrt(nr) < tol else "MAX_ITER")


def jacobi_eig(S):
    n = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(60):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-32:
            break
        for p in range(n):
            for q in range(p + 1, n):
                if abs(A[p][q]) < 1e-300:
                    continue
                th = 0.5 * math.atan2(2 * A[p][q], A[q][q] - A[p][p])
                cs, sn = math.cos(th), math.sin(th)
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p], A[k][q] = cs * akp - sn * akq, sn * akp + cs * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k], A[q][k] = cs * apk - sn * aqk, sn * apk + cs * aqk
                for k in range(n):
                    vkp, vkq = V[k][p], V[k][q]
                    V[k][p], V[k][q] = cs * vkp - sn * vkq, sn * vkp + cs * vkq
    order = sorted(range(n), key=lambda i: A[i][i])
    return [A[i][i] for i in order], [[V[k][i] for k in range(n)] for i in order]


# ---------------------------------------------------------------- MUB-pair projectors and WH operators
MUBP = []
for k in (1, 2, 3):
    for m1 in range(N):
        for m2 in range(m1 + 1, N):
            MUBP.append(("MUB", k, m1, m2, madd(PROJ[k][m1], PROJ[k][m2])))
WH = {}
for a in range(N):
    for c_ in range(N):
        W = [[0j] * N for _ in range(N)]
        for t in range(N):
            W[(t + a) % N][t] = zp(c_ * t)                     # X^a Z^c e_t = zeta^(c t) e_(t+a)
        WH[(a, c_)] = W


def near_mub(P):
    best = min(range(len(MUBP)), key=lambda i: mdist(P, MUBP[i][4]))
    return best, mdist(P, MUBP[best][4])


# ---------------------------------------------------------------- stage S
rng = random.Random(20261020)
exotic, runs, stat, mubhits, exotic_hits, unconv = [], 0, {}, 0, 0, 0
min_mub_dist_exotic = None
while time.monotonic() - T0 < 110.0:
    c0 = [rng.gauss(0.0, rng.choice([0.3, 1.0, 2.0])) for _ in range(12)]
    c, res, it, st = lm(c0)
    runs += 1
    stat[st] = stat.get(st, 0) + 1
    if res >= 1e-11:
        unconv += 1
        continue
    P = P_of(c)
    bi, bd = near_mub(P)
    if bd < 1e-3:
        mubhits += 1
        continue
    c, res, it, st = lm(c, iters=300, tol=1e-14)
    P = P_of(c)
    R2 = madd(mm(P, P), P, -1.0)
    rn = math.sqrt(sum(abs(R2[i][j]) ** 2 for i in range(N) for j in range(N)))
    tr = sum(P[i][i].real for i in range(N))
    if rn > 1e-12 or abs(tr - 2.0) > 1e-12:
        unconv += 1
        continue
    exotic_hits += 1
    md = near_mub(P)[1]
    min_mub_dist_exotic = md if min_mub_dist_exotic is None else min(min_mub_dist_exotic, md)
    for e in exotic:
        if mdist(P, e["P"]) < 1e-7:
            e["count"] += 1
            break
    else:
        exotic.append({"P": P, "c": c, "count": 1, "resid": rn})

# ---------------------------------------------------------------- stage O: WH-translation closure
def find_plane(P, plist, tol=1e-6):
    for i, Q in enumerate(plist):
        if mdist(P, Q) < tol:
            return i
    return None


planes = [x[4] for x in MUBP] + [e["P"] for e in exotic]
ptype = ["MUB"] * len(MUBP) + ["EXOTIC"] * len(exotic)
nM = len(MUBP)
perm, closure_missing = {}, 0
for w, W in WH.items():
    Wd = dag(W)
    row = []
    for i, P in enumerate(planes):
        j = find_plane(mm(mm(W, P), Wd), planes)
        if j is None:
            closure_missing += 1
        row.append(j)
    perm[w] = row
orbit_rep, reps = [None] * len(planes), []
for i in range(len(planes)):
    if orbit_rep[i] is not None:
        continue
    reps.append(i)
    for w in WH:
        j = perm[w][i]
        if j is not None and orbit_rep[j] is None:
            orbit_rep[j] = i

# ---------------------------------------------------------------- frames
def frame(P):
    cols = [[P[i][j] for i in range(N)] for j in range(N)]
    j1 = max(range(N), key=lambda j: sum(abs(x) ** 2 for x in cols[j]))
    v1 = cols[j1]
    n1 = math.sqrt(sum(abs(x) ** 2 for x in v1))
    v1 = [x / n1 for x in v1]
    best, bv = -1.0, None
    for j in range(N):
        pr = sum(v1[i].conjugate() * cols[j][i] for i in range(N))
        w = [cols[j][i] - pr * v1[i] for i in range(N)]
        nw = math.sqrt(sum(abs(x) ** 2 for x in w))
        if nw > best:
            best, bv = nw, [x / nw for x in w]
    return [v1, bv]


FR = [frame(P) for P in planes]


def rowvec(fr, e):
    return [sum(e[i].conjugate() * fr[c][i] for i in range(N)) for c in range(2)]


def couple_test(r, s, b):
    """(lambda_min_rel, lambda_2_rel, unitary_defect, K) for the linear system (e^* F_r) V (e^* F_s)^* = 0, e in b."""
    rows = []
    for e in BASES[b]:
        u, v = rowvec(FR[r], e), rowvec(FR[s], e)
        rows.append([u[i] * v[j].conjugate() for i in range(2) for j in range(2)])
    G = [[sum(rows[e][p].conjugate() * rows[e][q] for e in range(5)) for q in range(4)] for p in range(4)]
    Rm = [[0.0] * 8 for _ in range(8)]
    for p in range(4):
        for q in range(4):
            Rm[p][q] = G[p][q].real
            Rm[p][q + 4] = -G[p][q].imag
            Rm[p + 4][q] = G[p][q].imag
            Rm[p + 4][q + 4] = G[p][q].real
    ev, evec = jacobi_eig(Rm)
    scale = max(ev[-1], 1e-300)
    x = evec[0]
    Kv = [complex(x[p], x[p + 4]) for p in range(4)]
    K = [[Kv[0], Kv[1]], [Kv[2], Kv[3]]]
    KK = [[sum(K[i][l].conjugate() * K[i][j] for i in range(2)) for j in range(2)] for l in range(2)]
    t = (KK[0][0].real + KK[1][1].real) / 2
    defect = math.sqrt(abs(KK[0][0] - t) ** 2 + abs(KK[1][1] - t) ** 2 + 2 * abs(KK[0][1]) ** 2) / max(t, 1e-300)
    # eigenvalues of the real embedding come in pairs; ev[0], ev[1] = smallest complex eigenvalue, ev[2], ev[3] = next
    return ev[0] / scale, ev[2] / scale, defect, K


COMPAT = {}                                      # (rep r, s, b) -> bool
stats_c = {"tests": 0, "rank_deficient": 0, "compatible": 0, "kernel_ge2": 0, "tests_expected": len(reps) * len(planes) * 3}
for r in reps:
    for s in range(len(planes)):
        for b in ("Z", "X", "T"):
            if time.monotonic() - T0 > BUDGET - 40:
                continue
            l1, l2, dfc, K = couple_test(r, s, b)
            stats_c["tests"] += 1
            ok = False
            if l1 < 1e-18:
                stats_c["rank_deficient"] += 1
                if l2 < 1e-18:
                    stats_c["kernel_ge2"] += 1
                    ok = True                    # treated as compatible (conservative), flagged
                elif dfc < 1e-6:
                    ok = True
            if ok:
                stats_c["compatible"] += 1
            COMPAT[(r, s, b)] = ok
compat_types = {}
for (r, s, b), ok in COMPAT.items():
    if ok:
        key = "%s-%s-%s" % (ptype[r], ptype[s], b)
        compat_types[key] = compat_types.get(key, 0) + 1

# full adjacency by WH translation (compatibility is invariant under simultaneous conjugation by X^a Z^c)
w_to_rep = []
for r in range(len(planes)):
    w_to_rep.append(next((w for w in WH if perm[w][r] == orbit_rep[r]), None))
ADJ = {b: [set() for _ in planes] for b in ("Z", "X", "T")}
undecided = 0
for r in range(len(planes)):
    w = w_to_rep[r]
    for s in range(len(planes)):
        for b in ("Z", "X", "T"):
            s2 = perm[w][s] if w is not None else None
            val = COMPAT.get((orbit_rep[r], s2, b)) if s2 is not None else None
            if val is None:
                undecided += 1
            elif val:
                ADJ[b][r].add(s)


def full_verify(X):
    """X[r] (r = 2 i2 + j2): 5 x 2 lists; full 10 x 10 configuration on Cay(Z_5 x Z_2); returns (maxdev, rays)."""
    cells = {}
    for i1 in range(N):
        for i2 in range(2):
            for j1 in range(N):
                for j2 in range(2):
                    W = WH[(i1, j1)]
                    Xr = X[2 * i2 + j2]
                    q = []
                    for t in range(N):
                        for cc in range(2):
                            q.append(sum(W[t][u] * Xr[u][cc] for u in range(N)))
                    cells[((i1, i2), (j1, j2))] = q
    lines = {}
    for (a, b_) in cells:
        lines.setdefault(("r", a), []).append((a, b_))
        lines.setdefault(("c", b_), []).append((a, b_))
        lines.setdefault(("s", ((a[0] + b_[0]) % N, (a[1] + b_[1]) % 2)), []).append((a, b_))
    md = 0.0
    for L in lines.values():
        for x in range(len(L)):
            for y in range(len(L)):
                g = sum(cells[L[x]][i].conjugate() * cells[L[y]][i] for i in range(10))
                md = max(md, abs(g - (1.0 if x == y else 0.0)))
    keys = list(cells)
    reps_ = []
    for k_ in keys:
        v = cells[k_]
        nv = math.sqrt(sum(abs(z) ** 2 for z in v))
        for u in reps_:
            if 1.0 - abs(sum(u[i].conjugate() * v[i] for i in range(10))) ** 2 / max(nv * nv, 1e-300) < 1e-7:
                break
        else:
            reps_.append(v)
    return md, len(reps_)


assign, survivors, frame_checked, solutions, ker2_flags = 0, [], 0, [], 0
k4_incomplete = False
MINREM = [None]
for p00 in reps:
    for p01 in ADJ["Z"][p00]:
        for p10 in ADJ["X"][p00] & ADJ["T"][p01]:
            for p11 in ADJ["T"][p00] & ADJ["X"][p01] & ADJ["Z"][p10]:
                if time.monotonic() - T0 > BUDGET:
                    k4_incomplete = True
                    break
                assign += 1
                rec = {"00": p00, "01": p01, "10": p10, "11": p11,
                       "types": [ptype[p00], ptype[p01], ptype[p10], ptype[p11]]}
                # frames: U_00 = I, U_s = sqrt2 K^* from the 1-dim kernels at 00; then the three other couples
                U = {"00": [[1 + 0j, 0j], [0j, 1 + 0j]]}
                kflag = False
                for (s_lab, ps, b) in (("01", p01, "Z"), ("10", p10, "X"), ("11", p11, "T")):
                    l1, l2, dfc, K = couple_test(p00, ps, b)
                    if l2 < 1e-18:
                        kflag = True
                    U[s_lab] = [[math.sqrt(2) * K[j][i].conjugate() for j in range(2)] for i in range(2)]
                if kflag:
                    ker2_flags += 1
                    rec["kernel_ge2_at_00"] = True
                worst = 0.0
                pl = {"00": p00, "01": p01, "10": p10, "11": p11}
                for (ra, sa, b) in (("01", "11", "X"), ("10", "11", "Z"), ("01", "10", "T")):
                    V = [[sum(U[ra][i][l] * U[sa][j][l].conjugate() for l in range(2)) for j in range(2)] for i in range(2)]
                    for e in BASES[b]:
                        u, v = rowvec(FR[pl[ra]], e), rowvec(FR[pl[sa]], e)
                        val = sum(u[i] * V[i][j] * v[j].conjugate() for i in range(2) for j in range(2))
                        worst = max(worst, abs(val))
                frame_checked += 1
                rec["remaining_couples_max_residual"] = worst
                MINREM[0] = worst if MINREM[0] is None else min(MINREM[0], worst)
                if worst < 1e-9 and not kflag:
                    X = []
                    for lab in ("00", "01", "10", "11"):
                        F = FR[pl[lab]]
                        X.append([[sum(F[l][t] * U[lab][l][cc] for l in range(2)) / math.sqrt(2) for cc in range(2)] for t in range(N)])
                    md, ry = full_verify(X)
                    rec["full_maxdev"], rec["full_rays"] = md, ry
                    solutions.append(rec)
                if len(survivors) < 50:
                    survivors.append(rec)

cls_counts = {"MUB_pair_planes": nM, "exotic_planes": len(exotic)}
out = {"probe": "w8_flat_planes_couples_v2", "kind": "float stdlib exploration; evidence only",
       "search": {"runs": runs, "status": stat, "unconverged_or_rejected": unconv, "mub_pair_endpoints": mubhits,
                  "exotic_endpoints": exotic_hits, "distinct_exotic": len(exotic),
                  "exotic_multiplicities": sorted(e["count"] for e in exotic),
                  "min_frobenius_distance_exotic_to_mub_pair": min_mub_dist_exotic},
       "closure": {"planes": len(planes), "missing_images_under_WH": closure_missing, "orbit_representatives": len(reps),
                   "orbit_rep_types": [ptype[i] for i in reps]},
       "couples": {"stats": stats_c, "compatible_by_type_and_basis": compat_types},
       "K4": {"assignments_all_six_couples_compatible": assign, "incomplete_by_budget": k4_incomplete,
              "undecided_adjacency_lookups": undecided,
              "frame_checked": frame_checked, "kernel_ge2_flags": ker2_flags, "solutions": solutions,
              "survivors_first50": survivors, "min_remaining_residual_all": MINREM[0]},
       "exotic_a_blocks": [[[round(x, 12) for x in (e["c"][4 * k:4 * k + 4] + [-sum(e["c"][4 * k:4 * k + 4])])] for k in range(3)]
                           for e in exotic[:60]],
       "classes": cls_counts, "elapsed_s": round(time.monotonic() - T0, 3)}
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("search", "closure", "couples", "classes", "elapsed_s")}))
print(json.dumps({"K4_assignments": assign, "incomplete": k4_incomplete, "undecided": undecided, "frame_checked": frame_checked,
                  "kernel_ge2_flags": ker2_flags, "solutions": len(solutions),
                  "min_remaining_residual_all": MINREM[0]}))
