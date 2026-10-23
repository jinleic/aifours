#!/usr/bin/env python3
"""balforall_sharpness_search_v8 (ContinueOlson).  SHARPNESS INFORMATION for Lemma BAL-forall (proof-BALfull-v2.md
dffbfea8...a3e1); an aid, never a premise.  Directed random search, inside the (S')-relevant region t <= p - 1 and
p + 1 <= L <= 2t, for sequences Y = Y' Z with Y' index-<1 w.r.t. g = 1 (W <= 2p - 1), Z = g^(n+) N with S(N) = n+ + 2p
(unbalanced) and 1 <= s_i <= min(2t - 1, slack), such that Z is a LONGEST zero-sum of Y (exact DP).  Imports the frozen
probe v6 (c24471e0...8fda) by path.  Stdlib only; stdout only; self-stop at 150 s total or 5 examples per p."""
import json, random, time, runpy
V6 = runpy.run_path("code/balforall_falsify_probe_v6.py", run_name="v6lib")
max_zero_len, odd_vals = V6["max_zero_len"], V6["odd_vals"]
T0 = time.time()
rng = random.Random(1019)
report = {}
for p in (11, 13):
    n2 = 2 * p; vals = odd_vals(p)
    tp = time.time(); ex = []; samples = 0; feasible = 0; hist_gap = {}
    while len(ex) < 5 and time.time() - tp < 70 and time.time() - T0 < 150:
        samples += 1
        t = rng.randint((p + 1) // 2, p - 1); two_t = 2 * t
        L = rng.randint(p + 1, two_t) if two_t >= p + 1 else None
        if L is None:
            continue
        W = rng.randint(L, n2 - 1)
        if (W - L) % 2:
            W -= 1
        coeffs = [1] * L; extra = W - L
        while extra >= 2:
            i = rng.randrange(L); add = 2 * rng.randint(1, max(1, extra // 2))
            if coeffs[i] + add <= n2 - 1:
                coeffs[i] += add; extra -= add
        W = sum(coeffs)
        if W > n2 - 1:
            continue
        slack = n2 - 1 - W
        smax = min(two_t - 1, slack)
        if smax % 2 == 0:
            smax -= 1
        if smax < 1:
            continue
        nm = rng.randint(1, two_t - 1); npl = two_t - nm
        S = npl + n2
        if S < nm or S > nm * smax:
            continue
        s = [1] * nm; inc = (S - nm) // 2
        guard = 0
        while inc > 0 and guard < 100000:
            guard += 1
            i = rng.randrange(nm)
            if s[i] + 2 <= smax:
                s[i] += 2; inc -= 1
        if inc:
            continue
        feasible += 1
        seq = coeffs + [1] * npl + [n2 - x for x in s]
        counts = [seq.count(v) for v in vals]
        if max_zero_len(p, counts, vals) != two_t:
            continue
        gap = L - two_t
        hist_gap[gap] = hist_gap.get(gap, 0) + 1
        ex.append({"p": p, "t": t, "L": L, "W": W, "slack": slack, "Yprime_coeffs": sorted(coeffs), "n_plus": npl,
                   "N_s_values": sorted(s), "S_N": S, "L_minus_2t": gap})
    report[p] = {"samples": samples, "feasible_constructions": feasible, "unbalanced_longest_found": len(ex),
                 "gap_hist": hist_gap, "examples": ex, "elapsed_s": round(time.time() - tp, 1)}
print(json.dumps(report, indent=1))
