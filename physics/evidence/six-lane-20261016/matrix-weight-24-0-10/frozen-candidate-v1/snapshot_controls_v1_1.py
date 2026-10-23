"""Receipts for the frozen candidate (AMH Open Problem 1 table):
 1. primary: verify_amh on lambda_24_0_10.json (full AMH-indexed table)        -> must ALL_PASS
 2. positive controls: brute-force pair counts of hexacode (6,2^6,4) and dodecacode (12,2^12,6), regenerated
    here from explicit generators (controls.py), checked with the same verifier at their own (n, delta, A)
                                                                                -> must ALL_PASS
 3. n=24 Terwilliger-block control: pair counts of 3 random commuting even-weight additive groups of size 2^10
    (Gamma = 1_C 1_C^T is PSD)                                                  -> blocks must be PSD
 4. mutations of the table: +1, -1, swap two values, double all, delete one entry, add a spurious entry
                                                                                -> each must FAIL
Writes receipts/controls_v1_1.json (same controls, run against verify_amh_v1_1); exit code 0 iff all hold.
"""
import json
import random
import sys
from fractions import Fraction

from controls import CONTROLS, verify as verify_code
from pairs import group_from_generators, pair_counts, parse, symp
from verify_amh_v1_1 import Q3, alp, gam, psd, verify


def counts_from_lambda(lam):
    out = {}
    for (i, j, t, p), v in lam.items():
        key = json.dumps([sorted([j - t, i - t, p]), t - p])
        assert out.get(key, v) == v, "control table not S3-symmetric"
        out[key] = v
    return out


def blocks_psd(lam, n):
    x = {o: Fraction(v, gam(*o, n)) for o, v in lam.items()}
    bad = []
    for a in range(n + 1):
        for k in range(a, n + 1):
            if k > n + a - k:
                continue
            idx = list(range(k, n + a - k + 1))
            M = [[Q3(0) for _ in idx] for _ in idx]
            for r, i in enumerate(idx):
                for c, j in enumerate(idx):
                    for t in range(min(i, j) + 1):
                        for p in range(t + 1):
                            v = x.get((i, j, t, p), 0)
                            if v:
                                M[r][c] += alp(i, j, t, p, a, k, n) * v
            if not psd(M):
                bad.append((a, k))
    return bad


def random_even_group(n, r, seed):
    rng = random.Random(seed)
    gens = []
    while len(gens) < r:
        s = "".join(rng.choice("IXYZ") for _ in range(n))
        if sum(ch != "I" for ch in s) % 2 == 0 and all(symp(*parse(s), *parse(g)) == 0 for g in gens):
            gens.append(s)
    return gens


if __name__ == "__main__":
    rec = {}
    table = json.load(open("lambda_24_0_10.json"))
    entries = [[int(v) for v in e] for e in table["entries"]]
    r = verify(entries=entries)
    rec["primary_ALL_PASS"] = r["ALL_PASS"]
    rec["primary_report"] = r
    for (name, gens, n), delta in zip(CONTROLS[1:], (4, 6)):
        X, Z, wd, d = verify_code(gens, n)
        lam = pair_counts(X, Z, n)
        rr = verify(counts_from_lambda(lam), n=n, delta=delta, K=1, A={w: int(wd[w]) for w in range(n + 1)})
        rec[f"positive_{name}_ALL_PASS"] = rr["ALL_PASS"]
    ok24 = []
    for seed in range(3):
        X, Z = group_from_generators(random_even_group(24, 10, seed), 24)
        ok24.append(not blocks_psd(pair_counts(X, Z, 24), 24))
    rec["n24_random_even_groups_blocks_psd"] = ok24
    # sqrt(3) path: random commuting groups with odd-weight elements (alpha irrational when i+j is odd)
    okodd = []
    for seed in range(3):
        rng = random.Random(100 + seed)
        gens = []
        while len(gens) < 4:
            s = "".join(rng.choice("IXYZ") for _ in range(7))
            if s != "I" * 7 and all(symp(*parse(s), *parse(g)) == 0 for g in gens):
                try:
                    group_from_generators(gens + [s], 7)
                    gens.append(s)
                except AssertionError:
                    pass
        X, Z = group_from_generators(gens, 7)
        lam = pair_counts(X, Z, 7)
        has_odd = any((i + j) % 2 for (i, j, t, p) in lam)
        okodd.append(has_odd and not blocks_psd(lam, 7))
    rec["n7_random_groups_with_odd_weights_blocks_psd"] = okodd
    ok24 = ok24 + okodd
    order = sorted(range(len(entries)), key=lambda k: -entries[k][4])
    a, b = order[3], order[50]
    muts = {}
    m = [e[:] for e in entries]; m[a][4] += 1; muts["plus1"] = m
    m = [e[:] for e in entries]; m[b][4] -= 1; muts["minus1"] = m
    m = [e[:] for e in entries]; m[a][4], m[b][4] = m[b][4], m[a][4]; muts["swap"] = m
    m = [[*e[:4], 2 * e[4]] for e in entries]; muts["double"] = m
    m = [e[:] for e in entries if e is not entries[a]]; muts["delete_one"] = m
    m = [e[:] for e in entries] + [[11, 0, 0, 0, 1]]; muts["spurious_odd_weight"] = m
    for nm, mm in muts.items():
        rr = verify(entries=mm)
        rec[f"mutation_{nm}_fails"] = not rr["ALL_PASS"]
        rec[f"mutation_{nm}_failed_checks"] = [k for k, v in rr.items() if v is False]
    expect = [rec["primary_ALL_PASS"]] + [v for k, v in rec.items() if k.startswith("positive_")] + ok24 + \
             [v for k, v in rec.items() if k.startswith("mutation_") and k.endswith("_fails")]
    rec["ALL_EXPECTATIONS_HOLD"] = all(expect)
    json.dump(rec, open("receipts/controls_v1_1.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in rec.items() if k != "primary_report"}, indent=1))
    sys.exit(0 if rec["ALL_EXPECTATIONS_HOLD"] else 1)
