#!/usr/bin/env python3
"""[generalized copy of describe_rdsqs52.py: v and multiplier from argv]
Orbit-level description of a cyclic RDSQS certificate (stdlib; self-checking).
Outputs block-orbit representatives under G = Z_V x| <M> and class-orbit representatives of
the resolution at 0 under <M>, and verifies that these regenerate the block set and the
resolution at 0 exactly.  Usage: describe_cyclic_rdsqs.py CERT OUT.json OUT.md V M"""
import json, sys, hashlib
cert, oj, om = sys.argv[1:4]
v, M = int(sys.argv[4]), int(sys.argv[5])
blocks, res0, cur = [], [], None
for raw in open(cert):
    s = raw.split('#')[0].strip()
    if not s: continue
    t = s.split()
    if t[0] in ('RDSQS', 'BLOCKS'): continue
    if t[0] == 'POINT':
        if cur is not None: break
        cur = int(t[1]); continue
    if t[0] == 'CLASS': res0.append([]); continue
    if cur is None: blocks.append(tuple(sorted(map(int, t))))
    else: res0[-1].append(tuple(sorted(map(int, t))))
grp, x = [], 1
while True:
    grp.append(x); x = x * M % v
    if x == 1: break
G = [(m, b) for m in grp for b in range(v)]
img = lambda g, blk: tuple(sorted((g[0] * p + g[1]) % v for p in blk))
B = set(blocks); seen = set(); reps = []
for b in sorted(B):
    if b in seen: continue
    orb = {img(g, b) for g in G}; seen |= orb; reps.append((b, len(orb)))
assert seen == B
cls = [frozenset(C) for C in res0]; cset = set(cls); cseen = set(); creps = []
for C in sorted(cls, key=sorted):
    if C in cseen: continue
    orb = {frozenset(img((m, 0), t) for t in C) for m in grp}; cseen |= orb; creps.append((sorted(C), len(orb)))
assert cseen == cset
out = {"certificate_sha256": hashlib.sha256(open(cert, 'rb').read()).hexdigest(), "group": f"Z{v} x| <{M}>, (m,b): y -> m*y+b",
       "multiplier_group": grp, "block_orbit_reps": [{"rep": list(b), "orbit": s} for b, s in reps],
       "class_orbit_reps_at_0": [{"rep": [list(t) for t in C], "orbit": s} for C, s in creps]}
json.dump(out, open(oj, 'w'), indent=1)
md = [f"# RDSQS({v}): orbit data (generated and self-checked by code/describe_cyclic_rdsqs.py)", "",
      f"Certificate sha256 `{out['certificate_sha256']}`. G = Z{v} ⋊ ⟨{M}⟩ = {{y ↦ m·y + b : m ∈ {grp}, b ∈ Z{v}}} (order {len(G)}).", "",
      f"## {len(reps)} block-orbit representatives under G (orbit length in brackets)", "",
      "; ".join("{" + ",".join(map(str, b)) + f"}}[{s}]" for b, s in reps), "",
      f"## Resolution of the derived STS({v-1}) at 0: {len(creps)} class-orbit representatives under ⟨{M}⟩", ""]
for i, (C, s) in enumerate(creps):
    md.append(f"* K{i} [{s}]: " + " ".join("{" + ",".join(map(str, t)) + "}" for t in C))
md += ["", "The resolution at x is the translate x + (resolution at 0) (as a set of classes)."]
open(om, 'w').write("\n".join(md) + "\n")
print(len(reps), "block orbits;", [s for _, s in creps], "class orbits")
