"""Independent high-precision float route, VERSION 2 (mpmath, 150 digits) -- separate code path from ph3lib_v1.

v2 change log: v1 (60 digits) aborted in run f01-mpmath with mpmath's "matrix is numerically singular" in
lu_solve(-T0, t). mpmath's LU rejects pivots <= eps * ||A||_1; for n* near 40 the closing weight
W = prod(1 - m_i) ~ rho^(n-3) exceeds 1e70, so the threshold exceeded O(1) pivots of a nonsingular matrix
(the ball-arithmetic route b02 handled n = 64). v2 raises precision to 150 digits and caps beta at 10 (n* <= 32);
the seed and everything else are unchanged. v1 and its failed run stay as they are.

Re-implements Part B of proof/ph3-theorem-v1.md directly from its formulas, in ORIGINAL units, for
(1) a seeded random sweep of (a, b, c) and (2) boundary-adjacent parameters; then checks the PH definition,
the spectrum (mp.eig), the transform at seeded random complex points, the mean (alpha (-T)^-1 1 = 1/c + 2a/(a^2+b^2)),
and density nonnegativity at sample times (mp.expm) for a subset. Floating smoke only, not a proof.
argv[1] = run directory; writes mpmath.json (exclusive create).
"""
import sys
import json
import time
import random
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
mp.mp.dps = 150  # v2: v1 (60 digits) aborted in run f01-mpmath, see below
SEED = 20261018
rng = random.Random(SEED)
TOL = mp.mpf(10) ** -40


def nstar(a, b, c):
    beta = b / (a - c)
    n = 3
    while not (beta <= mp.cot(mp.pi / n)):
        n += 1
    return n


def build(a, b, c):
    """Part B in original units. Returns (alpha, T, info)."""
    delta = a - c
    beta = b / delta
    n = nstar(a, b, c)
    phi = mp.atan(beta)
    psi = mp.pi - 2 * phi
    S = 2 * mp.pi - (n - 3) * psi

    def G(t):
        return mp.sin(t + phi) * mp.sin((S - t) / 2 + phi) ** 2 - mp.sin(phi) ** 3

    t0 = max(mp.mpf(0), S - 2 * (mp.pi - phi))
    hi = S / 3
    if abs(G(hi)) < mp.mpf(10) ** -55:
        t = hi
    else:
        lo = t0
        assert G(lo) < 0 < G(hi), ("bracket", n, G(lo), G(hi))
        for _ in range(400):  # plain bisection, own implementation
            mid = (lo + hi) / 2
            if G(mid) < 0:
                lo = mid
            else:
                hi = mid
        t = (lo + hi) / 2
    th = [t, (S - t) / 2, (S - t) / 2] + [psi] * (n - 3)
    assert all(0 < x < mp.pi - phi for x in th)
    m = [-beta * mp.cot(x) for x in th]
    W = mp.fprod([1 - x for x in m])
    rho = (1 + beta ** 2) / 2
    ck = [(mp.cos(psi / 2) - mp.cos((k + mp.mpf(3) / 2) * psi)) / (2 * mp.sin(psi / 2) * mp.sin(psi)) for k in range(max(n - 3, 1))]
    A = a / delta
    C = c / delta
    K = C * (A ** 2 + beta ** 2)
    t_exit = [mp.mpf(0), mp.mpf(0), K] + [K * W * rho ** (-3 - (n - j)) * ck[n - j] for j in range(4, n + 1)]
    M = mp.zeros(n, n)
    for i in range(n):
        M[i, i] = m[i]
    for i in range(n - 1):
        M[i, i + 1] = 1
    M[n - 1, 0] = W
    T0 = M - A * mp.eye(n)
    v = mp.lu_solve(-T0, mp.matrix(t_exit))
    T = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            T[i, j] = delta * T0[i, j] * v[j] / v[i]
    alpha = mp.zeros(1, n)
    alpha[0, 0] = 1
    info = {"n": n, "beta": mp.nstr(beta, 20), "t": mp.nstr(t, 20), "v1": mp.nstr(v[0], 30),
            "min_v": mp.nstr(min(v), 10), "min_exit_pos": mp.nstr(min(t_exit[2:]), 10)}
    return alpha, T, info


def check(alpha, T, a, b, c, density=False):
    n = T.rows
    r = {}
    r["alpha_ok"] = all(alpha[0, i] >= 0 for i in range(n)) and abs(sum(alpha[0, i] for i in range(n)) - 1) < TOL
    r["metzler"] = all(T[i, j] >= 0 for i in range(n) for j in range(n) if i != j)
    scale = max(abs(T[i, i]) for i in range(n))
    rows = [sum(T[i, j] for j in range(n)) for i in range(n)]
    r["rowsum_le_0"] = all(rs <= TOL * scale for rs in rows)
    ev = mp.eig(T, left=False, right=False)
    r["max_re_eig"] = mp.nstr(max(e.real for e in ev), 15)
    r["hurwitz"] = max(e.real for e in ev) < 0
    r["poles_in_spectrum"] = all(min(abs(e - p) for e in ev) < mp.mpf(10) ** -25 * max(1, abs(p))
                                 for p in (mp.mpc(-c, 0), mp.mpc(-a, b), mp.mpc(-a, -b)))
    r["dominant_is_minus_c"] = abs(max(ev, key=lambda e: e.real) + c) < mp.mpf(10) ** -25 * max(1, c)
    exitv = mp.matrix([-rs for rs in rows])
    worst = mp.mpf(0)
    for _ in range(8):
        s = mp.mpc(rng.uniform(-0.5, 3) * c, rng.uniform(-3, 3) * (a + b))
        X = mp.lu_solve(s * mp.eye(n) - T, exitv)
        val = sum(alpha[0, i] * X[i] for i in range(n))
        F = c * (a * a + b * b) / ((s + c) * ((s + a) ** 2 + b * b))
        worst = max(worst, abs(val - F) / max(abs(F), mp.mpf(10) ** -30))
    r["transform_rel_err"] = mp.nstr(worst, 5)
    r["transform_ok"] = worst < mp.mpf(10) ** -30
    ones = mp.matrix([1] * n)
    mean = sum(alpha[0, i] * mp.lu_solve(-T, ones)[i] for i in range(n))
    mean_true = 1 / c + 2 * a / (a * a + b * b)
    r["mean_rel_err"] = mp.nstr(abs(mean - mean_true) / mean_true, 5)
    r["mean_ok"] = abs(mean - mean_true) / mean_true < mp.mpf(10) ** -30
    if density:
        mn = mp.inf
        for k in range(1, 9):
            tt = mp.mpf(k) / (2 * (a + b))
            dens = (alpha * mp.expm(T * tt) * exitv)[0, 0]
            mn = min(mn, dens)
        r["density_min_sampled"] = mp.nstr(mn, 10)
        r["density_nonneg"] = mn >= -mp.mpf(10) ** -40
    r["OK"] = all(r[k] for k in ("alpha_ok", "metzler", "rowsum_le_0", "hurwitz", "poles_in_spectrum",
                                 "dominant_is_minus_c", "transform_ok", "mean_ok")) and r.get("density_nonneg", True)
    return r


t_start = time.time()
recs = []
# (1) random sweep: c, a-c log-uniform in [1e-3, 1e3]; beta log-uniform in [1e-2, 10] (n* <= 32)
for k in range(160):
    c = mp.mpf(10) ** rng.uniform(-3, 3)
    delta = mp.mpf(10) ** rng.uniform(-3, 3)
    beta = mp.mpf(10) ** rng.uniform(-2, 1.0)  # v2: n* <= 32
    a, b = c + delta, beta * delta
    alpha, T, info = build(a, b, c)
    r = check(alpha, T, a, b, c, density=(k < 40))
    recs.append({"kind": "random", "k": k, "a": mp.nstr(a, 20), "b": mp.nstr(b, 20), "c": mp.nstr(c, 20), **info, **r})
# (2) boundary-adjacent: beta = cot(pi/n) exactly and beta = cot(pi/(n-1)) (1 + 1e-9), n = 4..16; c = 1, a - c = 2
for n in range(3, 17):
    for kind, beta in (("upper_endpoint", mp.cot(mp.pi / n)),
                       ("just_above_lower", mp.cot(mp.pi / (n - 1)) * (1 + mp.mpf(10) ** -9) if n >= 4 else None)):
        if beta is None:
            continue
        c, delta = mp.mpf(1), mp.mpf(2)
        a, b = c + delta, beta * delta
        alpha, T, info = build(a, b, c)
        r = check(alpha, T, a, b, c, density=True)
        recs.append({"kind": kind, "n_target": n, "a": mp.nstr(a, 20), "b": mp.nstr(b, 20), "c": mp.nstr(c, 20),
                     **info, **r})
        if info["n"] != n:
            recs[-1]["OK"] = False
            recs[-1]["nstar_mismatch"] = True

summary = {"seed": SEED, "dps": 150, "records": len(recs), "ALL_OK": all(r["OK"] for r in recs),
           "n_fail": sum(1 for r in recs if not r["OK"]), "max_n": max(r["n"] for r in recs),
           "elapsed_seconds": round(time.time() - t_start, 2)}
with lane_guard.xopen(RUN + "/mpmath.json") as fh:
    json.dump({"summary": summary, "records": recs}, fh, indent=1)
print("SUMMARY", json.dumps(summary))
