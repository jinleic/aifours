#!/usr/bin/env python3
"""Search for improvements using valid inequalities involving source copies.

All 17 variables are jointly realizable via conditional copying. This is a
bounded, single-thread floating LP; any resulting bound requires an independent
exact dual certificate. No solver result is asserted as a proof.
"""
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
import time

import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def load(name,path):
    spec=spec_from_file_location(name,ROOT/path); obj=module_from_spec(spec); spec.loader.exec_module(obj); return obj

sparse=load('sparse','frontier-20261028-sparse-certificate-cutting.py')
cert=sparse.cert; base=sparse.base
OUTPUT=ROOT/'frontier-20261028-cross-copy-upper-search-result.json'
SYMBOLS=tuple(cert.BASE)+("b'0","d'1","e'1","g'2","f'3","g'3","h'4")
BITS={v:1<<i for i,v in enumerate(SYMBOLS)}
N=len(SYMBOLS)
MAX_ROUNDS=4
SOLVE_SECONDS=35.0
CUTS_PER_ROUND=750


def mask_for(labels):
    result=0
    for name in labels:result|=BITS[name]
    return result


def compressed(terms):
    result={}
    for mask,value in terms:
        if mask:result[mask]=result.get(mask,0)+value
    return tuple(sorted((m,v) for m,v in result.items() if v))


def add_to(rows,terms,low,high,meta):
    key=compressed(terms)
    if key:
        rows.setdefault((key,low,high),meta)


def create_rows(source):
    inf=highspy.kHighsInf; rows={}
    for terms,low,high,meta in sparse.build_constraints(source,[]):
        add_to(rows,[(mask_for(labels),value) for labels,value in terms.items()],low,high,meta)
    # Complete explicitly defined copy equalities (orientation irrelevant).
    for key in cert.copy_forms():
        if key and key[0][1] < 0:continue
        add_to(rows,[(mask_for(labels),value) for labels,value in key],0,0,{'kind':'full-copy-equality'})
    # Entropy monotonicity for all subsets of size <=5 on the common joint law.
    for size in range(1,6):
        for subset in combinations(range(N),size):
            mask=sum(1<<i for i in subset)
            for i in subset:
                add_to(rows,[(mask,1),(mask^(1<<i),-1)],0,inf,
                       {'kind':'low-order-conditional-entropy','i':i})
    # Elemental CMIs I(i;j | Z) for |Z|<=3, across all branches as well.
    for i,j in combinations(range(N),2):
        others=[v for v in range(N) if v not in (i,j)]
        for zsize in range(4):
            for cond in combinations(others,zsize):
                z=sum(1<<v for v in cond)
                add_to(rows,base.cmi(1<<i,1<<j,z),0,inf,
                       {'kind':'low-order-CMI','i':i,'j':j,'z':z})
    return rows


def solve(rows):
    inf=highspy.kHighsInf
    masks={mask for (key,_,_) in rows for mask,_ in key}
    masks.update(range(1,1<<10))
    for size in range(1,6):
        masks.update(sum(1<<i for i in subset) for subset in combinations(range(N),size))
    masks=sorted(masks); col={mask:i for i,mask in enumerate(masks)}
    starts=[]; indices=[]; values=[]; lows=[]; highs=[]; labels=[]
    for (key,lo,hi),meta in rows.items():
        starts.append(len(indices))
        for mask,value in key:indices.append(col[mask]);values.append(float(value))
        lows.append(lo);highs.append(hi);labels.append((key,meta))
    cols=len(masks); lower=np.zeros(cols); upper=np.full(cols,inf)
    for i in range(10):upper[col[1<<i]]=1
    cost=np.zeros(cols);cost[col[(1<<10)-1]]=1
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=cols,len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=cost,lower,upper
    lp.row_lower_,lp.row_upper_=np.array(lows),np.array(highs)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(indices)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(indices,dtype=np.int32)
    lp.a_matrix_.value_=np.array(values,dtype=float)
    lp.sense_=highspy.ObjSense.kMaximize
    h=highspy.Highs();h.silent();h.setOptionValue('threads',1);h.setOptionValue('time_limit',SOLVE_SECONDS);h.passModel(lp)
    t=time.monotonic();h.run();elapsed=time.monotonic()-t
    status=h.modelStatusToString(h.getModelStatus());info=h.getInfo();sol=h.getSolution()
    result={'status':status,'objective_float_unverified':float(info.objective_function_value),
            'rows':len(starts),'columns':cols,'nnz':len(indices),'solve_elapsed_s':elapsed}
    if status!='Optimal':return result,None
    result['nonzero_row_duals_float']=[{'meta':meta,'row':key,'dual':float(value)}
        for (key,meta),value in zip(labels,sol.row_dual) if abs(float(value))>1e-8]
    result['nonzero_col_duals_float']=[{'mask':masks[i],'dual':float(value)}
        for i,value in enumerate(sol.col_dual) if abs(float(value))>1e-8]
    hvals=np.full(1<<N,np.nan);hvals[0]=0.0
    for mask,i in col.items():hvals[mask]=sol.col_value[i]
    return result,hvals


def separate(hvals,existing):
    def cmi(a,b,z):return hvals[a|z]+hvals[b|z]-hvals[a|b|z]-hvals[z]
    violations={};checks=0
    for i,j in combinations(range(N),2):
        A,B=1<<i,1<<j
        others=[x for x in range(N) if x not in (i,j)]
        for ci in others:
            C=1<<ci
            for di in others:
                if ci==di:continue
                D=1<<di
                for zi in (-1,*(x for x in others if x not in (ci,di))):
                    Z=0 if zi<0 else 1<<zi
                    a=cmi(A,B,C|Z); delta=cmi(A,B,D|Z)+cmi(C,D,Z)-cmi(A,B,Z)
                    d=cmi(A,C,B|Z)+cmi(B,C,A|Z)
                    for order in (1,2,3,4):
                        checks+=1; factor=order*(order+1)//2
                        slack=(order+1)*a+order*delta+factor*d
                        if slack < -1e-8:
                            terms=(base.cmi(A,B,C|Z,order+1)+base.cmi(A,B,D|Z,order)
                                   +base.cmi(C,D,Z,order)+base.cmi(A,B,Z,-order)
                                   +base.cmi(A,C,B|Z,factor)+base.cmi(B,C,A|Z,factor))
                            key=compressed(terms)
                            rowkey=(key,0,highspy.kHighsInf)
                            if rowkey not in existing:
                                meta={'kind':'copy-family-cross-variables','n':order,'A':i,'B':j,'C':ci,'D':di,'Z':zi}
                                old=violations.get(key)
                                if old is None or slack<old[0]:violations[key]=(float(slack),meta)
    return checks,violations


def main():
    t0=time.monotonic();data={key:(ROOT/info[0]).read_bytes() for key,info in cert.FILES.items()}
    for key,(_,expected) in cert.FILES.items():cert.pin(key,data[key],expected)
    source=cert.parse_input(data['layout'],data['text'])
    rows=create_rows(source);initial=len(rows);rounds=[]
    for index in range(MAX_ROUNDS):
        result,hvals=solve(rows);result['round']=index
        if hvals is None:
            result['stop']='not optimal';rounds.append(result);break
        t=time.monotonic();count,violations=separate(hvals,rows)
        selected=sorted(violations.items(),key=lambda p:p[1][0])[:CUTS_PER_ROUND]
        result.update({'substitutions_checked':count,'unique_violations':len(violations),
                       'minimum_slack_float':min((x[0] for x in violations.values()),default=0.0),
                       'scan_elapsed_s':time.monotonic()-t,'cuts_added':len(selected)})
        for key,(slack,meta) in selected:rows[(key,0,highspy.kHighsInf)]=meta
        rounds.append(result)
        target=ROOT/f'frontier-20261028-cross-copy-upper-round-{index}.json'
        with target.open('x',encoding='utf-8') as stream:
            json.dump({k:v for k,v in result.items() if not k.startswith('nonzero_')},stream,indent=2);stream.write('\n')
        if not selected:break
    out={'source_rows':len(source),'initial_distinct_rows':initial,'symbols':SYMBOLS,
         'source_pins':{key:value[1] for key,value in cert.FILES.items()},
         'scanned_family':'A,B,C,D distinct singleton variables in common 17-variable extension; Z empty or one distinct singleton; n=1..4.',
         'shannon':'all conditional entropies on subsets size<=5 and CMIs conditioned on at most 3 variables, plus full original 10-variable Shannon rows.',
         'full_copy_equalities_included':True,'solver_threads':1,'per_solve_time_limit_s':SOLVE_SECONDS,
         'rounds':rounds,'total_elapsed_s':time.monotonic()-t0,
         'limits':'Numerical LP proposals only. A stronger bound requires an independently checked exact dual certificate and proof of all source/copy/entropy semantics.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps([{k:v for k,v in r.items() if not k.startswith('nonzero_')} for r in rounds],indent=2))
    print('initial_rows',initial,'total_elapsed_s',out['total_elapsed_s'])


if __name__=='__main__':main()
