"""EXPLORATORY screen (numerics = evidence only, no claims): can the balanced 4-colouring second moment reach d = 8?

Exact exponent of |T(M)|/|P_{n,d}| per n (KPW (3.4) before Lemma 5's relaxation), derived in
review/D8_SCREEN.md, for k = 4:
    Psi_d(M) = (1 - d/2) ln k + (d/2) ln d + ((d-1)/k) sum m ln m - (1/k) min_{l in L(M)} sum_{unordered e} l_e ln l_e,
where L(M) = {l >= 0 on edges e = {(p,q),(r,s)} with p != r, q != s : sum_{e ∋ (p,q)} l_e = d m_pq for all (p,q)}.
The inner problem is solved through its concave dual
    g(lam) = sum_v c_v lam_v - sum_{e=uv} exp(lam_u + lam_v),   c_v = d m_v,
so min sum l ln l = max g + sum c / 2 = sum_v c_v lam*_v at the optimum (l_e = x_u x_v, x = exp(lam)).
Weak duality: Psi_d(M) <= U_lam(M) for EVERY lam (used in the certification plan).
KPW's relaxed exponent is ln k + phi_d(M) >= Psi_d(M), with equality at J.

Outputs: ../evidence/explore_exact_exponent.json (floats; evidence only). Single-threaded; finite loops only.
Run: OMP_NUM_THREADS=1 python -B explore_exact_exponent.py
"""
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

K = 4
CELLS = [(p, q) for p in range(K) for q in range(K)]
ADJ = np.array([[1.0 if (u[0] != v[0] and u[1] != v[1]) else 0.0 for v in CELLS] for u in CELLS])
J = np.full((K, K), 1.0 / K)


def solve_dual(m, d, tol=1e-13, maxit=200):
    """Return (lam, x, ok) maximising g on the support of m (cells with m > 1e-15)."""
    mv = m.reshape(-1)
    S = np.where(mv > 1e-15)[0]
    A = ADJ[np.ix_(S, S)]
    c = d * mv[S]
    x = np.sqrt(c / np.maximum(A.sum(axis=1), 1e-300))
    lam = np.log(x)
    ok = False
    for _ in range(maxit):
        x = np.exp(lam)
        Ax = A @ x
        grad = c - x * Ax
        if np.max(np.abs(grad)) < tol:
            ok = True
            break
        H = -(np.diag(x * Ax) + (x[:, None] * A * x[None, :]))
        try:
            step = np.linalg.solve(H, -grad)
        except np.linalg.LinAlgError:
            break
        g0 = c @ lam - 0.5 * x @ Ax
        t = 1.0
        while t > 1e-12:
            lam_n = lam + t * step
            xn = np.exp(lam_n)
            if c @ lam_n - 0.5 * xn @ (A @ xn) >= g0 - 1e-15:
                break
            t *= 0.5
        lam = lam + t * step
    lam_full = np.full(K * K, -np.inf)
    lam_full[S] = lam
    return lam_full, S, ok


def psi_exact(m, d):
    lam, S, ok = solve_dual(m, d)
    mv = m.reshape(-1)
    ent = sum(v * math.log(v) for v in mv if v > 0)
    inner = float(np.sum(d * mv[S] * lam[S]))
    val = (1 - d / 2) * math.log(K) + (d / 2) * math.log(d) + (d - 1) / K * ent - inner / K
    return val, lam, ok


def grad_exact(m, d, lam):
    mv = m.reshape(-1)
    g = np.zeros(K * K)
    for i, v in enumerate(mv):
        g[i] = (d - 1) / K * (math.log(max(v, 1e-300)) + 1) - d / K * lam[i] if v > 0 else 1e3
    return g


def relaxed(m, d):
    mv = m.reshape(-1)
    ent = sum(v * math.log(v) for v in mv if v > 0)
    rho = float(np.sum(mv * mv))
    return math.log(K) - ent / K + d / 2 * math.log(1 - 2 / K + rho / K ** 2)


def centre_value(d):
    return (2 - d) * math.log(K) + d * math.log(K - 1)


def sinkhorn(M, it=500):
    for _ in range(it):
        M = M / M.sum(axis=1, keepdims=True)
        M = M / M.sum(axis=0, keepdims=True)
    return M


def family(P, t):
    return (1 - t) * J + t * P


def local_max(m0, d):
    """SLSQP maximisation of Psi_d over the Birkhoff polytope (16 vars, 7 independent equalities, bounds)."""
    cons = []
    for p in range(K):
        cons.append({"type": "eq", "fun": (lambda z, p=p: z.reshape(K, K)[p, :].sum() - 1.0),
                     "jac": (lambda z, p=p: np.eye(K)[p].repeat(K) * 1.0)})
    for q in range(K - 1):
        cons.append({"type": "eq", "fun": (lambda z, q=q: z.reshape(K, K)[:, q].sum() - 1.0),
                     "jac": (lambda z, q=q: np.tile(np.eye(K)[q], K) * 1.0)})

    def f(z):
        M = np.clip(z.reshape(K, K), 1e-14, None)
        val, lam, ok = psi_exact(M, d)
        return -val

    def fg(z):
        M = np.clip(z.reshape(K, K), 1e-14, None)
        val, lam, ok = psi_exact(M, d)
        return -grad_exact(M, d, lam)

    res = minimize(f, m0.reshape(-1), jac=fg, method="SLSQP", bounds=[(1e-12, 1.0)] * (K * K),
                   constraints=cons, options={"maxiter": 400, "ftol": 1e-14})
    M = np.clip(res.x.reshape(K, K), 1e-14, None)
    M = sinkhorn(M, 50)
    val, lam, ok = psi_exact(M, d)
    return M, val, ok, res.success


def main():
    t0 = time.time()
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim."}
    # --- 1. consistency checks
    chk = {}
    for d in (7, 8, 9):
        v, lam, ok = psi_exact(J, d)
        chk[f"d={d} Psi(J) - closed form"] = v - centre_value(d)
        chk[f"d={d} relaxed(J) - closed form"] = relaxed(J, d) - centre_value(d)
    # Hessian at J along random tangent directions vs theory -(10-d)/10 * |a|^2 (i.e. coefficient (10-d)/20)
    rng = np.random.default_rng(8)
    hess = {}
    for d in (7, 8, 9):
        ratios = []
        for _ in range(5):
            a = rng.normal(size=(K, K))
            a -= a.mean(axis=1, keepdims=True)
            a -= a.mean(axis=0, keepdims=True)
            a /= np.linalg.norm(a)
            e = 1e-3
            vp = psi_exact(J + e * a, d)[0]
            vm = psi_exact(J - e * a, d)[0]
            v0 = psi_exact(J, d)[0]
            ratios.append((vp + vm - 2 * v0) / (2 * e * e))  # = coefficient c in Psi ~ Psi(J) + c |a|^2
        hess[f"d={d}"] = {"numeric coefficients": ratios, "theory -(k^2-2k-d+2)/(2(k^2-2k+2))": -(10 - d) / 20}
    chk["Hessian at J"] = hess
    # exact <= relaxed at random points
    worst = -1e9
    for _ in range(300):
        M = sinkhorn(np.exp(rng.normal(scale=2.0, size=(K, K))))
        for d in (7, 8, 9):
            worst = max(worst, psi_exact(M, d)[0] - relaxed(M, d))
    chk["max over 900 random (Psi - relaxed) (must be <= 0)"] = worst
    out["checks"] = chk
    # --- 2. families
    I = np.eye(K)
    fams = {
        "M_t=(1-t)J+tI": I,
        "one aligned: P=1(+)J3/3": np.block([[np.ones((1, 1)), np.zeros((1, 3))], [np.zeros((3, 1)), np.full((3, 3), 1 / 3)]]),
        "two aligned: P=I2(+)J2/2": np.block([[np.eye(2), np.zeros((2, 2))], [np.zeros((2, 2)), np.full((2, 2), 0.5)]]),
        "2+2 blocks: P=J2/2(+)J2/2": np.block([[np.full((2, 2), 0.5), np.zeros((2, 2))], [np.zeros((2, 2)), np.full((2, 2), 0.5)]]),
        "transposition-ish: P=perm(1032)": np.eye(K)[[1, 0, 3, 2]],
    }
    famres = {}
    for name, P in fams.items():
        rows = {}
        for d in (7, 8, 9, 10):
            best_rel, best_ex = (-1e9, None), (-1e9, None)
            worst_norm = 1e9
            tmin = -1 / 3 if name.startswith("M_t") else 0.0
            for t in np.linspace(tmin, 0.999, 400):
                if abs(t) < 1e-9:
                    continue
                M = family(P, t)
                if M.min() < -1e-12:
                    continue
                M = np.clip(M, 0, None)
                ex = psi_exact(M, d)[0] - centre_value(d)
                rl = relaxed(M, d) - centre_value(d)
                nrm = float(np.sum((M - J) ** 2))
                if ex > best_ex[0]:
                    best_ex = (ex, float(t))
                if rl > best_rel[0]:
                    best_rel = (rl, float(t))
                worst_norm = min(worst_norm, -ex / nrm)
            rows[f"d={d}"] = {"max exact Psi - Psi(J) [value, t]": best_ex, "max relaxed - centre [value, t]": best_rel,
                              "min normalised exact margin (Psi(J)-Psi)/|M-J|^2": worst_norm}
        famres[name] = rows
    out["families"] = famres
    # specific point M=(J+I)/2
    Mh = family(I, 0.5)
    out["M=(J+I)/2"] = {f"d={d}": {"exact - centre": psi_exact(Mh, d)[0] - centre_value(d),
                                   "relaxed - centre": relaxed(Mh, d) - centre_value(d)} for d in (7, 8, 9)}
    # --- 3. multistart over B_4
    ms = {}
    for d in (8, 9):
        found = []
        starts = 0
        for s in range(160):
            kind = s % 4
            if kind == 0:
                M0 = sinkhorn(np.exp(rng.normal(scale=rng.choice([0.5, 1, 2, 4]), size=(K, K))))
            elif kind == 1:
                perm = rng.permutation(K)
                M0 = family(np.eye(K)[perm], rng.uniform(0.2, 0.95))
            elif kind == 2:
                w = rng.dirichlet(np.ones(3))
                M0 = sum(wi * np.eye(K)[rng.permutation(K)] for wi in w)
                M0 = 0.9 * M0 + 0.1 * J
            else:
                M0 = sinkhorn(np.exp(rng.normal(scale=6.0, size=(K, K))))
            starts += 1
            M, val, ok, succ = local_max(M0, d)
            nrm = float(np.sum((M - J) ** 2))
            found.append((val - centre_value(d), nrm, ok, succ, M.round(4).tolist()))
        found.sort(key=lambda r: -r[0])
        noncentre = [r for r in found if r[1] > 1e-6]
        ms[f"d={d}"] = {
            "starts": starts,
            "best Psi - Psi(J) over all local maxima": found[0][0],
            "best non-centre local maximum (Psi-Psi(J), |M-J|^2, dual ok, slsqp ok, M)": noncentre[0] if noncentre else None,
            "number of runs ending at the centre (|M-J|^2 <= 1e-6)": len(found) - len(noncentre),
            "top 5 (value, |M-J|^2)": [(r[0], r[1]) for r in found[:5]],
        }
    out["multistart"] = ms
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_exact_exponent.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
