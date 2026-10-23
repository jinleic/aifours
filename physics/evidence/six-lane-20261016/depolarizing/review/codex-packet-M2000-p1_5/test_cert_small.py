"""Targeted smoke check of cert.py against brute force (2^M dims) at small M.

Cases: nonnegative mod-3 rank-2 codes (fast path), signed real and complex general rank-2 inputs
(positive-part splitting, k=None), both signs of I_c.  Enclosures must contain the brute-force value.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction

import numpy as np

from brute import brute_ic
from cert import certify


def wit(M, p, qs, amps, k=None, residues=None, D=None):
    rows = []
    for c in amps:
        if np.iscomplexobj(c):
            rows.append([[float(z.real).hex(), float(z.imag).hex()] for z in c])
        else:
            rows.append([float(z).hex() for z in c])
    return {"M": M, "p": str(p), "q": [str(q) for q in qs], "amps": rows, "k": k, "residues": residues,
            "D": D if D is not None else M}


def main():
    rng = np.random.default_rng(7)
    fails = 0
    cases = []
    for M in (4, 6, 7):
        for p in (Fraction(1, 10), Fraction(19, 100), Fraction(1, 4)):
            c0 = np.array([rng.uniform(0.1, 1) if j % 3 == 0 else 0.0 for j in range(M + 1)])
            c1 = np.array([rng.uniform(0.1, 1) if j % 3 == 1 else 0.0 for j in range(M + 1)])
            cases.append((M, p, [Fraction(9, 20), Fraction(11, 20)], [c0, c1], 3, [0, 1]))
        # signed real general
        c0 = rng.normal(size=M + 1)
        c1 = rng.normal(size=M + 1)
        cases.append((M, Fraction(3, 20), [Fraction(1, 3), Fraction(2, 3)], [c0, c1], None, None))
        # complex general
        c0 = rng.normal(size=M + 1) + 1j * rng.normal(size=M + 1)
        c1 = rng.normal(size=M + 1) + 1j * rng.normal(size=M + 1)
        cases.append((M, Fraction(1, 5), [Fraction(1, 2), Fraction(1, 2)], [c0, c1], None, None))
    for (M, p, qs, amps, k, res) in cases:
        w = wit(M, p, qs, amps, k, res)
        summ, _ = certify(w, None, ptail=0.0, pitail=0.0, verbose=False)
        eta = float(1 - Fraction(4, 3) * p)
        # brute force uses normalized vectors, weights q; purification sum sqrt(q) |i>|c_i/||c_i||>
        cs = [a / np.linalg.norm(a) for a in amps]
        b = brute_ic(M, eta, cs, [float(q) for q in qs])
        ok = summ["lower"] <= b <= summ["upper"]
        fails += (not ok)
        print(json.dumps({"M": M, "p": str(p), "k": k, "complex": bool(np.iscomplexobj(amps[0])),
                          "brute": b, "lower": summ["lower"], "upper": summ["upper"],
                          "width": summ["upper"] - summ["lower"], "ok": ok}))
    print("FAILS", fails)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
