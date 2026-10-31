#!/usr/bin/env python3
"""Exact rational switch search on a verified original 1-RQLS(10).

Each operation rotates a closed component of two orthogonal ray classes;
all 30 original bases are checked after EVERY accepted operation. It is a
bounded heuristic, not an unrestricted existence/nonexistence proof.
"""
import argparse
from collections import defaultdict
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import random
import time

HERE=Path(__file__).resolve().parent
N=10


def canonical(v):
    v=tuple(v)
    first=next(x for x in v if x)
    return v if first>0 else tuple(-x for x in v)


def blocks(labels):
    result=[[(r,c) for c in range(N)] for r in range(N)]
    result += [[(r,c) for r in range(N)] for c in range(N)]
    result += [[(r,c) for r in range(N) for c in range(N) if labels[r][c]==t] for t in range(N)]
    assert len(result)==30 and all(len(block)==N for block in result)
    assert all(set(row)==set(range(N)) for row in labels)
    assert all({labels[r][c] for r in range(N)}==set(range(N)) for c in range(N))
    return result


def classes(array):
    result=defaultdict(list)
    for r in range(N):
        for c in range(N):
            result[canonical(array[r][c])].append((r,c))
    return result


def verify(array,denom,bs):
    assert all(sum(x*x for x in array[r][c])==denom*denom for r in range(N) for c in range(N))
    for block in bs:
        for (r,c),(s,d) in combinations(block,2):
            assert sum(a*b for a,b in zip(array[r][c],array[s][d]))==0


def switch_options(array,bs):
    cls=classes(array)
    members=sorted(cls)
    options=[]
    for u,v in combinations(members,2):
        if sum(x*y for x,y in zip(u,v))!=0:
            continue
        verts=set(cls[u]+cls[v])
        adjacency={x:set() for x in verts}
        open_vertices=set()
        for block in bs:
            us=[x for x in block if x in verts and canonical(array[x[0]][x[1]])==u]
            vs=[x for x in block if x in verts and canonical(array[x[0]][x[1]])==v]
            assert len(us)<=1 and len(vs)<=1
            if us and vs:
                x,y=us[0],vs[0]
                adjacency[x].add(y)
                adjacency[y].add(x)
            elif us:
                open_vertices.add(us[0])
            elif vs:
                open_vertices.add(vs[0])
        remaining=set(verts)
        while remaining:
            stack=[min(remaining)]
            comp=set()
            while stack:
                x=stack.pop()
                if x in comp:
                    continue
                comp.add(x)
                stack.extend(adjacency[x]-comp)
            remaining-=comp
            if not (comp & open_vertices) and len(comp)<len(verts):
                options.append((u,v,tuple(sorted(comp))))
    return options


def apply_switch(array,denom,option):
    u,v,comp=option
    chosen=set(comp)
    out=[]
    for r in range(N):
        row=[]
        for c in range(N):
            old=canonical(array[r][c])
            if (r,c) not in chosen:
                row.append([5*x for x in old])
            elif old==u:
                row.append([3*x+4*y for x,y in zip(u,v)])
            else:
                assert old==v
                row.append([-4*x+3*y for x,y in zip(u,v)])
        out.append(row)
    newden=5*denom
    common=newden
    for row in out:
        for vec in row:
            for z in vec:
                common=gcd(common,abs(z))
    if common>1:
        newden//=common
        out=[[[z//common for z in vec] for vec in row] for row in out]
    return out,newden


def run():
    p=argparse.ArgumentParser()
    p.add_argument('--restarts',type=int,default=6)
    p.add_argument('--steps',type=int,default=30)
    p.add_argument('--seconds',type=float,default=45)
    p.add_argument('--seed',type=int,default=39173)
    args=p.parse_args()
    if args.restarts<1 or args.steps<1 or args.seconds<=0:
        raise ValueError('positive bounds required')
    source=json.loads((HERE/'frontier-20261028-coordinate-switch-result-v1.json').read_text())['partial_witness']
    if not source:
        raise ValueError('need exact initial partial witness')
    labels=source['labels']
    bs=blocks(labels)
    rng=random.Random(args.seed)
    start=time.monotonic()
    best={'ray_count':0}
    runs=[]
    for restart in range(args.restarts):
        arr=[[vec[:] for vec in row] for row in source['array']]
        denom=source['denominator']
        verify(arr,denom,bs)
        history=[]
        for step in range(args.steps):
            current=len(classes(arr))
            options=switch_options(arr,bs)
            if not options:
                break
            candidates=[]
            for option in options:
                trial,d=apply_switch(arr,denom,option)
                candidates.append((len(classes(trial)),option,trial,d))
            maximum=max(item[0] for item in candidates)
            choices=[item for item in candidates if item[0]==maximum]
            count,option,arr,denom=rng.choice(choices)
            verify(arr,denom,bs)
            history.append({'step':step+1,'options':len(options),'before':current,
                            'after':count,'component_size':len(option[2])})
            if count>best['ray_count']:
                best={'ray_count':count,'array':arr,'labels':labels,'denominator':denom,
                      'restart':restart,'step':step+1}
                print('new_best_rays',count,'restart',restart,'step',step+1,
                      'options',len(options),flush=True)
            if count==N*N or time.monotonic()-start>=args.seconds:
                break
        runs.append({'restart':restart,'steps':len(history),'history':history})
        print('restart',restart,'steps',len(history),'final_rays',len(classes(arr)),flush=True)
        if time.monotonic()-start>=args.seconds or best['ray_count']==N*N:
            break
    if best['ray_count']==0:
        best={'ray_count':source['ray_count'],'array':source['array'],
              'labels':labels,'denominator':source['denominator'],'restart':None,'step':0}
    record={'method':'exact closed-component orthogonal ray-pair rational switches',
            'parameters':vars(args),'elapsed_seconds':time.monotonic()-start,
            'runs':runs,'partial_witness':best,
            'caveat':'bounded heuristic; verified partial object is not a 100-ray witness unless ray_count=100'}
    output=HERE/'frontier-20261028-exact-switch-grow-result-v1.json'
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('best_exact_ray_count',best['ray_count'],'denominator',best['denominator'],flush=True)
    print('wrote',output.name,flush=True)


if __name__=='__main__':
    run()
