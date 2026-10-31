#!/usr/bin/env python3
"""Independent exact subset-enumeration replay for a five-variable separator.

Enumerates disjoint masks rather than digit assignments and uses first
differences / diagonal negative-cell sums for infinite families.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from math import comb
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=('frontier-20261028-fivevar-family-separator-witness-v3.json','c9ed697b7bf768af0e29ae96387e16963ca810e851cde16c63850b9237552842')
PSI=('frontier-20261028-five-variable-nonshannon-witness-v1.json','def19d886c86451744a8928a050c779658a6f0228afeccd83487a2b26d2d0392')
SOURCE=ROOT/'frontier-20261028-csirmaz-2026-five-variable.pdf'
SOURCE_HASH='401bd7d8bbec7fae5b355509ae8659a9fa43671051606d3ad220c639b5e2d6b6'
OUT=ROOT/'frontier-20261028-fivevar-family-separator-v3-independent-result.json'
FULL=31


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def subsets(mask,include_empty=True):
    x=mask
    while x:
        yield x;x=(x-1)&mask
    if include_empty:yield 0


def verify(h,coeff):
    if len(h)!=32 or h[0]!=0 or any(not isinstance(v,int) or v<0 for v in h):raise ValueError('VECTOR')
    def I(a,b,z):return h[a|z]+h[b|z]-h[a|b|z]-h[z]
    def ing(a,b,c,d,z):return -I(a,b,z)+I(a,b,c|z)+I(a,b,d|z)+I(c,d,z)
    count=0
    for i in range(5):
        if h[FULL]<h[FULL^(1<<i)]:raise ValueError('MONOTONICITY')
        count+=1
    for i,j in combinations(range(5),2):
        for z in subsets(FULL^(1<<i)^(1<<j)):
            if I(1<<i,1<<j,z)<0:raise ValueError('SHANNON')
            count+=1
    target=sum(c*h[m] for m,c in coeff.items())
    if target!=-13:raise ValueError(('PSI',target))
    return count,I,ing


def main():
    doc=pin(INPUT);psi=pin(PSI)
    if sha256(SOURCE.read_bytes()).hexdigest()!=SOURCE_HASH:raise ValueError('SOURCE_HASH')
    h=doc['values_by_subset_mask'];coeff={int(m):int(c) for m,c in psi['inequality_coefficients_by_mask']}
    count,I,ing=verify(h,coeff)
    Fcount=Scount=0;Fmin=S1min=S2min=None;innerneg=0;bad=[];maxdiag=0
    for A in subsets(FULL,False):
        for B in subsets(FULL^A,False):
            for C in subsets(FULL^A^B,False):
                for D in subsets(FULL^A^B^C,False):
                    remaining=FULL^A^B^C^D
                    for Z in subsets(remaining):
                        Fcount+=1;a=I(A,B,C|Z);delta=I(A,B,Z)-I(A,B,D|Z)-I(C,D,Z)
                        d=I(A,C,B|Z)+I(B,C,A|Z);c=a-delta
                        if min(a,d)<0:raise ValueError('FN_COMPONENT')
                        if d==0 and c<0:bad.append(('Fn_unbounded',A,B,C,D,Z));continue
                        if d==0:n0=1
                        else:n0=max(1,-((- (delta-a))//d)-1)
                        v=min(2*a+2*n*c+n*(n+1)*d for n in (n0,n0+1))
                        if v<0:bad.append(('Fn',A,B,C,D,Z,v))
                        Fmin=v if Fmin is None else min(Fmin,v)
                    for Z in subsets(remaining):
                        for W in subsets(remaining^Z):
                            Scount+=1;g=I(A,B,Z|W);zt=I(A,Z,B|W)+I(B,Z,A|W)
                            ct=I(A,C,B|W)+I(B,C,A|W);dt=I(A,D,B|W)+I(B,D,A|W)
                            if min(g,ct,dt)<0:raise ValueError('SOURCE_COMPONENT')
                            v=ing(A,B,C,D,W)+zt
                            if v>=0:s1=g
                            elif ct==0 or dt==0:s1=None
                            else:
                                innerneg+=1;s1=g;maxk=(-v-1)//min(ct,dt);maxdiag=max(maxdiag,maxk)
                                for diag in range(maxk+1):
                                    for i in range(diag+1):
                                        j=diag-i;term=v+i*ct+j*dt
                                        if term<0:s1+=comb(diag,i)*term
                            if s1 is None or s1<0:bad.append(('source1',A,B,C,D,Z,W,s1))
                            elif S1min is None or s1<S1min:S1min=s1
                            b=ing(A,C,B,D,W)+zt
                            if ct==0 and b<0:s2=None
                            elif ct==0:s2=2*g+2*b
                            else:
                                k0=max(1,-(b//ct))
                                s2=min(2*g+2*k*b+k*(k-1)*ct for k in (k0,k0+1))
                            if s2 is None or s2<0:bad.append(('source2',A,B,C,D,Z,W,s2))
                            elif S2min is None or s2<S2min:S2min=s2
    expected_f=sum((-1)**k*comb(4,k)*(6-k)**5 for k in range(5))
    expected_s=sum((-1)**k*comb(4,k)*(7-k)**5 for k in range(5))
    if Fcount!=expected_f or Scount!=expected_s:raise ValueError(('COUNT',Fcount,Scount,expected_f,expected_s))
    controls={}
    for tag,mut in (('nonzero_empty',lambda x:x.__setitem__(0,1)),
                    ('altered_target_coordinate',lambda x:x.__setitem__(1,x[1]+1))):
        changed=list(h);mut(changed)
        try:verify(changed,coeff)
        except ValueError:controls[tag]='rejected'
        else:raise ValueError(('CONTROL_ACCEPTED',tag))
    out={'point_sha256':INPUT[1],'psi_witness_sha256':PSI[1],'source_pdf_sha256':SOURCE_HASH,
         'elemental_shannon_checks':count,'psi_value':-13,'F_n_ordered_disjoint_substitutions':Fcount,
         'F_n_all_positive_n_min_twice':Fmin,'source_ordered_disjoint_substitutions':Scount,
         'source1_finite_staircases_min':S1min,'source1_negative_inner_cases':innerneg,
         'source2_all_positive_k_min_twice':S2min,'max_negative_cell_diagonal':maxdiag,
         'violations':bad,'mutation_controls':controls,
         'limits':'Exact algebraic separation from the named infinite families under disjoint block/conditioning substitutions only; no overlapping substitutions, entropy realization or novelty clearance.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
