#!/usr/bin/env python3
"""Find projectively coprime multi-minor certificates with seeded pivot shuffles.

Success is certified by a NONZERO explicit 62x62 homogeneous Sylvester
determinant mod 257, not by the number of pivot samples. The first v1 search
could not resolve six cases; this successor preserves it and searches more
31x31 minors by reproducible row/column permutations.
"""
import argparse
import importlib.util
import itertools
import json
from pathlib import Path
import random
import sys


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m


def trial_combination(base,multi,candidates):
    if len(candidates)<2:return None
    anchors=[j for j,x in enumerate(candidates) if x['infinity']]
    if not anchors:return None
    f=candidates[0]['polynomial'];anchor=anchors[0]
    for q in range(base.P):
        weights=[0]*len(candidates);weights[anchor]=1
        for j in range(1,len(candidates)):
            if j!=anchor:weights[j]=pow(q,j,base.P)
        g=[]
        for w,item in zip(weights,candidates):g=base.poly_add(g,[(w*x)%base.P for x in item['polynomial']])
        if base.gcd(f,g)!=[1]:continue
        res=multi.resultant(f,g,base.P,base.D)
        if res:
            return {'status':'CERTIFIED','minors':candidates,'combination_weights':weights,
                    'combination_polynomial':g,'homogeneous_resultant_mod_p':res,'selection_q':q}
    return None


def solve(base,multi,a,b,seed):
    candidates=[];seen=set();rng=random.Random(seed)
    def add_minor(minor,origin):
        if minor is None or minor in seen:return
        seen.add(minor);poly,inf=base.minor_poly(a,b,minor)
        candidates.append({'rows':minor[0],'cols':minor[1],'polynomial':poly,
                           'infinity':inf,'selection':origin})
    for t in [0,*range(1,33),None]:
        add_minor(base.choose_minor(base.mat_at(a,b,t)),{'type':'standard','t':t})
    found=trial_combination(base,multi,candidates)
    if found:return found
    for attempt in range(32):
        t=0 if attempt%2==0 else None
        mat=base.mat_at(a,b,t);rperm=list(range(60));cperm=list(range(36))
        rng.shuffle(rperm);rng.shuffle(cperm)
        selected=base.choose_minor([[mat[r][c] for c in cperm] for r in rperm])
        if selected is not None:
            minor=(tuple(rperm[r] for r in selected[0]),tuple(cperm[c] for c in selected[1]))
            add_minor(minor,{'type':'seeded_shuffle','t':t,'seed':seed,'attempt':attempt})
        found=trial_combination(base,multi,candidates)
        if found:return found
    return {'status':'NO_CERTIFICATE_IN_BOUNDED_PIVOT_SEARCH','minors_found':len(candidates),'seed':seed}


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('dense',type=Path)
    p.add_argument('base',type=Path);p.add_argument('multi',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    dense=load('dense',a.dense);base=load('base',a.base);multi=load('multi',a.multi)
    if base.P!=257 or base.D!=31 or not base.prime(base.P):raise ValueError('unexpected field')
    tensor,sha=dense.load_table(a.table);cases=[]
    for index,free in enumerate(itertools.combinations(range(4),2)):
        rest=tuple(j for j in range(4) if j not in free)
        for orient,(h,k) in enumerate((rest,rest[::-1])):
            a0,a1=base.make_pencil(tensor,free,h,k)
            cases.append({'free_parties':free,'H_party':h,'K_party':k,
                          **solve(base,multi,a0,a1,20261028+index*2+orient)})
    result={'table_sha256':sha,'prime':base.P,'minor_size':base.D,'cases':cases,
            'certified_count':sum(x['status']=='CERTIFIED' for x in cases),'total':len(cases),
            'scope':'Each success gives two integer homogeneous combinations of 31-minors with nonzero resultant mod 257, hence a complex-uniform Koszul-rank >=31.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({'table_sha256':sha,'prime':base.P,'certified_count':result['certified_count'],'total':result['total'],
               'cases':[{'free':x['free_parties'],'H':x['H_party'],'K':x['K_party'],'status':x['status'],
                         'minors':len(x.get('minors',[])),'resultant':x.get('homogeneous_resultant_mod_p')} for x in cases]},sys.stdout,indent=2);print()


if __name__=='__main__':main()
