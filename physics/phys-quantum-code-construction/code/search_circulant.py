#!/usr/bin/env python3
"""Exhaust all 32 undirected circulant graph-state frames for ((11,5,4)).

No claim about other graphs or general quantum codes follows from a miss.
"""
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
N=11


def error_pairs():
    out=[]
    for weight in range(1,4):
        for support in combinations(range(N),weight):
            for symbols in product((1,2,3),repeat=weight):
                x=sum(1<<i for i,p in zip(support,symbols) if p&1)
                z=sum(1<<i for i,p in zip(support,symbols) if p&2)
                out.append((x,z))
    return out


def graph_rows(mask):
    offsets=[j+1 for j in range(5) if mask>>j&1]
    return [sum(1<<((i+d)%N) for d in offsets)+sum(1<<((i-d)%N) for d in offsets)
            for i in range(N)]


def allowed_words(rows,errors):
    forbidden=set()
    zero_x=[]
    for x,z in errors:
        syndrome=z
        while x:
            bit=x&-x
            syndrome ^= rows[bit.bit_length()-1]
            x^=bit
        if syndrome:
            forbidden.add(syndrome)
    # Separate loop retains the original x for every zero syndrome.
    for x,z in errors:
        syndrome=z
        for i,row in enumerate(rows):
            if x>>i&1:
                syndrome ^= row
        if not syndrome:
            zero_x.append(x)
    return [c for c in range(1,1<<N) if c not in forbidden and
            all((c&x).bit_count()%2==0 for x in zero_x)]


def find_clique(vertices,need):
    allowed=set(vertices)
    adjacency=[]
    for i,a in enumerate(vertices):
        adjacency.append(sum(1<<j for j in range(i+1,len(vertices)) if a^vertices[j] in allowed))
    calls=0
    def recurse(candidates,left):
        nonlocal calls
        calls+=1
        if left==0:
            return []
        while candidates.bit_count()>=left:
            bit=candidates&-candidates
            candidates^=bit
            i=bit.bit_length()-1
            result=recurse(candidates&adjacency[i],left-1)
            if result is not None:
                return [vertices[i]]+result
        return None
    result=recurse((1<<len(vertices))-1,need)
    return result,calls


def main():
    errors=error_pairs()
    records=[]
    for mask in range(32):
        rows=graph_rows(mask)
        allowed=allowed_words(rows,errors)
        hit,calls=find_clique(allowed,4)
        anchor,_=find_clique(allowed,3)
        records.append({'connection_mask':mask,'offsets':[j+1 for j in range(5) if mask>>j&1],
                        'adjacency_rows':rows,'allowed_words':allowed,
                        'target_five_words':None if hit is None else [0]+hit,
                        'control_four_words':None if anchor is None else [0]+anchor,
                        'target_recursion_nodes':calls})
    out={'n':11,'distance':4,'target_K':5,'graph_frames':32,'errors_per_graph':len(errors),
         'target_hits':sum(r['target_five_words'] is not None for r in records),
         'control_hits':sum(r['control_four_words'] is not None for r in records),
         'records':records,'scope':'Only simple undirected circulant graph-state CWS frames, all word sets; no global claim'}
    (ROOT/'results/circulant-11-5-4.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Circulant graph frames:',out['graph_frames'],'; Pauli errors per frame:',len(errors))
    print('K=5 hits:',out['target_hits'],'; K=4 control hits:',out['control_hits'])
    print('Allowed-word sizes:',[len(r['allowed_words']) for r in records])
    print('Total target recursion nodes:',sum(r['target_recursion_nodes'] for r in records))


if __name__=='__main__':
    main()
