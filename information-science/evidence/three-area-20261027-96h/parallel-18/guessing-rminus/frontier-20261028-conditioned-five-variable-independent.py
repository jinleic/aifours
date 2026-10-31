#!/usr/bin/env python3
"""Independent exact conditional 2026 family scan of one rational base point.

Uses a different seven-ary split and quadratic-vertex check; no producer code is
imported. Checks all disjoint A,B,C,D,Z,W and all finite family parameters.
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
OUTPUT=ROOT/'frontier-20261028-conditioned-five-variable-independent-result.json'


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values'];values={tuple(x['entropy_variables']):Fraction(x['value']) for x in items}
    names='abcdefghij';h=[Fraction(0)]+[values[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(v.denominator for v in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    if max(abs(int(x)) for x in H)>=10**8:raise ValueError('INTEGER_RANGE')
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    count_low=7**6;codes=np.arange(count_low,dtype=np.int64);low=[np.zeros(count_low,dtype=np.int64) for _ in range(6)]
    t=codes.copy()
    for i in range(6):
        digit=t%7;t//=7
        for role in range(6):low[role]|=np.where(digit==role+1,1<<i,0)
    total=0;negative=0;negative_profiles=set();second_bad=0;min2=None;max_k=1
    for code in range(7**4):
        t=code;high=[0]*6
        for i in range(6,10):
            digit=t%7;t//=7
            if digit:high[digit-1]|=1<<i
        groups=[low[j]|high[j] for j in range(6)]
        ok=(groups[0]>0)&(groups[1]>0)&(groups[2]>0)&(groups[3]>0)&(groups[0]<groups[1])
        A,B,C,D,Z,W=(v[ok] for v in groups);total+=len(A)
        if not len(A):continue
        g=I(A,B,Z|W)
        zterm=I(A,Z,B|W)+I(B,Z,A|W)
        c=I(A,C,B|W)+I(B,C,A|W);d=I(A,D,B|W)+I(B,D,A|W)
        v=-I(A,B,W)+I(A,B,C|W)+I(A,B,D|W)+I(C,D,W)+zterm
        if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('NEGATIVE_CMI')
        positions=np.flatnonzero(v<0);negative+=len(positions)
        negative_profiles.update((int(g[j]),int(v[j]),int(c[j]),int(d[j])) for j in positions)
        for X,Y in ((A,B),(B,A)):
            s=-I(X,C,W)+I(X,C,Y|W)+I(X,C,D|W)+I(Y,D,W)+I(X,Z,Y|W)+I(Y,Z,X|W)
            Cterm=I(X,C,Y|W)+I(Y,C,X|W)
            if np.any((Cterm==0)&(s<0)):raise ValueError('FAMILY2_NEGATIVE_LINEAR_SLOPE')
            nz=Cterm>0;k=np.ones(len(X),dtype=np.int64)
            k[nz]=np.maximum(1,np.floor_divide(Cterm[nz]-2*s[nz],2*Cterm[nz]))
            k2=k+1;max_k=max(max_k,int(k2.max()))
            bound=int(max(np.max(np.abs(g)),np.max(np.abs(s)),np.max(np.abs(Cterm)),1))
            if 2*bound*(max_k+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
            q1=2*g+2*k*s+k*(k-1)*Cterm
            q2=2*g+2*k2*s+k2*(k2-1)*Cterm
            least=np.minimum(q1,q2);second_bad+=int(np.count_nonzero(least<0))
            local=int(least.min());min2=local if min2 is None else min(min2,local)
    expected=(7**10-4*6**10+6*5**10-4*4**10+3**10)//2
    if total!=expected:raise ValueError(('ENUMERATION_COUNT',total,expected))
    min_first=None;num_profiles=0
    for g,v,c,d in negative_profiles:
        if c<=0 or d<=0:raise ValueError(('FAMILY1_UNBOUNDED_NEGATIVE',g,v,c,d))
        # Sum all negative lattice-cell contributions. Their set is a finite
        # downward-closed order ideal; including any nonnegative cell cannot
        # improve the value, so this is the exact minimum over all finite S.
        value=g;cells=0
        for i in range((-v-1)//c+1):
            for j in range((-v-1-i*c)//d+1):
                value+=comb(i+j,i)*(v+i*c+j*d);cells+=1
        if value<0:raise ValueError(('FAMILY1_VIOLATION',g,v,c,d,value))
        min_first=value if min_first is None else min(min_first,value);num_profiles+=1
    if second_bad:raise ValueError(('FAMILY2_VIOLATIONS',second_bad))
    out={'point_sha256':EXPECTED,'scale':scale,'disjoint_substitutions_mod_AB_swap':total,
         'family1_negative_inner_assignments':negative,'family1_distinct_negative_profiles':num_profiles,
         'family1_minimum_over_all_finite_staircases_scaled':min_first,
         'family2_both_AB_orders_all_positive_k_pass':True,'family2_min_twice_scaled':min2,
         'family2_max_tested_adjacent_k':max_k,'elapsed_s':time.monotonic()-start,
         'limits':'One rational partial-source relaxation base profile; full source-copy extension and entropic feasibility unestablished. Source theorem proof not independently reviewed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
