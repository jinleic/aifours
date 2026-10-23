"""Smoke checks for Part A (numpy float64 + mpmath; finite, seeded; not a proof).

S1. Sector inequality (Theorem 6 / Lemma A): for seeded random Metzler matrices of order m = 3..9 (sparse and dense,
    reducible and irreducible patterns), every non-real eigenvalue satisfies |Im| <= (s(X) - Re) cot(pi/m) + tol.
    Also: the uniform m-cycle attains equality.
S2. Why trimming matters: take the order-n* representation built from the proof formulas (mpmath, 50 digits) and
    append one UNREACHABLE state with diagonal -c/2 (slower than the dominant pole) and a positive exit. F is
    unchanged, s(T) becomes -c/2 > -c, so Theorem 6 applied to the untrimmed T is weaker; after trimming the states
    unreachable from alpha, s(T_RR) = -c again.
argv[1] = run directory; writes sector.json (exclusive create).
"""
import sys
import json
import time
import math
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
SEED = 18102026
rng = np.random.default_rng(SEED)
out = {"seed": SEED}
t_start = time.time()

# S1
worst = {}
viol = 0
count = 0
for m in range(3, 10):
    cot = 1 / math.tan(math.pi / m)
    wr = 0.0
    for trial in range(4000):
        dens = rng.choice([0.2, 0.4, 0.7, 1.0])
        X = rng.exponential(1.0, (m, m)) * (rng.random((m, m)) < dens)
        if trial % 3 == 0:  # random cyclic backbone (irreducible) with random extra arcs
            perm = rng.permutation(m)
            for k in range(m):
                X[perm[k], perm[(k + 1) % m]] += rng.exponential(1.0)
        np.fill_diagonal(X, 0.0)
        X[np.diag_indices(m)] = -rng.exponential(2.0, m) - X.sum(axis=1) * rng.random()
        ev = np.linalg.eigvals(X)
        s = ev.real.max()
        for e in ev:
            if abs(e.imag) > 1e-9:
                ratio = abs(e.imag) / max(s - e.real, 1e-300)
                wr = max(wr, ratio / cot)
                count += 1
                if abs(e.imag) > (s - e.real) * cot + 1e-7 * (1 + abs(e)):
                    viol += 1
    worst[m] = wr
cyc = {}
for m in range(3, 10):
    C = np.zeros((m, m))
    for k in range(m):
        C[k, (k + 1) % m] = 1.0
    C -= 1.5 * np.eye(m)
    ev = np.linalg.eigvals(C)
    s = ev.real.max()
    r = max(abs(e.imag) / (s - e.real) for e in ev if abs(e.imag) > 1e-12)
    cyc[m] = r * math.tan(math.pi / m)
out["S1"] = {"complex_eigenvalues_tested": count, "violations": viol,
             "max_ratio_over_cot_by_order": {str(k): round(v, 12) for k, v in worst.items()},
             "uniform_cycle_ratio_over_cot": {str(k): round(v, 12) for k, v in cyc.items()}}

# S2
mp.mp.dps = 50


def build(a, b, c):
    delta = a - c
    beta = b / delta
    n = 3
    while not (beta <= mp.cot(mp.pi / n)):
        n += 1
    phi = mp.atan(beta)
    psi = mp.pi - 2 * phi
    S = 2 * mp.pi - (n - 3) * psi
    G = lambda t: mp.sin(t + phi) * mp.sin((S - t) / 2 + phi) ** 2 - mp.sin(phi) ** 3  # noqa: E731
    lo, hi = max(mp.mpf(0), S - 2 * (mp.pi - phi)), S / 3
    if abs(G(hi)) > mp.mpf(10) ** -45:
        for _ in range(300):
            mid = (lo + hi) / 2
            lo, hi = (mid, hi) if G(mid) < 0 else (lo, mid)
    t = hi
    th = [t, (S - t) / 2, (S - t) / 2] + [psi] * (n - 3)
    m = [-beta * mp.cot(x) for x in th]
    W = mp.fprod([1 - x for x in m])
    rho = (1 + beta ** 2) / 2
    ck = [(mp.cos(psi / 2) - mp.cos((k + 1.5) * psi)) / (2 * mp.sin(psi / 2) * mp.sin(psi)) for k in range(max(n - 3, 1))]
    A, Cn = a / delta, c / delta
    K = Cn * (A ** 2 + beta ** 2)
    tx = [0, 0, K] + [K * W * rho ** (-3 - (n - j)) * ck[n - j] for j in range(4, n + 1)]
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = m[i]
    for i in range(n - 1):
        M[i, i + 1] = 1
    M[n - 1, 0] = W
    T0 = M - A * mp.eye(n)
    v = mp.lu_solve(-T0, mp.matrix(tx))
    T = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            T[i, j] = delta * T0[i, j] * v[j] / v[i]
    return T


s2 = []
for (a, b, c) in [(3, 2, 1), (2, 3, 1), (5, 30, 1)]:
    a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
    T = build(a, b, c)
    n = T.rows
    Tb = mp.zeros(n + 1, n + 1)
    for i in range(n):
        for j in range(n):
            Tb[i, j] = T[i, j]
    Tb[n, n] = -c / 2          # unreachable slow state: exit rate c/2, i.e. row sum -c/2
    Tb[n, 0] = 0
    alpha = mp.zeros(1, n + 1)
    alpha[0, 0] = 1
    ex = mp.matrix([-sum(Tb[i, j] for j in range(n + 1)) for i in range(n + 1)])
    worst_tr = mp.mpf(0)
    for s in (mp.mpc(0, 0), mp.mpc(1, 2), mp.mpc(0.5, -3)):
        X = mp.lu_solve(s * mp.eye(n + 1) - Tb, ex)
        val = sum(alpha[0, i] * X[i] for i in range(n + 1))
        F = c * (a * a + b * b) / ((s + c) * ((s + a) ** 2 + b * b))
        worst_tr = max(worst_tr, abs(val - F))
    ev_full = mp.eig(Tb, left=False, right=False)
    ev_trim = mp.eig(T, left=False, right=False)
    s_full = max(e.real for e in ev_full)
    s_trim = max(e.real for e in ev_trim)
    s2.append({"a": float(a), "b": float(b), "c": float(c), "n_star": n,
               "transform_abs_err_with_unreachable_state": mp.nstr(worst_tr, 5),
               "s_untrimmed": mp.nstr(s_full, 15), "s_trimmed": mp.nstr(s_trim, 15),
               "untrimmed_theorem6_bound_holds_but_weaker": bool(b / (a - (-s_full)) <= mp.cot(mp.pi / (n + 1))),
               "trimmed_dominant_is_minus_c": bool(abs(s_trim + c) < mp.mpf(10) ** -30)})
out["S2"] = s2
out["elapsed_seconds"] = round(time.time() - t_start, 2)
with lane_guard.xopen(RUN + "/sector.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
