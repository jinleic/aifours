import sys, os, json
sys.path.insert(0, '.')
from km2 import KM2
from pool import single_base_cnf
from satlib import solve
def order_mod(a, q):
    k, x = 1, a % q
    while x != 1:
        x = x * a % q; k += 1
    return k
for q in (31, 43):
    m = (q-1)//2; mp = m//3
    g = next(a for a in range(2, q) if order_mod(a, q) == m)
    lam = next(a for a in range(2, q) if order_mod(a, q) == mp)
    n = 2*q+1; inf = 2*q
    def P(f):
        o = [0]*n
        for j in range(2):
            for x in range(q):
                x2, j2 = f(x, j); o[q*j+x] = q*j2 + (x2 % q)
        o[inf] = inf; return tuple(o)
    tau = P(lambda x, j: (x+1, j)); mg = P(lambda x, j: (g*x, j))
    psi = P(lambda x, j: (lam*x, 0) if j == 0 else (lam*(x-1)+1, 1))
    M = KM2(n, [tau, mg], [([mg], []), ([tau], [psi])], names=["S0","B1"])
    for j, name in ((1, "B1-alone"), (0, "S0-alone")):
        cnf, rv = single_base_cnf(M, j)
        p = f"runs/ansatz/single_{name}_q{q}.cnf"; sha = cnf.write(p)
        st, model, dt = solve(p, "kissat", timeout=300, seed=0)
        print(q, name, st, round(dt, 3), sha[:16])
