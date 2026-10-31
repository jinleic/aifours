#!/usr/bin/env python3
"""Exact necessary index screen for 384<=m<432 with conditioned-MI bound."""
from itertools import combinations_with_replacement
from math import factorial,gcd,prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-coset-index-screen432-result.json'


def screen():
    out=[];bounded=0
    for m in range(384,432):
        x=m;nu=0
        while x%2==0:nu+=1;x//=2
        for b in range(9):
            if b and (not nu or 2**nu-1<b):continue
            r=10-b;cut=m**3;base=2**b*3**(r-1)
            choices=[d for d in range(3,m+1) if m%d==0 and (base*d)**2<cut]
            for high in combinations_with_replacement(choices,r):
                p=(2**b*prod(high))**2;small=2 if b else high[0]
                if not p<cut<=small*p:continue
                bounded+=1
                if 2**b*prod(factorial(d) for d in high)%m:continue
                if r==2:
                    common=gcd(*high)
                    if not any(common%s==0 and m%s==0 and (m//s)&((m//s)-1)==0 for s in range(2,common+1)):continue
                out.append({'m':m,'binary_count':b,'nonbinary_indices':list(high)})
    return {'m_range':[384,431],'strict_and_conditioned_product_patterns':bounded,'survivors':out}


def main():
    out=screen();expected=[{'m':384,'binary_count':6,'nonbinary_indices':[3,3,3,4]},
                           {'m':384,'binary_count':7,'nonbinary_indices':[3,3,6]},
                           {'m':384,'binary_count':7,'nonbinary_indices':[3,4,4]}]
    if out['survivors']!=expected:raise ValueError(('SURVIVORS',out['survivors']))
    out['limits']='Exact arithmetic necessary-condition screen; group and entropy exclusion is a separate argument.'
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
