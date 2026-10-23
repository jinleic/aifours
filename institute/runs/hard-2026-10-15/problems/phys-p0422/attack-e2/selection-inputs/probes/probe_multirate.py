# <=5 min probe (NOT a certificate): multi-rate trials in Vorobyev's y->inf series form, general k.
# Psi_T = -sum_{j<=T} mu_j^2/j - (k-1) a E log(1 - R_1..R_k), mu_j = sum_i (-1)^i C(j,i) M_i,
# M_i = exp((k a/2)(nu_i - 1)), nu_i = E(1 - R_1..R_{k-1})^i. Decimal for the alternating sums; floats elsewhere.
from decimal import Decimal as D, getcontext
from itertools import product
from math import comb, log
import random, sys
getcontext().prec = 130
T = 128
C = [[D(comb(j, i)) for i in range(j+1)] for j in range(T+1)]
def psi(k, a, rates, weights):
    tot = sum(weights); weights = [w/tot for w in weights]
    def dist(m):
        out = {}
        for combo in product(range(len(rates)), repeat=m):
            w = 1.0; p = 1.0
            for c in combo: w *= weights[c]; p *= rates[c]
            out[p] = out.get(p, 0.0) + w
        return out
    dk1 = {D(p): D(w) for p, w in dist(k-1).items()}; lam = D(k)*D(a)/2
    M = [(lam*(sum(w*(1-p)**i for p, w in dk1.items()) - 1)).exp() for i in range(T+1)]
    var = D(0)
    for j in range(1, T+1):
        mu = sum((C[j][i] if i % 2 == 0 else -C[j][i]) * M[i] for i in range(j+1))
        var -= mu*mu / j
    cl = sum(w*log(1-p) for p, w in dist(k).items())
    return float(var) - (k-1)*a*cl
def search(k, a, nrates=3, iters=250, seed=1):
    rnd = random.Random(seed)
    best = None
    x = ([0.05, 0.45, 0.85][:nrates] if nrates == 3 else sorted(rnd.random() for _ in range(nrates)), [1.0]*nrates)
    fx = psi(k, a, *x); step = 0.15
    for it in range(iters):
        r = [min(0.999, max(1e-3, v + rnd.gauss(0, step))) for v in x[0]]
        w = [max(1e-3, v * (1 + rnd.gauss(0, step))) for v in x[1]]
        f = psi(k, a, r, w)
        if f < fx: x, fx = (r, w), f
        if it % 60 == 59: step *= 0.5
    return fx, x
k = int(sys.argv[1])
for a in [float(v) for v in sys.argv[2:]]:
    fx, (r, w) = search(k, a)
    s = sum(w)
    print(f"k={k} a={a} best Psi~{fx:+.3e} rates={[round(v,4) for v in r]} weights={[round(v/s,4) for v in w]}", flush=True)
