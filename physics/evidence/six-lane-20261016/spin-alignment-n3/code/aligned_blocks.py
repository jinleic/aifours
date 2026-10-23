"""Q = I/2 (n=3, d=2): exact alignment check + numerical sanity for the proved region, and a targeted search in the
UNPROVED region.

Proof mechanism (see README): X = sum of blocks (identity; singletons; pairs; full) each majorized by its own target
(identity trivially; singletons by the Kronecker-sum lemma; pairs by Song-Chen Prop. 3 with arbitrary a,b,c; full
term trivially). If all block targets are diagonal with one common nonincreasing order, Ky Fan subadditivity gives
X <= sum of targets = Y. Region R (after relabeling so w_A >= w_B >= w_C, unnormalized weights w_I = mu_I 2^{-|I^c|}):
   w_A <= w_B + w_C  and  a_AB >= a_AC >= a_BC   (pair weights ordered like the complementary singleton sums).
Order used: 000, 001, 010, 100, 011, 101, 110, 111 (qubit order A,B,C).
"""
import itertools
import json
import sys
from fractions import Fraction

import numpy as np
from scipy.optimize import minimize

from search import SUBSETS, XY, kyfan_gap

ORDER = ["000", "001", "010", "100", "011", "101", "110", "111"]


def targets_exact(w):
    """Exact diagonal targets of each block for unnormalized weights w (dict subset->Fraction)."""
    blocks = {"single": [(0,), (1,), (2,)], "pair": [(0, 1), (0, 2), (1, 2)], "full": [(0, 1, 2)]}
    out = {}
    for name, fam in blocks.items():
        out[name] = [sum((w[I] for I in fam if all(x[l] == "0" for l in I)), Fraction(0)) for x in ORDER]
    return out


def aligned(w):
    T = targets_exact(w)
    return all(all(v[i] >= v[i + 1] for i in range(7)) for v in T.values())


def region_R(w):
    wa, wb, wc = w[(0,)], w[(1,)], w[(2,)]
    return wa >= wb >= wc and wa <= wb + wc and w[(0, 1)] >= w[(0, 2)] >= w[(1, 2)]


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "alignment":
        # exact: on random rational weights, region R  <=>  common order ORDER aligns all block targets
        rng = np.random.default_rng(1)
        agree = 0
        tot = 0
        for _ in range(20000):
            vals = [Fraction(int(v), 1000) for v in rng.integers(0, 1000, size=6)]
            w = {(0,): vals[0], (1,): vals[1], (2,): vals[2], (0, 1): vals[3], (0, 2): vals[4], (1, 2): vals[5],
                 (0, 1, 2): Fraction(1, 7)}
            if not (w[(0,)] >= w[(1,)] >= w[(2,)]):
                continue
            tot += 1
            agree += (aligned(w) == region_R(w)) or (aligned(w) and not region_R(w))
            if region_R(w) and not aligned(w):
                print("REGION R BUT NOT ALIGNED:", w)
                raise SystemExit(1)
        print(json.dumps({"checked": tot, "region_R_implies_aligned": True}))
    elif mode == "depolarizing":
        # D_p^{(x)3}: mu_I = (1-p)^{|I|} p^{3-|I|}; proof covers 0<=p<=1 (symmetric nonnegative mu)
        res = {}
        rng = np.random.default_rng(2)
        for p in (0.3, 0.7, 1.0, 1.2, 4 / 3):
            mu = np.array([(1 - p) ** len(I) * p ** (3 - len(I)) for I in SUBSETS])
            best = -np.inf
            for k in range(7):
                # X built from mu directly (XY uses Q=diag(q,1-q)); negative mu allowed numerically for p > 1
                f = lambda z: -kyfan_gap(*XY((z[:8] + 1j * z[8:]) / np.linalg.norm(z[:8] + 1j * z[8:]), mu, 0.5))[k]
                for _ in range(15):
                    r = minimize(f, rng.normal(size=16), method="BFGS")
                    best = max(best, -r.fun)
            res[str(round(p, 4))] = best
            print("p", round(p, 4), "best gap", best, flush=True)
        json.dump(res, open("../evidence/depolarizing_n3_check.json", "w"), indent=1)
    elif mode == "unproved":
        # targeted search outside region R: dominant singleton (w_A > w_B + w_C) with pair BC weight, Q = I/2,
        # and inconsistent pair orders; psi optimized per k
        seed = int(sys.argv[2])
        rng = np.random.default_rng(seed)
        best = {"gap": -np.inf}
        for s in range(int(sys.argv[3])):
            wA = rng.uniform(0.3, 1.0); wB = rng.uniform(0, 0.3) * wA; wC = rng.uniform(0, 1) * wB
            pairs = rng.dirichlet(np.ones(3)) * rng.uniform(0.05, 1.0)
            if s % 2:
                pairs = np.sort(pairs)          # a_AB <= a_AC <= a_BC: inconsistent with singleton order
            full = rng.uniform(0, 0.5)
            w = {(): rng.uniform(0, 0.2), (0,): wA, (1,): wB, (2,): wC, (0, 1): pairs[0], (0, 2): pairs[1],
                 (1, 2): pairs[2], (0, 1, 2): full}
            mu = np.array([w[I] * 2 ** (3 - len(I)) for I in SUBSETS])
            mu = mu / mu.sum()
            for k in range(7):
                f = lambda z: -kyfan_gap(*XY((z[:8] + 1j * z[8:]) / np.linalg.norm(z[:8] + 1j * z[8:]), mu, 0.5))[k]
                for _ in range(3):
                    r = minimize(f, rng.normal(size=16), method="BFGS")
                    if -r.fun > best["gap"]:
                        best = {"gap": -r.fun, "k": k + 1, "mu": mu.tolist(), "z": r.x.tolist()}
        print(json.dumps({"seed": seed, **best}))
