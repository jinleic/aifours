"""Float survey (evidence only): classify maximal-overlap normal forms of dual unitaries into the cases of
review/LEMMA_R_NORMAL_FORM.md:
  G  : (dim A = 3 or dim B = 3) and (dim C = 3 or dim D = 3)      [Theorem G applies]
  S  : some corner N_0 or R_0 has operator norm 1                  [splitting lemma applies]
  R* : neither (remaining case); records whether the point is 2-unitary (AME)
Usage: python -B nf_case_survey.py SEED NPTS OUTJSONL
"""
import json
import os
import sys

import numpy as np
from scipy.optimize import least_squares, minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gates as g  # noqa: E402
import numcore as nc  # noqa: E402
from ascent import descend, gn_project  # noqa: E402


def unpack(x):
    return x[0:3] + 1j * x[3:6], x[6:9] + 1j * x[9:12]


def ent(x, U):
    a, b = unpack(x)
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    s = np.linalg.svd((U @ np.kron(a, b)).reshape(3, 3), compute_uv=False)
    return 1 - s[0] ** 2


def minors(x, U):
    a, b = unpack(x)
    o = (U @ np.kron(a, b)).reshape(3, 3)
    r = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        for (k, l) in [(0, 1), (0, 2), (1, 2)]:
            m = o[i, k] * o[j, l] - o[i, l] * o[j, k]
            r += [m.real, m.imag]
    r += [np.linalg.norm(a) ** 2 - 1, np.linalg.norm(b) ** 2 - 1, a[0].imag, b[0].imag]
    return np.array(r)


def complete(v):
    Mm = np.eye(3, dtype=complex)
    Mm[:, 0] = v
    Q, _ = np.linalg.qr(Mm)
    Q[:, 0] *= np.vdot(Q[:, 0], v)
    return Q


def normal_forms(U, rng, tries):
    out, seen = [], []
    for _ in range(tries):
        r = minimize(ent, rng.standard_normal(12), args=(U,), method="BFGS", options={"gtol": 1e-12})
        if r.fun > 1e-9:
            continue
        a, b = unpack(r.x)
        a = a / np.linalg.norm(a) * np.exp(-1j * np.angle(a[0]))
        b = b / np.linalg.norm(b) * np.exp(-1j * np.angle(b[0]))
        ls = least_squares(minors, np.concatenate([a.real, a.imag, b.real, b.imag]), args=(U,), xtol=1e-15,
                           ftol=1e-15, gtol=1e-15, method="lm")
        a, b = unpack(ls.x)
        a /= np.linalg.norm(a)
        b /= np.linalg.norm(b)
        v = np.kron(a, b)
        if any(abs(abs(np.vdot(v, w)) - 1) < 1e-6 for w in seen):
            continue
        seen.append(v)
        o = (U @ v).reshape(3, 3)
        W, s, Vh = np.linalg.svd(o)
        if s[1] > 1e-10:
            continue
        out.append(np.kron(complete(W[:, 0]), complete(Vh[0])).conj().T @ U @ np.kron(complete(a), complete(b)))
    return out


def rk(vs, tol=1e-8):
    return int((np.linalg.svd(np.array([v.ravel() for v in vs]), compute_uv=False) > tol).sum())


def classify(U1):
    phi = U1.reshape(3, 3, 3, 3).transpose(2, 3, 0, 1)
    N = [phi[0, 1:, 1:, d] for d in range(3)]
    Q = [phi[a, 1:, 1:, 0] for a in range(3)]
    R = [phi[1:, 0, c, 1:] for c in range(3)]
    T = [phi[1:, b, 0, 1:] for b in range(3)]
    dA, dB, dC, dD = rk(N), rk(Q), rk(R), rk(T)
    n0, r0 = np.linalg.norm(N[0], 2), np.linalg.norm(R[0], 2)
    if (dA == 3 or dB == 3) and (dC == 3 or dD == 3):
        case = "G"
    elif n0 > 1 - 1e-7 or r0 > 1 - 1e-7:
        case = "S"
    else:
        case = "R*"
    return case, (dA, dB, dC, dD), float(n0), float(r0)


def main():
    seed, npts, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = np.random.default_rng(seed)
    S = np.array(g.swap(), dtype=complex)
    with open(out, "a") as fo:
        for t in range(npts):
            kind = ["mr", "mr-ascent", "controlled", "Sdiag", "Us-theta", "P9"][t % 6]
            if kind == "mr":
                U = nc.mr_map(nc.haar(9, rng), iters=3000, tol=1e-10)[0]
            elif kind == "mr-ascent":
                U = nc.mr_map(nc.haar(9, rng), iters=3000, tol=1e-10)[0]
                U = descend(U, steps=300)[0]
            elif kind == "controlled":
                C = np.zeros((9, 9), complex)
                for a in range(3):
                    C[3 * a:3 * a + 3, 3 * a:3 * a + 3] = nc.haar(3, rng)
                U = S @ C
            elif kind == "Sdiag":
                U = S @ np.diag(np.exp(2j * np.pi * rng.random(9)))
            elif kind == "Us-theta":
                th = rng.uniform(0, 2 * np.pi)
                U = S @ np.array(g.U36(np.cos(th), np.sin(th)), dtype=complex)
            else:
                v = [nc.haar(3, rng) for _ in range(4)]
                U = np.kron(v[0], v[1]) @ np.array(g.P9(), dtype=complex) @ np.kron(v[2], v[3])
            U, res, _ = gn_project(U, tol=1e-13)
            if res > 1e-11:
                continue
            sv = np.linalg.svd(nc.G(U), compute_uv=False)
            rkG = int((sv > 1e-7).sum())
            ep = float(nc.ep(U))
            cases = {}
            rstar_non_ame = []
            for U1 in normal_forms(U, rng, 40):
                c, dims, n0, r0 = classify(U1)
                cases[c] = cases.get(c, 0) + 1
                if c == "R*" and ep < 1 - 1e-9:
                    rstar_non_ame.append({"dims": dims, "n0": n0, "r0": r0})
            rec = dict(seed=seed, t=t, kind=kind, ep=ep, rank_UG=rkG, cases=cases, rstar_non_ame=rstar_non_ame[:5])
            fo.write(json.dumps(rec) + "\n")
            fo.flush()
            print(t, kind, "rank", rkG, "ep", round(ep, 4), cases, "R*nonAME", len(rstar_non_ame), flush=True)


if __name__ == "__main__":
    main()
