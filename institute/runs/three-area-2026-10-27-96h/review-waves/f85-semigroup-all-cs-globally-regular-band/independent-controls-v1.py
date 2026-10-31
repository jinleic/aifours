#!/usr/bin/env python3
"""Opposite-band and isolated mutation controls for F85, no author imports."""
from itertools import product
from pathlib import Path
import hashlib, json, re
root=Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f85-semigroup-all-cs-globally-regular-band')
m=json.loads((root/'manifest-v2.json').read_text())
docs=[]
for n in (2,5):
    item=m['inputs_in_read_order'][n]; data=Path(item['path']).read_bytes()
    if hashlib.sha256(data).hexdigest()!=item['sha256']: raise RuntimeError('pin')
    docs.append(data.decode())
text,host=docs
fence=re.search(r'```text\n(.*?)\n```',text,re.S).group(1)
B=tuple(tuple(map(int,line.split())) for line in fence.splitlines())
BB=tuple(product(range(5),repeat=2))
def op(x,y): return B[y[0]][x[0]],B[y[1]][x[1]]
def fold(*xs):
    v=xs[0]
    for x in xs[1:]: v=op(v,x)
    return v
def swap(x): return x[1],x[0]
assert all(op(x,x)==x for x in BB)
assert all(op(op(x,y),z)==op(x,op(y,z)) for x,y,z in product(BB,repeat=3))
assert all(swap(swap(x))==x for x in BB)
assert all(swap(op(x,y))==op(swap(x),swap(y)) for x,y in product(BB,repeat=2))
sizes=[]
for e in BB:
    loc={op(op(e,x),e) for x in BB}
    assert all(fold(x,y,x,z,x)==fold(x,y,z,x) for x,y,z in product(loc,repeat=3))
    sizes.append(len(loc))
# Mutation 1 deliberately breaks idempotence of the exact 5-band.
changed=[list(row) for row in B]; changed[1][1]=2
assert changed[1][1]!=1
# Mutation 2 makes two actual source elements with the same q share their bands.
rows=[]
for a in range(4):
    line=next(l for l in host.splitlines() if l.startswith('a='+str(a)+' '))
    rows.append([tuple(map(int,xy)) for xy in re.findall(r'\((\d),(\d)\)',line)])
assert rows[0][0]!=(4,4) and rows[2][0]==(4,4)
rows[0][0]=(4,4)
s=(0,0,0); t=(0,2,0)
q=lambda p:(p[0],0 if p[1]==4 else p[1]%2,p[2])
assert s!=t and q(s)==q(t) and rows[s[1]][s[2]]==rows[t[1]][t[2]]
print(json.dumps({'opposite_band_order':len(BB),'opposite_associativity_triples':len(BB)**3,
 'opposite_corners':len(sizes),'opposite_corner_sizes':sorted(set(sizes)),
 'diagonal_mutation_rejected_for':'idempotence at 1','coefficient_mutation_rejected_for':'same-actor collision',
 'coefficient_collision':[s,t], 'limit':'controls test distinct named invariants, not arbitrary mutations'},indent=2))
