#!/usr/bin/env python3
"""s1sharp_support_probe_v3 (ContinueOlson): v2 with ITEMS replaced only.  Aid only, never a premise.

Independent of the written proof's Steps 3-9: for each item (p, kappa) it enumerates EVERY sequence T of odd elements of
Z_2p whose support has at most 3 distinct values and contains a generator (normalised to 1 by a unit), with |T| = N
even in [2p+2, 4kappa] and sum 0, and decides exactly whether every nonempty proper zero-sum subsequence of T has length
>= N - 2kappa (equivalently <= 2kappa).  Such a T is exactly a counterexample sequence to (ZP_kappa) => (S1_kappa)
(Y = T), and every counterexample Y contains one (a shortest zero-sum of length >= 2kappa+2), whose support lies in Y's.
So: 0 survivors at an item = no counterexample Y whose shortest long zero-sum has support size <= 3.
POS items (kappa = floor(2p/3)+1) must show the families g^(p+3)(3g)^(p-1) and, for p = 1 mod 3, g^(2p-1)(cg)^3.
"""
import json, sys, time

BUDGET_S = 270.0
T0 = time.monotonic()

def over_budget():
    return time.monotonic() - T0 > BUDGET_S

def survivor(p, kappa, x, a, y, b, z):
    """T = 1^x a^y b^z (b, z may be 0/None).  True iff every nonempty proper zero-sum has length >= l."""
    n2 = 2 * p
    N = x + y + z
    l = N - 2 * kappa
    # enumerate (j, k) with j + k < l; minimal i = residue; length i + j + k must be >= l unless (i,j,k) trivial/full
    for s in range(0, l):
        for j in range(0, min(y, s) + 1):
            k = s - j
            if k > z:
                continue
            rho = (-(a * j + b * k)) % n2
            if rho > x:
                continue
            L = rho + j + k
            if L == 0:
                continue          # empty set (rho = 0, j = k = 0)
            if L < l:
                return False      # short nonempty zero-sum; it is proper since L < l <= N
    return True

def run_item(kind, p, kappa):
    n2 = 2 * p
    rec = {"kind": kind, "p": p, "kappa": kappa, "N_range": [2 * p + 2, 4 * kappa], "T_checked": 0,
           "survivors": [], "status": "COMPLETE"}
    odds = [v for v in range(3, n2, 2)]
    for N in range(2 * p + 2, 4 * kappa + 1, 2):
        # two-value supports {1, a}
        for a in odds:
            for y in range(1, N):
                x = N - y
                if (x + a * y) % n2:
                    continue
                rec["T_checked"] += 1
                if survivor(p, kappa, x, a, y, 0, 0):
                    rec["survivors"].append({"N": N, "T": [[1, x], [a, y]]})
        # three-value supports {1, a, b}, a < b
        for ia, a in enumerate(odds):
            if over_budget():
                rec["status"] = "BUDGET_STOP"
                rec["stopped_at"] = {"N": N, "a": a}
                return rec
            for b in odds[ia + 1:]:
                for y in range(1, N - 1):
                    for z in range(1, N - y):
                        x = N - y - z
                        if (x + a * y + b * z) % n2:
                            continue
                        rec["T_checked"] += 1
                        if survivor(p, kappa, x, a, y, b, z):
                            rec["survivors"].append({"N": N, "T": [[1, x], [a, y], [b, z]]})
                            if len(rec["survivors"]) >= 50:
                                rec["status"] = "SURVIVOR_CAP"
                                return rec
    return rec

def main(path, items):
    with open(path, "x", encoding="utf-8") as f:
        f.write(json.dumps({"event": "start", "budget_s": BUDGET_S, "items": items}) + "\n")
        f.flush()
        for kind, p, kappa in items:
            if over_budget():
                f.write(json.dumps({"kind": kind, "p": p, "kappa": kappa, "status": "NOT_STARTED"}) + "\n")
                continue
            rec = run_item(kind, p, kappa)
            rec["elapsed_s"] = round(time.monotonic() - T0, 3)
            f.write(json.dumps(rec) + "\n")
            f.flush()
        f.write(json.dumps({"event": "end", "elapsed_s": round(time.monotonic() - T0, 3)}) + "\n")

ITEMS = [["TARGET", 37, 24], ["POS", 37, 25], ["TARGET", 41, 27], ["POS", 41, 28], ["TARGET", 43, 28], ["POS", 43, 29], ["TARGET", 47, 31], ["POS", 47, 32], ["TARGET", 53, 35], ["POS", 53, 36], ["TARGET", 59, 39], ["POS", 59, 40], ["TARGET", 61, 40], ["POS", 61, 41]]

if __name__ == "__main__":
    main(sys.argv[1], ITEMS)
