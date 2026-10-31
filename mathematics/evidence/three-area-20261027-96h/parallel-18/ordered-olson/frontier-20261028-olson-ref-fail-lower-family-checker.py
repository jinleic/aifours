#!/usr/bin/env python3
"""Check an exact REF-failing, low-raw-matching, solvable family."""
import argparse
from collections import Counter
import json


def product(word,idx,p):
    x,b=0,0
    for i in sorted(idx):
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def refl_support(word,p):
    values=[y for y,b in word if b]
    dp=[set() for _ in range(2*p+1)]
    dp[0].add(0)
    for i,y in enumerate(values):
        for k in range(min(i,2*p-1),-1,-1):
            dp[k+1] |= {(v+(y if k%2==0 else -y))%p for v in dp[k]}
    return dp[2*p]


def raw_graph(word,p):
    refs=[i for i,(_,b) in enumerate(word) if b]
    F=len(refs)
    edges=[]
    for q,i in enumerate(refs):
        j=refs[(q+1)%F]
        between=word[i+1:j] if q+1<F else word[i+1:]+word[:j]
        if len(between)>1 or any(b for _,b in between):
            raise ValueError('reflection cyclic gap not singleton')
        edges.append(bool(between) or word[i][0]!=word[j][0])
    def path_max(edge_slice):
        prev2=prev1=0
        for present in edge_slice:
            cur=max(prev1,prev2+int(present)) if present else prev1
            prev2,prev1=prev1,cur
        return prev1
    excluded=path_max(edges[:-1])
    included=1+path_max(edges[1:-2]) if edges[-1] else 0
    matching=max(excluded,included)
    degree=[int(edges[i-1])+int(edges[i]) for i in range(F)]
    return {'edges':sum(edges),'degree_counts':dict(Counter(degree)),'matching':matching}


def check(p):
    word=[[0,1],[1,0]]+[[0,1]]*(2*p-2)+[[1,0]]
    for j in range(1,p):
        word += [[j,1],[1,0]]
    refs=[i for i,(_,b) in enumerate(word) if b]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    if len(word)!=4*p-1 or len(refs)!=3*p-2 or len(rot)!=p+1 or any(word[i][0]==0 for i in rot):
        raise ValueError('wrong original counts or zero rotation')
    g=raw_graph(word,p)
    if g['edges']!=p+1 or g['matching']!=(p+1)//2 or g['matching']>p-3:
        raise ValueError('raw lower matching structure failed')
    support=refl_support(word,p)
    if 0 in support:
        raise ValueError('REF-failure claim false')
    d=(-pow(3,-1,p))%p
    if not 1<=d<=p-2:
        raise ValueError('tail separation not realizable')
    zero_refs=refs[:p-3]
    tail_refs=refs[2*p-1:]
    selector=sorted(zero_refs+rot+[tail_refs[0],tail_refs[d]])
    if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('actual original identity selector failed')
    return {'p':p,'raw_graph':g,'reflection_only_support':sorted(support),
            'tail_difference':d,'actual_selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_REF_FAIL_LOWER_SOLVABLE_FAMILY',
            'instances':[check(p) for p in (7,11,13,17,19)],
            'scope':'five exact family instances; other OLD/SEL/IPGEN/GS/DS3 failures not checked'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
