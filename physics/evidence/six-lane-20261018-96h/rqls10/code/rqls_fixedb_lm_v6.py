#!/usr/bin/env python3
"""rqls_fixedb_lm_v6: float Levenberg-Marquardt assay of the FIXED-B UNITARY MODEL (no orbit symmetry) for 1-RQLS(v)
(design note evidence/fixedb-unitary-model-proposal-v1.md). NOT a certificate; any target miss is a scoped UNKNOWN; a
qualifying endpoint is CANDIDATE_UNVERIFIED until independent exact or certified-interval verification.

Model (unchanged from v1-v4): B fixed Latin square; q_ij = U_i e_j with U_0 = I; unknowns U_1..U_{v-1} unitary; for
i < i', M = U_i^* U_i', residual = M[p,p] (columns) and M[p,pi(p)] (B-classes), pi(p) = column j' with
B[i'][j'] = B[i][p]; 2 v^2 (v-1) reals. Chart U_k <- U_k expm(A_k), A_k skew-Hermitian with zero diagonal, v (v-1)^2
real parameters; analytic Jacobian dM = -A_i M + M A_i' (A_0 = 0), pair-block normal equations; LM damping lam0 1e-3,
x10 on failure (12 tries), /3 on success, floor 1e-12; tolerance |r|^2 < 1e-26; polar re-unitarisation every 25
iterations. Every endpoint: full float Gram of all v rows, v columns, v B-classes; float-verified = finite deviation
< 1e-8; rays merged at 1 - |<q,q'>|^2 < 1e-7 ("minsep_nonmerged" = minimum separation over pairs NOT merged, which for
a v^2-ray endpoint is the minimum over all pairs).

v5 changes (Codex HOLD on v4, RUN/review/rqls10-fixedB-v4-source-codex-v1.prompt.stdout.txt):
 1. Protocol order: SIGTERM handler installed first, then the "GO" line is read, then NumPy is imported (no native
    numerical initialisation before GO); argument parsing and output opening happen inside the protected main path.
 2. LM halt precedence TERMINATED > DEADLINE > CONVERGED > STALL > MAX_ITER. The halt condition (SIGTERM flag; the
    effective deadline = min(stage end, T0 + BUDGET)) is checked before the initial residual, at the start of every
    iteration BEFORE the convergence test, after the normal-equation assembly, before each damping retry, after each
    solve, after each trial bundle (retraction + residual), before and after polar repair, and once more before every
    return (including exits from the retry loop). A halted run returns the last accepted finite iterate with status
    TERMINATED or DEADLINE and records pre_halt_status, the halt point ("where"), its monotonic time and iteration.
 3. Guarded run entry: start initialisation (Haar start, near-anchor or seeded retraction) runs inside run_entry() only
    after TERM and the effective deadline were checked; both are checked again after initialisation and immediately
    before LM entry. A run whose deadline passed before LM entry is not started (recorded NOT_STARTED_DEADLINE). The S
    stage checks TERM and BUDGET between numerical bundles. gate() reconciles TERM before and after writing.
 4. Modes: "full" (Phase 1) and "q1" (bounded behaviour qualification). Both run S, N, C, KP and KR with all their gates
    before any target stage; the former "target" mode (which skipped N, C, KR) is removed. "q1" uses fixed stage slots
    S 60, N 60, C 30, KP 300, KR 150, W 150, WD 150, WS 50 s (plan origin + cumulative ends) and needs BUDGET >= 1070.
 5. Telemetry: unrounded monotonic times of GO read (T0), plan origin, every planned stage end, every actual stage start
    and end, and per run: entry, initialisation done, LM start, last iteration start, halt observation, LM end, record
    write. Runtime identity: interpreter path/realpath/sha256, NumPy version and file, np.show_config(mode="dicts"),
    thread environment; gate S_single_thread (process CPU time / wall time <= 1.3 for repeated 1200 x 1200 matmuls).
 6. Witness reservation: ordinary JSONL records may use CAP - RESERVE bytes; a maximal-candidate or model-defect record
    may use the reserve, and is FIRST written to a separate exclusive WITNESS file (full U, B, seed, tag, convention). A
    witness or stop-receipt persistence failure is reported on stderr and gives exit code 9 (never silently ignored).
 7. S_anchors U_0 test uses max|U_0 - I| < 1e-14 (the Huang-Li anchor's U_0 is I only to rounding; v1-v4 required
    exact 0.0, which would have failed the gate).
 8. Records: finiteness flags (res_finite, md_finite), U convention ("U_re/U_im hold U_1..U_{v-1}; prepend U_0 = I"),
    WS parent endpoint identity (tag, seed).
 v6 (= v5 draft, never run, plus): np.show_config(mode="dicts") is passed through a JSON round trip with default=str
    (a non-serialisable value would otherwise crash the very first record); the first record also carries pid, pgid
    and ppid.
Stages (deterministic seeds; stage ends absolute from the plan origin; a stage starts when the previous one ends):
 S   gates S_runtime, S_single_thread, S_input_pins, S_jacobian (central differences, exact for bilinear M, < 1e-9;
     block vs dense normal equations at v = 5, 7 < 1e-12; retraction unitarity < 1e-12), S_anchors (Huang-Li v = 7:
     49 rays; Zhang-Cao v = 8: 64 rays; Parker v = 10: 10 rays; residual and Gram < 1e-12, U_0 = I to 1e-14, mutation
     residual >= 0.01).
 N   Cay(Z_4), Cay(Z_6) random starts: >= 1 run each, 0 verified, 0 defects (imports: Zhang-Cao arXiv:2608.29201v2
     Sec. 3 citing Ball-Simoens).
 C   Cay(Z_5): >= 1 run, 0 defects, every verified endpoint exactly 5 rays (same import).
 KP  near-anchor recovery at the three anchors, amp per chart coordinate in {1e-3, 1e-2, 0.1, 0.3} x 4 seeds; gate:
     the 8 runs with amp <= 1e-2 per anchor all started (none NOT_STARTED / SKIPPED) and float-verified, with 49 rays
     (v = 7) and 64 rays (v = 8); v = 10 rays recorded; 0 defects.
 KR  random starts on cyclic v = 7, XOR v = 8 (NKR each) and the Parker v = 10 B (NKR10): >= 1 run each, 0 defects;
     counts recorded, NOT detection power for v = 10 targets.
 S8  (full only, recorded) Cay(Z_8) x N8.  W Cay(Z_10) x NW.  WD Cay(D_5) x NWD.  WS up to NS seeded starts.
Immediate stops (after the endpoint record): v = 10 float-verified 100-ray endpoint with minsep_nonmerged > 1e-6 in
ANY stage -> exit 7; LM residual < 1e-10 with full deviation >= 1e-8 -> exit 8. Then TERMINATED -> exit 5.
Usage: rqls_fixedb_lm_v6.py OUT.jsonl WITNESS.json STOP_RECEIPT.json BUDGET_S MODE NN NC NKR NKR10 N8 NW NWD NS
Protocol (supervisor): no computation and no NumPy import before the line "GO" on stdin (otherwise exit 6, no output).
Exit codes: 0 done, 2 exception, 3 gate failure, 4 output cap, 5 SIGTERM, 6 no GO, 7 maximal candidate (unverified),
8 model defect, 9 witness or stop-receipt persistence failure. On every non-zero exit after GO an exclusive stop
receipt is attempted.
"""
import hashlib, json, math, os, signal, sys, time

TERM = [False]
TERM_MONO = [None]


def _on_term(s, f):
    if not TERM[0]:
        TERM_MONO[0] = time.monotonic()
    TERM[0] = True


signal.signal(signal.SIGTERM, _on_term)
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic()
import numpy as np  # noqa: E402  (deliberately after GO)

T_NUMPY = time.monotonic()
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ANCHORS = (LANE + "/evidence/fixedb_anchors_v1.result.json",
           "13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92")
PARKER = (LANE + "/evidence/parker_z7p3_classical_v1.result.json",
          "00e991d692e669411a49d45aa1623c52189346dc32acb6fb1feea1858b841c30")
CAP = 8 * 1024 * 1024
RESERVE = 1024 * 1024
ITERS = 300
ST = {"fh": None, "nb": 0, "nr": 0, "stage": "init", "out": None, "witness": None, "stop": None, "budget": None}
SAVED = {"v10": 0, "S8": 0}
U_CONVENTION = "U_re/U_im hold U_1..U_{v-1} as [k][row s][column j]; prepend U_0 = I; q_ij = U_i e_j"


class CapStop(Exception):
    pass


class GateFail(Exception):
    pass


class CandidateStop(Exception):
    pass


class ModelDefectStop(Exception):
    pass


class TermStop(Exception):
    pass


class PersistFail(Exception):
    pass


def mono():
    return time.monotonic()


def W(o, reserve_ok=False):
    s = json.dumps(o, separators=(",", ":"), allow_nan=False) + "\n"
    b = len(s.encode("utf-8"))
    limit = CAP if reserve_ok else CAP - RESERVE
    if ST["nb"] + b > limit:
        raise CapStop("jsonl cap %d bytes reached" % limit)
    ST["fh"].write(s)
    ST["fh"].flush()
    ST["nb"] += b
    ST["nr"] += 1


def elapsed():
    return mono() - T0


def term_check(where):
    if TERM[0]:
        raise TermStop("SIGTERM observed at " + where)


def budget_check(where):
    term_check(where)
    if elapsed() > ST["budget"]:
        raise GateFail("BUDGET_EXHAUSTED at " + where)


def gate(tag, ok, detail):
    term_check("gate " + tag)
    W({"GATE": tag, "pass": bool(ok), "detail": detail, "mono": mono()})
    if TERM[0]:
        W({"GATE_TERM_RECONCILE": tag, "mono": mono(), "term_mono": TERM_MONO[0]})
        raise TermStop("SIGTERM observed while writing gate " + tag)
    if not ok:
        raise GateFail(tag)


def finite(x):
    return x is not None and isinstance(x, float) and math.isfinite(x)


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


def lm(Pr, U, dl, iters=ITERS, tol=1e-26):
    """returns (U, residual norm, iterations, status, telemetry). Precedence TERMINATED > DEADLINE > other statuses."""
    tel = {"halt": None, "pre_halt_status": None, "last_iter_start_mono": None}

    def halt(where, it):
        if TERM[0]:
            h = "TERMINATED"
        elif mono() > dl:
            h = "DEADLINE"
        else:
            return None
        if tel["halt"] is None:
            tel["halt"] = {"reason": h, "where": where, "it": it, "mono": mono(), "term_mono": TERM_MONO[0]}
        return h
    status, it, lam = "MAX_ITER", 0, 1e-3
    h = halt("entry", 0)
    if h:
        return U, None, 0, h, tel
    r = Pr.resid(U)
    nf = float(np.sum(np.abs(r) ** 2))
    h = halt("after_initial_residual", 0)
    if h:
        tel["pre_halt_status"] = "NOT_ITERATED"
        return U, math.sqrt(nf), 0, h, tel
    for it in range(1, iters + 1):
        tel["last_iter_start_mono"] = mono()
        h = halt("iteration_start", it)
        if h:
            status = h
            break
        if nf < tol:
            status = "CONVERGED"
            break
        JTJ, JTr, _, _ = Pr.normal(U)
        h = halt("after_normal", it)
        if h:
            status = h
            break
        improved = False
        for _ in range(12):
            h = halt("before_solve", it)
            if h:
                break
            try:
                step = np.linalg.solve(JTJ + lam * Pr.eye, -JTr)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            h = halt("after_solve", it)
            if h:
                break
            if not np.all(np.isfinite(step)):
                lam *= 10
                continue
            U2 = Pr.retract(U, step)
            r2 = Pr.resid(U2)
            n2 = float(np.sum(np.abs(r2) ** 2))
            if math.isfinite(n2) and n2 < nf:
                U, r, nf = U2, r2, n2
                lam = max(lam / 3, 1e-12)
                improved = True
            h = halt("after_trial", it)
            if h or improved:
                break
            lam *= 10
        if h:
            status = h
            break
        if not improved:
            status = "STALL"
            break
        if it % 25 == 0:
            h = halt("before_polar", it)
            if h:
                status = h
                break
            Up = polar(U)
            rp = Pr.resid(Up)
            npf = float(np.sum(np.abs(rp) ** 2))
            if math.isfinite(npf):
                U, r, nf = Up, rp, npf
            h = halt("after_polar", it)
            if h:
                status = h
                break
    h = halt("before_return", it)
    if h and status not in ("TERMINATED", "DEADLINE"):
        tel["pre_halt_status"] = status
        status = h
    elif h and status == "DEADLINE" and h == "TERMINATED":
        tel["pre_halt_status"] = status
        status = h
    return U, math.sqrt(nf), it, status, tel


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
        return {"md": None, "mdf": None, "md_finite": False}
    dev, Q = verify(Pr, U)
    md = max(dev.values())
    out = {"md": md, "mdf": [dev["rows"], dev["columns"], dev["classes"]],
           "md_finite": all(math.isfinite(x) for x in dev.values())}
    if out["md_finite"] and md < 1e-6:
        out["rays"], out["minsep_nonmerged"] = ray_count(Q, Pr.v)
    return out


def u_payload(Pr, U):
    return {"U_re": U[1:].real.tolist(), "U_im": U[1:].imag.tolist(), "B_matrix": Pr.B.tolist(), "B_name": Pr.name,
            "U_convention": U_CONVENTION}


def persist_witness(rec):
    data = (json.dumps(rec, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
    try:
        fd = os.open(ST["witness"], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        try:
            view = memoryview(data)
            while view:
                k = os.write(fd, view)
                view = view[k:]
            os.fsync(fd)
        finally:
            os.close(fd)
    except OSError as ex:
        raise PersistFail("witness persistence failed: %r" % ex)


def run_entry(Pr, init_fn, tag, extra, end):
    """guarded run entry; returns (record, U) or (None, None) if the deadline passed before LM entry."""
    dl = min(end, T0 + ST["budget"])
    m_entry = mono()
    term_check("run entry " + tag)
    if m_entry > dl:
        return None, None
    U0 = init_fn()
    m_init = mono()
    term_check("after initialisation " + tag)
    if mono() > dl:
        W({"tag": tag, "status": "NOT_STARTED_DEADLINE", "mono_entry": m_entry, "mono_init_done": m_init})
        return None, None
    m_lm0 = mono()
    U, res, it, st, tel = lm(Pr, U0, dl)
    m_lm1 = mono()
    rec = {"tag": tag, "v": Pr.v, "B": Pr.name, "st": st, "it": it, "res": res,
           "res_finite": res is not None and math.isfinite(res), "mono_entry": m_entry, "mono_init_done": m_init,
           "mono_lm_start": m_lm0, "mono_lm_end": m_lm1, "deadline_mono": dl}
    rec.update(tel)
    rec.update(evaluate(Pr, U))
    rec.update(extra)
    rec["ok"] = bool(rec["md_finite"] and rec["md"] < 1e-8)
    rec["maximal_candidate"] = bool(Pr.v == 10 and rec["ok"] and rec.get("rays") == 100 and
                                    rec.get("minsep_nonmerged", 0.0) > 1e-6)
    rec["model_defect"] = bool(rec["res_finite"] and res < 1e-10 and rec["md_finite"] and rec["md"] >= 1e-8)
    special = rec["maximal_candidate"] or rec["model_defect"]
    save = special
    if not save and rec["ok"] and Pr.v == 10 and tag.startswith("W") and SAVED["v10"] < 32:
        SAVED["v10"] += 1
        save = True
    if not save and rec["ok"] and tag.startswith("S8") and SAVED["S8"] < 8:
        SAVED["S8"] += 1
        save = True
    if save:
        rec.update(u_payload(Pr, U))
    if special:
        persist_witness(dict(rec, stage=ST["stage"]))
    rec["mono_record"] = mono()
    W(rec, reserve_ok=special)
    if rec["model_defect"]:
        raise ModelDefectStop("model defect at " + tag)
    if rec["maximal_candidate"]:
        raise CandidateStop("unverified 100-ray candidate at " + tag)
    if st == "TERMINATED" or TERM[0]:
        raise TermStop("SIGTERM during or right after a %s run (status %s, it %d)" % (tag, st, it))
    return rec, U


def stage_begin(name, end):
    ST["stage"] = name
    W({"STAGE": name, "mono_start": mono(), "mono_end_planned": end})


def stage_end(name):
    W({"STAGE_END": name, "mono_end_actual": mono()})


def summarize(tag, recs, skipped):
    ver = [r for r in recs if r["ok"]]
    rh, st = {}, {}
    for r in ver:
        rh[str(r.get("rays"))] = rh.get(str(r.get("rays")), 0) + 1
    for r in recs:
        st[r["st"]] = st.get(r["st"], 0) + 1
    res = sorted(r["res"] for r in recs if r["res_finite"])

    def q(f):
        return res[min(len(res) - 1, int(f * (len(res) - 1)))] if res else None
    s = {"summary": tag, "runs": len(recs), "skipped_time": skipped, "verified": len(ver), "verified_rays": rh,
         "status": st, "model_defects": sum(r["model_defect"] for r in recs),
         "maximal_candidates": sum(r["maximal_candidate"] for r in recs),
         "resid_quantiles": {"min": q(0.0), "q01": q(0.01), "q10": q(0.1), "median": q(0.5), "max": q(1.0)},
         "mean_lm_s": (sum(r["mono_lm_end"] - r["mono_lm_start"] for r in recs) / len(recs) if recs else None),
         "mono": mono()}
    W(s)
    return s


def random_stage(tag, Pr, n, seed0, end):
    recs, Us, skipped = [], [], 0
    for k in range(n):
        rng = np.random.default_rng(seed0 + k)
        rec, U = run_entry(Pr, lambda: rand_U(Pr.v, rng), tag, {"seed": seed0 + k}, end)
        if rec is None:
            skipped = n - k
            break
        recs.append(rec)
        Us.append(U)
    if skipped:
        W({"tag": tag, "status": "SKIPPED_TIME", "count": skipped, "mono": mono()})
    return recs, Us, summarize(tag, recs, skipped)


def cyclic(v):
    return [[(j - i) % v for j in range(v)] for i in range(v)]


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
    recs, missing_small = [], 0
    for ai, amp in enumerate((1e-3, 1e-2, 0.1, 0.3)):
        for j in range(4):
            sd = seed0 + 10 * ai + j
            rng = np.random.default_rng(sd)
            rec, _ = run_entry(Pr, lambda: Pr.retract(Ua, amp * rng.standard_normal(Pr.P)), tag,
                               {"amp": amp, "seed": sd}, end)
            if rec is None:
                missing_small += int(amp <= 1e-2)
                W({"tag": tag, "amp": amp, "seed": sd, "status": "SKIPPED_TIME", "mono": mono()})
                continue
            recs.append(rec)
    small = [r for r in recs if r["amp"] <= 1e-2]
    ok = missing_small == 0 and len(small) == 8 and all(r["ok"] for r in small) and \
        (want_rays is None or all(r.get("rays") == want_rays for r in small)) and \
        not any(r["model_defect"] for r in recs)
    by = {}
    for r in recs:
        k = "%g" % r["amp"]
        by.setdefault(k, [0, 0, {}])
        by[k][0] += 1
        by[k][1] += int(r["ok"])
        if r["ok"]:
            by[k][2][str(r.get("rays"))] = by[k][2].get(str(r.get("rays")), 0) + 1
    W({"summary": tag, "by_amp_runs_verified_rays": by, "missing_small": missing_small, "mono": mono()})
    return ok, by, recs


def runtime_identity():
    exe = sys.executable
    real = os.path.realpath(exe)
    try:
        cfgd = json.loads(json.dumps(np.show_config(mode="dicts"), default=str))
    except Exception as ex:
        cfgd = {"error": repr(ex)}
    return {"executable": exe, "realpath": real, "realpath_sha256": sha(real), "python": sys.version,
            "numpy": np.__version__, "numpy_file": np.__file__, "numpy_config": cfgd,
            "thread_env": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
                                                           "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS")},
            "flags": {"optimize": sys.flags.optimize, "isolated": sys.flags.isolated,
                      "dont_write_bytecode": sys.flags.dont_write_bytecode}}


def single_thread_check():
    a = np.random.default_rng(5).standard_normal((1200, 1200))
    c0, w0 = time.process_time(), mono()
    for _ in range(3):
        a = a @ a
        a /= np.max(np.abs(a))
    c1, w1 = time.process_time(), mono()
    ratio = (c1 - c0) / max(w1 - w0, 1e-9)
    return {"cpu_s": c1 - c0, "wall_s": w1 - w0, "ratio": ratio}


def main(args):
    OUT, WITNESS, STOPR = args[0], args[1], args[2]
    ST["witness"], ST["stop"] = WITNESS, STOPR
    BUDGET, MODE = float(args[3]), args[4]
    NN, NC, NKR, NKR10, N8, NW, NWD, NS = (int(a) for a in args[5:13])
    ST["budget"] = BUDGET
    ST["fh"] = open(OUT, "x", encoding="utf-8")
    origin = mono()
    if MODE == "full":
        fixed = [("S", 60), ("N", 120), ("C", 60), ("KP", 300), ("KR", 900), ("S8", 420)]
        R = BUDGET - sum(b for _, b in fixed) - 120
        plan = fixed + [("W", 0.6 * R), ("WD", 0.3 * R), ("WS", 0.1 * R)] if R > 0 else None
    elif MODE == "q1":
        plan = [("S", 60), ("N", 60), ("C", 30), ("KP", 300), ("KR", 150), ("W", 150), ("WD", 150), ("WS", 50)]
        if BUDGET < sum(b for _, b in plan) + 120:
            plan = None
    else:
        plan = None
    ends, acc = {}, 0.0
    for tag, b in (plan or []):
        acc += b
        ends[tag] = origin + acc
    W({"assay": "rqls_fixedb_lm_v6", "argv": sys.argv[1:], "mode": MODE, "budget_s": BUDGET,
       "pid": os.getpid(), "pgid": os.getpgrp(), "ppid": os.getppid(),
       "T0_go_mono": T0, "numpy_imported_mono": T_NUMPY, "plan_origin_mono": origin, "plan_s": plan,
       "plan_end_mono": ends, "runtime": runtime_identity(), "cap": CAP, "reserve": RESERVE})
    if plan is None:
        raise GateFail("unknown MODE or budget too small for MODE %s" % MODE)
    stage_begin("S", ends["S"])
    rt = runtime_identity()
    gate("S_runtime", sys.flags.optimize == 0 and sys.flags.isolated == 1 and
         all(v == "1" for v in rt["thread_env"].values()), {"thread_env": rt["thread_env"], "flags": rt["flags"]})
    stc = single_thread_check()
    gate("S_single_thread", stc["ratio"] <= 1.3, stc)
    budget_check("S pins")
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
        budget_check("S jacobian " + name)
        js[name] = jac_selftest(Pr, rng)
    jok = all(t["fd"] < 1e-9 and (t["normal_eq"] is None or t["normal_eq"] < 1e-12) and t["retract_unitarity"] < 1e-12
              for t in js.values()) and js["cyc5"]["normal_eq"] is not None and js["cyc7"]["normal_eq"] is not None
    gate("S_jacobian", jok, {"by_B": js, "rule": "fd < 1e-9; block vs dense normal equations < 1e-12 (v <= 7); "
                                               "retraction unitarity < 1e-12"})
    an = {}
    for name, Pr, U, want in (("anchor7", P7, U7, 49), ("anchor8", P8, U8, 64), ("parker10", P10, U10, 10)):
        budget_check("S anchors " + name)
        res = float(np.max(np.abs(Pr.resid(U))))
        ev = evaluate(Pr, U)
        g = np.random.default_rng(777).standard_normal(Pr.P)
        Um = U.copy()
        Um[1] = Pr.retract(U, 0.3 * g)[1]
        resm = float(np.linalg.norm(Pr.resid(Um)))
        u0 = float(np.max(np.abs(U[0] - np.eye(Pr.v))))
        an[name] = {"res": res, "md": ev["md"], "rays": ev.get("rays"), "minsep_nonmerged": ev.get("minsep_nonmerged"),
                    "mut_res": resm, "U0_dev": u0}
        an[name]["pass"] = bool(res < 1e-12 and ev["md_finite"] and ev["md"] < 1e-12 and ev.get("rays") == want and
                                resm >= 0.01 and u0 < 1e-14)
    an["parker10"]["orthogonal_mate"] = orth
    gate("S_anchors", all(a["pass"] for a in an.values()) and orth,
         {"anchors": an, "rule": "residual < 1e-12, full Gram < 1e-12, rays 49/64/10, max|U_0 - I| < 1e-14, mutation "
                                 "residual >= 0.01; Parker mate orthogonal"})
    stage_end("S")
    stage_begin("N", ends["N"])
    nsum, st0 = {}, mono()
    for di, (v, seed0) in enumerate(((4, 100000), (6, 110000))):
        sub_end = st0 + (ends["N"] - st0) * (di + 1) / 2.0
        _, _, s = random_stage("N_negative_cyc%d" % v, Problem(cyclic(v), "cyc%d" % v), NN, seed0, sub_end)
        nsum[str(v)] = {"runs": s["runs"], "verified": s["verified"], "defects": s["model_defects"],
                        "min_res": s["resid_quantiles"]["min"]}
    gate("N_negative_controls", all(x["runs"] >= 1 and x["verified"] == 0 and x["defects"] == 0 for x in nsum.values()),
         {"by_v": nsum, "rule": ">= 1 run, 0 verified, 0 model defects for Cay(Z_4) and Cay(Z_6)"})
    stage_end("N")
    stage_begin("C", ends["C"])
    recs, _, s = random_stage("C_classical_only_cyc5", Problem(cyclic(5), "cyc5"), NC, 120000, ends["C"])
    bad = [r for r in recs if r["ok"] and r.get("rays") != 5]
    gate("C_classical_only_v5", s["runs"] >= 1 and s["model_defects"] == 0 and not bad,
         {"runs": s["runs"], "verified": s["verified"], "verified_rays": s["verified_rays"], "non5": len(bad),
          "rule": ">= 1 run, 0 defects, every verified endpoint has exactly 5 rays"})
    stage_end("C")
    stage_begin("KP", ends["KP"])
    kp_ok, kpd, st0 = True, {}, mono()
    for di, (name, Pr, Ua, want, seed0) in enumerate((("KP_anchor7", P7, U7, 49, 400000),
                                                       ("KP_anchor8", P8, U8, 64, 410000),
                                                       ("KP_parker10", P10, U10, None, 420000))):
        sub_end = st0 + (ends["KP"] - st0) * (0.2, 0.5, 1.0)[di]
        ok, by, _ = near_stage(name, Pr, Ua, seed0, sub_end, want)
        kp_ok = kp_ok and ok
        kpd[name] = by
    gate("KP_near_anchor", kp_ok, {"by_anchor": kpd, "rule": "the 8 runs with amp <= 1e-2 per anchor all started and "
                                                               "float-verified; rays 49 at v = 7 and 64 at v = 8; v = 10 "
                                                               "rays recorded; 0 defects"})
    stage_end("KP")
    stage_begin("KR", ends["KR"])
    krs, st0 = {}, mono()
    tot = ends["KR"] - st0
    for name, Pr, n, seed0, frac in (("KR_random_cyc7", P7, NKR, 200000, 0.15), ("KR_random_xor8", P8, NKR, 210000, 0.25),
                                     ("KR_random_parker10", P10, NKR10, 220000, 0.60)):
        sub_end = min(mono() + tot * frac, ends["KR"])
        _, _, s = random_stage(name, Pr, n, seed0, sub_end)
        krs[name] = {"runs": s["runs"], "verified": s["verified"], "rays": s["verified_rays"],
                     "defects": s["model_defects"], "mean_lm_s": s["mean_lm_s"]}
    gate("KR_known_class_recovery", all(x["runs"] >= 1 and x["defects"] == 0 for x in krs.values()),
         {"by_B": krs, "rule": ">= 1 run per B and 0 model defects; counts not gated; NOT v = 10 detection power"})
    stage_end("KR")
    if MODE == "full":
        stage_begin("S8", ends["S8"])
        random_stage("S8_cyc8", Problem(cyclic(8), "cyc8"), N8, 500000, ends["S8"])
        stage_end("S8")
    stage_begin("W", ends["W"])
    Pw = Problem(cyclic(10), "cyc10")
    rw, uw, sw = random_stage("W_target_cyc10", Pw, NW, 1000000, ends["W"])
    stage_end("W")
    stage_begin("WD", ends["WD"])
    Pd = Problem(dihedral5(), "d5")
    rd, ud, sd = random_stage("WD_target_d5", Pd, NWD, 1100000, ends["WD"])
    stage_end("WD")
    stage_begin("WS", ends["WS"])
    seeds = [(Pw, U, r) for r, U in zip(rw, uw) if r["ok"]] + [(Pd, U, r) for r, U in zip(rd, ud) if r["ok"]]
    ws, skipped = [], 0
    count = min(NS, 4 * len(seeds))
    for k in range(count):
        Pr, Us, pr = seeds[k % len(seeds)]
        rng = np.random.default_rng(1200000 + k)
        rec, _ = run_entry(Pr, lambda: Pr.retract(Us, 0.05 * rng.standard_normal(Pr.P)), "WS_target_seeded",
                           {"seed": 1200000 + k, "seed_B": Pr.name,
                            "seed_parent": {"tag": pr["tag"], "seed": pr.get("seed")}}, ends["WS"])
        if rec is None:
            skipped = count - k
            break
        ws.append(rec)
    if skipped:
        W({"tag": "WS_target_seeded", "status": "SKIPPED_TIME", "count": skipped, "mono": mono()})
    sws = summarize("WS_target_seeded", ws, skipped)
    stage_end("WS")
    keys = ("runs", "verified", "verified_rays", "maximal_candidates", "model_defects", "skipped_time")
    W({"end": True, "terminated": TERM[0], "target_cyc10": {k: sw[k] for k in keys}, "target_d5": {k: sd[k] for k in keys},
       "target_seeded": {k: sws[k] for k in keys}, "seed_pool": len(seeds), "records": ST["nr"], "bytes": ST["nb"],
       "mono": mono()})
    return 0


def stop_receipt(status, detail):
    if ST["stop"] is None:
        sys.stderr.write("STOP_RECEIPT_PATH_UNKNOWN %s %s\n" % (status, detail[:2000]))
        return False
    try:
        data = (json.dumps({"status": status, "stage": ST["stage"], "detail": detail, "jsonl_records": ST["nr"],
                            "jsonl_bytes": ST["nb"], "mono": mono(), "T0_go_mono": T0, "terminated": TERM[0],
                            "term_mono": TERM_MONO[0]}, indent=1) + "\n").encode("utf-8")
        fd = os.open(ST["stop"], os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        try:
            os.write(fd, data)
            os.fsync(fd)
        finally:
            os.close(fd)
        return True
    except OSError as ex:
        sys.stderr.write("STOP_RECEIPT_FAILED %r %s %s\n" % (ex, status, detail[:2000]))
        return False


if __name__ == "__main__":
    code, status, detail = 0, None, ""
    try:
        if len(sys.argv) != 14:
            raise GateFail("usage: OUT WITNESS STOP_RECEIPT BUDGET_S MODE NN NC NKR NKR10 N8 NW NWD NS")
        ST["stop"] = sys.argv[3]
        code = main(sys.argv[1:])
    except CapStop as ex:
        code, status, detail = 4, "CAP_STOP_UNKNOWN", repr(ex)
    except CandidateStop as ex:
        code, status, detail = 7, "CANDIDATE_UNVERIFIED_STOP", str(ex)
    except ModelDefectStop as ex:
        code, status, detail = 8, "MODEL_DEFECT_STOP", str(ex)
    except PersistFail as ex:
        code, status, detail = 9, "WITNESS_PERSISTENCE_FAILED", str(ex)
        sys.stderr.write(detail + "\n")
    except GateFail as ex:
        code, status, detail = 3, "GATE_FAIL_STOP", repr(ex)
    except TermStop as ex:
        code, status, detail = 5, "TERMINATED_UNKNOWN", str(ex)
    except Exception as ex:
        import traceback
        tb = traceback.format_exc()[-4000:]
        try:
            if ST["fh"] is not None:
                W({"exception": repr(ex), "traceback": tb, "mono": mono()}, reserve_ok=True)
        except Exception:
            pass
        code, status, detail = 2, "EXCEPTION_STOP", tb
    if code == 0 and TERM[0]:
        code, status, detail = 5, "TERMINATED_UNKNOWN", "SIGTERM received; stages after the flag are incomplete"
    if code != 0:
        if not stop_receipt(status, detail):
            code = 9
    try:
        if ST["fh"] is not None:
            ST["fh"].close()
    except OSError as ex:
        sys.stderr.write("OUT_CLOSE_FAILED %r\n" % ex)
        code = 9
    sys.exit(code)
