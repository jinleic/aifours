#!/usr/bin/env python3
"""Independent audit of o_pi=p+2 selectors (imports no producer code).

For every word: counts, singleton cyclic gaps, o_pi=p+2; the selector's size,
distinctness, rotation count and original-order product; and an independent
re-derivation of the branch: REF iff the cyclic odd-run labels contain a zero
alternating quadruple (sequential DP); otherwise the odd-label multiset must be
{c x3} + (F_p minus c); H if the two selected rotations are the first two
occupied gaps of one projected run (sub-branch from parities and the gamma
condition); otherwise canonical spares, Case A (no spare strictly between the
selected rotations) or Case B (exactly one, a c-spare), and the loss lambda.
"""
import argparse
from collections import Counter
import copy
import hashlib
import json


def product(w,idx,p):
    x,e=0,0
    for i in idx:
        y,b=w[i];x=(x+(-y if e else y))%p;e^=b
    return x,e


def quad_zero(labels,p):
    st={(0,0)}
    for y in labels:
        nx=set(st)
        for k,x in st:
            if k<4:nx.add((k+1,(x+(y if k%2==0 else -y))%p))
        st=nx
    return (4,0) in st


def projection(w):
    N=len(w);refs=[i for i,(_,e) in enumerate(w) if e];F=len(refs)
    k0=next(k for k in range(F) if w[refs[k]][0]!=w[refs[k-1]][0]);runs=[]
    for k in range(F):
        i=refs[(k0+k)%F]
        if runs and w[runs[-1][-1]][0]==w[i][0]:runs[-1].append(i)
        else:runs.append([i])
    return runs


def segment_pieces(w,a,b):
    """Odd/even pieces of reflections strictly after a, strictly before b (cyclic)."""
    N=len(w);seq=[];k=(a+1)%N
    while k!=b:
        if w[k][1]:seq.append(k)
        k=(k+1)%N
    out=[]
    for i in seq:
        if out and w[out[-1][-1]][0]==w[i][0]:out[-1].append(i)
        else:out.append([i])
    return out


def check(case):
    p,w=case['p'],case['word'];N=len(w)
    rots=[i for i,(_,e) in enumerate(w) if not e]
    if N!=4*p-1 or len(rots)!=p+1:raise ValueError('COUNTS')
    if any(not w[(r+1)%N][1] for r in rots):raise ValueError('SINGLETON')
    runs=projection(w);runof={i:t for t,r in enumerate(runs) for i in r}
    odd=[t for t,r in enumerate(runs) if len(r)%2]
    if len(odd)!=p+2:raise ValueError('O_PI')
    sel=case['selector']
    if len(sel)!=2*p or sel!=sorted(set(sel)) or not all(0<=i<N for i in sel):raise ValueError('SELECTOR')
    if product(w,sel,p)!=(0,0):raise ValueError('PRODUCT')
    srots=[i for i in sel if not w[i][1]]
    labels=[w[runs[t][0]][0] for t in odd]
    if quad_zero(labels,p):
        if srots or case['case']!='REF':raise ValueError('BRANCH_REF')
        return 'REF'
    cnt=Counter(labels);trip=[v for v,m in cnt.items() if m==3]
    if len(trip)!=1 or len(cnt)!=p:raise ValueError('MULTISET')
    c=trip[0]
    if len(srots)!=2:raise ValueError('ROTATION_COUNT')
    # orient the two selected rotations: r1 then r2 with no other selected letter rule; try both orders
    gapsof={}
    for r in rots:gapsof.setdefault(runof[(r-1)%N],[]).append(r)
    for r1,r2 in (srots,srots[::-1]):
        t=runof[(r1-1)%N]
        if runof[(r2-1)%N]==t:
            run=runs[t];g=sorted(gapsof[t],key=lambda r:run.index((r-1)%N))
            if g[:2]!=[r1,r2]:continue
            e=w[run[0]][0];u,v=w[r1][0],w[r2][0]
            a=run.index((r1-1)%N)+1;x=run.index((r2-1)%N)+1-a;b=len(run)-a-x
            Godd=len(run)%2
            if not Godd:sub='H-i' if a%2==0 and x%2==0 else ('H-ii' if x%2 else 'H-iii')
            elif x%2==0:sub='H-ivbc'
            elif a%2==0 and b%2==0:
                others=[w[runs[q][0]][0] for q in odd if q!=t]
                sub='H-iva' if (e+u-v)%p in others else 'H-iva-gamma'
            else:sub='H-v'
            if case['case']!=sub:raise ValueError('BRANCH_H %s vs %s'%(case['case'],sub))
            return sub
    if any(len(g)>=2 for g in gapsof.values()):raise ValueError('MULTIGAP_NOT_USED')
    spare=set()
    for t in odd:
        run=runs[t]
        if t in gapsof:
            k=run.index((gapsof[t][0]-1)%N)+1;piece=run[:k] if k%2 else run[k:]
        else:piece=run
        spare.add(piece[-1])
    for r1,r2 in (srots,srots[::-1]):
        between=[i for i in spare if 0<(i-r1)%N<(r2-r1)%N]
        PX=segment_pieces(w,r1,r2);PY=segment_pieces(w,r2,r1)
        opc=sum(len(q)%2 for q in PX+PY);lam=(opc-(p+2))//2
        if not between and case['case']=='A/L%d'%lam:return case['case']
        if len(between)==1 and w[between[0]][0]==c and case['case']=='B/L%d'%lam:return case['case']
    raise ValueError('BRANCH_AB '+case['case'])


def mutate(case,edit,expected):
    c=copy.deepcopy(case);edit(c)
    try:check(c)
    except ValueError as exc:
        if str(exc).startswith(expected):return expected
        raise ValueError('CONTROL_WRONG: '+str(exc)) from exc
    raise ValueError('CONTROL_SURVIVED')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('inputs',nargs='+');parser.add_argument('--output',required=True);args=parser.parse_args()
    pins={};branches=Counter();primes=Counter();sample=None;refsample=None
    for path in args.inputs:
        with open(path,'rb') as src:raw=src.read()
        pins[path]=hashlib.sha256(raw).hexdigest()
        for case in json.loads(raw)['cases']:
            b=check(case);branches[b]+=1;primes[case['p']]+=1
            if b!='REF' and sample is None:sample=case
            if b=='REF' and refsample is None:refsample=case
    def tamper(c):
        r=[i for i in c['selector'] if not c['word'][i][1]][0];c['word'][r][0]=(c['word'][r][0]+1)%c['p']
    controls=[mutate(sample,lambda c:c['selector'].__setitem__(1,c['selector'][0]),'SELECTOR'),
              mutate(sample,tamper,'PRODUCT'),
              mutate(refsample,lambda c:c.__setitem__('case','A/L0'),'BRANCH_REF')]
    result={'result':'PASS_INDEPENDENT_P2_BAND','input_sha256':pins,'actual_words_and_selectors':sum(branches.values()),
            'branches':dict(sorted(branches.items())),'primes':{str(k):v for k,v in sorted(primes.items())},
            'controls':controls}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
