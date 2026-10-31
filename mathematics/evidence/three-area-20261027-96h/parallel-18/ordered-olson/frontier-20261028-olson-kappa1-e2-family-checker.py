#!/usr/bin/env python3
"""Exact actual κ=1,e=2 lower-matching family and mixed witnesses."""
import argparse
from collections import Counter
import json


def build(p):
    word=[[0,1]]*(2*p-7)+[[1,0]]+[[1,1]]*2+[[0,1]]+[[p-1,1]]*2+[[0,1],[1,0]]
    for j in range(1,p):
        word += [[j,1],[1,0]]
    return word


def product(word,idx,p):
    x,b=0,0
    for i in idx:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def reflection_support(word,p):
    values=[x for x,b in word if b]
    dp=[set() for _ in range(2*p+1)]
    dp[0].add(0)
    for i,y in enumerate(values):
        for q in range(min(i,2*p-1),-1,-1):
            dp[q+1] |= {(v+(y if q%2==0 else -y))%p for v in dp[q]}
    return dp[2*p]


def graph(word,p):
    refs=[i for i,(_,b) in enumerate(word) if b]
    G={i:set() for i in range(len(refs))}
    edgecount=0
    for k,pos in enumerate(refs):
        j=refs[(k+1)%len(refs)]
        gap=word[pos+1:j] if k+1<len(refs) else word[pos+1:]+word[:j]
        if len(gap)>1 or any(x!=[1,0] for x in gap):
            raise ValueError('not zero-free cyclic singleton gaps')
        if gap or word[pos][0]!=word[j][0]:
            G[k].add((k+1)%len(refs))
            G[(k+1)%len(refs)].add(k)
            edgecount+=1
    components=[]
    unseen=set(G)
    while unseen:
        root=next(iter(unseen))
        stack=[root]
        comp=set()
        while stack:
            v=stack.pop()
            if v in comp:
                continue
            comp.add(v)
            stack.extend(G[v]-comp)
        unseen-=comp
        if any(len(G[v])>2 for v in comp):
            raise ValueError('nonpath raw component')
        if len(comp)>1 and sum(len(G[v])==1 for v in comp)!=2:
            raise ValueError('cyclic raw component')
        components.append(len(comp))
    matching=sum(v//2 for v in components)
    return {'edge_count':edgecount,'component_sizes':sorted(Counter(components).items()),'matching':matching}


def check(p):
    word=build(p)
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1:
        raise ValueError('wrong original word counts')
    g=graph(word,p)
    if g['matching']!=(p+5)//2 or g['matching']>p-3:
        raise ValueError('raw graph not in lower branch')
    if 0 in reflection_support(word,p):
        raise ValueError('REF-failure disproved')
    L=2*p-7
    # All L initial zeros, first rho, both +1 reflections, first middle zero,
    # both -1 reflections, and rho after the second (unselected) middle zero.
    selector=list(range(L+6))+[L+7]
    if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('mixed original selector failed')
    mutation=[x[:] for x in word]
    mutation[L+4][0]=1
    mutation[L+5][0]=1
    if 0 not in reflection_support(mutation,p):
        raise ValueError('opposite-even-label mutation not detected')
    return {'p':p,'raw_graph':g,'reflection_only_support':sorted(reflection_support(word,p)),
            'selector':selector,'opposite_even_label_mutation_REF_covered':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_KAPPA1_E2_REF_FAIL_MIXED_SELECTOR',
            'instances':[check(p) for p in (11,13,17,19)],
            'scope':'four exact family instances; OLD/SEL/IPGEN/DS3 not checked'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
