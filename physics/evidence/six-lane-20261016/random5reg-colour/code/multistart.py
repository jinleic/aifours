"""Full-domain multistart search for max L(m) over the 13-dim polytope M (no concavity assumption).

Variables: 18 edge weights x of K3 x K3.  Constraints: x >= floor, cone (5.4) at each vertex,
overlap row/col sums 1/3.  Objective L = sum_u psi(m^u) (evaluator B, mu-system).
Starts: random convex combinations of random LP vertices of M (so starts reach every boundary
layer), plus pure LP vertices pulled 1e-3 inward.  Usage: multistart.py SEED NSTARTS [plain]
"""
import sys, json, math, time
import numpy as np
from scipy.optimize import linprog, minimize
sys.path.insert(0, 'code')
from model import Model, cone_rows

seed = int(sys.argv[1]); nstarts = int(sys.argv[2])
rainbow = not (len(sys.argv) > 3 and sys.argv[3] == 'plain')
mod = Model(5, rainbow)
rng = np.random.default_rng(seed)
G = cone_rows(mod)[:4] if rainbow else np.zeros((0, 4))
# inequality A_ub x <= b_ub  (cone: -G m^u <= 0)
A_ub = []
for u in range(9):
    for g in G:
        row = np.zeros(36); row[4 * u:4 * u + 4] = -g
        A_ub.append(row @ mod.E)
A_ub = np.array(A_ub) if len(A_ub) else np.zeros((0, 18))
b_ub = np.zeros(len(A_ub))
# equalities: n^u = sum m^u / 5 ; rows i=0,1,2 and cols j=0,1
A_eq = []
for i in range(3):
    row = np.zeros(36)
    for j in range(3):
        row[4 * (3 * i + j):4 * (3 * i + j) + 4] = 1 / 5
    A_eq.append(row @ mod.E)
for j in range(2):
    row = np.zeros(36)
    for i in range(3):
        row[4 * (3 * i + j):4 * (3 * i + j) + 4] = 1 / 5
    A_eq.append(row @ mod.E)
A_eq = np.array(A_eq); b_eq = np.full(5, 1 / 3)
xstar = np.full(18, 5 / 36)
Lstar = mod.L(xstar)[0]

def lp_vertex():
    c = rng.normal(size=18)
    r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * 18, method='highs')
    return r.x

FLOOR = 1e-12
MARGIN = 1e-11
cons = [{'type': 'eq', 'fun': lambda x: A_eq @ x - b_eq, 'jac': lambda x: A_eq}]
if len(A_ub):
    cons.append({'type': 'ineq', 'fun': lambda x: -(A_ub @ x) - MARGIN, 'jac': lambda x: -A_ub})

def negL(x):
    xx = np.maximum(x, FLOOR)
    v, g, _ = mod.L(xx)
    return -v, -g

results = []
t0 = time.time()
verts = [lp_vertex() for _ in range(64)]
for k in range(nstarts):
    kind = k % 3
    if kind == 0:   # random interior combination of vertices (Dirichlet, possibly sparse)
        idx = rng.choice(len(verts), size=rng.integers(2, 8), replace=False)
        lam = rng.dirichlet(np.full(len(idx), rng.choice([0.2, 1.0, 5.0])))
        x0 = sum(l * verts[i] for l, i in zip(lam, idx))
    elif kind == 1:  # near a single vertex (boundary layer)
        eps = 10 ** rng.uniform(-4, -1)
        x0 = (1 - eps) * verts[rng.integers(len(verts))] + eps * xstar
    else:           # random point between centre and a random combination
        idx = rng.choice(len(verts), size=3, replace=False)
        lam = rng.dirichlet(np.ones(3))
        t = rng.uniform(0, 1)
        x0 = (1 - t) * xstar + t * sum(l * verts[i] for l, i in zip(lam, idx))
    x0 = np.maximum(x0, 1e-9)
    try:
        r = minimize(negL, x0, jac=True, method='SLSQP', constraints=cons,
                     bounds=[(FLOOR, None)] * 18, options={'maxiter': 500, 'ftol': 1e-15})
        xf = r.x
        val = -r.fun
        feas = max(np.max(np.abs(A_eq @ xf - b_eq)), np.max(np.maximum(A_ub @ xf, 0)) if len(A_ub) else 0)
        n9 = mod.n_from_x(xf)
        results.append({'k': k, 'kind': kind, 'L0': float(-negL(x0)[0]), 'L': float(val), 'gap': float(Lstar - val),
                        'dist_centre': float(np.max(np.abs(xf - xstar))), 'n9': n9.round(6).tolist(),
                        'feas': float(feas), 'success': bool(r.success), 'nit': int(r.nit)})
    except Exception as ex:  # record, never hide
        results.append({'k': k, 'kind': kind, 'error': repr(ex)})
good = [r for r in results if 'L' in r and r['success'] and r['feas'] < 1e-9]
best = max(good, key=lambda r: r['L']) if good else None
out = {'seed': seed, 'nstarts': nstarts, 'rainbow': rainbow, 'Lstar': Lstar, 'Fstar': math.exp(Lstar),
       'best_converged_feasible': best, 'runtime_s': time.time() - t0,
       'n_errors': sum('error' in r for r in results),
       'n_converged_feasible': len(good),
       'n_within_1e-4_of_centre': sum(1 for r in good if r['dist_centre'] < 1e-4),
       'max_L_minus_Lstar_converged_feasible': (max(r['L'] for r in good) - Lstar) if good else None,
       'results': results}
tag = 'rainbow' if rainbow else 'plain'
with open(f'evidence/multistart_{tag}_seed{seed}.json', 'w') as f:
    json.dump(out, f, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'results'}, indent=1))
