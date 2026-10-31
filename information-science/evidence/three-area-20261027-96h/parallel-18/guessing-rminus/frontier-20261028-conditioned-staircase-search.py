#!/usr/bin/env python3
"""Sample conditional 2026 staircase inequalities on a fixed LP base profile.

Tests extra outer conditioning W, unlike the preceding unconditioned scan.
Entropy coordinates and signs use exact integer arithmetic; sampling is not an
exhaustive global test. A found cut still requires source/proof and graph duals.
"""
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec,spec_from_file_location
from math import lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-conditioned-staircase-search-result.json'
spec=spec_from_file_location('stairs',ROOT/'frontier-20261028-staircase-family-scan.py')
source=module_from_spec(spec);spec.loader.exec_module(source)
SEED=2026102803
BATCH=100000
MAX_BATCHES=30


def main():
    start=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    rows=json.loads(raw)['primal_values'];vals={tuple(x['entropy_variables']):Fraction(x['value']) for x in rows}
    names='abcdefghij';h=[Fraction(0)]+[vals[tuple(names[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    stairs={}
    for triple,cells in source.staircases(5):stairs.setdefault(triple,cells)
    triples=sorted(stairs);bits=1<<np.arange(10,dtype=np.int64);rng=np.random.default_rng(SEED)
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    count=0;active_count=0;found=None;min_slack=0
    for batch in range(MAX_BATCHES):
        digits=rng.integers(0,7,size=(BATCH,10),dtype=np.int8)
        masks=[((digits==role)*bits).sum(axis=1,dtype=np.int64) for role in range(1,7)]
        good=(masks[0]>0)&(masks[1]>0)&(masks[2]>0)&(masks[3]>0)&(masks[0]<masks[1])
        A,B,C,D,Z,W=(m[good] for m in masks);count+=len(A)
        if not len(A):continue
        g=I(A,B,Z|W)
        v=-I(A,B,W)+I(A,B,C|W)+I(A,B,D|W)+I(C,D,W)+I(A,Z,B|W)+I(B,Z,A|W)
        c=I(A,C,B|W)+I(B,C,A|W);d=I(A,D,B|W)+I(B,D,A|W)
        if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('NEGATIVE_SHANNON_COMPONENT')
        active=np.flatnonzero(v<0);active_count+=len(active)
        for alpha,beta,gamma in triples:
            if not len(active):break
            s=g[active]+alpha*v[active]+beta*c[active]+gamma*d[active]
            min_slack=min(min_slack,int(s.min()))
            negative=np.flatnonzero(s<0)
            if len(negative):
                i=int(active[int(negative[0])])
                found={'masks':[int(x[i]) for x in (A,B,C,D,Z,W)],
                       'triplet':[alpha,beta,gamma],'staircase_cells':stairs[(alpha,beta,gamma)],
                       'scaled_terms':{'g':int(g[i]),'v':int(v[i]),'c':int(c[i]),'d':int(d[i])},
                       'exact_slack':str(Fraction(int(g[i]+alpha*v[i]+beta*c[i]+gamma*d[i]),scale)),
                       'batch':batch}
                break
        if found:break
    out={'point_sha256':EXPECTED,'source_pdf_sha256':source.SOURCE_SHA,'seed':SEED,
         'batch_size':BATCH,'max_batches':MAX_BATCHES,'staircases':len(triples),
         'nonempty_ordered_substitutions_checked':count,'negative_inner_term_count':active_count,
         'min_scaled_slack':min_slack,'exact_violation':found,'elapsed_s':time.monotonic()-start,
         'limits':'Sampled disjoint substitutions of 2026 source family, conditioned on additional W; not exhaustive, not an entropic law or graph-bound certificate.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
