#!/usr/bin/env python3
"""Check monotonicity on all known nested entropy-set pairs per source branch."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-source-monotone-primal-frozen.json'
EXPECTED='55afaaa4dc2bdffca9bdc59fcbaf7d4988b58f2a4bdb8a72d06a5eae257502bc'
OUTPUT=ROOT/'frontier-20261028-all-known-nested-check-result.json'
BASE=tuple('abcdefghij')
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values']
    values={frozenset(x['entropy_variables']):Fraction(x['value']) for x in items}
    if len(values)!=len(items):raise ValueError('DUPLICATE')
    values[frozenset()]=Fraction(0)
    summaries=[]
    for branch,labels in enumerate(BRANCHES,1):
        whole=frozenset(labels);n=len(labels);full=(1<<n)-1
        lookup={}
        for s,val in values.items():
            if s<=whole:
                mask=sum(1<<i for i,v in enumerate(labels) if v in s);lookup[mask]=val
        checked=0;bad=[]
        for small,val in lookup.items():
            rem=full^small;add=rem
            while add:
                large=small|add
                if large in lookup:
                    checked+=1;delta=lookup[large]-val
                    if delta<0:
                        bad.append({'smaller':[labels[i] for i in range(n) if small&(1<<i)],
                                    'larger':[labels[i] for i in range(n) if large&(1<<i)],
                                    'H_smaller':str(val),'H_larger':str(lookup[large]),
                                    'difference':str(delta)})
                add=(add-1)&rem
        bad.sort(key=lambda x:Fraction(x['difference']))
        summaries.append({'branch':branch,'known_nested_pairs_checked':checked,
                          'negative_pairs':len(bad),'first_20':bad[:20]})
    out={'point_sha256':EXPECTED,'branches':summaries,'elapsed_s':time.monotonic()-start,
         'limits':'Only pairs with both coordinates already present are tested. No missing coordinate or entropic realization is inferred.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
