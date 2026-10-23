"""Non-rigorous SP (energetic 1RSB, y=infinity) population dynamics, EXPLORATION ONLY.

Fixed-point map for the warning law R of random k-SAT with Poisson(k alpha/2)
clause degrees per literal sign:

    eta = R_1 ... R_{k-1},
    A_s = prod_{V^s} (1 - eta),  A_u = prod_{V^u} (1 - eta),
    R'  = (1 - A_u) A_s / (A_u + A_s - A_u A_s).

Used to (i) locate the stationary law of Psi_oo, (ii) seed finite-atom trial
laws by quantisation, and (iii) cross-check where the zero-energy complexity
changes sign. Nothing here is a premise of a certified inequality.
"""
import argparse
import json
import time

import numpy as np


def sweep(pop, k, lam, rng, nnew=None):
    n = len(pop) if nnew is None else nnew
    nu = rng.poisson(lam, n)
    ns = rng.poisson(lam, n)
    tot_u, tot_s = nu.sum(), ns.sum()

    def log1m_eta(count):
        idx = rng.integers(0, len(pop), size=(count, k - 1))
        eta = np.prod(pop[idx], axis=1)
        return np.log1p(-eta)

    lu = log1m_eta(tot_u)
    ls = log1m_eta(tot_s)
    seg_u = np.repeat(np.arange(n), nu)
    seg_s = np.repeat(np.arange(n), ns)
    logAu = np.bincount(seg_u, weights=lu, minlength=n)
    logAs = np.bincount(seg_s, weights=ls, minlength=n)
    Au, As = np.exp(logAu), np.exp(logAs)
    denom = Au + As - Au * As
    return (1.0 - Au) * As / denom


def complexity(pop, k, alpha, rng, nsamp):
    lam = k * alpha / 2
    na = rng.poisson(lam, nsamp)
    nb = rng.poisson(lam, nsamp)

    def logprod(counts):
        tot = counts.sum()
        idx = rng.integers(0, len(pop), size=(tot, k - 1))
        eta = np.prod(pop[idx], axis=1)
        seg = np.repeat(np.arange(len(counts)), counts)
        return np.bincount(seg, weights=np.log1p(-eta), minlength=len(counts))

    A, B = np.exp(logprod(na)), np.exp(logprod(nb))
    site = np.log(A + B - A * B)
    idx = rng.integers(0, len(pop), size=(nsamp, k))
    clause = np.log1p(-np.prod(pop[idx], axis=1))
    s_mean, s_se = site.mean(), site.std() / np.sqrt(nsamp)
    c_mean, c_se = clause.mean(), clause.std() / np.sqrt(nsamp)
    return s_mean - (k - 1) * alpha * c_mean, s_se, c_se


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--k', type=int, required=True)
    ap.add_argument('--alpha', type=float, required=True)
    ap.add_argument('--pop', type=int, default=200000)
    ap.add_argument('--sweeps', type=int, default=200)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    lam = a.k * a.alpha / 2
    pop = rng.uniform(0.0, 1.0, a.pop)
    t0 = time.time()
    for s in range(a.sweeps):
        pop = sweep(pop, a.k, lam, rng)
    q = np.quantile(pop, np.linspace(0, 1, 11))
    print('k', a.k, 'alpha', a.alpha, 'quantiles', np.round(q, 4).tolist(), 'mean', pop.mean(), 'time', round(time.time() - t0, 1), flush=True)
    if a.out:
        np.save(a.out, np.sort(pop))


if __name__ == '__main__':
    main()
