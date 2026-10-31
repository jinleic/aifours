#!/usr/bin/env python3
"""Exact disjoint-block scan of Csirmaz & Csirmaz (2026) theorem 1.

Enumerates every downward-closed S in D_n for n<=5, and every disjoint original
A,B,C,D,Z substitution modulo A/B swap. The LP point need not be entropic.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
SOURCE=ROOT/'frontier-20261028-csirmaz-2026-five-variable.pdf'
SOURCE_SHA='401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6'
OUTPUT=ROOT/'frontier-20261028-staircase-family-scan-result.json'
MAX_N=5


def staircases(n):
    def rec(i,prev,widths):
        if i==n:
            yield tuple(widths);return
        for w in range(min(prev,n-i)+1):
            yield from rec(i+1,w,widths+[w])
    for widths in rec(0,n,[]):
        cells=[(i,j) for i,w in enumerate(widths) for j in range(w)]
        alpha=sum(comb(i+j,i) for i,j in cells)
        beta=sum(i*comb(i+j,i) for i,j in cells)
        gamma=sum(j*comb(i+j,i) for i,j in cells)
        yield (alpha,beta,gamma),cells


def main():
    started=time.monotonic();raw=INPUT.read_bytes();pdf=SOURCE.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED or sha256(pdf).hexdigest()!=SOURCE_SHA:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];vals={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    B='abcdefghij';h=[Fraction(0)]+[vals[tuple(B[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('SCALE_RANGE')
    by_triple={};raw_count=0
    for triple,cells in staircases(MAX_N):
        raw_count+=1;by_triple.setdefault(triple,cells)
    if raw_count!=132:raise ValueError(('STAIRCASE_COUNT',raw_count))
    triples=sorted(by_triple)
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    nlow=6**7;codes=np.arange(nlow,dtype=np.int64)
    low=[np.zeros(nlow,dtype=np.int64) for _ in range(5)];t=codes.copy()
    for i in range(7):
        digit=t%6;t//=6
        for j in range(5):low[j]|=np.where(digit==j+1,1<<i,0)
    count=0;nontrivial=0;found=None;min_slack=0
    for code in range(6**3):
        t=code;high=[0]*5
        for i in range(7,10):
            digit=t%6;t//=6
            if digit:high[digit-1]|=1<<i
        groups=[low[j]|high[j] for j in range(5)]
        valid=(groups[0]>0)&(groups[1]>0)&(groups[2]>0)&(groups[3]>0)&(groups[0]<groups[1])
        A,Bv,C,D,Z=(x[valid] for x in groups);count+=len(A)
        if not len(A):continue
        g=I(A,Bv,Z)
        v=-I(A,Bv,0)+I(A,Bv,C)+I(A,Bv,D)+I(C,D,0)+I(A,Z,Bv)+I(Bv,Z,A)
        c=I(A,C,Bv)+I(Bv,C,A);d=I(A,D,Bv)+I(Bv,D,A)
        if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('SHANNON_COMPONENT')
        active=np.flatnonzero(v<0);nontrivial+=len(active)
        if not len(active):continue
        for alpha,beta,gamma in triples:
            slack=g[active]+alpha*v[active]+beta*c[active]+gamma*d[active]
            if len(slack):min_slack=min(min_slack,int(slack.min()))
            bad=np.flatnonzero(slack<0)
            if len(bad):
                j=int(active[int(bad[0])])
                found={'masks':[int(x[j]) for x in (A,Bv,C,D,Z)],'triplet':[alpha,beta,gamma],
                       'downward_closed_cells':by_triple[(alpha,beta,gamma)],
                       'g_scaled':int(g[j]),'v_scaled':int(v[j]),'C_scaled':int(c[j]),'D_scaled':int(d[j]),
                       'exact_slack':str(Fraction(int(g[j]+alpha*v[j]+beta*c[j]+gamma*d[j]),scale))}
                break
        if found:break
    out={'point_sha256':EXPECTED,'source_sha256':SOURCE_SHA,'scale':scale,
         'max_staircase_generation':MAX_N,'downward_closed_sets':raw_count,
         'distinct_parameter_triples':len(triples),'triples':[list(x) for x in triples],
         'substitutions_checked_before_stop':count,'substitutions_with_negative_ingleton_plus_Z':nontrivial,
         'min_scaled_slack':min_slack,'witness':found,'elapsed_s':time.monotonic()-started,
         'limits':'Exact finite-generation/disjoint-block scan of one LP point; untested later generations and overlapping substitutions remain open. Source theorem validity is an external import requiring proof review.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
