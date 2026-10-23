#!/usr/bin/env python3
"""probe_z9_types_and_pairing_congruence_v1.py (ContinueCFR21; frozen before execution; stdlib only; <=280 s).
(1) Heuristic calibration: mod-3 type of every pinned normalised orthomorphism of Z9 (old lane list of all 225),
    i.e. counts of x + theta(x) mod 3 (must be 3*f); report the type histogram and whether every theta is
    'minus one mod 3' (theta(x) = -x mod 3 for all x).
(2) Check of the derived pairing congruence on the 96 pinned P21 DM6 (n = 21, lambda = 7): for every 4 distinct
    rows and each of the 3 pairings chi = e_a+e_b-e_c-e_d, the three value counts of chi(c) mod 3 must all be
    congruent to 2 mod 3; for every 5 distinct rows and each (4,1) character the counts must be congruent to 1 mod 3;
    triple-sum counts must be multiples of 3. Report violations (expected none) and type histograms.
Args: z9_list sha p21_json sha."""
import sys, json, time, hashlib, itertools
T0 = time.monotonic()
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
z9 = [[0] + list(map(int, ln.split())) for ln in pinned(sys.argv[1], sys.argv[2]).decode().strip().splitlines()]
p21 = json.loads(pinned(sys.argv[3], sys.argv[4]))
out = {"status": "OK"}
th = {}; minus1 = 0; ok9 = 0
for f in z9:
    n = 9
    if sorted(f) == list(range(n)) and sorted((f[x] - x) % n for x in range(n)) == list(range(n)): ok9 += 1
    cnt = [0, 0, 0]
    for x in range(n): cnt[(x + f[x]) % 3] += 1
    t = str(sorted(cnt, reverse=True)); th[t] = th.get(t, 0) + 1
    if all((f[x] + x) % 3 == 0 for x in range(n)): minus1 += 1
out["z9_maps"] = len(z9); out["z9_valid_orthomorphisms"] = ok9
out["z9_sum_count_types"] = th; out["z9_minus_one_mod3"] = minus1
viol = {"triple": 0, "pairing": 0, "four_one": 0}; hist = {"triple": {}, "pairing": {}, "four_one": {}}
for dm in p21["dms"]:
    A = [[x % 3 for x in r] for r in dm["rows"]]; k = len(A); n = 21
    def counts(chi):
        c = [0, 0, 0]
        for col in range(n): c[sum(chi[i] * A[i][col] for i in range(k)) % 3] += 1
        return c
    for S in itertools.combinations(range(k), 3):
        chi = [0] * k
        for i in S: chi[i] = 1
        c = counts(chi); key = str(sorted(c, reverse=True)); hist["triple"][key] = hist["triple"].get(key, 0) + 1
        if any(x % 3 for x in c): viol["triple"] += 1
    for S in itertools.combinations(range(k), 4):
        a, b, c_, d = S
        for (p1, p2, m1, m2) in ((a, b, c_, d), (a, c_, b, d), (a, d, b, c_)):
            chi = [0] * k; chi[p1] = 1; chi[p2] = 1; chi[m1] = 2; chi[m2] = 2
            c = counts(chi); key = str(sorted(c, reverse=True)); hist["pairing"][key] = hist["pairing"].get(key, 0) + 1
            if any(x % 3 != 2 for x in c): viol["pairing"] += 1
    for S in itertools.combinations(range(k), 5):
        for neg in S:
            chi = [0] * k
            for i in S: chi[i] = 1
            chi[neg] = 2
            c = counts(chi); key = str(sorted(c, reverse=True)); hist["four_one"][key] = hist["four_one"].get(key, 0) + 1
            if any(x % 3 != 1 for x in c): viol["four_one"] += 1
out["p21_violations"] = viol; out["p21_count_histograms"] = hist
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))
