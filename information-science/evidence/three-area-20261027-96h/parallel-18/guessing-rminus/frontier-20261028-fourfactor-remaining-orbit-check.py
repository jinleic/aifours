#!/usr/bin/env python3
"""Verify the seven residual four-factor plane orbits after visibility cuts."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-fourfactor-residual-orbit-check-result.json','abad9a3797b4d2aefb9f59d67e21f33fd9051f9405c28cf7897dc489727b2d5b')
COV=('frontier-20261028-fourfactor-visibility-orbit-check-result.json','77b4c2e7e33f8e63b660bd0cd7f8d0ec45c54cd55328a88fab15d1c05e2d9a3f')
OUT=ROOT/'frontier-20261028-fourfactor-remaining-orbit-check-result.json'

def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError('HASH')
    return json.loads(raw)

def main():
    source=pin(SRC);cover=pin(COV)
    if not source['all_checked'] or not cover['all_checked']:raise ValueError('INPUT')
    allplanes={tuple(p) for o in source['orbits'] for p in o['members']};covered={tuple(x) for x in cover['covered_planes']}
    if len(allplanes)!=41 or len(covered)!=13 or not covered<=allplanes:raise ValueError('COVERAGE')
    remaining=allplanes-covered;orbits=[]
    for o in source['orbits']:
        mem={tuple(x) for x in o['members']};outside=mem&remaining
        if outside and outside!=mem:raise ValueError('PARTIAL_ORBIT')
        if outside:orbits.append(o)
    if len(remaining)!=28 or len(orbits)!=7 or any(len(o['members'])!=4 for o in orbits):raise ValueError('COUNTS')
    out={'all_checked':True,'remaining_planes':28,'orbits':orbits,'all_orbit_sizes':4,
         'limits':'Exact set-difference/orbit bookkeeping only, conditional on the separately written visibility theorem; no statement about remaining planes.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps({'all_checked':True,'remaining_planes':28,'remaining_orbits':len(orbits),'all_orbit_sizes':4},indent=2))


if __name__=='__main__':main()
