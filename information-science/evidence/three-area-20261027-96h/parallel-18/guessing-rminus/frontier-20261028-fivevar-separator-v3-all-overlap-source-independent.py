#!/usr/bin/env python3
"""Independent exact overlap/conditioning replay for both 2026 source families.

For each W contraction, uses C/D outer loops and A/B/Z vectors, plus
first-difference and diagonal-cell minima, unlike the producing scanner.
"""
from hashlib import sha256
from math import comb
from pathlib import Path
from time import monotonic
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fivevar-family-separator-witness-v3.json'
EXPECTED='c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842'
OUTPUT=ROOT/'frontier-20261028-fivevar-separator-v3-all-overlap-source-independent-result.json'


def min_ideal(g,v,c,d):
    if v>=0:return g,0
    if c==0 or d==0:return None,None
    end=(-v-1)//min(c,d);total=g;cells=0
    for diag in range(end+1):
        for i in range(diag+1):
            j=diag-i;x=v+i*c+j*d
            if x<0:total+=comb(diag,i)*x;cells+=1
    return total,cells


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    h=json.loads(raw)['values_by_subset_mask']
    if len(h)!=32 or h[0]!=0:raise ValueError('VECTOR')
    count1=count2=negative=0;min1=min2=None;maxk=1;cache={};violation=None
    for W in range(32):
        av=[i for i in range(5) if not W&(1<<i)];n=len(av);q=1<<n
        def expand(m):return sum(1<<av[i] for i in range(n) if m&(1<<i))
        H=np.array([h[W|expand(m)]-h[W] for m in range(q)],dtype=np.int64)
        A=np.repeat(np.arange(q,dtype=np.int64),q*q);B=np.tile(np.repeat(np.arange(q,dtype=np.int64),q),q);Z=np.tile(np.arange(q,dtype=np.int64),q*q)
        def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
        for C in range(q):
            for D in range(q):
                g=I(A,B,Z);zt=I(A,Z,B)+I(B,Z,A);ct=I(A,C,B)+I(B,C,A)
                inner2=-I(A,C,0)+I(A,C,B)+I(A,C,D)+I(B,D,0)+zt
                if np.any(g<0) or np.any(ct<0):raise ValueError('SHANNON_COMPONENT')
                bad=(ct==0)&(inner2<0);count2+=len(Z)
                if np.any(bad):
                    j=int(np.flatnonzero(bad)[0]);k=int(g[j]//(-inner2[j])+1)
                    violation={'family':'source2','W':W,'roles':[expand(int(A[j])),expand(int(B[j])),expand(C),expand(D),expand(int(Z[j]))],
                               'k':k,'twice_slack':int(2*g[j]+2*k*inner2[j])};break
                k=np.ones(len(Z),dtype=np.int64);nz=ct>0;k[nz]=np.maximum(1,-np.floor_divide(inner2[nz],ct[nz]));maxk=max(maxk,int((k+1).max()))
                bound=int(max(np.max(np.abs(g)),np.max(np.abs(inner2)),np.max(np.abs(ct)),1))
                if 2*bound*(maxk+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
                q1=2*g+2*k*inner2+k*(k-1)*ct;q2=2*g+2*(k+1)*inner2+(k+1)*k*ct
                local=int(min(q1.min(),q2.min()));min2=local if min2 is None else min(min2,local)
                if local<0:
                    j=int(np.flatnonzero((q1<0)|(q2<0))[0]);kk=int(k[j] if q1[j]<0 else k[j]+1)
                    violation={'family':'source2','W':W,'roles':[expand(int(A[j])),expand(int(B[j])),expand(C),expand(D),expand(int(Z[j]))],
                               'k':kk,'twice_slack':int(2*g[j]+2*kk*inner2[j]+kk*(kk-1)*ct[j])};break
                good=A<=B;count1+=int(good.sum())
                dt=I(A,D,B)+I(B,D,A);inner1=-I(A,B,0)+I(A,B,C)+I(A,B,D)+I(C,D,0)+zt
                if np.any(dt<0):raise ValueError('SHANNON_D')
                neg=good&(inner1<0);negative+=int(neg.sum())
                if np.any(neg):
                    profiles=np.unique(np.stack((g[neg],inner1[neg],ct[neg],dt[neg]),axis=1),axis=0)
                    for row in profiles:
                        key=tuple(int(x) for x in row)
                        if key not in cache:cache[key]=min_ideal(*key)
                        m,cells=cache[key]
                        if m is None or m<0:
                            ids=np.flatnonzero(neg&(g==key[0])&(inner1==key[1])&(ct==key[2])&(dt==key[3]));j=int(ids[0])
                            violation={'family':'source1','W':W,'roles':[expand(int(A[j])),expand(int(B[j])),expand(C),expand(D),expand(int(Z[j]))],
                                       'g_inner_c_d':key,'minimum':m,'negative_cells':cells};break
                        min1=m if min1 is None else min(min1,m)
                if violation:break
            if violation:break
        if violation:break
    expected2=33**5;expected1=sum(comb(5,w)*((1<<(5-w))*((1<<(5-w))+1)//2)*(1<<(3*(5-w))) for w in range(6))
    if not violation and (count1,count2)!=(expected1,expected2):raise ValueError(('COUNT',count1,count2,expected1,expected2))
    out={'point_sha256':EXPECTED,'scope':'all overlapping A,B,C,D,Z,W substitutions after conditioning contraction, including effective-empty roles; source1 A/B quotient, source2 ordered',
         'enumeration':'W contraction, C/D outer and A/B/Z vectorized',
         'source1_checked':count1,'source1_expected':expected1,'source1_negative_inner_cases':negative,
         'source1_unique_negative_profiles':len(cache),'source1_min_negative_ideal_value':min1,
         'source2_checked':count2,'source2_expected':expected2,'source2_min_twice_slack':min2,
         'source2_max_first_difference_neighbor_k':maxk,'all_parameters':'all finite staircases / all positive integers by exact minima',
         'first_violation':violation,'elapsed_seconds':monotonic()-start,
         'limits':'Only the two named 2026 source families on one rational polymatroid. No other inequality, entropy realization or literature-completeness conclusion.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
