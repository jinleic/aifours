# Feasibility probe (<=5 min): can an exact MILP (HiGHS) settle max-nonlinearity questions
# in a 9-variable symmetry class of ~60 orbits? Calibration class: RSBFs (9-cycle rotation),
# where exhaustive search (Kavut-Maitra-Sarkar-Yucel 2006/07) shows max nl = 241.
import itertools, time, sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
n = 9
def rot(x):  # rotate n-bit integer left by 1
    return ((x << 1) | (x >> (n - 1))) & ((1 << n) - 1)
seen = {}; orbits = []
for x in range(1 << n):
    if x in seen: continue
    o = []; y = x
    while y not in o:
        o.append(y); y = rot(y)
    for y in o: seen[y] = len(orbits)
    orbits.append(o)
k = len(orbits)
pc = np.array([bin(i).count('1') & 1 for i in range(1 << n)])
H = np.array([[1 - 2 * pc[a & x] for x in range(1 << n)] for a in range(1 << n)])
C = np.array([[H[orb_a[0], ob].sum() for ob in orbits] for orb_a in orbits])  # W(a) = sum_O C[a,O]*s_O
def run(T, balanced, tl):
    # s_O = 1 - 2 f_O ; W = C@1 - 2 C@f ; -T <= W <= T
    c0 = C.sum(axis=1)
    A = -2 * C
    lo = -T - c0; hi = T - c0
    if balanced:  # W(0) = 0 exactly (orbit of a=0 is index of orbit containing 0)
        i0 = seen[0]; lo[i0] = -c0[i0]; hi[i0] = -c0[i0]
    t = time.time()
    res = milp(c=np.zeros(k), constraints=LinearConstraint(A, lo, hi), integrality=np.ones(k),
               bounds=Bounds(0, 1), options={"time_limit": tl, "disp": False})
    dt = time.time() - t
    status = {0: 'FEASIBLE(optimal)', 1: 'TIMEOUT/iter-limit', 2: 'INFEASIBLE', 3: 'unbounded', 4: 'other'}.get(res.status, res.status)
    nl = None
    if res.x is not None:
        f = np.round(res.x).astype(int); s = 1 - 2 * f
        tt = np.zeros(1 << n, dtype=int)
        for O, ob in enumerate(orbits):
            for x in ob: tt[x] = f[O]
        W = H @ (1 - 2 * tt)  # independent full Walsh check
        nl = int((1 << (n - 1)) - np.abs(W).max() // 2); bal = int(W[0] == 0)
    else:
        bal = None
    print(f"orbits={k} T={T} balanced={balanced}: {status} in {dt:.1f}s; independent-check nl={nl} balanced={bal}", flush=True)
for T, bal in [(30, False), (28, False), (30, True), (32, True)]:
    run(T, bal, 70)
