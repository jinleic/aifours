#!/usr/bin/env python3
"""Independent gap-sensitive AP/e0 audit, including literal Doubling stretches."""
import argparse
from collections import Counter
import hashlib
import itertools
import json


def product(w,indices,p):
    x,e=0,0
    for i in indices:
        y,f=w[i]
        x=(x+((-1 if e else 1)*y))%p
        e ^= f
    return x,e


def cyclic(w):
    refs=[i for i,(_,e) in enumerate(w) if e]
    F=len(refs)
    gaps=[];boundary=[]
    for k,i in enumerate(refs):
        j=refs[(k+1)%F]
        gap=w[i+1:j] if k+1<F else w[i+1:]+w[:j]
        gaps.append(gap)
        boundary.append(bool(gap) or w[i][0]!=w[j][0])
    if not any(boundary):raise ValueError('CYCLE_NO_BOUNDARY')
    start=(next(k for k,b in enumerate(boundary) if b)+1)%F
    runs=[]
    for t in range(F):
        k=(start+t)%F
        if t==0 or boundary[(k-1)%F]:runs.append([w[refs[k]][0],1])
        else:runs[-1][1]+=1
    G=[set() for _ in refs]
    for k,b in enumerate(boundary):
        if b:G[k].add((k+1)%F);G[(k+1)%F].add(k)
    seen=set();components=[]
    for q in range(F):
        if q in seen:continue
        todo=[q];component=set()
        while todo:
            v=todo.pop()
            if v in component:continue
            component.add(v);todo.extend(G[v]-component)
        seen|=component
        if len(component)>1 and sum(len(G[v])==1 for v in component)!=2:
            raise ValueError('RAW_GRAPH_CYCLE')
        components.append(len(component))
    return refs,gaps,runs,sorted(components)


def projection_runs(w):
    vals=[x for x,e in w if e];F=len(vals)
    start=next(i for i in range(F) if vals[i]!=vals[(i-1)%F])
    runs=[]
    for k in range(F):
        y=vals[(start+k)%F]
        if not runs or runs[-1][0]!=y:runs.append([y,1])
        else:runs[-1][1]+=1
    return runs


def audit_doubling(w,p):
    refs,gaps_after,_,_=cyclic(w);F=len(refs);b=(p-1)//2
    # Index gap t BEFORE reflection t, as in the literal source.
    gaps=[gaps_after[(t-1)%F] for t in range(F)]
    beta=[];E=[];Z=[]
    for t,i in enumerate(refs):
        prev=refs[(t-1)%F];gap=gaps[t]
        diff=(w[i][0]-w[prev][0])%p
        beta.append((w[prev][0]-w[i][0]-sum(x for x,e in gap))%p)
        E.append(bool(gap) and diff==0)
        Z.append(not gap and diff!=0)
    if sum(E)!=2 or sum(Z)!=1:raise ValueError('GAP_TYPE_INVARIANT')
    tested=eligible=zeroalgebra=0
    for start in range(F):
        for j in range((p-1)//2+1):
            tested+=1
            P=[(start+2*k)%F for k in range(j+1)]
            M=[(start+2*k+1)%F for k in range(j)]
            ec=sum(E[t] for t in M);zc=sum(Z[t] for t in M)
            need=p-2*j-sum(len(gaps[t]) for t in M)
            algebra=(sum(beta[t] for t in M)+need*b)%p
            if algebra!=(ec+j-zc)%p:raise ValueError('DOUBLING_SIMPLIFICATION')
            if algebra==0:
                zeroalgebra+=1
                if not ((j==0 and ec==0 and zc==0) or (j==1 and ec==0 and zc==1)):
                    raise ValueError('DOUBLING_CASE_CLASSIFICATION')
            available=sum(len(gaps[t]) for t in P)
            if 0<=need<=available:
                eligible+=1
                if algebra==0:raise ValueError('OLD_DOUBLING_CERTIFICATE')
    return {'all_stretch_starts_and_j_checked':tested,'count_eligible':eligible,
            'algebra_zero_but_count_ineligible':zeroalgebra}


def check(case):
    p=case['p'];w=case['word'];b=(p-1)//2
    refs,gaps,runs,comps=cyclic(w)
    if len(w)!=4*p-1 or len(refs)!=3*p-2 or any(len(g)>1 for g in gaps) or sum(not e for _,e in w)!=p+1:
        raise ValueError('ORIGINAL_COUNTS')
    if any(x!=b for x,e in w if not e):raise ValueError('ROTATION_VALUES')
    if (sum(n%2 for _,n in runs),sum(n%2==0 for _,n in runs))!=(p+2,0):raise ValueError('ACTUAL_BLOCKS')
    proj=projection_runs(w)
    if len(proj)!=p or any(n%2==0 for _,n in proj):raise ValueError('PROJECTED_ODD_RUNS')
    labels=[y for y,_ in proj]
    if any((labels[(i+1)%p]-labels[i])%p!=1 for i in range(p)):
        raise ValueError('PROJECTED_ARITHMETIC_ORDER')
    nu=sum(n//2 for n in comps)
    if comps!=sorted([p+2,2]+[1]*(2*p-6)) or nu!=(p+3)//2 or nu>p-4:
        raise ValueError('RAW_GRAPH')
    if max(Counter(w[i][0] for i in refs).values())>=2*p-1:raise ValueError('SEL_COUNT')
    # Enumerate all nonempty even subsets of projected AP run labels; a
    # 2p-reflection choice cannot activate zero runs since H_proj=p-1.
    active=0
    for mask in range(1,1<<p):
        chosen=[j for j in range(p) if mask>>j&1]
        if len(chosen)%2:continue
        exponent=sum((1 if k%2==0 else -1)*labels[j] for k,j in enumerate(chosen))%p
        if exponent==0:raise ValueError('REF_ARITHMETIC_RUNS')
        active+=1
    deletion=[]
    for i in refs:
        _,_,rr,_=cyclic(w[:i]+w[i+1:])
        o=sum(n%2 for _,n in rr);e=sum(n%2==0 for _,n in rr);kappa=p-1-sum(n//2 for _,n in rr)
        deletion.append((o,e,kappa))
    if any(o<=p or kappa>=2 for o,e,kappa in deletion):raise ValueError('DELETION_CALLER')
    one=[i for i,(x,e) in enumerate(w) if e and x==1]
    two=[i for i,(x,e) in enumerate(w) if e and x==2]
    selector=sorted([0,1,2,3]+one[:2*p-6]+two[:2])
    if len(selector)!=2*p or product(w,selector,p)!=(0,0):raise ValueError('MIXED_SELECTOR')
    moved=[x[:] for x in w]
    rho=moved.pop(1)
    at=next(i for i in range(len(moved)-1) if moved[i]==[1,1] and moved[i+1]==[2,1])
    moved.insert(at+1,rho)
    _,_,newruns,_=cyclic(moved)
    if (sum(n%2 for _,n in newruns),sum(n%2==0 for _,n in newruns))!=(p,1):
        raise ValueError('OCCUPIED_EQUAL_GAP_CONTROL')
    return {'p':p,'actual_odd':p+2,'actual_even':0,'projected_odd':len(proj),
            'raw_matching':nu,'even_active_run_subsets_checked':active,
            'all_deletion_profiles':{str(k):v for k,v in Counter(deletion).items()},
            'old_doubling':audit_doubling(w,p),'selector':selector,
            'occupied_equal_gap_move_control':'detected actual o/e change'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as src:raw=src.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_AP_ODD_RUN_E0_CANDIDATES':raise ValueError('INPUT_KIND')
    result={'result':'PASS_INDEPENDENT_AP_E0_AUDIT','input_sha256':hashlib.sha256(raw).hexdigest(),
            'cases':[check(c) for c in data['cases']],
            'scope':'literal structural, REF and named caller checks on two words; IPGEN/complete OLD unreviewed'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
