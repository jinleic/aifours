#!/usr/bin/env python3
"""Check corrected two separated adjacent reflection pairs on original words."""
import argparse
from collections import Counter,defaultdict
import itertools
import json


def product(word,idx,p):
    x,parity=0,0
    for k in sorted(idx):
        a,b=word[k]
        x=(x+(-a if parity else a))%p
        parity ^= b
    return x,parity


def max_separated(bits):
    n=len(bits)
    dp=[0]*(n+1)
    for i in range(n-1,-1,-1):
        dp[i]=dp[i+1]
        for j in range(i+1,n):
            if bits[i]==bits[j]:
                dp[i]=max(dp[i],1+dp[j+1])
    return dp[0]


def check(p):
    # Core entirely before reflections; first two runs have lengths 2 and 3.
    word=[[1,0]]*(2*p-1)+[[4%p,1]]*2+[[p-1,0]]+[[4%p,1]]*3
    word += [entry for _ in range(p-3) for entry in ([p-1,0],[4%p,1])]
    rot=[i for i,(_,b) in enumerate(word) if not b]
    refs=[i for i,(_,b) in enumerate(word) if b]
    if len(word)!=4*p-1 or len(rot)!=3*p-3 or len(refs)!=p+2:
        raise ValueError('incorrect family counts')
    for i,j in itertools.combinations(refs,2):
        signed=Counter((-x if i<k<j else x)%p for k,(x,b) in enumerate(word) if not b)
        if max(signed.values())<=2*p-2:
            raise ValueError('prior signed-pair test unexpectedly qualifies')
        if signed[1]<2*p-1 or signed[p-1]>p-2:
            raise ValueError('actual signed majority pattern mismatch')
    fixed=rot[:2*p-2]
    if any(product(word,fixed+[i,j],p)==(0,0) for i,j in itertools.combinations(refs,2)):
        raise ValueError('prior fixed-I test unexpectedly succeeds')
    gaps=defaultdict(list)
    gap=0
    for x,b in word:
        if b:
            gap+=1
        else:
            gaps[gap].append(x)
    if any(len(set(v))>1 for v in gaps.values()):
        raise ValueError('prior same-gap unequal-pair condition unexpectedly succeeds')
    runs=[]
    for bit,group in itertools.groupby(b for _,b in word):
        runs.append((bit,len(list(group))))
    ref_runs=sorted(n for b,n in runs if b)
    if max(ref_runs)!=3 or ref_runs.count(2)!=1 or ref_runs.count(3)!=1:
        raise ValueError('not exactly the intended two- and three-runs')
    if max_separated([b for _,b in word])>=2*p-1:
        raise ValueError('prior saturated-pair condition unexpectedly succeeds')
    core=[i for i in rot if word[i][0]==1]
    extras=[i for i in rot if word[i][0]==p-1]
    selector=sorted(core[:p-2]+extras+refs[:4])
    if len(selector)!=2*p or len(set(selector))!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('four-reflection actual selector failed')
    mutation=sorted([i for i in selector if i!=refs[0]]+[next(i for i in core if i not in selector)])
    if product(word,mutation,p)==(0,0):
        raise ValueError('parity mutation survived')
    return {'p':p,'reflection_pairs':len(list(itertools.combinations(refs,2))),
            'selector':selector,'reflection_run_lengths':ref_runs,'old_certificates_fail':True,
            'parity_mutation_rejected':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_TWO_SEPARATED_ADJACENT_PAIRS_CORRECTED',
            'instances':[check(p) for p in (5,7,11,13)],
            'scope':'four exact instances of one written all-prime family'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
