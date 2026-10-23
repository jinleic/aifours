"""Exact finite-M coherent information of symmetric (Dicke-supported) inputs through D_eta^{(x)M} (float64).

Representation (independently derived, Schwinger two-mode picture):
  Sym^n basis |n;x> (x = number of |1>'s).  Single-particle loss (= partial trace of one qubit) and
  single-particle universal cloning step:
     L_{n->n-1}(X) = (1/n)   (a0 X a0^+ + a1 X a1^+)
     C_{n->n+1}(X) = (1/(n+2)) (a0^+ X a0 + a1^+ X a1)
  [L(X)]_{xy} = (1/n)     [sqrt((n-x)(n-y)) X_{xy} + sqrt((x+1)(y+1)) X_{x+1,y+1}]
  [C(X)]_{xy} = (1/(n+2)) [sqrt((n+1-x)(n+1-y)) X_{xy} + sqrt(x y) X_{x-1,y-1}]
Sector decomposition (arXiv:2609.39747 Thm II.3, II.9):
  D^{(x)M}(X) = sum_N p_N Phi_N(X) (x) I/m_{M,N},   Phi_N = sum_{s=0}^{N} pi_s C_{s->N} o L_{M->s}
  I_c(rho, D^{(x)M}) = sum_N p_N I_c(rho, Phi_N)        (multiplicity spaces cancel)
Horner evaluation of Phi_N: Z_{smin} = pi_smin Y_smin ; Z_{s+1} = C_{s->s+1}(Z_s) + pi_{s+1} Y_{s+1}, Y_s = L_{M->s}(X).
Output truncation to x <= D is exact for those entries (C never lowers x); the rest is one flag (data processing).
Sectors with negligible p_N or s-range tails are accounted as explicit error budgets (reported).
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

LOG2 = math.log(2.0)


def lchoose(n, k):
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def sector_probs(M: int, eta: float):
    """p_N for N = M, M-2, ... (dict). Eq. (II.6) of 2609.39747, evaluated in logs."""
    out = {}
    a = (1 + eta) / 2
    b = (1 - eta) / 2
    for N in range(M % 2, M + 1, 2):
        lam2 = (M - N) // 2
        # m_{M,N} = C(M,lam2) - C(M,lam2-1) = C(M,lam2) * (N+1)/(M-lam2+1)
        lm = lchoose(M, lam2) + math.log(N + 1) - math.log(M - lam2 + 1)
        # p_N = m * (ab)^lam2 * (a^{N+1}-b^{N+1})/eta
        lq = (N + 1) * math.log(a) + math.log1p(-(b / a) ** (N + 1)) - math.log(eta)
        out[N] = math.exp(lm + lam2 * math.log(a * b) + lq)
    return out


def pi_weights(N: int, eta: float):
    """pi_s, s=0..N (Eq. II.14): r=s+1 ~ Bin(N+1, tau) conditioned on r>=1, tau = 2eta/(1+eta)."""
    tau = 2 * eta / (1 + eta)
    r = np.arange(1, N + 2)
    lw = np.array([lchoose(N + 1, int(rr)) for rr in r]) + r * math.log(tau) + (N + 1 - r) * math.log1p(-tau)
    lnorm = math.log1p(-((1 - tau) ** (N + 1)))
    return np.exp(lw - lnorm)


def loss_step(Y: np.ndarray, n: int) -> np.ndarray:
    """L_{n->n-1} on an operator stored for x,y in [0, d-1] (d <= n+1). Returns size min(d, n)."""
    d = Y.shape[0]
    dn = min(d, n)  # new dimension: x <= n-1
    x = np.arange(dn, dtype=np.float64)
    s0 = np.sqrt(n - x)
    out = np.outer(s0, s0) * Y[:dn, :dn]
    if d > 1:
        m = min(dn, d - 1)
        s1 = np.sqrt(np.arange(1, m + 1, dtype=np.float64))
        out[:m, :m] += np.outer(s1, s1) * Y[1:m + 1, 1:m + 1]
    return out / n


def add_step(Z: np.ndarray, n: int, Dmax: int) -> np.ndarray:
    """C_{n->n+1}; Z stored for x,y in [0, d-1], d <= n+1; output truncated to x <= Dmax."""
    d = Z.shape[0]
    dn = min(d + 1, n + 2, Dmax + 1)
    out = np.zeros((dn, dn), dtype=Z.dtype)
    m0 = min(d, dn)
    x = np.arange(m0, dtype=np.float64)
    s0 = np.sqrt(n + 1 - x)
    out[:m0, :m0] = np.outer(s0, s0) * Z[:m0, :m0]
    m1 = min(d, dn - 1)
    if m1 > 0:
        s1 = np.sqrt(np.arange(1, m1 + 1, dtype=np.float64))
        out[1:m1 + 1, 1:m1 + 1] += np.outer(s1, s1) * Z[:m1, :m1]
    return out / (n + 2)


def entropy_bits(ev: np.ndarray) -> float:
    ev = ev[ev > 1e-300]
    return float(-(ev * np.log2(ev)).sum())


@dataclass
class SectorResult:
    N: int
    pN: float
    ic: float
    SB: float
    SRB: float
    flag: list
    pi_tail: float


def blocks_modular(D: int, k: int, residues):
    xs = np.arange(D + 1)
    Bblocks = [np.nonzero(xs % k == c)[0] for c in range(k)]
    RBblocks = []
    for c in range(k):
        RBblocks.append([np.nonzero(xs % k == (c + r) % k)[0] for r in residues])
    return Bblocks, RBblocks


def sector_ic_from_outputs(outs, qs, D, k, residues):
    """outs[(i,j)] (i<=j): truncated (<=D) Phi_N(|c_i><c_j|). Returns (ic, SB, SRB, flags)."""
    r = len(qs)
    dB = outs[(0, 0)].shape[0]
    Dm = dB - 1
    B = sum(qs[i] * outs[(i, i)] for i in range(r))
    w = [1.0 - float(np.real(np.trace(outs[(i, i)]))) for i in range(r)]
    if k is None:
        SB = entropy_bits(np.linalg.eigvalsh(B))
        n = dB
        Om = np.zeros((r * n, r * n), dtype=B.dtype)
        for i in range(r):
            for j in range(r):
                O = outs[(i, j)] if i <= j else outs[(j, i)].conj().T
                Om[i * n:(i + 1) * n, j * n:(j + 1) * n] = math.sqrt(qs[i] * qs[j]) * O
        SRB = entropy_bits(np.linalg.eigvalsh(Om))
    else:
        Bb, RBb = blocks_modular(Dm, k, residues)
        SB = sum(entropy_bits(np.linalg.eigvalsh(B[np.ix_(ix, ix)])) for ix in Bb)
        SRB = 0.0
        for c in range(k):
            ids = RBb[c]
            sizes = [len(v) for v in ids]
            offs = np.concatenate([[0], np.cumsum(sizes)])
            Om = np.zeros((offs[-1], offs[-1]), dtype=B.dtype)
            for i in range(r):
                for j in range(r):
                    O = outs[(i, j)] if i <= j else outs[(j, i)].conj().T
                    Om[offs[i]:offs[i + 1], offs[j]:offs[j + 1]] = math.sqrt(qs[i] * qs[j]) * O[np.ix_(ids[i], ids[j])]
            SRB += entropy_bits(np.linalg.eigvalsh(Om))
    # single flag for everything above D (modular case: flag RB block diagonal)
    fB = sum(qs[i] * max(w[i], 0.0) for i in range(r))
    SB += entropy_bits(np.array([fB]))
    SRB += entropy_bits(np.array([qs[i] * max(w[i], 0.0) for i in range(r)]))
    return SB - SRB, SB, SRB, w


def finite_ic(M: int, eta: float, cs, qs, D: int, k=None, residues=None, ptail=1e-18, pitail=1e-18,
              verbose=False):
    """cs: list of Dicke amplitude vectors (len K+1, normalized). Returns (lower-bound-style total, details).

    Total = sum over computed sectors p_N * I_c(T_D o Phi_N) - (uncomputed sector mass) * S(rho)
    (I_c >= -S(rho) for every channel). pi-tail truncation in s is reported (not yet a rigorous term).
    """
    r = len(cs)
    K = max(len(c) for c in cs) - 1
    cs = [np.pad(np.asarray(c), (0, K + 1 - len(c))) for c in cs]
    Srho = -sum(q * math.log2(q) for q in qs if q > 0)
    pN = sector_probs(M, eta)
    Ns = sorted(pN, key=lambda n: -pN[n])
    keep, acc = [], 0.0
    tot = sum(pN.values())
    for n in Ns:
        keep.append(n)
        acc += pN[n]
        if tot - acc < ptail:
            break
    keep = sorted(keep)
    dropped = max(0.0, 1.0 - acc)
    Nmin = keep[0]
    # Loss chain from M down; we need Y_s = L_{M->s}(X_ij) for s >= smin(Nmin)
    pis = {N: pi_weights(N, eta) for N in keep}
    smins = {}
    tails = {}
    for N in keep:
        w = pis[N]
        cdf = np.cumsum(w)
        smin = int(np.searchsorted(cdf, pitail))
        smins[N] = smin
        tails[N] = float(cdf[smin - 1]) if smin > 0 else 0.0
    smin_glob = min(smins.values())
    ops = {}
    for i in range(r):
        for j in range(i, r):
            ops[(i, j)] = np.outer(cs[i], np.conj(cs[j]))
    # store Y_s for s in [smin_glob, M]: memory heavy for big M -> store dict of arrays
    Ys = {key: {} for key in ops}
    cur = {key: ops[key][: min(K, M) + 1, : min(K, M) + 1] for key in ops}
    for s in range(M, smin_glob - 1, -1):
        if s < M:
            for key in ops:
                cur[key] = loss_step(cur[key], s + 1)
        for key in ops:
            Ys[key][s] = cur[key]
    results = []
    total = 0.0
    for N in keep:
        w = pis[N]
        smin = smins[N]
        outs = {}
        for key in ops:
            Z = w[smin] * Ys[key][smin][: D + 1, : D + 1]
            for s in range(smin, N):
                Z = add_step(Z, s, D)
                Y = Ys[key][s + 1]
                m = min(Y.shape[0], Z.shape[0])
                Z[:m, :m] += w[s + 1] * Y[:m, :m]
            outs[key] = Z
        ic, SB, SRB, flags = sector_ic_from_outputs(outs, qs, D, k, residues)
        results.append(SectorResult(N, pN[N], ic, SB, SRB, flags, tails[N]))
        total += pN[N] * ic
        if verbose:
            print(f"N={N} pN={pN[N]:.3e} ic={ic:+.6e} flags={max(flags):.1e} pitail={tails[N]:.1e}", flush=True)
    total -= dropped * Srho
    return total, results, dropped
