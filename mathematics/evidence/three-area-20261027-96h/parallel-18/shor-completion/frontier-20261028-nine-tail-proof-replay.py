#!/usr/bin/env python3
"""Replay symbolic exact-cover proof, independently of the generator."""
import json
from pathlib import Path

C=lambda k:(k,0,0,0)
U=(0,1,0,0);V=(0,0,1,0);W=(0,0,0,1)
Q=[C(x) for x in (0,1,7,13,14)]+[U,V,W]
A=[C(x) for x in (0,3,8,11)]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))

def tup(x):
    if not isinstance(x,list) or len(x)!=4 or any(type(v)!=int for v in x):raise ValueError('bad expression')
    return tuple(x)

def options(t):return [sub(t,s) for s in Q]

def reason(v,want,why,state,assumptions):
    if not isinstance(why,list) or not why:raise ValueError('bad reason')
    if why==['anchor']:
        if not want or v not in A:raise ValueError('bad anchor')
    elif why==['assume']:
        if not want or v not in assumptions:raise ValueError('bad assumption')
    elif why[0]=='hit' and len(why)==3:
        if want:raise ValueError('hit can only forbid')
        t,h=tup(why[1]),tup(why[2]);cand=options(t)
        if v not in cand or h not in cand or v==h or state.get(h) is not True:raise ValueError('bad hit')
    elif why[0]=='last' and len(why)==2:
        t=tup(why[1]);cand=options(t)
        if not want or v not in cand or any(state.get(x) is not False for x in cand if x!=v):
            raise ValueError('bad last candidate')
    else:raise ValueError('unknown reason')

stats={'nodes':0,'steps':0,'leaves':0,'branch_points':0,'empty':0,'double':0,'opposite':0}
def replay(node,assumptions):
    stats['nodes']+=1
    got=[tup(x) for x in node['assumptions']]
    if got!=assumptions:raise ValueError('wrong branch assumptions')
    state={}
    for item in node['steps']:
        if not isinstance(item,list) or len(item)!=3 or type(item[1])!=bool:raise ValueError('bad step')
        v,want,why=tup(item[0]),item[1],item[2]
        if v in state:raise ValueError('duplicate assignment')
        reason(v,want,why,state,assumptions);state[v]=want;stats['steps']+=1
    res=node['result'];kind=res['kind']
    if kind=='empty':
        if any(state.get(x) is not False for x in options(tup(res['target']))):raise ValueError('not empty')
    elif kind=='double':
        cand=options(tup(res['target']));yes=[tup(x) for x in res['yes']]
        if len(yes)!=2 or yes[0]==yes[1] or any(x not in cand or state.get(x) is not True for x in yes):
            raise ValueError('not double')
    elif kind=='opposite':
        v=tup(res['v']);want=res['want']
        if type(want)!=bool or state.get(v) is not (not want):raise ValueError('not opposite')
        reason(v,want,res['why'],state,assumptions)
    elif kind=='branch':
        cand=options(tup(res['target']))
        if any(state.get(x) is True for x in cand):raise ValueError('covered branch target')
        unknown=[x for x in cand if x not in state]
        got=[tup(x) for x in res['options']];children=res['children']
        if got!=unknown or len(children)!=len(got) or not got:raise ValueError('incomplete branch')
        stats['branch_points']+=1
        for x,child in zip(got,children):replay(child,assumptions+[x])
        return
    else:raise ValueError('bad conclusion')
    stats['leaves']+=1;stats[kind]+=1


if __name__=='__main__':
    path=Path(__file__).with_name('frontier-20261028-nine-tail-symbolic-proof-v1.json')
    data=json.loads(path.read_text())
    if data['extra_symbols']!=3 or [tup(x) for x in data['Q']]!=Q or [tup(x) for x in data['anchors_P']]!=A:
        raise ValueError('wrong statement')
    replay(data['tree'],[])
    if data['nodes']!=stats['nodes']:raise ValueError('wrong node count')
    print('PASS: exact symbolic coverage/collision proof replay')
    print(json.dumps(stats,sort_keys=True))
    print('Assumptions: Q elements distinct; P+Q direct and covering; A subset P.')
