#!/usr/bin/env python3
"""Exact exhaustive disjoint-block scan of the five-variable gluing inequality.

Five nonempty disjoint blocks and an optional disjoint conditioning block are
assigned from the ten original graph variables. A nonnegative result is only
for this one rational source-LP profile.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
WITNESS=ROOT/'frontier-20261028-five-variable-nonshannon-witness-v1.json'
WHASH='def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392'
OUTPUT=ROOT/'frontier-20261028-fivevar-original-all-blocks-scan-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes();wr=WITNESS.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(wr).hexdigest()!=WHASH:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];data={tuple(e['entropy_variables']):Fraction(e['value']) for e in entries}
    names='abcdefghij';vals=[Fraction(0)]+[data[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(v.denominator for v in vals));H=np.array([int(x*scale) for x in vals],dtype=np.int64)
    terms=[(int(m),int(c)) for m,c in json.loads(wr)['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0 or max(abs(int(x)) for x in H)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('TERM_OR_RANGE')
    nlow=7**6;codes=np.arange(nlow,dtype=np.int64);low=[np.zeros(nlow,dtype=np.int64) for _ in range(6)];t=codes.copy()
    for i in range(6):
        digit=t%7;t//=7
        for j in range(6):low[j]|=np.where(digit==j+1,1<<i,0)
    checked=0;minimum=None;viol=[]
    for code in range(7**4):
        t=code;high=[0]*6
        for i in range(6,10):
            digit=t%7;t//=7
            if digit:high[digit-1]|=1<<i
        blocks=[low[j]|high[j] for j in range(6)];ok=np.ones(nlow,dtype=bool)
        for j in range(5):ok &= blocks[j]>0
        roles=[x[ok] for x in blocks[:5]];z=blocks[5][ok]
        if not len(z):continue
        value=np.zeros(len(z),dtype=np.int64)
        for m,c in terms:
            index=z.copy()
            for j in range(5):
                if m&(1<<j):index|=roles[j]
            value+=c*H[index]
        checked+=len(z);local=int(value.min());minimum=local if minimum is None else min(minimum,local)
        if local<0:
            for i in np.flatnonzero(value<0)[:20]:
                viol.append({'role_masks':[int(x[i]) for x in roles],'condition_mask':int(z[i]),
                             'exact_slack':str(Fraction(int(value[i]),scale))})
            break
    expected=sum((-1)**k*comb(5,k)*(7-k)**10 for k in range(6))
    if not viol and checked!=expected:raise ValueError(('ENUMERATION',checked,expected))
    out={'profile_sha256':EXPECTED,'inequality_witness_sha256':WHASH,'base_scale':scale,
         'scope':'five pairwise-disjoint nonempty original-variable blocks, optional disjoint conditioning; no role-symmetry quotient',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'violations':viol,'elapsed_seconds':monotonic()-start,
         'limits':'One rational source-LP original profile only. Overlapping substitutions and general original entropy realizability remain open.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
