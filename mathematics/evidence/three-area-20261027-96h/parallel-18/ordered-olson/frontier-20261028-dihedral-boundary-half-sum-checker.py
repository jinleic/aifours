#!/usr/bin/env python3
"""Exact boundary-M support classification and coupled-gap examples."""
import argparse
from collections import Counter
import itertools
import json


def multiply(word,indices,p):
    a,b=0,0
    for i in sorted(indices):
        x,y=word[i]
        a=(a+(-x if b else x))%p
        b^=y
    return a,b


def subset_map(values,p):
    support={0:[]}
    for k,x in enumerate(values):
        new=dict(support)
        for total,idx in support.items():
            new.setdefault((total+x)%p,idx+[k])
        support=new
    return support


def exhaust_boundary(p):
    total=full=one_missing=0
    for diff in itertools.product(range(1,p),repeat=p-2):
        total+=1
        support=set(subset_map(diff,p))
        classes={min(v,p-v) for v in diff}
        T=sum(diff)%p
        if len(classes)>=2:
            if len(support)!=p:
                raise ValueError('diverse boundary support not full')
            full+=1
        else:
            if support!=set(range(p))-{(T*pow(2,-1,p))%p}:
                raise ValueError('one-class missing half-total formula failed')
            one_missing+=1
    return {'outlier_tuples':total,'full_support':full,'one_missing':one_missing}


def family(p):
    results=Counter()
    for y1,y2,y3 in itertools.product(range(p),repeat=3):
        word=[[0,0]]*(2*p-2)+[[y1,1],[1,0],[y2,1],[p-1,0],[y3,1]]+[[1,0]]*(p-4)+[[0,1]]*p
        rotations=[i for i,(_,b) in enumerate(word) if not b]
        refs=[i for i,(_,b) in enumerate(word) if b]
        if len(word)!=4*p-1 or len(rotations)!=3*p-4 or len(refs)!=p+3:
            raise ValueError('incorrect family word counts')
        raw_total=sum(word[i][0] for i in rotations)%p
        mus=[]
        candidates=[]
        for i,j in itertools.combinations(refs[:3],2):
            signed={k:(-word[k][0] if i<k<j else word[k][0])%p for k in rotations}
            counts=Counter(signed.values())
            if counts[0]!=2*p-2 or max(counts.values())!=2*p-2:
                raise ValueError('boundary signed majority failed')
            outliers=[k for k in rotations if signed[k]!=0]
            sums=subset_map([signed[k] for k in outliers],p)
            T=sum(signed.values())%p
            mu=T*pow(2,-1,p)%p
            if set(sums)!=set(range(p))-{mu}:
                raise ValueError('signed-pair exact half-total support failed')
            mus.append(mu)
            candidates.append((i,j,outliers,sums,mu,len(counts)))
        # combinations order is (0,1),(0,2),(1,2).
        if (mus[0]+mus[2]-mus[1])%p != raw_total*pow(2,-1,p)%p or raw_total==0:
            raise ValueError('boundary triple defect failed')
        pair=next((rec for rec in candidates if (word[rec[1]][0]-word[rec[0]][0])%p != rec[4]),None)
        if pair is None:
            raise ValueError('nonzero boundary defect did not force pair')
        i,j,outliers,sums,mu,support_count=pair
        target=(word[j][0]-word[i][0])%p
        chosen=[outliers[k] for k in sums[target]]
        zeros=[k for k in rotations if word[k][0]==0]
        selected=sorted(chosen+zeros[:2*p-2-len(chosen)]+[i,j])
        if len(selected)!=2*p or len(set(selected))!=2*p or multiply(word,selected,p)!=(0,0):
            raise ValueError('original boundary family selector failed')
        results[f'{refs.index(i)}-{refs.index(j)}']+=1
    return {'actual_words_and_selectors':sum(results.values()),'chosen_pair_ordinals':dict(results)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    result={'result':'PASS_BOUNDARY_HALF_SUM_CLASSIFICATION',
            'exhaustive_zero_majority_outlier_tuples':{str(p):exhaust_boundary(p) for p in (3,5,7)},
            'actual_family':{str(p):family(p) for p in (5,7,11,13)},
            'scope':'finite tuple classification and one actual family, not unrestricted closure'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
