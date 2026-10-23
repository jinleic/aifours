#!/usr/bin/env python3
"""s1full_profile_probe_v1 (ContinueOlson, math-2 lane, 96h run).  Aid only, never a premise.

Purpose: finite falsification control for the written S1-full route (checkpoint 002).  For each prime p, odd delta and
even D listed in ITEMS, enumerate every candidate T = Q u Q' in the representation forced by the written reductions
  Q  = g^m * S_Q   (S_Q: multiset of odd b >= 3 with sum(b-1) = p-delta, m = p+delta-|S_Q|),
  Q' = g^t' * Y    (0 <= t' < min S_Q, Y: odd a in [3, D+1], |Y| = l-t', sum(Y) = 2p-t'),
with l = p+delta-D, u = p+delta, N = u+l, coefficients w.r.t. a generator g of Z_2p (so g = 1).
For each candidate it decides EXACTLY (DP over the multiset) whether every nonempty proper zero-sum subsequence of T has
length in [l, u] ("survivor").  A survivor in the P1 range would refute the route (or a reduction) and is reported.
Controls: POS items outside P1 (delta = (p+2)/3, p = 1 mod 3) must contain the parent-checked family
g^(p+3)(3g)^(p-1) as a survivor; NEG items inside the accepted S1(g) range must have no survivor.
Standard library only; self wall budget BUDGET_S seconds checked between work units; output: one JSON line per item.
"""
import json, sys, time

BUDGET_S = 270.0
T0 = time.monotonic()

def over_budget():
    return time.monotonic() - T0 > BUDGET_S

def partitions(n, maxpart=None):
    """partitions of n into positive parts, nonincreasing, parts <= maxpart"""
    if maxpart is None or maxpart > n:
        maxpart = n
    if n == 0:
        yield []
        return
    for k in range(maxpart, 0, -1):
        for rest in partitions(n - k, k):
            yield [k] + rest

def zero_sum_lengths(counts, n2p):
    """counts: dict coefficient -> multiplicity.  Returns set of lengths c of sub-multisets with sum = 0 mod n2p
    (including empty and full)."""
    reach = [0] * n2p          # reach[s] = bitmask over lengths
    reach[0] = 1
    for a, mult in counts.items():
        a %= n2p
        for _ in range(mult):
            new = reach[:]
            for s in range(n2p):
                if reach[s]:
                    t = (s + a) % n2p
                    new[t] |= reach[s] << 1
            reach = new
    lens = set()
    bm = reach[0]
    c = 0
    while bm:
        if bm & 1:
            lens.add(c)
        bm >>= 1
        c += 1
    return lens

def check_T(p, l, u, counts):
    N = sum(counts.values())
    lens = zero_sum_lengths(counts, 2 * p)
    bad = sorted(c for c in lens if 0 < c < N and not (l <= c <= u))
    return (len(bad) == 0), bad[:6]

def run_item(kind, p, delta, D):
    u = p + delta
    l = u - D
    N = u + l
    rec = {"kind": kind, "p": p, "delta": delta, "D": D, "l": l, "u": u, "N": N,
           "profiles": 0, "candidates": 0, "survivors": [], "status": "COMPLETE"}
    base = (p + 3 * delta - 3 * D)
    if base % 2:
        rec["status"] = "PARITY_SKIP"
        return rec
    base //= 2
    for part in partitions((p - delta) // 2):
        if over_budget():
            rec["status"] = "BUDGET_STOP"
            return rec
        SQ = [2 * k + 1 for k in part]          # b = 2k+1, mass b-1 = 2k
        m = u - len(SQ)
        bmin = min(SQ)
        rec["profiles"] += 1
        for tp in range(0, bmin):
            X = tp - base
            if X < 0:
                continue
            ny = l - tp
            if ny <= 0:
                continue
            maxexc = (D - 2) // 2                # (a-3)/2 <= (D+1-3)/2
            if maxexc < 1 and X > 0:
                continue
            for ex in partitions(X, maxexc if maxexc >= 1 else None):
                if len(ex) > ny:
                    continue
                Y = [2 * e + 3 for e in ex] + [3] * (ny - len(ex))
                counts = {}
                counts[1] = m + tp
                for b in SQ:
                    counts[b] = counts.get(b, 0) + 1
                for a in Y:
                    counts[a] = counts.get(a, 0) + 1
                assert sum(counts.values()) == N
                assert sum(a * c for a, c in counts.items()) == 4 * p
                rec["candidates"] += 1
                ok, bad = check_T(p, l, u, counts)
                if ok:
                    rec["survivors"].append({"SQ": SQ, "tprime": tp, "Y_non3": sorted(a for a in Y if a != 3),
                                             "Y_len": ny})
                    if len(rec["survivors"]) >= 20:
                        rec["status"] = "SURVIVOR_CAP"
                        return rec
    return rec

def is_prime(n):
    return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))

def items():
    out = []
    # POS controls: p = 1 mod 3, delta' = (p+2)/3 (outside P1), D' = (2p-2)/3 (Claude family has D' = u'-l')
    for p in (13, 19, 31):
        dp = (p + 2) // 3
        out.append(("POS", p, dp, (2 * p - 2) // 3))
    # NEG controls inside the accepted S1(g) range (p >= max(3delta+4, 6delta-13)), every admissible even D
    for p, delta in ((13, 3), (19, 5), (29, 7), (31, 7)):
        for D in range(delta + 1, 2 * delta - 1):
            if D % 2 == 0:
                out.append(("NEG", p, delta, D))
    # NEW: P1 holds, S1(g) does not (3delta+4 <= p < 6delta-13)
    for p in range(29, 62):
        if not is_prime(p):
            continue
        for delta in range(3, p, 2):
            if 3 * delta + 4 <= p < 6 * delta - 13:
                for D in range(delta + 1, 2 * delta - 1):
                    if D % 2 == 0:
                        out.append(("NEW", p, delta, D))
    return out

def main(path):
    with open(path, "x", encoding="utf-8") as f:
        f.write(json.dumps({"event": "start", "budget_s": BUDGET_S}) + "\n")
        f.flush()
        for kind, p, delta, D in items():
            if over_budget():
                f.write(json.dumps({"kind": kind, "p": p, "delta": delta, "D": D, "status": "NOT_STARTED"}) + "\n")
                continue
            rec = run_item(kind, p, delta, D)
            rec["elapsed_s"] = round(time.monotonic() - T0, 3)
            f.write(json.dumps(rec) + "\n")
            f.flush()
        f.write(json.dumps({"event": "end", "elapsed_s": round(time.monotonic() - T0, 3)}) + "\n")

if __name__ == "__main__":
    main(sys.argv[1])
