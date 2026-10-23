#!/usr/bin/env python3
"""Exact finite checks for the point-cyclic 2-(88,4,1) nonexistence proof (PROOF.md).  Stdlib only, integers only.

These are CONTROLS of the finite lemmas used in the written proof, not the proof itself.

Usage: check88.py [v ...]      (default: 88 64 52 76 148; every v must satisfy v = 4 (mod 12))
For each v (point set Z_v, sigma = +1, n = v/4 blocks per class, r = (v-1)/3 classes):
  E1 (exhaustive, all C(v,4) 4-subsets): stabilizer of every 4-subset computed from its 3 candidate translations;
     tally of stabilizer orders; the "admissible" 4-subsets (no translate B+d != B meets B in >= 2 points, i.e.
     possible blocks of a sigma-invariant design with lambda = 1) with nontrivial stabilizer are listed; they must be
     exactly the n cosets of the order-4 subgroup <n>; every admissible 4-subset containing a diameter pair
     {x, x+v/2} must be such a coset.
  E2 (exhaustive over all divisors h of v and all m in 0..n): the admissible (class-stabilizer order h, number m
     of short blocks in the class) pairs under (i) v/h <= r, (ii) h | n-m, (iii) (v/h)*m <= n; also with the extra
     condition (iv) (h/gcd(h,4)) | m.  Reports whether type T1 (m in {0,n} only) is forced.
  E3 (if T1 forced): admissible stabilizer orders of the other classes: h | n and v/h <= r-1; their gcd g; the
     subgroup H_g = <v/g>; whether H_g is contained in H_4 = <n>.  If not, every nonzero d in H_g \\ H_4 gives a
     pair {0,d} that no block can contain (written proof, Steps 4-5): contradiction, so no point-cyclic resolution.
Exit code 0; a JSON receipt is written to evidence/check88-receipt.json when run with the default list.
"""
import itertools
import json
import math
import os
import sys
import time


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def subgroup(v, h):
    """the unique subgroup of Z_v of order h"""
    return frozenset(range(0, v, v // h))


def stabilizer(B, v):
    b0 = B[0]
    stab = [0]
    S = set(B)
    for b in B[1:]:
        d = (b - b0) % v
        if all(((x + d) % v) in S for x in B):
            stab.append(d)
    return frozenset(stab)


def admissible(B, v, stab):
    """no translate B+d different from B meets B in >= 2 points"""
    S = set(B)
    diffs = {}
    for x in B:
        for y in B:
            if x != y:
                diffs.setdefault((y - x) % v, []).append((x, y))
    # |B cap (B+d)| = number of ordered pairs (x,y) in B with y - x = d; >= 2 and d not in stab -> inadmissible
    for d, prs in diffs.items():
        if len(prs) >= 2 and d not in stab:
            return False
    return True


def e1(v):
    n = v // 4
    H4 = subgroup(v, 4)
    cosets = {frozenset((a + t) % v for t in H4) for a in range(v)}
    tally = {}
    nontriv_adm = set()
    diam_adm = set()
    t0 = time.time()
    for B in itertools.combinations(range(v), 4):
        st = stabilizer(B, v)
        tally[len(st)] = tally.get(len(st), 0) + 1
        has_diam = any((x + v // 2) % v in B for x in B)
        if len(st) > 1 or has_diam:
            if admissible(B, v, st):
                if len(st) > 1:
                    nontriv_adm.add(frozenset(B))
                if has_diam:
                    diam_adm.add(frozenset(B))
    ok = nontriv_adm == cosets and diam_adm == cosets and len(cosets) == n
    return dict(subsets=math.comb(v, 4), stabilizer_order_tally={str(k): tally[k] for k in sorted(tally)},
                admissible_with_nontrivial_stabilizer=len(nontriv_adm), admissible_with_diameter_pair=len(diam_adm),
                both_equal_the_cosets_of_H4=ok, seconds=round(time.time() - t0, 2))


def e2(v):
    n, r = v // 4, (v - 1) // 3
    rows = []
    for h in divisors(v):
        for m in range(0, n + 1):
            c1 = v <= r * h                 # v/h <= r, exact
            c2 = (n - m) % h == 0
            c3 = (v // h) * m <= n
            c4 = m % (h // math.gcd(h, 4)) == 0
            if c1 and c2 and c3:
                rows.append(dict(h=h, m=m, short_orbit_divisibility=c4))
    mixed = [x for x in rows if 1 <= x["m"] <= n - 1]
    mixed_iv = [x for x in mixed if x["short_orbit_divisibility"]]
    return dict(n=n, r=r, admissible_pairs=rows, mixed_admissible=mixed, mixed_admissible_with_iv=mixed_iv,
                T1_forced=not mixed, T1_forced_with_iv=not mixed_iv)


def e3(v):
    n, r = v // 4, (v - 1) // 3
    hs = [h for h in divisors(v) if n % h == 0 and v <= (r - 1) * h]
    if not hs:
        return dict(nonshort_stabilizer_orders=[], note="no admissible stabilizer: no resolution at all")
    g = 0
    for h in hs:
        g = math.gcd(g, h)
    Hg, H4 = subgroup(v, g), subgroup(v, 4)
    short_diffs = sorted(H4 - {0})
    witness = sorted(Hg - H4)
    return dict(nonshort_stabilizer_orders=hs, gcd=g, common_subgroup=sorted(Hg), short_block_differences=short_diffs,
                common_subgroup_inside_H4=Hg <= H4, uncovered_difference_witnesses=witness,
                contradiction=bool(witness))


def main(argv):
    vs = [int(x) for x in argv[1:]] or [88, 64, 52, 76, 148]
    out = []
    for v in vs:
        assert v % 12 == 4, v
        rec = dict(v=v)
        rec["E2"] = e2(v)
        if rec["E2"]["T1_forced"]:
            rec["E3"] = e3(v)
        rec["E1"] = e1(v) if v <= 100 else "skipped (v > 100)"
        out.append(rec)
        e2r = rec["E2"]
        print("v=%d n=%d r=%d  T1 forced: %s (with iv: %s); mixed (h,m): %s" % (
            v, e2r["n"], e2r["r"], e2r["T1_forced"], e2r["T1_forced_with_iv"],
            [(x["h"], x["m"]) for x in e2r["mixed_admissible"]]))
        print("   all admissible (h,m): %s" % [(x["h"], x["m"]) for x in e2r["admissible_pairs"]])
        if "E3" in rec:
            e = rec["E3"]
            print("   non-short stabilizer orders %s, gcd %s, common subgroup inside H4: %s, contradiction: %s, "
                  "witnesses %s" % (e["nonshort_stabilizer_orders"], e.get("gcd"), e.get("common_subgroup_inside_H4"),
                                    e.get("contradiction"), e.get("uncovered_difference_witnesses")))
        if isinstance(rec["E1"], dict):
            print("   E1: %s" % rec["E1"])
        sys.stdout.flush()
    if len(argv) == 1:
        here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(here, "evidence", "check88-receipt.json"), "w") as fh:
            json.dump(dict(finished_at=time.strftime("%Y-%m-%d %H:%M:%S %Z"), python=sys.version.split()[0],
                           results=out), fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
