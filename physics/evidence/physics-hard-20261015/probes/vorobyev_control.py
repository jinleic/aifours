# Positive control (<=5 min): evaluate Vorobyev's three-rate trial with the k-general y->infinity form of the probe functional:
# Psi_T = -sum_{j<=T} mu_j^2/j - (k-1) a E log(1 - R_1...R_k),  mu_j = sum_i (-1)^i C(j,i) M_i,
# M_i = exp((k a/2)(nu_i - 1)), nu_i = E(1 - R_1...R_{k-1})^i.  High-precision Decimal; floating summary only.
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from itertools import product
from math import comb
import sys
getcontext().prec = 160
def psi(k, a, rates, weights, T):
    a = D(a.numerator)/D(a.denominator)
    def E_pow(m, i):  # E (1 - prod of m rates)^i, exact rational
        s = F(0)
        for combo in product(range(len(rates)), repeat=m):
            w = F(1); p = F(1)
            for c in combo: w *= weights[c]; p *= rates[c]
            s += w * (1 - p)**i
        return s
    lam = D(k)*a/2
    M = [ (lam*(D((x:=E_pow(k-1, i)).numerator)/D(x.denominator) - 1)).exp() for i in range(T+1) ]
    var = D(0)
    for j in range(1, T+1):
        mu = sum(((-1)**i) * comb(j, i) * M[i] for i in range(j+1))
        var -= mu*mu / j
    cl = D(0)
    for combo in product(range(len(rates)), repeat=k):
        w = F(1); p = F(1)
        for c in combo: w *= weights[c]; p *= rates[c]
        cl += D(w.numerator)/D(w.denominator) * (1 - D(p.numerator)/D(p.denominator)).ln()
    return var, -(k-1)*a*cl, var - (k-1)*a*cl
rates = [F(1,20), F(2,5), F(17,20)]; weights = [F(1,4), F(1,2), F(1,4)]
v, c, tot = psi(3, F(1067,250), rates, weights, 128)
print(f"k=3 a=4.268 three-rate T=128: variable term {float(v):.8f}, clause term {float(c):+.8f}, Psi = {float(tot):.4e}")
v, c, tot = psi(3, F(4), rates, weights, 128)
print(f"negative control k=3 a=4.0 same trial: Psi = {float(tot):.4e} (must be >= 0)")
