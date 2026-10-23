#!/usr/bin/env python3
"""z5_flat_rank2_projectors_v1: float stdlib EXPLORATION (evidence only, never a proof premise) of the rank-2
projectors P on C^5 whose diagonals are flat (2/5) in the three Weyl-Heisenberg bases Z (computational), X (Fourier)
and T (eigenbasis of X Z^-1) used by the W8 ansatz (lane notes w8-wh5-c2-orbit-ansatz-setup-v1.md, addendum 1).

Parametrisation (exact identity, see the W8 decision note): P is flat in Z, X, T iff
  P = (2/5) I + sum_{k=1,2,3} sum_m (a_{k,m} / 5) psi^k_m psi^k_m^*,  sum_m a_{k,m} = 0,
with psi^k_m(t) = zeta^(3 k t^2 + m t) / sqrt5 the eigenbasis of X Z^k (k = 1, 2, 3: the complementary bases).
Unknowns c (12 reals: a_{k,0..3}; a_{k,4} = -sum). Residual: the 25 real components of P^2 - P. Levenberg-Marquardt
with the exact Jacobian G P + P G - G. Converged endpoints (||P^2 - P|| < 1e-12) are flat rank-2 projectors (trace 2
by construction). Classification: MUB-pair if exactly one block a_k is nonzero (P = span of two psi^k vectors);
otherwise NON-MUB-PAIR. Also: first-order kernel dimension of the Jacobian at the 30 MUB-pair points (expected 2 by
the written analysis) and built-in controls (bases orthonormal + mutually unbiased; flatness by construction).
Standard library only; self budget 250 s; output JSON (exclusive) argv[1]; seed fixed.
"""
import cmath, json, math, random, sys, time

T0 = time.monotonic()
BUDGET = 250.0
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


def ip(u, v):
    return sum(u[i].conjugate() * v[i] for i in range(N))


def outer(u):
    return [[u[i] * u[j].conjugate() for j in range(N)] for i in range(N)]


def mm(A, B):
    return [[sum(A[i][l] * B[l][j] for l in range(N)) for j in range(N)] for i in range(N)]


def madd(A, B, s=1.0):
    return [[A[i][j] + s * B[i][j] for j in range(N)] for i in range(N)]


def herm_reals(M):
    out = [M[i][i].real for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            out.append(M[i][j].real)
            out.append(M[i][j].imag)
    return out


# controls: orthonormal and mutually unbiased
allb = dict(BASES)
for k in (1, 2, 3):
    allb["k%d" % k] = COMP[k]
on_dev, mub_dev = 0.0, 0.0
names = list(allb)
for a in names:
    for i in range(N):
        for j in range(N):
            on_dev = max(on_dev, abs(ip(allb[a][i], allb[a][j]) - (1.0 if i == j else 0.0)))
for ia, a in enumerate(names):
    for b in names[ia + 1:]:
        for u in allb[a]:
            for v in allb[b]:
                mub_dev = max(mub_dev, abs(abs(ip(u, v)) ** 2 - 0.2))

PROJ = {k: [outer(COMP[k][m]) for m in range(N)] for k in (1, 2, 3)}
GEN = []
for k in (1, 2, 3):
    for i in range(4):
        GEN.append(madd(PROJ[k][i], PROJ[k][4], -1.0))
GEN = [[[x / 5.0 for x in row] for row in G] for G in GEN]
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
    cols = []
    for G in GEN:
        D = madd(madd(mm(G, P), mm(P, G)), G, -1.0)
        cols.append(herm_reals(D))
    return [list(r) for r in zip(*cols)]                      # 25 x 12


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


def norm2(v):
    return sum(x * x for x in v)


def lm(c, iters=150, tol=1e-12):
    lam = 1e-3
    P, r = resid(c)
    nr = norm2(r)
    status = "MAX_ITER"
    it = 0
    for it in range(1, iters + 1):
        if math.sqrt(nr) < tol:
            status = "CONVERGED"
            break
        J = jac(P)
        A = [[sum(J[k][i] * J[k][j] for k in range(25)) for j in range(12)] for i in range(12)]
        g = [sum(J[k][i] * r[k] for k in range(25)) for i in range(12)]
        while True:
            Ad = [[A[i][j] + (lam * (A[i][i] + 1e-12) if i == j else 0.0) for j in range(12)] for i in range(12)]
            step = solve(Ad, [-x for x in g])
            if step is not None:
                c2 = [c[i] + step[i] for i in range(12)]
                P2, r2 = resid(c2)
                n2 = norm2(r2)
                if n2 < nr:
                    c, P, r, nr = c2, P2, r2, n2
                    lam = max(lam / 3.0, 1e-15)
                    break
            lam *= 4.0
            if lam > 1e12:
                return c, math.sqrt(nr), it, "STALL"
    if status == "MAX_ITER" and math.sqrt(nr) < tol:
        status = "CONVERGED"
    return c, math.sqrt(nr), it, status


def blocks(c):
    out = []
    for k in range(3):
        a = c[4 * k:4 * k + 4]
        out.append(a + [-sum(a)])
    return out


def flat_dev(P):
    d = 0.0
    for b in ("Z", "X", "T"):
        for e in BASES[b]:
            val = sum(e[i].conjugate() * P[i][j] * e[j] for i in range(N) for j in range(N))
            d = max(d, abs(val - 0.4))
    return d


def jacobi_eig(S):
    """symmetric Jacobi: (eigenvalues ascending, matching eigenvectors as lists)."""
    n = len(S)
    A = [row[:] for row in S]
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(100):
        off = sum(A[i][j] ** 2 for i in range(n) for j in range(n) if i != j)
        if off < 1e-30:
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


def classify(c):
    bl = blocks(c)
    norms = [math.sqrt(sum(x * x for x in b)) for b in bl]
    nz = sum(1 for x in norms if x > 1e-6)
    return bl, norms, nz, ("MUB_PAIR" if nz == 1 else "NON_MUB_PAIR")


distinct = {}


def record(c, res, tag, run_id):
    P = P_of(c)
    key = tuple(round(x, 6) for x in herm_reals(P))
    bl, norms, nz, cl = classify(c)
    if key not in distinct:
        distinct[key] = {"count": 0, "block_norms": norms, "nonzero_blocks": nz, "class": cl,
                         "a": [[round(x, 12) for x in b] for b in bl], "resid": res, "flat_dev": flat_dev(P),
                         "first_seen": [tag, run_id]}
    distinct[key]["count"] += 1
    return key, cl


# controls on the 30 MUB-pair points: zero residual and first-order kernel dimension; kernel directions kept
mubpair, kernels = [], []
for k in range(3):
    for m1 in range(N):
        for m2 in range(m1 + 1, N):
            a = [-2.0] * N
            a[m1] = 3.0
            a[m2] = 3.0
            c = [0.0] * 12
            c[4 * k:4 * k + 4] = a[:4]
            P, r = resid(c)
            J = jac(P)
            JTJ = [[sum(J[t][i] * J[t][j] for t in range(25)) for j in range(12)] for i in range(12)]
            ev, evec = jacobi_eig(JTJ)
            ker = sum(1 for x in ev if x < 1e-18 * max(1.0, ev[-1]) or x < 1e-20)
            mubpair.append({"k": k + 1, "pair": [m1, m2], "resid": math.sqrt(norm2(r)), "flat_dev": flat_dev(P),
                            "JTJ_eigs_smallest4": ev[:4], "kernel_dim_real": ker})
            kernels.append((c, evec[:ker], (k + 1, m1, m2)))

# stage K: starts along first-order kernel directions at the ten k = 1 MUB-pair points (does a family leave them?)
near = []
for (c_m, kv, lab) in kernels[:10]:
    if len(kv) < 2:
        continue
    for eps in (0.05, 0.2):
        for th in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi):
            c0 = [c_m[i] + eps * (math.cos(th) * kv[0][i] + math.sin(th) * kv[1][i]) for i in range(12)]
            c, res, it, st = lm(c0)
            item = {"mub": list(lab), "eps": eps, "theta": round(th, 6), "status": st, "resid": res, "iters": it,
                    "dist_to_start_point": math.sqrt(sum((c[i] - c_m[i]) ** 2 for i in range(12)))}
            if res < 1e-12:
                key, cl = record(c, res, "K", len(near))
                item["class"] = cl
                item["returned_to_same_point"] = item["dist_to_start_point"] < 1e-6
            near.append(item)

rng = random.Random(20261019)
runs, conv = 0, 0
status_counts = {}
while time.monotonic() - T0 < BUDGET:
    scale = rng.choice([0.3, 1.0, 2.0])
    c0 = [rng.gauss(0.0, scale) for _ in range(12)]
    c, res, it, st = lm(c0)
    runs += 1
    status_counts[st] = status_counts.get(st, 0) + 1
    if res < 1e-12:
        conv += 1
        record(c, res, "R", runs)

cls = {}
for v in distinct.values():
    cls[v["class"]] = cls.get(v["class"], 0) + 1
out = {"probe": "z5_flat_rank2_projectors_v1", "kind": "float stdlib exploration; evidence only",
       "controls": {"orthonormal_max_dev": on_dev, "mub_max_dev": mub_dev,
                    "mubpair_points": len(mubpair),
                    "mubpair_max_resid": max(x["resid"] for x in mubpair),
                    "mubpair_max_flat_dev": max(x["flat_dev"] for x in mubpair),
                    "mubpair_kernel_dims": sorted(set(x["kernel_dim_real"] for x in mubpair))},
       "mubpair_details": mubpair,
       "kernel_direction_starts": near,
       "kernel_direction_summary": {"starts": len(near), "converged": sum(1 for x in near if x["resid"] < 1e-12),
                                    "returned_to_same_point": sum(1 for x in near if x.get("returned_to_same_point")),
                                    "classes": sorted(set(x.get("class", "UNCONVERGED") for x in near))},
       "runs": runs, "converged": conv, "status_counts": status_counts,
       "distinct_solutions": len(distinct), "distinct_by_class": cls,
       "nonzero_block_counts": sorted(set(v["nonzero_blocks"] for v in distinct.values())),
       "non_mub_pair_examples": [v for v in distinct.values() if v["class"] == "NON_MUB_PAIR"][:40],
       "mub_pair_multiplicities": sorted(v["count"] for v in distinct.values() if v["class"] == "MUB_PAIR"),
       "elapsed_s": round(time.monotonic() - T0, 3)}
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("runs", "converged", "status_counts", "distinct_solutions", "distinct_by_class",
                                       "nonzero_block_counts", "elapsed_s")}))
print(json.dumps(out["controls"]))
print(json.dumps(out["kernel_direction_summary"]))
