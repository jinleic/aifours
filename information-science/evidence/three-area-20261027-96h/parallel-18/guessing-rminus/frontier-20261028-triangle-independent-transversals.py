#!/usr/bin/env python3
"""Exact finite graph hypotheses for the triangle-syndrome slice theorem."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-triangle-independent-transversals-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def independent(s):return all(b not in N[a] for a,b in combinations(s,2))


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    triples=[t for t in combinations(range(1,11),3) if independent(t)]
    fours=[t for t in combinations(range(1,11),4) if independent(t)]
    by_omitted={}
    for t in triples:
        covered=[i for i,tr in enumerate(triangles) if set(t)&set(tr)]
        omitted=[i for i in range(10) if i not in covered]
        if len(omitted)!=1:raise ValueError(('TRIPLE_NOT_NINE_COVER',t,omitted))
        by_omitted[str(omitted[0])]=list(t)
    pairs=[]
    for a,b in combinations(range(10),2):
        options=[s for r in (1,2) for s in combinations(range(1,11),r)
                 if independent(s) and set(s)&set(triangles[a]) and set(s)&set(triangles[b])]
        if not options:raise ValueError(('PAIR_NOT_HIT',a,b))
        pairs.append({'triangle_indices':[a,b],'independent_transversal':options[0]})
    out={'baseline_result_sha256':EXPECTED,'independent_triples':triples,
         'independent_4_sets':fours,'omitted_triangle_index_to_triple':by_omitted,
         'all_triangle_pairs_have_independent_transversal':True,'triangle_pairs_checked':len(pairs),
         'triangle_pair_witnesses':pairs,
         'limits':'The slice theorem applies to the recorded triangle code; no global guessing-number upper or nonlinear entropy-ratio upper is claimed.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps({k:v for k,v in out.items() if k!='triangle_pair_witnesses'},indent=2))


if __name__=='__main__':main()
