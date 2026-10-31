#!/usr/bin/env python3
"""Bounded q=2 FD-support search with all graph-independent-set clique rows."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
SEED=('frontier-20261028-fd-law-search-precise-result.json','c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc')
OUT=ROOT/'frontier-20261028-binary-clique-mip-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def verify(words):
    if len(set(words))!=len(words) or any(not isinstance(w,int) or not 0<=w<1024 for w in words):raise ValueError('WORDS')
    for v in range(1,11):
        seen={}
        for w in words:
            key=tuple((w>>(u-1))&1 for u in N[v]);val=(w>>(v-1))&1
            if key in seen and seen[key]!=val:raise ValueError('FD')
            seen[key]=val
    return len(words)**3>2**20


def main():
    start=monotonic();raw=(ROOT/SEED[0]).read_bytes()
    if sha256(raw).hexdigest()!=SEED[1]:raise ValueError('HASH')
    seed=json.loads(raw)['support_words_one_based_bitsets'];verify(seed)
    if 0 not in seed:raise ValueError('SEED_TRANSLATION')
    nm=[sum(1<<(u-1) for u in N[i]) for i in range(1,11)]
    bad=[d for d in range(1,1024) if any((d>>i&1) and not(d&nm[i]) for i in range(10))]
    indep=[I for I in range(1,1024) if all(not(I&nm[i]) for i in range(10) if I>>i&1)]
    maximal=[I for I in indep if not any(I!=J and I&J==I for J in indep)]
    if len(bad)!=113 or len(maximal)!=7:raise ValueError('GRAPH')
    starts=[];idx=[];vals=[];lo=[];hi=[]
    def row(indices,upper):
        starts.append(len(idx));idx.extend(indices);vals.extend([1.]*len(indices));lo.append(-highspy.kHighsInf);hi.append(float(upper))
    pair_count=0
    for d in bad:
        for u in range(1024):
            v=u^d
            if u<v:row((u,v),1);pair_count+=1
    clique_count=0
    for I in maximal:
        fixed=1023^I
        for base in range(1024):
            if base&I:continue
            members=[];s=I
            while True:
                members.append(base|s)
                if not s:break
                s=(s-1)&I
            row(members,1);clique_count+=1
    if pair_count!=57856 or clique_count!=1024:raise ValueError(('ROW_COUNT',pair_count,clique_count))
    lp=highspy.HighsLp();lp.num_col_=1024;lp.num_row_=len(starts);lp.col_cost_=np.ones(1024)
    lower=np.zeros(1024);lower[0]=1;lp.col_lower_=lower;lp.col_upper_=np.ones(1024);lp.integrality_=[highspy.HighsVarType.kInteger]*1024
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(idx)],np.int32);lp.a_matrix_.index_=np.array(idx,np.int32);lp.a_matrix_.value_=np.array(vals,float)
    lp.sense_=highspy.ObjSense.kMaximize
    init=np.zeros(1024);init[seed]=1
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',25.)
    solver.passModel(lp);seed_status=str(solver.setSolution(1024,np.arange(1024,dtype=np.int32),init));solver.run();sol=solver.getSolution()
    chosen=[i for i in range(1024) if sol.col_value[i]>.5] if sol.value_valid else []
    strict=verify(chosen) if chosen else False
    out={'seed_sha256':SEED[1],'pair_conflict_rows':pair_count,'maximal_independent_set_clique_rows':clique_count,
         'solver_status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),'seed_status':seed_status,
         'incumbent_size':len(chosen),'incumbent_words':chosen,'strict_original_target_gain':strict,
         'elapsed_seconds':monotonic()-start,
         'limits':'Bounded global q2 MIP proposal, not an exact upper bound. Any strict incumbent requires separately pinned independent decoder and entropy verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='incumbent_words'},indent=2))


if __name__=='__main__':main()
