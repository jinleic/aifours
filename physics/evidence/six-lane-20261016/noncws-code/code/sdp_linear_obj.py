"""Optimize an arbitrary linear functional of the enumerator A_j(Pi) over the reduced SDP region.
Exploratory floating point. Objective given as coefficients on A_0..A_n (unnormalized, AMH convention)
or by name: S<j> (shadow), KBA<j> (K B_j - A_j), A<j>.
"""
import argparse
import json

import cvxpy as cp
import numpy as np

from code_sdp import build
from qlp import kraw
from terwilliger import gamma


def objective_coeffs(name, n, K):
    c = np.zeros(n + 1)
    if name.startswith("S"):
        j = int(name[1:])
        for i in range(n + 1):
            c[i] = (-1) ** i * kraw(j, i, n) / 2 ** n
    elif name.startswith("KBA"):
        j = int(name[3:])
        for i in range(n + 1):
            c[i] = K * kraw(j, i, n) / 2 ** n
        c[j] -= 1
    elif name.startswith("A"):
        c[int(name[1:])] = 1
    return c


def optimize(n, K, d, sizes, lp, pure, coeffs, sense, solver="CLARABEL", extra_eq=None):
    Iset, key, eqs, ineqs, blocks = build(n, K, d, partial_trace_sizes=tuple(sizes), lp=lp, pure=pure)
    x = cp.Variable(len(Iset))
    cons = []
    for row, rhs, tag in eqs:
        cons.append(sum(c * x[key[o]] for o, c in row.items()) == rhs)
    for row, rhs, tag in ineqs:
        cons.append(sum(c * x[key[o]] for o, c in row.items()) >= rhs)
    for a, k, M in blocks:
        m = len(M)
        expr = [[(sum(cf * x[key[o]] for o, cf in M[r][c].items()) if M[r][c] else cp.Constant(0.0))
                 for c in range(m)] for r in range(m)]
        Bx = cp.bmat(expr)
        S = cp.Variable((m, m), symmetric=True)
        cons += [S == (Bx + Bx.T) / 2, S >> 0]
    A = [K ** 2 * gamma(j, 0, 0, 0, n) * x[key[(j, 0, 0, 0)]] for j in range(n + 1)]
    if extra_eq:
        for cf, val in extra_eq:
            cons.append(sum(cf[j] * A[j] for j in range(n + 1)) == val)
    obj = sum(coeffs[j] * A[j] for j in range(n + 1))
    prob = cp.Problem(cp.Minimize(obj) if sense == "min" else cp.Maximize(obj), cons)
    prob.solve(solver=solver)
    Av = None if x.value is None else [float(K ** 2 * gamma(j, 0, 0, 0, n) * x.value[key[(j, 0, 0, 0)]]) for j in range(n + 1)]
    return prob.status, (None if prob.value is None else float(prob.value)), Av


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("K", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("objs")
    ap.add_argument("--sizes", default="")
    ap.add_argument("--lp", action="store_true")
    ap.add_argument("--pure", action="store_true")
    a = ap.parse_args()
    sizes = [int(s) for s in a.sizes.split(",") if s]
    for name in a.objs.split(","):
        c = objective_coeffs(name, a.n, a.K)
        lo = optimize(a.n, a.K, a.d, sizes, a.lp, a.pure, c, "min")
        hi = optimize(a.n, a.K, a.d, sizes, a.lp, a.pure, c, "max")
        print(json.dumps({"obj": name, "min": lo[1], "max": hi[1], "status": [lo[0], hi[0]],
                          "A_at_min": lo[2], "A_at_max": hi[2]}))
