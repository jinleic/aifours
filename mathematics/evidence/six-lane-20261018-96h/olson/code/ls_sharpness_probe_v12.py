#!/usr/bin/env python3
"""ls_sharpness_probe_v12 (ContinueOlson).  AID for LS (scope evidence/LS-scope-v1.md 80ae8041...dfa); never a premise.
Stdlib only; stdout only; self-stop at BUDGET_S.  Complete DFS (as in frozen probe v11, 912e592c...970e) over all (ZP_kappa)
multisets; records the LENGTH HISTOGRAM of (ZP)-and-not-(S1) multisets (a long zero-sum = length >= 2p + 2), the longest
such multisets, and for each of them whether some single term d lies in every long zero-sum (Y - d satisfies (S1)) and the
longest zero-sum length of Y - d.  Cells: p = 7 kappa = 5; p = 11 kappa = 8, 9 (canonical: value 1 a most frequent generator
value); p = 13 kappa = 9 (canonical, budget-limited)."""
import time, json
BUDGET_S = 280.0
T0 = time.time()
def left():
    return BUDGET_S - (time.time() - T0)

def add(reach, a, n2):
    new = reach[:]
    for r in range(n2):
        b = reach[r]
        if b:
            new[(r + a) % n2] |= b << 1
    return new

def reach_of(ys, n2):
    reach = [0] * n2; reach[0] = 1
    for a in ys:
        reach = add(reach, a, n2)
    return reach

def run(p, kappa, canon, tlimit):
    n2 = 2 * p; Rmax = 4 * p - 2
    FORB = sum(1 << L for L in range(2 * kappa + 2, 2 * p + 1))
    LONG = sum(1 << L for L in range(2 * p + 2, Rmax + 1))
    vals = [1] + list(range(3, n2, 2))
    hist = {}; best = []; st = {"complete": True}
    t1 = time.time(); counts = [0] * len(vals)
    def rec(i, reach, total, cap1):
        if time.time() - t1 > tlimit or left() < 8:
            st["complete"] = False; return
        if i == len(vals):
            if reach[0] & LONG:
                hist[total] = hist.get(total, 0) + 1
                ms = [v for v, c in zip(vals, counts) for _ in range(c)]
                best.append((total, ms)); best.sort(key=lambda x: -x[0]); del best[6:]
            return
        a = vals[i]; gen = (a % p != 0)
        maxc = Rmax - total
        if canon and i > 0 and gen:
            maxc = min(maxc, cap1)
        cur = reach; c = 0
        while True:
            counts[i] = c
            rec(i + 1, cur, total + c, c if i == 0 else cap1)
            if not st["complete"]:
                counts[i] = 0; return
            if c >= maxc:
                break
            nxt = add(cur, a, n2)
            if nxt[0] & FORB:
                break
            cur = nxt; c += 1
        counts[i] = 0
    r0 = [0] * n2; r0[0] = 1
    rec(0, r0, 0, 0)
    detail = []
    for total, ms in best:
        hit = []
        for j in range(len(ms)):
            rest = ms[:j] + ms[j + 1:]
            z = reach_of(rest, n2)[0]
            if not (z & LONG):
                hit.append([ms[j], z.bit_length() - 1])
        detail.append({"len": total, "Y": ms, "single_hitters_and_t0x2": hit[:6], "n_hitters": len(hit)})
    out = {"p": p, "kappa": kappa, "thr": p + 2 * kappa + 1, "canon": canon, "complete": st["complete"],
           "notS1_length_hist": hist, "longest_notS1": detail, "elapsed_s": round(time.time() - t1, 1)}
    print(json.dumps(out), flush=True)

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S}), flush=True)
    run(7, 5, False, 30.0)
    run(11, 8, True, 60.0)
    run(11, 9, True, 90.0)
    run(13, 9, True, max(10.0, left() - 10))
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
