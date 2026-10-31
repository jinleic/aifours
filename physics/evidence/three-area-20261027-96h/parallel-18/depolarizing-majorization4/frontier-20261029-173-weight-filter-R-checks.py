#!/usr/bin/env python3
"""Checks for the four-qubit weight filter R = M_2 - M_3 (packet 174).

Floating checks are diagnostics only. The cone-membership LP and the secular
inequality use exact Fractions. Nothing here proves positivity of R.
"""

import itertools
import json
import math
from fractions import Fraction as Fr

import numpy as np

SEED = 20261029
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Yp = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [I2, X, Yp, Z]


def kron(*ops):
    out = np.array([[1.0 + 0j]])
    for op in ops:
        out = np.kron(out, op)
    return out


def pauli_string(labels):
    return kron(*[PAULI[l] for l in labels])


STRINGS = list(itertools.product(range(4), repeat=4))
YY = kron(Yp, Yp, Yp, Yp)


def marginal_embed(rho, keep):
    """rho_keep tensor identity on the complement (unnormalized identity)."""
    t = rho.reshape([2] * 8)
    cur = list(range(4))
    out = t
    for s in sorted([x for x in range(4) if x not in keep], reverse=True):
        pos = cur.index(s)
        n = len(cur)
        out = np.trace(out, axis1=pos, axis2=pos + n)
        cur.pop(pos)
    k = len(cur)
    marg = out.reshape(2 ** k, 2 ** k)
    full = np.zeros((16, 16), dtype=complex)
    for x in range(16):
        bx = [(x >> (3 - j)) & 1 for j in range(4)]
        for y in range(16):
            by = [(y >> (3 - j)) & 1 for j in range(4)]
            if any(bx[j] != by[j] for j in range(4) if j not in keep):
                continue
            ix = int("".join(str(bx[j]) for j in keep), 2) if k else 0
            iy = int("".join(str(by[j]) for j in keep), 2) if k else 0
            full[x, y] = marg[ix, iy]
    return full


def M_k(rho, k):
    return sum(marginal_embed(rho, list(S)) for S in itertools.combinations(range(4), k))


def R_map(rho):
    return M_k(rho, 2) - M_k(rho, 3)


def random_state(rng):
    v = rng.normal(size=16) + 1j * rng.normal(size=16)
    return v / np.linalg.norm(v)


def bloch(v):
    out = []
    for i in range(4):
        r = []
        for a in (1, 2, 3):
            lab = [0, 0, 0, 0]
            lab[i] = a
            r.append(np.vdot(v, pauli_string(lab) @ v).real)
        out.append(np.array(r))
    return out


def D_op(v):
    rs = bloch(v)
    out = np.zeros((16, 16), dtype=complex)
    for i in range(4):
        for a in (1, 2, 3):
            lab = [0, 0, 0, 0]
            lab[i] = a
            out += 0.5 * rs[i][a - 1] * pauli_string(lab)
    return out


# magic basis (columns): (|00>+|11>)/sqrt2, i(|00>-|11>)/sqrt2, i(|01>+|10>)/sqrt2, (|01>-|10>)/sqrt2
MAG = np.array([[1, 0, 0, 1], [1j, 0, 0, -1j], [0, 1j, 1j, 0], [0, 1, -1, 0]], dtype=complex).T / math.sqrt(2)
MFULL = np.kron(MAG, MAG)


def T_matrix(A, B):
    Xl = A @ B.T - B @ A.T
    Yr = A.T @ B - B.T @ A
    T = np.zeros((16, 16))
    for idx in range(16):
        M = np.zeros(16)
        M[idx] = 1
        M = M.reshape(4, 4)
        out = A * np.sum(B * M) - B * np.sum(A * M) - Xl @ M + M @ Yr
        T[:, idx] = out.reshape(16)
    return T


def identity_checks(rng, count=50):
    worst = {"R_pure_form": 0.0, "spectral_symmetry": 0.0, "magic_T": 0.0,
             "odd_kramers": 0.0, "diag_value_C_plus_S_over_2": 0.0,
             "null_reduction": 0.0}
    for _ in range(count):
        v = random_state(rng)
        rho = np.outer(v, v.conj())
        vt = YY @ v.conj()
        R = R_map(rho)
        pure_form = np.eye(16) + D_op(v) + np.outer(vt, vt.conj()) - rho
        worst["R_pure_form"] = max(worst["R_pure_form"], np.abs(R - pure_form).max())
        ev = np.sort(np.linalg.eigvalsh(R))
        worst["spectral_symmetry"] = max(worst["spectral_symmetry"], np.abs(ev + ev[::-1] - 2).max())
        c = MFULL.conj().T @ v
        Psi = c.reshape(4, 4)
        Lmag = MFULL.conj().T @ (R - np.eye(16)) @ MFULL
        worst["magic_T"] = max(worst["magic_T"], np.abs(Lmag - 2j * T_matrix(Psi.real, Psi.imag)).max())
        for lab in STRINGS:
            w = sum(1 for l in lab if l)
            if w % 2 == 1:
                worst["odd_kramers"] = max(worst["odd_kramers"], abs(np.vdot(vt, pauli_string(lab) @ v)))
        S = sum(float(r @ r) for r in bloch(v))
        C = abs(np.vdot(vt, v)) ** 2
        worst["diag_value_C_plus_S_over_2"] = max(worst["diag_value_C_plus_S_over_2"],
                                                   abs(np.vdot(v, R @ v).real - (C + S / 2)))
        # null reduction: alpha-beta = sqrt(1-C)(xi xi^dag - xi~ xi~^dag), R-I scales by sqrt(1-C)
        Dlt = rho - np.outer(vt, vt.conj())
        w_, U_ = np.linalg.eigh(Dlt)
        xi = U_[:, -1]
        xit = YY @ xi.conj()
        Rxi = R_map(np.outer(xi, xi.conj()))
        worst["null_reduction"] = max(worst["null_reduction"],
                                      np.abs((R - np.eye(16)) - math.sqrt(max(0.0, 1 - C)) * (Rxi - np.eye(16))).max(),
                                      abs(np.vdot(xit, xi)))
    return {k: float(v) for k, v in worst.items()}


def lam_min(x):
    v = x[:16] + 1j * x[16:]
    v = v / np.linalg.norm(v)
    return float(np.linalg.eigvalsh(R_map(np.outer(v, v.conj())))[0])


def sharpened_gap(x):
    v = x[:16] + 1j * x[16:]
    v = v / np.linalg.norm(v)
    vt = YY @ v.conj()
    C = abs(np.vdot(vt, v)) ** 2
    return lam_min(x) - (1 - math.sqrt(max(0.0, 1 - C)))


def descend(fun, x, iters):
    val = fun(x)
    step = 0.05
    for _ in range(iters):
        g = np.zeros(32)
        h = 1e-7
        for j in range(32):
            e = np.zeros(32)
            e[j] = h
            g[j] = (fun(x + e) - val) / h
        nx = x - step * g / (np.linalg.norm(g) + 1e-15)
        nv = fun(nx)
        if nv < val:
            x, val = nx, nv
            step *= 1.2
        else:
            step *= 0.5
        if step < 1e-11:
            break
    return val


def cone_lp():
    """Exact Phase-I simplex: is f=(16,6,0,-2,0) a nonnegative combination of covariant CP, co-CP maps?"""
    def Ek(k, w):
        return sum(math.comb(w, j) * math.comb(4 - w, k - j) * Fr(-1, 2) ** j * Fr(3, 2) ** (k - j)
                   for j in range(0, k + 1) if j <= w and k - j <= 4 - w)
    cols = [[Ek(k, w) for w in range(5)] for k in range(5)] + [[(-1) ** w * Ek(k, w) for w in range(5)] for k in range(5)]
    target = [Fr(16), Fr(6), Fr(0), Fr(-2), Fr(0)]

    def solve(A, b):
        n = len(b)
        M = [row[:] + [b[i]] for i, row in enumerate(A)]
        for c in range(n):
            piv = next((r for r in range(c, n) if M[r][c] != 0), None)
            if piv is None:
                return None
            M[c], M[piv] = M[piv], M[c]
            for r in range(n):
                if r != c and M[r][c] != 0:
                    f = M[r][c] / M[c][c]
                    M[r] = [M[r][j] - f * M[c][j] for j in range(n + 1)]
        return [M[i][n] / M[i][i] for i in range(n)]

    feasible = 0
    for basis in itertools.combinations(range(10), 5):
        A = [[cols[j][w] for j in basis] for w in range(5)]
        x = solve(A, target)
        if x is not None and all(v >= 0 for v in x):
            feasible += 1
    return {"basic_feasible_solutions": feasible, "decomposable_by_covariant_CP_plus_coCP": feasible > 0}


def range_counterexample():
    mu = [Fr(2, 5), Fr(3, 10), Fr(1, 5), Fr(1, 10)]
    x = -(mu[2] + mu[3])
    phi = sum(m / (2 * m - x) for m in mu)
    return {"mu": [str(m) for m in mu], "phi_at_minus_mu3_minus_mu4": str(phi), "phi_exceeds_one": phi > 1,
            "consequence": "lambda_min(2diag(mu)-sqrt(mu)sqrt(mu)^T) < -(mu3+mu4), so spectral range of D(chi chi^dag) exceeds mu1+mu2+mu3+mu4=1"}


def main():
    rng = np.random.default_rng(SEED)
    ids = identity_checks(rng, 40)
    mins = []
    gaps = []
    for _ in range(12):
        v = random_state(rng)
        x = np.concatenate([v.real, v.imag])
        mins.append(descend(lam_min, x, 150))
        gaps.append(descend(sharpened_gap, x, 150))
    report = {
        "scope": "floating identity residuals and bounded optimization (diagnostics only); exact LP and exact secular inequality",
        "seed": SEED,
        "identity_max_residuals": ids,
        "optimized_min_lambda_min_R": min(mins),
        "optimized_min_of_lambda_min_minus_(1-sqrt(1-C))": min(gaps),
        "exact_cone_lp": cone_lp(),
        "exact_range_lemma_failure": range_counterexample(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
