#!/usr/bin/env python3
"""Screen three-variable-copy structures after grouping the copied triple into one tuple.

This valid weaker representation has nine abstract variables rather than thirteen.
Any exact separator is independent
of the numerical solver, but needs a separate checker and target-bound dual.
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
from z3 import Real,Solver,Sum,sat
spec=spec_from_file_location('pair',ROOT/'frontier-20261028-two-copy-orbit-search.py')
mod=module_from_spec(spec);spec.loader.exec_module(mod)
INPUT=mod.INPUT;EXPECTED=mod.EXPECTED
OUTPUT=ROOT/'frontier-20261028-compressed-triple-copy-search-result.json'
MAX_WALL_S=90.0
MAX_ORBITS=150
SOLVE_SECONDS=0.5
Z3_MS=10000


def make_abstract_base(base,triple):
    groups=[sum(1<<i for i in triple)]+[1<<i for i in range(10) if i not in triple]
    lookup={}
    for local in range(256):
        original=0
        for i,g in enumerate(groups):
            if local&(1<<i):original|=g
        lookup[local]=base[original]
    return groups,lookup


def make_rows(h,omitted_index):
    rows=[];known=0;base_full=255;copy=256;allmask=511
    def add(terms,equality,metadata):
        nonlocal known
        vec={}
        for m,c in terms:
            if m:vec[m]=vec.get(m,0)+c
        vec={m:c for m,c in vec.items() if c}
        const=sum((Fraction(c)*h[m] for m,c in vec.items() if m in h),Fraction())
        unknown={m-256:c for m,c in vec.items() if m not in h}
        if not unknown:
            known+=1
            if (equality and const) or (not equality and const<0):raise ValueError(('INVALID_BASE',metadata))
            return
        rows.append({'full':vec,'unknown':unknown,'rhs':-const,'equality':equality,'metadata':metadata})
    for i in range(9):add(((allmask,1),(allmask^(1<<i),-1)),False,{'kind':'conditional_entropy','i':i})
    for i,j in combinations(range(9),2):
        rest=allmask^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)),False,
                {'kind':'CMI','i':i,'j':j,'z':z})
            if not z:break
            z=(z-1)&rest
    for m in range(256,512):add(((m,1),),False,{'kind':'entropy_nonnegative','mask':m})
    Y=base_full^1^(1<<omitted_index);T=Y
    while True:
        add(((T|1,1),(T|copy,-1)),True,{'kind':'tuple_copy_marginal','conditioning_subset':T})
        if T==0:break
        T=(T-1)&Y
    add(((Y|copy,1),(base_full,1),(base_full|copy,-1),(Y,-1)),True,{'kind':'tuple_copy_independence'})
    return rows,known


def solve(rows,h,groups):
    starts=[];inds=[];vals=[];lo=[];hi=[]
    for row in rows:
        starts.append(len(inds))
        for j,c in row['unknown'].items():inds.append(j);vals.append(float(c))
        rhs=float(row['rhs']);lo.append(rhs);hi.append(rhs if row['equality'] else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=256;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(256);lp.col_lower_=np.full(256,-highspy.kHighsInf);lp.col_upper_=np.full(256,highspy.kHighsInf)
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32);lp.a_matrix_.index_=np.array(inds,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float);lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',SOLVE_SECONDS)
    solver.passModel(lp);t=time.monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    result={'status_float_unverified':status,'solve_elapsed_s':time.monotonic()-t,'rows':len(rows)}
    if status!='Infeasible':return result
    state,exists,ray=solver.getDualRay();result.update({'dual_ray_status':str(state),'dual_ray_exists':bool(exists)})
    if not exists:return result
    active=[i for i,x in enumerate(ray) if abs(float(x))>1e-8];result['float_ray_rows']=len(active)
    z=Solver();z.set(timeout=Z3_MS);q=[Real(f'q_{j}') for j in range(len(active))]
    for j,index in enumerate(active):
        if not rows[index]['equality']:z.add(q[j]>=0)
    used=sorted({c for index in active for c in rows[index]['unknown']})
    for c in used:z.add(Sum([q[j]*rows[index]['unknown'].get(c,0) for j,index in enumerate(active)])==0)
    z.add(Sum([q[j]*str(rows[index]['rhs']) for j,index in enumerate(active)])>=1)
    status2=z.check();result['rational_multiplier_status']=str(status2)
    if status2!=sat:return result
    model=z.model();weights=[Fraction(model.eval(v,model_completion=True).as_fraction()) for v in q]
    acc={};selected=[]
    for index,w in zip(active,weights):
        if not w:continue
        row=rows[index]
        if not row['equality'] and w<0:raise ValueError('NEGATIVE_MULTIPLIER')
        for m,c in row['full'].items():acc[m]=acc.get(m,Fraction())+w*c
        selected.append({'weight':str(w),'equality':row['equality'],'metadata':row['metadata'],
                         'terms':[[m,c] for m,c in sorted(row['full'].items())]})
    acc={m:c for m,c in acc.items() if c}
    if any(m not in h for m in acc):raise ValueError('UNCANCELLED_COPY')
    value=sum((h[m]*c for m,c in acc.items()),Fraction())
    if value>=0:raise ValueError('NONNEGATIVE_EVALUATION')
    original={}
    for local,coefficient in acc.items():
        m=0
        for i,g in enumerate(groups):
            if local&(1<<i):m|=g
        original[m]=original.get(m,Fraction())+coefficient
    result['exact_separator']={'selected_rows':selected,
        'local_base_coefficients':[[m,str(c)] for m,c in sorted(acc.items())],
        'original_base_coefficients':[[m,str(c)] for m,c in sorted(original.items()) if c],
        'base_value':str(value),'valid_signs_and_copy_cancellation':True}
    return result


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    data=json.loads(raw);B=mod.BASE
    original={sum(1<<B.index(v) for v in x['entropy_variables']):Fraction(x['value'])
              for x in data['primal_values'] if set(x['entropy_variables'])<=set(B)}
    if len(original)!=1023:raise ValueError('BASE_COUNT')
    original[0]=Fraction(0);G=mod.group()
    choices={(tuple(T),k) for T in combinations(range(10),3) for k in range(10) if k not in T}
    orbits=[]
    while choices:
        triple,k=min(choices);o={(tuple(sorted(p[i] for i in triple)),p[k]) for p in G}
        choices-=o;orbits.append(sorted(o))
    reps=[o[0] for o in orbits];records=[];found=None
    for triple,omitted in reps[:MAX_ORBITS]:
        if time.monotonic()-start>MAX_WALL_S:break
        groups,h=make_abstract_base(original,triple);omit_index=groups.index(1<<omitted)
        rows,known=make_rows(h,omit_index);result=solve(rows,h,groups)
        result.update({'copied_triple_one_based':[i+1 for i in triple],
                       'omitted_one_based':omitted+1,'abstract_group_masks':groups,'known_only_shannon_rows':known})
        records.append({k:v for k,v in result.items() if k!='exact_separator'})
        if 'exact_separator' in result:found=result;break
    out={'point_sha256':EXPECTED,'group_size':len(G),'triple_omit_orbits':len(orbits),
         'examined':records,'exact_separator':found,'elapsed_s':time.monotonic()-start,
         'limits':'Compressed-tuple one-copy LP is a relaxation of each full three-variable-copy structure. Feasibility is numerical only; a found exact separator needs an independent mathematical checker and graph upper dual.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exact_separator'},indent=2))
    if found:print('EXACT_SEPARATOR',found['copied_triple_one_based'],found['omitted_one_based'],
                   'rows',len(found['exact_separator']['selected_rows']),'base_value',found['exact_separator']['base_value'])


if __name__=='__main__':main()
