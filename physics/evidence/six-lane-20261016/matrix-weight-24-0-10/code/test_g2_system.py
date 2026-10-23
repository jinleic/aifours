"""Positive controls for the genus-2 linear system: hexacode (n=6, d=4) and dodecacode (n=12, d=6).
The actual pair counts must satisfy the system; if the solution is unique it must equal them (mod p)."""
import json

import numpy as np

from g2_system import build_mod, s3key, solve_mod
from genus2 import orbit_to_tau

P = 2147483647


def residual(Mfull, b, xvec, p=P):
    acc = np.zeros(Mfull.shape[0], dtype=object)
    for c in range(Mfull.shape[1]):
        if xvec[c]:
            acc = acc + Mfull[:, c].astype(object) * int(xvec[c])
    return [(int(a) - int(bb)) % p for a, bb in zip(acc, b)]


if __name__ == "__main__":
    data = json.load(open("../evidence/control_pair_counts.json"))
    res = {}
    for name, d in (("hexacode", 4), ("dodecacode_circulant_1_3_6", 6)):
        n = data[name]["n"]
        wd = data[name]["weight_distribution"]
        allowed = set([0] + [w for w in range(d, n + 1) if w % 2 == 0])
        A = {w: wd[w] for w in range(n + 1) if wd[w]}
        Mfull, b, okeys, orbits = build_mod(P, n=n, allowed=allowed, A=A, log=lambda *a: None)
        rank, cons, x, free = solve_mod(Mfull, b, P)
        lam = {tuple(map(int, k.split(","))): v for k, v in data[name]["lambda"].items()}
        actual = {}
        for o, v in lam.items():
            actual.setdefault(s3key(orbit_to_tau(o)), set()).add(v)
        sym_ok = all(len(v) == 1 for v in actual.values())
        support_ok = all(k in set(okeys) for k in actual)
        xa = [next(iter(actual.get(k, {0}))) for k in okeys]
        resid = residual(Mfull, b, xa)
        match = None
        if len(free) == 0:
            match = all(int(x[c]) == xa[c] % P for c in range(len(okeys)))
        res[name] = {"n": n, "unknown_orbits": len(okeys), "rank": rank, "consistent": bool(cons),
                     "solution_dim": len(okeys) - rank, "actual_S3_symmetric": sym_ok,
                     "actual_support_within_allowed": support_ok, "unique_solution_equals_actual": match,
                     "actual_satisfies_system": not any(resid)}
        print(name, res[name])
    json.dump(res, open("../evidence/g2_system_controls.json", "w"), indent=1)
