#!/usr/bin/env python3
"""Replay all half-frame obstruction witnesses without producer imports.

Independently generates dephased rows recursively, recomputes compatibility,
checks exact coverage and each isolated-vertex/odd-cut certificate.
"""
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
second=(0,0,1,1,2,2,3,3,4,4);zero=(0,)*10
rows=[]; remaining=[1,2,2,2,2]; current=[0]

def balanced(a,b):
    freq=[0]*5
    for x,y in zip(a,b):freq[(x-y)%5]+=1
    return freq==[2]*5

def generate():
    if len(current)==10:
        row=tuple(current)
        if balanced(row,second):rows.append(row)
        return
    for value in range(5):
        if remaining[value]:
            remaining[value]-=1;current.append(value);generate();current.pop();remaining[value]+=1

generate();assert len(rows)==1075 and rows==sorted(rows)
adj=[0]*len(rows);edges=0
for i in range(len(rows)):
    for j in range(i+1,len(rows)):
        if balanced(rows[i],rows[j]):
            adj[i]|=1<<j;adj[j]|=1<<i;edges+=1
assert edges==26715

D=json.loads((ROOT/'frontier-20261028-bh10-structural-cert-v1.json').read_text())
assert D['candidate_count']==len(rows)
records=D['certificates'];assert len(records)==16064
listed={}
for item in records:
    key=tuple(item['triple'])
    assert len(key)==3 and 0<=key[0]<key[1]<key[2]<len(rows) and key not in listed
    listed[key]=item

triangles=eligible=0
for i in range(len(rows)):
    js=adj[i]&~((1<<(i+1))-1)
    while js:
        bit=js&-js;js-=bit;j=bit.bit_length()-1
        ks=adj[i]&adj[j]&~((1<<(j+1))-1)
        while ks:
            bit=ks&-ks;ks-=bit;k=bit.bit_length()-1;triangles+=1
            if (adj[i]&adj[j]&adj[k]).bit_count()<5:continue
            eligible+=1
            item=listed.pop((i,j,k))
            E=(zero,second,rows[i],rows[j],rows[k])
            def edge(c,d):return len({(row[c]-row[d])%5 for row in E})==5
            if 'isolated' in item:
                v=item['isolated'];assert 0<=v<10
                assert all(not edge(v,w) for w in range(10) if w!=v)
            else:
                S=set(item['odd_component'])
                assert 0<len(S)<10 and len(S)%2==1 and S<=set(range(10))
                assert all(not edge(v,w) for v in S for w in set(range(10))-S)
assert triangles==53065 and eligible==16064 and not listed
print('PASS independent recursive 22680 balanced-row generation; 1075 candidates; 26715 edges')
print('PASS all53065 triangles; exactly16064 eligible triples covered once')
print('PASS each eligible graph has independently verified isolated vertex or odd cut')
print('consequence needs written BH normalization/physical transversal caller')
