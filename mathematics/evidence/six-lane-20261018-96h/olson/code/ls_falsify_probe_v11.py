#!/usr/bin/env python3
"""ls_falsify_probe_v11 (ContinueOlson).  FALSIFICATION AID for the parent's conjecture LS (scope evidence/LS-scope-v1.md
80ae8041...dfa); never a premise.  Stdlib only; stdout only; self-stop at BUDGET_S wall seconds (no external timeout).
LS(p, kappa): every Y of odd elements of C_(2p) (integers mod 2p, odd) with |Y| >= p + 2kappa + 1 and (ZP_kappa) (no zero-sum
of length in [2kappa+2, 2p]) has no zero-sum of length >= 2p + 2.
Part A: p = 7, kappa in (4, 5): complete DFS over ALL (ZP_kappa) multisets of every length <= 4p - 2 (EGZ bound), hereditary
pruning by an exact zero-sum-length DP.  Part B: p = 11, kappa in (8, 9): same DFS restricted to canonical multisets (value 1
is a most frequent generator value), budget-limited.  Part C: p in (11, 13), kappa in the new range: random Y = T X with T of
index 2 w.r.t. g = 1 (|T| >= 2p + 2) or T a random zero-sum of length in [2p+2, thr], X random; exact DP of (ZP).
A counterexample is printed in full (multiset as a sorted list)."""
import sys, time, json, random
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

def dfs(p, kappa, canon, tlimit):
    n2 = 2 * p
    Rmax = 4 * p - 2
    FORB = sum(1 << L for L in range(2 * kappa + 2, 2 * p + 1))
    LONG = sum(1 << L for L in range(2 * p + 2, Rmax + 1))
    thr = p + 2 * kappa + 1
    vals = [1] + [v for v in range(3, n2, 2)]
    st = {"p": p, "kappa": kappa, "thr": thr, "canon": canon, "leaves": 0, "leaves_ge_thr": 0, "COUNTEREXAMPLES": 0,
          "ctrl_notS1_below_thr": 0, "max_len_ZP": 0, "complete": True, "examples": [], "ctrl_examples": []}
    tstart = time.time()
    counts = [0] * len(vals)
    def rec(i, reach, total, cap1):
        if time.time() - tstart > tlimit or left() < 10:
            st["complete"] = False
            return
        if i == len(vals):
            st["leaves"] += 1
            st["max_len_ZP"] = max(st["max_len_ZP"], total)
            if reach[0] & LONG:
                if total >= thr:
                    st["COUNTEREXAMPLES"] += 1
                    if len(st["examples"]) < 5:
                        st["examples"].append(sorted(v for v, c in zip(vals, counts) for _ in range(c)))
                else:
                    st["ctrl_notS1_below_thr"] += 1
                    if len(st["ctrl_examples"]) < 2:
                        st["ctrl_examples"].append(sorted(v for v, c in zip(vals, counts) for _ in range(c)))
            if total >= thr:
                st["leaves_ge_thr"] += 1
            return
        a = vals[i]
        gen = (a % p != 0)
        maxc = Rmax - total
        if canon and i > 0 and gen:
            maxc = min(maxc, cap1)
        cur = reach
        c = 0
        while True:
            counts[i] = c
            rec(i + 1, cur, total + c, c if i == 0 else cap1)
            if st["complete"] is False:
                counts[i] = 0
                return
            if c >= maxc:
                break
            nxt = add(cur, a, n2)
            if nxt[0] & FORB:
                break
            cur = nxt
            c += 1
        counts[i] = 0
    reach0 = [0] * n2
    reach0[0] = 1
    rec(0, reach0, 0, 0)
    st["elapsed_s"] = round(time.time() - tstart, 1)
    return st

def zp_and_long(p, kappa, ys):
    n2 = 2 * p
    reach = [0] * n2
    reach[0] = 1
    for a in ys:
        reach = add(reach, a, n2)
    z = reach[0]
    forb = any((z >> L) & 1 for L in range(2 * kappa + 2, 2 * p + 1))
    lng = (z >> (2 * p + 2)) != 0
    return (not forb), lng

def part_C(tlimit):
    rng = random.Random(20261019 + 11)
    out = []
    cells = [(11, 8), (11, 9), (13, 9), (13, 10), (13, 11)]
    per = tlimit / len(cells)
    for (p, kappa) in cells:
        n2 = 2 * p; thr = p + 2 * kappa + 1
        odd = list(range(1, n2, 2))
        st = {"p": p, "kappa": kappa, "thr": thr, "trials_idx2": 0, "trials_rand": 0, "zp_hits": 0, "COUNTEREXAMPLES": 0,
              "examples": []}
        t1 = time.time()
        while time.time() - t1 < per and left() > 5:
            if rng.random() < 0.6:
                N = rng.randint(2 * p + 2, max(2 * p + 2, min(thr, 3 * p)))
                coeffs = [1] * N; extra = 4 * p - N
                if extra < 0 or extra % 2:
                    continue
                while extra > 0:
                    i = rng.randrange(N); add2 = 2 * rng.randint(1, max(1, extra // 2))
                    if add2 <= extra and coeffs[i] + add2 <= n2 - 1:
                        coeffs[i] += add2; extra -= add2
                T = coeffs
                st["trials_idx2"] += 1
            else:
                N = rng.randint(2 * p + 2, thr)
                if N % 2:
                    N += 1
                T = [rng.choice(odd) for _ in range(N - 1)]
                last = (-sum(T)) % n2
                if last % 2 == 0:
                    continue
                T.append(last)
                st["trials_rand"] += 1
            X = [rng.choice(odd) for _ in range(max(0, thr - len(T)))]
            Y = T + X
            u = rng.choice([u for u in range(1, n2, 2) if u % p])
            Y = [(u * a) % n2 for a in Y]
            zp, lng = zp_and_long(p, kappa, Y)
            if zp:
                st["zp_hits"] += 1
                if lng:
                    st["COUNTEREXAMPLES"] += 1
                    if len(st["examples"]) < 5:
                        st["examples"].append(sorted(Y))
        out.append(st)
        print(json.dumps({"part": "C", **st}), flush=True)
    return out

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S}), flush=True)
    for kappa in (4, 5):
        st = dfs(7, kappa, False, 60.0)
        print(json.dumps({"part": "A", **st}), flush=True)
    for kappa in (8, 9):
        st = dfs(11, kappa, True, 75.0)
        print(json.dumps({"part": "B", **st}), flush=True)
    part_C(max(10.0, left() - 10))
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
