#!/usr/bin/env python3
"""rqls_wh10_lm_v2: float Levenberg-Marquardt assay of the WH_d single-orbit ansatz (lane notes
evidence/wh10-reduction-v1.md, sha256 7e77051c33431921c6d50ddcd8bd2f1c1ba961a0956cb2678f529d0290c0cac8, and
evidence/structure-and-wh10-ansatz-proposal-v1.md). NOT a certificate; any target miss is a scoped UNKNOWN.

Ansatz (H_d): B = Cay(Z_d), B(i,j) = i + j; cell (i,j) carries q_ij = X^i Z^j x for ONE unit vector x in C^d
(X e_t = e_(t+1), Z e_t = omega^t e_t). Reduced conditions (note Lemma W1): x flat in the computational basis (rows), the
Fourier basis (columns) and the eigenbasis f_k(t) = lam_k^-t omega^(-t(t-1)/2)/sqrt d of U = X Z^-1 (B-classes),
lam_k = exp(-i pi (d-1)/d) omega^k. Residual over the used families: r = |V^* x|^2 - 1/d (d reals per family), theta =
(Re x, Im x); exact Jacobian (r is a sum of squares of linear forms). LM damping schedule as rqls_w8_lm_v2.
EVERY endpoint is verified on the FULL d x d configuration: Gram deviation of all d rows, d columns and d B-classes
(3d lines; per family recorded); "verified" = max deviation over the USED families < 1e-8. For deviation < 1e-6 the
distinct rays are counted (pairs with 1 - |<q,q'>|^2 < 1e-7 merged; minsep recorded) and, for d = 10, the CRT Bloch
components of M^* M (M = [b_0 b_1], b_j(s) = x_t for t = j mod 2, t = s mod 5; rows <-> z, columns <-> x, classes <-> y).
Maximal candidate (full conditions only) = deviation < 1e-8, d^2 rays, minsep > 1e-6: x is written at full precision.
Model-defect screen (parent rule): reduced residual < 1e-10 with deviation >= 1e-8 is a model defect REGARDLESS of LM
status (x written); counted per stage; any defect before the target is a gate failure.

Stages (deterministic seeds; wall-clock stage ends inside BUDGET_S; actual counts are recorded, unfinished runs are
written as SKIPPED_TIME):
 B   basis self-test, d in {2, 5, 6, 7, 9, 10}: the explicit Fourier and f_k bases are orthonormal and diagonalise X and
     U (deviation < 1e-12).
 A   exact anchors (float check). d = 5, 7, 9: x_t = omega^(a t^2 + b t)/sqrt d for every valid a (gcd(2a,d) = gcd(2a+1,d)
     = 1) and b in {0, 1}: residual < 1e-12, full deviation < 1e-12, rays = d; mutation x_0 -> omega x_0: residual >= 0.01
     and deviation >= 0.01. d = 10 relaxed anchors: Chu zeta_20^(t^2) (rows, columns), constant (rows, classes), e_0
     (columns, classes): residual on the used families < 1e-12, those families verify (< 1e-12), full residual >= 0.01,
     Bloch components on the paired axes < 1e-12 and on the free axis > 0.5.
 N   negative controls, full conditions, d = 2 and d = 6 (no solution: exact theorems W7 of the note): NN random starts
     each; gate: >= 1 run, 0 verified, 0 model defects.
 KP  near-anchor recovery, d = 5, 7, 9 (a = smallest valid, b = 0): theta_anchor + amp N(0,1), amp in {1e-3, 1e-2, 0.1,
     0.5}, 4 seeds each; gate: every amp <= 1e-2 run at d = 5, 7 verified (Jacobian kernel = phase only, design check
     evidence/wh10_design_check_v1.result.json); d = 9 recorded only (3-dimensional Jacobian kernel at its anchor);
     0 model defects at every d and amp.
 KR  random recovery of KNOWN solution classes, d = 5, 7, 9: NKR random starts each; gate: >= 1 run per d and 0 model
     defects; verified counts and ray-count histograms recorded, not gated. These rates are NOT detection power for d = 10.
 P   relaxed positives at d = 10 (rows+columns, rows+classes, columns+classes): NP random starts each; gate: >= 1
     verified per variant, 0 model defects, every verified solution has |Bloch| < 1e-6 on both paired axes.
 W   TARGET, d = 10, full conditions: NW random starts.
 WS  TARGET, seeded: up to 512 starts at verified P solutions (+ 0.05 N(0,1)), full conditions.
Usage: rqls_wh10_lm_v2.py OUT.jsonl BUDGET_S NN NKR NP NW STOP_RECEIPT
Protocol (owned_supervisor_v2): no computation before the line "GO" on stdin (otherwise exit 6, no output); SIGTERM sets
a flag honoured between runs. Exit codes: 0 done, 2 exception, 3 gate failure, 4 output cap, 5 SIGTERM, 6 no GO. On every
non-zero exit after GO a separate exclusive STOP_RECEIPT is written.
"""
import json, math, signal, sys, time
import numpy as np

TERM = [False]
signal.signal(signal.SIGTERM, lambda s, f: TERM.__setitem__(0, True))
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic()
OUT, BUDGET = sys.argv[1], float(sys.argv[2])
NN, NKR, NP, NW = (int(v) for v in sys.argv[3:7])
STOP_RECEIPT = sys.argv[7]
CAP = 8 * 1024 * 1024
fh = open(OUT, "x", encoding="utf-8")
NB = [0, 0]
STAGE = ["init"]
FAMS = ("rows", "columns", "classes")
AXIS = {"rows": "z", "columns": "x", "classes": "y"}
VALID = {5: [1, 3, 4], 7: [1, 2, 4, 5, 6], 9: [2, 5, 8]}


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


class Model:
    def __init__(self, d, fams):
        self.d, self.fams = d, tuple(fams)
        t = np.arange(d)
        self.om = np.exp(2j * np.pi / d)
        self.lam = np.exp(-1j * np.pi * (d - 1) / d) * self.om ** t
        tri = (t * (t - 1)) // 2
        Fk = (self.lam[None, :] ** (-t[:, None])) * (self.om ** (-tri))[:, None] / math.sqrt(d)
        Four = self.om ** np.outer(t, t) / math.sqrt(d)
        self.basis = {"rows": np.eye(d, dtype=complex), "columns": Four, "classes": Fk}
        ra, rb = [], []
        for f in self.fams:
            VH = self.basis[f].conj().T
            ra.append(np.hstack([VH.real, -VH.imag]))
            rb.append(np.hstack([VH.imag, VH.real]))
        self.A, self.B = np.vstack(ra), np.vstack(rb)
        self.npar = 2 * d

    def resid(self, th):
        a, b = self.A @ th, self.B @ th
        return a * a + b * b - 1.0 / self.d

    def jac(self, th):
        a, b = self.A @ th, self.B @ th
        return 2.0 * (a[:, None] * self.A + b[:, None] * self.B)


def th_of(x):
    return np.concatenate([x.real, x.imag])


def x_of(th, d):
    return th[:d] + 1j * th[d:]


def lm(Mo, th, iters=300, tol=1e-26):
    lam = 1e-3
    f = Mo.resid(th)
    nf = float(f @ f)
    status, it = "MAX_ITER", 0
    for it in range(1, iters + 1):
        if nf < tol:
            status = "CONVERGED"
            break
        J = Mo.jac(th)
        g = J.T @ f
        A = J.T @ J
        improved = False
        for _ in range(12):
            try:
                step = np.linalg.solve(A + lam * np.eye(len(th)), -g)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            f2 = Mo.resid(th + step)
            n2 = float(f2 @ f2)
            if n2 < nf:
                th, f, nf = th + step, f2, n2
                lam = max(lam / 3, 1e-12)
                improved = True
                break
            lam *= 10
        if not improved:
            status = "STALL"
            break
    return th, math.sqrt(nf), it, status


LINES = {}


def line_sets(d):
    if d not in LINES:
        LINES[d] = {"rows": [[(i, j) for j in range(d)] for i in range(d)],
                    "columns": [[(i, j) for i in range(d)] for j in range(d)],
                    "classes": [[(i, (s - i) % d) for i in range(d)] for s in range(d)]}
    return LINES[d]


def configuration(d, x):
    x = x / np.linalg.norm(x)
    t = np.arange(d)
    om = np.exp(2j * np.pi / d)
    Q = np.empty((d, d, d), dtype=complex)
    for j in range(d):
        zx = om ** (j * t) * x
        for i in range(d):
            Q[i, j] = np.roll(zx, i)
    return Q


def verify(d, x):
    Q = configuration(d, x)
    dev = {}
    for f, lines in line_sets(d).items():
        m = 0.0
        for L in lines:
            M = np.array([Q[c] for c in L])
            m = max(m, float(np.max(np.abs(M.conj() @ M.T - np.eye(d)))))
        dev[f] = m
    return dev, Q


def ray_count(Q, d):
    V = Q.reshape(d * d, d)
    V = V / np.linalg.norm(V, axis=1, keepdims=True)
    O = np.abs(V.conj() @ V.T) ** 2
    n = d * d
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


def bloch10(x):
    x = x / np.linalg.norm(x)
    M = np.zeros((5, 2), dtype=complex)
    for t in range(10):
        M[t % 5, t % 2] = x[t]
    rho = M.conj().T @ M
    return {"z": float(abs((rho[0, 0] - rho[1, 1]).real)), "x": float(abs(2.0 * rho[0, 1].real)),
            "y": float(abs(2.0 * rho[0, 1].imag)), "tr": float(rho[0, 0].real + rho[1, 1].real)}


def evaluate(d, fams, x, res):
    nx = float(np.linalg.norm(x))
    if not np.isfinite(nx) or nx < 1e-9:
        return {"md": 1e9, "mdf": None}, None
    dev, Q = verify(d, x)
    md = max(dev[f] for f in fams)
    out = {"md": md, "mdf": [dev["rows"], dev["columns"], dev["classes"]]}
    if md < 1e-6:
        nr, ms = ray_count(Q, d)
        out["rays"], out["minsep"] = nr, ms
        if d == 10:
            out["bloch"] = bloch10(x)
    return out, Q


def run_one(Mo, th0, tag, extra, iters=300):
    t0 = time.monotonic()
    th, res, it, st = lm(Mo, th0, iters)
    x = x_of(th, Mo.d)
    ev, Q = evaluate(Mo.d, Mo.fams, x, res)
    rec = {"tag": tag, "d": Mo.d, "fams": list(Mo.fams), "st": st, "it": it, "res": res}
    rec.update(ev)
    rec.update(extra)
    rec["v"] = bool(rec["md"] < 1e-8)
    rec["maximal_candidate"] = bool(Mo.fams == FAMS and rec["v"] and rec.get("rays") == Mo.d * Mo.d
                                    and rec.get("minsep", 0.0) > 1e-6)
    rec["model_defect"] = bool(res < 1e-10 and rec["md"] >= 1e-8)
    if rec["maximal_candidate"] or rec["model_defect"]:
        rec["x_re"], rec["x_im"] = x.real.tolist(), x.imag.tolist()
        rec["B"] = "Cay(Z_%d): B(i,j) = i + j" % Mo.d
    rec["s"] = round(time.monotonic() - t0, 4)
    W(rec)
    if rec["model_defect"]:
        raise ModelDefectStop("model defect at " + tag)
    if Mo.d == 10 and Mo.fams == FAMS and rec["maximal_candidate"]:
        raise CandidateStop("unverified 100-ray candidate at " + tag)
    return rec, x


def summarize(tag, recs, skipped):
    ran = [r for r in recs]
    ver = [r for r in ran if r["v"]]
    rh = {}
    for r in ver:
        rh[str(r.get("rays"))] = rh.get(str(r.get("rays")), 0) + 1
    st = {}
    for r in ran:
        st[r["st"]] = st.get(r["st"], 0) + 1
    res = sorted(r["res"] for r in ran)

    def q(f):
        return res[min(len(res) - 1, int(f * (len(res) - 1)))] if res else None
    s = {"summary": tag, "runs": len(ran), "skipped_time": skipped, "verified": len(ver), "verified_rays": rh,
         "status": st, "model_defects": sum(r["model_defect"] for r in ran),
         "maximal_candidates": sum(r["maximal_candidate"] for r in ran),
         "resid_quantiles": {"min": q(0.0), "q01": q(0.01), "q10": q(0.1), "median": q(0.5), "max": q(1.0)},
         "n_resid_lt": {"1e-2": sum(1 for v in res if v < 1e-2), "1e-4": sum(1 for v in res if v < 1e-4),
                        "1e-6": sum(1 for v in res if v < 1e-6)},
         "elapsed_s": round(elapsed(), 2)}
    W(s)
    return s


def random_stage(tag, d, fams, n, seed0, end):
    Mo = Model(d, fams)
    recs, xs, skipped = [], [], 0
    for k in range(n):
        if over(end):
            skipped += 1
            continue
        rng = np.random.default_rng(seed0 + k)
        th0 = rng.standard_normal(Mo.npar)
        th0 /= np.linalg.norm(th0)
        rec, x = run_one(Mo, th0, tag, {"seed": seed0 + k})
        recs.append(rec)
        xs.append(x)
    if skipped:
        W({"tag": tag, "status": "SKIPPED_TIME", "count": skipped})
    return recs, xs, summarize(tag, recs, skipped)


def anchor_x(d, a, b):
    t = np.arange(d)
    return np.exp(2j * np.pi * (a * t * t + b * t) / d) / math.sqrt(d)


def main():
    W({"assay": "rqls_wh10_lm_v2", "numpy": np.__version__, "python": sys.version, "budget_s": BUDGET, "argv": sys.argv[1:],
       "flags": {"optimize": sys.flags.optimize, "isolated": sys.flags.isolated}})
    if sys.flags.optimize:
        raise GateFail("python optimize flag set")
    plan = [("A", 30), ("N", 90), ("KP", 60), ("KR", 180), ("P", 180), ("W", BUDGET - 30 - 90 - 60 - 180 - 180 - 150 - 20),
            ("WS", 150)]
    ends, acc, t0 = {}, 0.0, time.monotonic()
    for tag, b in plan:
        acc += b
        ends[tag] = t0 + acc
    # B: basis self-test
    STAGE[0] = "B"
    bdev = {}
    for d in (2, 5, 6, 7, 9, 10):
        Mo = Model(d, FAMS)
        Xs = np.roll(np.eye(d), 1, axis=0)
        U = Xs @ np.diag(Mo.om ** (-np.arange(d)))
        Fk, Fo = Mo.basis["classes"], Mo.basis["columns"]
        bdev[str(d)] = max(float(np.max(np.abs(Fk.conj().T @ Fk - np.eye(d)))),
                           float(np.max(np.abs(U @ Fk - Fk * Mo.lam[None, :]))),
                           float(np.max(np.abs(Fo.conj().T @ Fo - np.eye(d)))),
                           float(np.max(np.abs(Xs @ Fo - Fo * (Mo.om ** (-np.arange(d)))[None, :]))))
    gate("B_basis_selftest", max(bdev.values()) < 1e-12, {"max_dev_by_d": bdev, "rule": "all < 1e-12"})
    # A: anchors
    STAGE[0] = "A"
    arecs, ok = [], True
    for d in (5, 7, 9):
        Mo = Model(d, FAMS)
        for a in VALID[d]:
            for b in (0, 1):
                x = anchor_x(d, a, b)
                res = float(np.linalg.norm(Mo.resid(th_of(x))))
                ev, Q = evaluate(d, FAMS, x, res)
                xm = x.copy()
                xm[0] *= Mo.om
                resm = float(np.linalg.norm(Mo.resid(th_of(xm))))
                devm, _ = verify(d, xm)
                r = {"d": d, "a": a, "b": b, "res": res, "md": ev["md"], "rays": ev.get("rays"),
                     "mut_res": resm, "mut_md": max(devm.values())}
                r["pass"] = bool(res < 1e-12 and ev["md"] < 1e-12 and ev.get("rays") == d and resm >= 0.01
                                 and max(devm.values()) >= 0.01)
                ok = ok and r["pass"]
                arecs.append(r)
    t10 = np.arange(10)
    rel = (("chu", np.exp(2j * np.pi * t10 * t10 / 20) / math.sqrt(10), ("rows", "columns"), "y"),
           ("constant", np.ones(10, dtype=complex) / math.sqrt(10), ("rows", "classes"), "x"),
           ("e0", np.eye(10, dtype=complex)[0], ("columns", "classes"), "z"))
    for name, x, fams, free in rel:
        Mo, Mf = Model(10, fams), Model(10, FAMS)
        res = float(np.linalg.norm(Mo.resid(th_of(x))))
        resf = float(np.linalg.norm(Mf.resid(th_of(x))))
        dev, _ = verify(10, x)
        bl = bloch10(x)
        paired = [AXIS[f] for f in fams]
        r = {"d": 10, "anchor": name, "fams": list(fams), "res": res, "full_res": resf, "dev": dev, "bloch": bl}
        r["pass"] = bool(res < 1e-12 and max(dev[f] for f in fams) < 1e-12 and resf >= 0.01
                         and all(bl[a] < 1e-12 for a in paired) and bl[free] > 0.5)
        ok = ok and r["pass"]
        arecs.append(r)
    W({"tag": "A_anchors", "records": arecs})
    gate("A_anchors", ok, {"n": len(arecs), "rule": "odd-d Gauss anchors exact to 1e-12 with d rays and failing mutation; "
                                                     "d=10 relaxed anchors verify their families, fail the full problem, "
                                                     "Bloch zero exactly on the paired axes"})
    # N: negative controls
    STAGE[0] = "N"
    nsum, st0 = {}, time.monotonic()
    for di, (d, seed0) in enumerate(((2, 100000), (6, 110000))):
        sub_end = st0 + (ends["N"] - st0) * (di + 1) / 2.0
        recs, _, s = random_stage("N_negative_d%d" % d, d, FAMS, NN, seed0, sub_end)
        nsum[str(d)] = {"runs": s["runs"], "verified": s["verified"], "defects": s["model_defects"],
                        "min_res": s["resid_quantiles"]["min"]}
    gate("N_negative_controls", all(v["runs"] >= 1 and v["verified"] == 0 and v["defects"] == 0 for v in nsum.values()),
         {"by_d": nsum, "rule": ">= 1 run, 0 verified, 0 model defects for d = 2 and d = 6"})
    # KP: near-anchor recovery
    STAGE[0] = "KP"
    kp, kp_ok = [], True
    for d in (5, 7, 9):
        Mo = Model(d, FAMS)
        th_a = th_of(anchor_x(d, VALID[d][0], 0))
        for ai, amp in enumerate((1e-3, 1e-2, 0.1, 0.5)):
            for j in range(4):
                if over(ends["KP"]):
                    kp_ok = False
                    W({"tag": "KP", "d": d, "amp": amp, "seed": j, "status": "SKIPPED_TIME"})
                    continue
                rng = np.random.default_rng(400000 + 1000 * d + 10 * ai + j)
                rec, _ = run_one(Mo, th_a + amp * rng.standard_normal(Mo.npar), "KP_near_anchor",
                                 {"amp": amp, "seed": 400000 + 1000 * d + 10 * ai + j, "a": VALID[d][0]})
                kp.append(rec)
    small = [r for r in kp if r["amp"] <= 1e-2 and r["d"] in (5, 7)]
    by = {}
    for r in kp:
        k = "%d/%g" % (r["d"], r["amp"])
        by.setdefault(k, [0, 0])
        by[k][0] += 1
        by[k][1] += int(r["v"])
    W({"summary": "KP_near_anchor", "by_d_amp_runs_verified": by,
       "verified_rays": sorted({r.get("rays") for r in kp if r["v"]}), "elapsed_s": round(elapsed(), 2)})
    gate("KP_near_anchor", kp_ok and len(small) == 16 and all(r["v"] for r in small) and not any(r["model_defect"] for r in kp),
         {"small_amp_runs_d5_d7": len(small), "small_amp_verified_d5_d7": sum(r["v"] for r in small),
          "d9_small_amp_verified": sum(1 for r in kp if r["d"] == 9 and r["amp"] <= 1e-2 and r["v"]),
          "rule": "all 16 runs with amp <= 1e-2 at d = 5, 7 (nondegenerate anchors) verified; d = 9 recorded, not gated "
                  "(its anchor has a 3-dimensional Jacobian kernel, design check); 0 model defects at every d and amp"})
    # KR: random recovery of known classes
    STAGE[0] = "KR"
    krs, st0 = {}, time.monotonic()
    for di, d in enumerate((5, 7, 9)):
        sub_end = st0 + (ends["KR"] - st0) * (di + 1) / 3.0
        recs, _, s = random_stage("KR_random_d%d" % d, d, FAMS, NKR, 200000 + 10000 * d, sub_end)
        krs[str(d)] = {"runs": s["runs"], "verified": s["verified"], "rays": s["verified_rays"], "defects": s["model_defects"]}
    gate("KR_known_class_recovery", all(v["runs"] >= 1 and v["defects"] == 0 for v in krs.values()),
         {"by_d": krs, "rule": ">= 1 run per d and 0 model defects; verified counts and ray histograms recorded, not gated; "
                               "rates are recovery of known classes, NOT d = 10 detection power"})
    # P: relaxed positives at d = 10
    STAGE[0] = "P"
    psum, seeds_x, p_ok, st0 = {}, [], True, time.monotonic()
    for vi, fams in enumerate((("rows", "columns"), ("rows", "classes"), ("columns", "classes"))):
        sub_end = st0 + (ends["P"] - st0) * (vi + 1) / 3.0
        recs, xs, s = random_stage("P_relaxed_" + "_".join(fams), 10, fams, NP, 300000 + 10000 * vi, sub_end)
        paired = [AXIS[f] for f in fams]
        viol = 0.0
        for r, x in zip(recs, xs):
            if r["v"]:
                bl = r.get("bloch") or bloch10(x)
                viol = max(viol, max(bl[a] for a in paired))
                seeds_x.append(x)
        psum["+".join(fams)] = {"runs": s["runs"], "verified": s["verified"], "defects": s["model_defects"],
                                "max_bloch_on_paired_axes": viol}
        p_ok = p_ok and s["verified"] >= 1 and s["model_defects"] == 0 and viol < 1e-6
    gate("P_relaxed_positive_d10", p_ok, {"by_variant": psum, "rule": ">= 1 verified per variant, 0 model defects, "
                                                                      "Bloch < 1e-6 on both paired axes"})
    # W: target
    STAGE[0] = "W"
    _, _, sw = random_stage("W_target_d10", 10, FAMS, NW, 1000000, ends["W"])
    # WS: seeded target
    STAGE[0] = "WS"
    Mo = Model(10, FAMS)
    ws, skipped = [], 0
    for k, x in enumerate(seeds_x[:512]):
        if over(ends["WS"]):
            skipped += 1
            continue
        rng = np.random.default_rng(2000000 + k)
        rec, _ = run_one(Mo, th_of(x) + 0.05 * rng.standard_normal(20), "WS_target_seeded_d10", {"seed": 2000000 + k})
        ws.append(rec)
    if skipped:
        W({"tag": "WS_target_seeded_d10", "status": "SKIPPED_TIME", "count": skipped})
    sws = summarize("WS_target_seeded_d10", ws, skipped)
    W({"end": True, "terminated": TERM[0], "target_random": {k: sw[k] for k in ("runs", "verified", "maximal_candidates",
                                                                              "model_defects", "skipped_time")},
       "target_seeded": {k: sws[k] for k in ("runs", "verified", "maximal_candidates", "model_defects", "skipped_time")},
       "records": NB[1], "bytes": NB[0], "elapsed_s": round(elapsed(), 2)})
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
