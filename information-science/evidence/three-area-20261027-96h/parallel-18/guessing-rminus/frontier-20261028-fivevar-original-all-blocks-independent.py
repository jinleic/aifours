#!/usr/bin/env python3
"""Independent exact replay of all disjoint five-block gluing substitutions.

Uses a different 5+5 base-seven enumeration split from the producing 6+4
scanner. No prior scanner module is imported. Only the fixed LP base point is
checked, with arbitrary optional disjoint conditioning.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
WITNESS=('frontier-20261028-five-variable-nonshannon-witness-v1.json','def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392')
OUTPUT=ROOT/'frontier-20261028-fivevar-original-all-blocks-independent-result.json'


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    start=monotonic();doc=pin(INPUT);w=pin(WITNESS)
    data={tuple(e['entropy_variables']):Fraction(e['value']) for e in doc['primal_values']};names='abcdefghij'
    vals=[Fraction(0)]+[data[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in vals));H=np.array([int(x*scale) for x in vals],dtype=np.int64)
    terms=[(int(m),int(c)) for m,c in w['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0:raise ValueError('TERM_MAP')
    if sum(c*w['values_by_subset_mask'][m] for m,c in terms)!=-2:raise ValueError('SEPARATING_WITNESS')
    if max(abs(int(x)) for x in H)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    low_count=7**5;codes=np.arange(low_count,dtype=np.int64)
    low=[np.zeros(low_count,dtype=np.int64) for _ in range(6)]
    for i in range(5):
        digit=(codes//(7**i))%7
        for role in range(6):low[role]|=np.where(digit==role+1,1<<i,0)
    checked=0;minimum=None;first=None
    for highcode in range(7**5):
        high=[0]*6
        for i in range(5):
            digit=(highcode//(7**i))%7
            if digit:high[digit-1]|=1<<(5+i)
        blocks=[low[j]|high[j] for j in range(6)]
        good=np.logical_and.reduce([blocks[j]>0 for j in range(5)])
        if not np.any(good):continue
        roles=[x[good] for x in blocks[:5]];z=blocks[5][good]
        result=np.zeros(len(z),dtype=np.int64)
        for m,c in terms:
            key=z.copy()
            for i in range(5):
                if m&(1<<i):key|=roles[i]
            result+=c*H[key]
        checked+=len(z);local=int(result.min());minimum=local if minimum is None else min(minimum,local)
        if local<0:
            i=int(np.flatnonzero(result<0)[0]);first={'role_masks':[int(x[i]) for x in roles],
                 'condition_mask':int(z[i]),'exact_slack':str(Fraction(int(result[i]),scale))};break
    expected=sum((-1)**k*comb(5,k)*(7-k)**10 for k in range(6))
    if first is None and checked!=expected:raise ValueError(('COUNT',checked,expected))
    out={'profile_sha256':INPUT[1],'witness_sha256':WITNESS[1],
         'scope':'all five nonempty pairwise-disjoint original blocks with optional disjoint condition; no role quotient',
         'enumeration_split':'base-seven first five / last five original variables',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'first_violation':first,'source_witness_value_check':'-1/2',
         'elapsed_seconds':monotonic()-start,
         'limits':'One base profile and one inequality family only; overlapping blocks, other inequalities, and actual entropy realizability remain open.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
