#!/usr/bin/env python3
"""Check actual-block vs reflection-projection counterexample family."""
import argparse
from collections import Counter
import json


def build(p):
    w=[[0,1],[1,0],[0,1],[1,0]]+[[0,1]]*(2*p-3)+[[1,0]]
    for j in range(1,p-1):w += [[j,1],[1,0]]
    w.append([p-1,1])
    return w


def product(w,idx,p):
    x,b=0,0
    for i in idx:
        y,c=w[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def check(p):
    w=build(p)
    refs=[i for i,(_,b) in enumerate(w) if b]
    rot=[i for i,(_,b) in enumerate(w) if not b]
    if len(w)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1 or any(w[i][0]==0 for i in rot):
        raise ValueError('wrong original count/zero status')
    # Start is a genuine cyclic actual-block boundary: last reflection differs.
    if w[refs[-1]][0]==w[refs[0]][0]:
        raise ValueError('unexpected cyclic block merge')
    actual=[]
    projected=[]
    G={q:set() for q in range(len(refs))}
    for q,i in enumerate(refs):
        if q==0 or i-refs[q-1]>1 or w[i][0]!=w[refs[q-1]][0]:
            actual.append([w[i][0],1])
        else:actual[-1][1]+=1
        if q==0 or w[i][0]!=w[refs[q-1]][0]:
            projected.append([w[i][0],1])
        else:projected[-1][1]+=1
        j=refs[(q+1)%len(refs)]
        gap=w[i+1:j] if q+1<len(refs) else w[i+1:]+w[:j]
        if len(gap)>1 or any(t!=[1,0] for t in gap):
            raise ValueError('cyclic gap not singleton')
        if gap or w[i][0]!=w[j][0]:
            G[q].add((q+1)%len(refs));G[(q+1)%len(refs)].add(q)
    o=sum(n%2 for _,n in actual); e=sum(n%2==0 for _,n in actual)
    op=sum(n%2 for _,n in projected); ep=sum(n%2==0 for _,n in projected)
    if (o,e,op,ep)!=(p+2,0,p,0):
        raise ValueError('actual/projected distinction mismatch')
    seen=set();sizes=[]
    for q in G:
        if q in seen:continue
        stack=[q]; comp=set()
        while stack:
            v=stack.pop()
            if v in comp:continue
            comp.add(v);stack.extend(G[v]-comp)
        seen |= comp
        if len(comp)>1 and sum(len(G[v])==1 for v in comp)!=2:
            raise ValueError('raw component not a path')
        sizes.append(len(comp))
    if sorted(sizes)!=sorted([p+3]+[1]*(2*p-5)):
        raise ValueError('unexpected raw graph components')
    nu=sum(n//2 for n in sizes)
    if nu!=(p+3)//2:
        raise ValueError('wrong raw matching')
    dp=[set() for _ in range(2*p+1)];dp[0].add(0)
    for q,i in enumerate(refs):
        y=w[i][0]
        for k in range(min(q,2*p-1),-1,-1):
            dp[k+1] |= {(v+(y if k%2==0 else -y))%p for v in dp[k]}
    if 0 in dp[2*p] or dp[2*p]!=set(range(1,p)):
        raise ValueError('projection not REF-failing with exact support')
    d=(-pow(3,-1,p))%p
    zeros=refs[:2*p-1];tail=refs[2*p-1:]
    selector=sorted(zeros[:p-3]+rot+[tail[0],tail[d]])
    if len(selector)!=2*p or product(w,selector,p)!=(0,0):
        raise ValueError('original mixed selector failed')
    if w[0]!=[0,1] or w[1]!=[1,0] or w[2]!=[0,1]:
        raise ValueError('literal SEL triple missing')
    return {'p':p,'actual_odd':o,'actual_even':e,'projected_odd':op,'projected_even':ep,
            'raw_matching':nu,'within_lower_matching':nu<=p-3,
            'REF_support':sorted(dp[2*p]),'SEL_predicate_applies':True,'mixed_selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_ACTUAL_VS_PROJECTED_COUNTEREXAMPLE',
            'instances':[check(p) for p in (7,11,13,17)],
            'scope':'explicit REF counterexample to an unconditional actual-odd-block lift; SEL-covered, not L_RES'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
