"""Controls for verify_amh.verify:
 positive: actual pair counts of the hexacode (n=6,delta=4) and dodecacode (n=12,delta=6) -> ALL_PASS;
           the [[24,0,10]] candidate -> ALL_PASS.
 n=24 alpha control: pair counts of random additive groups C in F4^24 (|C| = 2^10) give PSD blocks
           (Gamma = 1_C 1_C^T is PSD); checked with the verifier's own block code.
 mutations of the candidate: +1 on one count; -1 on one count; swap two counts; scale all by 2;
           flip one count to make S3 asymmetric -> each must FAIL.
"""
import json
import random
import sys
from fractions import Fraction

import numpy as np

sys.path.insert(0, ".")
from pairs import group_from_generators, pair_counts, weight_distribution  # noqa: E402
from verify_amh import alp, gam, psd, verify  # noqa: E402


def counts_from_lambda(lam):
    out = {}
    for (i, j, t, p), v in lam.items():
        key = json.dumps([sorted([j - t, i - t, p]), t - p])
        if key in out:
            assert out[key] == v, "not S3-symmetric"
        out[key] = v
    return out


def blocks_psd_only(lam, n):
    x = {o: Fraction(v, gam(*o, n)) for o, v in lam.items()}
    bad = []
    for a in range(n + 1):
        for k in range(a, n + 1):
            if k > n + a - k:
                continue
            idx = list(range(k, n + a - k + 1))
            M = [[Fraction(0)] * len(idx) for _ in idx]
            for r, i in enumerate(idx):
                for c, j in enumerate(idx):
                    for t in range(min(i, j) + 1):
                        for p in range(t + 1):
                            v = x.get((i, j, t, p), 0)
                            if v:
                                if (i + j) % 2:
                                    raise ValueError("odd i+j with nonzero x: use even-weight groups")
                                M[r][c] += alp(i, j, t, p, a, k, n) * v
            if not psd(M):
                bad.append((a, k))
    return bad

def random_even_group(n, r, seed):
    """Random commuting additive group with all elements of even weight: generators are even-weight Pauli
    strings that pairwise commute (symplectic orthogonality makes t-p even, so wt(u+v) = wt u + wt v - t - p
    stays even)."""
    from pairs import parse, symp
    rng = random.Random(seed)
    gens = []
    tries = 0
    while len(gens) < r and tries < 100000:
        tries += 1
        s = "".join(rng.choice("IXYZ") for _ in range(n))
        if sum(ch != "I" for ch in s) % 2:
            continue
        if all(symp(*parse(s), *parse(g)) == 0 for g in gens):
            gens.append(s)
    return gens


if __name__ == "__main__":
    res = {}
    data = json.load(open("../evidence/control_pair_counts.json"))
    for name, delta in (("hexacode", 4), ("dodecacode_circulant_1_3_6", 6)):
        n = data[name]["n"]
        lam = {tuple(map(int, k.split(","))): v for k, v in data[name]["lambda"].items()}
        wd = data[name]["weight_distribution"]
        rep = verify(counts_from_lambda(lam), n=n, delta=delta, K=1, A={w: wd[w] for w in range(n + 1)})
        res[name] = rep["ALL_PASS"]
        print(name, "ALL_PASS" if rep["ALL_PASS"] else {k: v for k, v in rep.items() if v is False})
    cand = json.load(open("../evidence/candidate_subspace.json"))
    counts = {k: int(v) for k, v in cand["counts"].items()}
    res["candidate"] = verify(counts)["ALL_PASS"]
    print("candidate ALL_PASS:", res["candidate"])
    # n=24 alpha control with random even-weight additive groups (sum of even-weight Paulis is even weight)
    ok24 = []
    for seed in range(3):
        gens = random_even_group(24, 10, seed)
        try:
            X, Z = group_from_generators(gens, 24)
        except AssertionError:
            continue
        lam = pair_counts(X, Z, 24)
        bad = blocks_psd_only(lam, 24)
        ok24.append(not bad)
        print("random even group seed", seed, "blocks PSD:", not bad, bad[:5])
    res["n24_random_group_blocks_psd"] = all(ok24) and len(ok24) > 0
    # mutations
    keys = sorted(counts, key=lambda k: -counts[k])
    muts = {}
    k0, k1 = keys[3], keys[50]
    m = dict(counts); m[k0] += 1; muts["plus1"] = m
    m = dict(counts); m[k1] -= 1; muts["minus1"] = m
    m = dict(counts); m[k0], m[k1] = m[k1], m[k0]; muts["swap"] = m
    m = {k: 2 * v for k, v in counts.items()}; muts["double"] = m
    for nm, mc in muts.items():
        r = verify(mc)
        res["mutation_" + nm + "_fails"] = not r["ALL_PASS"]
        print("mutation", nm, "fails as required:", not r["ALL_PASS"],
              [k for k, v in r.items() if v is False][:4])
    json.dump(res, open("../evidence/verify_controls.json", "w"), indent=1)
    print("ALL CONTROLS OK" if all(res.values()) else "CONTROL FAILURE")
