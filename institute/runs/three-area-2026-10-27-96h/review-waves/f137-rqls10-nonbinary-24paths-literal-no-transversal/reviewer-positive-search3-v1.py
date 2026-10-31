#!/usr/bin/env python3
"""reviewer-positive-search3-v1.py  (review f137, reviewer-written, exploratory, NUMERIC)

Unconstrained numeric search over ALL unimodular n x n matrices K (phases as parameters) for simultaneous
  K Hadamard  and  W = F_n (.) K Hadamard   (W[t][r] = zeta_n^{rt} K[t][r]),
i.e. a Fourier-product QLS of K whose diagonal {(r,r)} (with sigma = id) is a transversal.  Any transversal case can be
brought to this form by permuting K's rows/columns, so the loss has a zero iff some Fourier-product QLS of order n has a
transversal.  Loss = ||K^*K - nI||_F^2 + ||W^*W - nI||_F^2 ; Adam on phases, many random restarts.
Prints best loss per n.  Odd n (5) is the sanity case where zero loss must be reachable (K = F5).
"""
import json, subprocess, time, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
def clock(): return subprocess.run(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], capture_output=True, text=True).stdout.strip()
T0 = clock(); t0 = time.monotonic()

def run(n, restarts, iters, seed):
    rng = np.random.default_rng(seed)
    F = np.exp(2j * np.pi * np.outer(np.arange(n), np.arange(n)) / n)
    best = np.inf; best_theta = None
    for _ in range(restarts):
        th = rng.uniform(0, 2 * np.pi, (n, n)); m = np.zeros_like(th); v = np.zeros_like(th)
        lr = 0.05
        for it in range(iters):
            K = np.exp(1j * th); W = F * K
            G1 = K.conj().T @ K - n * np.eye(n); G2 = W.conj().T @ W - n * np.eye(n)
            loss = np.sum(np.abs(G1) ** 2) + np.sum(np.abs(G2) ** 2)
            # gradient wrt theta: d/dtheta of |G|^2 terms. dK = i K dtheta (elementwise).
            # dL = 2 Re tr(G1^* dG1) with dG1 = dK^* K + K^* dK  ->  dL/dtheta = 2 Re( conj(i K) * (K G1^*) ... ) computed as:
            gK1 = 2 * (K @ G1)            # dL/dconj(K) for first term (G1 hermitian)
            gK2 = 2 * (W @ G2) * F.conj()  # chain through W = F*K
            g = np.real(np.conj(1j * K) * (gK1 + gK2)) * 2   # dL/dtheta = 2 Re( conj(dK/dtheta) * dL/dconj(K) )
            m = 0.9 * m + 0.1 * g; v = 0.999 * v + 0.001 * g * g
            th -= lr * (m / (1 - 0.9 ** (it + 1))) / (np.sqrt(v / (1 - 0.999 ** (it + 1))) + 1e-12)
            if it > iters // 2: lr = 0.01
        K = np.exp(1j * th); W = F * K
        loss = np.sum(np.abs(K.conj().T @ K - n * np.eye(n)) ** 2) + np.sum(np.abs(W.conj().T @ W - n * np.eye(n)) ** 2)
        if loss < best:
            best = loss; best_theta = th.copy()
    return float(best), best_theta

out = {"clock_start": T0, "results": {}}
for n, restarts, iters in ((5, 40, 1500), (4, 60, 1500), (6, 60, 2500), (8, 40, 2500), (10, 60, 3000)):
    b, th = run(n, restarts, iters, 100 + n)
    out["results"][str(n)] = {"best_loss": b, "restarts": restarts, "iters": iters}
    print(f"n={n}: best loss over {restarts} restarts = {b:.6g}", flush=True)
    if b < 1e-6:
        out["results"][str(n)]["theta_over_2pi"] = (np.mod(th, 2 * np.pi) / (2 * np.pi)).round(6).tolist()
out["elapsed_seconds"] = time.monotonic() - t0; out["clock_end"] = clock()
(HERE / "reviewer-positive-search3-result-v1.json").write_text(json.dumps(out, indent=1) + "\n")
