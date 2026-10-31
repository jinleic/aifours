#!/usr/bin/env python3
"""Standalone exact check of the five-variable gluing inequality witness."""
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-five-variable-nonshannon-witness-v1.json'
EXPECTED='def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392'
SIX=ROOT/'frontier-20261028-six-variable-nonshannon-witness-v1.json'
SIXHASH='10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169'
OUTPUT=ROOT/'frontier-20261028-five-variable-witness-check-result.json'
C,R,H,P,Q=(1,2,4,8,16)
ROWS=((C,R,P|Q,1),(C,Q,H|P,1),(R,P,C|H|Q,1),
      (H,P,Q,1),(H,Q,C|R|P,1),(P,Q,R,1),(P,Q,C,1),(P,Q,C|R|H,-2))


def cmi(a,b,z):return ((a|z,1),(b|z,1),(a|b|z,-1),(z,-1))


def verify(doc,rows,six):
    if doc['variable_order']!=['C','R','H','P','Q'] or doc['scale']!=4:raise ValueError('SCHEMA')
    h=doc['values_by_subset_mask'];coeff={int(m):int(c) for m,c in doc['inequality_coefficients_by_mask']}
    if len(h)!=32 or h[0]!=0 or any(not isinstance(v,int) or v<0 for v in h):raise ValueError('VECTOR')
    checks=0;full=31
    for i in range(5):
        if h[full]-h[full^(1<<i)]<0:raise ValueError('MONOTONICITY')
        checks+=1
    for i,j in combinations(range(5),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if h[z|a]+h[z|b]-h[z|a|b]-h[z]<0:raise ValueError('CMI_NEGATIVE')
            checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    acc=Counter()
    for a,b,z,w in rows:
        if a==b or (a|b)&z or a&(a-1) or b&(b-1):raise ValueError('ROW_CONDITION')
        for m,c in cmi(a,b,z):
            if m:acc[m]+=w*c
    symbolic={m:c for m,c in acc.items() if c}
    reduced=Counter()
    for m,c in six['inequality_coefficients_by_mask']:
        if m>>1:reduced[m>>1]+=c
    reduced={m:c for m,c in reduced.items() if c}
    if symbolic!=coeff or reduced!=coeff or any((m&P) and (m&Q) for m in symbolic):raise ValueError('IDENTITY_OR_REDUCTION')
    val=sum(c*h[m] for m,c in coeff.items())
    if val!=-2 or doc['scaled_inequality_value']!=val:raise ValueError(('WITNESS_VALUE',val))
    if checks!=85:raise ValueError('CHECK_COUNT')
    return {'elemental_shannon_checks':checks,'five_variable_entropy_terms':len(coeff),
            'mixed_PQ_terms':0,'scaled_inequality_value':val,'inequality_value':str(Fraction(val,doc['scale']))}


def main():
    raw=INPUT.read_bytes();sixraw=SIX.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(sixraw).hexdigest()!=SIXHASH:raise ValueError('INPUT_HASH')
    doc=json.loads(raw);six=json.loads(sixraw);result=verify(doc,ROWS,six);controls={}
    def expect(tag,mut):
        d=deepcopy(doc);r=list(ROWS);q=deepcopy(six);mut(d,r,q)
        try:verify(d,r,q)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('nonzero_empty_entropy',lambda d,r,q:d['values_by_subset_mask'].__setitem__(0,1))
    expect('changed_entropy',lambda d,r,q:d['values_by_subset_mask'].__setitem__(1,d['values_by_subset_mask'][1]+1))
    expect('flipped_coefficient',lambda d,r,q:d['inequality_coefficients_by_mask'][0].__setitem__(1,1))
    expect('removed_CMI_identity_row',lambda d,r,q:r.pop(0))
    expect('overlapping_condition',lambda d,r,q:r.__setitem__(0,(C,R,C|P|Q,1)))
    out={'witness_sha256':EXPECTED,'six_variable_source_sha256':SIXHASH,'exact_checks':result,
         'mutation_controls':controls,
         'limits':'Verifies symbolic reduction and Shannon-cone witness. Entropy validity uses the written conditional-gluing proof; novelty and guessing-number improvement are unclaimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
