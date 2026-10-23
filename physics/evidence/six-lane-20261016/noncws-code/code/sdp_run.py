"""Solve the symmetry-reduced Gamma-SDP feasibility problem with optional NEW partial-trace constraints.

Formulation: maximize tau subject to all linear constraints and every block B_(a,k)(x) - tau*D_(a,k) >= 0,
where D_(a,k) is the (positive diagonal) image of the identity orbit vector. tau* < 0 means infeasible
(numerically); tau* >= 0 means feasible. Floating-point only: a negative tau* is a PROPOSAL that must be
certified by an exact dual certificate before any claim.
"""
import argparse
import json
import time

import cvxpy as cp
import numpy as np

from code_sdp import build


def solve(n, K, d, sizes=(), lp=False, pure=False, solver="CLARABEL", verbose=False, tau_cap=1.0):
    Iset, key, eqs, ineqs, blocks = build(n, K, d, partial_trace_sizes=tuple(sizes), lp=lp, pure=pure)
    x = cp.Variable(len(Iset))
    tau = cp.Variable()
    cons = []
    for row, rhs, tag in eqs:
        cons.append(sum(c * x[key[o]] for o, c in row.items()) == rhs)
    for row, rhs, tag in ineqs:
        cons.append(sum(c * x[key[o]] for o, c in row.items()) >= rhs)
    xid = {o: (1.0 if (o[0] == o[1] == o[2] == o[3]) else 0.0) for o in Iset}
    for a, k, M in blocks:
        m = len(M)
        expr = [[0 for _ in range(m)] for _ in range(m)]
        for r in range(m):
            for c in range(m):
                ent = M[r][c]
                if ent:
                    expr[r][c] = sum(cf * x[key[o]] for o, cf in ent.items())
                else:
                    expr[r][c] = cp.Constant(0.0)
        Bx = cp.bmat(expr)
        Dv = np.array([[sum(cf * xid[o] for o, cf in M[r][c].items()) for c in range(m)] for r in range(m)])
        S = cp.Variable((m, m), symmetric=True)
        cons.append(S == (Bx + Bx.T) / 2 - tau * Dv)
        cons.append(S >> 0)
    cons.append(tau <= tau_cap)
    prob = cp.Problem(cp.Maximize(tau), cons)
    t0 = time.time()
    try:
        prob.solve(solver=solver, verbose=verbose)
    except Exception as e:  # noqa
        return {"status": "solver_error", "error": str(e)}
    return {"n": n, "K": K, "d": d, "sizes": list(sizes), "lp": lp, "pure": pure, "solver": solver,
            "status": prob.status, "tau": None if tau.value is None else float(tau.value),
            "n_vars": len(Iset), "n_eqs": len(eqs), "n_blocks": len(blocks),
            "seconds": round(time.time() - t0, 2),
            "x": None if x.value is None else x.value.tolist()}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("n", type=int)
    ap.add_argument("K", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("--sizes", default="")
    ap.add_argument("--lp", action="store_true")
    ap.add_argument("--pure", action="store_true")
    ap.add_argument("--solver", default="CLARABEL")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    sizes = [int(s) for s in a.sizes.split(",") if s]
    r = solve(a.n, a.K, a.d, sizes, a.lp, a.pure, a.solver)
    xs = r.pop("x", None)
    print(json.dumps(r))
    if a.out:
        r["x"] = xs
        json.dump(r, open(a.out, "w"))
