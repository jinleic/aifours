#!/usr/bin/env python3
"""Pin a rational graph-FD balance identity with one Ingleton shape."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parent
PROPOSAL=ROOT/'frontier-20261028-one-ingleton-defect-search-result.json'
EXPECTED='76473f469e3690b02add60d24a5f9aefae08074e8c34ad07b5b718157d55cd00'
BASE=ROOT/'frontier-20261028-copy-family-upper-lp.py'
BASE_HASH='f23e91be2a2440ab29b759983f4b0306e146c4a2dabc90038c6a461582c275e0'
OUT=ROOT/'frontier-20261028-diamond-ingleton-exact-dual-v1.json'


def main():
    raw=PROPOSAL.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(BASE.read_bytes()).hexdigest()!=BASE_HASH:raise ValueError('INPUT_HASH')
    case=json.loads(raw)['cases'][0]
    if case['status_float_unverified']!='Optimal':raise ValueError('NO_SOLVER_PROPOSAL')
    sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
    spec=spec_from_file_location('entropybase',BASE);base=module_from_spec(spec);spec.loader.exec_module(base)
    orbit,reps=base.canonical_orbits(base.automorphism_group());rows=case['rows'];kinds=Counter(x['metadata']['kind'] for x in rows)
    if kinds!=Counter({'CMI':62,'conditional-ingleton':1,'FD':3}):raise ValueError(('SUPPORT_SHAPE',kinds))
    acc=[Fraction(0) for _ in reps]
    for row in rows:
        w=Fraction(row['weight'])
        if row['metadata']['kind']!='FD' and w<=0:raise ValueError('NONPOSITIVE_INEQUALITY_WEIGHT')
        for i,c in row['orbit_terms']:acc[i]+=w*c
    caps=[{'orbit_representative':1,'weight':'4/3'},{'orbit_representative':2,'weight':'8/3'},
          {'orbit_representative':4,'weight':'8/3'}]
    for x in caps:acc[orbit[x['orbit_representative']]]-=Fraction(x['weight'])
    acc[orbit[base.FULL]]+=1
    if any(acc):raise ValueError('EXACT_IDENTITY')
    ing=[r for r in rows if r['metadata']['kind']=='conditional-ingleton']
    m=ing[0]['metadata']
    if (m['A'],m['B'],m['C'],m['D'],m['Z_mask'],Fraction(ing[0]['weight']))!=(2,4,1,3,1008,Fraction(1,3)):
        raise ValueError('DIAMOND_ROW')
    out={'proposal_sha256':EXPECTED,'base_sha256':BASE_HASH,'claim_scope':'unrestricted graph-FD balance identity; Ingleton rank upper only',
         'bound':'20/3','orbits':reps,'caps':caps,'rows':rows,'expected_row_count':66,
         'fraction_status':'exact','ingleton_total':'1/3',
         'limits':'Candidate until a separate checker rebuilds graph, all row expressions, signs, caps and identity.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'row_kinds':dict(kinds),'orbits':len(reps),'ingleton_mass':'1/3','coefficient_residual':[]},indent=2))


if __name__=='__main__':main()
