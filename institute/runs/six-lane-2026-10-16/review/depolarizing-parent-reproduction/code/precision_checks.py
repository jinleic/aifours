#!/usr/bin/env python3
"""Non-rigorous floating-point error estimates for the M=2000 evaluation.

  P1. B_m windows (float64 positive recursion) vs mpmath closed form, sampled entries,
      m in {1120, 1466, 1700, 2000}, full production window rows<=440, cols<=300.
  P2. Coefficients g_l(y) (S_N) and h_r(w;x) (partial trace): float64 hi/lo log-factorial
      evaluation vs mpmath, random samples at M=2000.
  P3. Whole-block float64 pipeline vs an independent straightforward mpmath (40 digits)
      implementation of the same formulas (closed-form B_m, explicit loops, mp.eigsy),
      at the true size M=2000 for blocks r in {200, 267, 340}, on a reduced problem
      (witness truncated to x<=XT and renormalised, output window Dout_t).
  P4. Eigen-solver sensitivity on production blocks (Dout=440, full witness):
      eigvalsh vs SVD vs eigvalsh after a random orthogonal similarity.
Writes ../evidence/precision_checks.json
"""
import json
import math
import os
import sys
import time

import mpmath
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sym_depol import (LogFact, BWindows, apply_SN, assemble, partial_trace_factor,  # noqa: E402
                       entropy_nats, coherent_information)
from run_witness import load_witness  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../evidence/precision_checks.json")
M = 2000
P = mpmath.mpf(1) / 5


def mp_setup(dps=40):
    mpmath.mp.dps = dps
    eta = 1 - 4 * P / 3
    f = (1 - eta) / 2
    fac = [mpmath.mpf(1)]
    for n in range(1, M + 3):
        fac.append(fac[-1] * n)
    return eta, f, fac


def mp_B(m, kp, k, f, fac):
    if k > m or kp > m or k < 0 or kp < 0:
        return mpmath.mpf(0)
    rho = f / (1 - f)
    s = mpmath.mpf(0)
    for j in range(max(0, k + kp - m), min(k, kp) + 1):
        s += rho ** (k + kp - 2 * j) / (fac[j] * fac[k - j] * fac[kp - j] * fac[m - k - kp + j])
    return (1 - f) ** m * mpmath.sqrt(fac[k] * fac[m - k] * fac[kp] * fac[m - kp]) * s


def mp_binom(n, k, fac):
    if k < 0 or k > n:
        return mpmath.mpf(0)
    return fac[n] / (fac[k] * fac[n - k])


def P1(rng):
    eta, f, fac = mp_setup()
    want = [1120, 1466, 1700, 2000]
    Bw = BWindows(float(f), 440, 300)
    got = {}
    for m in want:
        got[m] = Bw.get(m).copy()
        Bw.set_keep_from(m + 1)
    rows = []
    for m in want:
        samples = [(0, 0), (440, 300), (440, 0), (0, 300), (200, 150), (300, 300), (30, 20)]
        samples += [(int(a), int(b)) for a, b in zip(rng.integers(0, 441, 40), rng.integers(0, 301, 40))]
        for kp, k in samples:
            ref = mp_B(m, kp, k, f, fac)
            val = got[m][kp, k]
            rel = float(abs(mpmath.mpf(val) - ref) / ref) if ref != 0 else (0.0 if val == 0 else float('inf'))
            rows.append(dict(m=m, kp=kp, k=k, ref=float(ref), val=float(val), rel=rel,
                             log10ref=float(mpmath.log10(ref)) if ref > 0 else None))
    ok = [r for r in rows if r["log10ref"] is not None and r["log10ref"] > -300]
    return dict(rows=rows, max_rel_error=max(r["rel"] for r in ok), n=len(ok))


def P2(rng):
    eta, f, fac = mp_setup()
    lf = LogFact(M + 2)
    out_g, out_h = [], []
    for _ in range(300):
        r = int(rng.integers(120, 441))
        N = M - 2 * r
        Q = int(rng.integers(0, 301))
        l = int(rng.integers(0, 300))
        y = int(rng.integers(l, l + 441))
        if N - y - Q - l < 0:
            continue
        ref = mpmath.sqrt(mp_binom(y + Q, l + Q, fac) * mp_binom(N - y - Q, l, fac) / mp_binom(N, y, fac))
        val = lf.exp_half([y + Q, N - y - Q, y, N - y], [l + Q, y - l, l, N - y - Q - l, N])
        if ref > 0:
            out_g.append(float(abs(mpmath.mpf(float(val)) - ref) / ref))
    for _ in range(300):
        r = int(rng.integers(120, 441))
        N = M - 2 * r
        x = int(rng.integers(0, 301))
        w = int(rng.integers(0, min(x, 2 * r) + 1))
        ref = mpmath.sqrt(mp_binom(2 * r, w, fac) * mp_binom(N, x - w, fac) / mp_binom(M, x, fac))
        val = lf.exp_half([2 * r, N, x, M - x], [w, 2 * r - w, x - w, N - x + w, M])
        if ref > 0:
            out_h.append(float(abs(mpmath.mpf(float(val)) - ref) / ref))
    return dict(g_max_rel=max(out_g), g_n=len(out_g), h_max_rel=max(out_h), h_n=len(out_h))


def mp_block(phis_mp, q, r, XT, Dt, dps=40):
    """Straightforward mpmath evaluation of S(rho_r^B) - S(rho_r^RB) for block r."""
    eta, f, fac = mp_setup(dps)
    N = M - 2 * r
    hh = {}

    def h(w, x):
        return mpmath.sqrt(mp_binom(2 * r, w, fac) * mp_binom(N, x - w, fac) / mp_binom(M, x, fac))
    # partial traces Z_ij[x',y'] (real amplitudes)
    Z = {}
    for (i, j) in [(0, 0), (1, 1), (0, 1)]:
        Zm = [[mpmath.mpf(0)] * (XT + 1) for _ in range(XT + 1)]
        for xp in range(XT + 1):
            for yp in range(XT + 1):
                s = mpmath.mpf(0)
                for w in range(0, min(2 * r, XT) + 1):
                    x, y = xp + w, yp + w
                    if x > XT or y > XT:
                        break
                    a, b = phis_mp[i][x], phis_mp[j][y]
                    if a == 0 or b == 0:
                        continue
                    key1, key2 = (w, x), (w, y)
                    if key1 not in hh:
                        hh[key1] = h(w, x)
                    if key2 not in hh:
                        hh[key2] = h(w, y)
                    s += hh[key1] * hh[key2] * a * b
                Zm[xp][yp] = s
        Z[(i, j)] = Zm
    Bc = {}

    def B(m, kp, k):
        key = (m, kp, k)
        if key not in Bc:
            Bc[key] = mp_B(m, kp, k, f, fac)
        return Bc[key]

    gc = {}
    etap = [eta ** n for n in range(4 * XT + 4 * Dt + 4)]

    def g(l, y, Q):
        key = (l, y, Q)
        if key in gc:
            return gc[key]
        if N - y - Q - l < 0 or y < l:
            v = mpmath.mpf(0)
        else:
            v = mpmath.sqrt(mp_binom(y + Q, l + Q, fac) * mp_binom(N - y - Q, l, fac) / mp_binom(N, y, fac))
        gc[key] = v
        return v
    Y = {}
    for key, Zm in Z.items():
        Ym = mpmath.matrix(Dt + 1, Dt + 1)
        for Q in range(-XT, XT + 1):
            for b in range(max(0, -Q), Dt + 1 - max(Q, 0)):
                a = b + Q
                s = mpmath.mpf(0)
                if Q >= 0:
                    for l in range(0, b + 1):
                        gb = g(l, b, Q)
                        if gb == 0:
                            continue
                        for yv in range(l, XT - Q + 1):
                            zv = Zm[yv + Q][yv]
                            if zv == 0:
                                continue
                            s += etap[2 * l + Q] * gb * g(l, yv, Q) * B(N - 2 * l - Q, b - l, yv - l) * zv
                else:   # use S(Z)[a,b] = S(Z^T)[b,a] (real case)
                    Qp = -Q
                    for l in range(0, a + 1):
                        ga = g(l, a, Qp)
                        if ga == 0:
                            continue
                        for yv in range(l, XT - Qp + 1):
                            zv = Zm[yv][yv + Qp]
                            if zv == 0:
                                continue
                            s += etap[2 * l + Qp] * ga * g(l, yv, Qp) * B(N - 2 * l - Qp, a - l, yv - l) * zv
                Ym[a, b] = s
        Y[key] = Ym
    YB = q[0] * Y[(0, 0)] + q[1] * Y[(1, 1)]
    n = Dt + 1
    YRB = mpmath.matrix(2 * n, 2 * n)
    s12 = mpmath.sqrt(q[0] * q[1])
    for a in range(n):
        for b in range(n):
            YRB[a, b] = q[0] * Y[(0, 0)][a, b]
            YRB[n + a, n + b] = q[1] * Y[(1, 1)][a, b]
            YRB[a, n + b] = s12 * Y[(0, 1)][a, b]
            YRB[n + b, a] = s12 * Y[(0, 1)][a, b]
    t = sum(YB[a, a] for a in range(n))

    def S(A):
        ev = mpmath.eigsy(A / t, eigvals_only=True)
        return -sum(v * mpmath.log(v) for v in ev if v > 0)
    SB, SRB = S(YB), S(YRB)
    return dict(SB=SB, SRB=SRB, dS=SB - SRB)


def P3(phis, XT=40, Dt=70, rs=(200, 267, 340)):
    out = []
    # truncated + renormalised (float64 values are the inputs for both pipelines)
    ph = [p[:XT + 1].copy() for p in phis]
    ph = [p / np.linalg.norm(p) for p in ph]
    mpmath.mp.dps = 40
    ph_mp = [[mpmath.mpf(float(v)) for v in p] for p in ph]
    nrm = [mpmath.sqrt(sum(v * v for v in p)) for p in ph_mp]
    ph_mp = [[v / c for v in p] for p, c in zip(ph_mp, nrm)]
    lf = LogFact(M + 2)
    for r in rs:
        t0 = time.time()
        fl = coherent_information(ph, [0.5, 0.5], M, 11 / 15, Dout=Dt, rs=[r], lf=lf)["blocks"][0]
        t1 = time.time()
        mp = mp_block(ph_mp, [mpmath.mpf(1) / 2, mpmath.mpf(1) / 2], r, XT, Dt)
        t2 = time.time()
        out.append(dict(r=r, XT=XT, Dout=Dt, dS_float=fl["dS"], dS_mp=float(mp["dS"]),
                        SB_float=fl["SB"], SB_mp=float(mp["SB"]), SRB_float=fl["SRB"], SRB_mp=float(mp["SRB"]),
                        abs_err_dS=abs(fl["dS"] - float(mp["dS"])),
                        abs_err_SB=abs(fl["SB"] - float(mp["SB"])),
                        sec_float=t1 - t0, sec_mp=t2 - t1))
        print("P3 r=%d dS float % .16e mp % .16e  err %.2e (%.0fs)" %
              (r, fl["dS"], float(mp["dS"]), out[-1]["abs_err_dS"], t2 - t1), flush=True)
    return out


def P4(phis, rs=(200, 267, 340), seed=5):
    rng = np.random.default_rng(seed)
    lf = LogFact(M + 2)
    res = coherent_information(phis, [0.5, 0.5], M, 11 / 15, Dout=440, rs=list(rs), lf=lf, keep_blocks=True)
    out = []
    for b in res["blocks"]:
        YB, YRB = b["YB"], b["YRB"]
        e1 = entropy_nats(np.linalg.eigvalsh(YB)) - entropy_nats(np.linalg.eigvalsh(YRB))
        e2 = entropy_nats(np.linalg.svd(YB, compute_uv=False)) - entropy_nats(np.linalg.svd(YRB, compute_uv=False))
        QB, _ = np.linalg.qr(rng.normal(size=YB.shape))
        QR, _ = np.linalg.qr(rng.normal(size=YRB.shape))
        e3 = (entropy_nats(np.linalg.eigvalsh(QB.T @ YB @ QB)) - entropy_nats(np.linalg.eigvalsh(QR.T @ YRB @ QR)))
        out.append(dict(r=b["r"], dS_eigvalsh=e1, dS_svd=e2, dS_rotated=e3,
                        spread=max(e1, e2, e3) - min(e1, e2, e3), min_evB=b["min_evB"], min_evRB=b["min_evRB"]))
        print("P4", out[-1], flush=True)
    return out


def main():
    rng = np.random.default_rng(11)
    W, phis, phis_exact, norms2, wsha = load_witness()
    rep = {}
    t0 = time.time()
    rep["P1_B_recursion_vs_mpmath"] = P1(rng)
    print("P1 max rel", rep["P1_B_recursion_vs_mpmath"]["max_rel_error"], time.time() - t0, flush=True)
    rep["P2_coefficients_vs_mpmath"] = P2(rng)
    print("P2", rep["P2_coefficients_vs_mpmath"], flush=True)
    rep["P4_eigensolver"] = P4(phis)
    rep["P3_block_float_vs_mpmath"] = P3(phis)
    rep["seconds"] = time.time() - t0
    with open(OUT, "w") as fh:
        json.dump(rep, fh, indent=1, default=str)
    print("done", rep["seconds"])


if __name__ == "__main__":
    main()
