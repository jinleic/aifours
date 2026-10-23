"""Checker A (python-flint arb) for the central box: local dual concavity via a quadratic majorant.

Notation: eta = (n00,n01,n10,n11) - 1/9 in B0 = [-r0, r0]^4; n^u = 1/9 + (A eta)_u;
multipliers y = Y eta (Y exact rational optimal linear response at n*); z^u = K_u eta, K_u = C_u Y.
  (W)  ln F(n) <= U(eta) = sum_u [n^u Psi*(z^u) + (3/2) n^u ln n^u]     (weak duality, any Y)
  (Q)  Psi*(z) <= Psi*(0) + (5/4) 1.z + (1/2) z^T Rbar z  for z in the region Z,
       Rbar = R(0) + eps * (I - J/4), certified by R(z) <= Rbar on Z (Taylor; R = Hess Psi*).
  (C)  Ubar(eta) = sum_u [n^u (Psi*(0) + l_u.eta + eta^T Q_u eta / 2) + (3/2) n^u ln n^u] has
       Ubar(0) = L*, grad Ubar(0) = 0 (exact identities) and Hess Ubar < 0 on B0 (rigorous),
       hence ln F(n) <= Ubar(eta) < L* for eta in B0 \\ {0}.
(Q) is checked on a grid of boxes covering the range of c = B3^T z (Psi* and R depend on z only
through B3^T z): parametric Krawczyk for the inner stationarity system in a (theta = B3 a), with
single-use exponent evaluation of the exponential family, then a congruence+Gershgorin test of
B3^T (Rbar - R) B3 > 0.  (C) is checked on an M^4 grid of sub-boxes of B0.
Usage: cert_ldc2.py R0 EPS NC M     e.g. 3/1000 1/10 12 4
"""
import sys, json, time, itertools
from fractions import Fraction
import numpy as np
import flint
from flint import arb, fmpq, arb_mat, fmpq_mat

flint.ctx.prec = 128
r0 = Fraction(sys.argv[1]); eps = Fraction(sys.argv[2]); NC = int(sys.argv[3]); M = int(sys.argv[4])
fq = lambda f: fmpq(f.numerator, f.denominator)

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
BETA = [[sum(B3[k][c] * s[k] for k in range(4)) for c in range(3)] for s in S]

# ---------------- exact data at n* ----------------
Zc = sum(W)
mh0 = [fmpq(sum(W[i] * S[i][k] for i in range(36)), Zc) for k in range(4)]
assert all(x == fmpq(5, 4) for x in mh0)
E2 = [[fmpq(sum(W[i] * S[i][k] * S[i][l] for i in range(36)), Zc) for l in range(4)] for k in range(4)]
V0 = fmpq_mat([[E2[k][l] - mh0[k] * mh0[l] for l in range(4)] for k in range(4)])
B3q = fmpq_mat(B3)
I4 = fmpq_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
J0 = B3q.transpose() * (fmpq(2, 5) * V0 - I4) * B3q          # (1/2) D^{-1} V - I with D = 5/4
R0 = -(V0 * B3q * J0.inv() * B3q.transpose())
Pperp = fmpq_mat([[fmpq(3, 4) if k == l else fmpq(-1, 4) for l in range(4)] for k in range(4)])
Rbar = R0 + fq(eps) * Pperp
Cq = [fmpq_mat(Cmat[u]) for u in range(9)]
G = Cq[0].transpose() * R0 * Cq[0]
for u in range(1, 9):
    G += Cq[u].transpose() * R0 * Cq[u]
ones = fmpq_mat([[1]] * 4)
bm = Cq[0].transpose() * ones * fmpq_mat([A[0]])
for u in range(1, 9):
    bm += Cq[u].transpose() * ones * fmpq_mat([A[u]])
Y = fmpq(-45, 4) * G.solve(bm)
Kq = [Cq[u] * Y for u in range(9)]
lq = [fmpq(5, 4) * (Kq[u].transpose() * ones) for u in range(9)]
Qq = [Kq[u].transpose() * Rbar * Kq[u] for u in range(9)]
# exact identities: Ubar(0) = L* (Psi*(0) = (5/2)ln(5/4) + ln 900; checked symbolically below),
# grad Ubar(0) = sum_u a_u Psi*(0) + (3/2)(ln(1/9)+1) a_u + (1/9) l_u = 0:
assert all(sum(A[u][c] for u in range(9)) == 0 for c in range(4))
lsum = lq[0]
for u in range(1, 9):
    lsum += lq[u]
assert all(lsum[i, 0] == 0 for i in range(4))


# ---------------- (Q): inner problem, single-use exponent ball evaluation ----------------
def fam(a):
    p = []
    for i in range(36):
        tot = arb(0)
        for j in range(36):
            ex = arb(0)
            for c in range(3):
                dlt = BETA[j][c] - BETA[i][c]
                if dlt:
                    ex += a[c] * dlt
            tot += arb(fmpq(W[j], W[i])) * ex.exp()
        p.append(1 / tot)
    mh = [sum((p[i] * S[i][k] for i in range(36) if S[i][k]), arb(0)) for k in range(4)]
    V = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        for j in range(i + 1, 36):
            pp = p[i] * p[j]
            d = [S[i][k] - S[j][k] for k in range(4)]
            for k in range(4):
                if d[k] == 0:
                    continue
                for l in range(k, 4):
                    if d[l]:
                        V[k][l] = V[k][l] + pp * (d[k] * d[l])
    Vm = arb_mat([[V[min(k, l)][max(k, l)] for l in range(4)] for k in range(4)])
    return mh, Vm


B3a = arb_mat(B3)
BtB = [[sum(B3[k][c] * B3[k][d] for k in range(4)) for d in range(3)] for c in range(3)]


def Gfun(a, cbox):
    mh, V = fam(a)
    lm = [x.log() / 2 for x in mh]
    return [sum((lm[k] * B3[k][c] for k in range(4)), arb(0)) - sum((a[d] * BtB[c][d] for d in range(3)), arb(0)) + cbox[c]
            for c in range(3)]


def Jfun(a):
    mh, V = fam(a)
    Dh = arb_mat([[(1 / mh[k]) / 2 if k == l else arb(0) for l in range(4)] for k in range(4)])
    I = arb_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
    return B3a.transpose() * (Dh * V - I) * B3a, mh, V


def float_inner(c):
    Sf = np.array(S, float); lw = np.log(np.array(W, float)); Bf = np.array(B3, float)
    a = np.zeros(3)
    for _ in range(100):
        th = Bf @ a
        zz = lw + Sf @ th; p = np.exp(zz - zz.max()); p /= p.sum()
        mh = Sf.T @ p; V = (Sf.T * p) @ Sf - np.outer(mh, mh)
        F = Bf.T @ (0.5 * np.log(mh)) - Bf.T @ Bf @ a + c
        if np.max(np.abs(F)) < 1e-15:
            break
        J = Bf.T @ (0.5 * V / mh[:, None] - np.eye(4)) @ Bf
        a = a - np.linalg.solve(J, F)
    return a, J


def interval(lo, hi):
    return arb(lo).union(arb(hi))


def check_Q(clo, chi):
    cbox = [interval(fq(l), fq(h)) for l, h in zip(clo, chi)]
    cmid = np.array([float((l + h) / 2) for l, h in zip(clo, chi)])
    at, Jf = float_inner(cmid)
    Yk = np.linalg.inv(Jf)
    Ya = arb_mat([[arb(float(Yk[i, j])) for j in range(3)] for i in range(3)])
    G0 = Gfun([arb(float(x)) for x in at], cbox)
    est = np.abs(Yk) @ np.array([abs(float(x.mid())) + float(x.rad()) for x in G0])
    rho = max(1.5 * est.max(), 1e-10)
    for attempt in range(12):
        Th = [interval(float(at[c] - rho), float(at[c] + rho)) for c in range(3)]
        JT, mhT, VT = Jfun(Th)
        I3 = arb_mat([[1 if i == j else 0 for j in range(3)] for i in range(3)])
        Mres = I3 - Ya * JT
        dv = arb_mat([[Th[c] - arb(float(at[c]))] for c in range(3)])
        Kv = arb_mat([[arb(float(at[c]))] for c in range(3)]) - Ya * arb_mat([[x] for x in G0]) + Mres * dv
        if all(((Kv[c, 0] - arb(float(at[c] - rho))) > 0) and ((arb(float(at[c] + rho)) - Kv[c, 0]) > 0) for c in range(3)):
            R = -(VT * B3a * JT.inv() * B3a.transpose())
            D = arb_mat([[arb(Rbar[i, j]) for j in range(4)] for i in range(4)]) - R
            D = B3a.transpose() * D * B3a
            Ds = arb_mat([[(D[i, j] + D[j, i]) / 2 for j in range(3)] for i in range(3)])
            ok, g = gersh_pos(Ds)
            return ok, ('krawczyk_ok', rho, str(g))
        rho *= 2
    return False, ('krawczyk_fail', rho)


def gersh_pos(Hs):
    """rigorous: Hs (symmetric ball matrix) positive definite via congruence by a float eigenbasis."""
    n = Hs.nrows()
    Hm = np.array([[float(Hs[i, j].mid()) for j in range(n)] for i in range(n)])
    _, P = np.linalg.eigh(0.5 * (Hm + Hm.T))
    Pq = fmpq_mat([[fmpq(*Fraction(float(P[i, j])).as_integer_ratio()) for j in range(n)] for i in range(n)])
    assert Pq.det() != 0
    Pa = arb_mat([[arb(Pq[i, j]) for j in range(n)] for i in range(n)])
    Mx = Pa.transpose() * Hs * Pa
    worst = None
    for i in range(n):
        g = Mx[i, i] - sum((abs(Mx[i, j]) for j in range(n) if j != i), arb(0))
        if not (g > 0):
            return False, g
        worst = g if worst is None else worst.min(g)
    return True, worst


# ---------------- (C): explicit Hessian of Ubar on sub-boxes of B0 ----------------
def check_C(lo, hi):
    eta = [interval(fq(l), fq(h)) for l, h in zip(lo, hi)]
    H = arb_mat(4, 4)
    for u in range(9):
        nu = arb(fmpq(1, 9)) + sum((eta[c] * A[u][c] for c in range(4)), arb(0))
        if not (nu > 0):
            return False, None
        a = arb_mat([[arb(A[u][c])] for c in range(4)])
        Qa = arb_mat([[arb(Qq[u][i, j]) for j in range(4)] for i in range(4)])
        la = arb_mat([[arb(lq[u][i, 0])] for i in range(4)])
        g = la + Qa * arb_mat([[x] for x in eta])
        H = H + a * g.transpose() + g * a.transpose() + nu * Qa + (arb(fmpq(3, 2)) / nu) * (a * a.transpose())
    Hn = arb_mat([[-(H[i, j] + H[j, i]) / 2 for j in range(4)] for i in range(4)])
    return gersh_pos(Hn)


if __name__ == '__main__':
    t0 = time.time()
    # range of c = B3^T K_u eta over eta in B0, all u
    gam = [Fraction(0)] * 3
    for u in range(9):
        BK = B3q.transpose() * Kq[u]
        for c in range(3):
            s = sum(abs(Fraction(int(BK[c, k].p), int(BK[c, k].q))) for k in range(4)) * r0
            gam[c] = max(gam[c], s)
    res_Q = {'boxes': 0, 'failed': 0, 'fails': []}
    grid = [[-gam[c] + Fraction(2 * i, NC) * gam[c] for i in range(NC + 1)] for c in range(3)]
    for idx in itertools.product(range(NC), repeat=3):
        clo = [grid[c][idx[c]] for c in range(3)]; chi = [grid[c][idx[c] + 1] for c in range(3)]
        ok, info = check_Q(clo, chi)
        res_Q['boxes'] += 1
        if not ok:
            res_Q['failed'] += 1
            res_Q['fails'].append([[str(x) for x in clo], info if isinstance(info, tuple) else str(info)])
    res_Q['runtime_s'] = round(time.time() - t0, 1)
    t1 = time.time()
    res_C = {'boxes': 0, 'failed': 0, 'min_margin': None}
    eg = [-r0 + Fraction(2 * i, M) * r0 for i in range(M + 1)]
    for idx in itertools.product(range(M), repeat=4):
        lo = [eg[i] for i in idx]; hi = [eg[i + 1] for i in idx]
        ok, g = check_C(lo, hi)
        res_C['boxes'] += 1
        if not ok:
            res_C['failed'] += 1
        elif g is not None:
            res_C['min_margin'] = g if res_C['min_margin'] is None else res_C['min_margin'].min(g)
    res_C['min_margin'] = str(res_C['min_margin'])
    res_C['runtime_s'] = round(time.time() - t1, 1)
    out = {'r0': str(r0), 'eps': str(eps), 'NC': NC, 'M': M, 'c_range': [str(g) for g in gam],
           'Q_check': res_Q, 'C_check': res_C,
           'verdict': 'PASS' if res_Q['failed'] == 0 and res_C['failed'] == 0 else 'FAIL'}
    print(json.dumps(out, default=str))
