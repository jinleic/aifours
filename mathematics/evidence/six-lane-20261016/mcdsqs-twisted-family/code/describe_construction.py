#!/usr/bin/env python3
"""Human-readable description of an affine-group mcDSQS certificate (standard library):
G-orbit representatives of the blocks (least block of each orbit), orbit lengths, and the
colouring at 0 organised by the orbits of y -> RES_GEN*y on its classes.
Usage: describe_construction.py CERT GENS RES_GEN OUT.json OUT.md"""
import json
import sys
from collections import deque

cert, gens_s, rg, oj, om = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5]
v = None
blocks, col, cur = [], {}, None
for raw in open(cert):
    s = raw.split("#")[0].strip()
    if not s:
        continue
    t = s.split()
    if t[0] == "MCDSQS":
        v = int(t[1])
    elif t[0] in ("COLOURS", "BLOCKS"):
        continue
    elif t[0] == "POINT":
        cur = int(t[1]); col[cur] = []
    elif t[0] == "CLASS":
        col[cur].append([])
    elif cur is None:
        blocks.append(tuple(sorted(int(x) for x in t)))
    else:
        col[cur][-1].append(tuple(sorted(int(x) for x in t)))
perms = [tuple((m * y + b) % v for y in range(v))
         for m, b in (tuple(int(z) for z in g.split(":")) for g in gens_s.split(","))]
e = tuple(range(v))
G, dq = {e}, deque([e])
while dq:
    a = dq.popleft()
    for p in perms:
        c = tuple(p[a[y]] for y in range(v))
        if c not in G:
            G.add(c); dq.append(c)
G = sorted(G)
left, orbits = set(blocks), []
for b in sorted(blocks):
    if b not in left:
        continue
    orb = {tuple(sorted(g[p] for p in b)) for g in G}
    assert orb <= left
    left -= orb
    orbits.append({"representative": list(b), "length": len(orb)})
lengths = {}
for o in orbits:
    lengths[o["length"]] = lengths.get(o["length"], 0) + 1
cls0 = col[0]
key = [frozenset(C) for C in cls0]
img = [key.index(frozenset(tuple(sorted((rg * p) % v for p in t)) for t in C)) for C in cls0]
cycles, seen = [], set()
for i in range(len(cls0)):
    if i in seen:
        continue
    cyc, j = [], i
    while j not in seen:
        seen.add(j); cyc.append(j); j = img[j]
    cycles.append(cyc)
miss0 = {y: [j for j, C in enumerate(cls0) if all(y not in t for t in C)] for y in range(1, v)}
desc = {"certificate": cert, "v": v, "generators": gens_s, "group_order": len(G),
        "block_orbits": len(orbits), "block_orbit_lengths": dict(sorted(lengths.items())),
        "orbits": orbits, "res_gen": rg, "class_cycles_under_res_gen": cycles,
        "class_sizes_at_0": [len(C) for C in cls0], "classes_at_0": cls0,
        "classes_missing_point_at_0": {str(y): miss0[y] for y in miss0}}
json.dump(desc, open(oj, "w"), indent=1)
L = [f"# Orbit description of `{cert}`", "",
     f"Group G = ⟨y ↦ m·y+b : {gens_s}⟩ on Z{v}, |G| = {len(G)}.", "",
     f"## Blocks: {len(orbits)} G-orbits, lengths {dict(sorted(lengths.items()))} "
     f"(sum {sum(o['length'] for o in orbits)})", "",
     "| # | least block of the orbit | length |", "|---|---|---|"]
L += [f"| {i} | {{{', '.join(map(str, o['representative']))}}} | {o['length']} |" for i, o in enumerate(orbits)]
L += ["", f"## Colouring at 0 (classes in certificate order; y ↦ {rg}·y permutes them in cycles "
      f"{[len(c) for c in cycles]})", ""]
for j, C in enumerate(cls0):
    L.append(f"* class {j} ({len(C)} triples): " + " ".join("{" + ",".join(map(str, t)) + "}" for t in C))
L += ["", "Every point y ≠ 0 is missed by exactly one class at 0: "
      + ("yes" if all(len(m) == 1 for m in miss0.values()) else "NO") + "."]
open(om, "w").write("\n".join(L) + "\n")
print(json.dumps({k: desc[k] for k in ("group_order", "block_orbits", "block_orbit_lengths",
                                       "class_sizes_at_0")} | {"cycles": [len(c) for c in cycles]}))
