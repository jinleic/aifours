#!/usr/bin/env python3
"""Search h* for single-variable copy cuts with singleton conditioning groups.

A=one original variable; Y=4 or 5 original singletons; R=the remaining tuple.
Copy A over Y independently of (A,R) conditional on Y. Full Shannon rows are
imposed on abstract variables A,Y_1,...,Y_k,R,A'. Floating feasibility is only
exploratory; an infeasible candidate gets an exact rational Farkas attempt.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
BASE=('frontier-20261028-separator-bound-primal.json','aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651')
GROUP=('frontier-20261028-two-copy-orbit-search.py','48a5d353fad17d0ce999c657d0d1a726b2c706d4920f327912b4135e01e599c1')
OUT=ROOT/'frontier-20261028-single-copy-split-search-result.json'
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
from z3 import Real,Solver,Sum,sat


def pin(item):
    raw=(ROOT/item[0]).read_bytes()
    if sha256(raw).hexdigest()!=item[1]:raise ValueError(('HASH',item[0]))
    return raw


def group():
    raw=pin(GROUP);spec=spec_from_file_location('copygroup',ROOT/GROUP[0]);mod=module_from_spec(spec);spec.loader.exec_module(mod);return mod.group()


def rows_for(base,u,Y):
    rem=[v for v in range(10) if v!=u and v not in Y]
    groups=[1<<u]+[1<<v for v in Y]+[sum(1<<v for v in rem)]
    n=len(groups);bc=(1<<n)-1;cp=1<<n;full=(cp<<1)-1;h={}
    for m in range(cp):
        original=0
        for i,g in enumerate(groups):
            if m>>i&1:original|=g
        h[m]=base[original]
    rows=[];known=0
    def add(terms,equality,meta):
        nonlocal known
        d={}
        for m,c in terms:
            if m:d[m]=d.get(m,0)+c
        d={m:c for m,c in d.items() if c};constant=sum((Fraction(c)*h[m] for m,c in d.items() if m in h),Fraction())
        unknown={m-cp:c for m,c in d.items() if m not in h}
        if not unknown:
            known+=1
            if (equality and constant) or (not equality and constant<0):raise ValueError(('BASE',meta))
        else:rows.append({'full':d,'unknown':unknown,'rhs':-constant,'equality':equality,'metadata':meta})
    total=n+1
    for i in range(total):add(((full,1),(full^(1<<i),-1)),False,{'kind':'conditional_entropy','i':i})
    for i,j in combinations(range(total),2):
        rest=full^(1<<i)^(1<<j);z=rest
        while True:
            add(((z|1<<i,1),(z|1<<j,1),(z|1<<i|1<<j,-1),(z,-1)),False,{'kind':'CMI','i':i,'j':j,'z':z})
            if not z:break
            z=(z-1)&rest
    for m in range(cp,2*cp):add(((m,1),),False,{'kind':'entropy_nonnegative','mask':m})
    ym=sum(1<<i for i in range(1,1+len(Y)));z=ym
    while True:
        add(((z|1,1),(z|cp,-1)),True,{'kind':'copy_marginal','conditioning_subset':z})
        if not z:break
        z=(z-1)&ym
    add(((ym|cp,1),(bc,1),(bc|cp,-1),(ym,-1)),True,{'kind':'copy_independence'})
    return groups,h,rows,known,cp


def solve(groups,h,rows,cp):
    starts=[];inds=[];vals=[];lo=[];hi=[]
    for row in rows:
        starts.append(len(inds))
        for j,c in row['unknown'].items():inds.append(j);vals.append(float(c))
        b=float(row['rhs']);lo.append(b);hi.append(b if row['equality'] else highspy.kHighsInf)
    lp=highspy.HighsLp();lp.num_col_=cp;lp.num_row_=len(rows);lp.col_cost_=np.zeros(cp)
    lp.col_lower_=np.full(cp,-highspy.kHighsInf);lp.col_upper_=np.full(cp,highspy.kHighsInf)
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi);lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],np.int32);lp.a_matrix_.index_=np.array(inds,np.int32);lp.a_matrix_.value_=np.array(vals,float)
    solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',.5);solver.passModel(lp);solver.run()
    result={'status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),'rows':len(rows)}
    if result['status_float_unverified']!='Infeasible':return result
    status,exists,ray=solver.getDualRay();result['dual_ray_exists']=bool(exists)
    if not exists:return result
    active=[i for i,x in enumerate(ray) if abs(float(x))>1e-8];z=Solver();z.set(timeout=10000);q=[Real(f'q_{j}') for j in range(len(active))]
    for j,idx in enumerate(active):
        if not rows[idx]['equality']:z.add(q[j]>=0)
    used=sorted({c for idx in active for c in rows[idx]['unknown']})
    for col in used:z.add(Sum([q[j]*rows[idx]['unknown'].get(col,0) for j,idx in enumerate(active)])==0)
    z.add(Sum([q[j]*str(rows[idx]['rhs']) for j,idx in enumerate(active)])>=1)
    zs=z.check();result['exactifier_status']=str(zs)
    if zs!=sat:return result
    model=z.model();weights=[Fraction(model.eval(v,model_completion=True).as_fraction()) for v in q];acc={};selected=[]
    for idx,w in zip(active,weights):
        if not w:continue
        row=rows[idx]
        if not row['equality'] and w<0:raise ValueError('NEGATIVE')
        for mask,c in row['full'].items():acc[mask]=acc.get(mask,Fraction())+w*c
        selected.append({'weight':str(w),'equality':row['equality'],'metadata':row['metadata'],'terms':[[m,c] for m,c in sorted(row['full'].items())]})
    acc={m:c for m,c in acc.items() if c}
    if any(m not in h for m in acc):raise ValueError('COPY_NOT_CANCELLED')
    value=sum((h[m]*c for m,c in acc.items()),Fraction())
    if value>=0:raise ValueError('NOT_SEPARATING')
    mapped={}
    for local,c in acc.items():
        original=0
        for i,g in enumerate(groups):
            if local>>i&1:original|=g
        mapped[original]=mapped.get(original,Fraction())+c
    result['exact_separator']={'selected_rows':selected,'abstract_base_coefficients':[[m,str(c)] for m,c in sorted(acc.items())],
                               'original_base_coefficients':[[m,str(c)] for m,c in sorted(mapped.items()) if c],
                               'base_value':str(value),'valid_signs_and_copy_cancellation':True}
    return result


def main():
    start=monotonic();raw=pin(BASE);data=json.loads(raw);base={0:Fraction(0)}
    for e in data['primal_values']:
        labs=e['entropy_variables']
        if not set(labs)<=set('abcdefghij'):continue
        m=sum(1<<'abcdefghij'.index(v) for v in labs);base[m]=Fraction(e['value'])
    if len(base)!=1024:raise ValueError('BASE_SIZE')
    G=group();allreps=[];orbit_counts={}
    for k in (4,5):
        remaining={(u,tuple(Y)) for u in range(10) for Y in combinations([v for v in range(10) if v!=u],k)};orbits=[]
        while remaining:
            u,Y=min(remaining);orb={(p[u],tuple(sorted(p[v] for v in Y))) for p in G};remaining-=orb;orbits.append(sorted(orb))
        orbit_counts[str(k)]=len(orbits);allreps.extend((k,*o[0]) for o in orbits)
    records=[];found=None
    for k,u,Y in allreps:
        if monotonic()-start>90:break
        groups,h,rows,known,cp=rows_for(base,u,Y);result=solve(groups,h,rows,cp)
        result.update({'copy_vertex_one_based':u+1,'conditioning_vertices_one_based':[v+1 for v in Y],
                       'remainder_tuple_mask':groups[-1],'abstract_group_masks':groups,'known_only_rows':known})
        records.append({key:val for key,val in result.items() if key!='exact_separator'})
        if 'exact_separator' in result:found=result;break
    out={'point_sha256':BASE[1],'group_order':len(G),'orbit_counts_by_conditioning_size':orbit_counts,
         'examined':records,'exact_separator':found,'elapsed_seconds':monotonic()-start,
         'limits':'Abstract single-copy one-tuple-complement LPs. Numerical feasibility is not exact; any separator requires independent verification and a graph upper dual.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('examined','exact_separator')},indent=2))
    print('examined',len(records),'separator_found',bool(found))


if __name__=='__main__':main()
