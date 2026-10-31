#!/usr/bin/env python3
"""Independent saved-word audit, importing no constructor/checker code."""
import argparse
from collections import Counter
from itertools import combinations
import hashlib
import json


def multiply(w,indices,p):
    out=(0,1)  # affine map x -> sign*x + offset; out=(offset,sign)
    for i in indices:
        y,b=w[i];off,sign=out
        out=((off+sign*y)%p,sign*(-1 if b else 1))
    return out


def run_parity_ref(runs,p):
    # exact F=3p-2 target2p test using run parities rather than element DP
    odd=sum(len(r)%2 for r in runs);need=odd-p+2
    dp={(0,0,0)}
    for r in runs:
        y=r[0];o=len(r)%2;new=set(dp)
        for k,x,score in dp:
            if k<2*p:new.add((k+1,(x+(y if k%2==0 else -y))%p,score+(1 if o else -1)))
        dp=new
    return any(k%2==0 and x==0 and score>=need for k,x,score in dp)


def check(case):
    p=case['p'];w=case['word'];N=len(w);sel=case['selector']
    if N!=4*p-1 or len(sel)!=2*p or sel!=sorted(set(sel)):raise ValueError('COUNTS_OR_SELECTION')
    if any(len(z)!=2 or not 0<=z[0]<p or z[1] not in (0,1) for z in w):raise ValueError('ENCODING')
    refs=[i for i,z in enumerate(w) if z[1]];F=len(refs)
    if F!=3*p-2 or sum(z[1]==0 for z in w)!=p+1:raise ValueError('COUNTS')
    if any(z[0]==0 or not w[(i+1)%N][1] for i,z in enumerate(w) if not z[1]):raise ValueError('ROTATION_OR_GAP')
    if multiply(w,sel,p)!=(0,1):raise ValueError('ACTUAL_PRODUCT')
    vals=[w[i][0] for i in refs];start=next(i for i in range(F) if vals[i]!=vals[i-1]);runs=[]
    for i in range(F):
        y=vals[(start+i)%F]
        if not runs or runs[-1][-1]!=y:runs.append([y])
        else:runs[-1].append(y)
    if (sum(len(r)%2 for r in runs),sum(len(r)%2==0 for r in runs))!=(p+4,2):raise ValueError('PROJECTION')
    if run_parity_ref(runs,p):raise ValueError('REF_FOUND')
    # path-component matching formula, not the producer's cycle DP
    edge=[vals[i]!=vals[(i+1)%F] or (refs[(i+1)%F]-refs[i])%N!=1 for i in range(F)]
    absent=next((i for i,x in enumerate(edge) if not x),None)
    if absent is None:raise ValueError('EXPECTED_PATHS')
    sizes=[];size=1
    for j in range(F-1):
        i=(absent+1+j)%F
        if edge[i]:size+=1
        else:sizes.append(size);size=1
    sizes.append(size)
    nu=sum(n//2 for n in sizes)
    if nu!=(p+9)//2:raise ValueError('MATCHING')
    return {'p':p,'nu':nu,'path_sizes':sorted(sizes),'ref_failure':True,'actual_identity':True}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('input');ap.add_argument('--output',required=True);args=ap.parse_args()
    with open(args.input,'rb') as f:raw=f.read()
    data=json.loads(raw);cases=[check(c) for c in data['cases']]
    # Recompute head extrema by a min/max recurrence rather than enumerating subsets.
    mn=[0]+[999]*8;mx=[0]+[-999]*8
    for n,y in enumerate([0,-1,-1,0,1,2,2,1]):
        for k in range(n,-1,-1):
            delta=y if k%2==0 else -y
            mn[k+1]=min(mn[k+1],mn[k]+delta);mx[k+1]=max(mx[k+1],mx[k]+delta)
    if any(data['head_bounds'][str(k)]!=[mn[k],mx[k]] for k in range(9)):raise ValueError('HEAD_TABLE')
    import copy
    c=copy.deepcopy(data['cases'][0]);c['selector'][1]=c['selector'][0]
    try:check(c)
    except ValueError as e:
        if str(e)!='COUNTS_OR_SELECTION':raise
    else:raise ValueError('DUPLICATE_CONTROL_SURVIVED')
    c=copy.deepcopy(data['cases'][0]);r=next(i for i in c['selector'] if not c['word'][i][1]);c['word'][r][0]=2
    try:check(c)
    except ValueError as e:
        if str(e)!='ACTUAL_PRODUCT':raise
    else:raise ValueError('PRODUCT_CONTROL_SURVIVED')
    result={'result':'PASS_INDEPENDENT_HIGH_SURPLUS_FAMILY','input_sha256':hashlib.sha256(raw).hexdigest(),
            'cases':cases,'head_table_recurrence_agrees':True,
            'controls':['DUPLICATE_SELECTION','ALTERED_SELECTED_ROTATION'],
            'scope':'no GEN/IPGEN or full L_RES classification; no disjoint proof review'}
    with open(args.output,'x',encoding='utf-8') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
    print(json.dumps({'result':result['result'],'primes':[c['p'] for c in cases],'controls':result['controls']},sort_keys=True))


if __name__=='__main__':main()
