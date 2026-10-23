"""Rigorous enclosure of I_c(rho, N_p^{(x)M}) for rank-r inputs on Sym^M (Dicke basis).

Every inequality used here is stated and proved in review/PROOFS.md (section numbers below).
  §1  Schur-Weyl sector decomposition: I_c(rho, D^{(x)M}) = sum_N p_N I_c(rho, Phi_N),
      Phi_N = sum_s pi_s C_{s->N} o L_{M->s}   (2609.39747 Thm II.3/II.9, re-derived).
  §2  Exact single-particle loss/add step formulas (Schwinger representation).
  §3  Double-double recursion on entrywise NONNEGATIVE operands (inputs split into nonnegative parts
      with phases 1,-1,i,-i): rigorous relative error (1+2^-100)^L - 1, plus absolute ABS_ENTRY.
  §4  Truncation to x <= D with one flag (data processing => lower bound); pi_s tail and atypical
      sectors by almost-convexity and Araki-Lieb; upper bounds by pinching + Alicki-Fannes-Winter.
  §5  Entropy enclosures in Arb: W = V^* A V (V exact dyadic float64 eigenvectors of the midpoint),
      Ostrowski scaling with delta >= ||V^*V - I||_F, Hermitian Gershgorin with component counting.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from fractions import Fraction

import numpy as np
import flint
from flint import arb, arb_mat, acb, acb_mat

import dd as DDm
from dd import DD

PREC = 160
flint.ctx.prec = PREC
EPS = Fraction(1, 2 ** 100)   # per-operation relative error constant of dd.py on nonnegative operands
STEP_OPS = 10                 # error-chain length per loss/add step (PROOFS §3 shows <= 6)
FLUSH = 2.0 ** -900           # nonzero |values| below are set to 0 (keeps every intermediate normal)
ABS_ENTRY = 1e-250            # absolute per-entry budget: flushes + underflow (PROOFS §3)
LOG2 = arb(2).log()
INV_E_LO, INV_E_HI = 0.367879, 0.367880


def A(x) -> arb:
    if isinstance(x, Fraction):
        return arb(x.numerator) / arb(x.denominator)
    if isinstance(x, (int, float)):
        return arb(x)
    if isinstance(x, arb):
        return x
    raise TypeError(type(x))


def up(x) -> float:
    return float(np.nextafter(float(x.upper()), np.inf))


def lo(x) -> float:
    return float(np.nextafter(float(x.lower()), -np.inf))


def h_point(x: float) -> arb:
    if x <= 0.0:
        return arb(0)
    X = arb(x)
    return -X * X.log() / LOG2


def h_range(a: float, b: float):
    """[min, max] of h(x) = -x log2 x over x in [a, b] intersected with [0, 1] (floats, outward)."""
    a = min(max(a, 0.0), 1.0)
    b = min(max(b, a), 1.0)
    ha, hb = h_point(a), h_point(b)
    hmin = max(min(lo(ha), lo(hb)), 0.0)
    if b <= INV_E_LO:
        hmax = up(hb)
    elif a >= INV_E_HI:
        hmax = up(ha)
    else:
        hmax = up(1 / (arb(1).exp() * LOG2))
    return hmin, hmax


def h2_upper(x: float) -> float:
    """upper bound of binary entropy h2(x) for 0 <= x <= 1/2."""
    if x <= 0:
        return 0.0
    X = arb(x)
    return up((-X * X.log() - (1 - X) * (1 - X).log()) / LOG2)


# ----------------------------------------------------------------------------------------------- witness
def parse_witness(w):
    M = int(w["M"])
    p = Fraction(w["p"])
    eta = 1 - Fraction(4, 3) * p
    qs = [Fraction(x) for x in w["q"]]
    assert sum(qs) == 1 and all(q > 0 for q in qs)
    amps = []
    for row in w["amps"]:
        if row and isinstance(row[0], list):
            amps.append(np.array([complex(float.fromhex(a), float.fromhex(b)) for a, b in row]))
        else:
            amps.append(np.array([float.fromhex(a) for a in row]))
    return M, p, eta, qs, amps, w.get("k"), w.get("residues"), int(w["D"])


def positive_parts(c: np.ndarray):
    """exact split c = sum_t phase_t v_t, v_t >= 0, phases in {1,-1,1j,-1j}."""
    re = np.real(c).astype(np.float64)
    im = np.imag(c).astype(np.float64) if np.iscomplexobj(c) else np.zeros_like(re)
    out = []
    for ph, v in ((1, np.maximum(re, 0)), (-1, np.maximum(-re, 0)), (1j, np.maximum(im, 0)),
                  (-1j, np.maximum(-im, 0))):
        if np.any(v > 0):
            out.append((ph, v))
    return out


# ----------------------------------------------------------------------------------------------- probabilities
def sector_probs_arb(M: int, eta: Fraction):
    a, b = (1 + eta) / 2, (1 - eta) / 2
    Aa, Ab, Ae = A(a), A(b), A(eta)
    out = {}
    for N in range(M % 2, M + 1, 2):
        lam2 = (M - N) // 2
        m = math.comb(M, lam2) - (math.comb(M, lam2 - 1) if lam2 >= 1 else 0)
        out[N] = arb(m) * (Aa * Ab) ** lam2 * (Aa ** (N + 1) - Ab ** (N + 1)) / Ae
    return out


def pi_arb(N: int, eta: Fraction):
    Ae = A(eta)
    two_e, one_m = 2 * Ae, 1 - Ae
    den = (1 + Ae) ** (N + 1) - (1 - Ae) ** (N + 1)
    res = []
    pa, pb = two_e, one_m ** N
    inv = 1 / one_m
    for s in range(N + 1):
        res.append(arb(math.comb(N + 1, s + 1)) * pa * pb / den)
        pa *= two_e
        pb *= inv
    return res


def arb_to_dd(x: arb):
    m = x.mid()
    hi = float(m)
    lo_ = float(m - arb(hi))
    err = abs(x - (arb(hi) + arb(lo_))) + x.rad()
    return DD(np.array(hi), np.array(lo_)), (up(err / x) if lo(x) > 0 else float("inf"))


# ----------------------------------------------------------------------------------------------- DD recursion
def _flush(Z: DD) -> DD:
    small = (Z.hi < FLUSH) & (Z.hi != 0)
    if np.any(small):
        Z.hi[small] = 0.0
        Z.lo[small] = 0.0
    return Z


def _scal(Z: DD, c: DD) -> DD:
    return DDm.mul(Z, DD(np.broadcast_to(c.hi, Z.shape), np.broadcast_to(c.lo, Z.shape)))


def loss_step_dd(Y: DD, n: int) -> DD:
    """[L_{n->n-1} Y]_xy = (1/n)[sqrt((n-x)(n-y)) Y_xy + sqrt((x+1)(y+1)) Y_{x+1,y+1}] (PROOFS §2)."""
    d = Y.shape[0]
    dn = min(d, n)
    a = DDm.sqrt_int(n - np.arange(dn, dtype=np.float64))
    out = DDm.mul(DDm.outer(a, a), Y[:dn, :dn])
    m = min(dn, d - 1)
    if m > 0:
        b = DDm.sqrt_int(np.arange(1, m + 1, dtype=np.float64))
        t2 = DDm.mul(DDm.outer(b, b), Y[1:m + 1, 1:m + 1])
        s = DDm.add(out[:m, :m], t2)
        out.hi[:m, :m] = s.hi
        out.lo[:m, :m] = s.lo
    return _flush(_scal(out, DDm.recip_int(np.array(float(n)))))


def add_step_dd(Z: DD, n: int, Dmax: int) -> DD:
    """[C_{n->n+1} Z]_xy = (1/(n+2))[sqrt((n+1-x)(n+1-y)) Z_xy + sqrt(xy) Z_{x-1,y-1}], x,y <= Dmax."""
    d = Z.shape[0]
    dn = min(d + 1, n + 2, Dmax + 1)
    out = DD(np.zeros((dn, dn)), np.zeros((dn, dn)))
    m0 = min(d, dn)
    a = DDm.sqrt_int(n + 1 - np.arange(m0, dtype=np.float64))
    t1 = DDm.mul(DDm.outer(a, a), Z[:m0, :m0])
    out.hi[:m0, :m0] = t1.hi
    out.lo[:m0, :m0] = t1.lo
    m1 = min(d, dn - 1)
    if m1 > 0:
        b = DDm.sqrt_int(np.arange(1, m1 + 1, dtype=np.float64))
        t2 = DDm.mul(DDm.outer(b, b), Z[:m1, :m1])
        s = DDm.add(out[1:m1 + 1, 1:m1 + 1], t2)
        out.hi[1:m1 + 1, 1:m1 + 1] = s.hi
        out.lo[1:m1 + 1, 1:m1 + 1] = s.lo
    return _flush(_scal(out, DDm.recip_int(np.array(float(n + 2)))))


def axpy_dd(Z: DD, pi: DD, Y: DD) -> DD:
    m = min(Y.shape[0], Z.shape[0])
    t = _scal(Y[:m, :m], pi)
    s = DDm.add(Z[:m, :m], t)
    Z.hi[:m, :m] = s.hi
    Z.lo[:m, :m] = s.lo
    return Z


STRIDE = 20   # checkpoint spacing of the loss chain (memory ~ (M-smin)/STRIDE + STRIDE matrices per chain)


class LossChain:
    """Y_s = L_{M->s}(X) with checkpoints at s = M, at multiples of STRIDE and at the lowest level reached.

    The same deterministic loss steps are replayed from a checkpoint, so replayed values are bitwise identical
    to a single straight descent (error model unchanged)."""

    def __init__(self, X: DD, M: int):
        self.ck = {M: X}
        self.low = M

    def extend_to(self, s: int):
        Y, t = self.ck[self.low], self.low
        while t > s:
            Y = loss_step_dd(Y, t)
            t -= 1
            if t % STRIDE == 0 or t == s:
                self.ck[t] = Y
        self.low = min(self.low, s)

    def segment(self, lo_: int, hi_: int):
        """{s: Y_s} for lo_ <= s <= hi_ (requires lo_ >= self.low)."""
        if lo_ < self.low:
            self.extend_to(lo_)
        start = min(l for l in self.ck if l >= hi_)
        Y, t = self.ck[start], start
        out = {}
        if lo_ <= t <= hi_:
            out[t] = Y
        while t > lo_:
            Y = loss_step_dd(Y, t)
            t -= 1
            if t <= hi_:
                out[t] = Y
        return out

    def drop_above(self, top: int):
        """keep the smallest checkpoint >= top and everything below it."""
        keep = min(l for l in self.ck if l >= top)
        for l in [l for l in self.ck if l > keep]:
            del self.ck[l]


def sector_output_dd(chain: LossChain, N: int, smin: int, pis_dd, D: int) -> DD:
    """Z = sum_{s=smin}^{N} pi_s C_{s->N}(Y_s), entries x,y <= D (Horner, PROOFS §2).

    Y_s are replayed in checkpoint-aligned segments [k*STRIDE, (k+1)*STRIDE-1] so each is computed once."""
    chain.extend_to(smin)
    Z = None
    s = smin
    while s <= N:
        seg_hi = min((s // STRIDE + 1) * STRIDE - 1, N)
        Ys = chain.segment(s, seg_hi)
        for t in range(s, seg_hi + 1):
            Y = Ys[t]
            if Z is None:
                m = min(Y.shape[0], D + 1)
                Z = _scal(Y[:m, :m], pis_dd[t])
                Z = DD(np.ascontiguousarray(Z.hi), np.ascontiguousarray(Z.lo))
            else:
                Z = add_step_dd(Z, t - 1, D)
                Z = axpy_dd(Z, pis_dd[t], Y)
        s = seg_hi + 1
    return Z


# ----------------------------------------------------------------------------------------------- entropy
def entropy_enclosure(entries, n: int, complex_: bool, mid: np.ndarray):
    """[lo, hi] for S(A) (bits); A Hermitian PSD, tr A <= 1, entries = nested lists of arb/acb (PROOFS §5)."""
    if n == 0:
        return 0.0, 0.0, {"n": 0}
    Am = acb_mat(entries) if complex_ else arb_mat(entries)
    _, V = np.linalg.eigh(mid)
    if complex_:
        Va = acb_mat([[acb(float(V[i, j].real), float(V[i, j].imag)) for j in range(n)] for i in range(n)])
        Vh = Va.transpose().conjugate()
    else:
        Va = arb_mat(V.tolist())
        Vh = Va.transpose()
    W = Vh * Am * Va
    G = Vh * Va
    d2 = arb(0)
    for i in range(n):
        for j in range(n):
            g = G[i, j] - 1 if i == j else G[i, j]
            d2 += abs(g) ** 2
    delta = up(d2.sqrt())
    if not delta < 1e-6:
        raise RuntimeError(f"Gram defect too large: {delta}")
    lows, highs = [], []
    for i in range(n):
        rsum = arb(0)
        for j in range(n):
            if j != i:
                rsum += abs(W[i, j])
        c = W[i, i].real if complex_ else W[i, i]
        lows.append(lo(c - rsum))
        highs.append(up(c + rsum))
    order = sorted(range(n), key=lambda i: lows[i])
    comps = []
    cur, cur_lo, cur_hi = [order[0]], lows[order[0]], highs[order[0]]
    for i in order[1:]:
        if lows[i] <= cur_hi:
            cur.append(i)
            cur_hi = max(cur_hi, highs[i])
        else:
            comps.append((cur, cur_lo, cur_hi))
            cur, cur_lo, cur_hi = [i], lows[i], highs[i]
    comps.append((cur, cur_lo, cur_hi))
    one_m, one_p = arb(1) - arb(delta), arb(1) + arb(delta)
    S_lo, S_hi = arb(0), arb(0)
    worst = 0.0
    for ci, (idx, a_, b_) in enumerate(comps):
        kc = len(idx)
        a_A = lo(arb(a_) / (one_p if a_ >= 0 else one_m))
        b_A = up(arb(b_) / (one_m if b_ >= 0 else one_p))
        hmin, hmax = h_range(a_A, b_A)
        if ci == 0 and kc > 1:
            # Lowest cluster = the kc smallest eigenvalues of W. Ky Fan: their sum <= tr of any kc-dim
            # compression, e.g. sum_{i in cluster} W_ii.  Hence sum of the kc smallest eigenvalues of A
            # <= (sum W_ii + kc*max(-a_,0)) / (1-delta); with each in [0, 1], concavity gives
            # sum h <= kc * h(mass/kc) whenever mass/kc <= 1/e (PROOFS §5).
            tr = arb(0)
            for i in idx:
                tr += (W[i, i].real if complex_ else W[i, i])
            mass = up((tr + kc * arb(max(-a_, 0.0))) / one_m)
            x = float(np.nextafter(max(mass, 0.0) / kc, np.inf))   # rounded up; h increasing on [0, 1/e]
            if x <= INV_E_LO:
                hmax = min(hmax, up(h_point(x)))
        S_lo += kc * arb(hmin)
        S_hi += kc * arb(hmax)
        worst = max(worst, kc * (hmax - hmin))
    return lo(S_lo), up(S_hi), {"n": n, "delta": delta, "components": len(comps), "worst": worst}


# ----------------------------------------------------------------------------------------------- sector
def operator_arb(parts, relE: float, idx_a, idx_b, scale: arb, complex_: bool):
    """Exact-midpoint ball entries for sum_t phase_t * Z_t restricted to (idx_a x idx_b), times scale."""
    na, nb = len(idx_a), len(idx_b)
    rad = np.zeros((na, nb))
    for _, Z in parts:
        rad += Z.hi[np.ix_(idx_a, idx_b)]
    # rad >= relE * sum_t value_t (value_t <= hi_t (1 + 2^-52)) + ABS_ENTRY (PROOFS §3)
    rad = rad * (relE * (1 + 1e-6)) + ABS_ENTRY
    rows = []
    for a in range(na):
        row = []
        for b in range(nb):
            if complex_:
                re, im = arb(0), arb(0)
                for ph, Z in parts:
                    v = arb(float(Z.hi[idx_a[a], idx_b[b]])) + arb(float(Z.lo[idx_a[a], idx_b[b]]))
                    re += v * ph.real
                    im += v * ph.imag
                rr = float(rad[a, b])
                row.append(acb(re + arb(0, rr), im + arb(0, rr)) * scale)
            else:
                v = arb(0)
                for ph, Z in parts:
                    v += (arb(float(Z.hi[idx_a[a], idx_b[b]])) + arb(float(Z.lo[idx_a[a], idx_b[b]]))) * int(np.real(ph))
                row.append((v + arb(0, float(rad[a, b]))) * scale)
        rows.append(row)
    return rows


def run_sector(N, M, chains, keys, qs, norms2, k, residues, D, smin, pis, pis_dd, pis_rel, complex_, Srho_hi):
    t0 = time.time()
    r = len(qs)
    outs = {}
    for key in keys:
        outs[key] = [(ph, sector_output_dd(ch, N, smin, pis_dd, D)) for ph, ch in chains[key]]
    nsteps = (M - smin) + (N - smin)
    L = STEP_OPS * nsteps + 20
    relE = up((1 + A(EPS)) ** L - 1) * 1.01 + 1.01 * max(pis_rel)
    dB = outs[keys[0]][0][1].shape[0]
    Dm = dB - 1
    if k is None and Dm < N:
        raise ValueError("non-modular inputs require D >= N (no truncation)")
    pi_mass = arb(0)
    for s in range(smin, N + 1):
        pi_mass += pis[s]
    eps_tail = max(up(1 - pi_mass), 0.0)
    inv_mass = 1 / pi_mass
    xs = np.arange(dB)
    sc_B = [A(qs[i]) / norms2[i] * inv_mass for i in range(r)]
    sc_RB = {(i, j): (A(qs[i]) * A(qs[j]) / (norms2[i] * norms2[j])).sqrt() * inv_mass
             for i in range(r) for j in range(r)}
    # truncated traces -> flag weights w_i (exact-midpoint arb sums)
    ws = []
    for i in range(r):
        parts = outs[(i, i)]
        tr = arb(0)
        rad_tr = 0.0
        for ph, Z in parts:
            for x in range(dB):
                v = arb(float(Z.hi[x, x])) + arb(float(Z.lo[x, x]))
                tr += v * (int(np.real(ph)) if not complex_ else ph.real)
                rad_tr += float(Z.hi[x, x])
        tr = tr + arb(0, rad_tr * relE * (1 + 1e-6) + dB * ABS_ENTRY)
        ws.append(1 - tr / norms2[i] * inv_mass)
    if Dm >= N:   # no truncation: T_D is the identity, the flag carries exactly zero weight (PROOFS §4)
        ws = [arb(0) for _ in range(r)]
    if k is None:
        blocks_B = [xs]
        blocks_RB = [[xs for _ in range(r)]]
    else:
        blocks_B = [np.nonzero(xs % k == c)[0] for c in range(k)]
        blocks_RB = [[np.nonzero(xs % k == (c + residues[i]) % k)[0] for i in range(r)] for c in range(k)]
    SB = [arb(0), arb(0)]
    SRB = [arb(0), arb(0)]
    info = []
    for ix in blocks_B:
        n = len(ix)
        entries = None
        mid = np.zeros((n, n), dtype=np.complex128 if complex_ else np.float64)
        for i in range(r):
            blk = operator_arb(outs[(i, i)], relE, ix, ix, sc_B[i], complex_)
            entries = blk if entries is None else [[entries[a][b] + blk[a][b] for b in range(n)] for a in range(n)]
            for ph, Z in outs[(i, i)]:
                mid += (ph if complex_ else np.real(ph)) * (Z.hi + Z.lo)[np.ix_(ix, ix)] * float(sc_B[i].mid())
        l_, h_, inf = entropy_enclosure(entries, n, complex_, mid)
        SB[0] += arb(l_)
        SB[1] += arb(h_)
        info.append(("B", inf))
    for ids in blocks_RB:
        sizes = [len(v) for v in ids]
        offs = np.concatenate([[0], np.cumsum(sizes)]).astype(int)
        nn = int(offs[-1])
        entries = [[None] * nn for _ in range(nn)]
        mid = np.zeros((nn, nn), dtype=np.complex128 if complex_ else np.float64)
        for i in range(r):
            for j in range(r):
                if i <= j:
                    blk = operator_arb(outs[(i, j)], relE, ids[i], ids[j], sc_RB[(i, j)], complex_)
                    for ph, Z in outs[(i, j)]:
                        mid[offs[i]:offs[i + 1], offs[j]:offs[j + 1]] += (ph if complex_ else np.real(ph)) * \
                            (Z.hi + Z.lo)[np.ix_(ids[i], ids[j])] * float(sc_RB[(i, j)].mid())
                else:
                    blk_t = operator_arb(outs[(j, i)], relE, ids[j], ids[i], sc_RB[(i, j)], complex_)
                    blk = [[(blk_t[b][a].conjugate() if complex_ else blk_t[b][a]) for b in range(sizes[j])]
                           for a in range(sizes[i])]
                    mid[offs[i]:offs[i + 1], offs[j]:offs[j + 1]] = np.conj(mid[offs[j]:offs[j + 1], offs[i]:offs[i + 1]]).T
                for a in range(sizes[i]):
                    for b in range(sizes[j]):
                        entries[offs[i] + a][offs[j] + b] = blk[a][b]
        l_, h_, inf = entropy_enclosure(entries, nn, complex_, mid)
        SRB[0] += arb(l_)
        SRB[1] += arb(h_)
        info.append(("RB", inf))
    # one flag (PROOFS §4): modular inputs => RB flag block diag(q_i w_i)
    w_lo = [max(lo(w), 0.0) for w in ws]
    w_hi = [max(up(w), 0.0) for w in ws]
    fB = h_range(lo(sum((A(qs[i]) * arb(w_lo[i]) for i in range(r)), arb(0))),
                 up(sum((A(qs[i]) * arb(w_hi[i]) for i in range(r)), arb(0))))
    fRB = [h_range(lo(A(qs[i]) * arb(w_lo[i])), up(A(qs[i]) * arb(w_hi[i]))) for i in range(r)]
    if k is None and Dm < N:
        raise ValueError("non-modular inputs require D >= N")
    ic_lo = (SB[0] + arb(fB[0])) - (SRB[1] + sum(arb(f[1]) for f in fRB))
    ic_hi = (SB[1] + arb(fB[1])) - (SRB[0] + sum(arb(f[0]) for f in fRB))
    w_tot = up(sum((A(qs[i]) * arb(w_hi[i]) for i in range(r)), arb(0)))
    # ---- lower bound for I_c(rho, Phi_N)  (PROOFS §4): DPI, then pi-tail almost-convexity
    e = eps_tail
    h2e = h2_upper(e) if e > 0 else 0.0
    icl = lo(ic_lo)
    lowN = ((1 - arb(e)) * arb(icl) if icl >= 0 else arb(icl)) - arb(e) * arb(Srho_hi) - arb(h2e)
    # ---- upper bound: pinching + AFW (needs small w), flag correction, pi-tail
    icu = up(ic_hi) + sum(f[1] for f in fRB)
    sw = math.sqrt(w_tot) * (1 + 1e-12)
    afw = 0.0
    if sw > 0:
        afw = w_tot * math.log2(r) + 2 * sw * math.log2(r) + (1 + sw) * h2_upper(min(sw / (1 + sw), 0.5))
        afw *= 1 + 1e-12
    upI = arb(icu) + arb(afw)
    upN = ((1 - arb(e)) * upI if lo(upI) < 0 else upI) + arb(e) * arb(Srho_hi) + arb(h2e)
    return {"N": N, "lo": lo(lowN), "hi": up(upN), "ic_trunc": [lo(ic_lo), up(ic_hi)], "eps_tail": e,
            "w_tail": w_tot, "relE": relE, "smin": smin, "nsteps": nsteps, "D": Dm,
            "secs": round(time.time() - t0, 2), "blocks": info}


def certify(witness, sectors_only=None, ptail=1e-30, pitail=1e-40, verbose=True, log=None):
    M, p, eta, qs, amps, k, residues, D = parse_witness(witness)
    r = len(qs)
    complex_ = any(np.iscomplexobj(c) and np.any(np.imag(c) != 0) for c in amps)
    K = max(len(c) for c in amps) - 1
    amps = [np.pad(c, (0, K + 1 - len(c))) for c in amps]
    for c in amps:
        nz = np.abs(c[c != 0])
        if nz.size and nz.min() < 1e-100:
            raise ValueError("witness amplitudes must be 0 or >= 1e-100 in modulus")
    assert M + D < 10 ** 6 and D < 10 ** 4
    norms2 = []
    for c in amps:
        s = arb(0)
        for z in c:
            if z != 0:
                s += arb(float(np.real(z))) ** 2 + arb(float(np.imag(z))) ** 2
        norms2.append(s)
    orth = all(np.vdot(amps[i], amps[j]) == 0 for i in range(r) for j in range(i + 1, r))
    if orth:   # rho = sum q_i |c_i><c_i| with orthonormal c_i: S(rho) = H(q)
        Srho = sum((-A(q) * A(q).log() / LOG2 for q in qs), arb(0))
    else:      # rank <= r
        Srho = arb(r).log() / LOG2
    Srho_hi = up(Srho)
    pN = sector_probs_arb(M, eta)
    tot = sum(pN.values(), arb(0))
    if not tot.contains(arb(1)):
        raise RuntimeError(f"sector probabilities do not sum to 1: {tot}")
    sel, rest = [], arb(0)
    for n in pN:
        if float(pN[n].mid()) >= ptail and (sectors_only is None or n in sectors_only):
            sel.append(n)
        else:
            rest += pN[n]
    sel.sort(reverse=True)
    parts = [positive_parts(c) for c in amps]
    keys = [(i, j) for i in range(r) for j in range(i, r)]
    chains = {}
    for (i, j) in keys:
        # nonnegative outer products grouped by combined phase; a part is merged into an existing matrix of the
        # same phase only when their supports are disjoint (then the entrywise sum is exact); otherwise it
        # gets its own chain. Real signed inputs: (+,+)&(-,-) merge, (+,-)&(-,+) merge -> 2 chains.
        groups = []
        for ph_a, va in parts[i]:
            for ph_b, vb in parts[j]:
                ph = complex(ph_a * np.conj(ph_b))
                Xh, Xl = DDm.two_prod(np.outer(va, np.ones(K + 1)), np.outer(np.ones(K + 1), vb))
                for g in groups:
                    if g[0] == ph and not np.any((g[1].hi != 0) & (Xh != 0)):
                        g[1] = DD(g[1].hi + Xh, g[1].lo + Xl)   # disjoint supports: exact
                        break
                else:
                    groups.append([ph, DD(Xh, Xl)])
        chains[(i, j)] = [((ph.real if (ph.imag == 0 and not complex_) else ph), LossChain(G, M))
                          for ph, G in groups]
    results = []
    tot_lo, tot_hi = arb(0), arb(0)
    for N in sel:
        pis = pi_arb(N, eta)
        cum, smin = arb(0), 0
        for s in range(N + 1):
            if up(cum + pis[s]) > pitail:
                smin = s
                break
            cum += pis[s]
        pis_dd, rels = {}, []
        for s in range(smin, N + 1):
            pis_dd[s], rel = arb_to_dd(pis[s])
            rels.append(rel)
        res = run_sector(N, M, chains, keys, qs, norms2, k, residues, D, smin, pis, pis_dd, rels, complex_, Srho_hi)
        res["pN"] = float(pN[N].mid())
        tot_lo += pN[N] * arb(res["lo"])
        tot_hi += pN[N] * arb(res["hi"])
        for lst in chains.values():
            for _, ch in lst:
                ch.drop_above(N - 2)
        results.append(res)
        if verbose:
            print(f"N={N} pN={res['pN']:.3e} Ic_N in [{res['lo']:+.9e},{res['hi']:+.9e}] smin={smin} "
                  f"w={res['w_tail']:.1e} eps={res['eps_tail']:.1e} relE={res['relE']:.1e} t={res['secs']}s",
                  flush=True)
        if log is not None:
            log.write(json.dumps({k_: v for k_, v in res.items() if k_ != "blocks"}) + "\n")
            log.flush()
    tot_lo -= rest * arb(Srho_hi)
    tot_hi += rest * arb(Srho_hi)
    return {"lower": lo(tot_lo), "upper": up(tot_hi), "rest_mass": up(rest), "Srho_hi": Srho_hi,
            "sectors": len(results), "M": M, "p": str(p), "eta": str(eta), "D": D}, results


def witness_sha256(w):
    return hashlib.sha256(json.dumps(w, sort_keys=True).encode()).hexdigest()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("witness")
    ap.add_argument("--out", required=True)
    ap.add_argument("--ptail", type=float, default=1e-30)
    ap.add_argument("--pitail", type=float, default=1e-40)
    ap.add_argument("--sectors", default=None, help="comma list of N, or lo:hi")
    a = ap.parse_args()
    w = json.load(open(a.witness))
    only = None
    if a.sectors:
        if ":" in a.sectors:
            l_, h_ = map(int, a.sectors.split(":"))
            only = set(range(l_, h_ + 1))
        else:
            only = set(int(x) for x in a.sectors.split(","))
    t0 = time.time()
    with open(a.out + ".sectors.jsonl", "a") as lg:
        summary, _ = certify(w, only, a.ptail, a.pitail, True, lg)
    summary["witness_sha256"] = witness_sha256(w)
    summary["secs"] = round(time.time() - t0, 1)
    summary["sectors_arg"] = a.sectors
    json.dump(summary, open(a.out, "w"), indent=1)
    print(json.dumps(summary))
