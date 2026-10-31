#!/usr/bin/env python3
"""Construct and exactly check a 9-word FD support without a 3-group split."""
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-nine-word-coloring-obstruction-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
FACTORS=((1,2,3),(1,3,4),(2,3,9),(3,4,8),(3,8,9))
PICKS=((0,(1,2)),(1,(1,3)),(1,(1,4)),(2,(2,3)),(2,(2,9)),(3,(4,8)),(4,(3,8)),(4,(3,9)))
WHEEL=(1,2,3,4,8,9);HUB=3


def main():
    for T in FACTORS:
        if any(v not in N[u] for u,v in combinations(T,2)):raise ValueError('NOT_TRIANGLE')
    words=[tuple([0]*10)]
    for t,e in PICKS:
        if not set(e)<=set(FACTORS[t]):raise ValueError('BAD_PICK')
        words.append(tuple((1<<t) if v in e else 0 for v in range(1,11)))
    if len(set(words))!=9:raise ValueError('DISTINCT')
    for word in words:
        for t,T in enumerate(FACTORS):
            if sum((word[v-1]>>t)&1 for v in T)%2:raise ValueError('XOR')
    differences=[]
    for x,y in combinations(range(9),2):
        D=tuple(v for v in range(1,11) if words[x][v-1]!=words[y][v-1]);differences.append({'word_pair':[x,y],'difference_vertices':D})
        if any(not any(w in D for w in N[v]) for v in D):raise ValueError('FD')
    wheel_edges={tuple(sorted((u,v))) for u,v in combinations(WHEEL,2) if v in N[u]}
    forced={tuple(d['difference_vertices']) for d in differences if len(d['difference_vertices'])==2}
    if len(wheel_edges)!=10 or not wheel_edges<=forced:raise ValueError('WHEEL_FORCE')
    valid=0
    for colors in product(range(3),repeat=6):
        col=dict(zip(WHEEL,colors))
        if all(col[u]!=col[v] for u,v in wheel_edges):valid+=1
    if valid:raise ValueError('WHEEL_COLORABLE')
    out={'vertices':list(range(1,11)),'alphabet_size':32,'triangles':FACTORS,'selected_edge_words':PICKS,
         'words':words,'difference_sets':differences,'forced_wheel_vertices':WHEEL,'forced_wheel_hub':HUB,
         'forced_wheel_edges':sorted(wheel_edges),'wheel_three_colorings_checked':3**6,'proper_wheel_three_colorings':valid,
         'all_checked':True,'limits':'A graph-FD support obstructing the three-group proof method, not a strict-gap FD law or guessing-number improvement.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('words','difference_sets')},indent=2))


if __name__=='__main__':main()
