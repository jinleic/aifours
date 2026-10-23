#!/usr/bin/env python3
"""rqls_assay_v1: float feasibility assay for maximal 1-RQLS(10) (NOT a certificate; numeric results are UNKNOWN).

Representation: a Latin square B (resolution) and unit vectors q_p, p in [v]^2, with every row, column and B-class an
orthonormal basis. Problems are given by representatives z_r and line slots (r, k) meaning the vector U^k z_r with U
diagonal (eigenbasis); unsymmetric problems have one representative per cell and U = 1.
Ansatz Z_n + h (lane note evidence/w2-cyclic-quasidifference-v1.md and erratum 1): representatives v_d, w_a, w'_b,
corner c_ab; lines R0, C0, S0 and the 3h inf-lines; corner representatives confined to a prescribed eigenspace.

Stages (each with its own wall budget inside GLOBAL_BUDGET):
 A  exact-anchor checks of the float verifier (Example 2.4 from the old lane file, hash-checked; a mutation; the
    classical Parker-type pair in three encodings);
 L  local analysis at classical Parker-type points in forced-form U (eigen-multiplicities (2,2,2,1,1,1,1)):
    Jacobian kernel modulo gauge and representative phases (exact central differences of a quadratic map),
    then Gauss-Newton continuation along excess kernel directions, monitoring the number of distinct rays;
    plus one unsymmetric kernel count at a classical point;
 C  controls for the RRR solver (v = 6 negative, v = 5 classical-only, v = 7/8 calibration, symmetric positives);
 T  RRR searches: Z_7+3 forced form (random and classical-start), Z_9+1, Z_5+5, unsymmetric v = 10.
Every reported solution is re-verified on the FULL v x v configuration (all 3v lines) and its distinct rays counted
(pairs with 1 - |<q,q'>|^2 < 1e-7 merged); a maximal candidate needs maxdev < 1e-8, all v^2 rays, minsep > 1e-6.

Usage: rqls_assay_v1.py OUT.jsonl GLOBAL_BUDGET_S CLASSICAL_JSON EX24_JSON EX24_SHA256
Output: JSONL, exclusive create, hard cap 8 MiB (excess records counted, not written).
"""
import hashlib, itertools, json, math, os, sys, time
import numpy as np

T0 = time.monotonic()
SRC_SHA = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
OUT, GLOBAL_BUDGET, CLASSICAL_JSON, EX24_JSON, EX24_SHA = sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
CAP = 8 * 1024 * 1024
TOL = 1e-10
BETA = 0.5


class Capped:
    def __init__(self, path, cap):
        self.fh = open(path, "x", encoding="utf-8")
        self.n, self.cap, self.dropped = 0, cap, 0

    def write(self, obj):
        s = json.dumps(obj, separators=(",", ":")) + "\n"
        b = len(s.encode("utf-8"))
        if self.n + b > self.cap:
            self.dropped += 1
            return False
        self.fh.write(s)
        self.fh.flush()
        self.n += b
        return True


W = Capped(OUT, CAP)


def elapsed():
    return time.monotonic() - T0


def over(end):
    return time.monotonic() > end or elapsed() > GLOBAL_BUDGET


def latin(B):
    v = len(B)
    full = list(range(v))
    return all(sorted(r) == full for r in B) and all(sorted(B[i][j] for i in range(v)) == full for j in range(v))


def lines_from_B(B):
    v = len(B)
    rows = [[(i, j) for j in range(v)] for i in range(v)]
    cols = [[(i, j) for i in range(v)] for j in range(v)]
    cls = [[(i, j) for i in range(v) for j in range(v) if B[i][j] == s] for s in range(v)]
    return rows + cols + cls


class Problem:
    def __init__(self, name, v, B, lines, nrep, Upow, masks, cells):
        assert latin(B), "B not Latin"
        assert all(len(L) == v for L in lines), "line length"
        assert len(cells) == v * v
        self.name, self.v, self.B, self.nrep, self.Upow, self.masks, self.cells = name, v, B, nrep, Upow, masks, cells
        self.nL = len(lines)
        self.rep = np.array([[r for r, k in L] for L in lines])
        sh = np.array([[k for r, k in L] for L in lines])
        self.fwd = Upow[sh]
        self.back = np.conj(self.fwd)
        addr = [[] for _ in range(nrep)]
        for li, L in enumerate(lines):
            for s, (r, k) in enumerate(L):
                addr[r].append((li, s))
        groups = {}
        for r in range(nrep):
            assert addr[r], "rep without slot"
            groups.setdefault(len(addr[r]), []).append(r)
        self.groups = []
        for m, rs in sorted(groups.items()):
            self.groups.append((np.array(rs), np.array([[a[0] for a in addr[r]] for r in rs]),
                                np.array([[a[1] for a in addr[r]] for r in rs]), masks[rs]))
        self.full_lines = lines_from_B(B)
        for L in self.full_lines:
            for p in L:
                assert p in cells
        self.allowed = masks > 0.5                       # (nrep, v)
        self.npar = 2 * int(self.allowed.sum())

    # ---- RRR projections
    def PA(self, X):
        M = np.swapaxes(X, 1, 2)
        Wm, s, Vh = np.linalg.svd(M)
        return np.swapaxes(Wm @ Vh, 1, 2)

    def PB(self, X, want_z=False):
        Xb = X * self.back
        out = np.empty_like(X)
        Z = np.zeros((self.nrep, self.v), dtype=complex) if want_z else None
        for rs, aL, aS, mk in self.groups:
            Y = Xb[aL, aS]
            S = np.einsum("pka,pkb->pab", Y, Y.conj()) * mk[:, :, None] * mk[:, None, :]
            ev, V = np.linalg.eigh(S)
            z = V[:, :, -1] * mk
            z /= np.maximum(np.linalg.norm(z, axis=1, keepdims=True), 1e-300)
            for _ in range(3):
                ov = np.einsum("pka,pa->pk", Y.conj(), z)
                ph = ov / np.maximum(np.abs(ov), 1e-300)
                z = np.einsum("pka,pk->pa", Y, ph) * mk
                z /= np.maximum(np.linalg.norm(z, axis=1, keepdims=True), 1e-300)
            ov = np.einsum("pka,pa->pk", Y.conj(), z)
            ph = ov / np.maximum(np.abs(ov), 1e-300)
            out[aL, aS] = np.conj(ph)[:, :, None] * z[:, None, :]
            if want_z:
                Z[rs] = z
        out *= self.fwd
        return (out, Z) if want_z else out

    def init_random(self, rng):
        X = rng.standard_normal((self.nL, self.v, self.v)) + 1j * rng.standard_normal((self.nL, self.v, self.v))
        return X / np.linalg.norm(X, axis=2, keepdims=True)

    def init_from(self, Z0, noise, rng):
        X = self.fwd * Z0[self.rep]
        X = X + noise * (rng.standard_normal(X.shape) + 1j * rng.standard_normal(X.shape))
        return X / np.linalg.norm(X, axis=2, keepdims=True)

    # ---- verification on the full configuration
    def full_vectors(self, Z):
        return {p: self.Upow[k] * Z[r] for p, (r, k) in self.cells.items()}

    def verify(self, Z):
        Q = self.full_vectors(Z)
        maxdev = 0.0
        for L in self.full_lines:
            M = np.array([Q[p] for p in L])
            G = M.conj() @ M.T
            maxdev = max(maxdev, float(np.max(np.abs(G - np.eye(len(L))))))
        cl = sorted(Q)
        V = np.array([Q[p] for p in cl])
        V = V / np.linalg.norm(V, axis=1, keepdims=True)
        O2 = np.abs(V.conj() @ V.T) ** 2
        n = len(cl)
        sep = 1.0 - O2[np.triu_indices(n, 1)]
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        for a, b in zip(*np.nonzero(np.triu(1.0 - O2 < 1e-7, 1))):
            ra, rb = find(int(a)), find(int(b))
            if ra != rb:
                parent[ra] = rb
        return maxdev, len({find(a) for a in range(n)}), float(sep.min())

    # ---- quadratic residual map and its exact Jacobian
    def theta_of(self, Z):
        return np.concatenate([Z.real[self.allowed], Z.imag[self.allowed]])

    def Z_of(self, th):
        th = np.atleast_2d(th)
        k = th.shape[1] // 2
        Z = np.zeros((th.shape[0], self.nrep, self.v), dtype=complex)
        Z[:, self.allowed] = th[:, :k] + 1j * th[:, k:]
        return Z

    def F_batch(self, TH):
        Z = self.Z_of(TH)                                          # (b, nrep, v)
        X = self.fwd[None] * Z[:, self.rep]                         # (b, nL, v, v) rows = slot vectors
        G = np.einsum("blia,blja->blij", X.conj(), X) - np.eye(self.v)[None, None]
        iu = np.triu_indices(self.v, 1)
        d = np.arange(self.v)
        return np.concatenate([G[:, :, d, d].real.reshape(len(Z), -1), G[:, :, iu[0], iu[1]].real.reshape(len(Z), -1),
                               G[:, :, iu[0], iu[1]].imag.reshape(len(Z), -1)], axis=1)

    def F(self, th):
        return self.F_batch(th[None])[0]

    def jac(self, th, chunk=128):
        p = len(th)
        cols = []
        for s in range(0, p, chunk):
            idx = np.arange(s, min(p, s + chunk))
            E = np.zeros((len(idx), p))
            E[np.arange(len(idx)), idx] = 1.0
            Fp = self.F_batch(th[None] + E)
            Fm = self.F_batch(th[None] - E)
            cols.append(((Fp - Fm) / 2.0).T)                      # exact for a quadratic map
        return np.concatenate(cols, axis=1)

    def trivial_tangents(self, Z, lab, n):
        """gauge (commutant of U) generators acting on all reps, plus one phase per representative."""
        v = self.v
        gens = []
        lab = np.array(lab) % n if lab is not None else np.zeros(v, dtype=int)
        for m in sorted(set(lab.tolist())):
            I = np.nonzero(lab == m)[0]
            for a in range(len(I)):
                for b in range(a, len(I)):
                    p, q = I[a], I[b]
                    if p == q:
                        X = np.zeros((v, v), complex); X[p, p] = 1j; gens.append(X)
                    else:
                        X = np.zeros((v, v), complex); X[p, q] = 1; X[q, p] = -1; gens.append(X)
                        X = np.zeros((v, v), complex); X[p, q] = 1j; X[q, p] = 1j; gens.append(X)
        T = [self.theta_of(Z @ X.T) for X in gens]                 # delta z_r = X z_r
        for r in range(self.nrep):
            D = np.zeros_like(Z); D[r] = 1j * Z[r]
            T.append(self.theta_of(D))
        return np.array(T).T


def rank_tol(s, rel=1e-8):
    return int(np.sum(s > rel * max(1.0, s[0] if len(s) else 1.0)))


def excess_basis(P, th, lab, n):
    J = P.jac(th)
    U_, s, Vt = np.linalg.svd(J, full_matrices=(J.shape[0] < J.shape[1]))
    r = rank_tol(s)
    K = Vt[r:].T                                                   # kernel basis (p, k)
    T = P.trivial_tangents(P.Z_of(th)[0], lab, n)
    JT = float(np.max(np.abs(J @ T))) if T.size else 0.0
    Ut, st, _ = np.linalg.svd(T, full_matrices=False)
    rt = rank_tol(st)
    Tb = Ut[:, :rt]
    Kp = K - Tb @ (Tb.T @ K)
    Uk, sk, _ = np.linalg.svd(Kp, full_matrices=False)
    ex = int(np.sum(sk > 1e-6))
    return {"ker": K.shape[1], "rankT": rt, "excess": ex, "JT_max": JT, "smallest_nonzero_sv": float(s[r - 1]) if r > 0 else 0.0,
            "largest_zero_sv": float(s[r]) if r < len(s) else 0.0}, Uk[:, :ex], J


def newton_correct(P, th, iters=10, tol=1e-12):
    for _ in range(iters):
        f = P.F(th)
        nf = float(np.linalg.norm(f))
        if nf < tol:
            return th, nf, True
        J = P.jac(th)
        step, *_ = np.linalg.lstsq(J, f, rcond=None)
        th = th - step
    nf = float(np.linalg.norm(P.F(th)))
    return th, nf, nf < tol


# ------------------------------------------------------------------ problem builders
def unsym(name, B):
    v = len(B)
    cells = {(i, j): (i * v + j, 0) for i in range(v) for j in range(v)}
    lines = [[(i * v + j, 0) for (i, j) in L] for L in lines_from_B(B)]
    return Problem(name, v, B, lines, v * v, np.ones((1, v), dtype=complex), np.ones((v * v, v)), cells)


def sym(name, n, h, Dinf, beta, gamma, delta, Lc, lab, corner_lab):
    v = n + h
    Dfin = [d for d in range(n) if d not in Dinf]
    nrep = n + 2 * h + h * h
    Wr = lambda a: n + a
    WP = lambda b: n + h + b
    C = lambda a, b: n + 2 * h + a * h + b
    lines = [[(d, 0) for d in range(n)] + [(WP(b), 0) for b in range(h)],
             [(d, (-d) % n) for d in range(n)] + [(Wr(a), 0) for a in range(h)],
             [(d, (-beta[d]) % n) for d in Dfin] + [(Wr(a), (-gamma[a]) % n) for a in range(h)] + [(WP(b), (-delta[b]) % n) for b in range(h)]]
    for a in range(h):
        lines.append([(Wr(a), k) for k in range(n)] + [(C(a, b), 0) for b in range(h)])
    for b in range(h):
        lines.append([(WP(b), k) for k in range(n)] + [(C(a, b), 0) for a in range(h)])
    for c in range(h):
        lines.append([(Dinf[c], k) for k in range(n)] + [(C(a, b), 0) for a in range(h) for b in range(h) if Lc[a][b] == c])
    labn = np.array(lab) % n
    Upow = np.exp(2j * np.pi * np.outer(np.arange(n), labn) / n)
    masks = np.ones((nrep, v))
    for a in range(h):
        for b in range(h):
            masks[C(a, b)] = (labn == corner_lab[a][b] % n).astype(float)
    B = [[None] * v for _ in range(v)]
    cells = {}
    for i in range(n):
        for d in range(n):
            j = (i + d) % n
            B[i][j] = (n + Dinf.index(d)) if d in Dinf else (i + beta[d]) % n
            cells[(i, j)] = (d, i)
    for a in range(h):
        for j in range(n):
            B[n + a][j] = (j + gamma[a]) % n
            cells[(n + a, j)] = (Wr(a), j)
    for b in range(h):
        for i in range(n):
            B[i][n + b] = (i + delta[b]) % n
            cells[(i, n + b)] = (WP(b), i)
    for a in range(h):
        for b in range(h):
            B[n + a][n + b] = n + Lc[a][b]
            cells[(n + a, n + b)] = (C(a, b), 0)
    return Problem(name, v, B, lines, nrep, Upow, masks, cells)


def cayley_cyclic(v):
    return [[(i + j) % v for j in range(v)] for i in range(v)]


def xor8():
    return [[i ^ j for j in range(8)] for i in range(8)]


def cayley_d5():
    def mul(g, hh):
        a, e = g % 5, g // 5
        b, f = hh % 5, hh // 5
        return ((a + (b if e == 0 else -b)) % 5) + 5 * ((e + f) % 2)
    return [[mul(g, hh) for hh in range(10)] for g in range(10)]


def valid_betas(n, Dfin, rng, k):
    out, tries = [], 0
    while len(out) < k and tries < 200000:
        tries += 1
        vals = rng.permutation(n)[:len(Dfin)]
        if len({(int(x) - d) % n for x, d in zip(vals, Dfin)}) == len(Dfin):
            out.append({d: int(x) for d, x in zip(Dfin, vals)})
    return out


def latin3_all():
    out = []
    for p in itertools.permutations(range(3)):
        for q in itertools.permutations(range(3)):
            L = [[None] * 3 for _ in range(3)]
            for a in range(3):
                for b in range(3):
                    L[p[a]][q[b]] = (a + b) % 3
            if L not in out:
                out.append(L)
    return out


def mate_labels(L, D2):
    cells = [(a, b) for a in range(3) for b in range(3)]
    cls, seen = [], set()
    for p in cells:
        if p in seen:
            continue
        g = [p] + [q for q in cells if q != p and q[0] != p[0] and q[1] != p[1] and L[q[0]][q[1]] != L[p[0]][p[1]]]
        seen.update(g)
        cls.append(g)
    assert len(cls) == 3 and all(len(g) == 3 for g in cls)
    out = []
    for perm in itertools.permutations(D2):
        M = [[None] * 3 for _ in range(3)]
        for g, m in zip(cls, perm):
            for (a, b) in g:
                M[a][b] = m
        out.append(M)
    return out


# ------------------------------------------------------------------ classical Parker-type encodings
OMEGA7 = np.exp(2j * np.pi / 7)


def enc7(sym_, ):
    z = np.zeros(10, dtype=complex)
    if sym_ < 7:
        z[:7] = OMEGA7 ** (np.arange(7) * sym_) / math.sqrt(7)
    else:
        z[sym_] = 1.0
    return z


def parker_problem(hit, resolution, mlab, name):
    """resolution 'B' (QLS = A) or 'A' (QLS = B). mlab = eigen labels of the three inf basis vectors (None: classical I_3)."""
    R = hit[resolution]
    Q = hit["A_array"] if resolution == "B" else hit["B_array"]
    Lc = [[x - 7 for x in row] for row in R["corner"]]
    beta = {int(k): v for k, v in R["beta"].items()}
    if mlab is None:
        lab = list(range(7)) + [0, 0, 0]
        M = [[0] * 3 for _ in range(3)]
    else:
        lab = list(range(7)) + list(mlab)
        M = [[mlab[Q[7 + a][7 + b] - 7] for b in range(3)] for a in range(3)]
    P = sym(name, 7, 3, R["Dinf"], beta, R["gamma"], R["delta"], Lc, lab, M)
    Z = np.zeros((P.nrep, 10), dtype=complex)
    for d in range(7):
        Z[d] = enc7(Q[0][d])
    for a in range(3):
        Z[7 + a] = enc7(Q[7 + a][0])
        Z[10 + a] = enc7(Q[0][7 + a])
    for a in range(3):
        for b in range(3):
            Z[13 + 3 * a + b] = enc7(Q[7 + a][7 + b])
    return P, Z, lab, M


# ------------------------------------------------------------------ RRR runner
def rrr(P, X, max_iter, end):
    err, status, it = float("inf"), "MAX_ITER", 0
    for it in range(1, max_iter + 1):
        pb = P.PB(X)
        pa = P.PA(2.0 * pb - X)
        d = pa - pb
        err = float(np.sqrt(np.mean(np.sum(np.abs(d) ** 2, axis=2))))
        X = X + BETA * d
        if not np.isfinite(err):
            status = "NONFINITE"
            break
        if err < TOL:
            status = "CONVERGED"
            break
        if (it & 127) == 0 and over(end):
            status = "TIME"
            break
    pb, Z = P.PB(X, want_z=True)
    return status, it, err, Z


def run(P, tag, seeds, max_iter, end, extra=None, start=None, noise=0.0):
    out = []
    for seed in seeds:
        if over(end):
            W.write({"tag": tag, "problem": P.name, "seed": seed, "status": "SKIPPED_TIME"})
            out.append("SKIPPED")
            continue
        t0 = time.monotonic()
        rng = np.random.default_rng(seed)
        X = P.init_random(rng) if start is None else P.init_from(start, noise, rng)
        status, it, err, Z = rrr(P, X, max_iter, end)
        maxdev, rays, minsep = P.verify(Z)
        maximal = bool(maxdev < 1e-8 and rays == P.v * P.v and minsep > 1e-6)
        rec = {"tag": tag, "problem": P.name, "seed": seed, "status": status, "iters": it, "err": err, "maxdev": maxdev,
               "rays": rays, "minsep": minsep, "secs": round(time.monotonic() - t0, 3), "maximal_candidate": maximal}
        if extra is not None:
            rec["config"] = extra
        if maximal:
            rec["Z_re"] = np.round(Z.real, 15).tolist()
            rec["Z_im"] = np.round(Z.imag, 15).tolist()
            rec["B"] = P.B
        W.write(rec)
        out.append(rec)
    return out


def summary(tag, recs):
    st, rays, maxc = {}, {}, 0
    for r in recs:
        if r == "SKIPPED":
            st["SKIPPED"] = st.get("SKIPPED", 0) + 1
            continue
        st[r["status"]] = st.get(r["status"], 0) + 1
        if r["maxdev"] < 1e-8:
            rays[str(r["rays"])] = rays.get(str(r["rays"]), 0) + 1
        maxc += int(r["maximal_candidate"])
    W.write({"summary": tag, "status_counts": st, "verified_ray_counts": rays, "maximal_candidates": maxc, "elapsed_s": round(elapsed(), 2)})


# ------------------------------------------------------------------ stages
def stage_A(classical, end):
    raw = open(EX24_JSON, "rb").read()
    h = hashlib.sha256(raw).hexdigest()
    ok_hash = (h == EX24_SHA)
    ex = json.loads(raw)
    N = int(ex["N"])
    zeta = np.exp(2j * np.pi / N)
    v = int(ex["v"])
    Z = np.zeros((v * v, v), dtype=complex)
    for i in range(v):
        for j in range(v):
            c = ex["cells"][i][j]
            Z[i * v + j] = np.array([sum(cf * zeta ** e for e, cf in coord) for coord in c["x"]]) / math.sqrt(c["n"])
    P = unsym("ex24", ex["B"])
    md, ry, ms = P.verify(Z)
    W.write({"tag": "A1_ex24_exact_anchor", "ex24_sha256": h, "hash_ok": ok_hash, "maxdev": md, "rays": ry, "minsep": ms,
             "expect": "maxdev<1e-12, rays=64", "pass": bool(ok_hash and md < 1e-12 and ry == 64 and ms > 1e-6)})
    Zm = Z.copy()
    Zm[1 * v + 0] = Zm[1 * v + 0] * np.exp(1j * np.pi / 4 * np.array([0, 0, 0, 1, 0, 0, 0, 0]))
    md2, ry2, ms2 = P.verify(Zm)
    W.write({"tag": "A2_ex24_phase_mutation", "maxdev": md2, "rays": ry2, "expect": "maxdev>0.1", "pass": bool(md2 > 0.1)})
    hit = classical["pairs"][0]
    for res in ("B", "A"):
        for mlab, nm in ((None, "classicalU"), ((0, 1, 3), "forcedU_013")):
            P, Z, lab, M = parker_problem(hit, res, mlab, "parker_%s_%s" % (res, nm))
            md, ry, ms = P.verify(Z)
            W.write({"tag": "A3_parker_exact_anchor", "resolution": res, "U": nm, "maxdev": md, "rays": ry,
                     "expect": "maxdev<1e-12, rays=10", "pass": bool(md < 1e-12 and ry == 10),
                     "F_norm_at_point": float(np.linalg.norm(P.F(P.theta_of(Z))))})
    Bfull = hit["B_array"]
    Pu = unsym("parker_unsym", Bfull)
    Zu = np.array([enc7(hit["A_array"][i][j]) for i in range(10) for j in range(10)])
    md, ry, ms = Pu.verify(Zu)
    W.write({"tag": "A4_parker_unsym_anchor", "maxdev": md, "rays": ry, "pass": bool(md < 1e-12 and ry == 10)})


def stage_L(classical, end, rng):
    hits = classical["pairs"]
    labsets = [(0, a, b) for a in range(1, 7) for b in range(1, 7) if a != b]
    jobs = [(hi, res, mlab) for hi in range(len(hits)) for res in ("B", "A") for mlab in labsets]
    order = rng.permutation(len(jobs))
    best = 0
    for oi in order:
        hi, res, mlab = jobs[int(oi)]
        hit = hits[hi]
        if True:
            if True:
                if over(end):
                    W.write({"tag": "L_local", "status": "SKIPPED_TIME", "remaining": int(len(order))})
                    break
                P, Z, lab, M = parker_problem(hit, res, mlab, "parker_local")
                th0 = P.theta_of(Z)
                info, Kx, J = excess_basis(P, th0, lab, 7)
                rec = {"tag": "L_local", "hit": hi, "resolution": res, "mlab": list(mlab), "F0": float(np.linalg.norm(P.F(th0)))}
                rec.update(info)
                paths = []
                if info["excess"] > 0:
                    for trial in range(2):
                        if over(end):
                            break
                        t = Kx @ rng.standard_normal(Kx.shape[1])
                        t /= np.linalg.norm(t)
                        th = th0.copy()
                        s = 0.04
                        steps, maxrays, last = 0, 10, None
                        while steps < 12 and s >= 0.0025 and not over(end):
                            cand, nf, ok = newton_correct(P, th + s * t)
                            if not ok:
                                s /= 2
                                continue
                            moved = float(np.linalg.norm(cand - th))
                            th = cand
                            steps += 1
                            Zc = P.Z_of(th)[0]
                            nrm = np.linalg.norm(Zc, axis=1)
                            md, ry, ms = P.verify(Zc / nrm[:, None])
                            maxrays = max(maxrays, ry)
                            last = {"step": steps, "s": s, "moved": moved, "resid": nf, "maxdev": md, "rays": ry, "minsep": ms,
                                    "norm_dev": float(np.max(np.abs(nrm - 1)))}
                            if ry == 100 and md < 1e-8 and ms > 1e-6:
                                W.write({"tag": "L_MAXIMAL_CANDIDATE", "hit": hi, "resolution": res, "mlab": list(mlab),
                                         "Z_re": np.round(Zc.real, 15).tolist(), "Z_im": np.round(Zc.imag, 15).tolist(), "B": P.B,
                                         "lab": lab, "M": M})
                                break
                            info2, Kx2, _ = excess_basis(P, th, lab, 7)
                            if info2["excess"] == 0:
                                last["excess_after"] = 0
                                break
                            tn = Kx2 @ (Kx2.T @ t)
                            if np.linalg.norm(tn) < 1e-3:
                                tn = Kx2[:, 0]
                            t = tn / np.linalg.norm(tn)
                        paths.append({"trial": trial, "steps": steps, "max_rays": maxrays, "last": last, "final_s": s})
                rec["paths"] = paths
                W.write(rec)
                best = max([best] + [p["max_rays"] for p in paths])
    # one unsymmetric kernel count at the first classical point
    if not over(end):
        hit = hits[0]
        Pu = unsym("parker_unsym", hit["B_array"])
        Zu = np.array([enc7(hit["A_array"][i][j]) for i in range(10) for j in range(10)])
        thu = Pu.theta_of(Zu)
        info, _, _ = excess_basis(Pu, thu, None, 1)
        W.write({"tag": "L_unsym_kernel", **info})
    W.write({"summary": "L_local", "best_rays_on_paths": best, "elapsed_s": round(elapsed(), 2)})


def main():
    W.write({"assay": "rqls_assay_v1", "src_sha256": SRC_SHA, "numpy": np.__version__, "python": sys.version, "budget_s": GLOBAL_BUDGET,
             "tol": TOL, "beta": BETA, "argv": sys.argv[1:],
             "env": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS", "TMPDIR", "PYTHONDONTWRITEBYTECODE")}})
    classical = json.load(open(CLASSICAL_JSON))
    plan = [("A", 30), ("L", 420), ("C1", 50), ("C2", 30), ("C3", 70), ("C4", 90), ("C5", 40), ("C6", 40), ("C7", 50),
            ("T1", 300), ("T1c", 120), ("T2", 150), ("T3", 100), ("T4", 160)]
    ends, acc, t0 = {}, 0, time.monotonic()
    for tag, b in plan:
        acc += b
        ends[tag] = t0 + acc
    rng = np.random.default_rng(20261019)
    stage_A(classical, ends["A"])
    stage_L(classical, ends["L"], rng)
    summary("C1_neg_v6", run(unsym("v6_cayley", cayley_cyclic(6)), "C1_neg_v6", [11, 12, 13, 14], 15000, ends["C1"]))
    summary("C2_v5_classical_only", run(unsym("v5_cayley", cayley_cyclic(5)), "C2_v5_classical_only", [21, 22, 23, 24, 25, 26], 15000, ends["C2"]))
    summary("C3_cal_v7_cayley", run(unsym("v7_cayley", cayley_cyclic(7)), "C3_cal_v7_cayley", [31, 32, 33, 34, 35, 36], 20000, ends["C3"]))
    summary("C4_cal_v8_xor", run(unsym("v8_xor", xor8()), "C4_cal_v8_xor", [41, 42, 43, 44, 45, 46], 20000, ends["C4"]))
    summary("C5_cal_sym_7p0", run(sym("sym_7p0", 7, 0, [], {d: (4 * d) % 7 for d in range(7)}, [], [], [], list(range(7)), []),
                                  "C5_cal_sym_7p0", list(range(51, 61)), 20000, ends["C5"]))
    F8beta = {1: 3, 2: 6, 3: 1, 4: 5, 5: 4, 6: 2}
    summary("C6_pos_sym_7p1_F8", run(sym("sym_7p1_F8", 7, 1, [0], F8beta, [0], [0], [[0]], list(range(7)) + [0], [[0]]),
                                     "C6_pos_sym_7p1_F8", list(range(61, 71)), 20000, ends["C6"]))
    hit0 = classical["pairs"][0]
    Pc, Zc, labc, Mc = parker_problem(hit0, "B", None, "sym_7p3_parker_classicalU")
    summary("C7_pos_sym_7p3_classical", run(Pc, "C7_pos_sym_7p3_classical", list(range(71, 81)), 20000, ends["C7"]))
    # T1 random forced form
    L3 = latin3_all()
    rcfg = np.random.default_rng(777)
    recs, cfg = [], 0
    while not over(ends["T1"]):
        Dinf = sorted(int(x) for x in rcfg.choice(7, 3, replace=False))
        Dfin = [d for d in range(7) if d not in Dinf]
        bl = valid_betas(7, Dfin, rcfg, 1)
        if not bl:
            continue
        beta = bl[0]
        gam = sorted(set(range(7)) - {(beta[d] - d) % 7 for d in Dfin})
        dlt = sorted(set(range(7)) - set(beta.values()))
        Lc = L3[int(rcfg.integers(len(L3)))]
        D2 = [0] + sorted(int(x) for x in rcfg.choice(np.arange(1, 7), 2, replace=False))
        Ms = mate_labels(Lc, D2)
        M = Ms[int(rcfg.integers(len(Ms)))]
        conf = {"Dinf": Dinf, "beta": {str(k): v for k, v in beta.items()}, "gamma": gam, "delta": dlt, "L": Lc, "D2": D2, "M": M, "cfg": cfg}
        try:
            P = sym("sym_7p3_forced", 7, 3, Dinf, beta, gam, dlt, Lc, list(range(7)) + D2, M)
        except AssertionError as ex:
            W.write({"tag": "T1_sym_7p3_forced", "config": conf, "status": "BAD_CONFIG", "why": repr(ex)})
            cfg += 1
            continue
        recs += run(P, "T1_sym_7p3_forced", [1000 + 2 * cfg, 1001 + 2 * cfg], 6000, ends["T1"], extra=conf)
        cfg += 1
    summary("T1_sym_7p3_forced", recs)
    # T1c classical-start RRR in forced form (all hits, both resolutions, random label sets, noise 0.15)
    recs, k = [], 0
    while not over(ends["T1c"]):
        hi = k % len(classical["pairs"])
        res = "B" if (k // len(classical["pairs"])) % 2 == 0 else "A"
        a, b = [int(x) for x in rcfg.choice(np.arange(1, 7), 2, replace=False)]
        P, Z0, lab, M = parker_problem(classical["pairs"][hi], res, (0, a, b), "parker_forced_start")
        recs += run(P, "T1c_classical_start", [5000 + k], 6000, ends["T1c"], extra={"hit": hi, "resolution": res, "mlab": [0, a, b]},
                    start=Z0, noise=0.15)
        k += 1
    summary("T1c_classical_start", recs)
    # T2 Z_9 + 1
    recs, cfg = [], 0
    while not over(ends["T2"]):
        Dfin = list(range(1, 9))
        bl = valid_betas(9, Dfin, rcfg, 1)
        if not bl:
            continue
        beta = bl[0]
        gam = sorted(set(range(9)) - {(beta[d] - d) % 9 for d in Dfin})
        dlt = sorted(set(range(9)) - set(beta.values()))
        mstar = int(rcfg.integers(9))
        conf = {"Dinf": [0], "beta": {str(k): v for k, v in beta.items()}, "gamma": gam, "delta": dlt, "mstar": mstar, "cfg": cfg}
        try:
            P = sym("sym_9p1", 9, 1, [0], beta, gam, dlt, [[0]], list(range(9)) + [mstar], [[mstar]])
        except AssertionError as ex:
            W.write({"tag": "T2_sym_9p1", "config": conf, "status": "BAD_CONFIG", "why": repr(ex)})
            cfg += 1
            continue
        recs += run(P, "T2_sym_9p1", [2000 + 2 * cfg, 2001 + 2 * cfg], 6000, ends["T2"], extra=conf)
        cfg += 1
    summary("T2_sym_9p1", recs)
    # T3 Z_5 + 5
    recs, cfg = [], 0
    while not over(ends["T3"]):
        Dinf = [int(x) for x in rcfg.permutation(5)]
        gam = [int(x) for x in rcfg.permutation(5)]
        dlt = [int(x) for x in rcfg.permutation(5)]
        s_, t_ = [int(x) for x in rcfg.integers(1, 5, 2)]
        while True:
            s2, t2 = [int(x) for x in rcfg.integers(1, 5, 2)]
            if (s_ * t2 - t_ * s2) % 5 != 0:
                break
        Lc = [[(s_ * a + t_ * b) % 5 for b in range(5)] for a in range(5)]
        M = [[(s2 * a + t2 * b) % 5 for b in range(5)] for a in range(5)]
        conf = {"Dinf": Dinf, "gamma": gam, "delta": dlt, "L": Lc, "M": M, "cfg": cfg}
        try:
            P = sym("sym_5p5", 5, 5, Dinf, {}, gam, dlt, Lc, list(range(5)) + list(range(5)), M)
        except AssertionError as ex:
            W.write({"tag": "T3_sym_5p5", "config": conf, "status": "BAD_CONFIG", "why": repr(ex)})
            cfg += 1
            continue
        recs += run(P, "T3_sym_5p5", [3000 + 2 * cfg, 3001 + 2 * cfg], 6000, ends["T3"], extra=conf)
        cfg += 1
    summary("T3_sym_5p5", recs)
    # T4 unsymmetric v = 10
    recs = []
    for nm, B in (("v10_parkerB", hit0["B_array"]), ("v10_cayD5", cayley_d5()), ("v10_cayZ10", cayley_cyclic(10))):
        recs += run(unsym(nm, B), "T4_unsym_v10", [4001, 4002], 20000, ends["T4"], extra={"B": nm})
    summary("T4_unsym_v10", recs)
    W.write({"end": True, "elapsed_s": round(elapsed(), 2), "dropped_records": W.dropped, "bytes": W.n})


if __name__ == "__main__":
    code = 0
    try:
        main()
    except Exception as ex:
        import traceback
        W.write({"exception": repr(ex), "traceback": traceback.format_exc()[-4000:], "elapsed_s": round(elapsed(), 2)})
        code = 2
    W.fh.close()
    sys.exit(code)
