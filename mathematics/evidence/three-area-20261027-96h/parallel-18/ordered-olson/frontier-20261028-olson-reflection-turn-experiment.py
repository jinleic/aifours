#!/usr/bin/env python3
"""Construct reflection-only original witnesses by adjacent-edge flip."""
import argparse
import json
import random

SEED=2026102818


def direct(word,indices,p):
    x,b=0,0
    for i in indices:
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def match_outside(values,p,t):
    F=len(values)
    pairs=[]
    for lo,hi in ((0,t),(t+3,F)):
        for i in range(lo,hi-1,2):
            if values[i]!=values[i+1]:
                pairs.append((i,i+1))
    if len(pairs)<p-3:
        raise ValueError('nonzero matching outside turn unavailable')
    return pairs[:p-3]


def analyze_matching(values,p,matching):
    starts={i:j for i,j in matching}
    blocks=[]
    i=0
    while i<len(values):
        if i in starts:
            j=starts[i]
            if j!=i+1:
                raise ValueError('nonadjacent pair')
            blocks.append((i,j))
            i=j+1
        else:
            blocks.append((i,))
            i+=1
    if len(blocks)!=2*p:
        raise ValueError('wrong selected reflection count')
    base=0
    C=0
    delta=[]
    for q,block in enumerate(blocks):
        sign=1 if q%2==0 else -1
        base+=sign*values[block[0]]
        if len(block)==1:
            C+=2*sign*values[block[0]]
        else:
            C+=sign*(values[block[0]]+values[block[1]])
            delta.append((sign*(values[block[1]]-values[block[0]]),q))
    support={0:[]}
    for d,q in delta:
        nxt=dict(support)
        for v,choices in support.items():
            nxt.setdefault((v+d)%p,choices+[q])
        support=nxt
    target=(-base)%p
    selected=None
    if target in support:
        swap=set(support[target])
        selected=[block[1] if q in swap else block[0] for q,block in enumerate(blocks)]
    return {'double_midpoint':C%p,'support_size':len(support),'selected_ordinals':selected}


def full_word(rng,p,values):
    F=len(values)
    gaps=set(rng.sample(range(F),p+1))
    word=[]
    refs=[]
    for t,y in enumerate(values):
        refs.append(len(word))
        word.append([y,1])
        if t in gaps:
            word.append([rng.randrange(1,p),0])
    return word,refs


def evaluate(rng,p,steps,kind):
    values=[rng.randrange(p)]
    for d in steps:
        values.append((values[-1]+d)%p)
    word,refs=full_word(rng,p,values)
    if len(word)!=4*p-1 or len(refs)!=3*p-2:
        raise ValueError('wrong original counts')
    turn=next((i for i in range(len(steps)-1) if steps[i] and steps[i+1] and steps[i]!=steps[i+1]),None)
    if turn is None:
        if not all(d==steps[0] and d!=0 for d in steps):
            return None
        selected=list(range(2*p))
        details={'mode':'constant-step','step':steps[0]}
    else:
        common=match_outside(values,p,turn)
        M1=sorted(common+[(turn,turn+1)])
        M2=sorted(common+[(turn+1,turn+2)])
        A=analyze_matching(values,p,M1)
        B=analyze_matching(values,p,M2)
        if A['support_size']<p-1 or B['support_size']<p-1 or A['double_midpoint']==B['double_midpoint']:
            raise ValueError('matching support or midpoint flip failed')
        if A['selected_ordinals'] is not None:
            selected=A['selected_ordinals']
            chosen=0
        elif B['selected_ordinals'] is not None:
            selected=B['selected_ordinals']
            chosen=1
        else:
            raise ValueError('both matching families miss identity')
        details={'mode':'turn-flip','turn_ordinal':turn,'common_pairs':common,
                 'matchings':[M1,M2],'double_midpoints':[A['double_midpoint'],B['double_midpoint']],
                 'support_sizes':[A['support_size'],B['support_size']],'chosen_matching':chosen}
    selector=sorted(refs[i] for i in selected)
    if len(selector)!=2*p or direct(word,selector,p)!=(0,0):
        raise ValueError('original reflection-only selector failed')
    return {'p':p,'label':kind,'word':word,'selector':selector,'details':details}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    rng=random.Random(SEED)
    cases=[]
    skipped={}
    for p in (3,5,7,11,13):
        length=3*p-3
        for trial in range(150):
            zeros=rng.randrange((p-1)//2+1)
            zero_sites=set(rng.sample(range(length),zeros))
            steps=[0 if i in zero_sites else rng.randrange(1,p) for i in range(length)]
            result=evaluate(rng,p,steps,{'kind':'turn-random','trial':trial,'zero_edges':zeros})
            if result is None:
                skipped[str(p)]=skipped.get(str(p),0)+1
            else:
                cases.append(result)
        for d in range(1,p):
            cases.append(evaluate(rng,p,[d]*length,{'kind':'constant-step','d':d}))
    if any(c is None for c in cases):
        raise ValueError('unexpected empty record')
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump({'seed':SEED,'cases':cases,'skipped':skipped},out,sort_keys=True,separators=(',',':'))
        out.write('\n')
    bymode={}
    for c in cases:
        mode=c['details']['mode']
        bymode[mode]=bymode.get(mode,0)+1
    print(json.dumps({'result':'PASS_REFLECTION_TURN_WITNESSES','original_words':len(cases),
                      'branches':bymode,'skipped_not_claimed':skipped},sort_keys=True))


if __name__=='__main__':
    main()
