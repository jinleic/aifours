#!/usr/bin/env python3
"""ReviewF179RminusExact: FLOAT falsification sanity search for the decoded DFZ item
3 7 2 2 3 0 0 3 2 (packet line 2088, form of packet lines 1960-1962).  NOT a proof and
NOT an independent reconstruction; it only searches small random laws of (A,B,C,D) for a
violation.  Power check: the same search on Ingleton (known not to be an information
inequality), and on the false inequality I(A;B) <= I(A;B|C)."""
import itertools
import json
import math
import random
import sys
import time

COEF = dict(zip("abcdefghi", [3, 7, 2, 2, 3, 0, 0, 3, 2]))


def H(p, idx):
    m = {}
    for x, v in p.items():
        t = tuple(x[i] for i in idx)
        m[t] = m.get(t, 0.0) + v
    return -sum(v * math.log2(v) for v in m.values() if v > 0)


def I(p, X, Y, Z=()):
    return H(p, X + Z) + H(p, Y + Z) - H(p, X + Y + Z) - H(p, Z)


A, B, C, D = (0,), (1,), (2,), (3,)


def dfz_slack(p):
    rhs = (COEF["b"] * I(p, A, B, C) + COEF["c"] * I(p, A, C, B) + COEF["d"] * I(p, B, C, A)
           + COEF["e"] * I(p, A, B, D) + COEF["f"] * I(p, A, D, B) + COEF["g"] * I(p, B, D, A)
           + COEF["h"] * I(p, C, D) + COEF["i"] * I(p, C, D, A))
    return rhs - COEF["a"] * I(p, A, B)


def ingleton_slack(p):
    # Ingleton: I(A;B) <= I(A;B|C) + I(A;B|D) + I(C;D)  (fails for some entropic laws)
    return I(p, A, B, C) + I(p, A, B, D) + I(p, C, D) - I(p, A, B)


def false_slack(p):
    return I(p, A, B, C) - I(p, A, B)


def main():
    t0 = time.time()
    rnd = random.Random(1104360)
    worst = {"dfz": float("inf"), "ingleton": float("inf"), "false": float("inf")}
    viol = {"dfz": 0, "ingleton": 0, "false": 0}
    n = 0
    pts = list(itertools.product(range(2), repeat=4))
    pts3 = list(itertools.product(range(3), repeat=4))
    while time.time() - t0 < 60:
        k = rnd.choice([2, 3, 4, 4, 4, 5, 6, 8])
        base = pts if rnd.random() < 0.7 else pts3
        supp = rnd.sample(base, k)
        w = [rnd.random() ** rnd.choice([1, 2, 4]) + 1e-9 for _ in supp]
        s = sum(w)
        p = {x: v / s for x, v in zip(supp, w)}
        n += 1
        for name, f in (("dfz", dfz_slack), ("ingleton", ingleton_slack), ("false", false_slack)):
            v = f(p)
            worst[name] = min(worst[name], v)
            if v < -1e-9:
                viol[name] += 1
    out = {"samples": n, "seed": 1104360, "min_slack": worst, "violations": viol,
           "dfz_no_violation_found": viol["dfz"] == 0,
           "power_checks_found_violations": viol["ingleton"] > 0 and viol["false"] > 0,
           "runtime_s": round(time.time() - t0, 2),
           "note": "float search only; absence of violation is not a proof"}
    print(json.dumps(out, sort_keys=True))
    return 0 if out["dfz_no_violation_found"] else 1


if __name__ == "__main__":
    sys.exit(main())
