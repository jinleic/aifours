#!/usr/bin/env python3
"""Compare the cited expanded move input to all affine planes avoiding origin."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/balanced-nl242/frontier-20261028-seed1-second-layer-results.json')
EXPECTED='bc2d389fbba21515ba8e52c78b327eb5859080a007816f97cc59d87afb8c537d'
OUTPUT=ROOT/'frontier-review-f60-move-input-check-result.json'


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    obj=json.loads(raw);nodes=obj['seeds']
    if len(nodes)!=45:raise ValueError('NODE_COUNT')
    observed=set()
    for node in nodes:
        qs=node['preserving_quads']
        if len(qs)!=node['peak_preserving_count']:raise ValueError('ROW_COUNT')
        for q in qs:
            if len(q)!=4 or len(set(q))!=4 or any(not isinstance(x,int) or not 0<=x<512 for x in q):
                raise ValueError('BAD_QUAD')
            observed.add(tuple(sorted(q)))
    basis=(27,45,195,325);offset=[]
    for u in range(16):
        x=365
        for i,b in enumerate(basis):
            if u&(1<<i):x^=b
        offset.append(x)
    if len(set(offset))!=16:raise ValueError('BAD_BASIS')
    expected={tuple(sorted(offset[i] for i in q)) for q in combinations(range(1,16),4)
              if q[0]^q[1]^q[2]^q[3]==0}
    if len(expected)!=105 or observed!=expected:raise ValueError(('MOVE_SET_MISMATCH',len(observed),len(expected)))
    out={'input_sha256':EXPECTED,'source_nodes':len(nodes),'input_union_moves':len(observed),
         'all_affine_2_planes_avoiding_origin_count':len(expected),'exact_move_set_equality':True,
         'limits':'This checks the cited expanded-move set against independently generated affine planes; it does not by itself validate the prior second-layer search history.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
