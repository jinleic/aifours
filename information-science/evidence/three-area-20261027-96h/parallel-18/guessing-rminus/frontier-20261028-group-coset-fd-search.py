#!/usr/bin/env python3
"""Bounded group-coset FD-law proposals; all incumbent checks are integer exact.

For X_i=gH_i, the graph FD is intersection of neighbor subgroups <= H_i.
Strict entropy imbalance is (product |H_i|)^2 > |G|^17 |intersection H_i|^3.
Floating MIP objectives/statuses are search guidance, not impossibility proofs.
"""
from collections import deque
from itertools import permutations
from math import log,prod
from pathlib import Path
from time import monotonic
import json,sys
import numpy as np

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-highspy'))
import highspy
OUT=ROOT/'frontier-20261028-group-coset-fd-search-result.json'
N=((1,2,3,4,5,6),(0,2,6,8,9),(0,1,3,7,8),(0,2,4,7,9),
   (0,3,5,8,9),(0,4,6,7,8),(0,1,5,7,9),(2,3,5,6,8,9),
   (1,2,4,5,7),(1,3,4,6,7))
CASE_SECONDS=4.


def group(n):
    elements=list(permutations(range(n)));identity=tuple(range(n))
    elements.remove(identity);elements.insert(0,identity);index={p:i for i,p in enumerate(elements)}
    table=[[index[tuple(p[q[i]] for i in range(n))] for q in elements] for p in elements]
    if any(table[0][i]!=i or table[i][0]!=i for i in range(len(elements))):raise ValueError('IDENTITY')
    return elements,table


def generated(mask,g,table):
    known=[i for i in range(len(table)) if mask>>i&1];queue=deque([])
    if not mask>>g&1:mask|=1<<g;known.append(g);queue.append(g)
    while queue:
        x=queue.popleft()
        for y in tuple(known):
            for z in (table[x][y],table[y][x]):
                if not mask>>z&1:mask|=1<<z;known.append(z);queue.append(z)
    return mask


def subgroups(table):
    seen={1};queue=deque([1]);n=len(table)
    while queue:
        H=queue.popleft()
        for g in range(n):
            if not H>>g&1:
                K=generated(H,g,table)
                if K not in seen:seen.add(K);queue.append(K)
    out=sorted(seen,key=lambda x:(x.bit_count(),x))
    for H in out:
        bits=[i for i in range(n) if H>>i&1]
        if not H&1 or any(not H>>table[i][j]&1 for i in bits for j in bits):raise ValueError('SUBGROUP_CLOSURE')
    return out


def build(n,subgroups):
    ns=len(subgroups);nc=10*ns+n;members=[[j for j,H in enumerate(subgroups) if H>>g&1] for g in range(n)]
    starts=[];inds=[];vals=[];lo=[];hi=[]
    def row(terms,lower,upper):
        starts.append(len(inds))
        for k,v in sorted(terms.items()):
            if v:inds.append(k);vals.append(float(v))
        lo.append(float(lower));hi.append(float(upper))
    for i in range(10):row({i*ns+j:1 for j in range(ns)},1,1)
    for i,neighbors in enumerate(N):
        for g in range(n):
            d={i*ns+j:-1 for j in members[g]}
            for v in neighbors:
                for j in members[g]:d[v*ns+j]=1
            row(d,-highspy.kHighsInf,len(neighbors)-1)
    for g in range(n):
        for i in range(10):
            d={10*ns+g:1};d.update({i*ns+j:-1 for j in members[g]});row(d,-highspy.kHighsInf,0)
        d={10*ns+g:-1}
        for i in range(10):
            for j in members[g]:d[i*ns+j]=1
        row(d,-highspy.kHighsInf,9)
    row({10*ns+g:1 for g in range(n)},0,0)  # filled per case
    lp=highspy.HighsLp();lp.num_col_,lp.num_row_=nc,len(starts)
    lp.col_cost_=np.array([log(H.bit_count()) for _ in range(10) for H in subgroups]+[0.]*n)
    lp.col_lower_=np.zeros(nc);lp.col_upper_=np.ones(nc);lp.integrality_=[highspy.HighsVarType.kInteger]*nc
    lp.row_lower_,lp.row_upper_=np.array(lo),np.array(hi)
    lp.a_matrix_.format_=highspy.MatrixFormat.kRowwise
    lp.a_matrix_.start_=np.array(starts+[len(inds)],dtype=np.int32);lp.a_matrix_.index_=np.array(inds,dtype=np.int32)
    lp.a_matrix_.value_=np.array(vals,dtype=float);lp.sense_=highspy.ObjSense.kMaximize
    return lp


def exact_verify(indices,H,n):
    selected=[H[i] for i in indices];intersection=(1<<n)-1
    for S in selected:intersection&=S
    for i,neighbors in enumerate(N):
        meet=(1<<n)-1
        for j in neighbors:meet&=selected[j]
        if meet&~selected[i]:raise ValueError(('FD',i))
    sizes=[S.bit_count() for S in selected];k=intersection.bit_count()
    left=prod(sizes)**2;right=n**17*k**3
    return {'subgroup_indices':indices,'subgroup_orders':sizes,'intersection_order':k,'left_integer':str(left),
            'right_integer':str(right),'strict_gain_witness':left>right}


def main():
    start=monotonic();results=[];witness=None
    for degree in (3,4):
        elements,table=group(degree);H=subgroups(table);n=len(elements)
        expected={3:6,4:30}[degree]
        if len(H)!=expected:raise ValueError(('SUBGROUP_COUNT',degree,len(H)))
        lp=build(n,H)
        for k in sorted({h.bit_count() for h in H}):
            if k==n:continue
            lp.row_lower_[-1]=k;lp.row_upper_[-1]=k
            solver=highspy.Highs();solver.silent();solver.setOptionValue('threads',1);solver.setOptionValue('time_limit',CASE_SECONDS)
            solver.passModel(lp);case_start=monotonic();solver.run();solution=solver.getSolution()
            entry={'degree':degree,'group_order':n,'subgroup_count':len(H),'fixed_intersection_order':k,
                   'status_float_unverified':solver.modelStatusToString(solver.getModelStatus()),'elapsed_seconds':monotonic()-case_start}
            if solution.value_valid:
                ids=[]
                for i in range(10):
                    chosen=[j for j in range(len(H)) if solution.col_value[i*len(H)+j]>.5]
                    if len(chosen)!=1:raise ValueError('ONEHOT')
                    ids.append(chosen[0])
                checked=exact_verify(ids,H,n)
                if checked['intersection_order']!=k:raise ValueError('INTERSECTION')
                entry['exact_incumbent']=checked
                if checked['strict_gain_witness']:
                    witness={'degree':degree,'elements':elements,'subgroup_masks':[str(H[j]) for j in ids],**checked};results.append(entry);break
            results.append(entry)
        if witness:break
    out={'cases':results,'strict_gain_witness':witness,'per_case_time_limit_seconds':CASE_SECONDS,'elapsed_seconds':monotonic()-start,
         'limits':'Bounded MIP proposals over S3 and S4; numerical statuses are not exact nonexistence proofs. A strict integer incumbent needs independent original-graph and group verification.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
