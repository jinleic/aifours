"""Control: genus-2 MacWilliams self-duality f_hat = |C|^2 f on brute-force pair counts of the hexacode and the
dodecacode (exact integer arithmetic), plus a mutation control (one count perturbed must fail)."""
import json

import numpy as np

from genus2 import brute_T, orbit_to_tau, transform_row


def fhat(f, n, T):
    acc = np.zeros((n + 1,) * 4, dtype=object)
    for tau, val in f.items():
        acc = acc + val * transform_row(tau, n, T)
    return acc


if __name__ == "__main__":
    T = brute_T()
    data = json.load(open("../evidence/control_pair_counts.json"))
    res = {}
    for name in ("hexacode", "dodecacode_circulant_1_3_6"):
        n = data[name]["n"]
        lam = {tuple(map(int, k.split(","))): v for k, v in data[name]["lambda"].items()}
        f = {orbit_to_tau(o): v for o, v in lam.items()}
        C = data[name]["group_size"]
        F = fhat(f, n, T)
        ok = True
        bad = 0
        for idx in np.ndindex(F.shape):
            if sum(idx) > n:
                continue
            want = C * C * f.get(tuple(idx), 0)
            if F[idx] != want:
                ok = False
                bad += 1
        # mutation: perturb one nonzero count by +1
        tau0 = next(t for t in f if sum(t) > 0)
        g = dict(f)
        g[tau0] += 1
        G = fhat(g, n, T)
        mut_fail = any(G[idx] != C * C * g.get(tuple(idx), 0) for idx in np.ndindex(G.shape) if sum(idx) <= n)
        res[name] = {"self_dual_identity_holds": ok, "n_bad": bad, "mutation_detected": mut_fail}
        print(name, res[name])
    json.dump(res, open("../evidence/g2_macwilliams_controls.json", "w"), indent=1)
