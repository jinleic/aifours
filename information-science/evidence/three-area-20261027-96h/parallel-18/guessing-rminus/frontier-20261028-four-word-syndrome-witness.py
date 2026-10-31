#!/usr/bin/env python3
"""Check a four-word FD law with a fair syndrome bit hidden from each vertex."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-four-word-syndrome-witness-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
WORDS=(649,759,697,711)


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    tr=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    occ={v:[j for j,t in enumerate(tr) if v in t] for v in range(1,11)}
    if any(len(a)!=3 for a in occ.values()):raise ValueError('COVER')
    def sigma(w):
        return sum((sum((w>>(v-1))&1 for v in t if occ[v][0]==j)%2)<<j for j,t in enumerate(tr))
    for x,y in combinations(WORDS,2):
        d=x^y
        for v in range(1,11):
            if d&(1<<(v-1)) and not any(d&(1<<(u-1)) for u in N[v]):raise ValueError(('FD',x,y,v))
    groups={s:[w for w in WORDS if sigma(w)==s] for s in sorted({sigma(w) for w in WORDS})}
    if sorted(groups)!=[51,53] or any(len(g)!=2 for g in groups.values()):raise ValueError('S_PROBABILITY')
    marg={}
    for v in range(1,11):
        counts=[sum((w>>(v-1))&1 for w in groups[s]) for s in (51,53)]
        if counts[0]!=counts[1]:raise ValueError(('NOT_INDEPENDENT',v))
        marg[v]=counts
    out={'triangle_cover_sha256':EXPECTED,'words':WORDS,'word_to_syndrome':{str(w):sigma(w) for w in WORDS},
         'original_graph_pairwise_FD_checks':60,'vertex_ones_given_each_syndrome':marg,
         'syndrome_entropy_bits':1,'every_vertex_mutual_information_with_syndrome_bits':0,
         'q8_embedding':'(bit,0,0) in each vertex triangle-occurrence coordinate order',
         'limits':'A counterexample to the separate syndrome-information inequality, not a guessing-number improvement.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
