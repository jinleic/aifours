#!/usr/bin/env python3
"""Exact bipartite crossover of actual binary R-minus FD supports.

For an FD-valid support S and each graph-automorphism/bit-flip image T, find a
maximum FD-valid subset of S union T using bipartite maximum matching. Any
winning support is verified independently by original-neighbour lookup. This
is a bounded search, not a global optimum or alphabet restriction theorem.
"""
from collections import deque
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import time

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-fd-law-search-precise-result.json'
EXPECTED='c82613f4fb2ae9f70192eedf73c5cc755de332e3be4d8cb0ddedc20899586bfc'
OUTPUT=ROOT/'frontier-20261028-binary-isometry-crossover-result.json'
NEIGHBOURS={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
            5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
            9:(2,3,5,6,8),10:(2,4,5,7,8)}
GENS=((7,9,6,5,8,2,3,0,1,4),(0,4,5,6,1,2,3,7,8,9))
MAX_WALL=35.0
MAX_ROUNDS=3


def valid(words):
    tables={v:{} for v in range(1,11)}
    for w in words:
        for v,ns in NEIGHBOURS.items():
            key=tuple((w>>(u-1))&1 for u in ns);bit=(w>>(v-1))&1
            if key in tables[v] and tables[v][key]!=bit:return False
            tables[v][key]=bit
    return len(words)==len(set(words))


def automorphisms():
    edges={frozenset((u-1,v-1)) for u,ns in NEIGHBOURS.items() for v in ns}
    if len(edges)!=26:raise ValueError('EDGE_COUNT')
    for p in GENS:
        if {frozenset(p[i] for i in e) for e in edges}!=edges:raise ValueError('AUTOMORPHISM')
    found={tuple(range(10))};queue=deque(found)
    while queue:
        p=queue.popleft()
        for g in GENS:
            q=tuple(g[p[i]] for i in range(10))
            if q not in found:found.add(q);queue.append(q)
    return sorted(found)


def permute(w,p):return sum(1<<p[i] for i in range(10) if w&(1<<i))


def choose_union(S,T,bad):
    common=S&T;L=sorted(S-T);R=sorted(T-S)
    adjacency=[[j for j,b in enumerate(R) if (a^b) in bad] for a in L]
    pairL=[-1]*len(L);pairR=[-1]*len(R)
    while True:
        dist=[-1]*len(L);Q=deque()
        for i in range(len(L)):
            if pairL[i]<0:dist[i]=0;Q.append(i)
        while Q:
            i=Q.popleft()
            for j in adjacency[i]:
                p=pairR[j]
                if p>=0 and dist[p]<0:dist[p]=dist[i]+1;Q.append(p)
        def dfs(i):
            for j in adjacency[i]:
                p=pairR[j]
                if p<0 or (dist[p]==dist[i]+1 and dfs(p)):
                    pairL[i]=j;pairR[j]=i;return True
            dist[i]=-1;return False
        progress=sum(1 for i in range(len(L)) if pairL[i]<0 and dfs(i))
        if not progress:break
    # Alternating reachability from unmatched L: independent set is reachable L
    # plus nonreachable R; common vertices are compatible with both sides.
    seenL={i for i in range(len(L)) if pairL[i]<0};seenR=set();Q=deque(seenL)
    while Q:
        i=Q.popleft()
        for j in adjacency[i]:
            if pairL[i]==j or j in seenR:continue
            seenR.add(j);p=pairR[j]
            if p>=0 and p not in seenL:seenL.add(p);Q.append(p)
    chosen=common|{L[i] for i in seenL}|{R[j] for j in range(len(R)) if j not in seenR}
    matching=sum(p>=0 for p in pairL)
    if len(chosen)!=len(S|T)-matching:raise ValueError('MATCHING_COVER_IDENTITY')
    return chosen,matching


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    best=set(json.loads(raw)['support_words_one_based_bitsets'])
    if len(best)!=88 or not valid(sorted(best)):raise ValueError('INVALID_START')
    masks={v:sum(1<<(u-1) for u in ns) for v,ns in NEIGHBOURS.items()}
    bad={d for d in range(1,1024) if any(d&(1<<(v-1)) and not d&mask for v,mask in masks.items())}
    if len(bad)!=113:raise ValueError('FORBIDDEN_DIFF_COUNT')
    group=automorphisms();history=[];stop='round limit'
    for round_index in range(MAX_ROUNDS):
        incumbent=set(best);candidate=set(best);tested=0;complete=True
        for p in group:
            image={permute(w,p) for w in incumbent}
            for shift in range(1024):
                if time.monotonic()-start>MAX_WALL:complete=False;break
                other={w^shift for w in image}
                chosen,_=choose_union(incumbent,other,bad);tested+=1
                if len(chosen)>len(candidate):
                    if not valid(sorted(chosen)):raise ValueError('INVALID_CROSSOVER')
                    candidate=chosen
            if not complete:break
        history.append({'round':round_index,'starting_size':len(incumbent),'transformations_examined':tested,
                        'all_8192_examined':complete,'best_union_subset_size':len(candidate),
                        'strict_original_gain':len(candidate)**3>2**20})
        if len(candidate)>len(best):best=candidate
        else:stop='no improvement within examined isometry crossover';break
        if len(best)**3>2**20:stop='strict original gain candidate found';break
        if not complete:stop='wall limit after improvement';break
    out={'input_sha256':EXPECTED,'automorphism_group_size':len(group),'forbidden_binary_differences':len(bad),
         'rounds':history,'best_size':len(best),'best_support':sorted(best),'independent_lookup_check':valid(sorted(best)),
         'strict_original_20_over_3_gain_exact':len(best)**3>2**20,'stop':stop,'elapsed_s':time.monotonic()-start,
         'limits':'Only two-set isometry crossovers of the recorded incumbent and binary alphabet. No general q=2 or arbitrary-alphabet upper bound follows.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='best_support'},indent=2))


if __name__=='__main__':main()
