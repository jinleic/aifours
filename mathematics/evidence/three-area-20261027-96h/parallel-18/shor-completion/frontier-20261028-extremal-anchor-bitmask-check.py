#!/usr/bin/env python3
"""Independent bitmask replay of flagged max-plus anchor proof."""
import json

D=(3,5,8,11)
MASK=(1<<11)-1
ANCHORS={0,1,7,13,14}
FIRST={0,1,7}


def seed():
    states=[]
    for mask in range(1<<11):
        pos={i for i in range(11) if mask&(1<<(10-i))}
        if not FIRST<=pos:continue
        if any(j-i in D for i in pos for j in pos if j>i):continue
        states.append(mask)
    if len(states)!=1:raise AssertionError('initial state not unique')
    return {(states[0],0):3}


def step(old,pos,flag=True,wrap=False):
    out={}
    for (mask,bad),score in old.items():
        if pos not in ANCHORS:
            b=bad | int(flag and pos>=30 and pos%16==14)
            key=((mask<<1)&MASK,b);out[key]=max(out.get(key,-1),score)
        if not wrap and not any(mask&(1<<(d-1)) for d in D):
            key=(((mask<<1)|1)&MASK,bad);out[key]=max(out.get(key,-1),score+1)
    if not out:raise AssertionError('empty frontier')
    return out


def prefix(t):
    vec=seed()
    for j in range(11,t):vec=step(vec,j)
    return vec


def period(a,b):
    if set(a)!=set(b):raise ValueError('STATE_SET_MISMATCH')
    if any(b[k]!=v+4 for k,v in a.items()):raise ValueError('SCORE_MISMATCH')


def cyclic(n):
    vec=prefix(n-17)
    for j in range(n-17,n):
        wrap=any(n-(j-a) in D for a in FIRST)
        vec=step(vec,j,flag=False,wrap=wrap)
    return [max(v for (m,b),v in vec.items() if b==0),
            max(v for (m,b),v in vec.items() if b==1)]


def main():
    a,b=prefix(129),prefix(145);period(a,b)
    mutation=dict(b);key=next(iter(mutation));mutation[key]+=1
    try:period(a,mutation)
    except ValueError as e:
        if str(e)!='SCORE_MISMATCH':raise
    else:raise AssertionError('score mutation passed')
    mutation=dict(b);del mutation[key]
    try:period(a,mutation)
    except ValueError as e:
        if str(e)!='STATE_SET_MISMATCH':raise
    else:raise AssertionError('state mutation passed')
    vals={n:cyclic(n) for n in range(48,193,16)}
    if any(v!=[n//4-1,n//4-2] for n,v in vals.items()):
        raise AssertionError('unexpected extremal gap')
    for n in (660,1320):
        # Non-multiples of16 are outside this theorem and must not be processed.
        if n%16==0:raise AssertionError('boundary selection error')
    return {'period_prefix':[129,145],'states':len(a),
            'score_and_state_mutations_rejected':True,'cyclic_orders':vals,
            'scope':'flagged row packing only; not a completed code'}


if __name__=='__main__':print(json.dumps(main(),indent=2))
