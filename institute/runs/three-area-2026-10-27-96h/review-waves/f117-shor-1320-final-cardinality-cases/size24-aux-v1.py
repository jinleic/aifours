#!/usr/bin/env python3
"""size24-aux-v1.py -- two auxiliary reviewer controls for the f117 |P|=24 branch.

(1) Small-n exhaustive sanity control of the assumed premise (S) [Sands, necessary direction]:
    for every direct tiling A (+) B = Z_n with 0 in A, 0 in B, |A| <= |B|, n <= NMAX, check that
    the gcd classes of nonzero differences of A and of B are disjoint.  Exhaustive over all A
    containing 0 with |A| dividing n and |A|^2 <= n, and over ALL tiling complements B of each A
    (DFS on the smallest uncovered residue).  This is a finite sanity control of the *statement*
    used by the author; it is NOT a proof of (S) and does not replace the f114 review of it.

(2) Root counting under the full known forbidden set G_full = {3,5,8,11} + H + {10,15,22,30,33,66}
    (the six forced-head-minus-old-head classes the author omitted): report which relaxed quota
    is already infeasible by counting at the root, i.e. without any search.
"""
import hashlib, json, os, subprocess, sys, time
from itertools import combinations
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "size24-aux-v1.json")
NMAX = 36


def native_date():
    return subprocess.run(["/bin/date"], capture_output=True, text=True, check=True).stdout.strip()


def classes(S, n):
    return {gcd(a - b, n) for a, b in combinations(S, 2)}


def complements(A, n):
    """All B with 0 in B and A (+) B = Z_n (every residue covered exactly once)."""
    A = sorted(A)
    covered = [False] * n
    for a in A:
        covered[a] = True        # 0 in B
    out = []

    def rec(B):
        try:
            x = covered.index(False)
        except ValueError:
            out.append(sorted(B))
            return
        for a in A:
            b = (x - a) % n
            if b <= 0 or b in B:   # b=0 is already used; B elements chosen once
                continue
            shift = [(a2 + b) % n for a2 in A]
            if any(covered[s] for s in shift):
                continue
            for s in shift:
                covered[s] = True
            B.append(b)
            rec(B)
            B.pop()
            for s in shift:
                covered[s] = False
    rec([0])
    return out


def sands_small_n(nmax):
    stats = {"nmax": nmax, "tilings_checked": 0, "violations": [], "per_n": {}}
    for n in range(2, nmax + 1):
        cnt = 0
        for k in range(1, n + 1):
            if n % k or k * k > n:
                continue
            for rest in combinations(range(1, n), k - 1):
                A = (0,) + rest
                for B in complements(A, n):
                    cnt += 1
                    cA, cB = classes(A, n), classes(B, n)
                    if cA & cB:
                        stats["violations"].append({"n": n, "A": list(A), "B": B, "common": sorted(cA & cB)})
        stats["per_n"][str(n)] = cnt
        stats["tilings_checked"] += cnt
    return stats


def gfull_root(n=1320):
    A, Y = (0, 3, 8, 11), (0, 1, 7, 13, 14)
    GA, GY = classes(A, n), classes(Y, n)
    heads = [x for x in range(n) if all(x == a or gcd(x - a, n) not in GY for a in A)]
    forced = [x for x in heads if x % 8 in (1, 2, 5, 6)]
    H = classes(forced, n)
    extra = {gcd(f - a, n) for f in forced for a in A} - GA
    G = GA | H
    Gfull = G | extra
    preds = (lambda x: x % 5 == 0, lambda x: x % 5 == 4, lambda x: x % 11 == 0, lambda x: x % 11 == 3)
    names = ("mod5=0", "mod5=4", "mod11=0", "mod11=3")
    res = {}
    for label, forb in (("G_author", G), ("G_full", Gfull)):
        cand = [x for x in range(n) if any(p(x) for p in preds) and all(x == y or gcd(x - y, n) not in forb for y in Y)]
        avail = [x for x in cand if x not in (0, 14) and all(gcd(x - y, n) not in forb for y in (0, 14))]
        need = [11 - 1, 11 - 1, 5 - 1, 5 - 1]   # anchors 0 (mod5=0, mod11=0) and 14 (mod5=4, mod11=3)
        counts = [sum(1 for x in avail if p(x)) for p in preds]
        res[label] = {"forbidden": sorted(forb), "candidates": len(cand), "available_after_anchors": len(avail),
                      "available_per_group": dict(zip(names, counts)), "need_per_group": dict(zip(names, need)),
                      "root_infeasible_groups": [names[j] for j in range(4) if counts[j] < need[j]]}
    return res


def main():
    t0 = native_date(); w0 = time.time()
    rep = {"sands_small_n_control": sands_small_n(NMAX), "gfull_root_counting": gfull_root()}
    rep["sands_small_n_control"]["violations_count"] = len(rep["sands_small_n_control"]["violations"])
    assert rep["sands_small_n_control"]["violations"] == []
    t1 = native_date()
    with open(__file__, "rb") as f:
        own = hashlib.sha256(f.read()).hexdigest()
    rep["receipt"] = {"script_sha256": own, "python": sys.version.split()[0], "native_date_before": t0,
                      "native_date_after": t1, "wall_seconds": round(time.time() - w0, 2)}
    with open(OUT, "w") as f:
        json.dump(rep, f, indent=1, sort_keys=True); f.write("\n")
    print(json.dumps({k: v for k, v in rep.items() if k != "sands_small_n_control"}, indent=1, sort_keys=True))
    s = rep["sands_small_n_control"]
    print(json.dumps({"sands_small_n_control": {"nmax": s["nmax"], "tilings_checked": s["tilings_checked"],
                                                "violations_count": s["violations_count"], "per_n": s["per_n"]}}, indent=1))


if __name__ == "__main__":
    main()
