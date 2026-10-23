"""Exploratory: for an FD-consistent binary code C (no two words agree on N(v) and differ at v), optimize a
probability distribution p on C to maximize  H(p) / max_v H(p_v)  (bits).  Any p supported on C satisfies
the game FDs exactly; the typicality bridge (to be written separately) turns a ratio into a lower bound
on gn.  Float search only; a promising p must be re-certified exactly (rational p, exact entropy sign).
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, nbmasks

def fd_ok(code, nbm):
    for v in range(10):
        seen = {}
        for x in code:
            k = x & nbm[v]; b = (x >> v) & 1
            if seen.setdefault(k, b) != b: return False
    return True

def ratio_and_grad(theta, bits, beta=60.0):
    p = np.exp(theta - theta.max()); p /= p.sum()
    lp = np.log(p + 1e-300)
    H = -(p * lp).sum()
    # marginals
    q1 = bits.T @ p                      # P(x_v = 1), shape (10,)
    q1 = np.clip(q1, 1e-15, 1 - 1e-15)
    Hv = -(q1 * np.log(q1) + (1 - q1) * np.log(1 - q1))
    # smooth max
    w = np.exp(beta * (Hv - Hv.max())); w /= w.sum()
    M = (w * Hv).sum()  # soft-weighted max (close to max for large beta)
    # gradients wrt p
    dH = -lp - 1
    dHv = np.log((1 - q1) / q1)          # dHv/dq1
    dM_dp = bits @ (w * dHv)             # approx (ignores w's dependence; fine for ascent)
    R = H / M
    dR_dp = (dH * M - H * dM_dp) / (M * M)
    # softmax chain
    g = p * (dR_dp - (p * dR_dp).sum())
    return R, g, H, Hv

def optimize(code, iters=3000, lr=0.05, seed=0, restarts=6):
    bits = np.array([[(x >> v) & 1 for v in range(10)] for x in code], dtype=float)
    rng = np.random.default_rng(seed); best = (0, None)
    for r in range(restarts):
        th = rng.normal(0, 0.3, len(code))
        m = np.zeros_like(th); s = np.zeros_like(th)
        for t in range(1, iters + 1):
            R, g, H, Hv = ratio_and_grad(th, bits)
            m = 0.9 * m + 0.1 * g; s = 0.999 * s + 0.001 * g * g
            th += lr * (m / (1 - 0.9 ** t)) / (np.sqrt(s / (1 - 0.999 ** t)) + 1e-12)
        p = np.exp(th - th.max()); p /= p.sum()
        lp = np.log(p + 1e-300); H = -(p * lp).sum()
        q1 = bits.T @ p; q1 = np.clip(q1, 1e-15, 1 - 1e-15)
        Hv = -(q1 * np.log(q1) + (1 - q1) * np.log(1 - q1))
        Rt = H / Hv.max()
        if Rt > best[0]: best = (Rt, p)
    return best

if __name__ == "__main__":
    d = json.load(open(sys.argv[1]))
    code = d["code"]; nbm = nbmasks(R_MINUS_EDGES)
    assert fd_ok(code, nbm)
    R, p = optimize(code)
    print(json.dumps(dict(code_size=len(code), uniform_ratio=float(np.log(len(code)) / np.log(2)), best_ratio=float(R))))
