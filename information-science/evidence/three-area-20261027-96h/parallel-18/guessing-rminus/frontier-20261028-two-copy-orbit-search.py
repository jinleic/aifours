#!/usr/bin/env python3
"""Search distinct two-variable conditional-copy structures at a base profile.

The known source pair-copy orbit is excluded. A candidate separator is accepted
only after exact rational auxiliary cancellation and a strict base evaluation;
all numerical feasibility/timeout outputs are exploratory and non-global.
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
OUTPUT=ROOT/'frontier-20261028-two-copy-orbit-search-result.json'
BASE='abcdefghij';FULL=1023;NEW=(1024,2048)
NEIGHBOURS={
 1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
 5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
 9:(2,3,5,6,8),10:(2,4,5,7,8)}
GENS=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
MAX_WALL_S=90.0
MAX_ORBITS=10
PER_COPY_SOLVE_S=7.0
Z3_MS=15000


def group():
    edges={frozenset((u-1,v-1)) for u,ns in NEIGHBOURS.items() for v in ns}
    if len(edges)!=26:raise ValueError('GRAPH_EDGES')
    for p in GENS:
        if {frozenset(p[i] for i in e) for e in edges}!=edges:raise ValueError('INVALID_AUTOMORPHISM')
    identity=tuple(range(10));seen={identity};queue=deque([identity])
    while queue:
        p=queue.popleft()
        for g in GENS:
            q=tuple(g[p[i]] for i in range(10))
            if q not in seen:seen.add(q);queue.append(q)
    return seen


def base_shannon_rows(base):
    rows=[];known_only=0
    def add(terms,meta):
        nonlocal known_only
        full={}
        for m,c in terms:
            if m:full[m]=full.get(m,0)+c
        full={m:c for m,c in full.items() if c}
        const=sum((Fraction(c)*base[m] for m,c in full.items() if m in base),Fraction())
        small={m-1024:c for m,c in full.items() if m not in base}
        if not small:
            known_only+=1
            if const<0:raise ValueError(('INVALID_BASE',meta))
            return
        rows.append({'full':full,'unknown':small,'rhs':-const,'equality':False,'metadata':meta})
    all12=4095
    for i in range(12):add(((all12,1),(all12^(1<<i),-1)),{'kind':'conditional_entropy','i':i})
    for i,j in combinations(range(12),2):
        rest=all12^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|(1<<i),1),(z|(1<<j),1),(z|(1<<i)|(1<<j),-1),(z,-1)),
                {'kind':'CMI','i':i,'j':j,'z':z})
            if not z:break
            z=(z-1)&rest
    for m in range(1024,4096):add(((m,1),),{'kind':'entropy_nonnegative','mask':m})
    return rows,known_only


def copy_rows(base,i,j,omit):
    Y=FULL^(1<<i)^(1<<j)^(1<<omit);rows=[]
    for choice in (1,2,3):
        old=((1<<i) if choice&1 else 0)|((1<<j) if choice&2 else 0)
        new=(NEW[0] if choice&1 else 0)|(NEW[1] if choice&2 else 0)
        T=Y
        while True:
            terms=((T|old,1),(T|new,-1));full={}
            for m,c in terms:full[m]=full.get(m,0)+c
            const=sum((Fraction(c)*base[m] for m,c in full.items() if m in base),Fraction())
            small={m-1024:c for m,c in full.items() if m not in base}
            rows.append({'full':full,'unknown':small,'rhs':-const,'equality':True,
                         'metadata':{'kind':'copy_marginal','old_choice':choice,'conditioning_subset':T}})
            if not T:break
            T=(T-1)&Y
    copy=NEW[0]|NEW[1]
    terms=((Y|copy,1),(FULL,1),(FULL|copy,-1),(Y,-1));full={}
    for m,c in terms:full[m]=full.get(m,0)+c
    const=sum((Fraction(c)*base[m] for m,c in full.items() if m in base),Fraction())
    small={m-1024:c for m,c in full.items() if m not in base}
    rows.append({'full':full,'unknown':small,'rhs':-const,'equality':True,'metadata':{'kind':'copy_independence'}})
    return rows


def solve(rows,base):
    starts=[];ids=[];coefs=[];lo=[];hi=[]
    for row in rows:
        starts.append(len(ids))
        for k,c in row['unknown'].items():ids.append(k);coefs.append(float(c))
        r=float(row['rhs']);lo.append(r);hi.append(r if row['equality'] else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=3072;lp.num_row_=len(rows)
    lp.col_cost_=np.zeros(3072);lp.col_lower_=np.full(3072,-highspy.kHighsInf);lp.col_upper_=np.full(3072,highspy.kHighsInf)
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(ids)],dtype=np.int32);lp.a_matrix_.index_=np.array(ids,dtype=np.int32)
    lp.a_matrix_.value_=np.array(coefs,dtype=float);lp.sense_=highspy.ObjSense.kMinimize
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',PER_COPY_SOLVE_S)
    solver.passModel(lp);t=time.monotonic();solver.run();status=solver.modelStatusToString(solver.getModelStatus())
    result={'status_float_unverified':status,'solve_elapsed_s':time.monotonic()-t,'rows':len(rows)}
    if status!='Infeasible':return result
    state,exists,ray=solver.getDualRay();result.update({'dual_ray_status':str(state),'dual_ray_exists':bool(exists)})
    if not exists:return result
    active=[i for i,x in enumerate(ray) if abs(float(x))>1e-8];result['float_ray_rows']=len(active)
    zs=Solver();zs.set(timeout=Z3_MS);y=[Real(f'y_{k}') for k in range(len(active))]
    for k,index in enumerate(active):
        if not rows[index]['equality']:zs.add(y[k]>=0)
    involved=sorted({j for index in active for j in rows[index]['unknown']})
    for j in involved:zs.add(Sum([y[k]*rows[index]['unknown'].get(j,0) for k,index in enumerate(active)])==0)
    zs.add(Sum([y[k]*str(rows[index]['rhs']) for k,index in enumerate(active)])>=1)
    st=zs.check();result['rational_multiplier_status']=str(st)
    if st!=sat:return result
    model=zs.model();weights=[Fraction(model.eval(v,model_completion=True).as_fraction()) for v in y]
    acc={};selected=[]
    for index,w in zip(active,weights):
        if not w:continue
        row=rows[index]
        if not row['equality'] and w<0:raise ValueError('NEGATIVE_MULTIPLIER')
        for m,c in row['full'].items():acc[m]=acc.get(m,Fraction())+w*c
        selected.append({'weight':str(w),'equality':row['equality'],'metadata':row['metadata'],
                         'terms':[[m,c] for m,c in sorted(row['full'].items())]})
    acc={m:c for m,c in acc.items() if c}
    if any(m not in base for m in acc):raise ValueError('UNCANCELLED_COPY')
    value=sum((base[m]*c for m,c in acc.items()),Fraction())
    if value>=0:raise ValueError(('NONNEGATIVE_EVALUATION',str(value)))
    result['exact_separator']={'selected_rows':selected,'base_coefficients':[[m,str(c)] for m,c in sorted(acc.items())],
                               'base_value':str(value),'valid_signs_and_copy_cancellation':True}
    return result


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    point=json.loads(raw);base={sum(1<<BASE.index(v) for v in x['entropy_variables']):Fraction(x['value'])
                                for x in point['primal_values'] if set(x['entropy_variables'])<=set(BASE)}
    if len(base)!=1023:raise ValueError('BASE_COUNT')
    base[0]=Fraction(0);G=group()
    triples={(tuple(sorted((i,j))),k) for i,j in combinations(range(10),2) for k in range(10) if k not in (i,j)}
    orbits=[]
    while triples:
        pair,k=min(triples);orbit={(tuple(sorted((g[pair[0]],g[pair[1]]))),g[k]) for g in G}
        triples-=orbit;orbits.append(sorted(orbit))
    source=next(o for o in orbits if ((3,4),9) in o)
    representatives=[o[0] for o in orbits if o!=source]
    fixed,known=base_shannon_rows(base);records=[];found=None
    for pair,k in representatives[:MAX_ORBITS]:
        if time.monotonic()-started>MAX_WALL_S:break
        rows=fixed+copy_rows(base,pair[0],pair[1],k)
        result=solve(rows,base)
        result.update({'copied_vertices_one_based':[pair[0]+1,pair[1]+1],'omitted_vertex_one_based':k+1})
        records.append({a:b for a,b in result.items() if a!='exact_separator'})
        if 'exact_separator' in result:found=result;break
    out={'input_sha256':EXPECTED,'group_size':len(G),'tuple_copy_orbit_count':len(orbits),
         'source_pair_copy_orbit_excluded_zero_based':source,'orbit_representatives_one_based':[[i+1,j+1,k+1] for (i,j),k in representatives],
         'planned_orbits_cap':MAX_ORBITS,'examined':records,'exact_separator':found,
         'known_base_only_shannon_rows':known,'elapsed_s':time.monotonic()-started,
         'limits':'Bounded search only; a found exact separator needs independent verifier and later graph-bound dual. Numerical feasible/infeasible/timeout statuses alone prove nothing.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exact_separator'},indent=2))
    if found:print('EXACT_SEPARATOR',found['copied_vertices_one_based'],found['omitted_vertex_one_based'],
                   'rows',len(found['exact_separator']['selected_rows']),'base_value',found['exact_separator']['base_value'])


if __name__=='__main__':main()
