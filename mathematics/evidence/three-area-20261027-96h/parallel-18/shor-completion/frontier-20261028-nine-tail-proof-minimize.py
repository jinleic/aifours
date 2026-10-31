#!/usr/bin/env python3
"""Prune unused facts from a symbolic proof tree, preserving complete branches."""
import json
from pathlib import Path

C=lambda x:(x,0,0,0);U=(0,1,0,0);V=(0,0,1,0);W=(0,0,0,1)
Q=[C(x) for x in (0,1,7,13,14)]+[U,V,W]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))

def opts(t):return [sub(t,x) for x in Q]
def tt(v):return tuple(v)


def minimize(node):
    facts={tt(v):(want,why) for v,want,why in node['steps']};ordered=[];seen=set();visiting=set()
    def need(v,want,external=None):
        key=(v,want)
        if key in seen:return
        if key in visiting:raise ValueError('cyclic proof')
        visiting.add(key)
        if external is None:
            actual,why=facts[v]
            if actual!=want:raise ValueError('wrong fact')
        else:why=external
        if why[0]=='hit':need(tt(why[2]),True)
        elif why[0]=='last':
            for z in opts(tt(why[1])):
                if z!=v:need(z,False)
        elif why[0] not in ('anchor','assume'):raise ValueError('bad reason')
        visiting.remove(key);seen.add(key)
        if external is None:ordered.append([v,want,why])
    r=node['result'];kind=r['kind'];result=dict(r)
    if kind=='empty':
        for x in opts(tt(r['target'])):need(x,False)
    elif kind=='double':
        for x in r['yes']:need(tt(x),True)
    elif kind=='opposite':
        v=tt(r['v']);need(v,not r['want']);need(v,r['want'],r['why'])
    elif kind=='branch':
        survivors={tt(x) for x in r['options']}
        for x in opts(tt(r['target'])):
            if x not in survivors:need(x,False)
        result['children']=[minimize(x) for x in r['children']]
    else:raise ValueError('bad node')
    return {'assumptions':node['assumptions'],'steps':ordered,'result':result}


if __name__=='__main__':
    root=Path(__file__).parent
    data=json.loads((root/'frontier-20261028-nine-tail-symbolic-proof-v1.json').read_text())
    data['tree']=minimize(data['tree']);data['variant']='dependency-pruned'
    out=root/'frontier-20261028-nine-tail-symbolic-proof-pruned-v1.json'
    if out.exists():raise FileExistsError('refuse overwrite')
    out.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n')
    print(json.dumps({'proof':str(out),'bytes':out.stat().st_size}))
