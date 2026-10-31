#!/usr/bin/env python3
"""Pin and rationally verify a two-Ingleton FD balance-identity proposal."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
PROPOSAL=ROOT/'frontier-20261028-defect-multiplier-lp-result.json'
EXPECTED='0653cb9625c0be1a168ba5461e54be8a6fb33e6eea82d394629f00997d1f073e'
BASE=ROOT/'frontier-20261028-copy-family-upper-lp.py'
BASE_HASH='f23e91be2a2440ab29b759983f4b0306e146c4a2dabc90038c6a461582c275e0'
OUT=ROOT/'frontier-20261028-two-ingleton-exact-dual-v1.json'


def main():
    raw=PROPOSAL.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(BASE.read_bytes()).hexdigest()!=BASE_HASH:raise ValueError('INPUT_HASH')
    doc=json.loads(raw)
    if doc['status_float_unverified']!='Optimal':raise ValueError('NO_SOLVER_PROPOSAL')
    sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
    spec=spec_from_file_location('entropybase',BASE);base=module_from_spec(spec);spec.loader.exec_module(base)
    orbit,reps=base.canonical_orbits(base.automorphism_group());rows=doc['rows'];kinds=Counter(x['metadata']['kind'] for x in rows)
    if kinds!=Counter({'CMI':99,'conditional-ingleton':2,'FD':3}):raise ValueError(('SUPPORT_SHAPE',kinds))
    acc=[Fraction(0) for _ in reps]
    for row in rows:
        w=Fraction(row['weight'])
        if row['metadata']['kind']!='FD' and w<0:raise ValueError('NEGATIVE_INEQUALITY_WEIGHT')
        for i,c in row['orbit_terms']:acc[i]+=w*c
    caps=[{'orbit_representative':1,'weight':'4/3'},{'orbit_representative':2,'weight':'8/3'},
          {'orbit_representative':4,'weight':'8/3'}]
    for x in caps:acc[orbit[x['orbit_representative']]]-=Fraction(x['weight'])
    acc[orbit[base.FULL]]+=1
    if any(acc):raise ValueError('EXACT_IDENTITY')
    mass=sum(Fraction(r['weight']) for r in rows if r['metadata']['kind']=='conditional-ingleton')
    if mass!=Fraction(1,4):raise ValueError('INGLETON_MASS')
    out={'proposal_sha256':EXPECTED,'base_sha256':BASE_HASH,'claim_scope':'unrestricted FD balance identity; rank upper uses Ingleton only',
         'bound':'20/3','orbits':reps,'caps':caps,
         'rows':[{'metadata':r['metadata'],'orbit_terms':r['orbit_terms'],'weight':r['weight']} for r in rows],
         'expected_row_count':104,'fraction_status':'exact','ingleton_total':'1/4',
         'limits':'Candidate until separate checker rebuilds graph, all row expressions, signs, caps and identity.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'row_kinds':dict(kinds),'orbits':len(reps),'ingleton_mass':str(mass),'coefficient_residual':[]},indent=2))


if __name__=='__main__':main()
