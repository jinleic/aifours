#!/usr/bin/env python3
"""All-order transfer certificate for mandatory tails in extremal Shor row0.

An extra flag records whether an optional 14 mod16 tail was omitted. The last
17 positions are processed separately so the non-optional n-2 is not flagged.
"""
import json

Q=frozenset((3,5,8,11))
W=11
ANCHORS=frozenset((0,1,7,13,14))
FIRST=frozenset((0,1,7))


def initial():
    for j in set(range(W))-FIRST:
        if not any(abs(j-a) in Q for a in FIRST):
            raise AssertionError('additional initial bit possible')
    return {(tuple(sorted(W-j for j in FIRST)),False):len(FIRST)}


def step(vec,pos,flag_enabled=True,wrap_allowed=True):
    out={}
    for (ages,bad),score in vec.items():
        aged=tuple(a+1 for a in ages if a<W)
        if pos not in ANCHORS:
            flag=bad or (flag_enabled and pos>=30 and pos%16==14)
            key=(aged,flag);out[key]=max(out.get(key,-1),score)
        if wrap_allowed and not set(ages)&Q:
            key=((1,)+aged,bad);out[key]=max(out.get(key,-1),score+1)
    if not out:raise AssertionError(('empty transfer',pos))
    return out


def prefix(length):
    vec=initial()
    for pos in range(W,length):vec=step(vec,pos)
    return vec


def period_check():
    a,b=prefix(129),prefix(145)
    if set(a)!=set(b):raise AssertionError('period state sets differ')
    if any(b[s]!=v+4 for s,v in a.items()):raise AssertionError('period scores differ')
    return len(a)


def cyclic(n):
    if n<48 or n%16:raise ValueError('n must be multiple16 and >=48')
    cut=n-17
    vec=prefix(cut)
    for pos in range(cut,n):
        allowed=not any(n-(pos-a) in Q for a in FIRST)
        vec=step(vec,pos,flag_enabled=False,wrap_allowed=allowed)
    good=max((v for (a,b),v in vec.items() if not b),default=None)
    bad=max((v for (a,b),v in vec.items() if b),default=None)
    return {'n':n,'all_optional_present_max':good,'some_optional_missing_max':bad,
            'row_packing_upper':n//4-1}


def main():
    states=period_check()
    rows=[cyclic(n) for n in range(48,177,16)]
    for row in rows:
        if row['all_optional_present_max']!=row['row_packing_upper']:
            raise AssertionError('positive extremal control failed')
        if row['some_optional_missing_max']!=row['row_packing_upper']-1:
            raise AssertionError('omission is not strictly subextremal')
    return {'period_prefix_lengths':[129,145],'state_count':states,'score_increment':4,
            'checked_cyclic_orders':rows,
            'scope':'finite transfer certificate; all-order induction and completeness caller separate'}


if __name__=='__main__':print(json.dumps(main(),indent=2))
