#!/usr/bin/env python3
"""Find projectively coprime combinations of 31x31 Koszul pencil minors.

The first exploratory script tested only pairs of individual minors. Here one
homogeneous linear combination of several independently selected minors is
allowed: every minor still vanishes whenever the pencil rank is below 31.
The 62x62 homogeneous Sylvester determinant is computed modulo 257 explicitly.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import sys


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def resultant(f,g,p,degree):
    f=(f+[0]*(degree+1-len(f)))[:degree+1]
    g=(g+[0]*(degree+1-len(g)))[:degree+1]
    matrix=[]
    for poly in (list(reversed(f)),list(reversed(g))):
        for shift in range(degree):
            row=[0]*(2*degree)
            row[shift:shift+degree+1]=poly
            matrix.append(row)
    det=1;n=2*degree
    for j in range(n):
        pivot=next((i for i in range(j,n) if matrix[i][j]%p),None)
        if pivot is None:return 0
        if pivot!=j:matrix[j],matrix[pivot]=matrix[pivot],matrix[j];det=-det
        val=matrix[j][j]%p;det=det*val%p;inv=pow(val,-1,p)
        for i in range(j+1,n):
            scale=matrix[i][j]*inv%p
            if scale:
                for k in range(j+1,n):matrix[i][k]=(matrix[i][k]-scale*matrix[j][k])%p
    return det%p


def solve(base,a,b):
    candidates=[];seen=set()
    # 0 and infinity anchor independent projective endpoints; extra samples are
    # used only to choose row/column minors, never as a proof by sampling.
    for t in [0,*range(1,33),None]:
        minor=base.choose_minor(base.mat_at(a,b,t))
        if minor is None or minor in seen:continue
        seen.add(minor);polynomial,inf=base.minor_poly(a,b,minor)
        candidates.append({'rows':minor[0],'cols':minor[1],'polynomial':polynomial,
                           'infinity':inf,'selected_at':t})
    inf_indices=[j for j,x in enumerate(candidates) if x['infinity']]
    if not candidates or not inf_indices:
        return {'status':'NO_INFINITY_MINOR','minors_found':len(candidates)}
    f=candidates[0]['polynomial'];anchor=inf_indices[0]
    for q in range(base.P):
        weights=[0]*len(candidates);weights[anchor]=1
        for j in range(1,len(candidates)):
            if j!=anchor:weights[j]=pow(q,j,base.P)
        g=[]
        for weight,item in zip(weights,candidates):
            g=base.poly_add(g,[(weight*x)%base.P for x in item['polynomial']])
        if base.gcd(f,g)!=[1]:continue
        res=resultant(f,g,base.P,base.D)
        if not res:continue
        return {'status':'CERTIFIED','minors':candidates,'combination_weights':weights,
                'combination_polynomial':g,'gcd_mod_p':[1],
                'homogeneous_resultant_mod_p':res,'selection_q':q}
    return {'status':'NO_CERTIFICATE_IN_BOUNDED_COMBINATIONS','minors_found':len(candidates)}


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('dense',type=Path)
    p.add_argument('base',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    dense=load('dense',a.dense);base=load('mixed',a.base)
    tensor,sha=dense.load_table(a.table)
    results=[]
    for free in itertools.combinations(range(4),2):
        rest=tuple(j for j in range(4) if j not in free)
        for h,k in (rest,rest[::-1]):
            m0,m1=base.make_pencil(tensor,free,h,k)
            results.append({'free_parties':free,'H_party':h,'K_party':k,**solve(base,m0,m1)})
    result={'table_sha256':sha,'field':base.P,'minor_size':base.D,
            'certified_count':sum(x['status']=='CERTIFIED' for x in results),'total':len(results),
            'cases':results,
            'scope':'If certified, 31x31 minors have no common complex projective root via nonzero integer homogeneous resultant; this bounds each mixed-sector 3-tensor rank below.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({'table_sha256':sha,'field':base.P,'minor_size':base.D,'certified_count':result['certified_count'],
               'total':result['total'],'cases':[{'free':r['free_parties'],'H':r['H_party'],'K':r['K_party'],
               'status':r['status'],'resultant_mod_p':r.get('homogeneous_resultant_mod_p')} for r in results]},sys.stdout,indent=2);print()


if __name__=='__main__':main()
