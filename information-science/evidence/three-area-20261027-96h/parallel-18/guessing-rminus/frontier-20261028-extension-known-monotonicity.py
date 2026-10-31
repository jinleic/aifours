#!/usr/bin/env python3
"""Check all immediately nested known entropy coordinates in source branches."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
OUTPUT=ROOT/'frontier-20261028-extension-known-monotonicity-result.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
BASE=tuple('abcdefghij')
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values']
    values={frozenset(x['entropy_variables']):Fraction(x['value']) for x in items}
    if len(values)!=len(items):raise ValueError('DUPLICATE')
    values[frozenset()]=Fraction(0)
    result=[]
    for branch,labels in enumerate(BRANCHES,1):
        allowed=set(labels);valid=[s for s in values if s<=allowed];checked=0;bad=[]
        for s in valid:
            for vertex in allowed-s:
                t=s|{vertex}
                if t not in values:continue
                checked+=1;delta=values[t]-values[s]
                if delta<0:
                    bad.append({'smaller':sorted(s),'larger':sorted(t),'added':vertex,
                                'H_smaller':str(values[s]),'H_larger':str(values[t]),
                                'conditional_entropy':str(delta)})
        bad.sort(key=lambda x:Fraction(x['conditional_entropy']))
        result.append({'branch':branch,'known_monotonicity_edges_checked':checked,
                       'violations':len(bad),'first_20_most_negative':bad[:20]})
    out={'point_sha256':EXPECTED,'branches':result,
         'limits':'Each negative nested pair disproves extension of this fixed point to an entropy vector. It does not rule out another auxiliary extension of the same base projection or improve the original bound.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    for x in result:
        print(json.dumps({'branch':x['branch'],'checked':x['known_monotonicity_edges_checked'],
                          'violations':x['violations'],'first':x['first_20_most_negative'][:1]},indent=2))


if __name__=='__main__':main()
