#!/usr/bin/env python3
"""Exact syndrome audit for one q=8 R-minus triangle-cover strategy.

For every nonzero parity syndrome, seek an explicit difference with an isolated
vertex. This proves a two-coset restriction, not a global guessing-number bound.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-triangle-coset-obstruction-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triples=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    if len(triples)!=10 or len(set(triples))!=10:raise ValueError('COVER_SIZE')
    if any(len(t)!=3 or len(set(t))!=3 or any(b not in N[a] for a in t for b in t if a!=b) for t in triples):
        raise ValueError('NOT_TRIANGLES')
    if any(sum(v in t for t in triples)!=3 for v in range(1,11)):raise ValueError('NOT_TRIPLE_COVER')
    stars={};coverable={};allowed_sets={}
    for v in range(1,11):
        allowed={v}|(set(range(1,11))-set(N[v])-{v})
        allowed_sets[v]=allowed
        stars[v]=sum(1<<i for i,t in enumerate(triples) if v in t)
        coverable[v]=sum(1<<i for i,t in enumerate(triples) if set(t)&allowed)
    counts=Counter();uncovered=[];witnesses=[]
    for syndrome in range(1,1024):
        viable=[v for v in range(1,11)
                if syndrome&stars[v] and not syndrome & (~coverable[v] & 1023)]
        counts[len(viable)]+=1
        if not viable:uncovered.append(syndrome);continue
        v=viable[0];local=[]
        for i,t in enumerate(triples):
            bit=(syndrome>>i)&1
            chosen=None
            if bit:
                chosen=v if v in t else next(u for u in t if u in allowed_sets[v])
            local.append(chosen)
        if not any(local[i]==v for i in range(10)):raise ValueError('ISOLATED_VERTEX_ZERO')
        if any(u in N[v] for u in local if u is not None):raise ValueError('NEIGHBOUR_NONZERO')
        if sum((u is not None)<<i for i,u in enumerate(local))!=syndrome:raise ValueError('WRONG_SYNDROME')
        witnesses.append({'syndrome':syndrome,'isolated_vertex':v,'triangle_coordinate_nonzero_vertex':local})
    out={'input_sha256':EXPECTED,'triples':triples,'star_masks':stars,'coverable_masks':coverable,
         'nonzero_syndromes_checked':1023,'uncovered_syndromes':uncovered,
         'all_nonzero_syndromes_have_isolated_vertex_witness':not uncovered,
         'isolating_vertex_count_distribution':dict(sorted(counts.items())),
         'witnesses':witnesses,
         'limits':'If every syndrome is covered, no subset of the union of the baseline code and ONE other coset has size > baseline; arbitrary multi-coset or nonlinear strategies remain open.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))


if __name__=='__main__':main()
