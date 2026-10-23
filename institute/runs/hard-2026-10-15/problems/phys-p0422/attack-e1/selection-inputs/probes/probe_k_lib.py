# <=5 min feasibility probe (floating point, NOT a certificate). numpy only.
# Single-rate energetic trial, general k (derivation in catalog.md section c):
# Phi(y,eta)=E_{dA,dB~Poi(k a/2)} log E[exp(-y min(nA,nB))] - (k-1) a log(1-eta^k (1-e^{-y})), nA|dA~Bin(dA,eta^(k-1)).
# Phi<0 for some (y,eta)  ==> (if the interpolation inequality holds) random k-SAT at density a is UNSAT whp.
import numpy as np, math, sys
def pois(lam, D):
    n = np.arange(D+1); return np.exp(-lam + n*math.log(lam) - np.array([math.lgamma(i+1) for i in n]))
def binom_mat(D, q):
    G = np.zeros((D+1, D+1)); lg = np.array([math.lgamma(i+1) for i in range(D+1)])
    for d in range(D+1):
        j = np.arange(d+1)
        with np.errstate(divide='ignore'):
            G[d,:d+1] = np.exp(lg[d]-lg[j]-lg[d-j] + j*math.log(q) + (d-j)*math.log1p(-q)) if 0<q<1 else (j==(d if q==1 else 0)).astype(float)
    return G
def Phi(k, a, y, eta, D):
    lam = k*a/2; q = eta**(k-1); pd = pois(lam, D)
    S = np.cumsum(binom_mat(D, q)[:, ::-1], axis=1)[:, ::-1]
    ek = np.exp(-y*np.arange(D+1)); idx = np.where(pd > 1e-13)[0]; Si = S[idx]
    tot = 0.0
    for dA in idx:
        pm = S[dA][None,:]*Si
        pmin = pm - np.concatenate([pm[:,1:], np.zeros((len(idx),1))], axis=1)
        tot += pd[dA]*np.dot(pd[idx], np.log(np.maximum(pmin@ek, 1e-300)))
    return tot - (k-1)*a*math.log(1 - eta**k*(1-math.exp(-y)))
