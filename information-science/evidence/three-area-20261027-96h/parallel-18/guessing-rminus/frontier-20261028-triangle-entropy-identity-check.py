#!/usr/bin/env python3
"""Integer-coefficient check of the triangle entropy-gap identity.

Thirty formal component variables are indexed by triangle position. The
identity holds before imposing the triangle conditional-FD equalities.
No entropy values, floating arithmetic, or source-specific LP are used.
"""
from collections import defaultdict
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-triangle-entropy-identity-check-result.json'


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triples=[tuple(t) for t in json.loads(raw)['chosen_triangles']]
    if len(triples)!=10 or any(len(set(t))!=3 for t in triples):raise ValueError('TRIPLES')
    forms=defaultdict(int);own={v:0 for v in range(1,11)};past=0
    def add(mask,c):
        if mask:forms[mask]+=c
    def cmi(x,y,z,weight=1):
        add(z|x,weight);add(z|y,weight);add(z|x|y,-weight);add(z,-weight)
    triangle_cmis=temporal_cmis=triangle_fds=0
    for t in triples:
        j=triangle_cmis//3
        bits=[1<<(3*j+i) for i in range(3)];allbits=bits[0]|bits[1]|bits[2]
        for i,k in combinations(range(3),2):
            cmi(bits[i],bits[k],past);triangle_cmis+=1
        for v,current in zip(t,bits):
            cmi(current,past,own[v],2);temporal_cmis+=1
            own[v] |= current
        # Subtract the three formal triangle conditional-FD terms.
        for i,k in combinations(range(3),2):
            add(past|allbits,-1);add(past|bits[i]|bits[k],1);triangle_fds+=1
        past |= allbits
    # Subtract the proposed gap 2*sum H(X_v) - 3*H(X_all).
    for mask in own.values():add(mask,-2)
    add(past,3)
    remainder={str(m):c for m,c in forms.items() if c}
    if remainder:raise ValueError(('NONZERO_REMAINDER',remainder))
    out={'baseline_result_sha256':EXPECTED,'component_variables':30,'triangle_terms':10,
         'pair_conditional_mutual_informations':triangle_cmis,
         'temporal_conditional_mutual_informations_weight_2':temporal_cmis,
         'triangle_conditional_FD_terms_subtracted':triangle_fds,
         'integer_coefficient_remainder':remainder,
         'limits':'Symbolic entropy identity checked exactly; its use for entropy ratios requires all named triangle FD equalities and the written nonnegative-CMI argument.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
