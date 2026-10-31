#!/usr/bin/env python3
"""Construct exact pairwise Shannon amalgams between source branches 2 and 3.

The selected pair fixes its two 11-variable marginals from the independently checked
14-variable star primal, adds all 12-variable Shannon inequalities WITHOUT
conditional independence, and reconstructs cross-entropies rationally. Pairwise
systems are NOT an all-16-variable or all-17-variable joint amalgam.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from math import lcm
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-separator-bound-primal.json';BASE_HASH='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
C12=ROOT/'frontier-20261028-crossbranch12-exact-candidate.json';C12_HASH='1037f7daf3cea8700b8b0a4a8c4f9981bc563a6b1038fdf91def9e921e84c739'
C13=ROOT/'frontier-20261028-crossbranch13-all-cuts-exact-candidate.json';C13_HASH='1d7263364c8c543bdd07a4b140c7a7ab2d65753c38506f26c02072fc9bd29703'
PROJECTION=ROOT/'frontier-20261028-exact-affine-reconstruction.py'
OUTPUT=ROOT/'frontier-20261028-crosspair-round2-noind-result.json'
BASEV=tuple('abcdefghij');SECOND=("d'1",);THIRD=("g'3",)
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('projection',PROJECTION);projection=module_from_spec(spec);spec.loader.exec_module(projection)


def pin(path,expected):
    raw=path.read_bytes()
    if sha256(raw).hexdigest()!=expected:raise ValueError(('HASH',path.name))
    return json.loads(raw)


def main():
    start=monotonic();base=pin(BASE,BASE_HASH);c12=pin(C12,C12_HASH);c13=pin(C13,C13_HASH)
    original={tuple(sorted(e['entropy_variables'])):Fraction(e['value']) for e in base['primal_values'] if set(e['entropy_variables'])<=set(BASEV)}
    if len(original)!=1023:raise ValueError('BASE_COORDINATES')
    results=[]
    for aa in SECOND:
        for bb in THIRD:
            variables=BASEV+(aa,bb);index={v:i for i,v in enumerate(variables)}
            known={0:Fraction(0)}
            def mask(labels):return sum(1<<index[v] for v in labels)
            for labels,v in original.items():known[mask(labels)]=v
            for doc,sym in ((c12,aa),(c13,bb)):
                allowed=set(BASEV)|{sym}
                for e in doc['auxiliary_values']:
                    labels=e['entropy_variables']
                    if sym in labels and set(labels)<=allowed:
                        m=mask(labels)
                        if m in known:raise ValueError('DUPLICATE_MARGINAL')
                        known[m]=Fraction(e['value'])
            if len(known)!=3072:raise ValueError(('FIXED_SIZE',aa,bb,len(known)))
            scale=lcm(*(x.denominator for x in known.values()));fixed={m:int(x*scale) for m,x in known.items()}
            unknown=[m for m in range(1,4096) if m not in known];cols={m:i for i,m in enumerate(unknown)}
            if len(unknown)!=1024:raise ValueError('UNKNOWN_SIZE')
            starts=array('i');indices=array('i');coef=array('d');lo=array('d');hi=array('d');lower=[];upper=[];known_only=0
            def add(terms,equality=False):
                nonlocal known_only
                constant=0;un={}
                for m,c in terms:
                    if m in fixed:constant+=c*fixed[m]
                    else:un[cols[m]]=un.get(cols[m],0)+c
                un={j:c for j,c in un.items() if c}
                if not un:
                    known_only+=1
                    if (equality and constant) or (not equality and constant<0):raise ValueError(('KNOWN_CONTRADICTION',aa,bb,terms,constant))
                    return
                starts.append(len(indices))
                for j,c in un.items():indices.append(j);coef.append(float(c))
                lower.append(-constant);upper.append(-constant if equality else None)
                lo.append(-constant/scale);hi.append(-constant/scale if equality else highspy.kHighsInf)
            full=4095
            for i in range(12):add(((full,1),(full^(1<<i),-1)))
            for i,j in combinations(range(12),2):
                a,b=1<<i,1<<j;z=full^a^b
                while True:
                    add(((z|a,1),(z|b,1),(z|a|b,-1),(z,-1)))
                    if not z:break
                    z=(z-1)&(full^a^b)
            original_mask=1023;a,b=1<<10,1<<11
            lp=highspy.HighsLp();lp.num_col_,lp.num_row_=len(unknown),len(starts)
            lp.col_cost_,lp.col_lower_,lp.col_upper_=np.zeros(len(unknown)),np.zeros(len(unknown)),np.full(len(unknown),12.)
            lp.row_lower_,lp.row_upper_=np.frombuffer(lo,dtype=np.float64),np.frombuffer(hi,dtype=np.float64)
            lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
            lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
            lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(coef,dtype=np.float64)
            lp.sense_=highspy.ObjSense.kMinimize
            solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('solver','ipm')
            solver.setOptionValue('run_crossover','off');solver.setOptionValue('time_limit',12.0);solver.passModel(lp);solver.run()
            status=solver.modelStatusToString(solver.getModelStatus())
            result={'pair':[aa,bb],'fixed_marginal_coordinates':3071,'cross_coordinates':1024,
                    'elemental_shannon_rows':67596,'conditional_independence_rows':0,
                    'known_only_exact_checks':known_only,'status_float_unverified':status}
            if status=='Optimal':
                report,x=projection.reconstruct(solver.getSolution().col_value,starts,indices,coef,lower,upper,scale,12,seconds=10)
                result['exact_affine_reconstruction']=report
                if x is not None:
                    result['exact_candidate_found']=True
                    result['cross_values']=[{'entropy_variables':[variables[i] for i in range(12) if m&(1<<i)],'value':str(x[j])}
                                            for j,m in enumerate(unknown)]
            path=ROOT/'frontier-20261028-crosspair-round2-noind-candidate.json'
            with path.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
            result['candidate_file']=path.name;result['candidate_sha256']=sha256(path.read_bytes()).hexdigest()
            results.append({k:v for k,v in result.items() if k!='cross_values'})
            print(json.dumps({k:v for k,v in results[-1].items() if k!='exact_affine_reconstruction'}),flush=True)
    out={'base_sha256':BASE_HASH,'cross12_sha256':C12_HASH,'cross13_sha256':C13_HASH,'pairs':results,
         'single_pair_exact_candidate':all(r.get('exact_candidate_found',False) for r in results),
         'elapsed_seconds':monotonic()-start,
         'limits':'A single 12-variable Shannon system without conditional independence. Numerical status is not proof; any exact candidate needs an independent checker. No original-base or entropic realization follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({'pairs':len(results),'single_pair_exact_candidate':out['single_pair_exact_candidate'],'elapsed_seconds':out['elapsed_seconds']}))


if __name__=='__main__':main()
