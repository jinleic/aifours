#!/usr/bin/env python3
"""f172 reviewer floating sanity checks (ReviewF172DepolFresh).

NON-EXACT and NON-PROOF: double-precision numpy sampling only, used to look
for gross contradictions with the written tube bound (27), the Hessian margin
(21) and the t<=1/200 all-density statement.  Independently written; no
author code or author files.  Fixed seed; bounded sample counts.
"""
import itertools
import json
import sys

import numpy as np

SEED = 20261029
rng = np.random.default_rng(SEED)
P1 = np.eye(2, dtype=complex)
PX = np.array([[0, 1], [1, 0]], dtype=complex)
PY = np.array([[0, -1j], [1j, 0]], dtype=complex)
PZ = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [P1, PX, PY, PZ]
PAULIS4 = []
for s in itertools.product(range(4), repeat=4):
    M = PAULI[s[0]]
    for k in s[1:]:
        M = np.kron(M, PAULI[k])
    PAULIS4.append((sum(1 for k in s if k), M))
WT = np.array([bin(x).count("1") for x in range(16)])


def lam(p, X):
    out = np.zeros((16, 16), dtype=complex)
    for w, P in PAULIS4:
        c = np.trace(X @ P) / 16
        if c != 0:
            out += c * (1 - p) ** w * P
    return out


def k3(X):
    return np.sort(np.linalg.eigvalsh((X + X.conj().T) / 2))[::-1][:3].sum()


def R3(t):
    a, b = (1 + t) / 2, (1 - t) / 2
    return a ** 4 + 2 * a ** 3 * b


def rand_normal_v():
    v = (rng.normal(size=16) + 1j * rng.normal(size=16)) * (WT >= 2)
    # random weight emphasis to visit single-weight and mixed directions
    mode = rng.integers(0, 5)
    if mode < 3:
        v = v * (WT == (mode + 2))
    return v / np.linalg.norm(v)


def hessian(v, t):
    a, b = (1 + t) / 2, (1 - t) / 2
    lamh = [a ** (4 - h) * b ** h for h in range(5)]
    e0 = np.zeros(16, dtype=complex)
    e0[0] = 1
    V = lam(1 - t, np.outer(v, e0.conj()) + np.outer(e0, v.conj()))
    Wm = lam(1 - t, np.outer(v, v.conj()) - np.outer(e0, e0.conj()))
    A = Wm[0, 0].real + sum(abs(V[k, 0]) ** 2 / (lamh[0] - lamh[WT[k]]) for k in range(16) if WT[k] >= 2)
    e1 = [8, 4, 2, 1]
    M = np.array([[Wm[e1[i], e1[j]] + sum(V[e1[i], k] * V[k, e1[j]] / (lamh[1] - lamh[WT[k]])
                                          for k in range(16) if WT[k] >= 2) for j in range(4)] for i in range(4)])
    ev = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))[::-1]
    return A + ev[0] + ev[1]


def main():
    out = {"tool": "reviewer-float-sanity-v1.py", "seed": SEED, "numpy": np.__version__,
           "python": sys.version.split()[0], "nonexact": True}
    # F1 tube bound (27): R3 - K3(Lam rho) >= t eta^2/32 for psi = sqrt(1-eta^2)|0> + eta v
    ratios = []
    refl_dev = 0.0
    for t in (1 / 200, 1 / 2000, 1 / 20000):
        for trial in range(150):
            v = rand_normal_v()
            eta = [9 / 40, 1e-3, 0.05][trial % 3] if trial < 3 else rng.uniform(1e-3, 9 / 40)
            psi = np.sqrt(1 - eta ** 2) * np.eye(16)[0] + eta * v
            rho = np.outer(psi, psi.conj())
            gap = R3(t) - k3(lam(1 - t, rho))
            ratios.append(gap / (t * eta ** 2 / 32))
            refl_dev = max(refl_dev, abs(k3(lam(1 + t, rho)) - k3(lam(1 - t, rho))))
    out["F1_tube_min_ratio_gap_over_t_eta2_div32"] = float(min(ratios))
    out["F1_samples"] = len(ratios)
    out["F1_reflection_max_abs_K3_difference_p_vs_2-p"] = refl_dev
    # F2 Hessian margin (21): (A + K2(M))/t <= -15/64
    hs = []
    for t in (1 / 200, 1 / 2000):
        for _ in range(200):
            hs.append(hessian(rand_normal_v(), t) / t)
    out["F2_max_A_plus_K2M_over_t"] = float(max(hs))
    out["F2_bound"] = -15 / 64
    out["F2_samples"] = len(hs)
    # F3 all-density sanity at t=1/200 and p=1+t: random Haar pure and structured states
    t = 1 / 200
    gaps = []
    structured = []
    ghz = np.zeros(16, dtype=complex); ghz[0] = ghz[15] = 1 / np.sqrt(2); structured.append(ghz)
    wst = np.zeros(16, dtype=complex); wst[[8, 4, 2, 1]] = 0.5; structured.append(wst)
    d2 = np.array([1.0 if WT[x] == 2 else 0 for x in range(16)], dtype=complex); structured.append(d2 / np.linalg.norm(d2))
    cl = np.array([(-1) ** (((x >> 3) & (x >> 2) & 1) + ((x >> 2) & (x >> 1) & 1) + ((x >> 1) & x & 1))
                   for x in range(16)], dtype=complex) / 4; structured.append(cl)
    prod = np.zeros(16, dtype=complex); prod[0] = 1; structured.append(prod)
    for _ in range(400):
        z = rng.normal(size=16) + 1j * rng.normal(size=16)
        structured.append(z / np.linalg.norm(z))
    for psi in structured:
        rho = np.outer(psi, psi.conj())
        for p in (1 - t, 1 + t):
            gaps.append(R3(t) - k3(lam(p, rho)))
    out["F3_min_R3_minus_K3"] = float(min(gaps))
    out["F3_samples"] = len(gaps)
    ok = (out["F1_tube_min_ratio_gap_over_t_eta2_div32"] >= 1 - 1e-6 and refl_dev < 1e-12
          and out["F2_max_A_plus_K2M_over_t"] <= -15 / 64 + 1e-9 and out["F3_min_R3_minus_K3"] >= -1e-12)
    out["no_gross_contradiction_observed"] = bool(ok)
    text = json.dumps(out, indent=1) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "x", encoding="utf-8") as fh:
            fh.write(text)
    print(text)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
