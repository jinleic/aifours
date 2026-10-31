#!/usr/bin/env python3
"""Formal entropy coefficient replay of the syndrome-conditioned identity."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-syndrome-entropy-identity-check-result.json'
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def verify(skip_pair=None,skip_fd=None,syndrome_coefficient=-3):
    bits={(t,v):1<<(3*t+j) for t,tri in enumerate(TRI) for j,v in enumerate(tri)}
    full=(1<<30)-1;S=1<<30;vertex={v:sum(b for (t,w),b in bits.items() if v==w) for v in range(1,11)}
    vec={};fd={}
    def add(d,m,c):
        if m:d[m]=d.get(m,0)+c
    def cmi(d,A,B,Z,c):
        add(d,A|Z,c);add(d,B|Z,c);add(d,A|B|Z,-c);add(d,Z,-c)
    past=0;own={v:0 for v in range(1,11)};counts={'pair_cmis':0,'cross_factor_cmis':0,'conditional_affine_xor_fds':0}
    for t,tri in enumerate(TRI):
        local=sum(bits[t,v] for v in tri)
        for i,j in combinations(tri,2):
            if skip_pair!=(t,i,j):cmi(vec,bits[t,i],bits[t,j],S|past,1)
            counts['pair_cmis']+=1
        for i in tri:
            cmi(vec,bits[t,i],past,S|own[i],2);counts['cross_factor_cmis']+=1
            if skip_fd!=(t,i):add(fd,S|past|local,1);add(fd,S|past|(local^bits[t,i]),-1)
            counts['conditional_affine_xor_fds']+=1
        past|=local
        for i in tri:own[i]|=bits[t,i]
    # Add 3 Delta + 2 sum I(X_i;S) - 3 H(S).
    add(vec,full,3)
    for v in range(1,11):add(vec,vertex[v],-2);cmi(vec,vertex[v],S,0,2)
    add(vec,S,syndrome_coefficient)
    # This equals sum(factor FDs) - 3 H(S|X_V).
    for mask,c in fd.items():add(vec,mask,-c)
    add(vec,full|S,3);add(vec,full,-3)
    if any(vec.values()):raise ValueError('COEFFICIENT_RESIDUAL')
    return {**counts,'component_bits':30,'syndrome_tuple_atoms':1,'entropy_coordinates_checked':len(vec),'coefficient_residual_nonzero':0}


def main():
    checks=verify();controls={}
    for name,kwargs in (('omitted_pair',{'skip_pair':(0,1,2)}),('omitted_factor_fd',{'skip_fd':(0,1)}),('changed_syndrome_coefficient',{'syndrome_coefficient':-4})):
        try:verify(**kwargs)
        except ValueError as exc:
            if str(exc)!='COEFFICIENT_RESIDUAL':raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]='COEFFICIENT_RESIDUAL'
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Formal integer entropy-coefficient identity; fixed-parity FDs and S as syndrome are separate written arguments.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
