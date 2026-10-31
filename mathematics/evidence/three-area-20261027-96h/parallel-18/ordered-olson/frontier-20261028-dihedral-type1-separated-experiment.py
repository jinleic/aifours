#!/usr/bin/env python3
"""Exact type-I selectors for two low edges with bounded net increment."""
import argparse
import itertools
import json
import random

SEED=2026102815


def product(word,indices,p):
    x,b=0,0
    for i in sorted(indices):
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def low_pair(word,p):
    refs=[i for i,(_,b) in enumerate(word) if b]
    Q={}
    z=0
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=z
        else:
            z+=1 if x==1 else -1
    edges=[(i,j,Q[j]-Q[i]) for i,j in itertools.combinations(refs,2) if 1<=Q[j]-Q[i]<=p+1]
    result=next(((a,b) for a in edges for b in edges if a[1]<b[0] and a[2]+b[2]<=p),None)
    return result,Q


def evaluate(word,p,label):
    pairs,Q=low_pair(word,p)
    if pairs is None:
        return None
    rot=[i for i,(_,b) in enumerate(word) if not b]
    for i,j,u in pairs:
        signed={t:(-word[t][0] if i<t<j else word[t][0])%p for t in rot}
        plus=[t for t,v in signed.items() if v==1]
        minus=[t for t,v in signed.items() if v==p-1]
        target=(word[j][0]-word[i][0])%p
        for q in range(2*p-1):
            other=2*p-2-q
            if q<=len(plus) and other<=len(minus) and (q-other)%p==target:
                selected=sorted(plus[:q]+minus[:other]+[i,j])
                if product(word,selected,p)!=(0,0):
                    raise ValueError('two-reflection original product failed')
                return {'p':p,'label':label,'word':word,'low_pairs':pairs,'mode':'two',
                        'selected_pair':[i,j],'selector':selected}
    selected_refs=[pairs[0][0],pairs[0][1],pairs[1][0],pairs[1][1]]
    signed={t:(-word[t][0] if sum(r<t for r in selected_refs)%2 else word[t][0])%p for t in rot}
    plus=[t for t,v in signed.items() if v==1]
    minus=[t for t,v in signed.items() if v==p-1]
    if len(plus)<p-1 or len(minus)<1:
        raise ValueError('required same-actual-sign omissions unavailable')
    omitted=plus[:p-1]+minus[:1]
    selected=sorted((set(rot)-set(omitted))|set(selected_refs))
    if len(selected)!=2*p or product(word,selected,p)!=(0,0):
        raise ValueError('four-reflection original product failed')
    return {'p':p,'label':label,'word':word,'low_pairs':pairs,'mode':'four',
            'omitted':omitted,'selector':selected}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    random_cases=[]
    forced=[]
    skipped={}
    for p in (3,5,7,11,13):
        for trial in range(120):
            kinds=[0]*(2*p-1)+[1]*(p-3)+[2]*(p+3)
            rng.shuffle(kinds)
            word=[[1,0] if t==0 else [p-1,0] if t==1 else [rng.randrange(p),1] for t in kinds]
            case=evaluate(word,p,{'generation':'random','trial':trial})
            if case is None:
                skipped[str(p)]=skipped.get(str(p),0)+1
                continue
            random_cases.append(case)
            pairs,_=low_pair(word,p)
            forcedword=[v[:] for v in word]
            for i,j,u in pairs:
                forcedword[i][0]=0
                forcedword[j][0]=(2*(1-u))%p
            result=evaluate(forcedword,p,{'generation':'pair-gauge','trial':trial})
            if result is None or result['mode']!='four':
                raise ValueError('pair gauge did not require four branch')
            forced.append(result)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'random_cases':random_cases,'forced_cases':forced,'skipped':skipped},
                  out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    branches={}
    for case in random_cases+forced:
        key=case['label']['generation']+'/'+case['mode']
        branches[key]=branches.get(key,0)+1
    print(json.dumps({'result':'PASS_TYPE1_SEPARATED_LOW_EDGES','actual_words':len(random_cases)+len(forced),
                      'skipped_patterns':skipped,'branches':branches},sort_keys=True))


if __name__=='__main__':
    main()
