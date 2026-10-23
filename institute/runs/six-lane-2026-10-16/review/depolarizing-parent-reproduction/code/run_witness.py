#!/usr/bin/env python3
"""Evaluate the pinned witness with the independent evaluator sym_depol.py.

Example:
  OMP_NUM_THREADS=4 VECLIB_MAXIMUM_THREADS=4 python run_witness.py --p 1/5 --Dout 440 \
      --out ../evidence/ic_p1_5_D440.json
"""
import argparse
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import mpmath
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sym_depol import (LogFact, BWindows, apply_SN, assemble, partial_trace_factor,  # noqa: E402
                       entropy_nats, coherent_information)

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESS = os.path.normpath(os.path.join(
    HERE, "../../depolarizing-parent-inputs-v1/evidence/cert/witness_g3_M2000_p1_5.json"))


def load_witness(path=WITNESS):
    raw = open(path, "rb").read()
    W = json.loads(raw)
    phis_exact = [[Fraction(float.fromhex(s)) for s in a] for a in W["amps"]]
    phis = [np.array([float(v) for v in a]) for a in phis_exact]
    norms2 = [sum(v * v for v in a) for a in phis_exact]          # exact rationals
    return W, phis, phis_exact, norms2, hashlib.sha256(raw).hexdigest()


def exact_log_weights(M, p_frac, dps=60):
    """log p_r with mpmath at dps digits from the exact rational p (tr X = 1)."""
    mpmath.mp.dps = dps
    p = mpmath.mpf(p_frac.numerator) / p_frac.denominator
    eta = 1 - 4 * p / 3
    f = (1 - eta) / 2
    out, tot = [], mpmath.mpf(0)
    for r in range(M // 2 + 1):
        N = M - 2 * r
        mr = mpmath.binomial(M, r) - (mpmath.binomial(M, r - 1) if r > 0 else 0)
        val = mr * (f * (1 - f)) ** r * ((1 - f) ** (N + 1) - f ** (N + 1)) / (1 - 2 * f)
        tot += val
        out.append(float(mpmath.log(val)))
    return np.array(out), float(tot - 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--p", default="1/5")
    ap.add_argument("--Dout", type=int, default=440)
    ap.add_argument("--tail", type=float, default=-60.0, help="keep blocks with log p_r > tail")
    ap.add_argument("--norm", choices=["exact", "raw"], default="exact")
    ap.add_argument("--perturb", type=float, default=0.0,
                    help="relative random perturbation of amplitudes (rounding-sensitivity test)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    t0 = time.time()
    W, phis, phis_exact, norms2, wsha = load_witness()
    M = int(W["M"])
    p_frac = Fraction(args.p)
    eta_frac = 1 - Fraction(4, 3) * p_frac
    eta = float(eta_frac)
    q = [float(Fraction(s)) for s in W["q"]]
    mpmath.mp.dps = 60
    if args.norm == "exact":
        inv = [float(1 / mpmath.sqrt(mpmath.mpf(n.numerator) / n.denominator)) for n in norms2]
        phis = [ph * c for ph, c in zip(phis, inv)]
    if args.perturb:
        rng = np.random.default_rng(args.seed)
        phis = [ph * (1 + args.perturb * rng.uniform(-1, 1, size=ph.size)) for ph in phis]
    logp, wsum_err = exact_log_weights(M, p_frac)
    rs = [r for r in range(M // 2 + 1) if logp[r] > args.tail]
    excl = math.fsum(math.exp(v) for r, v in enumerate(logp) if r not in set(rs))
    lf = LogFact(M + 2)
    res = coherent_information(phis, q, M, eta, Dout=args.Dout, rs=rs, lf=lf, verbose=True)
    # replace float log-weights by the mpmath ones (identical up to ~1e-13 relative)
    for b in res["blocks"]:
        b["p_float"] = b["p"]
        b["logp"] = float(logp[b["r"]])
        b["p"] = math.exp(logp[b["r"]])
    Ic = math.fsum(b["p"] * b["dS"] for b in res["blocks"])
    Ic_float_weights = math.fsum(b["p_float"] * b["dS"] for b in res["blocks"])
    out = dict(
        witness_sha256=wsha, M=M, p=str(p_frac), eta=str(eta_frac), eta_float=eta, q=W["q"],
        Dout=args.Dout, tail_logp=args.tail, norm=args.norm, perturb=args.perturb, seed=args.seed,
        exact_norm2_minus_1=[float(n - 1) for n in norms2],
        overlap_exact=str(sum(a * b for a, b in zip(phis_exact[0], phis_exact[1]))),
        r_min=min(rs), r_max=max(rs), nblocks=len(rs),
        p_weights_sum_minus_1_mpmath=wsum_err, p_excluded=excl,
        bound_excluded_contribution=excl * math.log(2),
        Ic_nats=Ic, Ic_bits=Ic / math.log(2), Ic_nats_floatweights=Ic_float_weights,
        max_abs_deficit=max(abs(b["deficit"]) for b in res["blocks"]),
        max_diag_tail=max(b["diag_tail"] for b in res["blocks"]),
        min_ev_B=min(b["min_evB"] for b in res["blocks"]),
        min_ev_RB=min(b["min_evRB"] for b in res["blocks"]),
        seconds=time.time() - t0,
        blocks=res["blocks"],
    )
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    print("I_c = %.10e nats = %.10e bits  (blocks %d, r in [%d,%d], excluded p %.2e, %.0fs)"
          % (Ic, Ic / math.log(2), len(rs), min(rs), max(rs), excl, out["seconds"]))


if __name__ == "__main__":
    main()
