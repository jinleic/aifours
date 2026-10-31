#!/usr/bin/env python3
"""Exact five-variable point check against infinite known inequality families.

Exhausts disjoint block substitutions of F_n and both pinned Csirmaz 2026
families, all positive parameters / finite staircases, for one integer vector.
No literature completeness or original-graph claim is made.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations,product
from math import comb
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=('frontier-20261028-fivevar-family-separator-witness-v3.json','c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842')
PSI=('frontier-20261028-five-variable-nonshannon-witness-v1.json','def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392')
SOURCE=ROOT/'frontier-20261028-csirmaz-2026-five-variable.pdf'
SOURCE_HASH='401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6'
OUT=ROOT/'frontier-20261028-fivevar-family-separator-check-v3-result.json'


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    doc=pin(INPUT);psi=pin(PSI)
    if sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_HASH:raise ValueError('SOURCE_HASH')
    h=doc['values_by_subset_mask'];coeff={int(m):int(c) for m,c in psi['inequality_coefficients_by_mask']}
    if len(h)!=32 or h[0]!=0 or any(not isinstance(x,int) or x<0 for x in h):raise ValueError('VECTOR')
    shannon=0
    for i in range(5):
        if h[31]-h[31^(1<<i)]<0:raise ValueError('MONOTONICITY')
        shannon+=1
    for i,j in combinations(range(5),2):
        a,b=1<<i,1<<j;rest=31^a^b;z=rest
        while True:
            if h[z|a]+h[z|b]-h[z|a|b]-h[z]<0:raise ValueError('SHANNON_CMI')
            shannon+=1
            if not z:break
            z=(z-1)&rest
    target=sum(c*h[m] for m,c in coeff.items())
    if shannon!=85 or target!=-13:raise ValueError(('TARGET',shannon,target))
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    def ing(a,b,c,d,z):return -I(a,b,z)+I(a,b,c|z)+I(a,b,d|z)+I(c,d,z)
    def fmin(a,c,d):
        if a<0 or d<0:raise ValueError('SHANNON_COMPONENT')
        if d==0:
            return None if c<0 else 2*a+2*c
        n=max(1,(-(2*c+d))//(2*d))
        return min(2*a+2*k*c+k*(k+1)*d for k in (n,n+1))
    fcount=0;fminval=None;fail=[]
    for ds in product(range(6),repeat=5):
        A,B,C,D,Z=[sum(1<<i for i,x in enumerate(ds) if x==j) for j in range(1,6)]
        if not (A and B and C and D):continue
        fcount+=1;a=I(A,B,C|Z);delta=I(A,B,Z)-I(A,B,D|Z)-I(C,D,Z)
        d=I(A,C,B|Z)+I(B,C,A|Z);v=fmin(a,a-delta,d)
        if v is None or v<0:fail.append({'family':'F_n','roles':[A,B,C,D,Z],'twice_min':v})
        elif fminval is None or v<fminval:fminval=v
    expected_f=sum((-1)**k*comb(4,k)*(6-k)**5 for k in range(5))
    if fcount!=expected_f:raise ValueError(('F_COUNT',fcount,expected_f))
    scount=0;min1=None;min2=None;negative_inner=0
    for ds in product(range(7),repeat=5):
        A,B,C,D,Z,W=[sum(1<<i for i,x in enumerate(ds) if x==j) for j in range(1,7)]
        if not (A and B and C and D):continue
        scount+=1;g=I(A,B,Z|W);zt=I(A,Z,B|W)+I(B,Z,A|W)
        ct=I(A,C,B|W)+I(B,C,A|W);dt=I(A,D,B|W)+I(B,D,A|W)
        if min(g,ct,dt)<0:raise ValueError('SOURCE_SHANNON_COMPONENT')
        inner=ing(A,B,C,D,W)+zt
        if inner>=0:minimum=g
        else:
            negative_inner+=1
            if ct==0 or dt==0:minimum=None
            else:
                minimum=g;i=0
                while inner+i*ct<0:
                    j=0
                    while inner+i*ct+j*dt<0:
                        minimum+=comb(i+j,i)*(inner+i*ct+j*dt);j+=1
                    i+=1
        if minimum is None or minimum<0:fail.append({'family':'source1','roles':[A,B,C,D,Z,W],'minimum':minimum})
        elif min1 is None or minimum<min1:min1=minimum
        b=ing(A,C,B,D,W)+zt
        if ct==0:
            min_k=None if b<0 else 2*g+2*b
        else:
            k=max(1,(ct-2*b)//(2*ct))
            min_k=min(2*g+2*j*b+j*(j-1)*ct for j in (k,k+1))
        if min_k is None or min_k<0:fail.append({'family':'source2','roles':[A,B,C,D,Z,W],'twice_min':min_k})
        elif min2 is None or min_k<min2:min2=min_k
    expected_s=sum((-1)**k*comb(4,k)*(7-k)**5 for k in range(5))
    if scount!=expected_s:raise ValueError(('SOURCE_COUNT',scount,expected_s))
    out={'point_sha256':INPUT[1],'psi_witness_sha256':PSI[1],'pinned_source_pdf_sha256':SOURCE_HASH,
         'elemental_shannon_checks':shannon,'psi_value':target,
         'F_n_ordered_disjoint_substitutions':fcount,'F_n_all_positive_n_min_twice':fminval,
         'source_ordered_disjoint_substitutions':scount,'source1_finite_staircases_min':min1,
         'source1_negative_inner_cases':negative_inner,'source2_all_positive_k_min_twice':min2,
         'failures':fail,'all_listed_families_hold':not fail,
         'limits':'Only named F_n and pinned 2026 theorem families on pairwise-disjoint 5-variable block/condition substitutions. No overlapping substitutions, full literature novelty, entropic realization or graph improvement is implied.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
