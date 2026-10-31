#!/usr/bin/env python3
"""Find actual adjacent-packet DS3 witnesses for a frozen candidate word."""
import argparse
import functools
import hashlib
import itertools
import json


def product(word,indices,p):
    x,b=0,0
    for i in sorted(indices):
        y,c=word[i]
        x=(x+(-y if b else y))%p
        b^=c
    return x,b


def find_for_K(word,p,K):
    refs=[i for i,(_,b) in enumerate(word) if b]
    C=2*p-len(K)
    need=p-3
    F=len(refs)
    SK=sum(word[i][0] for i in K)%p
    z=[(word[i][0]+2*sum(word[k][0] for k in K if k<i))%p for i in refs]
    visited=0
    @functools.lru_cache(None)
    def rec(pos,q,b,res):
        nonlocal visited
        visited+=1
        if q==C:
            return () if b==need and (res+SK)%p==0 else None
        if pos>=F or b>need or q>C:
            return None
        if F-pos < (C-q)+(need-b) or (F-pos)//2 < need-b:
            return None
        ans=rec(pos+1,q,b,res)
        if ans is not None:
            return (('skip',pos),)+ans
        sign=1 if q%2==0 else -1
        ans=rec(pos+1,q+1,b,(res+sign*z[pos])%p)
        if ans is not None:
            return (('single',pos),)+ans
        if b<need and pos+1<F and z[pos]!=z[pos+1]:
            for pick in (pos,pos+1):
                ans=rec(pos+2,q+1,b+1,(res+sign*z[pick])%p)
                if ans is not None:
                    return (('binary',pos,pos+1,pick),)+ans
        return None
    actions=rec(0,0,0,0)
    if actions is None:
        return None,visited
    chosen=[]
    packets=[]
    for action in actions:
        if action[0]=='single':
            chosen.append(refs[action[1]])
            packets.append({'kind':'single','positions':[refs[action[1]]],'chosen':refs[action[1]]})
        elif action[0]=='binary':
            chosen.append(refs[action[3]])
            packets.append({'kind':'binary','positions':[refs[action[1]],refs[action[2]]],
                            'chosen':refs[action[3]],'gauge_delta':(z[action[2]]-z[action[1]])%p})
    selector=sorted(list(K)+chosen)
    if len(selector)!=2*p or product(word,selector,p)!=(0,0):
        raise ValueError('DS3 original-word witness invalid')
    return {'K':K,'C':C,'p_minus_3_binary_packets':need,'packets':packets,'selector':selector},visited


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as src:
        raw=src.read()
    data=json.loads(raw)
    case=next(x for x in data['cases'] if x['p']==args.p)
    word=case['word']
    rot=[i for i,(_,b) in enumerate(word) if not b]
    result=None
    tried=states=0
    for K in itertools.combinations(rot,2):
        tried+=1
        result,count=find_for_K(word,args.p,K)
        states+=count
        if result is not None:break
    summary={'result':'ACTUAL_DS3_PACKET_WITNESS_FOUND' if result else 'NO_ADJACENT_PACKET_WITNESS_FOR_K2_CUT0',
             'p':args.p,'input_sha256':hashlib.sha256(raw).hexdigest(),'K_pairs_tried':tried,
             'memo_states_visited':states,'witness':result,
             'scope':'positive actual adjacent-packet witness only; a negative would not settle general DS3'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(summary,out,sort_keys=True,indent=2)
        out.write('\n')
    print(json.dumps(summary,sort_keys=True))


if __name__=='__main__':
    main()
