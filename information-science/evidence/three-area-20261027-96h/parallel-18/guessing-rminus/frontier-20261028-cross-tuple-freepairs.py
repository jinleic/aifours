#!/usr/bin/env python3
"""Attempt one exact 13-variable multi-auxiliary cross-copy amalgam.

Fixes only same-branch marginals of (d'1,g'2,f'3) from checked star systems;
all pair and triple cross-entropies are free. Adds every 13-variable Shannon
row and I(d'1,g'2;f'3|X)=0.
A fixed-marginal failure does not exclude alternative source-copy assignments.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import lcm
from pathlib import Path
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
C12=('frontier-20261028-crossbranch12-exact-candidate.json','1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739')
C13=('frontier-20261028-crossbranch13-threefamilies-exact-candidate.json','e31643a10db9556bf8394d7b7d2a9cf1b20fa9380bf3da98b57bd2c655ca8474')
OUT=ROOT/'frontier-20261028-cross-tuple-freepairs-result.json'
CAND=ROOT/'frontier-20261028-cross-tuple-freepairs-candidate.json'
ORIGINAL=tuple('abcdefghij');AUX=("d'1","g'2","f'3");VARS=ORIGINAL+AUX
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('projection',ROOT/'frontier-20261028-exact-affine-reconstruction.py');projection=module_from_spec(spec);spec.loader.exec_module(projection)


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return json.loads(raw)


def main():
    base,c12,c13=map(pin,(BASE,C12,C13));index={v:i for i,v in enumerate(VARS)}
    def mask(labels):return sum(1<<index[v] for v in labels)
    known={0:Fraction(0)}
    for e in base['primal_values']:
        labs=e['entropy_variables']
        if set(labs)<=set(ORIGINAL):known[mask(labs)]=Fraction(e['value'])
    if len(known)!=1024:raise ValueError('BASE')
    # Singletons and the within-V pair are fixed by the star systems.
    for doc,allowed in ((c12,set(ORIGINAL)|set(AUX[:2])),(c13,set(ORIGINAL)|{AUX[2]})):
        for e in doc['auxiliary_values']:
            labs=e['entropy_variables']
            if set(labs)<=allowed and set(labs)&set(AUX):
                m=mask(labs)
                if m in known:raise ValueError('DUPLICATE_STAR')
                known[m]=Fraction(e['value'])
    if len(known)!=5120:raise ValueError(('KNOWN_SIZE',len(known)))
    scale=lcm(*(v.denominator for v in known.values()));fixed={m:int(v*scale) for m,v in known.items()}
    unknown=[m for m in range(1,8192) if m not in known];cols={m:i for i,m in enumerate(unknown)}
    if len(unknown)!=3072:raise ValueError('UNKNOWN_SIZE')
    starts=array('i');indices=array('i');coeff=array('d');lo=array('d');hi=array('d');lower=[];upper=[];known_only=0
    def add(terms,equality=False):
        nonlocal known_only
        constant=0;un={}
        for m,c in terms:
            if m in fixed:constant+=c*fixed[m]
            else:un[cols[m]]=un.get(cols[m],0)+c
        un={i:c for i,c in un.items() if c}
        if not un:
            known_only+=1
            if (equality and constant) or (not equality and constant<0):raise ValueError(('KNOWN_CONTRADICTION',terms,constant))
            return
        starts.append(len(indices))
        for i,c in un.items():indices.append(i);coeff.append(float(c))
        lower.append(-constant);upper.append(-constant if equality else None)
        lo.append(-constant/scale);hi.append(-constant/scale if equality else highspy.kHighsInf)
    full=8191
    for i in range(13):add(((full,1),(full^(1<<i),-1)))
    for i,j in combinations(range(13),2):
        a,b=1<<i,1<<j;z=full^a^b
        while True:
            add(((z|a,1),(z|b,1),(z|a|b,-1),(z,-1)))
            if not z:break
            z=(z-1)&(full^a^b)
    X=1023;A=(1<<10)|(1<<11);B=1<<12
    add(((X|A,1),(X|B,1),(X|A|B,-1),(X,-1)),equality=True)
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=len(unknown),len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=np.zeros(len(unknown)),np.zeros(len(unknown)),np.full(len(unknown),13.)
    lp.row_lower_,lp.row_upper_=np.frombuffer(lo,dtype=np.float64),np.frombuffer(hi,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(coeff,dtype=np.float64);lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('solver','ipm');solver.setOptionValue('run_crossover','off');solver.setOptionValue('time_limit',20.);solver.passModel(lp);solver.run()
    status=solver.modelStatusToString(solver.getModelStatus());result={'variables':VARS,'fixed_coordinates':5119,'unknown_coordinates':3072,
        'known_only_exact_checks':known_only,'status_float_unverified':status}
    if status=='Optimal':
        report,x=projection.reconstruct(solver.getSolution().col_value,starts,indices,coeff,lower,upper,scale,13,seconds=15)
        result['exact_affine_reconstruction']=report
        if x is not None:
            result['exact_candidate_found']=True
            result['cross_values']=[{'entropy_variables':[VARS[i] for i in range(13) if m&(1<<i)],'value':str(x[j])} for j,m in enumerate(unknown)]
    with CAND.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    result['base_sha256']=BASE[1];result['cross12_sha256']=C12[1];result['cross13_sha256']=C13[1]
    result['candidate_file']=CAND.name;result['candidate_sha256']=sha256(CAND.read_bytes()).hexdigest()
    result['limits']='Only one 13-variable system with fixed chosen same-branch marginals and free pair/triple cross-entropies; any candidate needs independent checking, and no all-17-variable or entropic conclusion follows.'
    with OUT.open('x',encoding='utf-8') as stream:json.dump({k:v for k,v in result.items() if k!='cross_values'},stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in result.items() if k!='cross_values'},indent=2))


if __name__=='__main__':main()
