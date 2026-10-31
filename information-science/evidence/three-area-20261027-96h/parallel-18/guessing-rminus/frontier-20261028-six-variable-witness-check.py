#!/usr/bin/env python3
"""Standalone integer verification of the six-variable gluing inequality witness."""
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-six-variable-nonshannon-witness-v1.json'
EXPECTED='10aa3d5daa42b42223193b5a465aa32e5883b592a916be5d5941ee00bc5dc169'
OUTPUT=ROOT/'frontier-20261028-six-variable-witness-check-result.json'
B,C,R,H,P,Q=(1,2,4,8,16,32)
ROWS=((B,R,C|H|P|Q,1),(C,R,B|P|Q,1),(C,Q,B|H|P,1),
      (R,P,C|H|Q,1),(H,P,B|Q,1),(H,Q,B|C|R|P,1),
      (P,Q,B|R,1),(P,Q,B|C,1),(P,Q,B|C|R|H,-2))


def cmi(a,b,z):return ((a|z,1),(b|z,1),(a|b|z,-1),(z,-1))


def verify(doc,rows):
    if doc['variable_order']!=['B','C','R','H','P','Q'] or doc['scale']!=6900000:raise ValueError('SCHEMA')
    h=doc['values_by_subset_mask'];coeff={int(m):int(c) for m,c in doc['inequality_coefficients_by_mask']}
    if len(h)!=64 or h[0]!=0 or any(not isinstance(v,int) or v<0 for v in h):raise ValueError('VECTOR')
    checks=0;full=63
    for i in range(6):
        if h[full]-h[full^(1<<i)]<0:raise ValueError('MONOTONICITY')
        checks+=1
    for i,j in combinations(range(6),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            if h[z|a]+h[z|b]-h[z|a|b]-h[z]<0:raise ValueError('CMI_NEGATIVE')
            checks+=1
            if not z:break
            z=(z-1)&(full^a^b)
    acc=Counter()
    for a,b,z,w in rows:
        if a==b or (a|b)&z or a&(a-1) or b&(b-1):raise ValueError('ROW_CONDITION')
        for mask,c in cmi(a,b,z):
            if mask:acc[mask]+=w*c
    symbolic={m:c for m,c in acc.items() if c}
    if symbolic!=coeff or any((m&P) and (m&Q) for m in symbolic):raise ValueError('SYMBOLIC_IDENTITY')
    val=sum(c*h[m] for m,c in coeff.items())
    if val!=-50548 or doc['scaled_inequality_value']!=val:raise ValueError(('WITNESS_VALUE',val))
    if checks!=246:raise ValueError('CHECK_COUNT')
    return {'elemental_shannon_checks':checks,'six_variable_entropy_terms':len(coeff),
            'mixed_PQ_terms':0,'scaled_inequality_value':val,'inequality_value':str(Fraction(val,doc['scale']))}


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    doc=json.loads(raw);result=verify(doc,ROWS);controls={}
    def expect(tag,mut):
        d=deepcopy(doc);r=list(ROWS);mut(d,r)
        try:verify(d,r)
        except (ValueError,KeyError):controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    expect('nonzero_empty_entropy',lambda d,r:d['values_by_subset_mask'].__setitem__(0,1))
    expect('changed_entropy',lambda d,r:d['values_by_subset_mask'].__setitem__(3,d['values_by_subset_mask'][3]+1))
    expect('flipped_coefficient',lambda d,r:d['inequality_coefficients_by_mask'][0].__setitem__(1,1))
    expect('removed_CMI_identity_row',lambda d,r:r.pop(0))
    expect('overlapping_condition',lambda d,r:r.__setitem__(0,(B,R,B|C|H|P|Q,1)))
    out={'witness_sha256':EXPECTED,'exact_checks':result,'mutation_controls':controls,
         'limits':'Verifies symbolic identity and Shannon-cone witness only. Entropy validity uses the separate written conditional-gluing proof; novelty and guessing-number improvement are unclaimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
