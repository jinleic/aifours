#!/usr/bin/env python3
"""rqls_w8_lm_v2: float LM test of the WH_p (x) C^2 orbit ansatz for B = Cay(Z_p x Z_2) (lane notes
evidence/w8-wh5-c2-orbit-ansatz-setup-v1.md and addendum 1). NOT a certificate; numeric results are UNKNOWN.

Representatives X_r (r = 00, 01, 10, 11) are p x 2 complex matrices; cell ((i1,i2),(j1,j2)) carries
q = (X^i1 Z^j1 (x) I_2) vec(X_(i2 j2)) in C^p (x) C^2 (index 2t + c). Reduced conditions (W8 setup): for every vector e of
the bases Z (computational), X (eigenbasis of the shift), T (eigenbasis of X Z^-1): every row e^dag X_r has norm^2 1/p,
and the rows of the couples Z: 00-01, 10-11; X: 00-10, 01-11; T: 00-11, 01-10 are orthogonal. LM with central-difference
Jacobian (exact for this quadratic residual up to rounding). EVERY endpoint is re-verified on the FULL 2p x 2p
configuration (all rows, columns and B-classes; Gram deviation) and its distinct rays counted (1 - |<q,q'>|^2 < 1e-7
merged); maximal candidate = maxdev < 1e-8, all 4p^2 rays, minsep > 1e-6.
Stages: P (relaxed positive control, p = 5, rows + columns only: >= 1 run must verify rows and columns),
N (negative control, p = 3, full conditions: no run may verify all lines, since no 1-RQLS(6) exists [IMPORT, as gate
C1 of the v7 assay]), W (target, p = 5, full conditions). Also recorded: reduced residual vs full verification
consistency (a reduced zero must verify; mismatches are counted and gate the target stage).
v2 (supersedes the unrun v1 draft): obeys the owned-supervisor protocol - no computation before the line "GO" arrives on
stdin (EOF or anything else: exit 6 without output); SIGTERM sets a flag honoured between runs (exit 5, records kept).
Usage: rqls_w8_lm_v2.py OUT.jsonl BUDGET_S NP NN NW   (exclusive output; exit 0 done, 3 gate failure, 2 exception)
"""
import json, math, signal, sys, time
import numpy as np
TERM = [False]
signal.signal(signal.SIGTERM, lambda s, f: TERM.__setitem__(0, True))
if sys.stdin.readline().strip() != "GO":
    sys.exit(6)
T0 = time.monotonic()
OUT, BUDGET, NP, NN, NW = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
fh = open(OUT, "x", encoding="utf-8")
def W(o):
    fh.write(json.dumps(o, separators=(",", ":")) + "\n"); fh.flush()
def over():
    return TERM[0] or time.monotonic() - T0 > BUDGET
COUPLES = {"Z": [(0, 1), (2, 3)], "X": [(0, 2), (1, 3)], "T": [(0, 3), (1, 2)]}   # rep index r = 2*a + b for x_ab


class Model:
    def __init__(self, p, bases):
        self.p = p
        z = np.exp(2j * np.pi / p)
        Xs = np.roll(np.eye(p), 1, axis=0)                     # X|t> = |t+1>
        Zc = np.diag(z ** np.arange(p))
        self.Xs, self.Zc = Xs, Zc
        def eigbasis(U):
            w, V = np.linalg.eig(U)
            Q, _ = np.linalg.qr(V)
            return Q
        self.F = {"Z": np.eye(p, dtype=complex), "X": eigbasis(Xs.astype(complex)), "T": eigbasis(Xs @ np.linalg.inv(Zc))}
        self.bases = bases
        self.npar = 4 * p * 2 * 2

    def Xr(self, TH):
        TH = np.atleast_2d(TH)
        h = TH.shape[1] // 2
        return (TH[:, :h] + 1j * TH[:, h:]).reshape(TH.shape[0], 4, self.p, 2)

    def resid_batch(self, TH):
        X = self.Xr(TH)
        out = []
        for b in self.bases:
            R = np.einsum("te,bstc->bsec", self.F[b].conj(), X)          # rows e^dag X_r: (batch, 4, p, 2)
            out.append((np.einsum("bsec,bsec->bse", R.conj(), R).real - 1.0 / self.p).reshape(X.shape[0], -1))
            for (r, s) in COUPLES[b]:
                ip = np.einsum("bec,bec->be", R[:, r], R[:, s].conj())
                out += [ip.real, ip.imag]
        return np.concatenate(out, axis=1)

    def jac(self, th, h=1e-5):
        E = np.eye(len(th)) * h
        return ((self.resid_batch(th[None] + E) - self.resid_batch(th[None] - E)) / (2 * h)).T

    def full(self, th):
        p = self.p
        X = self.Xr(th)[0]
        cells = {}
        for i1 in range(p):
            for i2 in range(2):
                for j1 in range(p):
                    for j2 in range(2):
                        Wop = np.linalg.matrix_power(self.Xs, i1) @ np.linalg.matrix_power(self.Zc, j1)
                        q = np.kron(Wop, np.eye(2)) @ X[2 * i2 + j2].reshape(-1)
                        cells[((i1, i2), (j1, j2))] = q
        return cells

    def verify(self, th, classes=True):
        p = self.p
        cells = self.full(th)
        keys = list(cells)
        lines = {}
        for (a, b) in keys:
            lines.setdefault(("row", a), []).append((a, b))
            lines.setdefault(("col", b), []).append((a, b))
            if classes:
                lines.setdefault(("cls", ((a[0] + b[0]) % p, (a[1] + b[1]) % 2)), []).append((a, b))
        md = 0.0
        for L in lines.values():
            M = np.array([cells[c] for c in L])
            md = max(md, float(np.max(np.abs(M.conj() @ M.T - np.eye(len(L))))))
        V = np.array([cells[c] / max(np.linalg.norm(cells[c]), 1e-300) for c in keys])
        O = np.abs(V.conj() @ V.T) ** 2
        n = len(keys)
        parent = list(range(n))
        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        minsep = 1.0
        for i in range(n):
            for j in range(i + 1, n):
                d = 1.0 - O[i, j]
                if d < 1e-7:
                    parent[find(i)] = find(j)
                else:
                    minsep = min(minsep, d)
        rays = len({find(i) for i in range(n)})
        return md, rays, minsep


def lm(Mo, th, iters=400, tol=1e-26):
    lam = 1e-3
    f = Mo.resid_batch(th[None])[0]
    nf = float(f @ f)
    status = "MAX_ITER"
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
                d = np.linalg.solve(A + lam * np.eye(len(th)), -g)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            f2 = Mo.resid_batch((th + d)[None])[0]
            n2 = float(f2 @ f2)
            if n2 < nf:
                th, f, nf = th + d, f2, n2
                lam = max(lam / 3, 1e-12)
                improved = True
                break
            lam *= 10
        if not improved:
            status = "STALL"
            break
    return th, math.sqrt(nf), it, status


def stage(tag, p, bases, classes, n, seed0):
    Mo = Model(p, bases)
    recs = []
    for k in range(n):
        if over():
            W({"tag": tag, "seed": seed0 + k, "status": "SKIPPED_TIME"})
            continue
        rng = np.random.default_rng(seed0 + k)
        th0 = rng.standard_normal(Mo.npar) / math.sqrt(4 * p)
        t0 = time.monotonic()
        th, res, it, st = lm(Mo, th0)
        md, rays, ms = Mo.verify(th, classes)
        rec = {"tag": tag, "p": p, "seed": seed0 + k, "status": st, "iters": it, "resid": res, "maxdev": md, "rays": rays,
               "minsep": ms, "verified": bool(md < 1e-8), "secs": round(time.monotonic() - t0, 3),
               "maximal_candidate": bool(classes and md < 1e-8 and rays == 4 * p * p and ms > 1e-6)}
        if rec["maximal_candidate"] or (res < 1e-10 and md >= 1e-8):
            rec["theta"] = np.round(th, 15).tolist()
        W(rec)
        recs.append(rec)
    ver = [r for r in recs if r["verified"]]
    mism = [r for r in recs if r["resid"] < 1e-10 and not r["verified"]]
    summ = {"summary": tag, "runs": len(recs), "verified": len(ver), "rays": {str(x): sum(1 for r in ver if r["rays"] == x) for x in sorted({r["rays"] for r in ver})},
            "maximal_candidates": sum(r["maximal_candidate"] for r in recs), "reduced_zero_not_verified": len(mism),
            "status": {s: sum(1 for r in recs if r["status"] == s) for s in ("CONVERGED", "STALL", "MAX_ITER")}, "elapsed_s": round(time.monotonic() - T0, 2)}
    W(summ)
    return summ


def main():
    W({"assay": "rqls_w8_lm_v2", "numpy": np.__version__, "python": sys.version, "budget_s": BUDGET, "argv": sys.argv[1:]})
    sP = stage("P_relaxed_rows_cols_p5", 5, ["Z", "X"], False, NP, 1000)
    okP = sP["verified"] >= 1 and sP["reduced_zero_not_verified"] == 0
    W({"GATE": "P_relaxed_positive", "pass": okP})
    if not okP:
        return 3
    sN = stage("N_negative_p3", 3, ["Z", "X", "T"], True, NN, 2000)
    okN = sN["verified"] == 0 and sN["runs"] >= 1
    W({"GATE": "N_negative_p3", "pass": okN, "reduced_zero_not_verified": sN["reduced_zero_not_verified"]})
    if not okN:
        return 3
    sW = stage("W_target_p5", 5, ["Z", "X", "T"], True, NW, 3000)
    W({"end": True, "elapsed_s": round(time.monotonic() - T0, 2), "target_reduced_zero_not_verified": sW["reduced_zero_not_verified"]})
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as ex:
        W({"error": repr(ex)})
        code = 2
    if code == 0 and TERM[0]:
        W({"terminated": True})
        code = 5
    fh.close()
    sys.exit(code)
