#!/usr/bin/env python3
"""Exact certificates for every extendibility-eligible 5-row BH half-frame.

For each compatible triple with at least5 common candidate neighbors, report
an isolated column or an odd connected component in its half-matching graph.
"""
from itertools import permutations,combinations
from collections import Counter
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
second=(0,0,1,1,2,2,3,3,4,4)
zero=(0,)*10

def balanced(a,b):
    counts=[0]*5
    for x,y in zip(a,b):counts[(x-y)%5]+=1
    return counts==[2]*5


tails=sorted(set(permutations((0,1,1,2,2,3,3,4,4))))
assert len(tails)==22680
rows=[(0,)+tail for tail in tails if balanced((0,)+tail,second)]
assert len(rows)==1075
adj=[0]*len(rows)
for i in range(len(rows)):
    for j in range(i+1,len(rows)):
        if balanced(rows[i],rows[j]):adj[i]|=1<<j;adj[j]|=1<<i

records=[];hist=Counter();triples=0
for i in range(len(rows)):
    js=adj[i]&~((1<<(i+1))-1)
    while js:
        bit=js&-js;js-=bit;j=bit.bit_length()-1
        ks=adj[i]&adj[j]&~((1<<(j+1))-1)
        while ks:
            bit=ks&-ks;ks-=bit;k=bit.bit_length()-1;triples+=1
            if (adj[i]&adj[j]&adj[k]).bit_count()<5:continue
            E=(zero,second,rows[i],rows[j],rows[k])
            graph=[set() for _ in range(10)]
            for c,d in combinations(range(10),2):
                if len({(v[c]-v[d])%5 for v in E})==5:
                    graph[c].add(d);graph[d].add(c)
            isolated=[v for v in range(10) if not graph[v]]
            if isolated:
                witness={'triple':[i,j,k],'isolated':isolated[0]}
                hist[('isolated',len(isolated))]+=1
            else:
                rem=set(range(10));components=[]
                while rem:
                    stack=[min(rem)];comp=set()
                    while stack:
                        v=stack.pop()
                        if v in comp:continue
                        comp.add(v);stack.extend(graph[v]-comp)
                    rem-=comp;components.append(sorted(comp))
                odd=next((c for c in components if len(c)%2),None)
                if odd is None:
                    raise AssertionError(('no elementary certificate',i,j,k,components))
                witness={'triple':[i,j,k],'odd_component':odd}
                hist[('odd_component',len(odd))]+=1
            records.append(witness)
assert triples==53065 and len(records)==16064
out=ROOT/'frontier-20261028-bh10-structural-cert-v1.json'
out.write_text(json.dumps({'row_order':'lexicographic deduplicated dephased rows',
 'candidate_count':len(rows),'triples_examined':triples,'certificates':records,
 'scope':'eligible half-frames only, not a formal proof of full QLS impossibility'},
 separators=(',',':'))+'\n')
print('all',triples,'triangles; extendibility-eligible',len(records))
print('elementary obstruction histogram',dict(sorted(hist.items())))
print('wrote',out.name)
