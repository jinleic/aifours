#!/usr/bin/env python3
"""rqls_fixedb_lm_v2: float Levenberg-Marquardt assay of the FIXED-B UNITARY MODEL (no orbit symmetry) for 1-RQLS(v)
(design note evidence/fixedb-unitary-model-proposal-v1.md). NOT a certificate; any target miss is a scoped UNKNOWN.

Model: B is a fixed Latin square (the resolution). Cell (i, j) carries q_ij = U_i e_j with U_0 = I (rows built in);
unknowns U_1..U_{v-1} unitary. For i < i' let M = U_i^* U_i'. Residual (complex, 2v per pair) = M[p, p] (columns) and
M[p, pi(p)] (B-classes), pi(p) = the column j' with B[i'][j'] = B[i][p]; real residual = (Re, Im); 2 v^2 (v - 1) reals.
Chart: U_k <- U_k expm(A_k), A_k skew-Hermitian with ZERO diagonal (right phases removed); real parameters x_ab, y_ab
(a < b): A[a,b] = x + i y, A[b,a] = -x + i y; v (v - 1)^2 parameters. Analytic Jacobian (validated in pure Python by
code/fixedb_jacobian_v1.py, receipt evidence/fixedb_jacobian_v1.receipt.md): dM = -A_i M + M A_i', A_0 = 0. Normal
equations assembled pair-block-wise. LM damping schedule as rqls_wh10_lm_v2 (lam0 1e-3, x10 on failure up to 12 tries,
/3 on success, floor 1e-12); CONVERGED when |r|^2 < 1e-26; STALL; MAX_ITER after ITERS; polar re-unitarisation every 25
iterations.
EVERY endpoint is verified on the FULL configuration: Gram deviation of all v rows, v columns and v B-classes (3v
lines, per family recorded); "verified" = max deviation < 1e-8. For deviation < 1e-6 distinct rays are counted (pairs
with 1 - |<q,q'>|^2 < 1e-7 merged; minsep recorded). Maximal candidate = v = 10 (ANY stage), verified, 100 rays, minsep >
1e-6: U written at full precision, then IMMEDIATE stop (exit 7). Model defect = LM residual < 1e-10 with deviation >=
1e-8 (any stage): U written, IMMEDIATE stop (exit 8). U is also written for the first 32 verified v = 10 TARGET
endpoints (stages W, WD, WS; v2 change: v1 also spent these slots on the Parker calibration stages) and the first 8
verified S8 endpoints.

Stages (deterministic seeds; wall-clock stage ends inside BUDGET; actual counts recorded; unfinished runs SKIPPED_TIME):
 S   self-tests (gate): input pins (sha256) of the exact anchors and the Parker pair; analytic Jacobian vs central
     differences (exact for the bilinear M) at Haar-random U for cyclic v = 4, 5, 7, 10, XOR v = 8, Cay(D_5): relative
     error < 1e-9; block normal equations vs dense J^T J, J^T r at v = 5 and 7 (< 1e-12 relative); retraction
     unitarity < 1e-12; float anchors: Huang-Li v = 7 (cyclic B) and Zhang-Cao Example 3.3 v = 8 (XOR B): residual <
     1e-12, deviation < 1e-12, rays 49 / 64, U_0 = I; classical Parker v = 10 point (B_array, mate A_array relabelled so
     that A(0, j) = j): residual 0, deviation 0, rays 10; mutation U_1 <- U_1 expm(A(0.3 g)): residual >= 0.01.
 N   negative controls (gate: >= 1 run, 0 verified, 0 defects): v = 4, B = Cay(Z_4) and v = 6, B = Cay(Z_6). Imports
     (Zhang-Cao arXiv:2608.29201v2 Sec. 3, citing Ball-Simoens): every 1-RQLS(4) is classical, no 1-RQLS(6) exists;
     Cay(Z_4) has no transversal.
 C   classical-only control (gate: >= 1 run, 0 defects, every verified endpoint has exactly 5 rays): v = 5, Cay(Z_5).
     Import: every 1-RQLS(5) is classical (same source).
 KP  near-anchor recovery: U_anchor expm(A(amp g)), g ~ N(0,1)^P, amp in {1e-3, 1e-2, 0.1, 0.3}, 4 seeds, at the v = 7
     and v = 8 anchors and the classical v = 10 Parker point. Gate: every amp <= 1e-2 run verified, with 49 rays (v = 7)
     and 64 rays (v = 8); v = 10 amp <= 1e-2 runs verified (rays recorded: the point has trade directions); 0 defects.
 KR  random-start recovery of KNOWN classes (gate: >= 1 run each, 0 defects; counts and ray histograms recorded, NOT
     detection power for v = 10 targets): v = 7 cyclic B, v = 8 XOR B (NKR each), v = 10 Parker B (NKR10).
 S8  sensitivity probe (recorded, no gate): v = 8, B = Cay(Z_8) (no classical solution, Hall-Paige), N8 random starts.
 W   TARGET v = 10, B = Cay(Z_10), B(i,j) = (j - i) mod 10: NW random starts.
 WD  TARGET v = 10, B = Cay(D_5), B(i,j) = index(g_i^-1 g_j), g = r^a s^b <-> a + 5b: NWD random starts.
 WS  TARGET seeded: up to NS starts at verified (non-maximal) W/WD endpoints, U expm(A(0.05 g)).
MODE "full" runs every stage with fixed calibration slots (S 60 s, N 120, C 60, KP 300, KR 900, S8 420) and splits the
remainder R = BUDGET - 1980 as W 0.6 R, WD 0.3 R, WS 0.1 R (120 s reserve). MODE "target" runs S and KP (the gated
self-tests and near-anchor recovery) and then W / WD / WS on R = BUDGET - 480 (same split). R <= 0 is a gate failure.
Usage: rqls_fixedb_lm_v2.py OUT.jsonl BUDGET_S MODE NN NC NKR NKR10 N8 NW NWD NS STOP_RECEIPT
Protocol (owned_supervisor_v2): no computation before the line "GO" on stdin (otherwise exit 6, no output); SIGTERM sets
a flag honoured between runs. Exit codes: 0 done, 2 exception, 3 gate failure, 4 output cap, 5 SIGTERM, 6 no GO,
7 maximal candidate (unverified; immediate), 8 model defect (immediate). On every non-zero exit after GO a separate
exclusive STOP_RECEIPT is written.
"""
import hashlib, json, math, signal, sys, time
import numpy as np

TERM = [False]
signal.signal(signal.SIGTERM, lambda s, f: TERM.__setitem__(0, True))
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic()
OUT, BUDGET, MODE = sys.argv[1], float(sys.argv[2]), sys.argv[3]
NN, NC, NKR, NKR10, N8, NW, NWD, NS = (int(a) for a in sys.argv[4:12])
STOP_RECEIPT = sys.argv[12]
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ANCHORS = (LANE + "/evidence/fixedb_anchors_v1.result.json",
           "13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92")
PARKER = (LANE + "/evidence/parker_z7p3_classical_v1.result.json",
          "00e991d692e669411a49d45aa1623c52189346dc32acb6fb1feea1858b841c30")
CAP = 8 * 1024 * 1024
ITERS = 300
fh = open(OUT, "x", encoding="utf-8")
NB = [0, 0]
STAGE = ["init"]
SAVED = {"v10": 0, "S8": 0}


class CapStop(Exception):
    pass


class GateFail(Exception):
    pass


class CandidateStop(Exception):
    pass


class ModelDefectStop(Exception):
    pass


def W(o):
    s = json.dumps(o, separators=(",", ":")) + "\n"
    b = len(s.encode("utf-8"))
    if NB[0] + b > CAP:
        raise CapStop("jsonl cap %d bytes reached" % CAP)
    fh.write(s)
    fh.flush()
    NB[0] += b
    NB[1] += 1


def elapsed():
    return time.monotonic() - T0


def over(end):
    return TERM[0] or time.monotonic() > end or elapsed() > BUDGET


def gate(tag, ok, detail):
    W({"GATE": tag, "pass": bool(ok), "detail": detail, "elapsed_s": round(elapsed(), 2)})
    if not ok:
        raise GateFail(tag)


def is_latin(B):
    v = B.shape[0]
    return all(sorted(B[i].tolist()) == list(range(v)) for i in range(v)) and \
        all(sorted(B[:, j].tolist()) == list(range(v)) for j in range(v))


class Problem:
    def __init__(self, B, name):
        B = np.asarray(B, dtype=np.int64)
        v = B.shape[0]
        if B.shape != (v, v) or not is_latin(B):
            raise GateFail("B not Latin: " + name)
        self.v, self.name, self.B = v, name, B
        pos = np.empty((v, v), dtype=np.int64)
        for i in range(v):
            pos[i, B[i]] = np.arange(v)
        self.pos = pos
        self.pairs = [(i, ip) for i in range(v) for ip in range(i + 1, v)]
        n = len(self.pairs)
        self.npairs = n
        self.I = np.array([p[0] for p in self.pairs], dtype=np.int64)
        self.IP = np.array([p[1] for p in self.pairs], dtype=np.int64)
        pi = np.stack([pos[ip, B[i]] for (i, ip) in self.pairs])
        R2 = 2 * v
        self.Prow = np.concatenate([np.arange(v), np.arange(v)])
        self.Qrow = np.concatenate([np.tile(np.arange(v), (n, 1)), pi], axis=1)
        pl = [(a, b) for a in range(v) for b in range(a + 1, v)]
        self.half = len(pl)
        self.nb = 2 * self.half
        self.P = (v - 1) * self.nb
        self.ia = np.array([a for a, b in pl], dtype=np.int64)
        self.ib = np.array([b for a, b in pl], dtype=np.int64)
        pidx = -np.ones((v, v), dtype=np.int64)
        for k, (a, b) in enumerate(pl):
            pidx[a, b] = k
            pidx[b, a] = k
        r = np.arange(v)
        coli = np.broadcast_to(pidx[self.Prow[:, None], r[None, :]], (n, R2, v))
        sgi = np.broadcast_to(-np.sign(r[None, :] - self.Prow[:, None]).astype(float), (n, R2, v))
        self.mi = (coli >= 0) & (self.I >= 1)[:, None, None]
        colp = pidx[r[None, None, :], self.Qrow[:, :, None]]
        sgp = np.sign(self.Qrow[:, :, None] - r[None, None, :]).astype(float)
        self.mp = colp >= 0
        base = np.broadcast_to((np.arange(n)[:, None, None] * R2 + np.arange(R2)[None, :, None]) * (2 * self.nb),
                               (n, R2, v))
        self.fxi = (base + coli)[self.mi]
        self.fyi = (base + self.half + coli)[self.mi]
        self.fxp = (base + self.nb + colp)[self.mp]
        self.fyp = (base + self.nb + self.half + colp)[self.mp]
        self.sgi = sgi[self.mi]
        self.sgp = sgp[self.mp]
        self.gn = np.broadcast_to(np.arange(n)[:, None, None], (n, R2, v))
        self.gr = np.broadcast_to(r[None, None, :], (n, R2, v))
        self.gq = np.broadcast_to(self.Qrow[:, :, None], (n, R2, v))
        self.gp = np.broadcast_to(self.Prow[None, :, None], (n, R2, v))
        self.rn = np.broadcast_to(np.arange(n)[:, None], (n, R2))
        self.rp = np.broadcast_to(self.Prow[None, :], (n, R2))
        self.eye = np.eye(self.P)

    def Ms(self, U):
        return np.conj(U[self.I]).transpose(0, 2, 1) @ U[self.IP]

    def resid(self, U):
        return self.Ms(U)[self.rn, self.rp, self.Qrow]

    def normal(self, U):
        M = self.Ms(U)
        res = M[self.rn, self.rp, self.Qrow]
        Mcol = M[self.gn, self.gr, self.gq]
        Mrow = M[self.gn, self.gp, self.gr]
        J = np.zeros(self.npairs * 2 * self.v * 2 * self.nb, dtype=complex)
        J[self.fxi] = self.sgi * Mcol[self.mi]
        J[self.fyi] = -1j * Mcol[self.mi]
        J[self.fxp] = self.sgp * Mrow[self.mp]
        J[self.fyp] = 1j * Mrow[self.mp]
        J = J.reshape(self.npairs, 2 * self.v, 2 * self.nb)
        Jr = np.concatenate([J.real, J.imag], axis=1)
        rr = np.concatenate([res.real, res.imag], axis=1)
        G = np.matmul(Jr.transpose(0, 2, 1), Jr)
        g = np.einsum("nra,nr->na", Jr, rr)
        nb = self.nb
        JTJ = np.zeros((self.P, self.P))
        JTr = np.zeros(self.P)
        for k, (i, ip) in enumerate(self.pairs):
            b = slice((ip - 1) * nb, ip * nb)
            JTJ[b, b] += G[k, nb:, nb:]
            JTr[b] += g[k, nb:]
            if i >= 1:
                a = slice((i - 1) * nb, i * nb)
                JTJ[a, a] += G[k, :nb, :nb]
                JTJ[a, b] += G[k, :nb, nb:]
                JTJ[b, a] += G[k, nb:, :nb]
                JTr[a] += g[k, :nb]
        return JTJ, JTr, res, Jr

    def A_of(self, th):
        T = th.reshape(self.v - 1, self.nb)
        x, y = T[:, :self.half], T[:, self.half:]
        A = np.zeros((self.v - 1, self.v, self.v), dtype=complex)
        A[:, self.ia, self.ib] = x + 1j * y
        A[:, self.ib, self.ia] = -x + 1j * y
        return A

    def retract(self, U, th):
        w, V = np.linalg.eigh(-1j * self.A_of(th))
        E = (V * np.exp(1j * w)[:, None, :]) @ np.conj(V).transpose(0, 2, 1)
        U2 = U.copy()
        U2[1:] = U[1:] @ E
        return U2


def rand_U(v, rng):
    Z = (rng.standard_normal((v - 1, v, v)) + 1j * rng.standard_normal((v - 1, v, v))) / math.sqrt(2.0)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=1, axis2=2)
    U = np.empty((v, v, v), dtype=complex)
    U[0] = np.eye(v)
    U[1:] = Q * (d / np.abs(d))[:, None, :]
    return U


def polar(U):
    Wm, _, Vh = np.linalg.svd(U[1:])
    U2 = U.copy()
    U2[1:] = Wm @ Vh
    return U2


def lm(Pr, U, iters=ITERS, tol=1e-26):
    lam = 1e-3
    r = Pr.resid(U)
    nf = float(np.sum(np.abs(r) ** 2))
    status, it = "MAX_ITER", 0
    for it in range(1, iters + 1):
        if nf < tol:
            status = "CONVERGED"
            break
        JTJ, JTr, _, _ = Pr.normal(U)
        improved = False
        for _ in range(12):
            try:
                step = np.linalg.solve(JTJ + lam * Pr.eye, -JTr)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            if not np.all(np.isfinite(step)):
                lam *= 10
                continue
            U2 = Pr.retract(U, step)
            r2 = Pr.resid(U2)
            n2 = float(np.sum(np.abs(r2) ** 2))
            if n2 < nf:
                U, r, nf = U2, r2, n2
                lam = max(lam / 3, 1e-12)
                improved = True
                break
            lam *= 10
        if not improved:
            status = "STALL"
            break
        if it % 25 == 0:
            U = polar(U)
            r = Pr.resid(U)
            nf = float(np.sum(np.abs(r) ** 2))
    return U, math.sqrt(nf), it, status


def verify(Pr, U):
    v = Pr.v
    Id = np.eye(v)
    Gr = np.conj(U).transpose(0, 2, 1) @ U
    Q = U.transpose(0, 2, 1)
    C = Q.transpose(1, 0, 2)
    Gc = np.conj(C) @ C.transpose(0, 2, 1)
    S = Q[np.arange(v)[None, :], Pr.pos.T]
    Gs = np.conj(S) @ S.transpose(0, 2, 1)
    dev = {"rows": float(np.max(np.abs(Gr - Id))), "columns": float(np.max(np.abs(Gc - Id))),
           "classes": float(np.max(np.abs(Gs - Id)))}
    return dev, Q


def ray_count(Q, v):
    V = Q.reshape(v * v, v)
    V = V / np.linalg.norm(V, axis=1, keepdims=True)
    O = np.abs(np.conj(V) @ V.T) ** 2
    n = v * v
    parent = list(range(n))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    iu = np.triu_indices(n, 1)
    sep = 1.0 - O[iu]
    close = sep < 1e-7
    for a, b in zip(iu[0][close], iu[1][close]):
        parent[find(int(a))] = find(int(b))
    far = sep[~close]
    return len({find(a) for a in range(n)}), (float(far.min()) if far.size else 1.0)


def evaluate(Pr, U):
    if not np.all(np.isfinite(U)):
        return {"md": 1e9, "mdf": None}
    dev, Q = verify(Pr, U)
    md = max(dev.values())
    out = {"md": md, "mdf": [dev["rows"], dev["columns"], dev["classes"]]}
    if md < 1e-6:
        out["rays"], out["minsep"] = ray_count(Q, Pr.v)
    return out


def u_payload(Pr, U):
    return {"U_re": U[1:].real.tolist(), "U_im": U[1:].imag.tolist(), "B_matrix": Pr.B.tolist(), "B_name": Pr.name}


def run_one(Pr, U0, tag, extra):
    t0 = time.monotonic()
    U, res, it, st = lm(Pr, U0)
    rec = {"tag": tag, "v": Pr.v, "B": Pr.name, "st": st, "it": it, "res": res}
    rec.update(evaluate(Pr, U))
    rec.update(extra)
    rec["ok"] = bool(rec["md"] < 1e-8)
    rec["maximal_candidate"] = bool(Pr.v == 10 and rec["ok"] and rec.get("rays") == 100 and rec.get("minsep", 0.0) > 1e-6)
    rec["model_defect"] = bool(res < 1e-10 and rec["md"] >= 1e-8)
    save = rec["maximal_candidate"] or rec["model_defect"]
    if not save and rec["ok"] and Pr.v == 10 and tag.startswith("W") and SAVED["v10"] < 32:
        SAVED["v10"] += 1
        save = True
    if not save and rec["ok"] and tag.startswith("S8") and SAVED["S8"] < 8:
        SAVED["S8"] += 1
        save = True
    if save:
        rec.update(u_payload(Pr, U))
    rec["s"] = round(time.monotonic() - t0, 4)
    W(rec)
    if rec["model_defect"]:
        raise ModelDefectStop("model defect at " + tag)
    if rec["maximal_candidate"]:
        raise CandidateStop("unverified 100-ray candidate at " + tag)
    return rec, U


def summarize(tag, recs, skipped):
    ver = [r for r in recs if r["ok"]]
    rh, st = {}, {}
    for r in ver:
        rh[str(r.get("rays"))] = rh.get(str(r.get("rays")), 0) + 1
    for r in recs:
        st[r["st"]] = st.get(r["st"], 0) + 1
    res = sorted(r["res"] for r in recs)

    def q(f):
        return res[min(len(res) - 1, int(f * (len(res) - 1)))] if res else None
    s = {"summary": tag, "runs": len(recs), "skipped_time": skipped, "verified": len(ver), "verified_rays": rh,
         "status": st, "model_defects": sum(r["model_defect"] for r in recs),
         "maximal_candidates": sum(r["maximal_candidate"] for r in recs),
         "resid_quantiles": {"min": q(0.0), "q01": q(0.01), "q10": q(0.1), "median": q(0.5), "max": q(1.0)},
         "n_resid_lt": {"1e-2": sum(1 for x in res if x < 1e-2), "1e-4": sum(1 for x in res if x < 1e-4),
                        "1e-6": sum(1 for x in res if x < 1e-6)},
         "mean_s": (round(sum(r["s"] for r in recs) / len(recs), 4) if recs else None),
         "elapsed_s": round(elapsed(), 2)}
    W(s)
    return s


def random_stage(tag, Pr, n, seed0, end):
    recs, Us, skipped = [], [], 0
    for k in range(n):
        if over(end):
            skipped += 1
            continue
        rng = np.random.default_rng(seed0 + k)
        rec, U = run_one(Pr, rand_U(Pr.v, rng), tag, {"seed": seed0 + k})
        recs.append(rec)
        Us.append(U)
    if skipped:
        W({"tag": tag, "status": "SKIPPED_TIME", "count": skipped})
    return recs, Us, summarize(tag, recs, skipped)


def cyclic(v):
    return [[(j - i) % v for j in range(v)] for i in range(v)]


def xor(v):
    return [[i ^ j for j in range(v)] for i in range(v)]


def dihedral5():
    el = [(a, b) for b in range(2) for a in range(5)]
    idx = {g: t for t, g in enumerate(el)}

    def mul(g, h):
        return ((g[0] + (h[0] if g[1] == 0 else -h[0])) % 5, (g[1] + h[1]) % 2)

    def inv(g):
        return ((-g[0]) % 5, 0) if g[1] == 0 else g
    return [[idx[mul(inv(el[i]), el[j])] for j in range(10)] for i in range(10)]


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_anchor(d, key, N, den):
    z = np.exp(2j * np.pi * np.arange(N) / N)
    C = np.array(d[key]["U_form"], dtype=float)
    return (C @ z / den).transpose(0, 2, 1), d[key]["B"]


def jac_selftest(Pr, rng):
    U = rand_U(Pr.v, rng)
    th = rng.standard_normal(Pr.P)
    JTJ, JTr, res, Jr = Pr.normal(U)
    T = th.reshape(Pr.v - 1, Pr.nb)
    loc = np.zeros((Pr.npairs, 2 * Pr.nb))
    for k, (i, ip) in enumerate(Pr.pairs):
        if i >= 1:
            loc[k, :Pr.nb] = T[i - 1]
        loc[k, Pr.nb:] = T[ip - 1]
    Jt = np.einsum("nra,na->nr", Jr, loc)
    eps = 1e-4
    A = Pr.A_of(th)

    def pert(s):
        U2 = U.copy()
        U2[1:] = U[1:] @ (np.eye(Pr.v) + s * eps * A)
        rc = Pr.resid(U2)
        return np.concatenate([rc.real, rc.imag], axis=1)
    fd = (pert(1.0) - pert(-1.0)) / (2 * eps)
    e_fd = float(np.max(np.abs(Jt - fd)) / max(1.0, float(np.max(np.abs(Jt)))))
    e_ne = None
    if Pr.v <= 7:
        Jd = np.zeros((Pr.npairs * 4 * Pr.v, Pr.P))
        for k, (i, ip) in enumerate(Pr.pairs):
            rows = slice(k * 4 * Pr.v, (k + 1) * 4 * Pr.v)
            if i >= 1:
                Jd[rows, (i - 1) * Pr.nb:i * Pr.nb] = Jr[k, :, :Pr.nb]
            Jd[rows, (ip - 1) * Pr.nb:ip * Pr.nb] = Jr[k, :, Pr.nb:]
        rr = np.concatenate([res.real, res.imag], axis=1).reshape(-1)
        e_ne = max(float(np.max(np.abs(Jd.T @ Jd - JTJ)) / max(1.0, float(np.max(np.abs(JTJ))))),
                   float(np.max(np.abs(Jd.T @ rr - JTr)) / max(1.0, float(np.max(np.abs(JTr))))))
    U3 = Pr.retract(U, 0.3 * th / max(1.0, float(np.linalg.norm(th))))
    e_un = float(np.max(np.abs(np.conj(U3).transpose(0, 2, 1) @ U3 - np.eye(Pr.v))))
    return {"fd": e_fd, "normal_eq": e_ne, "retract_unitarity": e_un}


def near_stage(tag, Pr, Ua, seed0, end, want_rays):
    recs, ok = [], True
    for ai, amp in enumerate((1e-3, 1e-2, 0.1, 0.3)):
        for j in range(4):
            sd = seed0 + 10 * ai + j
            if over(end):
                ok = False
                W({"tag": tag, "amp": amp, "seed": sd, "status": "SKIPPED_TIME"})
                continue
            rng = np.random.default_rng(sd)
            g = rng.standard_normal(Pr.P)
            rec, _ = run_one(Pr, Pr.retract(Ua, amp * g), tag, {"amp": amp, "seed": sd})
            recs.append(rec)
    small = [r for r in recs if r["amp"] <= 1e-2]
    ok = ok and len(small) == 8 and all(r["ok"] for r in small) and \
        (want_rays is None or all(r.get("rays") == want_rays for r in small))
    by = {}
    for r in recs:
        k = "%g" % r["amp"]
        by.setdefault(k, [0, 0, {}])
        by[k][0] += 1
        by[k][1] += int(r["ok"])
        if r["ok"]:
            by[k][2][str(r.get("rays"))] = by[k][2].get(str(r.get("rays")), 0) + 1
    W({"summary": tag, "by_amp_runs_verified_rays": by, "elapsed_s": round(elapsed(), 2)})
    return ok, by, recs


def main():
    W({"assay": "rqls_fixedb_lm_v2", "numpy": np.__version__, "python": sys.version, "budget_s": BUDGET,
       "argv": sys.argv[1:], "flags": {"optimize": sys.flags.optimize, "isolated": sys.flags.isolated}})
    if sys.flags.optimize:
        raise GateFail("python optimize flag set")
    if MODE == "full":
        fixed = [("S", 60), ("N", 120), ("C", 60), ("KP", 300), ("KR", 900), ("S8", 420)]
    elif MODE == "target":
        fixed = [("S", 60), ("KP", 300)]
    else:
        raise GateFail("unknown MODE " + MODE)
    R = BUDGET - sum(b for _, b in fixed) - 120
    if R <= 0:
        raise GateFail("budget too small for MODE %s: R = %.1f s" % (MODE, R))
    plan = fixed + [("W", 0.6 * R), ("WD", 0.3 * R), ("WS", 0.1 * R)]
    ends, acc, t0 = {}, 0.0, time.monotonic()
    for tag, b in plan:
        acc += b
        ends[tag] = t0 + acc
    W({"plan_s": plan, "mode": MODE, "reserve_s": 120})
    # S: self-tests
    STAGE[0] = "S"
    pins = {"anchors": sha(ANCHORS[0]) == ANCHORS[1], "parker": sha(PARKER[0]) == PARKER[1]}
    gate("S_input_pins", all(pins.values()), {"pins": pins})
    with open(ANCHORS[0], "r", encoding="utf-8") as f:
        AN = json.load(f)
    with open(PARKER[0], "r", encoding="utf-8") as f:
        PK = json.load(f)["pairs"][0]
    U7, B7 = load_anchor(AN, "v7", 7, 7.0)
    U8, B8 = load_anchor(AN, "v8", 8, 2.0)
    Apk, Bpk = np.array(PK["A_array"]), np.array(PK["B_array"])
    sig = np.empty(10, dtype=np.int64)
    sig[Apk[0]] = np.arange(10)
    Arel = sig[Apk]
    U10 = np.zeros((10, 10, 10), dtype=complex)
    for i in range(10):
        U10[i, Arel[i], np.arange(10)] = 1.0
    orth = len({(int(a), int(b)) for a, b in zip(Arel.reshape(-1), Bpk.reshape(-1))}) == 100
    P7, P8, P10 = Problem(B7, "cyclic7_huang_li"), Problem(B8, "xor8_zhang_cao"), Problem(Bpk, "parker_z7p3_pair0_B")
    rng = np.random.default_rng(12345)
    js = {}
    for name, Pr in (("cyc4", Problem(cyclic(4), "cyc4")), ("cyc5", Problem(cyclic(5), "cyc5")), ("cyc7", P7),
                     ("xor8", P8), ("cyc10", Problem(cyclic(10), "cyc10")), ("d5", Problem(dihedral5(), "d5"))):
        js[name] = jac_selftest(Pr, rng)
    jok = all(t["fd"] < 1e-9 and (t["normal_eq"] is None or t["normal_eq"] < 1e-12) and t["retract_unitarity"] < 1e-12
              for t in js.values()) and js["cyc5"]["normal_eq"] is not None and js["cyc7"]["normal_eq"] is not None
    gate("S_jacobian", jok, {"by_B": js, "rule": "fd < 1e-9; block normal equations vs dense < 1e-12 (v <= 7); "
                                               "retraction unitarity < 1e-12"})
    an = {}
    for name, Pr, U, want in (("anchor7", P7, U7, 49), ("anchor8", P8, U8, 64), ("parker10", P10, U10, 10)):
        res = float(np.max(np.abs(Pr.resid(U))))
        ev = evaluate(Pr, U)
        g = np.random.default_rng(777).standard_normal(Pr.P)
        Um = U.copy()
        Um[1] = Pr.retract(U, 0.3 * g)[1]
        resm = float(np.linalg.norm(Pr.resid(Um)))
        u0 = float(np.max(np.abs(U[0] - np.eye(Pr.v))))
        an[name] = {"res": res, "md": ev["md"], "rays": ev.get("rays"), "minsep": ev.get("minsep"), "mut_res": resm,
                    "U0_dev": u0}
        an[name]["pass"] = bool(res < 1e-12 and ev["md"] < 1e-12 and ev.get("rays") == want and resm >= 0.01
                                and u0 == 0.0)
    an["parker10"]["orthogonal_mate"] = orth
    gate("S_anchors", all(a["pass"] for a in an.values()) and orth,
         {"anchors": an, "rule": "float residual < 1e-12, full Gram < 1e-12, rays 49/64/10, U_0 = I, mutation residual "
                                 ">= 0.01; Parker mate orthogonal"})
    if MODE == "full":
        # N: negative controls
        STAGE[0] = "N"
        nsum, st0 = {}, time.monotonic()
        for di, (v, seed0) in enumerate(((4, 100000), (6, 110000))):
            sub_end = st0 + (ends["N"] - st0) * (di + 1) / 2.0
            _, _, s = random_stage("N_negative_cyc%d" % v, Problem(cyclic(v), "cyc%d" % v), NN, seed0, sub_end)
            nsum[str(v)] = {"runs": s["runs"], "verified": s["verified"], "defects": s["model_defects"],
                            "min_res": s["resid_quantiles"]["min"]}
        gate("N_negative_controls", all(x["runs"] >= 1 and x["verified"] == 0 and x["defects"] == 0
                                        for x in nsum.values()),
             {"by_v": nsum, "rule": ">= 1 run, 0 verified, 0 model defects for Cay(Z_4) and Cay(Z_6)"})
        # C: classical-only control
        STAGE[0] = "C"
        recs, _, s = random_stage("C_classical_only_cyc5", Problem(cyclic(5), "cyc5"), NC, 120000, ends["C"])
        bad = [r for r in recs if r["ok"] and r.get("rays") != 5]
        gate("C_classical_only_v5", s["runs"] >= 1 and s["model_defects"] == 0 and not bad,
             {"runs": s["runs"], "verified": s["verified"], "verified_rays": s["verified_rays"], "non5": len(bad),
              "rule": ">= 1 run, 0 defects, every verified endpoint has exactly 5 rays"})
    # KP: near-anchor recovery
    STAGE[0] = "KP"
    kp_ok, kpd, st0 = True, {}, time.monotonic()
    for di, (name, Pr, Ua, want, seed0) in enumerate((("KP_anchor7", P7, U7, 49, 400000),
                                                       ("KP_anchor8", P8, U8, 64, 410000),
                                                       ("KP_parker10", P10, U10, None, 420000))):
        sub_end = st0 + (ends["KP"] - st0) * (di + 1) / 3.0
        ok, by, _ = near_stage(name, Pr, Ua, seed0, sub_end, want)
        kp_ok = kp_ok and ok
        kpd[name] = by
    gate("KP_near_anchor", kp_ok, {"by_anchor": kpd, "rule": "every amp <= 1e-2 run verified (8 per anchor); rays 49 at "
                                                               "v = 7 and 64 at v = 8; v = 10 rays recorded; 0 defects"})
    if MODE == "full":
        # KR: random recovery of known classes
        STAGE[0] = "KR"
        krs, st0 = {}, time.monotonic()
        tot = ends["KR"] - st0
        for name, Pr, n, seed0, frac in (("KR_random_cyc7", P7, NKR, 200000, 0.15),
                                         ("KR_random_xor8", P8, NKR, 210000, 0.25),
                                         ("KR_random_parker10", P10, NKR10, 220000, 0.60)):
            sub_end = time.monotonic() + tot * frac
            _, _, s = random_stage(name, Pr, n, seed0, min(sub_end, ends["KR"]))
            krs[name] = {"runs": s["runs"], "verified": s["verified"], "rays": s["verified_rays"],
                         "defects": s["model_defects"], "mean_s": s["mean_s"]}
        gate("KR_known_class_recovery", all(x["runs"] >= 1 and x["defects"] == 0 for x in krs.values()),
             {"by_B": krs, "rule": ">= 1 run per B and 0 model defects; counts recorded, not gated; NOT v = 10 "
                                   "detection power"})
        # S8: sensitivity probe
        STAGE[0] = "S8"
        random_stage("S8_cyc8", Problem(cyclic(8), "cyc8"), N8, 500000, ends["S8"])
    # W, WD: targets
    STAGE[0] = "W"
    Pw = Problem(cyclic(10), "cyc10")
    rw, uw, sw = random_stage("W_target_cyc10", Pw, NW, 1000000, ends["W"])
    STAGE[0] = "WD"
    Pd = Problem(dihedral5(), "d5")
    rd, ud, sd = random_stage("WD_target_d5", Pd, NWD, 1100000, ends["WD"])
    # WS: seeded target
    STAGE[0] = "WS"
    seeds = [(Pw, U) for r, U in zip(rw, uw) if r["ok"]] + [(Pd, U) for r, U in zip(rd, ud) if r["ok"]]
    ws, skipped = [], 0
    for k in range(min(NS, 4 * len(seeds))):
        if over(ends["WS"]):
            skipped += 1
            continue
        Pr, Us = seeds[k % len(seeds)]
        rng = np.random.default_rng(1200000 + k)
        rec, _ = run_one(Pr, Pr.retract(Us, 0.05 * rng.standard_normal(Pr.P)), "WS_target_seeded",
                         {"seed": 1200000 + k, "seed_B": Pr.name})
        ws.append(rec)
    if skipped:
        W({"tag": "WS_target_seeded", "status": "SKIPPED_TIME", "count": skipped})
    sws = summarize("WS_target_seeded", ws, skipped)
    keys = ("runs", "verified", "verified_rays", "maximal_candidates", "model_defects", "skipped_time")
    W({"end": True, "terminated": TERM[0], "target_cyc10": {k: sw[k] for k in keys}, "target_d5": {k: sd[k] for k in keys},
       "target_seeded": {k: sws[k] for k in keys}, "seed_pool": len(seeds), "records": NB[1], "bytes": NB[0],
       "elapsed_s": round(elapsed(), 2)})
    return 0


def stop_receipt(status, detail):
    try:
        with open(STOP_RECEIPT, "x", encoding="utf-8") as sf:
            json.dump({"status": status, "stage": STAGE[0], "detail": detail, "jsonl_records": NB[1], "jsonl_bytes": NB[0],
                       "elapsed_s": round(elapsed(), 2), "terminated": TERM[0]}, sf, indent=1)
    except OSError:
        pass


if __name__ == "__main__":
    code = 0
    try:
        code = main()
    except CapStop as ex:
        stop_receipt("CAP_STOP_UNKNOWN", repr(ex))
        code = 4
    except CandidateStop as ex:
        stop_receipt("CANDIDATE_UNVERIFIED_STOP", str(ex))
        code = 7
    except ModelDefectStop as ex:
        stop_receipt("MODEL_DEFECT_STOP", str(ex))
        code = 8
    except GateFail as ex:
        stop_receipt("GATE_FAIL_STOP", repr(ex))
        code = 3
    except Exception as ex:
        import traceback
        tb = traceback.format_exc()[-4000:]
        try:
            W({"exception": repr(ex), "traceback": tb, "elapsed_s": round(elapsed(), 2)})
        except CapStop:
            pass
        stop_receipt("EXCEPTION_STOP", tb)
        code = 2
    if code == 0 and TERM[0]:
        stop_receipt("TERMINATED_UNKNOWN", "SIGTERM received; stages after the flag are incomplete")
        code = 5
    fh.close()
    sys.exit(code)
