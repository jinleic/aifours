#!/usr/bin/env python3
"""Standard-library expander: compact cyclic RDSQS seed -> certificate bytes.
Usage: expand_rdsqs_seed.py SEED.json OUT [COMPARE]"""
import json, sys, hashlib
seed = json.load(open(sys.argv[1]))
v = seed["v"]; gen = seed["multiplier_generator"]
M, x = [], 1
while True:
    M.append(x); x = x * gen % v
    if x == 1: break
G = sorted(tuple((m * y + b) % v for y in range(v)) for m in M for b in range(v))
classes = [[tuple(t) for t in C] for C in seed["classes_at_0"]]
D0 = [t for C in classes for t in C]
blocks = sorted({tuple(sorted(((p + s) % v) for p in (0,) + t)) for t in D0 for s in range(v)})
res = {}
for g in G:
    if g[0] not in res:
        res[g[0]] = [sorted(tuple(sorted(g[p] for p in t)) for t in C) for C in classes]
assert sorted(res) == list(range(v))
lines = [seed["certificate_header"], f"RDSQS {v}", "BLOCKS"]
lines += [" ".join(map(str, b)) for b in blocks]
for xx in range(v):
    lines.append(f"POINT {xx}")
    for c, C in enumerate(res[xx]):
        lines.append(f"CLASS {c}")
        lines += [" ".join(map(str, t)) for t in C]
data = ("\n".join(lines) + "\n").encode()
open(sys.argv[2], "wb").write(data)
print("blocks", len(blocks), "sha256", hashlib.sha256(data).hexdigest())
if len(sys.argv) > 3:
    same = open(sys.argv[3], "rb").read() == data
    print("byte-identical to", sys.argv[3], ":", same)
    sys.exit(0 if same else 1)
