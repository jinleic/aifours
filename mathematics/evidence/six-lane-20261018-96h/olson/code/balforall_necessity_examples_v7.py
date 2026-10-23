#!/usr/bin/env python3
"""balforall_necessity_examples_v7 (ContinueOlson).  POSITIVE CONTROL for Lemma BAL-forall (proof-BALfull-v2.md
dffbfea8...a3e1): extract explicit sequences with an UNBALANCED longest zero-sum Z (some index-<1 generator g) and
L = |Y - Z| >= p + 1 but L < 2t, i.e. outside the lemma's hypothesis L >= 2t + 1.  Imports the frozen probe v6
(c24471e0...8fda) functions by path; same seeded generator as its Part B, p = 11 only; stops after 3 examples or 60 s.
An aid, never a premise.  Stdlib only; stdout only."""
import json, random, time, runpy, sys
V6 = runpy.run_path("code/balforall_falsify_probe_v6.py", run_name="v6lib")
max_zero_len, longest_Zs, gens, odd_vals = V6["max_zero_len"], V6["longest_Zs"], V6["gens"], V6["odd_vals"]
T0 = time.time()
p = 11; n2 = 2 * p; vals = odd_vals(p)
rng = random.Random(20261019)
found = []
samples = 0
while len(found) < 3 and time.time() - T0 < 60:
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
    samples += 1
    tt = max_zero_len(p, counts, vals)
    LL = sum(counts) - tt
    if LL < p + 1 or LL >= tt:
        continue
    for z in longest_Zs(p, counts, vals, tt):
        yp = [c - zz for c, zz in zip(counts, z)]
        for g in gens(p):
            gi = pow(g, -1, n2)
            Wy = sum(m * ((v * gi) % n2) for v, m in zip(vals, yp) if m)
            if Wy > n2 - 1:
                continue
            npos = 0; S = 0; Nl = []
            for v, m in zip(vals, z):
                if m:
                    r = (v * gi) % n2
                    if r == 1:
                        npos += m
                    else:
                        S += (n2 - r) * m; Nl += [n2 - r] * m
            if S != npos and len(found) < 3:
                Ycoef = sorted([(v * gi) % n2 for v, m in zip(vals, yp) for _ in range(m)])
                found.append({"p": p, "Y_counts_by_odd_value": dict(zip(vals, counts)), "two_t": tt, "L": LL, "g": g,
                              "Yprime_coeffs_wrt_g": Ycoef, "W": Wy, "n_plus": npos, "N_s_values": sorted(Nl), "S_N": S})
print(json.dumps({"samples": samples, "examples": found, "elapsed_s": round(time.time() - T0, 2)}, indent=1))
