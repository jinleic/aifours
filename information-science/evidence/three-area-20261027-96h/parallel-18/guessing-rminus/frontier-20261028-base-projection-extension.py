#!/usr/bin/env python3
"""Try to extend only the all-F_n original entropy profile to source branches.

All auxiliary entropy coordinates are free; original coordinates are fixed.
Every source copy equality and every branch elemental Shannon inequality is
included. Numerical infeasibility/timeout is not proof. A proposed exact point
is reported only after all branch rows are checked with Fraction arithmetic.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from itertools import combinations
from math import lcm
from pathlib import Path
import gc
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
spec=spec_from_file_location('cert2',ROOT/'frontier-20261028-gurpinar-certificate-independent.py')
cert=module_from_spec(spec);spec.loader.exec_module(cert)
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUTPUT=ROOT/'frontier-20261028-base-projection-extension-result.json'
BASE=tuple('abcdefghij')
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))
SOLVE_SECONDS=30.0


def solve_branch(number,variables,base_values,all_copy_forms):
    started=time.monotonic();n=len(variables);full=(1<<n)-1
    def key(mask):return tuple(sorted(variables[i] for i in range(n) if mask&(1<<i)))
    index={v:i for i,v in enumerate(variables)}
    def mask(labels):return sum(1<<index[v] for v in labels)
    known={0:Fraction(0)}
    for m in range(1,full+1):
        k=key(m)
        if k in base_values:known[m]=base_values[k]
    if len(known)!=1024:raise ValueError(('BASE_COUNT',number,len(known)))
    scale=lcm(*(v.denominator for v in known.values()))
    fixed={m:int(value*scale) for m,value in known.items()}
    unknown=[m for m in range(1,full+1) if m not in known]
    cols={m:i for i,m in enumerate(unknown)}
    starts=array('i');indices=array('i');coeff=array('d');lo=array('d');hi=array('d')
    exact_lower=[];exact_upper=[];known_only=0;total=0;copy_count=0
    def add(terms,equality=False):
        nonlocal known_only,total
        total+=1;constant=0;unknown_terms={}
        for m,c in terms:
            if m in fixed:constant+=c*fixed[m]
            else:unknown_terms[cols[m]]=unknown_terms.get(cols[m],0)+c
        unknown_terms={i:c for i,c in unknown_terms.items() if c}
        if not unknown_terms:
            known_only+=1
            if (equality and constant!=0) or (not equality and constant<0):
                raise ValueError(('FIXED_CONTRADICTION',number,terms,constant,scale))
            return
        starts.append(len(indices))
        for i,c in unknown_terms.items():indices.append(i);coeff.append(float(c))
        exact_lower.append(-constant);exact_upper.append(-constant if equality else None)
        lo.append(-constant/scale);hi.append(-constant/scale if equality else highspy.kHighsInf)
    for v in range(n):add(((full,1),(full^(1<<v),-1)))
    for i,j in combinations(range(n),2):
        rest=full^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)))
            if z==0:break
            z=(z-1)&rest
    for form in all_copy_forms:
        labels={v for names,_ in form for v in names}
        if labels<=set(variables):
            copy_count+=1;add(tuple((mask(names),value) for names,value in form),equality=True)
    lp=highspy.HighsLp();lp.num_col_=len(unknown);lp.num_row_=len(starts)
    lp.col_cost_=np.zeros(len(unknown));lp.col_lower_=np.zeros(len(unknown));lp.col_upper_=np.full(len(unknown),float(n))
    lp.row_lower_=np.frombuffer(lo,dtype=np.float64);lp.row_upper_=np.frombuffer(hi,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32);lp.a_matrix_.value_=np.frombuffer(coeff,dtype=np.float64)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',SOLVE_SECONDS)
    solver.passModel(lp);t=time.monotonic();solver.run();elapsed=time.monotonic()-t
    status=solver.modelStatusToString(solver.getModelStatus())
    result={'branch':number,'variables':variables,'fixed_base_coordinates':1023,
            'unknown_auxiliary_coordinates':len(unknown),'all_elemental_plus_copy_rows':total,
            'full_copy_equality_rows':copy_count,'known_only_rows_exactly_checked':known_only,
            'solver_rows':len(starts),'solver_nnz':len(indices),
            'status_float_unverified':status,'solver_elapsed_s':elapsed}
    if status=='Optimal':
        solution=solver.getSolution().col_value;attempts=[]
        for maxden in (1000,10000,100000,1000000):
            x=[Fraction(float(v)).limit_denominator(maxden) for v in solution]
            bad=sum(1 for v in x if v<0 or v>n)
            for row in range(len(starts)):
                end=starts[row+1] if row+1<len(starts) else len(indices)
                value=sum((x[indices[j]]*int(coeff[j]) for j in range(starts[row],end)),Fraction(0))*scale
                if value<exact_lower[row] or (exact_upper[row] is not None and value>exact_upper[row]):bad+=1
            attempts.append({'max_denominator':maxden,'violations':bad})
            if not bad:
                result['exact_rational_branch_extension_found']=True
                result['auxiliary_values']=[{'entropy_variables':key(m),'value':str(x[i])} for i,m in enumerate(unknown)]
                break
        result['rationalization_attempts']=attempts
    result['total_elapsed_s']=time.monotonic()-started
    return result


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw);values={tuple(x['entropy_variables']):Fraction(x['value']) for x in data['primal_values']
                                   if set(x['entropy_variables'])<=set(BASE)}
    if len(values)!=1023:raise ValueError(('BASE_COORDINATES',len(values)))
    forms=[key for key in cert.copy_forms() if key and key[0][1]>0]
    records=[]
    for number,variables in enumerate(BRANCHES,1):
        result=solve_branch(number,variables,values,forms);records.append(result)
        path=ROOT/f'frontier-20261028-base-projection-extension-branch-{number}.json'
        with path.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
        print(json.dumps({k:v for k,v in result.items() if k!='auxiliary_values'},indent=2),flush=True)
        gc.collect()
    output={'input_sha256':EXPECTED,'base_coordinates_fixed':1023,'solver_threads':1,
            'per_branch_limit_s':SOLVE_SECONDS,'branches':records,
            'all_three_exact_branch_extensions':all(r.get('exact_rational_branch_extension_found',False) for r in records),
            'elapsed_s':time.monotonic()-started,
            'limits':'Exact feasible branch extensions would establish a full source-LP primal for this fixed base profile, not entropic realizability. Numerical infeasible/timeout or failed rationalization alone are not mathematical proof.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')


if __name__=='__main__':main()
