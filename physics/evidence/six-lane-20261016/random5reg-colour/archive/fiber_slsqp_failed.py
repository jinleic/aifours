"""F(n) by maximising L over the 9-dim fibre M(n) (concave problem: slice concavity is proved
exactly in evidence/slice_poly.json, so a local maximum of the fibre problem is global).

Also returns the optimal pairing multipliers y (18 edges) from the KKT system, used later as
dual certificates.  Evaluator B (mu-system)."""
import sys, math
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, 'code')
from model import Model, cone_rows, nine_from_four

MOD = Model(5, True)
G4 = cone_rows(MOD)[:4]
A_ub = []
for u in range(9):
    for g in G4:
        row = np.zeros(36); row[4 * u:4 * u + 4] = -g
        A_ub.append(row @ MOD.E)
A_ub = np.array(A_ub)
A_vert = np.zeros((9, 18))
for u in range(9):
    row = np.zeros(36); row[4 * u:4 * u + 4] = 1.0
    A_vert[u] = row @ MOD.E   # sum of m^u = 5 n^u
XSTAR = np.full(18, 5 / 36)


def F_of_n(n9, x0=None, floor=1e-13, margin=1e-13):
    """max L over x >= 0 with sum m^u = 5 n^u and the cone constraints."""
    n9 = np.asarray(n9, float)
    active = n9 > 0
    if x0 is None:
        # feasible-ish start: scale the centre edge weights by geometric means of endpoint masses
        x0 = np.array([5 * math.sqrt(max(n9[u], 1e-12) * max(n9[v], 1e-12)) / 4 * 9 / 9
                       for (u, k, v, kv) in MOD.edges])
    cons = [{'type': 'eq', 'fun': lambda x: A_vert @ x - 5 * n9, 'jac': lambda x: A_vert},
            {'type': 'ineq', 'fun': lambda x: -(A_ub @ x) - margin, 'jac': lambda x: -A_ub}]

    def negL(x):
        xx = np.maximum(x, floor)
        v, g, _ = MOD.L(xx)
        return -v, -g

    r = minimize(negL, np.maximum(x0, 1e-12), jac=True, method='SLSQP', constraints=cons,
                 bounds=[(floor, None)] * 18, options={'maxiter': 1000, 'ftol': 1e-15})
    return -r.fun, r.x, r


if __name__ == '__main__':
    Lstar = MOD.L(XSTAR)[0]
    print('centre', Lstar)
    I3 = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1]) / 3
    C = np.full(9, 1 / 9)
    for t in [0.0, 0.2, 0.5, 0.8, 0.9, 0.95, 0.97, 0.98, 0.985, 0.99, 0.995]:
        n9 = (1 - t) * C + t * I3
        v, x, r = F_of_n(n9)
        print(f't={t:6.3f} n_off={n9[1]:.5f} lnF={v:.9f} gap={Lstar - v:.6f} ok={r.success}')
