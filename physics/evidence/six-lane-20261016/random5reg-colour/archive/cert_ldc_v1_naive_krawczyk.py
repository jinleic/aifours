"""Checker A (python-flint arb) for the central region: local dual concavity (LDC).

Claim: for every eta in the box B0 = [-r0, r0]^4 (eta = (n00,n01,n10,n11) - 1/9), eta != 0,
    ln F(n* + eta) <= U(eta) < U(0) = L* = (5/2) ln 5 + ln(25/24),
where U(eta) = sum_u [ n^u Psi*(K_u eta) + (3/2) n^u ln n^u ],  n^u = 1/9 + (A eta)_u,  K_u = C_u Y.
First inequality: weak duality with multipliers y = Y eta (valid for any Y).  Second: U is C^2 on
B0, grad U(0) = 0 exactly, and Hess U(eta) is negative definite on every sub-box (rigorous:
Krawczyk enclosure of the inner maximiser theta(z), ball-arithmetic Hessian, congruence +
Gershgorin).  Y = exact rational optimal linear response at n* (any rational Y would be valid).
Usage: cert_ldc.py R0_FRACTION K  (B0 split into K^4 sub-boxes)
"""
import sys, json, time, itertools, math
from fractions import Fraction
import numpy as np
import flint
from flint import arb, fmpq, arb_mat, fmpq_mat

flint.ctx.prec = 128
r0 = Fraction(sys.argv[1]); K = int(sys.argv[2])

# ---------------- combinatorial data (independent of model.py) ----------------
S = [(a, b, c, 5 - a - b - c) for a, b, c in itertools.product(range(6), repeat=3)
     if a + b + c <= 5 and min(a + b, 5 - a - b) >= 1 and min(a + c, 5 - a - c) >= 1]
assert len(S) == 36
FACT = [1, 1, 2, 6, 24, 120]
W = [120 // (FACT[a] * FACT[b] * FACT[c] * FACT[d]) for (a, b, c, d) in S]
OFF = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
EDGES, seen = [], set()
for u in range(9):
    i, j = divmod(u, 3)
    for k, (r, t) in enumerate(OFF):
        v = 3 * ((i + r) % 3) + (j + t) % 3
        kv = OFF.index((-r, -t))
        if (u, k) in seen:
            continue
        seen.add((u, k)); seen.add((v, kv))
        EDGES.append((u, k, v, kv))
Cmat = [[[0] * 18 for _ in range(4)] for _ in range(9)]
for e, (u, k, v, kv) in enumerate(EDGES):
    Cmat[u][k][e] += 1
    Cmat[v][kv][e] -= 1
A = [[1, 0, 0, 0], [0, 1, 0, 0], [-1, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, -1, -1],
     [-1, 0, -1, 0], [0, -1, 0, -1], [1, 1, 1, 1]]
B3 = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]]

# ---------------- exact Y from R(0) ----------------
Zc = sum(W)
mh0 = [fmpq(sum(W[i] * S[i][k] for i in range(36)), Zc) for k in range(4)]
assert all(x == fmpq(5, 4) for x in mh0)
E2 = [[fmpq(sum(W[i] * S[i][k] * S[i][l] for i in range(36)), Zc) for l in range(4)] for k in range(4)]
V0 = fmpq_mat([[E2[k][l] - mh0[k] * mh0[l] for l in range(4)] for k in range(4)])
B3q = fmpq_mat(B3)
Dinv0 = fmpq_mat([[fmpq(4, 5) if k == l else 0 for l in range(4)] for k in range(4)])
I4 = fmpq_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
J0 = B3q.transpose() * (fmpq(1, 2) * Dinv0 * V0 - I4) * B3q
R0 = -(V0 * B3q * J0.inv() * B3q.transpose())
Cq = [fmpq_mat(Cmat[u]) for u in range(9)]
G = sum((Cq[u].transpose() * R0 * Cq[u] for u in range(1, 9)), Cq[0].transpose() * R0 * Cq[0])
ones = fmpq_mat([[1]] * 4)
bmat = sum((Cq[u].transpose() * ones * fmpq_mat([A[u]]) for u in range(1, 9)), Cq[0].transpose() * ones * fmpq_mat([A[0]]))
Y = fmpq(-45, 4) * G.solve(bmat)          # 18 x 4 exact
Kq = [Cq[u] * Y for u in range(9)]          # 4 x 4 exact
# exact gradient check at 0: sum_u A_u = 0 and sum_u K_u^T 1 = 0
assert all(sum(A[u][c] for u in range(9)) == 0 for c in range(4))
sK = sum((Kq[u].transpose() * ones for u in range(1, 9)), Kq[0].transpose() * ones)
assert all(sK[i, 0] == 0 for i in range(4))


# ---------------- inner problem in ball arithmetic ----------------
def fam(theta):  # theta: list of 4 arb
    ex = []
    for s, w in zip(S, W):
        ex.append(arb(w) * (sum((theta[k] * s[k] for k in range(4)), arb(0))).exp())
    Z = sum(ex, arb(0))
    p = [x / Z for x in ex]
    mh = [sum((p[i] * S[i][k] for i in range(36)), arb(0)) for k in range(4)]
    E2 = [[sum((p[i] * (S[i][k] * S[i][l]) for i in range(36)), arb(0)) for l in range(4)] for k in range(4)]
    V = arb_mat([[E2[k][l] - mh[k] * mh[l] for l in range(4)] for k in range(4)])
    return mh, V


def Gfun(a, z):  # a: 3 arb, z: 4 arb  -> 3 arb
    th = [sum((a[c] * B3[k][c] for c in range(3)), arb(0)) for k in range(4)]
    mh, V = fam(th)
    F = [mh[k].log() / 2 - th[k] + z[k] for k in range(4)]
    return [sum((F[k] * B3[k][c] for k in range(4)), arb(0)) for c in range(3)]


def Jfun(a):
    th = [sum((a[c] * B3[k][c] for c in range(3)), arb(0)) for k in range(4)]
    mh, V = fam(th)
    Dinv = arb_mat([[(1 / mh[k]) / 2 if k == l else arb(0) for l in range(4)] for k in range(4)])
    I = arb_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
    B = arb_mat(B3)
    return B.transpose() * (Dinv * V - I) * B, mh, V


def float_inner(z):
    a = np.zeros(3)
    Bf = np.array(B3, float)
    Sf = np.array(S, float); lw = np.log(np.array(W, float))
    for _ in range(100):
        th = Bf @ a
        zz = lw + Sf @ th; p = np.exp(zz - zz.max()); p /= p.sum()
        mh = Sf.T @ p; V = (Sf.T * p) @ Sf - np.outer(mh, mh)
        F = Bf.T @ (0.5 * np.log(mh) - th + z)
        if np.max(np.abs(F)) < 1e-15:
            break
        J = Bf.T @ (0.5 * V / mh[:, None] - np.eye(4)) @ Bf
        a = a - np.linalg.solve(J, F)
    return a


def inner_enclosure(zb):
    """zb: list of 4 arb (z box). Returns (mh, R) enclosures for all z in zb, or None."""
    zmid = np.array([float(x.mid()) for x in zb])
    at = float_inner(zmid)
    Jm, _, _ = Jfun([arb(x) for x in at])
    Yk = np.linalg.inv(np.array([[float(Jm[i, j].mid()) for j in range(3)] for i in range(3)]))
    Ya = arb_mat([[arb(float(Yk[i, j])) for j in range(3)] for i in range(3)])
    G0 = Gfun([arb(x) for x in at], zb)
    est = np.abs(Yk) @ np.array([float(x.rad()) + abs(float(x.mid())) for x in G0])
    rho = max(2 * est.max(), 1e-12)
    for attempt in range(40):
        Th = [arb(at[c]).union(arb(at[c] - rho)).union(arb(at[c] + rho)) for c in range(3)]
        JT, mhT, VT = Jfun(Th)
        I3 = arb_mat([[1 if i == j else 0 for j in range(3)] for i in range(3)])
        Mres = I3 - Ya * JT
        dv = arb_mat([[Th[c] - arb(at[c])] for c in range(3)])
        Kv = arb_mat([[arb(at[c])] for c in range(3)]) - Ya * arb_mat([[x] for x in G0]) + Mres * dv
        ok = True
        for c in range(3):
            lo_ok = (Kv[c, 0] - arb(at[c] - rho)) > 0
            hi_ok = (arb(at[c] + rho) - Kv[c, 0]) > 0
            if not (lo_ok and hi_ok):
                ok = False
        if ok:
            B = arb_mat(B3)
            R = -(VT * B * JT.inv() * B.transpose())
            return mhT, R, rho
        rho *= 2
        if rho > 1.0:
            return None
    return None


def check_box(lo, hi):
    """lo, hi: exact Fractions (4 each). Returns (ok, max Gershgorin upper bound)."""
    eta = [arb(fmpq(l.numerator, l.denominator)).union(arb(fmpq(h.numerator, h.denominator))) for l, h in zip(lo, hi)]
    H = arb_mat(4, 4)
    for u in range(9):
        nu = arb(fmpq(1, 9)) + sum((eta[c] * A[u][c] for c in range(4)), arb(0))
        if not (nu > 0):
            return False, None
        Ka = arb_mat([[arb(Kq[u][i, j]) for j in range(4)] for i in range(4)])
        zb = [sum((Ka[i, c] * eta[c] for c in range(4)), arb(0)) for i in range(4)]
        res = inner_enclosure(zb)
        if res is None:
            return False, None
        mh, R, rho = res
        a = arb_mat([[arb(A[u][c])] for c in range(4)])
        km = Ka.transpose() * arb_mat([[x] for x in mh])
        H = H + (arb(fmpq(3, 2)) / nu) * (a * a.transpose()) + a * km.transpose() + km * a.transpose() \
            + nu * (Ka.transpose() * R * Ka)
    Hm = np.array([[float(H[i, j].mid()) for j in range(4)] for i in range(4)])
    _, P = np.linalg.eigh(0.5 * (Hm + Hm.T))
    Pq = fmpq_mat([[fmpq(*Fraction(float(P[i, j])).as_integer_ratio()) for j in range(4)] for i in range(4)])
    assert Pq.det() != 0
    Pa = arb_mat([[arb(Pq[i, j]) for j in range(4)] for i in range(4)])
    M = Pa.transpose() * H * Pa
    worst = None
    for i in range(4):
        g = M[i, i] + sum((abs(M[i, j]) for j in range(4) if j != i), arb(0))
        if not (g < 0):
            return False, g
        worst = g if worst is None else worst.max(g)
    return True, worst


if __name__ == '__main__':
    t0 = time.time()
    edges = [-r0 + Fraction(2 * i, K) * r0 for i in range(K + 1)]
    nfail, worst = 0, None
    boxes = 0
    for idx in itertools.product(range(K), repeat=4):
        lo = [edges[i] for i in idx]; hi = [edges[i + 1] for i in idx]
        ok, g = check_box(lo, hi)
        boxes += 1
        if not ok:
            nfail += 1
            print('FAIL box', [str(x) for x in lo], [str(x) for x in hi], g, flush=True)
        else:
            worst = g if worst is None else worst.max(g)
    # exact value / gradient identities at 0
    out = {'r0': str(r0), 'K': K, 'boxes': boxes, 'failed': nfail,
           'max_gershgorin_upper': str(worst), 'runtime_s': round(time.time() - t0, 1),
           'Y_exact_denominator_bits': max(int(Y[i, j].denom()).bit_length() for i in range(18) for j in range(4)),
           'verdict': 'PASS' if nfail == 0 else 'FAIL'}
    print(json.dumps(out))
