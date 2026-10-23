#!/usr/bin/env python3
"""Exact structure (necessary conditions only, NO search) for optimal (v,k,1) CPCW codes, written for the
cpcw-optimal lane (independent of the prep structure_notes.py).

For each (v,k):
  H = floor((v-1)/2) coverable +-classes [d]={d,-d}, d=1..H (for even v the class v/2 is self-paired and can never
  be covered: a pair {a,a+v/2} gives the ordered difference v/2 twice).  s = floor((v-1)/(k(k-1))) codewords,
  each covering C(k,2) classes; leave c = H - s*C(k,2) uncovered classes besides v/2.
  Even v: a codeword with i elements of one parity and k-i of the other (type i, 0<=i<=k/2; translation by an odd
  number swaps the parities, so i ~ k-i) has C(i,2)+C(k-i,2) same-parity pairs (even classes) and i(k-i)
  cross pairs (odd classes).  Solve sum a_i = s, sum i(k-i) a_i = (#odd coverable classes) - z_odd,
  sum [C(i,2)+C(k-i,2)] a_i = (#even coverable classes) - z_even, z_odd + z_even = c.
  Leave orbits: orbits of c-subsets of classes under Z_v^* (multiplier action on classes).
Output: JSON on stdout.
"""
import itertools
import json
import math
import sys


def orbit_reps_of_leaves(v, H, c, allowed=None):
    units = [m for m in range(1, v) if math.gcd(m, v) == 1]
    cls = lambda d: min(d % v, (-d) % v)
    classes = list(range(1, H + 1)) if allowed is None else allowed
    if c == 0:
        return [[]], 1
    seen, reps = set(), []
    for S in itertools.combinations(classes, c):
        key = tuple(sorted(S))
        if key in seen:
            continue
        orb = set()
        for m in units:
            orb.add(tuple(sorted(cls(m * d) for d in S)))
        seen |= orb
        reps.append((list(key), len(orb)))
    return reps, len(seen)


def parity_systems(v, k, s, c):
    H = (v - 1) // 2
    odd = sum(1 for d in range(1, H + 1) if d % 2 == 1)
    even = H - odd
    out = []
    for z_odd in range(c + 1):
        z_even = c - z_odd
        if z_odd > odd or z_even > even:
            continue
        for a in itertools.product(range(s + 1), repeat=k // 2 + 1):
            if sum(a) != s:
                continue
            cross = sum(i * (k - i) * a[i] for i in range(len(a)))
            same = sum((i * (i - 1) // 2 + (k - i) * (k - i - 1) // 2) * a[i] for i in range(len(a)))
            if cross == odd - z_odd and same == even - z_even:
                out.append({"z_odd": z_odd, "z_even": z_even, "a": list(a)})
    return {"odd_coverable_classes": odd, "even_coverable_classes": even, "solutions": out}


def unit_info(v):
    units = [m for m in range(1, v) if math.gcd(m, v) == 1]
    def order(a):
        x, o = a, 1
        while x != 1:
            x = x * a % v
            o += 1
        return o
    orders = sorted({order(a) for a in units})
    return {"phi": len(units), "element_orders": orders}


def main():
    cases = [(122, 6), (123, 6), (124, 6), (143, 5), (144, 5), (146, 5), (162, 5), (167, 5),
             (121, 6), (125, 6), (126, 6), (62, 6), (92, 6), (82, 5)]
    rep = {}
    for v, k in cases:
        H = (v - 1) // 2
        s = (v - 1) // (k * (k - 1))
        c = H - s * k * (k - 1) // 2
        r = {"v": v, "k": k, "s": s, "H_coverable_classes": H, "classes_per_codeword": k * (k - 1) // 2,
             "leave_c": c, "half_v_forced_uncovered": v % 2 == 0, "units": unit_info(v)}
        if v % 2 == 0:
            r["parity"] = parity_systems(v, k, s, c)
        if c <= 2:
            allowed = None
            reps, tot = orbit_reps_of_leaves(v, H, c, allowed)
            r["leave_orbits_all"] = {"count": len(reps), "total_leaves": tot,
                                     "reps": reps if c > 0 else []}
            if v % 2 == 0 and c > 0:
                sols = r["parity"]["solutions"]
                ok = []
                for S, size in reps:
                    zo = sum(1 for d in S if d % 2 == 1)
                    if any(x["z_odd"] == zo for x in sols):
                        ok.append([S, size])
                r["leave_orbits_parity_admissible"] = {"count": len(ok), "reps": ok}
        elif c == 3:
            reps, tot = orbit_reps_of_leaves(v, H, c)
            r["leave_orbits_all"] = {"count": len(reps), "total_leaves": tot}
        rep["%d,%d" % (v, k)] = r
    json.dump(rep, sys.stdout, indent=1, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
