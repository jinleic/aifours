"""Rigorous (arb + exact rationals) lower bound for the exact exponent at M_t, t = 3/4, d = 9 (exploratory screen).

Psi_d(M) = (1 - d/2) ln 4 + (d/2) ln d + ((d-1)/4) sum m ln m - (1/4) min_{l in L(M)} sum_e l_e ln l_e.
ANY feasible l gives min <= sum l ln l, hence a rigorous LOWER bound on Psi_d(M).
At M_t (diagonal m_D = (1+3t)/4, off-diagonal m_O = (1-t)/4) use l constant on the three edge types
  D-D (6 edges), D-O (24 edges), O-O (42 edges); each D cell has 3 D- and 6 O-neighbours, each O cell 2 D- and 7 O-.
Feasibility: 3 l_DD + 6 l_DO = d m_D,  2 l_DO + 7 l_OO = d m_O,  l >= 0.
Choose rational l_DO near the entropy optimum; l_DD, l_OO then follow exactly.
Also gives a rigorous UPPER bound for comparison via weak duality U_lam with a rational dual lam (constant per type),
and repeats both for d = 8 (where the centre should win at this point).
Writes ../evidence/d9_failure_enclosure.json.
"""
import json
import os
from fractions import Fraction as Fr

from flint import arb, ctx

ctx.prec = 200


def A(x):
    return arb(x.numerator) / arb(x.denominator) if isinstance(x, Fr) else arb(x)


def xlnx(x):
    return arb(0) if x == 0 else A(x) * A(x).log()


def centre(d):
    return (2 - d) * arb(4).log() + d * arb(3).log()


def bounds_at(t, d):
    mD = (1 + 3 * t) / 4
    mO = (1 - t) / 4
    cD, cO = d * mD, d * mO
    ent = 4 * xlnx(mD) + 12 * xlnx(mO)
    base = (1 - arb(d) / 2) * arb(4).log() + arb(d) / 2 * arb(d).log() + arb(d - 1) / 4 * ent
    # numerical optimum of product form x_D, x_O (float Newton), then rationalise l_DO
    xD, xO = 1.0, 0.2
    for _ in range(200):
        f1 = xD * (3 * xD + 6 * xO) - float(cD)
        f2 = xO * (2 * xD + 7 * xO) - float(cO)
        j11, j12 = 6 * xD + 6 * xO, 6 * xD
        j21, j22 = 2 * xO, 2 * xD + 14 * xO
        det = j11 * j22 - j12 * j21
        xD, xO = xD - (f1 * j22 - f2 * j12) / det, xO - (j11 * f2 - j21 * f1) / det
    lDO = Fr(round(xD * xO * 10 ** 12), 10 ** 12)
    lDD = (cD - 6 * lDO) / 3
    lOO = (cO - 2 * lDO) / 7
    feasible = lDD >= 0 and lOO >= 0 and lDO >= 0
    primal = 6 * xlnx(lDD) + 24 * xlnx(lDO) + 42 * xlnx(lOO)
    lower = base - primal / 4
    # weak-duality upper bound with rational dual lam_D = ln xD, lam_O = ln xO (rationalised x)
    XD, XO = Fr(round(xD * 10 ** 12), 10 ** 12), Fr(round(xO * 10 ** 12), 10 ** 12)
    lamD, lamO = A(XD).log(), A(XO).log()
    dual = (4 * A(cD) * lamD + 12 * A(cO) * lamO) - (6 * A(XD * XD) + 24 * A(XD * XO) + 42 * A(XO * XO))
    upper = base - (dual + 2 * d) / 4
    c = centre(d)
    return {
        "t": str(t), "d": d, "l_DD, l_DO, l_OO (exact rationals)": [str(lDD), str(lDO), str(lOO)],
        "primal feasible": bool(feasible),
        "rigorous lower bound Psi(M_t) - Psi(J)": str(lower - c),
        "rigorous upper bound Psi(M_t) - Psi(J) (weak duality)": str(upper - c),
        "lower > 0 (certain)": bool(lower - c > 0),
        "upper < 0 (certain)": bool(upper - c < 0),
    }


def main():
    out = {"note": "rigorous enclosures at single points; exploratory screen; no claim beyond these points"}
    out["d=9, t=3/4"] = bounds_at(Fr(3, 4), 9)
    out["d=8, t=3/4"] = bounds_at(Fr(3, 4), 8)
    out["d=8, t=2/3"] = bounds_at(Fr(2, 3), 8)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "d9_failure_enclosure.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
