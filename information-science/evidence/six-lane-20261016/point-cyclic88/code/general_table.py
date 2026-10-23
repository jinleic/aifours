#!/usr/bin/env python3
"""Consistency table for the general form of the obstruction (PROOF.md, Section 6), v = 4n = 4 (mod 12), v <= VMAX.

For each v: is type T1 forced by conditions (i)-(iii) [and with the extra condition (iv)]?  If T1 is forced: the
admissible stabilizer orders h of the other classes (h | n, v/h <= r-1), their gcd g, and whether <v/g> is inside
H4 = <n>.  "EXCLUDED" means the written argument (Lemmas 1-4 for general v) proves that no point-cyclic resolution
of a 2-(v,4,1) design exists.  Controls (must hold, else the argument or the code is wrong):
  - known existence (must NOT be excluded): v = 52 (Lam-Miao-Mishima 2001, via the source), v = 64 (the source),
    and v = 4q with q a prime = 13 (mod 24) (Lam-Miao 1999 as quoted by the source: q a product of primes 12s+1,
    s odd; only the prime cases are used here);
  - known nonexistence (consistency, should be excluded): v = 4p, p prime, p = 7 (mod 12) (Genma-Mishima-Jimbo 1997
    as quoted by the source: v/k prime forces v/k = 1 (mod k(k-1))).
Exact integer arithmetic only.  Writes evidence/general-table.json.
"""
import json
import math
import os
import sys


def isprime(p):
    return p > 1 and all(p % q for q in range(2, int(p ** 0.5) + 1))


def analyse(v, use_iv):
    n, r = v // 4, (v - 1) // 3
    divs = [h for h in range(1, v + 1) if v % h == 0]
    mixed = []
    for h in divs:
        if v > r * h:
            continue
        for m in range(1, n):
            if (n - m) % h == 0 and (v // h) * m <= n and (not use_iv or m % (h // math.gcd(h, 4)) == 0):
                mixed.append((h, m))
    if mixed:
        return dict(T1_forced=False, mixed_example=mixed[0], excluded=False)
    hs = [h for h in divs if n % h == 0 and v <= (r - 1) * h]
    if not hs:
        return dict(T1_forced=True, nonshort_h=[], excluded=True, reason="no admissible non-short stabilizer")
    g = 0
    for h in hs:
        g = math.gcd(g, h)
    return dict(T1_forced=True, nonshort_h=hs, gcd=g, excluded=(4 % g != 0),
                reason="common subgroup of order %d not inside H4" % g if 4 % g else "common subgroup inside H4")


def main(argv):
    vmax = int(argv[1]) if len(argv) > 1 else 2000
    rows, problems = [], []
    known_exist = {52: "LMM2001", 64: "TZ2026"}
    for p in range(13, vmax // 4 + 1):
        if isprime(p) and p % 24 == 13:
            known_exist[4 * p] = "LM1999 prime case"
    known_none = {4 * p: "GMJ1997 prime" for p in range(5, vmax // 4 + 1) if isprime(p) and p % 12 == 7}
    for v in range(16, vmax + 1, 12):
        a, b = analyse(v, False), analyse(v, True)
        row = dict(v=v, n=v // 4, basic=a, with_iv=b, known=known_exist.get(v) or known_none.get(v))
        if v in known_exist and (a["excluded"] or b["excluded"]):
            problems.append("known-existence v=%d excluded" % v)
        if v in known_none and not a["excluded"]:
            row["note"] = "GMJ exclusion not reproduced by this argument (allowed; not a contradiction)"
        rows.append(row)
    excl = [r["v"] for r in rows if r["basic"]["excluded"]]
    excl_iv = [r["v"] for r in rows if r["with_iv"]["excluded"]]
    print("v <= %d, v = 4 (mod 12): %d values" % (vmax, len(rows)))
    print("excluded by (i)-(iii): %s" % excl)
    print("excluded with (iv) as well: %s" % excl_iv)
    print("known-existence controls: %s" % sorted(known_exist))
    print("GMJ controls (should be excluded): %s; reproduced: %s" % (
        sorted(known_none), sorted(v for v in known_none if v in excl)))
    print("PROBLEMS: %s" % (problems or "none"))
    fam_a = sorted(4 * p for p in range(5, vmax // 4 + 1) if isprime(p) and p % 12 == 7)
    fam_b = sorted(8 * p for p in range(5, vmax // 8 + 1) if isprime(p) and p % 12 == 11)
    print("family A = {4p : p prime, p = 7 mod 12}: %s" % fam_a)
    print("family B = {8p : p prime, p = 11 mod 12}: %s" % fam_b)
    print("excluded set equals A u B (pattern observation up to vmax, not a theorem): %s" % (sorted(fam_a + fam_b) == excl))
    for v in (16, 28, 40, 52, 64, 76, 88, 100, 112, 124, 136, 148, 160, 172, 184, 196):
        r = next(x for x in rows if x["v"] == v)
        print("  v=%d: %s | with iv: %s" % (v, r["basic"], r["with_iv"]))
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(here, "evidence", "general-table.json"), "w") as fh:
        json.dump(dict(vmax=vmax, excluded=excl, excluded_with_iv=excl_iv, problems=problems, rows=rows), fh, indent=1)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
