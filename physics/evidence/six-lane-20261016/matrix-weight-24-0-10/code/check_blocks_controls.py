"""Control for the exact AMH-block pipeline: actual pair counts of hexacode / dodecacode / [[5,1,3]]-stabilizer
must give PSD Terwilliger blocks (Gamma = 1_S 1_S^T is PSD). Uses the same alpha_exact formula with general n.
Also reports the identity-orbit check (block of the identity orbit vector must be positive diagonal)."""
import json
from fractions import Fraction

import numpy as np

from terwilliger import C, beta, blocks_index, gamma


def alpha_exact_n(i, j, t, p, a, k, n, q=4):
    b = beta(n - a, t - a, i - a, j - a, k - a)
    if b == 0:
        return 0.0
    s = 0
    for g in range(0, p + 1):
        s += (-1) ** ((a - g) % 2) * C(a, g) * C(t - a, p - g) * (q - 2) ** (t - a - p + g)
    return float(b * s) * (q - 1) ** ((i + j) / 2.0 - t)


def blocks_from_lambda(lam, n):
    x = {o: v / gamma(*o, n) for o, v in lam.items()}
    mins = []
    for (a, k) in blocks_index(n):
        idx = list(range(k, n + a - k + 1))
        m = len(idx)
        B = np.zeros((m, m))
        Did = np.zeros(m)
        for r, i in enumerate(idx):
            for cc, j in enumerate(idx):
                for t in range(min(i, j) + 1):
                    for p in range(t + 1):
                        o = (i, j, t, p)
                        if o in x:
                            B[r, cc] += alpha_exact_n(i, j, t, p, a, k, n) * x[o]
            Did[r] = alpha_exact_n(i, i, i, i, a, k, n)
        Dm = 1.0 / np.sqrt(np.abs(Did))
        Bn = Dm[:, None] * B * Dm[None, :]
        mins.append(((a, k), float(np.linalg.eigvalsh((Bn + Bn.T) / 2).min()), bool((Did > 0).all())))
    return mins


if __name__ == "__main__":
    data = json.load(open("../evidence/control_pair_counts.json"))
    out = {}
    for name in data:
        n = data[name]["n"]
        lam = {tuple(map(int, k.split(","))): v for k, v in data[name]["lambda"].items()}
        if name == "five_qubit_stabilizer":
            pass
        mins = blocks_from_lambda(lam, n)
        worst = min(mins, key=lambda r: r[1])
        out[name] = {"worst_block": worst, "all_identity_diag_positive": all(m[2] for m in mins)}
        print(name, out[name])
    json.dump(out, open("../evidence/blocks_controls.json", "w"), indent=1)
