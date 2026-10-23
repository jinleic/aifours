#!/usr/bin/env python3
"""rqls_fixedb_lm_v7: float Levenberg-Marquardt assay of the FIXED-B UNITARY MODEL (no orbit symmetry) for 1-RQLS(v)
(design note evidence/fixedb-unitary-model-proposal-v1.md). NOT a certificate; any target miss is a scoped UNKNOWN; a
qualifying endpoint is CANDIDATE_UNVERIFIED until independent exact or certified-interval verification.

Model, LM, stages, seeds, amplitudes, gates and stop rules are unchanged from v6 (controls unchanged): B fixed Latin
square; q_ij = U_i e_j with U_0 = I; unknowns U_1..U_{v-1} unitary; for i < i', M = U_i^* U_i', residual = M[p,p]
(columns) and M[p,pi(p)] (B-classes), pi(p) = column j' with B[i'][j'] = B[i][p]; 2 v^2 (v-1) reals. Chart U_k <- U_k
expm(A_k), A_k skew-Hermitian with zero diagonal, v (v-1)^2 real parameters; analytic Jacobian dM = -A_i M + M A_i'
(A_0 = 0), pair-block normal equations; LM damping lam0 1e-3, x10 on failure (12 tries), /3 on success, floor 1e-12;
tolerance |r|^2 < 1e-26; polar re-unitarisation every 25 iterations. Every endpoint: full float Gram of all v rows, v
columns, v B-classes; float-verified = finite deviation < 1e-8; rays merged at 1 - |<q,q'>|^2 < 1e-7 (transitively).

v7 changes (Codex HOLD on v6, RUN/review/rqls10-fixedB-v6-source-codex-v1.prompt.stdout.txt, findings 5-10; v5/v6
history in code/rqls_fixedb_lm_v6.py):
 1. Protected post-GO bootstrap (finding 5): after "GO" the argument list is validated, the three output paths are
    preflighted (normalized absolute, distinct, absent, real-directory ancestors) and OUT is created exclusively; TERM is
    reconciled; only then NumPy is imported inside the protected path (an import failure gives BOOTSTRAP_FAIL with a
    stop receipt, exit 2); TERM is reconciled again after the import. Logical start boundaries: a run starts at its
    guarded entry (TERM + effective deadline checked before and after initialisation); RNG construction now happens
    inside the guarded initialisation; Problem construction is guarded (TERM, and in S the budget); S checks TERM and
    BUDGET between all numerical bundles (each matmul of the single-thread probe; each anchor step). Asynchronous
    signals are not excluded atomically; they are observed at these checks.
 2. Halt telemetry (finding 6): halt_first (first observation) and halt_final (final effective halt; a later TERMINATED
    supersedes an earlier DEADLINE) are recorded separately; the returned status equals halt_final.reason when halted.
    Per run also first_work_mono (after the first normal-equation assembly of iteration 1). Final ordering: the JSONL is
    fsynced and closed FIRST, then TERM is reconciled at that explicit boundary, then the exit code is decided
    (candidate 7 and defect 8 keep priority over later persistence or TERM events), then the stop receipt is written
    with the final record and byte counts.
 3. Persistence (finding 7): every write (JSONL records, witness, stop receipt) is a complete-write loop that rejects
    zero progress; JSONL write errors are persistence failures (exit 9); destinations are preflighted at bootstrap.
    Persistence here means exclusive creation, complete writes and fsync before close for the witness and the stop
    receipt; the JSONL is written record by record (unbuffered) and fsynced once at close; crash durability of
    unfsynced JSONL records is not claimed. The S anchor endpoints now pass through the same endpoint assessment as
    every run (assess_endpoint: candidate/defect -> witness first, then the record, then exit 7/8).
 4. Strict JSON (finding 8): residuals and Gram diagnostics are emitted only if finite (else null plus a reason flag);
    mdf has exactly three entries; allow_nan=False everywhere.
 5. Runtime identity (finding 9): the loaded numerical backend is identified (np.show_config blas/lapack names, the
    loaded dyld images matching Accelerate/vecLib and NumPy, sha256 of NumPy's two extension modules and of the
    interpreter), and the single-thread configuration is ESTABLISHED by the Accelerate BLAS threading API (macOS 15+:
    BLASSetThreading(BLAS_THREADING_SINGLE_THREADED) on the main thread, where all numerics run, then BLASGetThreading()
    must return 1). S_runtime fails if any of this cannot be established. The CPU/wall ratio (S_single_thread) is kept
    unchanged as supporting telemetry. Input files are hashed and parsed from the same bytes; digests are recorded.
 6. Naming (finding 10): "minsep_nonclose_pair" (minimum of 1 - |<q,q'>|^2 over pairs NOT below the closeness
    threshold; such a pair may still lie in one transitively merged component; for a v^2-ray endpoint it is the minimum
    over all pairs) replaces "minsep_nonmerged".
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
 Modes "full" (Phase 1) and "q1" (fixed slots S 60, N 60, C 30, KP 300, KR 150, W 150, WD 150, WS 50 s; BUDGET >= 1070).
Immediate stops (after the endpoint record): v = 10 float-verified 100-ray endpoint with minsep_nonclose_pair > 1e-6 in
ANY stage -> exit 7; LM residual < 1e-10 with full deviation >= 1e-8 (any endpoint, S anchors included) -> exit 8. Then
TERMINATED -> exit 5.
Usage: rqls_fixedb_lm_v7.py OUT.jsonl WITNESS.json STOP_RECEIPT.json BUDGET_S MODE NN NC NKR NKR10 N8 NW NWD NS
Protocol (supervisor): no computation and no NumPy import before the line "GO" on stdin (otherwise exit 6, no output).
Exit codes: 0 done, 2 exception or bootstrap failure, 3 gate failure, 4 output cap, 5 SIGTERM, 6 no GO, 7 maximal
candidate (unverified), 8 model defect, 9 persistence failure (JSONL write/close, witness or stop receipt). On every
non-zero exit after GO an exclusive stop receipt is attempted.
"""
import ctypes, hashlib, importlib, json, math, os, platform, signal, stat, sys, threading, time

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
np = None
T_NUMPY = [None]
VERSION = "rqls_fixedb_lm_v7"
LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/rqls10"
ANCHORS = (LANE + "/evidence/fixedb_anchors_v1.result.json",
           "13d6ed64d8aafde833ce7981d7ed10044b2b06975d425a5778328ea610e22b92")
PARKER = (LANE + "/evidence/parker_z7p3_classical_v1.result.json",
          "00e991d692e669411a49d45aa1623c52189346dc32acb6fb1feea1858b841c30")
ACCELERATE = "/System/Library/Frameworks/Accelerate.framework/Accelerate"
CAP = 8 * 1024 * 1024
RESERVE = 1024 * 1024
ITERS = 300
ST = {"fd": None, "nb": 0, "nr": 0, "stage": "bootstrap", "out": None, "witness": None, "stop": None, "budget": None}
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


class BootstrapFail(Exception):
    pass


def mono():
    return time.monotonic()


def write_all(fd, data):
    view = memoryview(data)
    while view:
        k = os.write(fd, view)
        if k <= 0:
            raise OSError("zero-progress write")
        view = view[k:]


def W(o, reserve_ok=False):
    b = (json.dumps(o, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
    limit = CAP if reserve_ok else CAP - RESERVE
    if ST["nb"] + len(b) > limit:
        raise CapStop("jsonl cap %d bytes reached" % limit)
    try:
        write_all(ST["fd"], b)
    except OSError as ex:
        raise PersistFail("jsonl write failed: %r" % ex)
    ST["nb"] += len(b)
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


def fnum(x):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return x if math.isfinite(x) else None


def norm_abs(p):
    return isinstance(p, str) and p.startswith("/") and os.path.abspath(p) == p


def real_dir_chain(d):
    cur = ""
    for comp in os.path.abspath(d).split("/")[1:]:
        cur = cur + "/" + comp
        try:
            st = os.lstat(cur)
        except OSError:
            return False
        if stat.S_ISLNK(st.st_mode) or not stat.S_ISDIR(st.st_mode):
            return False
    return True


def read_regular(path, max_bytes):
    st0 = os.lstat(path)
    if not stat.S_ISREG(st0.st_mode) or st0.st_size > max_bytes:
        raise OSError("not a bounded regular file: %s" % path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    try:
        st1 = os.fstat(fd)
        if (st1.st_dev, st1.st_ino, st1.st_size) != (st0.st_dev, st0.st_ino, st0.st_size):
            raise OSError("changed while opening: %s" % path)
        parts, got = [], 0
        while got < st0.st_size:
            chunk = os.read(fd, st0.st_size - got)
            if not chunk:
                raise OSError("short read: %s" % path)
            parts.append(chunk)
            got += len(chunk)
        if os.read(fd, 1):
            raise OSError("grew while read: %s" % path)
    finally:
        os.close(fd)
    return b"".join(parts)


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


def guarded_problem(B, name, in_s=False):
    (budget_check if in_s else term_check)("before Problem " + name)
    Pr = Problem(B, name)
    (budget_check if in_s else term_check)("after Problem " + name)
    return Pr


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
    """returns (U, residual norm, iterations, status, telemetry). Precedence TERMINATED > DEADLINE > other statuses;
    halt_first keeps the first halt observation, halt_final the final effective one (status == halt_final.reason)."""
    tel = {"halt_first": None, "halt_final": None, "pre_halt_status": None, "last_iter_start_mono": None,
           "first_work_mono": None}

    def halt(where, it):
        if TERM[0]:
            h = "TERMINATED"
        elif mono() > dl:
            h = "DEADLINE"
        else:
            return None
        obs = {"reason": h, "where": where, "it": it, "mono": mono(), "term_mono": TERM_MONO[0]}
        if tel["halt_first"] is None:
            tel["halt_first"] = obs
        if tel["halt_final"] is None or (h == "TERMINATED" and tel["halt_final"]["reason"] != "TERMINATED"):
            tel["halt_final"] = obs
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
        return U, math.sqrt(nf) if math.isfinite(nf) else None, 0, h, tel
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
        if tel["first_work_mono"] is None:
            tel["first_work_mono"] = mono()
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
    if tel["halt_final"] is not None:
        status = tel["halt_final"]["reason"]
    return U, (math.sqrt(nf) if math.isfinite(nf) else None), it, status, tel


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
    """(number of rays after transitive merging at 1 - |<q,q'>|^2 < 1e-7, minsep_nonclose_pair = minimum separation
    over pairs that are NOT below the closeness threshold; such a pair may still lie in one merged component)."""
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
    nonclose = sep[~close]
    return len({find(a) for a in range(n)}), (fnum(nonclose.min()) if nonclose.size else 1.0)


def evaluate(Pr, U):
    if not np.all(np.isfinite(U)):
        return {"md": None, "mdf": [None, None, None], "md_finite": False, "md_reason": "NONFINITE_U"}
    dev, Q = verify(Pr, U)
    vals = [dev["rows"], dev["columns"], dev["classes"]]
    fin = all(math.isfinite(x) for x in vals)
    out = {"md": max(vals) if fin else None, "mdf": [fnum(x) for x in vals], "md_finite": fin}
    if not fin:
        out["md_reason"] = "NONFINITE_GRAM_DEVIATION"
    if fin and out["md"] < 1e-6:
        out["rays"], out["minsep_nonclose_pair"] = ray_count(Q, Pr.v)
    return out


def u_payload(Pr, U):
    return {"U_re": U[1:].real.tolist(), "U_im": U[1:].imag.tolist(), "B_matrix": Pr.B.tolist(), "B_name": Pr.name,
            "U_convention": U_CONVENTION}


def persist_witness(rec):
    try:
        data = (json.dumps(rec, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")
        fd = os.open(ST["witness"], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
        try:
            write_all(fd, data)
            os.fsync(fd)
        finally:
            os.close(fd)
    except (OSError, ValueError) as ex:
        raise PersistFail("witness persistence failed: %r" % ex)


def assess_endpoint(Pr, U, rec, res, tag):
    """common scientific endpoint assessment (every run and the S anchor endpoints): diagnostics, flags, witness first
    for a candidate or defect, then the record, then the stop (7 or 8)."""
    rec.update(evaluate(Pr, U))
    rec["res"] = fnum(res)
    rec["res_finite"] = rec["res"] is not None
    if res is not None and rec["res"] is None:
        rec["res_reason"] = "NONFINITE_RESIDUAL"
    rec["ok"] = bool(rec["md_finite"] and rec["md"] < 1e-8)
    rec["maximal_candidate"] = bool(Pr.v == 10 and rec["ok"] and rec.get("rays") == 100 and
                                    (rec.get("minsep_nonclose_pair") or 0.0) > 1e-6)
    rec["model_defect"] = bool(rec["res_finite"] and rec["res"] < 1e-10 and rec["md_finite"] and rec["md"] >= 1e-8)
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
    return rec


def run_entry(Pr, init_fn, tag, extra, end):
    """guarded run entry; init_fn builds its RNG and start inside the guard. Returns (record, U) or (None, None) if the
    deadline passed before LM entry."""
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
    rec = {"tag": tag, "v": Pr.v, "B": Pr.name, "st": st, "it": it, "mono_entry": m_entry, "mono_init_done": m_init,
           "mono_lm_start": m_lm0, "mono_lm_end": m_lm1, "deadline_mono": dl}
    rec.update(tel)
    rec.update(extra)
    rec = assess_endpoint(Pr, U, rec, res, tag)
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
        sd = seed0 + k
        rec, U = run_entry(Pr, lambda: rand_U(Pr.v, np.random.default_rng(sd)), tag, {"seed": sd}, end)
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


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


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
    return {"fd": fnum(e_fd), "normal_eq": None if e_ne is None else fnum(e_ne), "retract_unitarity": fnum(e_un)}


def near_stage(tag, Pr, Ua, seed0, end, want_rays):
    recs, missing_small = [], 0
    for ai, amp in enumerate((1e-3, 1e-2, 0.1, 0.3)):
        for j in range(4):
            sd = seed0 + 10 * ai + j
            rec, _ = run_entry(Pr, lambda: Pr.retract(Ua, amp * np.random.default_rng(sd).standard_normal(Pr.P)), tag,
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


def dyld_images():
    lc = ctypes.CDLL("/usr/lib/libSystem.B.dylib")
    lc._dyld_image_count.restype = ctypes.c_uint32
    lc._dyld_image_count.argtypes = ()
    lc._dyld_get_image_name.restype = ctypes.c_char_p
    lc._dyld_get_image_name.argtypes = (ctypes.c_uint32,)
    out = []
    for i in range(lc._dyld_image_count()):
        name = lc._dyld_get_image_name(i)
        if name:
            out.append(name.decode("utf-8", "replace"))
    return out


def blas_threading_single(establish=True):
    """establish (once, before any numerical work) and verify single-threaded Accelerate BLAS/LAPACK on the calling
    (main) thread, macOS 15+ API; with establish=False only re-query."""
    out = {"main_thread": threading.current_thread() is threading.main_thread(), "library": ACCELERATE,
           "established_here": establish}
    try:
        acc = ctypes.CDLL(ACCELERATE)
        acc.BLASSetThreading.argtypes = (ctypes.c_uint,)
        acc.BLASSetThreading.restype = ctypes.c_int
        acc.BLASGetThreading.argtypes = ()
        acc.BLASGetThreading.restype = ctypes.c_uint
        out["before"] = int(acc.BLASGetThreading())
        if establish:
            out["set_rc"] = int(acc.BLASSetThreading(1))
        out["after"] = int(acc.BLASGetThreading())
    except (OSError, AttributeError) as ex:
        out["error"] = repr(ex)
    out["single_threaded"] = bool(out["main_thread"] and (out.get("set_rc") == 0 or not establish) and
                                  out.get("after") == 1 and "error" not in out)
    return out


def runtime_identity():
    exe = sys.executable
    real = os.path.realpath(exe)
    rec = {"executable": exe, "realpath": real, "python": sys.version, "numpy": np.__version__, "numpy_file": np.__file__,
           "mac_ver": platform.mac_ver()[0], "uname_release": os.uname().release,
           "thread_env": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
                                                          "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS")},
           "flags": {"optimize": sys.flags.optimize, "isolated": sys.flags.isolated,
                     "dont_write_bytecode": sys.flags.dont_write_bytecode}, "errors": []}
    try:
        rec["realpath_sha256"] = sha_bytes(read_regular(real, 1 << 30))
    except OSError as ex:
        rec["errors"].append("interpreter hash %r" % ex)
    try:
        cfgd = json.loads(json.dumps(np.show_config(mode="dicts"), default=str))
        bd = cfgd["Build Dependencies"]
        rec["blas_name"], rec["lapack_name"] = bd["blas"]["name"], bd["lapack"]["name"]
        rec["numpy_config"] = cfgd
    except Exception as ex:
        rec["errors"].append("numpy config %r" % ex)
    mods = {}
    for key, mod in (("multiarray_umath", "numpy._core._multiarray_umath"), ("umath_linalg", "numpy.linalg._umath_linalg")):
        try:
            p = os.path.realpath(importlib.import_module(mod).__file__)
            mods[key] = {"path": p, "sha256": sha_bytes(read_regular(p, 1 << 30))}
        except (ImportError, AttributeError, OSError, TypeError) as ex:
            rec["errors"].append("extension %s %r" % (key, ex))
    rec["extension_modules"] = mods
    try:
        imgs = dyld_images()
        rec["images_accelerate"] = sorted(x for x in imgs if "/Accelerate.framework/" in x or "/vecLib.framework/" in x)
        rec["images_numpy"] = sorted(x for x in imgs if "/numpy/" in x)
        rec["images_count"] = len(imgs)
    except (OSError, AttributeError) as ex:
        rec["errors"].append("dyld images %r" % ex)
    return rec


def single_thread_check():
    a = np.random.default_rng(5).standard_normal((1200, 1200))
    c0, w0 = time.process_time(), mono()
    for k in range(3):
        budget_check("single-thread probe matmul %d" % k)
        a = a @ a
        a /= np.max(np.abs(a))
    c1, w1 = time.process_time(), mono()
    ratio = (c1 - c0) / max(w1 - w0, 1e-9)
    return {"cpu_s": c1 - c0, "wall_s": w1 - w0, "ratio": fnum(ratio), "role": "supporting telemetry"}


def bootstrap(argv):
    if len(argv) != 14:
        raise BootstrapFail("usage: OUT WITNESS STOP_RECEIPT BUDGET_S MODE NN NC NKR NKR10 N8 NW NWD NS")
    out, wit, stop = argv[1], argv[2], argv[3]
    if norm_abs(stop):
        ST["stop"] = stop
    paths = [out, wit, stop]
    if not all(norm_abs(p) for p in paths) or len(set(paths)) != 3:
        raise BootstrapFail("OUT, WITNESS and STOP_RECEIPT must be distinct normalized absolute paths")
    for p in paths:
        try:
            os.lstat(p)
            raise BootstrapFail("destination exists: %s" % p)
        except FileNotFoundError:
            pass
        if not real_dir_chain(os.path.dirname(p)):
            raise BootstrapFail("destination ancestor is not a real directory: %s" % p)
    ST["out"], ST["witness"] = out, wit
    try:
        ST["fd"] = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
    except OSError as ex:
        raise BootstrapFail("OUT create failed: %r" % ex)
    try:
        budget = float(argv[4])
        counts = [int(a) for a in argv[6:14]]
    except ValueError as ex:
        raise BootstrapFail("bad numeric argument: %r" % ex)
    if not math.isfinite(budget) or budget <= 0 or any(c < 0 for c in counts):
        raise BootstrapFail("budget must be finite and positive, counts nonnegative")
    ST["budget"] = budget
    term_check("bootstrap before NumPy import")
    global np
    try:
        import numpy as _np
    except BaseException as ex:
        raise BootstrapFail("NumPy import failed: %r" % ex)
    np = _np
    T_NUMPY[0] = mono()
    term_check("bootstrap after NumPy import")
    return argv[5], budget, counts


def main(MODE, BUDGET, counts):
    NN, NC, NKR, NKR10, N8, NW, NWD, NS = counts
    try:
        self_sha = sha_bytes(read_regular(os.path.realpath(__file__), 1 << 24))
    except OSError as ex:
        self_sha = "UNREADABLE %r" % ex
    bt = blas_threading_single()
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
    W({"assay": VERSION, "assay_sha256": self_sha, "argv": sys.argv[1:], "mode": MODE, "budget_s": BUDGET,
       "counts": {"NN": NN, "NC": NC, "NKR": NKR, "NKR10": NKR10, "N8": N8, "NW": NW, "NWD": NWD, "NS": NS},
       "pid": os.getpid(), "pgid": os.getpgrp(), "ppid": os.getppid(), "T0_go_mono": T0,
       "numpy_imported_mono": T_NUMPY[0], "plan_origin_mono": origin, "plan_s": plan, "plan_end_mono": ends,
       "budget_end_mono": T0 + BUDGET, "blas_threading": bt, "cap": CAP, "reserve": RESERVE,
       "outputs": {"jsonl": ST["out"], "witness": ST["witness"], "stop": ST["stop"]}})
    if plan is None:
        raise GateFail("unknown MODE or budget too small for MODE %s" % MODE)
    stage_begin("S", ends["S"])
    rt = runtime_identity()
    bt2 = blas_threading_single(establish=False)
    rt_ok = (sys.flags.optimize == 0 and sys.flags.isolated == 1 and all(v == "1" for v in rt["thread_env"].values())
             and not rt["errors"] and rt.get("blas_name") == "accelerate" and rt.get("lapack_name") == "accelerate"
             and bool(rt.get("images_accelerate")) and bt["single_threaded"] and bt2["single_threaded"])
    gate("S_runtime", rt_ok, {"runtime": rt, "blas_threading": bt, "blas_threading_requery": bt2,
                              "rule": "flags optimize 0 / isolated 1; thread env all 1; NumPy backend accelerate for "
                                      "BLAS and LAPACK and Accelerate loaded; BLASSetThreading(1) == 0 and "
                                      "BLASGetThreading() == 1 on the main thread before any numerical work and again "
                                      "after identification; no identity error"})
    stc = single_thread_check()
    gate("S_single_thread", stc["ratio"] is not None and stc["ratio"] <= 1.3, stc)
    budget_check("S pins")
    raw_a, raw_p = read_regular(ANCHORS[0], 1 << 26), read_regular(PARKER[0], 1 << 26)
    dig = {"anchors": sha_bytes(raw_a), "parker": sha_bytes(raw_p)}
    pins_ok = dig["anchors"] == ANCHORS[1] and dig["parker"] == PARKER[1]
    gate("S_input_pins", pins_ok, {"digests_of_parsed_bytes": dig, "expected": {"anchors": ANCHORS[1],
                                                                                "parker": PARKER[1]}})
    AN = json.loads(raw_a.decode("utf-8"))
    PK = json.loads(raw_p.decode("utf-8"))["pairs"][0]
    budget_check("S anchors load")
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
    P7 = guarded_problem(B7, "cyclic7_huang_li", True)
    P8 = guarded_problem(B8, "xor8_zhang_cao", True)
    P10 = guarded_problem(Bpk, "parker_z7p3_pair0_B", True)
    budget_check("S jacobian rng")
    rng = np.random.default_rng(12345)
    js = {}
    for name, B, Pr in (("cyc4", cyclic(4), None), ("cyc5", cyclic(5), None), ("cyc7", None, P7), ("xor8", None, P8),
                        ("cyc10", cyclic(10), None), ("d5", dihedral5(), None)):
        if Pr is None:
            Pr = guarded_problem(B, name, True)
        budget_check("S jacobian " + name)
        js[name] = jac_selftest(Pr, rng)
    jok = all(t["fd"] is not None and t["fd"] < 1e-9 and t["retract_unitarity"] is not None and
              t["retract_unitarity"] < 1e-12 for t in js.values()) and \
        all(js[k]["normal_eq"] is not None and js[k]["normal_eq"] < 1e-12 for k in ("cyc4", "cyc5", "cyc7"))
    gate("S_jacobian", jok, {"by_B": js, "rule": "fd < 1e-9; block vs dense normal equations < 1e-12 (v <= 7); "
                                               "retraction unitarity < 1e-12"})
    an = {}
    for name, Pr, U, want in (("anchor7", P7, U7, 49), ("anchor8", P8, U8, 64), ("parker10", P10, U10, 10)):
        budget_check("S anchors residual " + name)
        rv = Pr.resid(U)
        res_inf = fnum(np.max(np.abs(rv)))
        res_2 = fnum(np.sqrt(np.sum(np.abs(rv) ** 2)))
        budget_check("S anchors endpoint " + name)
        rec = assess_endpoint(Pr, U, {"tag": "S_anchor_" + name, "v": Pr.v, "B": Pr.name, "st": "ANCHOR", "it": 0,
                                      "res_inf": res_inf}, res_2, "S_anchor_" + name)
        budget_check("S anchors mutation " + name)
        g = np.random.default_rng(777).standard_normal(Pr.P)
        Um = U.copy()
        Um[1] = Pr.retract(U, 0.3 * g)[1]
        resm = fnum(np.linalg.norm(Pr.resid(Um)))
        u0 = fnum(np.max(np.abs(U[0] - np.eye(Pr.v))))
        an[name] = {"res_inf": res_inf, "md": rec["md"], "rays": rec.get("rays"),
                    "minsep_nonclose_pair": rec.get("minsep_nonclose_pair"), "mut_res": resm, "U0_dev": u0}
        an[name]["pass"] = bool(res_inf is not None and res_inf < 1e-12 and rec["md_finite"] and rec["md"] < 1e-12 and
                                rec.get("rays") == want and resm is not None and resm >= 0.01 and u0 is not None and
                                u0 < 1e-14)
    an["parker10"]["orthogonal_mate"] = orth
    gate("S_anchors", all(a["pass"] for a in an.values()) and orth,
         {"anchors": an, "rule": "residual < 1e-12, full Gram < 1e-12, rays 49/64/10, max|U_0 - I| < 1e-14, mutation "
                                 "residual >= 0.01; Parker mate orthogonal"})
    stage_end("S")
    stage_begin("N", ends["N"])
    nsum, st0 = {}, mono()
    for di, (v, seed0) in enumerate(((4, 100000), (6, 110000))):
        sub_end = st0 + (ends["N"] - st0) * (di + 1) / 2.0
        _, _, s = random_stage("N_negative_cyc%d" % v, guarded_problem(cyclic(v), "cyc%d" % v), NN, seed0, sub_end)
        nsum[str(v)] = {"runs": s["runs"], "verified": s["verified"], "defects": s["model_defects"],
                        "min_res": s["resid_quantiles"]["min"]}
    gate("N_negative_controls", all(x["runs"] >= 1 and x["verified"] == 0 and x["defects"] == 0 for x in nsum.values()),
         {"by_v": nsum, "rule": ">= 1 run, 0 verified, 0 model defects for Cay(Z_4) and Cay(Z_6)"})
    stage_end("N")
    stage_begin("C", ends["C"])
    recs, _, s = random_stage("C_classical_only_cyc5", guarded_problem(cyclic(5), "cyc5"), NC, 120000, ends["C"])
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
        random_stage("S8_cyc8", guarded_problem(cyclic(8), "cyc8"), N8, 500000, ends["S8"])
        stage_end("S8")
    stage_begin("W", ends["W"])
    Pw = guarded_problem(cyclic(10), "cyc10")
    rw, uw, sw = random_stage("W_target_cyc10", Pw, NW, 1000000, ends["W"])
    stage_end("W")
    stage_begin("WD", ends["WD"])
    Pd = guarded_problem(dihedral5(), "d5")
    rd, ud, sd = random_stage("WD_target_d5", Pd, NWD, 1100000, ends["WD"])
    stage_end("WD")
    stage_begin("WS", ends["WS"])
    seeds = [(Pw, U, r) for r, U in zip(rw, uw) if r["ok"]] + [(Pd, U, r) for r, U in zip(rd, ud) if r["ok"]]
    ws, skipped = [], 0
    count = min(NS, 4 * len(seeds))
    for k in range(count):
        Pr, Us, pr = seeds[k % len(seeds)]
        sdk = 1200000 + k
        rec, _ = run_entry(Pr, lambda: Pr.retract(Us, 0.05 * np.random.default_rng(sdk).standard_normal(Pr.P)),
                           "WS_target_seeded", {"seed": sdk, "seed_B": Pr.name,
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


def close_out():
    """fsync and close the JSONL; returns None or an error string."""
    if ST["fd"] is None:
        return None
    fd, ST["fd"] = ST["fd"], None
    try:
        os.fsync(fd)
    except OSError as ex:
        try:
            os.close(fd)
        except OSError:
            pass
        return "fsync %r" % ex
    try:
        os.close(fd)
    except OSError as ex:
        return "close %r" % ex
    return None


def stop_receipt(status, detail, close_err):
    if ST["stop"] is None:
        sys.stderr.write("STOP_RECEIPT_PATH_UNKNOWN %s %s\n" % (status, detail[:2000]))
        return False
    try:
        data = (json.dumps({"status": status, "stage": ST["stage"], "detail": detail, "jsonl_records": ST["nr"],
                            "jsonl_bytes": ST["nb"], "jsonl_close_error": close_err, "mono": mono(),
                            "T0_go_mono": T0, "terminated": TERM[0], "term_mono": TERM_MONO[0], "assay": VERSION},
                           indent=1, allow_nan=False) + "\n").encode("utf-8")
        fd = os.open(ST["stop"], os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o644)
        try:
            write_all(fd, data)
            os.fsync(fd)
        finally:
            os.close(fd)
        return True
    except (OSError, ValueError) as ex:
        sys.stderr.write("STOP_RECEIPT_FAILED %r %s %s\n" % (ex, status, detail[:2000]))
        return False


def entry():
    code, status, detail = 0, None, ""
    try:
        mode, budget, counts = bootstrap(sys.argv)
        code = main(mode, budget, counts)
    except BootstrapFail as ex:
        code, status, detail = 2, "BOOTSTRAP_FAIL", str(ex)
    except CapStop as ex:
        code, status, detail = 4, "CAP_STOP_UNKNOWN", repr(ex)
    except CandidateStop as ex:
        code, status, detail = 7, "CANDIDATE_UNVERIFIED_STOP", str(ex)
    except ModelDefectStop as ex:
        code, status, detail = 8, "MODEL_DEFECT_STOP", str(ex)
    except PersistFail as ex:
        code, status, detail = 9, "PERSISTENCE_FAILED", str(ex)
        sys.stderr.write(detail + "\n")
    except GateFail as ex:
        code, status, detail = 3, "GATE_FAIL_STOP", repr(ex)
    except TermStop as ex:
        code, status, detail = 5, "TERMINATED_UNKNOWN", str(ex)
    except Exception as ex:
        import traceback
        tb = traceback.format_exc()[-4000:]
        try:
            if ST["fd"] is not None:
                W({"exception": repr(ex), "traceback": tb, "mono": mono()}, reserve_ok=True)
        except Exception:
            pass
        code, status, detail = 2, "EXCEPTION_STOP", tb
    close_err = close_out()
    if code == 0 and TERM[0]:
        code, status, detail = 5, "TERMINATED_UNKNOWN", "SIGTERM before the final boundary (after JSONL close)"
    if close_err is not None and code not in (7, 8):
        detail = "%s; previous status %s" % (close_err, status)
        code, status = 9, "JSONL_CLOSE_FAILED"
    if code != 0:
        if not stop_receipt(status, detail, close_err) and code not in (7, 8):
            code = 9
    return code


if __name__ == "__main__":
    sys.exit(entry())
