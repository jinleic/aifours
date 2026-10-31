#!/usr/bin/env python3
"""Find a linear-rank-only R-minus upper bound using conditional Ingleton.

All Shannon, graph FD and singleton conditional-Ingleton rows are included on
all graph-automorphism entropy orbits. HiGHS is only a proposer: a separate
exact nonnegative dual identity is required before claiming any bound.
Ingleton is NOT asserted for nonlinear or arbitrary entropy vectors.
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
INPUT=ROOT/'frontier-20261028-copy-family-upper-lp.py'
OUTPUT=ROOT/'frontier-20261028-conditional-ingleton-linear-lp-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('base',INPUT);base=module_from_spec(spec);spec.loader.exec_module(base)


def main():
    start=monotonic();group=base.automorphism_group();orbit,reps=base.canonical_orbits(group)
    rows=base.shannon_rows(orbit);shannon_count=len(rows);ing_count=0
    for ai,bi in combinations(range(10),2):
        remain=[k for k in range(10) if k not in (ai,bi)];a,b=1<<ai,1<<bi
        for ci,di in combinations(remain,2):
            c,d=1<<ci,1<<di;zset=base.FULL^a^b^c^d;z=zset
            while True:
                terms=(base.cmi(a,b,c|z)+base.cmi(a,b,d|z)+base.cmi(c,d,z)+base.cmi(a,b,z,-1))
                key=base.row_from_terms(terms,orbit)
                if key and key not in rows:
                    rows[key]={'kind':'conditional-ingleton','A':ai+1,'B':bi+1,'C':ci+1,'D':di+1,'Z_mask':z};ing_count+=1
                if z==0:break
                z=(z-1)&zset
    fd=base.fd_rows(orbit);starts=[];indices=[];values=[];lo=[];hi=[];meta=[];inf=highspy.kHighsInf
    def add(key,l,u,m):
        starts.append(len(indices))
        for i,x in key:indices.append(i);values.append(float(x))
        lo.append(l);hi.append(u);meta.append((key,m))
    for key,m in rows.items():add(key,0,inf,m)
    for key,m in fd.items():add(key,0,0,m)
    count=len(reps);clo=np.zeros(count);chi=np.full(count,inf)
    for i in range(10):chi[orbit[1<<i]]=1
    cost=np.zeros(count);cost[orbit[base.FULL]]=1
    lp=highspy.HighsLp();lp.num_col_=count;lp.num_row_=len(starts)
    lp.col_cost_,lp.col_lower_,lp.col_upper_=cost,clo,chi
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(indices)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(indices,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    lp.sense_=highspy.ObjSense.kMaximize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',20.0)
    solver.passModel(lp);st=monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    sol=solver.getSolution();out={'base_module_sha256':sha256(INPUT.read_bytes()).hexdigest(),'graph_automorphisms':len(group),
        'orbit_columns':count,'shannon_orbit_rows':shannon_count,'conditional_ingleton_orbit_rows':ing_count,
        'FD_orbit_rows':len(fd),'status_float_unverified':status,'solver_seconds':monotonic()-st,
        'objective_float_unverified':float(solver.getInfo().objective_function_value),
        'limits':'Only vector-linear/representable rank profiles satisfy these added inequalities. Float solver is not a proof; no nonlinear upper bound follows.'}
    if status=='Optimal':
        duals=[];res=[Fraction(0) for _ in range(count)];constant=Fraction(0);bad=[]
        for (key,m),value in zip(meta,sol.row_dual):
            if abs(value)<1e-9:continue
            q=Fraction(float(value)).limit_denominator(1000000)
            if abs(float(q)-float(value))>1e-8:bad.append(('row',float(value),str(q)))
            if m['kind']!='FD' and q>0:bad.append(('row_wrong_sign',m,str(q)))
            for i,x in key:res[i] += -q*x
            duals.append({'kind':'row','metadata':m,'orbit_terms':key,'dual':str(q)})
        for i,value in enumerate(sol.col_dual):
            if abs(value)<1e-9:continue
            q=Fraction(float(value)).limit_denominator(1000000)
            if abs(float(q)-float(value))>1e-8:bad.append(('column',i,float(value),str(q)))
            if q>0:
                if not np.isfinite(chi[i]):bad.append(('positive_unbounded_column',i,str(q)))
                constant+=q;res[i]-=q
            else:res[i]-=q
            duals.append({'kind':'column','orbit_representative':reps[i],'dual':str(q)})
        res[orbit[base.FULL]] +=1
        residual=[[reps[i],str(q)] for i,q in enumerate(res) if q]
        out.update({'nonzero_duals':duals,'rationalization_bad':bad,
                    'rational_constant_candidate':str(constant),'rational_coefficient_residual':residual,
                    'exact_dual_identity_candidate':not bad and not residual,
                    'target_20_over_3_or_lower':constant<=Fraction(20,3) if not bad and not residual else None})
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('nonzero_duals','rational_coefficient_residual')},indent=2))
    if status=='Optimal':print('dual_nonzeros',len(out['nonzero_duals']),'exact_residual_count',len(out['rational_coefficient_residual']))
    print('total_seconds',monotonic()-start)


if __name__=='__main__':main()
