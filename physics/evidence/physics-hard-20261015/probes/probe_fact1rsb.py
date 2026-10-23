# <=5 min feasibility probe (floating point, NOT a certificate):
# factorized 1RSB energetic trial for 3-SAT interpolation bound (derived in catalog notes)
# Phi(y,eta) = E_{dA,dB~Poi(3a/2)} log E[exp(-y*min(nA,nB))] - 2a*log(1-eta^3*(1-exp(-y))),
# nA~Bin(dA,eta^2), nB~Bin(dB,eta^2) (inner). Phi<0 for some (y,eta) => alpha_3 <= a (if derivation right).
import numpy as np
from scipy.stats import poisson, binom
from scipy.optimize import minimize
def Phi(a, y, eta, D=60):
    lam = 1.5*a; q = eta**2
    pd = poisson.pmf(np.arange(D+1), lam)
    # g[d][n] = P(nA=n | dA=d)
    G = np.zeros((D+1, D+1))
    for d in range(D+1):
        G[d,:d+1] = binom.pmf(np.arange(d+1), d, q)
    # survival S[d][k] = P(nA >= k | d)
    S = np.cumsum(G[:, ::-1], axis=1)[:, ::-1]
    tot = 0.0
    ek = np.exp(-y*np.arange(D+1))
    for dA in range(D+1):
        for dB in range(D+1):
            w = pd[dA]*pd[dB]
            if w < 1e-16: continue
            # P(min>=k) = S[dA][k]*S[dB][k]; E e^{-y min} = sum_k P(min=k) e^{-yk}
            pm = S[dA]*S[dB]
            pmin = pm - np.append(pm[1:], 0.0)
            tot += w*np.log(np.dot(pmin, ek))
    return tot - 2*a*np.log(1 - eta**3*(1-np.exp(-y)))
for a in [4.2, 4.3, 4.4, 4.4898, 4.6, 4.8, 5.0, 5.2]:
    best = None
    for y0 in [0.5, 1, 2, 4, 8]:
        for e0 in [0.3, 0.5, 0.7, 0.85, 0.95]:
            r = minimize(lambda v: Phi(a, np.exp(v[0]), 1/(1+np.exp(-v[1]))), [np.log(y0), np.log(e0/(1-e0))], method='Nelder-Mead', options={'xatol':1e-6,'fatol':1e-9,'maxiter':400})
            if best is None or r.fun < best.fun: best = r
    y = np.exp(best.x[0]); eta = 1/(1+np.exp(-best.x[1]))
    print(f"a={a:.4f} min Phi={best.fun:+.6f} at y={y:.4f} eta={eta:.4f}")
