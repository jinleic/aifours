#!/usr/bin/env python3
"""Exact all-k source-family scan where exactly one of six blocks has size 2.

Uses disjoint original-variable blocks plus any remaining conditioning subset.
This screens one relaxation point, not an entropic law or a global bound.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import lcm
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-ingleton-sum-double-block-scan-result.json'
SOURCE=ROOT/'frontier-20261028-csirmaz-ingleton-stability-2026-v1.html'
SOURCE_SHA='36e107ae6654e59885f5ed264237134159238df72ca41072fd0d21e97ccba842'
PATTERNS=((2,1,1,1,1,1),(1,1,2,1,1,1),(1,1,1,2,1,1),(1,1,1,1,2,1))


def allocations(sizes):
    def rec(pos,remaining,masks):
        if pos==6:
            yield tuple(masks),remaining;return
        for group in combinations(remaining,sizes[pos]):
            mask=sum(1<<x for x in group)
            if pos==1 and sizes[0]==sizes[1] and masks[0]>=mask:continue
            if pos==5 and sizes[4]==sizes[5] and masks[4]>=mask:continue
            rest=tuple(x for x in remaining if x not in group)
            yield from rec(pos+1,rest,masks+[mask])
    yield from rec(0,tuple(range(10)),[])


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_SHA:raise ValueError('INPUT_HASH')
    values={tuple(x['entropy_variables']):Fraction(x['value']) for x in json.loads(raw)['primal_values']}
    names='abcdefghij';h=[Fraction(0)]+[values[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=[int(x*scale) for x in h]
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    def Ing(x,y,a,b,w):return -I(x,y,w)+I(x,y,a|w)+I(x,y,b|w)+I(a,b,w)
    per=[];found=None
    for pattern in PATTERNS:
        count=0;maxk=1;minimum=None
        for (X,Y,A,B,C,D),remaining in allocations(pattern):
            for wcode in range(1<<len(remaining)):
                W=sum(1<<v for j,v in enumerate(remaining) if wcode&(1<<j));count+=1
                g=I(X,Y,W);a=I(X,A,Y|W)+I(Y,A,X|W)
                S=Ing(X,Y,A,B,W)+Ing(X,Y,C,D,W)+I(X,B,Y|W)+I(Y,B,X|W)
                if g<0 or a<0:raise ValueError('SHANNON_COMPONENT')
                if a==0 and S<0:k=g//(-S)+1
                elif a==0:k=1
                else:k=max(1,-(S//(2*a)))
                maxk=max(maxk,k);value=g+k*S+k*(k-1)*a
                minimum=value if minimum is None else min(minimum,value)
                if value<0:
                    found={'pattern':pattern,'masks':[X,Y,A,B,C,D,W],'k':k,
                           'g_scaled':g,'S_scaled':S,'A_scaled':a,'exact_slack':str(Fraction(value,scale))}
                    break
            if found:break
        per.append({'pattern':pattern,'substitutions_checked':count,'max_candidate_k':maxk,'min_scaled_slack':minimum})
        if found:break
    out={'point_sha256':EXPECTED,'source_sha256':SOURCE_SHA,'scale':scale,'patterns':per,'exact_violation':found,
         'elapsed_s':time.monotonic()-start,
         'limits':'Only disjoint blocks with one double and all other blocks singleton; no general-family, other-point, full-LP or original-bound conclusion.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
