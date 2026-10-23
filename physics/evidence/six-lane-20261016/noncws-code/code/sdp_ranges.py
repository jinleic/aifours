"""Ranges of enumerator-level quantities over the reduced SDP feasible region (exploratory, floating point).

For each j: min/max of A_j(Pi) = K^2 * gamma[j,0,0,0] * x[j,0,0,0] subject to the SDP constraints with
blocks >= 0 (tau fixed at 0). Also reports whether the base optimum violates the NEW constraints.
"""
import argparse
import json

import cvxpy as cp
import numpy as np

from code_sdp import build, residuals
from terwilliger import gamma


def region(n, K, d, sizes, lp, pure, objective_key, sense, solver="CLARABEL"):
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
    obj = K ** 2 * gamma(*objective_key, n) * x[key[objective_key]]
    prob = cp.Problem(cp.Minimize(obj) if sense == "min" else cp.Maximize(obj), cons)
    prob.solve(solver=solver)
    return prob.status, (None if prob.value is None else float(prob.value)), x.value, (Iset, key, eqs, ineqs, blocks)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("K", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("--sizes", default="")
    ap.add_argument("--lp", action="store_true")
    ap.add_argument("--pure", action="store_true")
    a = ap.parse_args()
    sizes = [int(s) for s in a.sizes.split(",") if s]
    out = {}
    for j in range(a.n + 1):
        lo = region(a.n, a.K, a.d, sizes, a.lp, a.pure, (j, 0, 0, 0), "min")
        hi = region(a.n, a.K, a.d, sizes, a.lp, a.pure, (j, 0, 0, 0), "max")
        out[j] = (lo[0], lo[1], hi[0], hi[1])
        print(f"A_{j}: [{lo[1]:.6f}, {hi[1]:.6f}]  ({lo[0]}, {hi[0]})")
    # does the base-region optimum (min A_1) violate new constraints?
    st, val, xv, data = region(a.n, a.K, a.d, [], a.lp, a.pure, (1, 0, 0, 0), "max")
    full = build(a.n, a.K, a.d, partial_trace_sizes=tuple(range(1, a.d)), lp=a.lp, pure=a.pure)
    er, ir, mins = residuals(xv, *full)
    print("base max-A1 point: residuals of NEW families:", {k: v for k, v in er.items() if k.startswith("ptrace")})
