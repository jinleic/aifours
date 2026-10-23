#!/usr/bin/env python3
"""balance_probe_v4 (ContinueOlson).  Aid only, never a premise.

Question: in the regime where Lemma LAMBDA's hypotheses fail, can a sequence Y of odd elements of Z_2p with (S1) at kappa
(all zero-sum subsequences of length <= 2kappa), |Y| = R = 2p + 2kappa - k, have EVERY longest zero-sum Z unbalanced
w.r.t. EVERY index-<1 generator h of Y - Z?  (Balanced: writing Z's terms as b h with b odd in (-p, p], the positive
ones are h and the negative coefficients -s_i satisfy sum s_i = #(b = 1).)
Exact enumeration over all Y whose support has <= 3 distinct values and contains a generator (normalised to 1).
Reports per (p, k, kappa): number of Y with (S1); number with SOME longest Z unbalanced for some h; number with ALL
(longest Z, h) unbalanced ("obstruction candidates").  Standard library only; self budget 270 s.
"""
import json, sys, time
from itertools import product

BUDGET_S = 270.0
T0 = time.monotonic()
def over(): return time.monotonic() - T0 > BUDGET_S

def zs_vectors(p, vals, mults):
    """all count vectors (i0, i1, i2) <= mults with sum(i*v) = 0 mod 2p, excluding all-zero"""
    n2 = 2 * p
    out = []
    ranges = [range(m + 1) for m in mults]
    for vec in product(*ranges):
        if sum(vec) == 0: continue
        if sum(i * v for i, v in zip(vec, vals)) % n2 == 0:
            out.append(vec)
    return out

def bcoef(p, h, y):
    """odd b in (-p, p] with b*h = y mod 2p (h a generator, y odd)"""
    n2 = 2 * p
    inv = pow(h, -1, n2)
    a = (y * inv) % n2          # in [0, 2p), odd
    return a if a <= p else a - n2

def index_lt1_gens(p, vals, mults):
    n2 = 2 * p
    gens = []
    for h in range(1, n2, 2):
        if h == p: continue
        inv = pow(h, -1, n2)
        tot = 0
        for v, m in zip(vals, mults):
            if m == 0: continue
            tot += ((v * inv) % n2) * m
        if tot <= n2 - 1:
            gens.append(h)
    return gens

def analyse(p, kappa, vals, mults):
    zs = zs_vectors(p, vals, mults)
    lens = [sum(v) for v in zs]
    if max(lens) > 2 * kappa:
        return None                       # (S1) fails
    tmax = max(lens)
    longest = [v for v in zs if sum(v) == tmax]
    any_unbal = False
    all_unbal = True
    for Zv in longest:
        rest = [m - z for m, z in zip(mults, Zv)]
        gens = index_lt1_gens(p, vals, rest)
        if not gens:
            all_unbal = False             # SC0 should give a generator; record as not-unbalanced (anomaly counted)
            continue
        for h in gens:
            npos = 0; ssum = 0; ok_struct = True
            for v, z in zip(vals, Zv):
                if z == 0: continue
                b = bcoef(p, h, v)
                if b == 1: npos += z
                elif b < 0: ssum += (-b) * z
                else: ok_struct = False
            bal = ok_struct and (ssum == npos)
            if bal:
                all_unbal = False
            else:
                any_unbal = True
    return (tmax, any_unbal, all_unbal)

def lam_fails(p, k, kappa):
    return not ((8 * kappa <= 4 * p - 3 * k + 5) or (2 * kappa * (2 * kappa - 1) < 2 * p))

def run(p, k, kappa, f):
    n2 = 2 * p
    R = 2 * p + 2 * kappa - k
    odds = list(range(3, n2, 2))
    rec = {"p": p, "k": k, "kappa": kappa, "R": R, "Y_S1": 0, "some_unbal": 0, "all_unbal": 0, "examples": [],
           "status": "COMPLETE"}
    supports = [(1,)] + [(1, a) for a in odds] + [(1, a, b) for i, a in enumerate(odds) for b in odds[i + 1:]]
    for vals in supports:
        if over():
            rec["status"] = "BUDGET_STOP"; break
        nv = len(vals)
        if nv == 1:
            comps = [(R,)]
        elif nv == 2:
            comps = [(R - y, y) for y in range(1, R)]
        else:
            comps = [(R - y - z, y, z) for y in range(1, R) for z in range(1, R - y)]
        for mults in comps:
            r = analyse(p, kappa, vals, mults)
            if r is None: continue
            rec["Y_S1"] += 1
            if r[1]: rec["some_unbal"] += 1
            if r[2]:
                rec["all_unbal"] += 1
                if len(rec["examples"]) < 10:
                    rec["examples"].append({"vals": vals, "mults": mults, "two_t": r[0]})
    rec["elapsed_s"] = round(time.monotonic() - T0, 3)
    f.write(json.dumps(rec) + "\n"); f.flush()

def main(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(json.dumps({"event": "start"}) + "\n")
        for p in (13, 17, 19):
            for k in range(p - 1, 2, -1):
                if 3 * k <= 2 * p + 1: break
                for kappa in range(2, k):
                    if 2 * kappa + k > 2 * p - 1: continue
                    if not lam_fails(p, k, kappa): continue
                    if over():
                        f.write(json.dumps({"p": p, "k": k, "kappa": kappa, "status": "NOT_STARTED"}) + "\n"); continue
                    run(p, k, kappa, f)
        f.write(json.dumps({"event": "end", "elapsed_s": round(time.monotonic() - T0, 3)}) + "\n")

if __name__ == "__main__":
    main(sys.argv[1])
