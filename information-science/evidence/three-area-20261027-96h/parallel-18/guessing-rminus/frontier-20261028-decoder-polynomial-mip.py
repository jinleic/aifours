#!/usr/bin/env python3
"""Bounded binary-decoder MIP proposal for integer polynomial witnesses.

Each support word implies ten neighbour-lookup outputs. A MIP incumbent is
checked by exact integer arithmetic; floating optimality is not a proof.
"""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from random import Random
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
EXPECTED='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUTPUT=ROOT/'frontier-20261028-decoder-polynomial-mip-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
CASE_SECONDS=10.0;MAX_CASES=3


def main():
    start=monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    seed=json.loads(raw)['support_words_one_based_bitsets']
    offsets={};ncol=1024
    for v,ns in N.items():offsets[v]=ncol;ncol+=1<<len(ns)
    starts=[];ind=[];val=[];upper=[];seed_dec={}
    for w in range(1024):
        for v,ns in N.items():
            pattern=sum(((w>>(u-1))&1)<<j for j,u in enumerate(ns));b=(w>>(v-1))&1
            starts.append(len(ind));ind.extend((w,offsets[v]+pattern));val.extend((1.,-1. if b else 1.));upper.append(0. if b else 1.)
            if w in seed:
                key=(v,pattern)
                if key in seed_dec and seed_dec[key]!=b:raise ValueError('SEED_FD')
                seed_dec[key]=b
    initial=np.zeros(ncol);initial[seed]=1
    for (v,p),b in seed_dec.items():initial[offsets[v]+p]=b
    random=Random(2026102807);cases=[];witness=None
    for case in range(MAX_CASES):
        skew=set(random.sample(range(10),4))
        t=[[1,1] if v not in skew else ([2,3] if random.randrange(2) else [3,2]) for v in range(10)]
        D=1
        for a,b in t:D*=(a**3+b**3)**2
        weights=[]
        for w in range(1024):
            z=1
            for v in range(10):z*=t[v][(w>>v)&1]**2
            weights.append(z)
        cost=np.zeros(ncol);cost[:1024]=weights
        lp=highspy.HighsLp();lp.num_col_,lp.num_row_=ncol,len(starts)
        lp.col_cost_,lp.col_lower_,lp.col_upper_=cost,np.zeros(ncol),np.ones(ncol)
        lp.integrality_=[highspy.HighsVarType.kInteger]*ncol
        lp.row_lower_,lp.row_upper_=np.full(len(starts),-highspy.kHighsInf),np.array(upper)
        lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
        lp.a_matrix_.start_=np.array(starts+[len(ind)],dtype=np.int32)
        lp.a_matrix_.index_=np.array(ind,dtype=np.int32);lp.a_matrix_.value_=np.array(val,dtype=float)
        lp.sense_=highspy.ObjSense.kMaximize
        solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',CASE_SECONDS)
        solver.passModel(lp);seed_status=str(solver.setSolution(ncol,np.arange(ncol,dtype=np.int32),initial))
        t0=monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus());sol=solver.getSolution()
        entry={'integer_weights_t':t,'status_float_unverified':status,'seed_status':seed_status,'elapsed_seconds':monotonic()-t0}
        if sol.value_valid:
            W=[w for w in range(1024) if sol.col_value[w]>0.5]
            if any(any((a^b)&(1<<(v-1)) and all(not ((a^b)&(1<<(u-1))) for u in ns) for v,ns in N.items()) for a,b in combinations(W,2)):
                raise ValueError('MIP_FD_CONFLICT')
            S=sum(weights[w] for w in W);entry.update({'incumbent_size':len(W),'S':str(S),'strict_integer_witness':S**3>D})
            if S**3>D:witness={'support':W,'integer_weights_t':t,'S':str(S),'D':str(D)}
        cases.append(entry)
        if witness:break
    out={'seed_support_sha256':EXPECTED,'random_seed':2026102807,'case_limit_seconds':CASE_SECONDS,
         'decoder_variables':ncol-1024,'support_variables':1024,'implication_rows':len(starts),
         'cases':cases,'strict_integer_witness':witness,'elapsed_seconds':monotonic()-start,
         'limits':'Bounded q2 MIP proposals only. Floating solver status is not a proof; any positive integer witness requires separate original-graph and balancing verification.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_integer_witness'},indent=2))
    if witness:print('STRICT INTEGER WITNESS: independent verification required')


if __name__=='__main__':main()
