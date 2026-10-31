#!/usr/bin/env python3
"""Exact syndrome-triple conflict cliques for the q=8 triangle code."""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-syndrome-triple-cliques-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def setup():
    inc={v:[t for t,T in enumerate(TRI) if v in T] for v in range(1,11)}
    if any(len(x)!=3 for x in inc.values()):raise ValueError('INCIDENCE')
    sm=[[sum(1<<inc[v][k] for k in range(3) if a>>k&1) for a in range(8)] for v in range(1,11)]
    am=[sum(1<<x for x in inc[v]) for v in range(1,11)]
    return sm,am


def syndrome(z,sm):
    out=0
    for i in range(10):out^=sm[i][(z>>(3*i))&7]
    return out


def conflict(z):
    return any(((z>>(3*(v-1)))&7) and all(not ((z>>(3*(u-1)))&7) for u in N[v]) for v in range(1,11))


def differences(sm):
    D=set()
    for v in range(1,11):
        free=[u for u in range(1,11) if u!=v and u not in N[v]]
        for a in range(1,8):
            for code in range(8**len(free)):
                z=a<<(3*(v-1));x=code
                for u in free:z|=(x&7)<<(3*(u-1));x>>=3
                D.add(z)
    if len(D)!=231497:raise ValueError(('DEGREE',len(D)))
    buckets=[[] for _ in range(1024)]
    for z in D:buckets[syndrome(z,sm)].append(z)
    for b in buckets:b.sort()
    if buckets[0] or min(len(b) for b in buckets[1:])!=68:raise ValueError('SYNDROME_CONFLICT')
    return D,buckets


def main():
    sm,am=setup();D,buckets=differences(sm);local=0;exceptions=[]
    for s,t in combinations(range(1,1024),2):
        if any((s&a) and (t&a) and (s&a)!=(t&a) for a in am):local+=1;continue
        hit=None
        for u in buckets[s]:
            for v in buckets[t]:
                if (u^v) in D:hit=(u,v);break
            if hit:break
        if hit is None:raise ValueError(('NO_CLIQUE',s,t))
        u,v=hit
        if not(conflict(u) and conflict(v) and conflict(u^v)):raise ValueError('CONFLICT')
        exceptions.append({'s':s,'t':t,'u':u,'v':v})
    if local!=522231 or len(exceptions)!=522:raise ValueError(('COUNT',local,len(exceptions)))
    out={'triangles':TRI,'local_incident_syndrome_masks':am,'conflict_difference_count':len(D),
         'nonzero_syndrome_pairs':local+len(exceptions),'single_vertex_pairs':local,
         'exceptional_witness_count':len(exceptions),'exceptional_witnesses':exceptions,'all_checked':True,
         'limits':'Exact conflict-triangle witnesses only; clique-factor/cardinality consequences are written separately.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='exceptional_witnesses'},indent=2))


if __name__=='__main__':main()
