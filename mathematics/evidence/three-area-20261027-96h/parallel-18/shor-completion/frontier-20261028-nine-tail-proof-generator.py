#!/usr/bin/env python3
"""Generate a finite symbolic coverage/collision proof for |Q|=8.

All expressions are triples of arbitrary extra-tail coefficients plus a
constant. It never assumes symbols are independent under specialization;
symbolically ignored coincidences only weaken its propagation. Output is a
proof tree, independently replayed by a separate checker.
"""
from collections import deque
import json
from pathlib import Path

m=3;C=lambda c:(c,)+(0,)*m
extra=[tuple([0]+[int(i==j) for j in range(m)]) for i in range(m)]
Q=[C(x) for x in (0,1,7,13,14)]+extra
anchors=[C(x) for x in (0,3,8,11)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
nodecount=0


def make_node(assumptions):
    global nodecount
    nodecount+=1
    if nodecount>100:raise RuntimeError('node cap; no proof produced')
    state={};steps=[];targets=set()
    pending=deque([(x,True,['anchor']) for x in anchors]+[(x,True,['assume']) for x in assumptions])
    while pending:
        v,want,why=pending.popleft()
        if v in state:
            if state[v]!=want:
                return {'assumptions':assumptions,'steps':steps,
                        'result':{'kind':'opposite','v':v,'want':want,'why':why}}
            continue
        if len(steps)>=5000:raise RuntimeError('step cap; no proof produced')
        state[v]=want;steps.append([v,want,why])
        for p in Q:
            t=add(v,p);targets.add(t);opts=[sub(t,x) for x in Q]
            yes=[x for x in opts if state.get(x) is True]
            unknown=[x for x in opts if x not in state]
            if len(yes)>1:
                return {'assumptions':assumptions,'steps':steps,
                        'result':{'kind':'double','target':t,'yes':yes[:2]}}
            if not yes:
                if not unknown:
                    return {'assumptions':assumptions,'steps':steps,
                            'result':{'kind':'empty','target':t}}
                if len(unknown)==1:pending.append((unknown[0],True,['last',t]))
            else:
                for x in unknown:pending.append((x,False,['hit',t,yes[0]]))
    best=[];count=len(Q)+1
    for t in sorted(targets):
        opts=[sub(t,x) for x in Q]
        if any(state.get(x) is True for x in opts):continue
        unknown=[x for x in opts if x not in state]
        if not unknown:raise AssertionError('unprocessed empty clause')
        if len(unknown)<count:count=len(unknown);best=[(t,unknown)]
        elif len(unknown)==count:best.append((t,unknown))
    if not best:raise RuntimeError('stable branch; no proof produced')
    t,options=best[0]
    children=[make_node(assumptions+[v]) for v in options]
    return {'assumptions':assumptions,'steps':steps,
            'result':{'kind':'branch','target':t,'options':options,'children':children}}


if __name__=='__main__':
    tree=make_node([])
    output={'statement':'No direct P+Q with Q=Y plus 3 distinct extras and A subset P',
            'extra_symbols':m,'Q':Q,'anchors_P':anchors,'tree':tree,'nodes':nodecount}
    path=Path(__file__).with_name('frontier-20261028-nine-tail-symbolic-proof-v1.json')
    if path.exists():raise FileExistsError('refuse to overwrite a pinned proof')
    path.write_text(json.dumps(output,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'proof':str(path),'nodes':nodecount,'bytes':path.stat().st_size}))
