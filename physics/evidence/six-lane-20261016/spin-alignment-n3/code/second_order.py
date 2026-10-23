"""Second-order expansion of K_k(X) - K_k(Y) around the aligned state |000> (Song-Chen Conjecture 2, n=3, d=2).

psi = |000> + eps*phi with phi _|_ |000> (phi in C^7 <-> v in R^14). Then X = Y + eps X1 + eps^2 X2 + O(eps^3) with
X1 = M(|phi><0| + |0><phi|) (zero diagonal), X2 = M(|phi><phi|) - |phi|^2 Y, M = sum_I mu_I Tr_{I^c}(.) (x) Q^{I^c}.
If y_(k) > y_(k+1) (top-k set S of the diagonal Y):
   K_k(X) - K_k(Y) = eps^2 G_k(phi) + O(eps^3),
   G_k(phi) = Tr(P_S X2) + sum_{i in S, j notin S} |X1_ij|^2 / (y_i - y_j).
If y has a tie across the cut, the first-order term is eps * K_r(X1 restricted to the tied block) (r = slots of the
block inside the top k); it is > 0 iff that compression is nonzero.
This script: H_k = Hessian of the real quadratic form G_k on R^14; reports max eigenvalue over k and scans (mu, q).
"""
import json
import sys

import numpy as np

from search import SUBSETS, embed


def Mmap(R, mu, q):
    Q = np.diag([q, 1 - q])
    out = np.zeros((8, 8), dtype=complex)
    T = R.reshape([2] * 6)
    for m, I in zip(mu, SUBSETS):
        if m == 0:
            continue
        rest = [l for l in range(3) if l not in I]
        # partial trace over rest of an operator R on 3 qubits (ket axes 0..2, bra axes 3..5)
        A = T
        for l in sorted(rest, reverse=True):
            A = np.trace(A, axis1=l, axis2=l + A.ndim // 2)
        d = 2 ** len(I)
        out += m * embed(A.reshape(d, d), I, Q)
    return out


def Ydiag(mu, q):
    return np.real(np.diag(Mmap(np.diag([1.0] + [0.0] * 7), mu, q)))


def G_value(v, mu, q, k, y=None, order=None):
    phi = np.zeros(8, dtype=complex)
    phi[1:] = v[:7] + 1j * v[7:]
    e0 = np.zeros(8); e0[0] = 1
    X1 = Mmap(np.outer(phi, e0) + np.outer(e0, phi.conj()), mu, q)
    X2 = Mmap(np.outer(phi, phi.conj()), mu, q) - np.vdot(phi, phi).real * np.diag(y)
    S, notS = order[:k], order[k:]
    val = np.real(np.trace(X2[np.ix_(S, S)]))
    for i in S:
        for j in notS:
            val += abs(X1[i, j]) ** 2 / (y[i] - y[j])
    return val


def hessian_max(mu, q, k):
    y = Ydiag(mu, q)
    order = list(np.argsort(-y, kind="stable"))
    ys = y[order]
    if ys[k - 1] - ys[k] < 1e-12:
        return None, "tie"
    E = np.eye(14)
    g = np.array([G_value(E[m], mu, q, k, y, order) for m in range(14)])
    H = np.zeros((14, 14))
    for a in range(14):
        H[a, a] = g[a]
        for b in range(a + 1, 14):
            H[a, b] = H[b, a] = (G_value(E[a] + E[b], mu, q, k, y, order) - g[a] - g[b]) / 2
    ev, evec = np.linalg.eigh(H)
    return ev[-1], evec[:, -1]


def tie_first_order(mu, q, k, trials=20, rng=None):
    """Max over random phi of K_r(X1|block) when the cut falls inside a tie of y (first-order term)."""
    y = Ydiag(mu, q)
    order = list(np.argsort(-y, kind="stable"))
    ys = y[order]
    yk = ys[k - 1]
    block = [i for i in range(8) if abs(y[i] - yk) < 1e-12]
    r = sum(1 for i in order[:k] if abs(y[i] - yk) < 1e-12)
    best = 0.0
    e0 = np.zeros(8); e0[0] = 1
    for _ in range(trials):
        phi = np.zeros(8, dtype=complex)
        phi[1:] = rng.normal(size=7) + 1j * rng.normal(size=7)
        phi /= np.linalg.norm(phi)
        X1 = Mmap(np.outer(phi, e0) + np.outer(e0, phi.conj()), mu, q)
        B = X1[np.ix_(block, block)]
        ev = np.sort(np.linalg.eigvalsh((B + B.conj().T) / 2))[::-1]
        best = max(best, float(ev[:r].sum()))
    return best, block, r


if __name__ == "__main__":
    n, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    worst = {"hmax": -np.inf}
    ties = {"first_order_max": 0.0}
    for s in range(n):
        mu = rng.dirichlet(np.ones(8) * (0.3 if s % 2 else 1.0))
        q = 0.5 + 0.5 * rng.random()
        for k in range(1, 8):
            h, info = hessian_max(mu, q, k)
            if h is None:
                fo, block, r = tie_first_order(mu, q, k, rng=rng)
                if fo > ties["first_order_max"]:
                    ties = {"first_order_max": fo, "mu": mu.tolist(), "q": q, "k": k, "block": block, "r": r}
                continue
            if h > worst["hmax"]:
                worst = {"hmax": float(h), "k": k, "mu": mu.tolist(), "q": q, "direction": info.tolist()}
    print(json.dumps({"samples": n, "seed": seed, "max_hessian_eig": worst, "tie_first_order": ties}))
