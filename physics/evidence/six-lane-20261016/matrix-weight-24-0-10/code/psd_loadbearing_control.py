"""PSD load-bearing control: a nonnegative INTEGRAL point of the same exact genus-2 affine family that passes every
LINEAR AMH gate (31 parity/triple/rows/KL, 32, 33, 34, 35, 38) but FAILS Eq. (31) block positivity, with an exact
negative certificate v^T B v < 0 (rational v, rational B since all weights are even).
Point: integrality-lattice point nearest the nonnegativity-LP center (no block constraints imposed).
Output: evidence/psd_control_point.json (full AMH-indexed table) + evidence/psd_control_certificate.json.
"""
import json
import sys
from fractions import Fraction

import sympy

from g2_polytope import load_space

sys.path.insert(0, "../frozen-candidate-v1")
from verify_amh import Q3, alp, gam, verify  # noqa: E402  (frozen independent verifier)


def nearest_lattice_point(ref, s0, B):
    BT = sympy.Matrix(B).T
    rhs = sympy.Matrix([sympy.Rational(str(Fraction(r))) - s0[f] for f, r in enumerate(ref)])
    y = BT.LUsolve(rhs)
    yr = [int(sympy.floor(v + sympy.Rational(1, 2))) for v in y]
    return [s0[f] + sum(yr[j] * B[j][f] for j in range(len(s0))) for f in range(len(s0))]


if __name__ == "__main__":
    keys, piv, free, c, V = load_space()
    ref = json.load(open("../evidence/family_lp_center.json"))["s"]
    L = json.load(open("../evidence/int_lattice.json"))
    s = nearest_lattice_point(ref, [int(v) for v in L["s0"]], [[int(v) for v in r] for r in L["B"]])
    x = [c[i] + sum(V[i][f] * s[f] for f in range(len(free))) for i in range(len(keys))]
    assert all(v.denominator == 1 for v in x)
    counts = {json.dumps(keys[i]): int(x[i]) for i in range(len(keys))}
    n = 24
    entries = []
    for i in range(n + 1):
        for j in range(n + 1):
            for t in range(min(i, j) + 1):
                for p in range(t + 1):
                    if i + j <= t + n:
                        v = counts.get(json.dumps([sorted([j - t, i - t, p]), t - p]), 0)
                        if v:
                            entries.append([i, j, t, p, v])
    rep = verify(entries=entries)
    linear_keys = [k for k in rep if k not in ("31_blocks_psd", "31_blocks_failing", "n_blocks", "ALL_PASS")]
    print("linear gates:", {k: rep[k] for k in linear_keys})
    print("PSD failing blocks:", rep["31_blocks_failing"][:10], "count", len(rep["31_blocks_failing"]))
    # exact certificate: first failing block, search a coordinate or 2x2 witness with v^T B v < 0
    lam = {(e[0], e[1], e[2], e[3]): Fraction(e[4]) for e in entries}
    xx = {o: v / gam(*o, n) for o, v in lam.items()}
    a, k = rep["31_blocks_failing"][0]
    idx = list(range(k, n + a - k + 1))
    M = [[Q3(0) for _ in idx] for _ in idx]
    for r, i in enumerate(idx):
        for cc, j in enumerate(idx):
            for t in range(min(i, j) + 1):
                for p in range(t + 1):
                    v = xx.get((i, j, t, p), 0)
                    if v:
                        M[r][cc] += alp(i, j, t, p, a, k, n) * v
    cert = None
    for r in range(len(idx)):
        if M[r][r].sign() < 0:
            cert = {"block": [a, k], "type": "negative diagonal entry", "row_weight_index": idx[r],
                    "v": [int(q == r) for q in range(len(idx))], "vTBv_rational": str(M[r][r].a),
                    "vTBv_sqrt3_part": str(M[r][r].b)}
            break
    if cert is None:
        for r in range(len(idx)):
            for q in range(r + 1, len(idx)):
                if M[r][r].sign() >= 0 and M[q][q].sign() >= 0:
                    # 2x2 minor negative => non-PSD; v = (M_qq, -M_rq) gives v^T B v = M_qq * det
                    det = M[r][r] * M[q][q] - M[r][q] * M[r][q]
                    if det.sign() < 0 and M[q][q].sign() > 0:
                        cert = {"block": [a, k], "type": "negative 2x2 principal minor",
                                "rows": [idx[r], idx[q]], "det_rational": str(det.a), "det_sqrt3": str(det.b)}
                        break
            if cert:
                break
    print("certificate:", cert)
    json.dump({"s": [str(v) for v in s], "entries": entries, "verifier_report": rep},
              open("../evidence/psd_control_point.json", "w"))
    json.dump(cert, open("../evidence/psd_control_certificate.json", "w"), indent=1)
    ok = all(rep[k] for k in linear_keys) and not rep["31_blocks_psd"] and cert is not None
    print("PSD LOAD-BEARING CONTROL:", "OK" if ok else "NOT ESTABLISHED")
