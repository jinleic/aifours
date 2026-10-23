#!/usr/bin/env python3
"""balforall_falsify_probe_v6 (ContinueOlson).  FALSIFICATION CONTROL for Lemma BAL-forall (proof-BALfull-v2.md
dffbfea8...a3e1); an aid, never a premise.  Stdlib only; self-budgeted (stops itself at BUDGET_S wall seconds; no
external timeout); writes only to stdout.
Core statement tested: Y a sequence of odd elements of C_(2p); Z ANY longest zero-sum (|Z| = 2t); Y' = Y - Z with
L = |Y'| >= p + 1; g ANY odd generator with index-<1 coefficients on Y' (W <= 2p - 1).  Lemma: if L >= 2t + 1 then
sum s_i = n+ (Z balanced).  Also recorded: ZSTRUCT shape violations (should be 0), and unbalanced (Z, g) with L <= 2t
(sharpness information only).
Part A: p = 7, EXHAUSTIVE over all multisets of size R in [10, RMAX_A].  Part B: p in (11, 13, 17, 19), random structured
sequences (Y' index-<1 w.r.t. g = 1, Z = g^(n+) N with 1 <= s_i <= slack), all longest Z and all index-<1 g of the
resulting Y checked."""
import sys, time, random, itertools, json
BUDGET_S = 270.0
RMAX_A = 17
T0 = time.time()
def left():
    return BUDGET_S - (time.time() - T0)

def odd_vals(p):
    return list(range(1, 2 * p, 2))

def max_zero_len(p, counts, vals):
    n2 = 2 * p
    reach = [0] * n2
    reach[0] = 1
    for v, c in zip(vals, counts):
        for _ in range(c):
            new = reach[:]
            for r in range(n2):
                b = reach[(r - v) % n2]
                if b:
                    new[r] |= b << 1
            reach = new
    return reach[0].bit_length() - 1

def longest_Zs(p, counts, vals, two_t):
    n2 = 2 * p
    out = []
    def rec(i, rem, s, cur):
        if i == len(vals):
            if rem == 0 and s % n2 == 0:
                out.append(tuple(cur))
            return
        rest = sum(counts[i + 1:])
        lo = max(0, rem - rest)
        for z in range(lo, min(counts[i], rem) + 1):
            cur.append(z)
            rec(i + 1, rem - z, s + z * vals[i], cur)
            cur.pop()
    rec(0, two_t, 0, [])
    return out

def gens(p):
    n2 = 2 * p
    return [g for g in range(1, n2, 2) if g != p]

def check_Y(p, counts, vals, stats):
    R = sum(counts)
    two_t = max_zero_len(p, counts, vals)
    L = R - two_t
    if L < p + 1:
        return
    stats["Y_tested"] += 1
    n2 = 2 * p
    ginv = {g: pow(g, -1, n2) for g in gens(p)}
    for z in longest_Zs(p, counts, vals, two_t):
        yp = [c - zz for c, zz in zip(counts, z)]
        for g, gi in ginv.items():
            W = sum(m * ((v * gi) % n2) for v, m in zip(vals, yp) if m)
            if W > n2 - 1:
                continue
            slack = n2 - 1 - W
            nplus = 0; S = 0; bad = False
            for v, m in zip(vals, z):
                if not m:
                    continue
                r = (v * gi) % n2
                if r == 1:
                    nplus += m
                else:
                    s = n2 - r
                    if s > slack or s > max(two_t - 1, 0):
                        bad = True
                    S += s * m
            stats["pairs"] += 1
            if bad:
                stats["zstruct_violation"] += 1
                if len(stats["examples_zstruct"]) < 3:
                    stats["examples_zstruct"].append([p, counts, list(z), g])
            if S != nplus:
                if L >= two_t + 1:
                    stats["UNBAL_L_ge_2t_plus_1"] += 1
                    if len(stats["examples_counter"]) < 5:
                        stats["examples_counter"].append([p, counts, list(z), g, two_t, L])
                elif L == two_t:
                    stats["unbal_L_eq_2t"] += 1
                    if len(stats["examples_sharp"]) < 5:
                        stats["examples_sharp"].append([p, counts, list(z), g, two_t, L])
                else:
                    stats["unbal_L_lt_2t"] += 1

def new_stats():
    return {"Y_tested": 0, "pairs": 0, "zstruct_violation": 0, "UNBAL_L_ge_2t_plus_1": 0, "unbal_L_eq_2t": 0,
            "unbal_L_lt_2t": 0, "examples_counter": [], "examples_sharp": [], "examples_zstruct": []}

def part_A():
    p = 7
    vals = odd_vals(p)
    res = {}
    for R in range(10, RMAX_A + 1):
        st = new_stats(); st["complete"] = False; st["multisets"] = 0
        for bars in itertools.combinations(range(R + len(vals) - 1), len(vals) - 1):
            prev = -1; counts = []
            for b in bars:
                counts.append(b - prev - 1); prev = b
            counts.append(R + len(vals) - 1 - prev - 1)
            st["multisets"] += 1
            check_Y(p, counts, vals, st)
            if st["multisets"] % 2000 == 0 and left() < 60:
                break
        else:
            st["complete"] = True
        res[R] = st
        print(json.dumps({"part": "A", "p": p, "R": R, **st}), flush=True)
        if not st["complete"]:
            break
    return res

def part_B():
    rng = random.Random(20261019)
    for p in (11, 13, 17, 19):
        st = new_stats(); st["samples"] = 0
        n2 = 2 * p; vals = odd_vals(p)
        tB = time.time()
        while left() > 5 and time.time() - tB < max(1.0, (left() - 5) / 2):
            L = rng.randint(p + 1, 2 * p - 1)
            W = rng.randint(L, 2 * p - 1)
            if (W - L) % 2:
                W -= 1
            coeffs = [1] * L
            extra = W - L
            while extra >= 2:
                i = rng.randrange(L); add = 2 * rng.randint(1, max(1, extra // 2))
                if coeffs[i] + add <= n2 - 1:
                    coeffs[i] += add; extra -= add
            if sum(coeffs) > n2 - 1:
                continue
            slack = n2 - 1 - sum(coeffs)
            two_t = 2 * rng.randint(1, max(1, (L - 1) // 2 + 1))
            npl = rng.randint(0, two_t - 1); nm = two_t - npl
            N = [rng.randrange(1, max(2, slack + 1), 2) for _ in range(nm)]
            seq = coeffs + [1] * npl + [(n2 - s) % n2 for s in N]
            counts = [seq.count(v) for v in vals]
            st["samples"] += 1
            check_Y(p, counts, vals, st)
        print(json.dumps({"part": "B", "p": p, **st}), flush=True)

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S, "rmax_A": RMAX_A}), flush=True)
    part_A()
    part_B()
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
