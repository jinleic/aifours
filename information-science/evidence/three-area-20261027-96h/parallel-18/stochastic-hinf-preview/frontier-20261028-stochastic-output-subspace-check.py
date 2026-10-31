#!/usr/bin/env python3
"""Exact subspace checks plus bounded actual-SDE moment illustrations."""
from fractions import Fraction as F
import json
import math
import random


def mv(M, v):
    return tuple(sum((a*b for a, b in zip(row, v)), F(0)) for row in M)


def rank(vectors):
    if not vectors:
        return 0
    rows = [list(v) for v in vectors]
    r = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        fac = rows[r][col]
        rows[r] = [x / fac for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                fac = rows[i][col]
                rows[i] = [a - fac*b for a, b in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def basis(vectors):
    out = []
    for v in vectors:
        if rank(out + [v]) > len(out):
            out.append(v)
    return out


def closure(seeds, mats):
    out = basis(seeds)
    dims = [len(out)]
    while True:
        nxt = basis(out + [mv(M, v) for M in mats for v in out])
        if len(nxt) == len(out):
            return out, dims
        out = nxt
        dims.append(len(out))


def certificate(P, Q, Fcol, Gcol, O):
    rd, rd_dims = closure([Fcol], [P])
    d0 = basis([Gcol] + [mv(Q, v) for v in rd])
    d, dims = closure(d0, [P, Q])
    visible = [sum((a*b for a, b in zip(O, v)), F(0)) for v in d]
    oq = [sum((O[i] * Q[i][j] for i in range(len(O))), F(0)) for j in range(len(O))]
    return {"deterministic_reachable_dims": rd_dims,
            "diffusion_word_dims": dims,
            "visible_on_basis": [str(x) for x in visible],
            "old_OQ_row": [str(x) for x in oq],
            "deterministic_output_test": all(x == 0 for x in visible)}


def main():
    z, one = F(0), F(1)
    a, sigma, kappa = F(6,5), F(2,5), F(7,10)
    P = ((-a,z,z),(z,z,z),(z,z,z))
    Q = ((z,z,kappa),(z,sigma,z),(z,z,z))
    Fcol, Gcol, O = (one,z,z), (z,one,z), (-a,z,z)
    hidden = certificate(P,Q,Fcol,Gcol,O)
    if not hidden["deterministic_output_test"] or all(x == "0" for x in hidden["old_OQ_row"]):
        raise RuntimeError("hidden diffusion extension check failed")

    Z = ((z,z,z),(z,z,z),(z,z,z))
    cascade_Q = ((z,one,z),(z,z,one),(z,z,z))
    cascade = certificate(Z,cascade_Q,(z,z,z),(z,z,one),(one,z,z))
    if cascade["deterministic_output_test"] or cascade["diffusion_word_dims"] != [1,2,3]:
        raise RuntimeError("three-noise cascade check failed")
    # X1=(W^3-3tW)/6: E[X1^2]=(15-18+9)t^3/36=t^3/6.
    variance_coefficient = (F(15)-F(18)+F(9))/36
    if variance_coefficient != F(1,6):
        raise RuntimeError("cascade Gaussian variance identity failed")

    empty = certificate(Z,cascade_Q,(z,z,z),(z,z,z),(one,z,z))
    if not empty["deterministic_output_test"] or empty["diffusion_word_dims"] != [0]:
        raise RuntimeError("zero forcing degeneracy failed")

    rng = random.Random(20261028)
    n, steps = 12000, 96
    dt = 1.0/steps
    hidden_x2_sq = cascade_x1_sum = cascade_x1_sq = 0.0
    for _ in range(n):
        W = x2 = 0.0
        for _j in range(steps):
            dw = rng.gauss(0.0, math.sqrt(dt))
            x2 += (float(sigma)*x2 + 1.0)*dw
            W += dw
        x1 = (W**3-3.0*W)/6.0
        hidden_x2_sq += x2*x2
        cascade_x1_sum += x1
        cascade_x1_sq += x1*x1
    result = {
        "hidden_actual_system": "dx1=(-6/5*x1+w)dt+7/10*x3*dW; dx2=(2/5*x2+w)dW; dx3=0; z=w-6/5*x1",
        "hidden_exact_subspace": hidden,
        "cascade_actual_system": "dx3=w dW; dx2=x3 dW; dx1=x2 dW; z=x1; w=1",
        "cascade_exact_subspace": cascade,
        "cascade_exact_output_variance_coefficient": str(variance_coefficient),
        "zero_forcing": empty,
        "sample_hidden_x2_second_moment": hidden_x2_sq/n,
        "continuous_hidden_x2_second_moment": (math.exp(float(sigma*sigma))-1.0)/float(sigma*sigma),
        "sample_cascade_x1_mean": cascade_x1_sum/n,
        "sample_cascade_x1_second_moment": cascade_x1_sq/n,
        "exact_cascade_x1_second_moment": str(variance_coefficient),
        "seed": 20261028, "paths": n, "steps": steps,
        "limits": "Rational matrix arithmetic is exact only for these tests; Monte Carlo/Euler values do not prove the universal characterization."
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
