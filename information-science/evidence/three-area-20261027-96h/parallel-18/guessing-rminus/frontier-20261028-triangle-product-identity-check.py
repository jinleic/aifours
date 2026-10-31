#!/usr/bin/env python3
"""Symbolically check the ten-triangle product-support entropy identity."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-triangle-product-identity-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def verify(skip_pair=None,skip_fd=None,edges=None,target_joint=-3):
    edges=edges if edges is not None else {tuple(sorted((v,w))) for v in N for w in N[v]}
    if any(tuple(sorted((u,v))) not in edges for tri in TRI for u,v in combinations(tri,2)):raise ValueError('GRAPH_TRIANGLE')
    if any(sum(v in tri for tri in TRI)!=3 for v in range(1,11)):raise ValueError('INCIDENCE')
    bits={(t,v):1<<(3*t+j) for t,tri in enumerate(TRI) for j,v in enumerate(tri)}
    allbits=(1<<30)-1;vertex={v:sum(b for (t,w),b in bits.items() if w==v) for v in range(1,11)}
    def add(vec,m,c):
        if m:vec[m]=vec.get(m,0)+c
    def cmi(vec,A,B,Z,coef):
        add(vec,A|Z,coef);add(vec,B|Z,coef);add(vec,A|B|Z,-coef);add(vec,Z,-coef)
    rhs={};fd={};past=0;ownpast={v:0 for v in range(1,11)};pairs=couplings=fds=0
    for t,tri in enumerate(TRI):
        full=sum(bits[t,v] for v in tri)
        for i,j in combinations(tri,2):
            if skip_pair!=(t,i,j):cmi(rhs,bits[t,i],bits[t,j],past,1)
            pairs+=1
        for i in tri:
            cmi(rhs,bits[t,i],past,ownpast[i],2);couplings+=1
            if skip_fd!=(t,i):
                other=full^bits[t,i];add(fd,past|full,1);add(fd,past|other,-1)
            fds+=1
        past|=full
        for i in tri:ownpast[i]|=bits[t,i]
    # RHS - target must equal the 30 zero factor-FD rows.
    for v in range(1,11):add(rhs,vertex[v],-2)
    add(rhs,allbits,-target_joint)
    for mask,c in fd.items():add(rhs,mask,-c)
    residual={k:v for k,v in rhs.items() if v}
    if residual:raise ValueError('COEFFICIENT_RESIDUAL')
    return {'component_bits':len(bits),'triangles':len(TRI),'pair_cmis':pairs,'cross_factor_cmis':couplings,
            'conditional_xor_fd_rows':fds,'symbolic_entropy_coordinates_checked':len(rhs),'coefficient_residual_nonzero':0}


def main():
    checks=verify();controls={}
    for name,kwargs,reason in (
        ('omitted_pair_cmi',{'skip_pair':(0,1,2)},'COEFFICIENT_RESIDUAL'),
        ('omitted_xor_fd',{'skip_fd':(0,1)},'COEFFICIENT_RESIDUAL'),
        ('changed_joint_coefficient',{'target_joint':-4},'COEFFICIENT_RESIDUAL'),
        ('missing_graph_edge',{'edges':{tuple(sorted((v,w))) for v in N for w in N[v]}-{(1,2)}},'GRAPH_TRIANGLE')):
        try:verify(**kwargs)
        except ValueError as exc:
            if str(exc)!=reason:raise ValueError(('WRONG_REASON',name,str(exc)))
            controls[name]=reason
        else:raise ValueError(('MUTATION_ACCEPTED',name))
    out={'exact_checks':checks,'all_checked':True,'mutation_controls':controls,
         'limits':'Formal integer coefficient identity plus graph/triangle incidence. Entropy nonnegativity and XOR decoding are written arguments, not a proof-assistant proof.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
