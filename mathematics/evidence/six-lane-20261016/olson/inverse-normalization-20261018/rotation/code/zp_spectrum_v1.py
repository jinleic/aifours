#!/usr/bin/env python3
"""Size of the zero-pattern prefilter for PM*-normal forms (all k = o blocks odd), rotation slice 2026-10-18.
For N = 4p-2, o >= 3, kappa = p-1-H >= 0: R = 2p + 2 kappa - o, F = 2H + o.  Proved necessary conditions used:
  zero pattern (GRX, z = +): no zero-sum (even length L, sum 0) with L in [2 kappa + 2, 2p];
  EGZ: R <= 3p-2;  Davenport-alpha: R + H <= 3p-2  (<=> kappa <= o - 1).
Prints, per (o, kappa), the number of rotation multisets passing, and how many are non-rigid.
"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_zero_lemmas_v1 import zero_lengths, multisets  # noqa: E402


def rigid(mult, p):
    vals = [v for v in range(p) if mult[v]]
    if 0 in vals:
        return False
    return len(vals) <= 1 or (len(vals) == 2 and (vals[0] + vals[1]) % p == 0)


def main():
    p = int(sys.argv[1])
    res = []
    for kappa in range(0, p):
        H = p - 1 - kappa
        for o in range(3, 4 * p):
            R = 2 * p + 2 * kappa - o
            F = 2 * H + o
            if R < 0 or R > 3 * p - 2 or kappa > o - 1 or F + R != 4 * p - 2:
                continue
            npass = nnr = 0
            ex = []
            for mult in multisets(p, R):
                Ls = zero_lengths(mult, p, 2 * p)
                if any(2 * kappa + 2 <= L <= 2 * p and L % 2 == 0 for L in Ls):
                    continue
                npass += 1
                if not rigid(mult, p):
                    nnr += 1
                    if len(ex) < 3:
                        ex.append(mult)
            res.append({'o': o, 'kappa': kappa, 'R': R, 'F': F, 'pass': npass, 'nonrigid': nnr, 'ex': ex})
            print(json.dumps(res[-1]), flush=True)


if __name__ == '__main__':
    main()
