#!/usr/bin/env python3
"""Standard-library expander: compact mcDSQS seed (affine point-transitive group + colouring at
0) -> certificate bytes.  Usage: expand_seed.py SEED.json OUT [COMPARE]"""
import hashlib
import json
import sys
from collections import deque

seed = json.load(open(sys.argv[1]))
v, r = seed["v"], seed["colours"]
perms = [tuple((m * y + b) % v for y in range(v))
         for m, b in (tuple(int(z) for z in g.split(":")) for g in seed["group_generators"])]
e = tuple(range(v))
G, dq = {e}, deque([e])
while dq:
    a = dq.popleft()
    for p in perms:
        c = tuple(p[a[y]] for y in range(v))
        if c not in G:
            G.add(c); dq.append(c)
G = sorted(G)
classes = [[tuple(t) for t in C] for C in seed["classes_at_0"]]
D0 = [t for C in classes for t in C]
blocks = sorted({tuple(sorted(g[p] for p in (0,) + t)) for t in D0 for g in G})
gx = {}
for g in G:
    gx.setdefault(g[0], g)
assert sorted(gx) == list(range(v)), "group is not transitive"
lines = [seed["certificate_header"], f"MCDSQS {v}", f"COLOURS {r}", "BLOCKS"]
lines += [" ".join(map(str, b)) for b in blocks]
for x in range(v):
    lines.append(f"POINT {x}")
    for c, C in enumerate(classes):
        lines.append(f"CLASS {c}")
        lines += [" ".join(map(str, t)) for t in sorted(tuple(sorted(gx[x][p] for p in t)) for t in C)]
data = ("\n".join(lines) + "\n").encode()
open(sys.argv[2], "wb").write(data)
print("group order", len(G), "blocks", len(blocks), "sha256", hashlib.sha256(data).hexdigest())
if len(sys.argv) > 3:
    same = open(sys.argv[3], "rb").read() == data
    print("byte-identical to", sys.argv[3], ":", same)
    sys.exit(0 if same else 1)
