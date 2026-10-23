#!/usr/bin/env python3
"""fixedb_jacobian_v1: stdlib (pure Python, float complex) validation of the residual and analytic Jacobian of the
proposed fixed-B unitary model (lane note evidence/fixedb-unitary-model-proposal-v1.md), and local tangent count at the
exact anchors of evidence/fixedb_anchors_v1.result.json. NOT a search.

Model: Latin square B (v x v); q_ij = U_i e_j with U_0 = I; unknowns U_1..U_{v-1} unitary. For i < i' put
M = U_i^* U_i'. Residual (complex) = M[p, p] (columns) and M[p, pi(p)] (B-classes), pi(p) = the column j' with
B[i'][j'] = B[i][p]; real residual = (Re, Im). Chart: U_k <- U_k expm(A_k), A_k skew-Hermitian with ZERO diagonal
(right-phase gauge removed), real parameters x_ab, y_ab (a < b): A[a,b] = x + i y, A[b,a] = -x + i y.
Analytic Jacobian (dM = -A_i M + M A_i', A_0 = 0):
  d c / d x_(i; p, r) = -sgn(r - p) M[r, q],  d c / d y_(i; p, r) = -i M[r, q]         (r != p, block i >= 1)
  d c / d x_(i'; r, q) =  sgn(q - r) M[p, r],  d c / d y_(i'; r, q) =  i M[p, r]         (r != q)
Checks: (1) central differences along U_k (I + eps A_k) (M is bilinear, so the central difference is exact up to rounding)
against J t at random unitaries for B = cyclic v = 4, 5, 7, XOR v = 8, and at the anchors; (2) residual and full Gram
deviation (rows, columns, classes) at the anchors < 1e-12 and ray counts 49 / 64; (3) numerical rank of the real Jacobian
at the anchors by modified Gram-Schmidt with reorthogonalisation (accepted / rejected column-norm gap recorded), kernel
dimension, the v - 1 left-phase gauge vectors offdiag(U_k^* i Lambda U_k) checked to lie in the kernel, excess = kernel -
gauge rank; (4) the same at a classical v = 7 point (B cyclic, U_k = permutation matrices of a classical mate).
Standard library only; output JSON (exclusive) argv[2]; anchors JSON argv[1].
"""
import cmath, json, math, random, sys, time

T0 = time.monotonic()
ANCH, OUT = sys.argv[1], sys.argv[2]


def ct(A):
    n, m = len(A), len(A[0])
    return [[A[r][c].conjugate() for r in range(n)] for c in range(m)]


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for r in range(n):
        Ar = A[r]
        row = [0j] * m
        for t in range(k):
            a = Ar[t]
            if a != 0:
                Bt = B[t]
                for c in range(m):
                    row[c] += a * Bt[c]
        out.append(row)
    return out


def eye(v):
    return [[1 + 0j if r == c else 0j for c in range(v)] for r in range(v)]


class Problem:
    def __init__(self, B):
        v = len(B)
        self.v, self.B = v, B
        pos = [{B[i][j]: j for j in range(v)} for i in range(v)]
        self.res = []
        for i in range(v):
            for ip in range(i + 1, v):
                for p in range(v):
                    self.res.append((i, ip, p, p))
                for p in range(v):
                    self.res.append((i, ip, p, pos[ip][B[i][p]]))
        self.pl = [(a, b) for a in range(v) for b in range(a + 1, v)]
        self.pidx = {pr: k for k, pr in enumerate(self.pl)}
        self.nb = v * (v - 1)
        self.P = (v - 1) * self.nb

    def xi(self, k, a, b):
        return (k - 1) * self.nb + self.pidx[(min(a, b), max(a, b))]

    def yi(self, k, a, b):
        return self.xi(k, a, b) + self.nb // 2

    def Ms(self, U):
        v = self.v
        UH = [ct(U[i]) for i in range(v)]
        return {(i, ip): mm(UH[i], U[ip]) for i in range(v) for ip in range(i + 1, v)}

    def resid(self, U):
        Ms = self.Ms(U)
        return [Ms[(i, ip)][p][q] for (i, ip, p, q) in self.res]

    def jac(self, U):
        """complex Jacobian rows as dicts {param index: d c / d param}."""
        v = self.v
        Ms = self.Ms(U)
        rows = []
        for (i, ip, p, q) in self.res:
            M = Ms[(i, ip)]
            row = {}
            if i >= 1:
                for r in range(v):
                    if r != p:
                        sg = 1.0 if r > p else -1.0
                        row[self.xi(i, p, r)] = -sg * M[r][q]
                        row[self.yi(i, p, r)] = -1j * M[r][q]
            for r in range(v):
                if r != q:
                    sg = 1.0 if q > r else -1.0
                    row[self.xi(ip, r, q)] = sg * M[p][r]
                    row[self.yi(ip, r, q)] = 1j * M[p][r]
            rows.append(row)
        return rows

    def A_of(self, th, k):
        v = self.v
        A = [[0j] * v for _ in range(v)]
        for (a, b) in self.pl:
            x, y = th[self.xi(k, a, b)], th[self.yi(k, a, b)]
            A[a][b] = complex(x, y)
            A[b][a] = complex(-x, y)
        return A

    def gram_dev(self, U):
        v = self.v
        Q = [[[U[i][s][j] for s in range(v)] for j in range(v)] for i in range(v)]
        lines = [[(i, j) for j in range(v)] for i in range(v)] + [[(i, j) for i in range(v)] for j in range(v)]
        cls = {}
        for i in range(v):
            for j in range(v):
                cls.setdefault(self.B[i][j], []).append((i, j))
        lines += list(cls.values())
        dev = 0.0
        for L in lines:
            for a in range(v):
                for b in range(a, v):
                    x, y = Q[L[a][0]][L[a][1]], Q[L[b][0]][L[b][1]]
                    g = sum(xx.conjugate() * yy for xx, yy in zip(x, y))
                    dev = max(dev, abs(g - (1.0 if a == b else 0.0)))
        return dev, Q

    def rays(self, Q):
        v = self.v
        vecs = [Q[i][j] for i in range(v) for j in range(v)]
        reps = []
        minsep = 1.0
        for x in vecs:
            hit = False
            for r in reps:
                o = abs(sum(a.conjugate() * b for a, b in zip(r, x))) ** 2
                if 1.0 - o < 1e-7:
                    hit = True
                    break
                minsep = min(minsep, 1.0 - o)
            if not hit:
                reps.append(x)
        return len(reps), minsep


def rand_unitary(v, rng):
    cols = []
    while len(cols) < v:
        x = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(v)]
        for c in cols:
            o = sum(a.conjugate() * b for a, b in zip(c, x))
            x = [b - o * a for a, b in zip(c, x)]
        n = math.sqrt(sum(abs(t) ** 2 for t in x))
        if n > 1e-8:
            cols.append([t / n for t in x])
    return [[cols[c][r] for c in range(v)] for r in range(v)]


def fd_check(Pr, U, rng, ntests=3, eps=1e-4):
    v = Pr.v
    rows = Pr.jac(U)
    worst = 0.0
    for _ in range(ntests):
        th = [rng.gauss(0, 1) for _ in range(Pr.P)]
        Jt = [sum(c * th[k] for k, c in row.items()) for row in rows]

        def pert(s):
            Us = [U[0]] + [mm(U[k], [[(1.0 if r == c else 0.0) + s * eps * Pr.A_of(th, k)[r][c] for c in range(v)]
                                     for r in range(v)]) for k in range(1, v)]
            return Pr.resid(Us)
        rp, rm = pert(1.0), pert(-1.0)
        fd = [(a - b) / (2 * eps) for a, b in zip(rp, rm)]
        scale = max(1.0, max(abs(t) for t in Jt))
        worst = max(worst, max(abs(a - b) for a, b in zip(Jt, fd)) / scale)
    return worst


def real_columns(Pr, rows):
    R = len(rows)
    cols = [[0.0] * (2 * R) for _ in range(Pr.P)]
    for rho, row in enumerate(rows):
        for k, c in row.items():
            cols[k][rho] = c.real
            cols[k][R + rho] = c.imag
    return cols


def mgs_rank(cols, tol):
    Q = []
    acc_norms, rej_norms = [], []
    for c in cols:
        n0 = math.sqrt(sum(t * t for t in c))
        x = list(c)
        for _ in range(2):
            for q in Q:
                o = sum(a * b for a, b in zip(q, x))
                if o != 0.0:
                    x = [b - o * a for a, b in zip(q, x)]
        n = math.sqrt(sum(t * t for t in x))
        rel = n / n0 if n0 > 0 else 0.0
        if n0 > 0 and rel > tol:
            Q.append([t / n for t in x])
            acc_norms.append(rel)
        else:
            rej_norms.append(rel)
    return len(Q), acc_norms, rej_norms, Q


def gauge_vectors(Pr, U):
    """left-phase gauge: A_k = offdiag(U_k^* i Lambda U_k), Lambda = E_tt, t = 0..v-1 (returns v parameter vectors)."""
    v = Pr.v
    out = []
    for t in range(v):
        th = [0.0] * Pr.P
        for k in range(1, v):
            # (U^* i E_tt U)[a][b] = i conj(U[t][a]) U[t][b]
            for (a, b) in Pr.pl:
                z = 1j * U[k][t][a].conjugate() * U[k][t][b]
                th[Pr.xi(k, a, b)] = z.real
                th[Pr.yi(k, a, b)] = z.imag
        out.append(th)
    return out


def tangent(Pr, U, label, tol=1e-9):
    rows = Pr.jac(U)
    cols = real_columns(Pr, rows)
    rk, acc, rej, _ = mgs_rank(cols, tol)
    rk6 = sum(1 for a in acc if a > 1e-6)
    acc, rej = sorted(acc)[:6], sorted(rej)[-6:]
    gv = gauge_vectors(Pr, U)
    gres = 0.0
    for th in gv:
        Jt = [sum(c * th[k] for k, c in row.items()) for row in rows]
        gres = max(gres, max(abs(z) for z in Jt))
    grank, _, _, _ = mgs_rank([list(g) for g in gv], 1e-9)
    ker = Pr.P - rk
    return {"label": label, "v": Pr.v, "params": Pr.P, "real_residuals": 2 * len(Pr.res), "rank_tol1e-9": rk,
            "rank_tol1e-6": rk6, "smallest_accepted_rel_norms": acc, "largest_rejected_rel_norms": rej,
            "kernel_dim": ker, "gauge_rank": grank, "gauge_in_kernel_max_abs": gres, "excess": ker - grank}


def load_anchor(d, key, N, den):
    z = [cmath.exp(2j * math.pi * k / N) for k in range(N)]
    UF = d[key]["U_form"]
    v = len(UF)
    U = []
    for i in range(v):
        Ui = [[0j] * v for _ in range(v)]
        for j in range(v):
            for s in range(v):
                Ui[s][j] = sum(c * z[k] for k, c in enumerate(UF[i][j][s])) / den
        U.append(Ui)
    return U, d[key]["B"]


out = {"probe": "fixedb_jacobian_v1"}
rng = random.Random(20261019)
with open(ANCH, "r", encoding="utf-8") as fh:
    AN = json.load(fh)
U7, B7 = load_anchor(AN, "v7", 7, 7.0)
U8, B8 = load_anchor(AN, "v8", 8, 2.0)

# (1) FD checks at random unitaries
fd = {}
for name, B in (("cyc4", [[(j - i) % 4 for j in range(4)] for i in range(4)]),
                ("cyc5", [[(j - i) % 5 for j in range(5)] for i in range(5)]),
                ("cyc7", B7), ("xor8", B8)):
    Pr = Problem(B)
    U = [eye(Pr.v)] + [rand_unitary(Pr.v, rng) for _ in range(Pr.v - 1)]
    fd[name] = fd_check(Pr, U, rng)
P7, P8 = Problem(B7), Problem(B8)
fd["anchor7"] = fd_check(P7, U7, rng)
fd["anchor8"] = fd_check(P8, U8, rng)
out["fd_max_rel_err"] = fd

# (2) anchors: residual, Gram, rays
an = {}
for name, Pr, U in (("anchor7", P7, U7), ("anchor8", P8, U8)):
    r = Pr.resid(U)
    dev, Q = Pr.gram_dev(U)
    nr, ms = Pr.rays(Q)
    an[name] = {"max_abs_resid": max(abs(t) for t in r), "gram_dev": dev, "rays": nr, "minsep": ms,
                "U0_dev": max(abs(U[0][a][b] - (1 if a == b else 0)) for a in range(Pr.v) for b in range(Pr.v))}
out["anchors"] = an

# (3) tangent counts at the anchors and (4) at a classical v = 7 point: A(i, j) = (j + 3 i) mod 7 is orthogonal to
# B7(i, j) = (j - i) mod 7 because (i, j) -> (j - i, j + 3 i) has determinant -4, a unit mod 7; A(0, j) = j gives U_0 = I.
tg = []
for label, Pr, U in (("anchor7_huang_li_cyclic", P7, U7), ("anchor8_zhang_cao_xor", P8, U8)):
    if time.monotonic() - T0 > 200:
        tg.append({"label": label, "status": "SKIPPED_TIME"})
        continue
    tg.append(tangent(Pr, U, label))
Ucl = []
for i in range(7):
    Ui = [[0j] * 7 for _ in range(7)]
    for j in range(7):
        Ui[(j + 3 * i) % 7][j] = 1 + 0j
    Ucl.append(Ui)
dcl, Qcl = P7.gram_dev(Ucl)
if time.monotonic() - T0 > 200:
    tg.append({"label": "classical7_cyclic_mate_j+3i", "status": "SKIPPED_TIME"})
else:
    tg.append(dict(tangent(P7, Ucl, "classical7_cyclic_mate_j+3i"), gram_dev=dcl, rays=P7.rays(Qcl)[0]))
out["tangent"] = tg
out["gates"] = {"fd_ok": max(fd.values()) < 1e-7,
                "anchors_ok": all(a["max_abs_resid"] < 1e-12 and a["gram_dev"] < 1e-12 and a["U0_dev"] < 1e-15 for a in an.values())
                and an["anchor7"]["rays"] == 49 and an["anchor8"]["rays"] == 64,
                "gauge_in_kernel": all(t.get("gauge_in_kernel_max_abs", 1.0) < 1e-10 for t in tg),
                "rank_tolerance_stable": all("rank_tol1e-9" in t and t["rank_tol1e-9"] == t["rank_tol1e-6"] for t in tg),
                "classical_point_ok": dcl < 1e-15}
out["elapsed_s"] = round(time.monotonic() - T0, 3)
with open(OUT, "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({"fd": fd, "anchors": an, "tangent": [{k: t.get(k) for k in ("label", "params", "rank_tol1e-9", "rank_tol1e-6",
                  "kernel_dim", "gauge_rank", "excess", "gauge_in_kernel_max_abs")} for t in tg], "gates": out["gates"],
                  "elapsed_s": out["elapsed_s"]}))
