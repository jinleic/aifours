#!/usr/bin/env python3
"""Test whether the frozen partial entropy point extends to each full branch.

Known coordinates are fixed; missing coordinates are LP variables, never zero
by default. HiGHS is a bounded numerical screen. Only a rational solution that
passes every elemental inequality exactly could be treated as an exact primal;
a numerical infeasibility result alone is not a certificate.
"""
from array import array
from fractions import Fraction
from hashlib import sha256
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
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUTPUT=ROOT/'frontier-20261028-partial-point-extension-result.json'
BASE=tuple('abcdefghij')
BRANCHES=(BASE+("b'0",),BASE+("d'1","e'1","g'2"),BASE+("f'3","g'3","h'4"))
SOLVE_SECONDS=25.0


def solve_branch(number,variables,all_values):
    started=time.monotonic();n=len(variables);full=(1<<n)-1
    def key(mask):return tuple(sorted(variables[i] for i in range(n) if mask&(1<<i)))
    known={0:Fraction(0)}
    for mask in range(1,full+1):
        k=key(mask)
        if k in all_values:known[mask]=all_values[k]
    if any(x<0 or x>n for x in known.values()):raise ValueError(('KNOWN_ENTROPY_RANGE',number))
    scale=lcm(*(v.denominator for v in known.values()))
    ints={mask:int(value*scale) for mask,value in known.items()}
    unknown=[m for m in range(1,full+1) if m not in known]
    ids={mask:i for i,mask in enumerate(unknown)}
    starts=array('i');indices=array('i');coefficients=array('d');lower=array('d');upper=array('d')
    exact_lower=[]
    known_only=0; total=0
    def add(terms):
        nonlocal known_only,total
        total+=1
        entries={};constant=0
        for mask,coefficient in terms:
            if mask in ints:constant+=coefficient*ints[mask]
            else:entries[ids[mask]]=entries.get(ids[mask],0)+coefficient
        entries={j:c for j,c in entries.items() if c}
        if not entries:
            known_only+=1
            if constant<0:raise ValueError(('KNOWN_SHANNON_FAILURE',number,terms,constant,scale))
            return
        starts.append(len(indices))
        for j,c in entries.items():indices.append(j);coefficients.append(float(c))
        lower.append(-constant/scale);upper.append(highspy.kHighsInf)
        exact_lower.append(-constant)
    for v in range(n):add(((full,1),(full^(1<<v),-1)))
    for i,j in combinations(range(n),2):
        remaining=full^(1<<i)^(1<<j);z=remaining
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)))
            if z==0:break
            z=(z-1)&remaining
    lp=highspy.HighsLp();lp.num_col_=len(unknown);lp.num_row_=len(starts)
    lp.col_cost_=np.zeros(len(unknown));lp.col_lower_=np.zeros(len(unknown));lp.col_upper_=np.full(len(unknown),float(n))
    lp.row_lower_=np.frombuffer(lower,dtype=np.float64);lp.row_upper_=np.frombuffer(upper,dtype=np.float64)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.append(np.frombuffer(starts,dtype=np.int32),np.int32(len(indices)))
    lp.a_matrix_.index_=np.frombuffer(indices,dtype=np.int32)
    lp.a_matrix_.value_=np.frombuffer(coefficients,dtype=np.float64)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1)
    solver.setOptionValue('time_limit',SOLVE_SECONDS);solver.passModel(lp)
    st=time.monotonic();solver.run();elapsed=time.monotonic()-st
    status=solver.modelStatusToString(solver.getModelStatus())
    result={'branch':number,'variables':variables,'known_coordinates':len(known)-1,
            'unknown_coordinates':len(unknown),'total_elemental_rows':total,
            'known_only_rows_exactly_checked':known_only,'solver_rows':len(starts),
            'solver_nnz':len(indices),'status_float_unverified':status,
            'solver_elapsed_s':elapsed,'total_elapsed_s':time.monotonic()-started}
    if status=='Optimal':
        solution=solver.getSolution().col_value
        # Reconstruct exact rationals; verify every matrix row with integer and
        # Fraction arithmetic and all 0..n bounds. A failed rounding is not a
        # proof that no exact solution exists.
        attempts=[]
        for maxden in (1000,10000,100000):
            x=[Fraction(float(v)).limit_denominator(maxden) for v in solution]
            bad=0
            for value in x:
                if value<0 or value>n:bad+=1
            for row in range(len(starts)):
                end=starts[row+1] if row+1<len(starts) else len(indices)
                lhs=sum((x[indices[j]]*int(coefficients[j]) for j in range(starts[row],end)),Fraction(0))
                if lhs*scale<exact_lower[row]:bad+=1
            attempts.append({'max_denominator':maxden,'violations':bad})
            if not bad:
                result['exact_rational_extension_found']=True
                result['extension_values']=[{'entropy_variables':key(mask),'value':str(x[i])}
                                            for i,mask in enumerate(unknown)]
                break
        result['rounding_attempts']=attempts
    return result


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    point=json.loads(raw)
    values={tuple(item['entropy_variables']):Fraction(item['value']) for item in point['primal_values']}
    if len(values)!=len(point['primal_values']):raise ValueError('DUPLICATE')
    records=[]
    for number,variables in enumerate(BRANCHES,1):
        result=solve_branch(number,variables,values);records.append(result)
        path=ROOT/f'frontier-20261028-partial-point-extension-branch-{number}.json'
        with path.open('x',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
        print(json.dumps({k:v for k,v in result.items() if k!='extension_values'},indent=2),flush=True)
        gc.collect()
    output={'input_sha256':EXPECTED,'branches':records,'solver_threads':1,
            'per_branch_time_limit_s':SOLVE_SECONDS,'elapsed_s':time.monotonic()-start,
            'limits':'Numerical status is not proof. Even exact branch-wise Shannon/copy extensions do not establish entropic realizability. Failed rounding and timeout do not prove infeasibility.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(output,stream,indent=2);stream.write('\n')


if __name__=='__main__':main()
