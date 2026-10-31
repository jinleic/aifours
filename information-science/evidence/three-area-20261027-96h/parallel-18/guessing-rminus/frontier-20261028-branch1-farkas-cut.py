#!/usr/bin/env python3
"""Extract and verify an exact copy-Shannon separator of a fixed base profile.

HiGHS suggests a small infeasibility ray; Z3 reconstructs nonnegative rational
multipliers on that support. All cancellation and separation checks are exact.
A missing ray or failed reconstruction is NOT an infeasibility proof.
"""
from fractions import Fraction
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
from z3 import Real, Solver, Sum, sat
spec=spec_from_file_location('cert2',ROOT/'frontier-20261028-gurpinar-certificate-independent.py')
cert=module_from_spec(spec);spec.loader.exec_module(cert)
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUTPUT=ROOT/'frontier-20261028-branch1-farkas-cut-result.json'
SYMBOLS=tuple('abcdefghij')+("b'0",)
BASE=set('abcdefghij')
SOLVE_SECONDS=30.0


def mask(names):return sum(1<<SYMBOLS.index(v) for v in names)


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values']
    base_values={mask(x['entropy_variables']):Fraction(x['value']) for x in entries
                 if set(x['entropy_variables'])<=BASE}
    if len(base_values)!=1023:raise ValueError('BASE_COUNT')
    base_values[0]=Fraction(0)
    unknown=[m for m in range(1,1<<11) if m not in base_values]
    col={m:i for i,m in enumerate(unknown)}
    rows=[];known_only=0
    def add(terms,equality,metadata):
        nonlocal known_only
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        const=sum((Fraction(c)*base_values[m] for m,c in full.items() if m in base_values),Fraction())
        small={col[m]:c for m,c in full.items() if m not in base_values}
        if not small:
            known_only+=1
            if (equality and const!=0) or (not equality and const<0):raise ValueError(('BASE_CONTRADICTION',metadata))
            return
        rows.append({'full':full,'unknown':small,'rhs':-const,'equality':equality,'metadata':metadata})
    allmask=(1<<11)-1
    for i in range(11):add(((allmask,1),(allmask^(1<<i),-1)),False,{'kind':'conditional_entropy','i':i})
    for i,j in combinations(range(11),2):
        rest=allmask^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)),False,
                {'kind':'CMI','i':i,'j':j,'z':z})
            if not z:break
            z=(z-1)&rest
    for m in unknown:add(((m,1),),False,{'kind':'entropy_nonnegative','mask':m})
    copy_count=0
    for form in cert.copy_forms():
        if not form or form[0][1]<0:continue
        names={x for labels,_ in form for x in labels}
        if names<=set(SYMBOLS):
            copy_count+=1
            add(tuple((mask(labels),c) for labels,c in form),True,{'kind':'copy_equality'})
    starts=[];indices=[];values=[];lower=[];upper=[]
    for row in rows:
        starts.append(len(indices))
        for j,c in row['unknown'].items():indices.append(j);values.append(float(c))
        b=float(row['rhs']);lower.append(b);upper.append(b if row['equality'] else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=len(unknown);lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(len(unknown));lp.col_lower_=np.full(len(unknown),-highspy.kHighsInf)
    lp.col_upper_=np.full(len(unknown),highspy.kHighsInf)
    lp.row_lower_,lp.row_upper_=np.array(lower),np.array(upper)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(indices)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(indices,dtype=np.int32);lp.a_matrix_.value_=np.array(values,dtype=float)
    lp.sense_=highspy.ObjSense.kMinimize
    hs=highspy.Highs();hs.silent();hs.setOptionValue('threads',1);hs.setOptionValue('time_limit',SOLVE_SECONDS)
    hs.passModel(lp);t=time.monotonic();hs.run();status=hs.modelStatusToString(hs.getModelStatus())
    result={'base_point_sha256':EXPECTED,'symbols':SYMBOLS,'status_float_unverified':status,
            'unknown_columns':len(unknown),'rows':len(rows),'known_only_rows':known_only,
            'copy_form_count':copy_count,'solver_s':time.monotonic()-t}
    if status=='Infeasible':
        ray_status,exists,ray=hs.getDualRay()
        result['dual_ray_status']=str(ray_status);result['dual_ray_exists']=bool(exists)
        if exists:
            active=[i for i,x in enumerate(ray) if abs(float(x))>1e-8]
            result['float_ray_nonzero_rows']=len(active)
            y=[Real(f'y_{i}') for i in range(len(active))]
            solver=Solver();solver.set(timeout=15000)
            for j,index in enumerate(active):
                if not rows[index]['equality']:solver.add(y[j]>=0)
            cols_in_use=sorted({c for index in active for c in rows[index]['unknown']})
            for c in cols_in_use:
                solver.add(Sum([y[j]*rows[index]['unknown'].get(c,0) for j,index in enumerate(active)])==0)
            solver.add(Sum([y[j]*str(rows[index]['rhs']) for j,index in enumerate(active)])>=1)
            exact_status=solver.check();result['exact_multiplier_solver_status']=str(exact_status)
            if exact_status==sat:
                model=solver.model();weights=[model.eval(v,model_completion=True).as_fraction() for v in y]
                aggregate={}
                selected=[]
                for index,weight in zip(active,weights):
                    weight=Fraction(weight)
                    if not weight:continue
                    row=rows[index]
                    if not row['equality'] and weight<0:raise ValueError('NEGATIVE_MULTIPLIER')
                    for m,c in row['full'].items():aggregate[m]=aggregate.get(m,Fraction())+weight*c
                    selected.append({'row_index':index,'weight':str(weight),'equality':row['equality'],
                                     'metadata':row['metadata'],'terms':[[m,c] for m,c in sorted(row['full'].items())]})
                aggregate={m:c for m,c in aggregate.items() if c}
                if any(m not in base_values for m in aggregate):raise ValueError('AUXILIARY_DID_NOT_CANCEL')
                evaluation=sum((base_values[m]*c for m,c in aggregate.items()),Fraction())
                if evaluation>=0:raise ValueError(('SEPARATOR_NOT_NEGATIVE',str(evaluation)))
                result['exact_separator']={'selected_rows':selected,
                    'original_entropy_coefficients':[[m,str(c)] for m,c in sorted(aggregate.items())],
                    'point_evaluation':str(evaluation),'auxiliary_coefficients_zero':True,
                    'all_inequality_weights_nonnegative':True}
    result['elapsed_s']=time.monotonic()-started
    result['limits']='A verified separator excludes this base entropy point from this one-copy Shannon extension; it does not itself prove an improved R-minus upper bound or an entropic witness.'
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
