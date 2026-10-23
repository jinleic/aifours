#!/usr/bin/env python3
"""Exact symmetry audit of an MCDSQS certificate built over an affine group (standard library).
G = <y -> m*y + b for the given generators m:b>.  Checks:
 (i)   the block set is invariant under every generator of G;
 (ii)  G is transitive on points; reports |G| and the stabilizer G_0 (as multipliers);
 (iii) the colouring at 0 is invariant under y -> r*y (r = RES_GEN): r maps classes onto classes;
 (iv)  every POINT x section equals g_x(POINT 0) class by class, g_x the least element of G
       (sorted image tuples) with g_x(0) = x;
 (v)   for EVERY g in G, g(colouring at 0) equals the colouring at g(0) as a set of classes.
Informational: whether y -> y+1 preserves the block set (cyclicity).
Usage: audit_symmetry.py CERT GENS RES_GEN OUT.json   (GENS like 1:2,3:1)"""
import json
import sys
from collections import deque

cert, gens_s, rg, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
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
        blocks.append(frozenset(int(x) for x in t))
    else:
        col[cur][-1].append(frozenset(int(x) for x in t))
gens = [tuple(int(z) for z in g.split(":")) for g in gens_s.split(",")]
perms = [tuple((m * y + b) % v for y in range(v)) for m, b in gens]
e = tuple(range(v))
G, dq = {e}, deque([e])
while dq:
    a = dq.popleft()
    for p in perms:
        c = tuple(p[a[y]] for y in range(v))
        if c not in G:
            G.add(c); dq.append(c)
G = sorted(G)
B = set(blocks)
rec = {"certificate": cert, "v": v, "generators": gens_s, "res_gen": rg, "group_order": len(G)}
rec["blocks_invariant_under_generators"] = all(frozenset(p[y] for y in b) in B for p in perms for b in B)
rec["transitive"] = sorted({g[0] for g in G}) == list(range(v))
rec["stabilizer_of_0_multipliers"] = sorted(g[1] for g in G if g[0] == 0)
cls0 = [frozenset(C) for C in col[0]]
rimg = [frozenset(frozenset((rg * p) % v for p in t) for t in C) for C in cls0]
rec["colouring_at_0_res_invariant"] = set(rimg) == set(cls0)
gx = {}
for g in G:
    gx.setdefault(g[0], g)
rec["points_are_least_element_images"] = all(
    [frozenset(frozenset(gx[x][p] for p in t) for t in C) for C in cls0] == [frozenset(C) for C in col[x]]
    for x in range(v))
rec["every_g_maps_colouring_0_to_colouring_g0"] = all(
    {frozenset(frozenset(g[p] for p in t) for t in C) for C in cls0} == {frozenset(C) for C in col[g[0]]}
    for g in G)
rec["info_translation_by_1_preserves_blocks"] = all(frozenset((y + 1) % v for y in b) in B for b in B)
rec["result"] = "PASS" if all(rec[k] for k in (
    "blocks_invariant_under_generators", "transitive", "colouring_at_0_res_invariant",
    "points_are_least_element_images", "every_g_maps_colouring_0_to_colouring_g0")) else "FAIL"
json.dump(rec, open(out, "w"), indent=1)
print(json.dumps(rec))
