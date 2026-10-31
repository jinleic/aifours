#!/usr/bin/env python3
"""Six-support FD-law proposals using exact pairwise strict-MI gate.

Selected rational distributions only. Floating MIP statuses are not proofs;
integer entropy comparisons and subgroup-free graph checks verify incumbents.
"""
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import log,prod
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
HELPER=('frontier-20261028-six-point-fd-search.py','09bb778d696bad401afc46f1892134a2babdd44324cd2b630ad51757a9849d5d')
OUT=ROOT/'frontier-20261028-six-point-mi-skew-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy


def helper():
    raw=(ROOT/HELPER[0]).read_bytes()
    if sha256(raw).hexdigest()!=HELPER[1]:raise ValueError('HASH')
    spec=spec_from_file_location('supporthelper',ROOT/HELPER[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod


def sizes(part,weights):
    return [sum(weights[i] for i,x in enumerate(part) if x==v) for v in set(part)]


def factor(blocks):return prod(v**v for v in blocks if v)


def compatible(p,q,weights,pfactor,qfactor,totalfactor):
    joint=factor(sizes(list(zip(p,q)),weights))
    return pfactor*qfactor*qfactor>totalfactor*joint*joint and qfactor*pfactor*pfactor>totalfactor*joint*joint


def run_case(mod,weights,parts,seconds):
    n=len(parts);npairs=list(combinations(range(6),2));factors=[factor(sizes(p,weights)) for p in parts];T=sum(weights)**sum(weights)
    incompatible=[(i,j) for i,j in combinations(range(n),2) if not compatible(parts[i],parts[j],weights,factors[i],factors[j],T)]
    starts=[];inds=[];vals=[];lower=[];upper=[];cols=11*n
    def row(d,lo,hi):
        starts.append(len(inds))
        for k,v in sorted(d.items()):
            if v:inds.append(k);vals.append(float(v))
        lower.append(float(lo));upper.append(float(hi))
    for i in range(10):row({i*n+p:1 for p in range(n)},1,1)
    for x,y in npairs:
        separate=[p for p,part in enumerate(parts) if part[x]!=part[y]]
        for i,nb in enumerate(mod.N):
            d={i*n+p:-1 for p in separate}
            for j in nb:
                for p in separate:d[j*n+p]=1
            row(d,0,highspy.kHighsInf)
        row({i*n+p:1 for i in range(10) for p in separate},1,highspy.kHighsInf)
    for p in range(n):
        d={i*n+p:1 for i in range(10)};d[10*n+p]=-1;row(d,0,0)
    for p,q in incompatible:row({10*n+p:1,10*n+q:1},-highspy.kHighsInf,1)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=cols,len(starts)
    lp.col_cost_=np.array([mod.entropy_cost(weights,p) for _ in range(10) for p in parts]+[0.]*n)
    lp.col_lower_=np.zeros(cols);lp.col_upper_=np.ones(cols);lp.integrality_=[highspy.HighsVarType.kInteger]*cols
    lp.row_lower_,lp.row_upper_=np.array(lower),np.array(upper);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],np.int32);lp.a_matrix_.index_=np.array(inds,np.int32);lp.a_matrix_.value_=np.array(vals,float)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',seconds);solver.passModel(lp);t0=monotonic();solver.run();sol=solver.getSolution()
    rec={'weights':list(weights),'allowed_partition_types':n,'incompatible_partition_pairs':len(incompatible),'rows':len(starts),
         'status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),'elapsed_seconds':monotonic()-t0,'incumbent':None}
    if sol.value_valid:
        chosen=[];picked=[]
        for i in range(10):
            hit=[p for p in range(n) if sol.col_value[i*n+p]>.5]
            if len(hit)!=1:raise ValueError('ONEHOT')
            picked.append(hit[0]);chosen.append(parts[hit[0]])
        if len(set(picked))!=10 or any(not compatible(parts[p],parts[q],weights,factors[p],factors[q],T) for p,q in combinations(picked,2)):raise ValueError('MI_GATE')
        rec['incumbent']=mod.exact_check(weights,chosen)
    return rec


def main():
    mod=helper();parts=[p for p in mod.partitions(6) if 1<len(set(p))<6]
    if len(parts)!=201:raise ValueError('PARTITION_COUNT')
    cases=((20,20,1,1,1,1),(40,20,1,1,1,1),(50,5,1,1,1,1),(100,100,2,2,1,1),(100,50,3,2,1,1),(100,5,4,3,2,1));results=[];witness=None
    for weights in cases:
        r=run_case(mod,weights,parts,8.);results.append(r)
        if r['incumbent'] and r['incumbent']['exact_gap_test_left_gt_right']:witness=r['incumbent'];break
    out={'source_helper_sha256':HELPER[1],'cases':results,'strict_witness':witness,'per_case_time_limit_seconds':8.,
         'limits':'Selected six-point distributions, full original FD constraints, exact strict-pair-MI pruning; numerical statuses do not prove nonexistence. Positive incumbent needs separate verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='strict_witness'},indent=2))


if __name__=='__main__':main()
