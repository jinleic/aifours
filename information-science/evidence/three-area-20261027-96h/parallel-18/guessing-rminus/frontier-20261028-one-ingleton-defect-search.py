#!/usr/bin/env python3
"""Test whether either of the two conditional Ingleton shapes alone suffices.

Each orbit-reduced conic LP is a floating proposer. Feasibility or a numerical
coefficient is not a proof; a separate exact dual checker is required.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=ROOT/'frontier-20261028-copy-family-upper-lp.py'
OUTPUT=ROOT/'frontier-20261028-one-ingleton-defect-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('base',BASE);base=module_from_spec(spec);spec.loader.exec_module(base)


def main():
    start=monotonic();group=base.automorphism_group();orbit,reps=base.canonical_orbits(group)
    shannon=base.shannon_rows(orbit);fd=base.fd_rows(orbit)
    targets=[{'kind':'conditional-ingleton','A':2,'B':4,'C':1,'D':3,'Z_mask':1008},
             {'kind':'conditional-ingleton','A':2,'B':5,'C':3,'D':6,'Z_mask':713}]
    cases=[]
    for meta in targets:
        a,b,c,d=[1<<(meta[k]-1) for k in ('A','B','C','D')];z=meta['Z_mask']
        key=base.row_from_terms(base.cmi(a,b,c|z)+base.cmi(a,b,d|z)+base.cmi(c,d,z)+base.cmi(a,b,z,-1),orbit)
        variables=list(shannon.items())+[(key,meta)]+list(fd.items());starts=[];ind=[];values=[];cost=[];lo=[];hi=[];inf=highspy.kHighsInf
        for row,m in variables:
            starts.append(len(ind))
            for i,x in row:ind.append(i);values.append(float(x))
            cost.append(1.0 if m['kind']=='conditional-ingleton' else 0.0)
            lo.append(-inf if m['kind']=='FD' else 0.0);hi.append(inf)
        rhs=np.zeros(len(reps));rhs[orbit[1]]=4/3;rhs[orbit[2]]=8/3;rhs[orbit[4]]=8/3;rhs[orbit[base.FULL]]=-1
        lp=highspy.HighsLp();lp.num_col_,lp.num_row_=len(variables),len(reps)
        lp.col_cost_,lp.col_lower_,lp.col_upper_=np.array(cost),np.array(lo),np.array(hi)
        lp.row_lower_,lp.row_upper_=rhs,rhs;lp.a_matrix_.format_=highspy.MatrixFormat.kColwise
        lp.a_matrix_.start_=np.array(starts+[len(ind)],dtype=np.int32)
        lp.a_matrix_.index_=np.array(ind,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
        lp.sense_=highspy.ObjSense.kMinimize
        solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',12.0)
        solver.passModel(lp);solver.run();status=solver.modelStatusToString(solver.getModelStatus())
        out={'shape':meta,'status_float_unverified':status,'objective_float_unverified':float(solver.getInfo().objective_function_value)}
        if status=='Optimal':
            acc=[Fraction(0) for _ in reps];nonzero=[];bad=[]
            for (row,m),x in zip(variables,solver.getSolution().col_value):
                if abs(x)<1e-9:continue
                q=Fraction(float(x)).limit_denominator(1000000)
                if m['kind']!='FD' and q<0:bad.append((m,str(q)))
                for i,c in row:acc[i]+=q*c
                nonzero.append({'metadata':m,'orbit_terms':row,'weight':str(q)})
            for mask,c in ((1,Fraction(4,3)),(2,Fraction(8,3)),(4,Fraction(8,3)),(base.FULL,Fraction(-1))):acc[orbit[mask]]-=c
            residual=[[reps[i],str(x)] for i,x in enumerate(acc) if x]
            out.update({'rows':nonzero,'bad_signs':bad,'coefficient_residual':residual,
                        'exact_identity_candidate':not residual and not bad})
        cases.append(out)
    result={'base_sha256':sha256(BASE.read_bytes()).hexdigest(),'group_size':len(group),'orbits':len(reps),
            'cases':cases,'elapsed_seconds':monotonic()-start,
            'limits':'Single-shape floating search only; exact feasibility/proof requires an independent rational checker and Ingleton is not universal entropy.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps([{k:v for k,v in x.items() if k not in ('rows','coefficient_residual')} for x in cases],indent=2))


if __name__=='__main__':main()
