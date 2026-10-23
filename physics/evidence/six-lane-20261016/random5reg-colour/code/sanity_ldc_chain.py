"""Floating-point sanity check of the central chain ln F(n) <= U(eta) <= Ubar(eta) < L* (not a proof)."""
import sys, math, json
import numpy as np
sys.argv = ['x', '1/10000', '3/20', '1', '1']
src = open('code/cert_ldc3.py').read().split("if __name__ == '__main__':")[0]
exec(src)
sys.path.insert(0, 'code')
from dual import solve_dual, inner, C as Cd
LS = 2.5 * math.log(5) + math.log(25 / 24)
Yf = np.array([[float(toF(Y[i, j])) for j in range(4)] for i in range(18)])
Kf = [np.array([[float(toF(Kq[u][i, j])) for j in range(4)] for i in range(4)]) for u in range(9)]
lf = [np.array([float(toF(lq[u][i, 0])) for i in range(4)]) for u in range(9)]
Qf = [np.array([[float(toF(Qq[u][i, j])) for j in range(4)] for i in range(4)]) for u in range(9)]
psi0 = 2.5 * math.log(1.25) + math.log(900)
rng = np.random.default_rng(11)
rows = []
for r0 in [1e-4, 1e-3]:
    for _ in range(6):
        eta = rng.uniform(-r0, r0, 4)
        n9 = np.array([1 / 9 + sum(A[u][c] * eta[c] for c in range(4)) for u in range(9)])
        lnF = solve_dual(n9)[0]
        U = sum(n9[u] * inner(Kf[u] @ eta)[0] + 1.5 * n9[u] * math.log(n9[u]) for u in range(9))
        Ub = sum(n9[u] * (psi0 + lf[u] @ eta + 0.5 * eta @ Qf[u] @ eta) + 1.5 * n9[u] * math.log(n9[u]) for u in range(9))
        rows.append((r0, float(LS - lnF), float(LS - U), float(LS - Ub)))
        assert lnF <= U + 1e-12 and U <= Ub + 1e-12 and Ub < LS
for r in rows:
    print('r0=%g  L*-lnF=%.3e  L*-U=%.3e  L*-Ubar=%.3e' % r)
print('chain consistent on', len(rows), 'random points')
