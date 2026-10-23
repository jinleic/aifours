#!/usr/bin/env python3
"""Read-only structure analysis of the colouring at point 0 of a T1 MCDSQS certificate
(labels y in Z_{2p}, (x,i) = (y mod p, y mod 2)).  For every class: missing point, triple
types (a: two copy-0 points, b: one copy-0 point, c: copy-1 only), and for type-a triples the
copy-0 pairs {y,z} with their ratio z/y, sum y+z and product yz (mod p).  Prints JSON lines.
Usage: analyze_colouring.py CERT P"""
import json
import sys

cert, p = sys.argv[1], int(sys.argv[2])
v = 2 * p
classes, cur, pt = [], None, None
for raw in open(cert):
    s = raw.split("#")[0].strip()
    if not s:
        continue
    t = s.split()
    if t[0] == "POINT":
        if pt is not None:
            break
        pt = int(t[1])
    elif t[0] == "CLASS" and pt == 0:
        classes.append([])
    elif pt == 0:
        classes[-1].append(tuple(int(x) for x in t))
xi = lambda y: (y % p, y % 2)
inv = lambda a: pow(a % p, p - 2, p)
allpts = {xi(y) for y in range(1, v)}
for j, C in enumerate(classes):
    pts = {xi(y) for T in C for y in T}
    miss = sorted(allpts - pts)
    kinds = {"a": [], "b": [], "c": []}
    for T in C:
        P = [xi(y) for y in T]
        n0 = sum(1 for x, i in P if i == 0)
        if n0 == 2:
            (y1, _), (y2, _) = [q for q in P if q[1] == 0]
            (u, _), = [q for q in P if q[1] == 1]
            kinds["a"].append({"pair": sorted([y1, y2]), "lift": u, "ratio": sorted([y2 * inv(y1) % p, y1 * inv(y2) % p]),
                               "sum": (y1 + y2) % p, "prod": y1 * y2 % p})
        elif n0 == 1:
            kinds["b"].append(sorted(P))
        elif n0 == 0:
            kinds["c"].append(sorted(x for x, _ in P))
        else:
            kinds.setdefault("copy0_only", []).append(sorted(x for x, _ in P))
    print(json.dumps({"class": j, "size": len(C), "missing": miss, "n_a": len(kinds["a"]), "n_b": len(kinds["b"]),
                      "n_c": len(kinds["c"]), "a_sums": sorted(k["sum"] for k in kinds["a"]),
                      "a_ratios": sorted(k["ratio"][0] for k in kinds["a"]), "c": kinds["c"]}))
