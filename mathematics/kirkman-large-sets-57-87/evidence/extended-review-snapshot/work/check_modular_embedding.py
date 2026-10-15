#!/usr/bin/env python3
"""Embed an existing cyclic LKTS base in the joint modular model, then resolve it.
Run: uv run --with ortools==9.15.6755 python work/check_modular_embedding.py evidence/denniston15.txt
This checks representability; it is not an unhinted construction claim.
"""
import argparse
import json
from pathlib import Path
from ortools.sat.python import cp_model
from check_lkts import parse_certificate
from search_modular import build_model, extract
import search_staged as staged

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("certificate",type=Path)
args = ap.parse_args()
v,systems = parse_certificate(args.certificate)
n = v-2
blocks = [tuple(sorted(b)) for pc in systems[0] for b in pc]
assert (0,n,n+1) in blocks
starts = []
for infinity in (n,n+1):
    positions = {}
    for b in blocks:
        if infinity in b and len([x for x in b if x>=n]) == 1:
            x,y = [x for x in b if x<n]
            delta = (y-x)%n
            d = min(delta,n-delta)
            positions[d] = x if delta == d else y
    starts.append([positions[d] for d in range(1,(n+1)//2)])
swapped = starts[0][0] > starts[1][0]
if swapped:
    starts.reverse()
    blocks = [tuple(sorted(2*n+1-x if x>=n else x for x in b)) for b in blocks]
model,primary,infinity_vars,shifts,reps = build_model(v)
finite = {staged.orbit_key(b,n):b for b in blocks if b[-1]<n}
values = starts[0]+starts[1]
for rep in reps:
    target = finite[rep]
    candidates = [c for c in target if tuple(sorted((x+c)%n for x in rep)) == target]
    assert len(candidates) == 1
    values.append(candidates[0])
assert len(values) == len(primary)
for var,value in zip(primary,values):
    model.add(var == value)
solver,status,info = staged.cp_solve(model,30,1,123)
assert status in (cp_model.OPTIMAL,cp_model.FEASIBLE),info
actual,matchings = extract(v,solver,infinity_vars,shifts,reps)
assert set(actual) == set(blocks)
base,resolution = staged.resolve(v,actual,matchings,30,1,123)
assert base is not None,resolution
receipt = {"verdict":"PASS","v":v,"scope":"known certificate representability, not unhinted discovery",
           "certificate_sha256":staged.digest(args.certificate),"swapped_infinity_labels":swapped,
           "modular_model":info,"resolution":resolution,"source_sha256":staged.digest(__file__),
           "model_source_sha256":staged.digest(Path(__file__).with_name("search_modular.py"))}
output = Path(__file__).resolve().parent.parent/f"evidence/extended-modular-embedding{v}.json"
output.write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt,indent=2))
