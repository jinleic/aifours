#!/usr/bin/env python3
"""Separate a base profile by new one-copy structures modulo graph symmetry.

Skip the publisher's existing (X2,X3) copy orbit. HiGHS supplies candidate
infeasibility rays; Z3 and exact Fraction checks reconstruct separators. No
numerical status, source-core separation, or local search failure is a bound.
"""
from collections import deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
from z3 import Real,Solver,Sum,sat
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-distinct-copy-orbit-search-result.json'
BASE='abcdefghij'; FULL=1023; COPY=1024
NEIGHBOURS={
 1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
 5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
 9:(2,3,5,6,8),10:(2,4,5,7,8)}
GENS=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
MAX_WALL_S=80.0
PER_COPY_SOLVE_S=4.0
Z3_MS=10000


def group():
    edges={frozenset((u-1,v-1)) for u,ns in NEIGHBOURS.items() for v in ns}
    if len(edges)!=26:raise ValueError('GRAPH_EDGES')
    for p in GENS:
        if {frozenset(p[i] for i in e) for e in edges}!=edges:raise ValueError('INVALID_AUTOMORPHISM')
    identity=tuple(range(10));found={identity};q=deque([identity])
    while q:
        p=q.popleft()
        for g in GENS:
            r=tuple(g[p[i]] for i in range(10))
            if r not in found:found.add(r);q.append(r)
    return found


def rows_for_pair(base_values,copy_i,omit_j):
    unknown=range(1024,2048);col={m:m-1024 for m in unknown};rows=[]
    def add(terms,equality,metadata):
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        const=sum((Fraction(c)*base_values[m] for m,c in full.items() if m in base_values),Fraction())
        residual={col[m]:c for m,c in full.items() if m not in base_values}
        if not residual:
            if (equality and const!=0) or (not equality and const<0):raise ValueError(('INVALID_BASE_POINT',metadata))
            return
        rows.append({'full':full,'unknown':residual,'rhs':-const,'equality':equality,'metadata':metadata})
    whole=2047
    for v in range(11):add(((whole,1),(whole^(1<<v),-1)),False,{'kind':'conditional_entropy','i':v})
    for i,j in combinations(range(11),2):
        rest=whole^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)),False,
                {'kind':'CMI','i':i,'j':j,'z':z})
            if z==0:break
            z=(z-1)&rest
    for m in unknown:add(((m,1),),False,{'kind':'entropy_nonnegative','mask':m})
    Y=FULL^(1<<copy_i)^(1<<omit_j);T=Y
    while True:
        add(((T|(1<<copy_i),1),(T|COPY,-1)),True,{'kind':'copy_marginal','conditioning_subset':T})
        if T==0:break
        T=(T-1)&Y
    add(((Y|COPY,1),(FULL,1),(FULL|COPY,-1),(Y,-1)),True,{'kind':'copy_independence'})
    return rows


def solve_pair(rows,base_values):
    starts=[];ids=[];coeff=[];lo=[];hi=[]
    for row in rows:
        starts.append(len(ids))
        for j,c in row['unknown'].items():ids.append(j);coeff.append(float(c))
        v=float(row['rhs']);lo.append(v);hi.append(v if row['equality'] else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=1024;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(1024);lp.col_lower_=np.full(1024,-highspy.kHighsInf);lp.col_upper_=np.full(1024,highspy.kHighsInf)
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32)
    lp.a_matrix_.index_=np.array(ids,dtype=np.int32);lp.a_matrix_.value_=np.array(coeff,dtype=float)
    lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',PER_COPY_SOLVE_S)
    solver.passModel(lp);t=time.monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    result={'status_float_unverified':status,'solve_elapsed_s':time.monotonic()-t,'rows':len(rows)}
    if status!='Infeasible':return result
    status_ray,exists,ray=solver.getDualRay();result.update({'dual_ray_status':str(status_ray),'dual_ray_exists':bool(exists)})
    if not exists:return result
    active=[i for i,x in enumerate(ray) if abs(float(x))>1e-8]
    result['float_ray_rows']=len(active)
    z3=Solver();z3.set(timeout=Z3_MS);variables=[Real(f'y_{i}') for i in range(len(active))]
    for i,index in enumerate(active):
        if not rows[index]['equality']:z3.add(variables[i]>=0)
    used=sorted({c for index in active for c in rows[index]['unknown']})
    for c in used:z3.add(Sum([variables[i]*rows[index]['unknown'].get(c,0) for i,index in enumerate(active)])==0)
    z3.add(Sum([variables[i]*str(rows[index]['rhs']) for i,index in enumerate(active)])>=1)
    exact_status=z3.check();result['rational_multiplier_status']=str(exact_status)
    if exact_status!=sat:return result
    m=z3.model();weights=[Fraction(m.eval(v,model_completion=True).as_fraction()) for v in variables]
    accum={};selected=[]
    for index,w in zip(active,weights):
        if not w:continue
        row=rows[index]
        if not row['equality'] and w<0:raise ValueError('NEGATIVE_MULTIPLIER')
        for x,c in row['full'].items():accum[x]=accum.get(x,Fraction())+w*c
        selected.append({'weight':str(w),'equality':row['equality'],'metadata':row['metadata'],
                         'terms':[[x,c] for x,c in sorted(row['full'].items())]})
    accum={x:v for x,v in accum.items() if v}
    if any(x not in base_values for x in accum):raise ValueError('UNCANCELLED_COPY')
    value=sum((base_values[x]*v for x,v in accum.items()),Fraction())
    if value>=0:raise ValueError(('NONNEGATIVE_EVALUATION',str(value)))
    result['exact_separator']={'selected_rows':selected,'base_coefficients':[[x,str(c)] for x,c in sorted(accum.items())],
                               'base_value':str(value),'valid_signs_and_copy_cancellation':True}
    return result


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    point=json.loads(raw);base_values={sum(1<<BASE.index(v) for v in x['entropy_variables']):Fraction(x['value'])
                                      for x in point['primal_values'] if set(x['entropy_variables'])<=set(BASE)}
    if len(base_values)!=1023:raise ValueError('BASE_COUNT')
    base_values[0]=Fraction(0);G=group();pairs={(i,j) for i in range(10) for j in range(10) if i!=j};orbits=[]
    while pairs:
        p=min(pairs);orbit={(g[p[0]],g[p[1]]) for g in G};pairs-=orbit;orbits.append(sorted(orbit))
    existing=next(o for o in orbits if (1,2) in o)
    reps=[o[0] for o in orbits if o!=existing]
    records=[];found=None
    for copy_i,omit_j in reps:
        if time.monotonic()-started>MAX_WALL_S:break
        rows=rows_for_pair(base_values,copy_i,omit_j);result=solve_pair(rows,base_values)
        result.update({'copied_vertex_one_based':copy_i+1,'omitted_vertex_one_based':omit_j+1})
        records.append({k:v for k,v in result.items() if k!='exact_separator'})
        if 'exact_separator' in result:
            found=result;break
    out={'input_sha256':EXPECTED,'automorphism_group_size':len(G),'ordered_pair_orbit_count':len(orbits),
         'source_copy_orbit_excluded':[list(x) for x in existing],
         'other_orbit_representatives':[[i+1,j+1] for i,j in reps],
         'examined':records,'exact_separator':found,'elapsed_s':time.monotonic()-started,
         'limits':'Only the given base profile and selected one-copy structures. A found exact inequality needs independent row/protocol verification and a separate R-minus dual certificate; no global bound follows from solver statuses.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exact_separator'},indent=2))
    if found:print('EXACT_SEPARATOR pair',found['copied_vertex_one_based'],found['omitted_vertex_one_based'],
                   'rows',len(found['exact_separator']['selected_rows']),'base_value',found['exact_separator']['base_value'])


if __name__=='__main__':main()
