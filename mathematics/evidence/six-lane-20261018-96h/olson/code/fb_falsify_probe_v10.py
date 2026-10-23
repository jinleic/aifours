#!/usr/bin/env python3
"""fb_falsify_probe_v10 (ContinueOlson).  FALSIFICATION AID for Lemma FB (evidence/proof-FB-v1.md 339dcadc...cc6b); never a
premise.  Stdlib only; stdout only; self-stop at BUDGET_S wall seconds (no external timeout).  Imports the frozen probe v6
(code/balforall_falsify_probe_v6.py c24471e0...8fda) functions by path.
Lemma FB (tested form): Y odd elements of C_(2p); Z ANY longest zero-sum, |Z| = 2t < 2p; Y' = Y - Z with L >= p + 1; g ANY
odd generator with W = sum of least positive coefficients of Y' w.r.t. g <= 2p - 1; then every z in Z is g or -s g with
1 <= s <= slack = 2p - 1 - W (ZSTRUCT) and S(N) = sum s <= slack (FB), hence S(N) = n+ and W + n+ <= 2p - 1.
Part A: p = 7, EXHAUSTIVE over all multisets of size R in [10, 18].  Part B: p in (11, 13, 17, 19, 23), random ZSTRUCT-shaped
constructions Y = Y' g^(n+) N (g = 1) with S(N) = n+ (mod 2p) and S(N) >= 2p - W (FB-violating shape); DP decides whether Z is
longest (a 'longest' hit would be a counterexample).  Positive control: same generator with S(N) = n+ <= slack; count how
often Z is longest (must be > 0 for the test to be informative)."""
import sys, time, random, itertools, json, runpy
V6 = runpy.run_path("code/balforall_falsify_probe_v6.py", run_name="v6lib")
max_zero_len, longest_Zs, gens, odd_vals = V6["max_zero_len"], V6["longest_Zs"], V6["gens"], V6["odd_vals"]
BUDGET_S = 285.0
T0 = time.time()
def left():
    return BUDGET_S - (time.time() - T0)

def check_pairs(p, counts, vals, st):
    n2 = 2 * p
    R = sum(counts)
    two_t = max_zero_len(p, counts, vals)
    L = R - two_t
    if L < p + 1 or two_t >= n2:
        return
    st["Y_tested"] += 1
    for z in longest_Zs(p, counts, vals, two_t):
        yp = [c - zz for c, zz in zip(counts, z)]
        for g in gens(p):
            gi = pow(g, -1, n2)
            W = sum(mm * ((v * gi) % n2) for v, mm in zip(vals, yp) if mm)
            if W > n2 - 1:
                continue
            slack = n2 - 1 - W
            nplus = 0; S = 0; shape_ok = True
            for v, mm in zip(vals, z):
                if not mm:
                    continue
                r = (v * gi) % n2
                if r == 1:
                    nplus += mm
                else:
                    s = n2 - r
                    if s > slack or s > two_t - 1:
                        shape_ok = False
                    S += s * mm
            st["pairs"] += 1
            if not shape_ok:
                st["zstruct_violation"] += 1
            if S > slack:
                st["FB_VIOLATION"] += 1
                if len(st["examples"]) < 5:
                    st["examples"].append([p, counts, list(z), g, two_t, L, W, nplus, S])
            if S != nplus:
                st["unbalanced"] += 1
            if W + nplus > n2 - 1:
                st["room_violation"] += 1

def new_st():
    return {"Y_tested": 0, "pairs": 0, "zstruct_violation": 0, "FB_VIOLATION": 0, "unbalanced": 0, "room_violation": 0,
            "examples": []}

def part_A():
    p = 7; vals = odd_vals(p)
    for R in range(10, 19):
        st = new_st(); st["multisets"] = 0; st["complete"] = True
        for combo in itertools.combinations_with_replacement(range(len(vals)), R):
            st["multisets"] += 1
            if st["multisets"] % 2000 == 0 and left() < 150:
                st["complete"] = False
                break
            counts = [0] * len(vals)
            for i in combo:
                counts[i] += 1
            check_pairs(p, counts, vals, st)
        print(json.dumps({"part": "A", "p": p, "R": R, **st}), flush=True)
        if not st["complete"]:
            break

def part_B():
    rng = random.Random(20261019 + 10)
    plist = (11, 13, 17, 19, 23)
    for idx, p in enumerate(plist):
        n2 = 2 * p; vals = odd_vals(p)
        st = {"p": p, "viol_shape_built": 0, "viol_shape_longest": 0, "ctrl_built": 0, "ctrl_longest": 0, "examples": []}
        share = max(1.0, (left() - 5) / (len(plist) - idx))
        tB = time.time()
        while time.time() - tB < share and left() > 5:
            L = rng.randint(p + 1, 2 * p - 1)
            W = rng.randint(L, n2 - 1)
            if (W - L) % 2:
                W -= 1
            coeffs = [1] * L; extra = W - L
            while extra >= 2:
                i = rng.randrange(L); add = 2 * rng.randint(1, max(1, extra // 2))
                if coeffs[i] + add <= n2 - 1 and add <= extra:
                    coeffs[i] += add; extra -= add
            W = sum(coeffs)
            if W > n2 - 1:
                continue
            slack = n2 - 1 - W; delta = slack + 1
            t = rng.randint(1, p - 1); two_t = 2 * t
            smax = min(two_t - 1, slack)
            if smax % 2 == 0:
                smax -= 1
            if smax < 1:
                continue
            ctrl = rng.random() < 0.3
            nm = rng.randint(1, two_t); npl = two_t - nm
            target = npl if ctrl else npl + n2 * rng.randint(0, 2)
            if not ctrl and target < delta:
                continue
            if ctrl and target > slack:
                continue
            if target < nm or target > nm * smax or (target - nm) % 2:
                continue
            s = [1] * nm; inc = (target - nm) // 2; guard = 0
            while inc > 0 and guard < 100000:
                guard += 1
                i = rng.randrange(nm)
                if s[i] + 2 <= smax:
                    s[i] += 2; inc -= 1
            if inc:
                continue
            seq = coeffs + [1] * npl + [n2 - x for x in s]
            counts = [seq.count(v) for v in vals]
            longest = (max_zero_len(p, counts, vals) == two_t)
            if ctrl:
                st["ctrl_built"] += 1; st["ctrl_longest"] += int(longest)
            else:
                st["viol_shape_built"] += 1
                if longest:
                    st["viol_shape_longest"] += 1
                    if len(st["examples"]) < 5:
                        st["examples"].append({"coeffs": sorted(coeffs), "n_plus": npl, "s": sorted(s), "t": t})
        print(json.dumps({"part": "B", **st}), flush=True)

if __name__ == "__main__":
    print(json.dumps({"start": True, "budget_s": BUDGET_S}), flush=True)
    part_A()
    part_B()
    print(json.dumps({"done": True, "elapsed_s": round(time.time() - T0, 1)}), flush=True)
