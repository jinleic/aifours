"""Batch re-test of fully-closed marginal boxes with an exhaustive six-chart LP (exploratory).

Usage: python closed_recheck.py LIST.txt OUT.jsonl [WORKERS] [DPS]
LIST.txt lines: "<records.jsonl> <n> <it>".  For each record:
  1. rebuild the endpoint polynomials in DPS-digit arithmetic (mpmath);
  2. verify the n-2 contact conditions, compute the contact singular values (rank check) and an
     orthonormal basis v1..v3 of their null space;
  3. on a log grid (4000 points over the band range +- 3 decades plus 16 points around every x_i,
     never at x_i) form rows r = (P_c(t; v_k)/|K_c(jw)|^2)_k for the four corners, normalized to unit
     length (rows computed in mpmath, then rounded to float64);
  4. decide grid feasibility of {lambda != 0 : R lambda >= 0} exhaustively with six charts
     lambda_q = +-1, |lambda_j| <= 1 (every nonzero lambda can be scaled into one chart): in each
     chart solve max s s.t. R lambda >= s; feasible iff some chart has s >= 0 (witness lambda);
  5. validate the best witness: min of R lambda over all rows (float), coefficient signs and
     beta(j w) != 0 checks of beta = sum lambda_k v_k evaluated in mpmath.
Outcome labels: "grid-feasible" (witness with min_row >= -1e-12), "grid-infeasible" (all six
chart optima < 0), or "solver-issue".  Not a continuum certificate.
"""
from __future__ import annotations

import json
import sys
from multiprocessing import Pool

import mpmath as mp
import numpy as np
from scipy.optimize import linprog

from closed_exact3 import basis_row, decode_mp, endpoints_mp, pder, pval


def build_rows(rec, n, dps):
    mp.mp.dps = dps
    x, llo, lhi = decode_mp(rec["u"], n)
    (Em, Ep), (Om, Op) = endpoints_mp(x, n, llo, lhi)
    Es, Os = (Em, Ep), (Om, Op)
    C = []
    for xi in x[1:n - 1]:
        ie = min((0, 1), key=lambda i: abs(pval(Es[i], xi)))
        io = min((0, 1), key=lambda i: abs(pval(Os[i], xi)))
        tol = mp.mpf(10) ** (-dps // 2)
        if abs(pval(Es[ie], xi)) > tol or abs(pval(Os[io], xi)) > tol:
            raise ValueError("contact corner not found")
        row = basis_row(n, xi, pval(pder(Es[ie]), xi), pval(pder(Os[io]), xi))
        nr = mp.sqrt(mp.fsum([v * v for v in row]))
        C.append([v / nr for v in row])
    U, S, V = mp.svd_r(mp.matrix(C), full_matrices=True)
    sv = [float(S[i]) for i in range(len(S))]
    null = [[V[r, c] for c in range(n + 1)] for r in range(n - 2, n + 1)]
    lx = [mp.log10(v) for v in x]
    ts = [mp.mpf(10) ** (lx[0] - 3 + (lx[-1] - lx[0] + 6) * mp.mpf(i) / 3999) for i in range(4000)]
    for xi in x:
        for d in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 1e-6]:
            ts += [xi * (1 - mp.mpf(d)), xi * (1 + mp.mpf(d))]
    ts = [mp.mpf(0)] + sorted(ts)
    rows = []
    for t in ts:
        for i in (0, 1):
            for j in (0, 1):
                Ev, Ov = pval(Es[i], t), pval(Os[j], t)
                den = Ev * Ev + t * Ov * Ov
                if den == 0:
                    continue
                b = basis_row(n, t, Ev, Ov)
                r = [mp.fsum([b[k] * vec[k] for k in range(n + 1)]) / den for vec in null]
                nr = mp.sqrt(mp.fsum([v * v for v in r]))
                if nr > 0:
                    rows.append([float(v / nr) for v in r])
    return np.array(rows), null, sv, x


def six_charts(R):
    best = None
    for q in range(3):
        for sgn in (1.0, -1.0):
            bounds = [(-1, 1)] * 3 + [(None, 1)]
            bounds[q] = (sgn, sgn)
            res = linprog([0, 0, 0, -1], A_ub=np.hstack([-R, np.ones((len(R), 1))]),
                          b_ub=np.zeros(len(R)), bounds=bounds, method="highs")
            if res.status != 0:
                return None, "solver-issue"
            if best is None or res.x[-1] > best[0]:
                best = (res.x[-1], res.x[:3].copy())
    return best, None


def one(args):
    path, n, it, dps = args
    try:
        rec = next(json.loads(l) for l in open(path) if json.loads(l)["it"] == it)
        R, null, sv, x = build_rows(rec, n, dps)
        best, err = six_charts(R)
        if err:
            return {"file": path, "n": n, "it": it, "outcome": err}
        s, lam = best
        minrow = float((R @ lam).min())
        mp.mp.dps = dps
        beta = [mp.fsum([mp.mpf(float(lam[q])) * null[q][k] for q in range(3)]) for k in range(n + 1)]
        bmax = max(abs(v) for v in beta)
        signs = [int(mp.sign(v)) if abs(v) > bmax * mp.mpf(10) ** -30 else 0 for v in beta]
        outcome = "grid-feasible" if minrow >= -1e-12 else ("grid-infeasible" if s < 0 else "solver-issue")
        return {"file": path, "n": n, "it": it, "outcome": outcome, "chart_max": float(s),
                "min_row_at_witness": minrow, "contact_sv_min": min(sv), "contact_sv_max": max(sv),
                "rows": int(len(R)), "beta_signs": signs,
                "beta": [mp.nstr(v / bmax, 12) for v in beta], "orig_lp_s": rec.get("s")}
    except Exception as e:  # pragma: no cover
        return {"file": path, "n": n, "it": it, "outcome": "error", "error": repr(e)}


def main():
    lst, out = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    dps = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    tasks = []
    for line in open(lst):
        if line.strip():
            p, n, it = line.split()
            tasks.append((p, int(n), int(it), dps))
    counts = {}
    with Pool(workers) as pool, open(out, "w") as fh:
        for r in pool.imap_unordered(one, tasks):
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            counts[(r["n"], r["outcome"])] = counts.get((r["n"], r["outcome"]), 0) + 1
    print(json.dumps({f"n={k[0]} {k[1]}": v for k, v in sorted(counts.items())}))


if __name__ == "__main__":
    main()
