#!/usr/bin/env python3
"""Propose a lower total Ingleton coefficient for the exact FD balance identity.

Finds a conic certificate for (2/3)sum_v h(v)-h(V), with orbit-reduced
Shannon and singleton conditional-Ingleton rows. Float output is only a
proposal; an independently verified rational certificate is required.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-copy-family-upper-lp.py'
OUTPUT=ROOT/'frontier-20261028-defect-multiplier-lp-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('base',BASE);base=module_from_spec(spec);spec.loader.exec_module(base)


def main():
    start=monotonic();group=base.automorphism_group();orbit,reps=base.canonical_orbits(group)
    rows=base.shannon_rows(orbit);shannon_count=len(rows);ing_count=0
    for ai,bi in combinations(range(10),2):
        other=[k for k in range(10) if k not in (ai,bi)];a,b=1<<ai,1<<bi
        for ci,di in combinations(other,2):
            c,d=1<<ci,1<<di;zall=base.FULL^a^b^c^d;z=zall
            while True:
                key=base.row_from_terms(base.cmi(a,b,c|z)+base.cmi(a,b,d|z)+base.cmi(c,d,z)+base.cmi(a,b,z,-1),orbit)
                if key and key not in rows:
                    rows[key]={'kind':'conditional-ingleton','A':ai+1,'B':bi+1,'C':ci+1,'D':di+1,'Z_mask':z};ing_count+=1
                if not z:break
                z=(z-1)&zall
    fd=base.fd_rows(orbit);variables=list(rows.items())+list(fd.items());ncol=len(variables);nrow=len(reps)
    starts=[];ind=[];value=[];cost=[];low=[];high=[];inf=highspy.kHighsInf
    for key,meta in variables:
        starts.append(len(ind))
        for i,c in key:ind.append(i);value.append(float(c))
        cost.append(1.0 if meta['kind']=='conditional-ingleton' else 0.0)
        low.append(-inf if meta['kind']=='FD' else 0.0);high.append(inf)
    rhs=np.zeros(nrow);rhs[orbit[1]]=4/3;rhs[orbit[2]]=8/3;rhs[orbit[4]]=8/3;rhs[orbit[base.FULL]]=-1
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=ncol,nrow
    lp.col_cost_,lp.col_lower_,lp.col_upper_=np.array(cost),np.array(low),np.array(high)
    lp.row_lower_,lp.row_upper_=rhs,rhs
    lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_=np.array(starts+[len(ind)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(ind,dtype=np.int32);lp.a_matrix_.value_=np.array(value,dtype=float)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',25.0)
    solver.passModel(lp);t=monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    out={'base_sha256':sha256(BASE.read_bytes()).hexdigest(),'orbits':nrow,'shannon_rows':shannon_count,
         'ingleton_rows':ing_count,'FD_rows':len(fd),'status_float_unverified':status,
         'objective_float_unverified':float(solver.getInfo().objective_function_value),
         'solver_seconds':monotonic()-t,'total_seconds':monotonic()-start,
         'limits':'Numerical proposal only. Any defect bound requires exact reconstruction of every nonnegative weight, row and identity; no nonlinear numeric guessing-number upper follows by itself.'}
    if status=='Optimal':
        sol=solver.getSolution();nonzero=[];acc=[Fraction(0) for _ in reps];bad=[]
        for (key,meta),value in zip(variables,sol.col_value):
            if abs(value)<1e-9:continue
            q=Fraction(float(value)).limit_denominator(1000000)
            if meta['kind']!='FD' and q<0:bad.append(('negative',meta,str(q)))
            for i,c in key:acc[i]+=q*c
            nonzero.append({'metadata':meta,'orbit_terms':key,'weight':str(q),'weight_float':float(value)})
        targets={orbit[1]:Fraction(4,3),orbit[2]:Fraction(8,3),orbit[4]:Fraction(8,3),orbit[base.FULL]:Fraction(-1)}
        for i,x in targets.items():acc[i]-=x
        out.update({'rows':nonzero,'candidate_ingleton_weight_sum':str(sum(Fraction(x['weight']) for x in nonzero if x['metadata']['kind']=='conditional-ingleton')),
                    'rationalization_bad':bad,'coefficient_residual':[[reps[i],str(x)] for i,x in enumerate(acc) if x]})
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','coefficient_residual')},indent=2))
    if status=='Optimal':print('support',len(nonzero),'rational_residual',len(out['coefficient_residual']))


if __name__=='__main__':main()
