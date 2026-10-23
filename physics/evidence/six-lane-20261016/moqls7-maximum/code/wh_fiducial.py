#!/usr/bin/env python3
"""wh_fiducial.py: EXPLORATION ONLY. Lane moqls7-maximum.

Translation-equivariant ONB-assignments on a Desarguesian net of order 7: psi_(a,b) = X^a Z^b psi with
X|k> = |k+1>, Z|k> = w^k |k>, w = exp(2 pi i/7). Two points differing by v = (t, s) are orthogonal iff
<psi, X^t Z^s psi> = 0. A line of direction m (int) has differences (t, m t); direction inf has (0, t).
So psi must satisfy <psi, D_v psi> = 0 for all v != 0 on the 4 direction lines, i.e. psi is unbiased to the
4 MUBs of those directions. The assignment is classical iff psi is an eigenvector of some D_v (then its orbit has
7 rays). The objective sum |<psi, D_v psi>|^2 is minimised from random starts; rays of the orbit are counted.
"""
import argparse
import json

import numpy as np
from scipy.optimize import minimize

P = 7
w = np.exp(2j * np.pi / P)
X = np.roll(np.eye(P), 1, axis=0)
Z = np.diag([w ** k for k in range(P)])


def D(t, s):
    return np.linalg.matrix_power(X, t % P) @ np.linalg.matrix_power(Z, s % P)


def diffs(dirs):
    out = []
    for d in dirs:
        for t in range(1, P):
            out.append((0, t) if d == "inf" else (t, (d * t) % P))
    return out


def run(dirs, starts, seed):
    Ds = [D(*v) for v in diffs(dirs)]

    def f(x):
        psi = x[:P] + 1j * x[P:]
        n2 = np.vdot(psi, psi).real
        val = 0.0
        g = np.zeros(P, complex)
        for Dm in Ds:
            a = np.vdot(psi, Dm @ psi)
            val += abs(a) ** 2
            # d/dconj(psi) of |a|^2 with a = psi^H D psi: conj(a) D psi + a D^H psi
            g += np.conj(a) * (Dm @ psi) + a * (Dm.conj().T @ psi)
        val += (n2 - 1) ** 2
        g += 2 * (n2 - 1) * psi
        return val, np.concatenate([2 * g.real, 2 * g.imag])
    rng = np.random.default_rng(seed)
    res_all = []
    for s in range(starts):
        r = minimize(f, rng.normal(size=2 * P), jac=True, method="L-BFGS-B",
                     options={"maxiter": 5000, "ftol": 1e-30, "gtol": 1e-14})
        psi = r.x[:P] + 1j * r.x[P:]
        psi /= np.linalg.norm(psi)
        orbit = [D(a, b) @ psi for a in range(P) for b in range(P)]
        reps = []
        for v in orbit:
            if not any(abs(abs(np.vdot(u, v)) - 1) < 1e-6 for u in reps):
                reps.append(v)
        eig = any(abs(abs(np.vdot(psi, D(t, s2) @ psi)) - 1) < 1e-6 for t in range(P) for s2 in range(P)
                  if (t, s2) != (0, 0))
        res_all.append({"start": s, "f": r.fun, "orbit_rays": len(reps), "eigvec_of_some_D": eig})
        print(json.dumps(res_all[-1]), flush=True)
    return res_all


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs")
    ap.add_argument("--starts", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    run([d if d == "inf" else int(d) for d in a.dirs.split(",")], a.starts, a.seed)
