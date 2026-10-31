#!/usr/bin/env python3
"""Formal entropy-coefficient check of the per-factor causal syndrome identity."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-causal-syndrome-identity-check-result.json'
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def verify(skip_pair=None,skip_parity_fd=None):
    bits={(t,v):1<<(3*t+j) for t,T in enumerate(TRI) for j,v in enumerate(T)}
    syn=[1<<(30+t) for t in range(10)];full=(1<<30)-1
    vertex={v:sum(x for (t,w),x in bits.items() if v==w) for v in range(1,11)}
    vec={};fd={};past=0;own={v:0 for v in range(1,11)};count={'syndrome_conditions':0,'bit_syndrome_cmis':0,'pair_cmis':0,'cross_factor_cmis':0,'xor_fd_rows':0}
    def add(d,m,c):
        if m:d[m]=d.get(m,0)+c
    def cond(d,A,Z,c):add(d,A|Z,c);add(d,Z,-c)
    def cmi(d,A,B,Z,c):add(d,A|Z,c);add(d,B|Z,c);add(d,A|B|Z,-c);add(d,Z,-c)
    for t,T in enumerate(TRI):
        z=sum(bits[t,v] for v in T);st=syn[t];cond(vec,st,past,3);count['syndrome_conditions']+=1
        for i in T:
            cmi(vec,bits[t,i],st,past,-2);count['bit_syndrome_cmis']+=1
            cmi(vec,bits[t,i],past,own[i],-2);count['cross_factor_cmis']+=1
            # Subtract the formal residual: -3 H(S_t|Z_t,past) + sum H(bit|other bits,S_t,past).
            cond(fd,bits[t,i],st|past|(z^bits[t,i]),-1);count['xor_fd_rows']+=1
        for i,j in combinations(T,2):
            if skip_pair!=(t,i,j):cmi(vec,bits[t,i],bits[t,j],st|past,-1)
            count['pair_cmis']+=1
        if skip_parity_fd!=t:cond(fd,st,z|past,3)
        past|=z
        for i in T:own[i]|=bits[t,i]
    # RHS (22) minus 3 Delta equals 3 syndrome FDs minus factor-bit FDs.
    add(vec,full,-3)
    for v in range(1,11):add(vec,vertex[v],2)
    for mask,c in fd.items():add(vec,mask,-c)
    if any(vec.values()):raise ValueError('COEFFICIENT_RESIDUAL')
    return {**count,'component_bits':30,'syndrome_bits':10,'entropy_coordinates_checked':len(vec),'coefficient_residual_nonzero':0}


def main():
    checks=verify();controls={}
    for name,kwargs in (('omitted_pair_cmi',{'skip_pair':(0,1,2)}),('omitted_syndrome_fd',{'skip_parity_fd':0})):
        try:verify(**kwargs)
        except ValueError as exc:
            if str(exc)!='COEFFICIENT_RESIDUAL':raise ValueError(('WRONG_REASON',str(exc)))
            controls[name]='COEFFICIENT_RESIDUAL'
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Formal entropy-coefficient identity only; XOR determinism and entropy nonnegativity are written deductions.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
