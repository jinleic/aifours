#!/usr/bin/env python3
"""Independent run-parity and graph audit of κ1/e2 REF-failing family."""
import argparse
import itertools
import json


def product(word,indices,p):
    x,b=0,0
    for i in indices:
        y,c=word[i]
        x=(x+((-1 if b else 1)*y))%p
        b^=c
    return x,b


def main_case(p):
    L=2*p-7
    word=[[0,1]]*L+[[1,0]]+[[1,1]]*2+[[0,1]]+[[p-1,1]]*2+[[0,1],[1,0]]
    for j in range(1,p):
        word += [[j,1],[1,0]]
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:
        raise ValueError('wrong original counts')
    values=[word[i][0] for i in refs]
    runs=[]
    for y in values:
        if not runs or runs[-1][0]!=y:
            runs.append([y,1])
        else:
            runs[-1][1]+=1
    if runs[0][0]==runs[-1][0]:
        raise ValueError('unexpected cyclic run merge')
    odd=sum(length%2 for _,length in runs)
    even=sum(length%2==0 for _,length in runs)
    if (odd,even)!=(p+2,2):
        raise ValueError('wrong κ1/e2 run profile')
    F=len(refs)
    graph={i:set() for i in range(F)}
    edges=0
    for k,i in enumerate(refs):
        j=refs[(k+1)%F]
        gap=word[i+1:j] if k+1<F else word[i+1:]+word[:j]
        if len(gap)>1 or any(x!=[1,0] for x in gap):
            raise ValueError('not zero-free singleton gaps')
        if gap or word[i][0]!=word[j][0]:
            graph[k].add((k+1)%F)
            graph[(k+1)%F].add(k)
            edges+=1
    unseen=set(graph)
    comps=[]
    while unseen:
        root=next(iter(unseen))
        stack=[root]
        comp=set()
        while stack:
            v=stack.pop()
            if v in comp:
                continue
            comp.add(v)
            stack.extend(graph[v]-comp)
        unseen-=comp
        if len(comp)>1 and (max(len(graph[v]) for v in comp)>2 or sum(len(graph[v])==1 for v in comp)!=2):
            raise ValueError('raw component not a path')
        comps.append(len(comp))
    if sorted(comps)!=sorted([p+2,3,2]+[1]*(2*p-9)):
        raise ValueError('wrong raw graph path components')
    matching=sum(c//2 for c in comps)
    if matching!=(p+5)//2 or matching>p-3:
        raise ValueError('wrong lower-branch matching')
    # Each mask chooses odd parity for the three odd zero runs and the two
    # even ±1 runs. A parity pattern's maximal selected count is 2H+z-y+t.
    prefix=[]
    for mask in range(1<<5):
        z=sum(bool(mask>>j&1) for j in (0,2,4))
        y=sum(bool(mask>>j&1) for j in (1,3))
        labels=[value for j,value in enumerate((0,1,0,p-1,0)) if mask>>j&1]
        P=sum((1 if i%2==0 else -1)*x for i,x in enumerate(labels))%p
        prefix.append((z,y,len(labels),P))
    checked=0
    tail=[i for i in range(1,p)]
    for mask in range(1<<(p-1)):
        chosen=[tail[j] for j in range(p-1) if mask>>j&1]
        t=len(chosen)
        S=sum((1 if i%2==0 else -1)*x for i,x in enumerate(chosen))%p
        for z,y,h,P in prefix:
            if t<4+y-z or (h+t)%2:
                continue
            exponent=(P+((-1 if h%2 else 1)*S))%p
            if exponent==0:
                raise ValueError('run parity pattern yields REF identity')
            checked+=1
    selector=list(range(L+6))+[L+7]
    if len(selector)!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('exact original mixed selector failed')
    return {'p':p,'odd_runs':odd,'even_runs':even,'raw_matching':matching,
            'run_parity_tail_cases_checked':checked,'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_INDEPENDENT_KAPPA1_E2_PARITY_AUDIT',
            'instances':[main_case(p) for p in (11,13,17,19)],
            'scope':'finite parity supersets/actual graph and mixed witnesses; remaining old callers unchecked'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
