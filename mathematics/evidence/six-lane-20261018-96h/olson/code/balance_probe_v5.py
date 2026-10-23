#!/usr/bin/env python3
"""balance_probe_v5 (ContinueOlson).  Aid only, never a premise.  Supersedes balance_probe_v4 (frozen, never run: its
zero-sum enumeration was too slow for the budget).

Question: where Lemma LAMBDA's hypotheses fail (8kappa > 4p-3k+5 and 2kappa(2kappa-1) >= 2p), can a sequence Y of
R = 2p + 2kappa - k odd elements of Z_2p with (S1_kappa) have EVERY longest zero-sum Z unbalanced for EVERY index-<1
generator h of Y - Z?  Balanced := writing Z's terms as b h (b odd in (-p, p]), every positive b equals 1 and
sum of |b| over negative b equals #(b = 1).
Exact over every Y whose support has <= 3 values and contains a generator (normalised to 1).
Per item: Y_S1 (Y with S1), some_unbal, all_unbal (obstruction candidates), zstruct_viol (a positive b >= 3 in some
longest Z for some h; ZSTRUCT predicts 0), no_gen (a longest Z whose complement has no index-<1 generator; SC0 predicts 0
when |Y - Z| >= p+1).  CONTROL items satisfy LAMBDA, so all_unbal and some_unbal must be 0 there.
"""
import json, sys, time

BUDGET_S = 270.0
T0 = time.monotonic()
def over(): return time.monotonic() - T0 > BUDGET_S

def max_zero_len(p, vals, mults):
    n2 = 2 * p
    reach = [0] * n2
    reach[0] = 1
    for v, m in zip(vals, mults):
        for _ in range(m):
            new = reach[:]
            for s in range(n2):
                b = reach[s]
                if b:
                    new[(s + v) % n2] |= b << 1
            reach = new
    return reach[0].bit_length() - 1

def longest_vectors(p, vals, mults, L):
    n2 = 2 * p
    out = []
    if len(vals) == 1:
        if (L * vals[0]) % n2 == 0 and L <= mults[0]: out.append((L,))
        return out
    if len(vals) == 2:
        for j in range(max(0, L - mults[0]), min(mults[1], L) + 1):
            i = L - j
            if (i * vals[0] + j * vals[1]) % n2 == 0: out.append((i, j))
        return out
    for j in range(0, min(mults[1], L) + 1):
        for k in range(0, min(mults[2], L - j) + 1):
            i = L - j - k
            if i > mults[0]: continue
            if (i * vals[0] + j * vals[1] + k * vals[2]) % n2 == 0: out.append((i, j, k))
    return out

def index_lt1_gens(p, vals, mults):
    n2 = 2 * p
    gens = []
    for h in range(1, n2, 2):
        if h == p: continue
        inv = pow(h, -1, n2)
        tot = sum(((v * inv) % n2) * m for v, m in zip(vals, mults) if m)
        if tot <= n2 - 1: gens.append(h)
    return gens

def bcoef(p, h, y):
    n2 = 2 * p
    a = (y * pow(h, -1, n2)) % n2
    return a if a <= p else a - n2

def lam_fails(p, k, kappa):
    return not ((8 * kappa <= 4 * p - 3 * k + 5) or (2 * kappa * (2 * kappa - 1) < 2 * p))

def run(kind, p, k, kappa, f):
    n2 = 2 * p
    R = 2 * p + 2 * kappa - k
    odds = list(range(3, n2, 2))
    rec = {"kind": kind, "p": p, "k": k, "kappa": kappa, "R": R, "lam_fails": lam_fails(p, k, kappa),
           "Y_S1": 0, "some_unbal": 0, "all_unbal": 0, "zstruct_viol": 0, "no_gen": 0, "examples": [],
           "status": "COMPLETE"}
    supports = [(1,)] + [(1, a) for a in odds] + [(1, a, b) for i, a in enumerate(odds) for b in odds[i + 1:]]
    for vals in supports:
        if over():
            rec["status"] = "BUDGET_STOP"; break
        nv = len(vals)
        if nv == 1: comps = [(R,)]
        elif nv == 2: comps = [(R - y, y) for y in range(1, R)]
        else: comps = [(R - y - z, y, z) for y in range(1, R) for z in range(1, R - y)]
        for mults in comps:
            L2 = max_zero_len(p, vals, mults)
            if L2 > 2 * kappa: continue
            rec["Y_S1"] += 1
            any_u = False; all_u = True
            for Zv in longest_vectors(p, vals, mults, L2):
                rest = tuple(m - z for m, z in zip(mults, Zv))
                gens = index_lt1_gens(p, vals, rest)
                if not gens:
                    rec["no_gen"] += 1; all_u = False; continue
                for h in gens:
                    npos = 0; ssum = 0; viol = False
                    for v, z in zip(vals, Zv):
                        if not z: continue
                        b = bcoef(p, h, v)
                        if b == 1: npos += z
                        elif b < 0: ssum += (-b) * z
                        else: viol = True
                    if viol: rec["zstruct_viol"] += 1
                    if (not viol) and ssum == npos: all_u = False
                    else: any_u = True
            if L2 == 0: all_u = False
            if any_u: rec["some_unbal"] += 1
            if all_u:
                rec["all_unbal"] += 1
                if len(rec["examples"]) < 10: rec["examples"].append({"vals": vals, "mults": mults, "two_t": L2})
    rec["elapsed_s"] = round(time.monotonic() - T0, 3)
    f.write(json.dumps(rec) + "\n"); f.flush()

def items():
    out = [("CONTROL", 13, 10, 2), ("CONTROL", 13, 12, 2), ("CONTROL", 17, 14, 3)]
    for p in (13, 17, 19, 23):
        for k in range(p - 1, 2, -1):
            if 3 * k <= 2 * p + 1: break
            for kappa in range(2, k):
                if 2 * kappa + k > 2 * p - 1: continue
                if lam_fails(p, k, kappa): out.append(("TEST", p, k, kappa))
    return out

def main(path):
    with open(path, "x", encoding="utf-8") as f:
        its = items()
        f.write(json.dumps({"event": "start", "n_items": len(its)}) + "\n")
        for kind, p, k, kappa in its:
            if over():
                f.write(json.dumps({"kind": kind, "p": p, "k": k, "kappa": kappa, "status": "NOT_STARTED"}) + "\n"); continue
            run(kind, p, k, kappa, f)
        f.write(json.dumps({"event": "end", "elapsed_s": round(time.monotonic() - T0, 3)}) + "\n")

if __name__ == "__main__":
    main(sys.argv[1])
