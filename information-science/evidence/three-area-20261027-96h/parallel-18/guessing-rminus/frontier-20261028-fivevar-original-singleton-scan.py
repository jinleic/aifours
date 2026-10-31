#!/usr/bin/env python3
"""Exact conditional singleton substitutions of the universal six-var inequality.

Scans the fixed rational original profile. A violation would yield a valid
original-variable cut; absence is only this restricted substitution scope.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations,permutations
from math import lcm,perm
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
WITNESS=ROOT/'frontier-20261028-five-variable-nonshannon-witness-v1.json'
WHASH='def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392'
OUTPUT=ROOT/'frontier-20261028-fivevar-original-singleton-scan-result.json'


def main():
    start=monotonic();raw=INPUT.read_bytes();wr=WITNESS.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(wr).hexdigest()!=WHASH:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];data={tuple(e['entropy_variables']):Fraction(e['value']) for e in entries}
    names='abcdefghij';values=[Fraction(0)]+[data[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in values));H=np.array([int(x*scale) for x in values],dtype=np.int64)
    terms=[(int(m),int(c)) for m,c in json.loads(wr)['inequality_coefficients_by_mask']]
    if len(terms)!=15 or sum(c for _,c in terms)!=0:raise ValueError('TERM_MAP')
    if max(abs(int(x)) for x in H)*sum(abs(c) for _,c in terms)>=2**62:raise ValueError('INTEGER_RANGE')
    checked=0;minimum=None;violations=[]
    for zsize in range(6):
        for zs in combinations(range(10),zsize):
            z=sum(1<<i for i in zs);available=[i for i in range(10) if i not in zs]
            flat=np.fromiter((i for p in permutations(available,5) for i in p),dtype=np.int16)
            if not len(flat):continue
            pairs=flat.reshape((-1,5));bits=np.left_shift(1,pairs.astype(np.int64));value=np.zeros(len(pairs),dtype=np.int64)
            for m,c in terms:
                indices=np.full(len(pairs),z,dtype=np.int64)
                for j in range(5):
                    if m&(1<<j):indices |= bits[:,j]
                value += c*H[indices]
            checked+=len(pairs);local=int(value.min());minimum=local if minimum is None else min(minimum,local)
            if local<0:
                for j in np.flatnonzero(value<0)[:10]:
                    violations.append({'role_vertices':[int(x)+1 for x in pairs[j]],'condition_mask':z,
                                       'exact_slack':str(Fraction(int(value[j]),scale))})
                break
        if violations:break
    expected=perm(10,5)*(1<<5)
    if not violations and checked!=expected:raise ValueError(('ENUMERATION',checked,expected))
    out={'profile_sha256':EXPECTED,'inequality_witness_sha256':WHASH,'base_scale':scale,
         'scope':'five distinct singleton original variables; arbitrary disjoint conditioning subset',
         'substitutions_checked':checked,'complete_expected_count':expected,
         'minimum_exact_slack':str(Fraction(minimum,scale)) if minimum is not None else None,
         'violations':violations,'elapsed_seconds':monotonic()-start,
         'limits':'Checks only this rational source-LP original profile and five-singleton substitutions; no entropy realization or general bound follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
