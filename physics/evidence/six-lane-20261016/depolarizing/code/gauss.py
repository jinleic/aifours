"""Gaussian-limit evaluator for the depolarizing threshold problem (exploration, float64).

Emergent channel of arXiv:2609.39747 Thm 6: G_eta = A_G o L_T with T = 2 eta^2/(1+eta), G = (1+eta)/(2 eta)
(thermal attenuator, transmissivity eta, N_E = 1/(2 eta)).  eta = 1 - 4p/3.

Input: rank-r state rho = sum_i q_i |psi_i><psi_i| on a single mode, psi_i supported on Fock levels n <= K.
Optional modular structure: psi_i supported on n = r_i (mod k); then every output operator E(|psi_i><psi_j|)
has entries only at x - y = r_i - r_j (mod k) (phase covariance), so B and RB are block diagonal.

Output truncation: Fock levels x <= D kept, everything above collapsed to ONE flag state (a CPTP post-processing,
so by data processing the computed value is a lower bound on I_c of the untruncated channel, in exact arithmetic).
Flag RB block is diag(q_i w_i) in the modular case (off-diagonal flag terms vanish because r_i != r_j mod k);
w_i = 1 - tr(P_D E(psi_i)).
"""
from __future__ import annotations

import math
import torch

torch.set_default_dtype(torch.float64)


def log_binom_table(nmax: int) -> torch.Tensor:
    """lgamma table: lf[n] = log n!"""
    n = torch.arange(nmax + 2, dtype=torch.float64)
    return torch.lgamma(n + 1)


class GaussChannel:
    def __init__(self, eta: float, K: int, D: int):
        self.eta = float(eta)
        self.K, self.D = K, D
        self.T = 2 * eta * eta / (1 + eta)
        self.G = (1 + eta) / (2 * eta)
        lf = log_binom_table(max(K, D) + 2)
        T, G = self.T, self.G
        # loss coefficients: c_u(x) = sqrt(C(x+u,u) T^x (1-T)^u), x = 0..K-u
        self.loss = []
        for u in range(K + 1):
            x = torch.arange(0, K + 1 - u, dtype=torch.float64)
            lc = 0.5 * (lf[(x + u).long()] - lf[x.long()] - lf[u] + x * math.log(T) + u * math.log1p(-T))
            self.loss.append(torch.exp(lc))
        # amplifier coefficients: a_t(x) = sqrt(C(x,t) (G-1)^t / G^(x+1)), x = t..D
        self.amp = []
        for t in range(D + 1):
            x = torch.arange(t, D + 1, dtype=torch.float64)
            la = 0.5 * (lf[x.long()] - lf[t] - lf[(x - t).long()] + t * math.log(G - 1) - (x + 1) * math.log(G))
            self.amp.append(torch.exp(la))

    def apply(self, X: torch.Tensor) -> torch.Tensor:
        """X: (K+1)x(K+1) operator (real or complex). Returns (D+1)x(D+1) truncated output."""
        K, D = self.K, self.D
        Y = torch.zeros((K + 1, K + 1), dtype=X.dtype)
        for u in range(K + 1):
            c = self.loss[u].to(X.dtype)
            Y[: K + 1 - u, : K + 1 - u] = Y[: K + 1 - u, : K + 1 - u] + torch.outer(c, c) * X[u:, u:]
        Yp = torch.zeros((D + 1, D + 1), dtype=X.dtype)
        Yp[: K + 1, : K + 1] = Y
        Z = torch.zeros((D + 1, D + 1), dtype=X.dtype)
        for t in range(D + 1):
            a = self.amp[t].to(X.dtype)
            Z[t:, t:] = Z[t:, t:] + torch.outer(a, a) * Yp[: D + 1 - t, : D + 1 - t]
        return Z


def entropy_bits(evals: torch.Tensor) -> torch.Tensor:
    ev = torch.clamp(evals, min=0.0)
    m = ev > 1e-300
    return -(ev[m] * torch.log2(ev[m])).sum()


def coherent_info_modular(ch: GaussChannel, psis, qs, residues, k):
    """psis: list of (K+1) real/complex tensors (normalized, supported on n = residues[i] mod k)."""
    r = len(psis)
    D = ch.D
    outs = {}
    for i in range(r):
        for j in range(i, r):
            X = torch.outer(psis[i], psis[j].conj())
            outs[(i, j)] = ch.apply(X)
    # B blocks by x mod k
    B = sum(qs[i] * outs[(i, i)] for i in range(r))
    w = [1.0 - torch.real(torch.trace(outs[(i, i)])) for i in range(r)]
    xs = torch.arange(D + 1)
    SB = torch.zeros(())
    for c in range(k):
        idx = (xs % k == c).nonzero().flatten()
        blk = B[idx][:, idx]
        SB = SB + entropy_bits(torch.linalg.eigvalsh(blk))
    flagB = sum(qs[i] * w[i] for i in range(r))
    SB = SB + entropy_bits(torch.stack([flagB]))
    # RB blocks: class c contains (i, x) with x = c + residues[i] mod k
    SRB = torch.zeros(())
    for c in range(k):
        idx_list = []
        for i in range(r):
            idx_list.append((xs % k == (c + residues[i]) % k).nonzero().flatten())
        sizes = [len(v) for v in idx_list]
        n = sum(sizes)
        Om = torch.zeros((n, n), dtype=B.dtype)
        offs = [0]
        for s_ in sizes:
            offs.append(offs[-1] + s_)
        for i in range(r):
            for j in range(r):
                if i <= j:
                    O = outs[(i, j)]
                else:
                    O = outs[(j, i)].conj().T
                blk = math.sqrt(1.0) * O[idx_list[i]][:, idx_list[j]]
                fac = torch.sqrt(qs[i] * qs[j])
                Om[offs[i]:offs[i + 1], offs[j]:offs[j + 1]] = fac * blk
        SRB = SRB + entropy_bits(torch.linalg.eigvalsh(Om))
    SRB = SRB + entropy_bits(torch.stack([qs[i] * w[i] for i in range(r)]))
    return SB - SRB, SB, SRB, w


def hashing_ic(p: float) -> float:
    """n=1 maximally mixed input: 1 - h(p) - p log2 3 (total-error convention)."""
    h = -p * math.log2(p) - (1 - p) * math.log2(1 - p)
    return 1 - h - p * math.log2(3)
