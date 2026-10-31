#!/usr/bin/env python3
"""Construct original selectors from three separated zero-net reflection pairs."""
import argparse
import itertools
import json
import random

SEED=2026102816


def product(word,indices,p):
    x,b=0,0
    for i in sorted(indices):
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def get_pairs(word):
    refs=[i for i,(_,b) in enumerate(word) if b]
    Q={}
    q=0
    for i,(x,b) in enumerate(word):
        if b:
            Q[i]=q
        else:
            q+=1 if x==1 else -1
    edges=sorted(((i,j) for i,j in itertools.combinations(refs,2) if Q[i]==Q[j]),key=lambda e:(e[1],e[0]))
    pairs=[]
    last=-1
    for i,j in edges:
        if i>last:
            pairs.append((i,j))
            last=j
            if len(pairs)==3:
                return pairs,Q
    return None,Q


def evaluate(word,p,label):
    pairs,Q=get_pairs(word)
    if pairs is None:
        return None
    rot=[i for i,(_,b) in enumerate(word) if not b]
    differences=[(word[j][0]-word[i][0])%p for i,j in pairs]
    for (i,j),delta in zip(pairs,differences):
        if delta in (0,2%p):
            continue
        signed={k:(-word[k][0] if i<k<j else word[k][0])%p for k in rot}
        plus=[k for k,v in signed.items() if v==1]
        minus=[k for k,v in signed.items() if v==p-1]
        for q in range(2*p-1):
            other=2*p-2-q
            if q<=len(plus) and other<=len(minus) and (q-other)%p==delta:
                selector=sorted(plus[:q]+minus[:other]+[i,j])
                if product(word,selector,p)!=(0,0):
                    raise ValueError('two-reflection selector failed')
                return {'p':p,'label':label,'word':word,'zero_pairs':pairs,'mode':'two',
                        'chosen_pairs':[(i,j)],'selector':selector}
        raise ValueError('nonexceptional pair unexpectedly failed')
    if 2%p in differences and 0 in differences:
        use=[pairs[differences.index(2%p)],pairs[differences.index(0)]]
        qminus=0
        mode='four-mixed'
    elif all(d==2%p for d in differences) and p>=5:
        use=pairs[:2]
        qminus=1
        mode='four-all-two'
    else:
        use=pairs
        qminus=0
        mode='six'
    chosen_refs=sorted(i for pair in use for i in pair)
    signed={t:(-word[t][0] if sum(r<t for r in chosen_refs)%2 else word[t][0])%p for t in rot}
    plus=[t for t,v in signed.items() if v==1]
    minus=[t for t,v in signed.items() if v==p-1]
    to_omit=3*p-4-(2*p-len(chosen_refs))
    qplus=to_omit-qminus
    if qminus>len(minus) or qplus>len(plus):
        raise ValueError('omission availability failed')
    omitted=plus[:qplus]+minus[:qminus]
    selector=sorted((set(rot)-set(omitted)) | set(chosen_refs))
    if len(selector)!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('four/six reflection selector failed')
    return {'p':p,'label':label,'word':word,'zero_pairs':pairs,'mode':mode,
            'chosen_pairs':use,'omitted':omitted,'selector':selector}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    skipped={}
    for p in (3,5,7,11,13):
        for trial in range(100):
            kinds=[0]*(2*p-1)+[1]*(p-3)+[2]*(p+3)
            rng.shuffle(kinds)
            word=[[1,0] if t==0 else [p-1,0] if t==1 else [rng.randrange(p),1] for t in kinds]
            result=evaluate(word,p,{'generation':'random','trial':trial})
            if result is None:
                skipped[str(p)]=skipped.get(str(p),0)+1
                continue
            cases.append(result)
            pairs,_=get_pairs(word)
            for ds in ((0,0,0),(0,2%p,0),(2%p,2%p,2%p)):
                forced=[x[:] for x in word]
                for (i,j),d in zip(pairs,ds):
                    forced[i][0]=0
                    forced[j][0]=d
                check=evaluate(forced,p,{'generation':'forced','pattern':ds,'trial':trial})
                if check is None or check['mode']=='two':
                    raise ValueError('forced branch unexpectedly two')
                cases.append(check)
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases,'skipped':skipped},out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    branches={}
    for case in cases:
        key=case['label']['generation']+'/'+case['mode']
        branches[key]=branches.get(key,0)+1
    print(json.dumps({'result':'PASS_TYPE1_ZERO_TRIPLETS','actual_words':len(cases),
                      'branches':branches,'skipped_patterns':skipped},sort_keys=True))


if __name__=='__main__':
    main()
