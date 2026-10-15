#!/usr/bin/env python3
"""Finite arithmetic accompanying proof.md; no assertion of LKTS existence.
Reproduce: python3 work/screen_symmetries.py
"""
from collections import Counter
import hashlib
import json
import math
from pathlib import Path


def cycles(multiplier,n):
    unused = set(range(n))
    counts = Counter()
    while unused:
        x = min(unused)
        orbit = []
        while x not in orbit:
            orbit.append(x)
            unused.remove(x)
            x = multiplier*x % n
        counts[len(orbit)] += 1
    counts[1] += 2  # Both infinity points are fixed.
    return dict(sorted(counts.items()))


rows = []
for n in (55,85):
    for a in range(1,n):
        if math.gcd(a,n) != 1:
            continue
        powers = [a]
        while powers[-1] != 1:
            powers.append(powers[-1]*a % n)
        reasons = []
        for p in powers:
            cs = cycles(p,n)
            if p == n-1:
                reasons.append({"power":p,"obstruction":"negation fixes both infinities","proof":"proof.md#2"})
            if math.gcd(p-1,n) == 5:
                reasons.append({"power":p,"obstruction":"seven-point fixed subsystem","proof":"proof.md#3"})
            if 2 not in cs and cs[1] % 3:
                reasons.append({"power":p,"obstruction":"fixed class, no point 2-cycles, fixed-point count not 0mod3","proof":"proof.md#8"})
            if p != 1 and p*p % n == 1 and (n+2) % cs[1]:
                reasons.append({"power":p,"obstruction":"involution fixed-point count does not divide v","proof":"proof.md#7","fixed_points":cs[1]})
        rows.append({"n":n,"v":n+2,"multiplier":a,"order":len(powers),"point_cycle_counts":cycles(a,n),
                     "excluded_by_elementary_proof":bool(reasons),"reasons":reasons})
root = Path(__file__).resolve().parent.parent
result = {"scope":"cyclic transversal base KTS with multiplier-invariant resolution, both infinities fixed",
          "survivors":{str(n):[r["multiplier"] for r in rows if r["n"]==n and not r["excluded_by_elementary_proof"]] for n in (55,85)},
          "rows":rows,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert len(rows) == 104  # phi(55)=40, phi(85)=64.
assert result["survivors"] == {"55":[1], "85":[1]}
(root/"evidence/symmetry-screen.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result["survivors"],indent=2))
