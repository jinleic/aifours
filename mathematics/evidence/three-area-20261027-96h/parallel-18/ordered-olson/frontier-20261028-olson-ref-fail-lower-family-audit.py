#!/usr/bin/env python3
"""Independent exhaustive tail and path audit for a REF-failing family."""
import argparse
from collections import Counter
import json


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+((-1 if b else 1)*y))%p
        b^=c
    return x,b


def check(p):
    word=[[0,1],[1,0]]+[[0,1]]*(2*p-2)+[[1,0]]
    for j in range(1,p):
        word += [[j,1],[1,0]]
    refs=[i for i,(_,b) in enumerate(word) if b]
    rotations=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rotations)!=p+1:
        raise ValueError('incorrect full word counts')
    edges=[]
    for k,i in enumerate(refs):
        j=refs[(k+1)%len(refs)]
        gap=word[i+1:j] if k+1<len(refs) else word[i+1:]+word[:j]
        if len(gap)>1 or any(t!=[1,0] for t in gap):
            raise ValueError('not zero-free cyclic singleton gaps')
        if gap or word[i][0]!=word[j][0]:
            edges.append((k,(k+1)%len(refs)))
    graph={v:set() for v in range(len(refs))}
    for i,j in edges:
        graph[i].add(j)
        graph[j].add(i)
    active=[v for v,nbr in graph.items() if nbr]
    ends=[v for v in active if len(graph[v])==1]
    if len(edges)!=p+1 or len(active)!=p+2 or len(ends)!=2 or any(len(graph[v])>2 for v in active):
        raise ValueError('raw graph not the claimed path plus isolates')
    path=[ends[0]]
    while path[-1]!=ends[1]:
        options=graph[path[-1]]-set(path)
        if len(options)!=1:
            raise ValueError('nonpath connected component')
        path.append(next(iter(options)))
    if len(path)!=p+2:
        raise ValueError('raw path omitted vertices')
    matching=len(path)//2
    if matching!=(p+1)//2 or matching>p-3:
        raise ValueError('not in lower matching branch')
    zeros=refs[:2*p-1]
    tail=refs[2*p-1:]
    tailclasses=0
    seen=set()
    for mask in range(1,1<<(p-1)):
        selected_tail=[tail[j] for j in range(p-1) if mask>>j&1]
        q=2*p-len(selected_tail)
        idx=sorted(zeros[:q]+selected_tail)
        value=product(word,idx,p)
        if len(idx)!=2*p or value[1] or value[0]==0:
            raise ValueError('reflection-only failure falsified')
        seen.add(value[0])
        tailclasses+=1
    if seen!=set(range(1,p)):
        raise ValueError('nonzero reflection support not full')
    d=(-pow(3,-1,p))%p
    selector=sorted(zeros[:p-3]+rotations+[tail[0],tail[d]])
    if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('original-order mixed selector failed')
    return {'p':p,'tail_subsets_exhausted':tailclasses,'raw_path_edges':len(edges),
            'raw_matching':matching,'reflection_only_support':sorted(seen),'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_INDEPENDENT_REF_FAIL_LOWER_FAMILY',
            'instances':[check(p) for p in (7,11,13,17,19)],
            'scope':'all tail-subset classes in five explicit words; no other caller failures checked'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
