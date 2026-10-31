#!/usr/bin/env python3
"""Bounded feasibility screen of the exact source-certificate optimal face.

The published exact dual forces all weighted >= and cap rows tight at its
endpoint. This program adds those valid equalities to the full three-branch
Shannon/copy LP and seeks a feasible point. Floating outputs are not proofs.
"""
from array import array
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('sparse',ROOT/'frontier-20261028-sparse-certificate-cutting.py')
sparse=module_from_spec(spec);spec.loader.exec_module(sparse)
cert=sparse.cert;base=sparse.base
CUTS=ROOT/'frontier-20261028-all-order-cut-refinement-result.json'
OUTPUT=ROOT/'frontier-20261028-full-source-optimal-face-result.json'
SYMBOLS=tuple(cert.BASE)+("b'0","d'1","e'1","g'2","f'3","g'3","h'4")
SB={v:1<<i for i,v in enumerate(SYMBOLS)}
BRANCHES=(tuple(cert.BASE)+("b'0",),tuple(cert.BASE)+("d'1","e'1","g'2"),
          tuple(cert.BASE)+("f'3","g'3","h'4"))
SOLVE_SECONDS=75.0


def smask(labels):
    m=0
    for s in labels:m|=SB[s]
    return m


def main():
    started=time.monotonic();data={k:(ROOT/info[0]).read_bytes() for k,info in cert.FILES.items()}
    for k,(_,digest) in cert.FILES.items():cert.pin(k,data[k],digest)
    source=cert.parse_input(data['layout'],data['text']);cutbytes=CUTS.read_bytes();extras=json.loads(cutbytes)['all_added_cuts']
    maps=[];allmasks=set()
    for branch in BRANCHES:
        local=[]
        for mask in range(1<<len(branch)):
            value=0
            for i,name in enumerate(branch):
                if mask&(1<<i):value|=SB[name]
            local.append(value)
            if value:allmasks.add(value)
        maps.append(local)
    masks=sorted(allmasks);col={m:i for i,m in enumerate(masks)}
    starts=array('i');indices=array('i');values=array('d');lower=array('d');upper=array('d')
    category={'source_tight':0,'full_branch_shannon':0,'copy_equality':0,'original_FD':0,'base_symmetry':0,'Fn_cut':0,'objective_fix':0}
    inf=highspy.kHighsInf
    def add(terms,lo,hi,kind):
        acc={}
        for m,c in terms:
            if m:acc[m]=acc.get(m,0)+c
        acc={m:c for m,c in acc.items() if c}
        if not acc:return
        starts.append(len(indices))
        for m,c in acc.items():indices.append(col[m]);values.append(float(c))
        lower.append(float(lo));upper.append(float(hi));category[kind]+=1
    # Tightness of every source inequality/cap is necessary at objective U:
    # their signs and nonzero coefficients were checked in the exact dual.
    for row in source:
        terms=[(smask(names),c) for names,c in row['terms'].items()]
        add(terms,row['rhs'],row['rhs'],'source_tight')
    for branch,local in zip(BRANCHES,maps):
        n=len(branch);full=(1<<n)-1
        for i in range(n):add(((local[full],1),(local[full^(1<<i)],-1)),0,inf,'full_branch_shannon')
        for i,j in combinations(range(n),2):
            rest=full^(1<<i)^(1<<j);z=rest
            while True:
                add(((local[z|(1<<i)],1),(local[z|(1<<j)],1),
                     (local[z|(1<<i)|(1<<j)],-1),(local[z],-1)),0,inf,'full_branch_shannon')
                if z==0:break
                z=(z-1)&rest
    for form in cert.copy_forms():
        if form and form[0][1]>0:
            add(((smask(names),c) for names,c in form),0,0,'copy_equality')
    for v,ns in base.NEIGHBOURS.items():
        n=sum(1<<(u-1) for u in ns);add(((n|(1<<(v-1)),1),(n,-1)),0,0,'original_FD')
    for permutation in base.GENERATORS:
        for m in range(1,1024):
            mapped=base.permute_mask(m,permutation)
            if mapped!=m:add(((m,1),(mapped,-1)),0,0,'base_symmetry')
    for meta in extras:
        row=sparse.fn_row(meta)
        add(((smask(names),c) for names,c in row.items()),0,inf,'Fn_cut')
    add(((1023,1),),1847/276,1847/276,'objective_fix')
    ncols=len(masks);clo=np.zeros(ncols);chi=np.full(ncols,inf)
    for v in cert.BASE:chi[col[SB[v]]]=1.0
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=ncols,len(starts)
    lp.col_cost_=np.zeros(ncols);lp.col_lower_,lp.col_upper_=clo,chi
    lp.row_lower_=np.frombuffer(lower,dtype=np.float64);lp.row_upper_=np.frombuffer(upper,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(values,dtype=np.float64)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',SOLVE_SECONDS);solver.passModel(lp)
    solve_t=time.monotonic();solver.run();elapsed=time.monotonic()-solve_t
    status=solver.modelStatusToString(solver.getModelStatus());info=solver.getInfo();sol=solver.getSolution()
    result={'source_pins':{k:v[1] for k,v in cert.FILES.items()},'added_fn_sha256':sha256(cutbytes).hexdigest(),
            'source_tight_row_count':category['source_tight'],'row_categories':category,
            'columns':ncols,'rows':len(starts),'nnz':len(indices),'solver_threads':1,
            'solver_limit_s':SOLVE_SECONDS,'status_float_unverified':status,'solver_elapsed_s':elapsed,
            'total_elapsed_s':time.monotonic()-started,
            'max_primal_infeasibility_float':float(info.max_primal_infeasibility),
            'limits':'At most a numerical feasibility screen. Infeasibility needs exact Farkas verification; feasibility needs exact rational row-by-row verification. Even an exact LP primal is not an entropic law.'}
    if status=='Optimal':result['primal_values_float']=[[m,float(sol.col_value[i])] for i,m in enumerate(masks)]
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='primal_values_float'},indent=2))


if __name__=='__main__':main()
