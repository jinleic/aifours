#!/usr/bin/env python3
"""Exact-integer sampled search for F_n violations with overlapping blocks.

Samples substitutions on a fixed partial relaxation point; unlike the prior
exhaustive scan, A,B,C,D,Z are allowed to overlap. A found cut is a candidate
for the source-core LP, not a graph-theorem or an entropic violation.
"""
from fractions import Fraction
from hashlib import sha256
from math import lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED='97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'
OUTPUT=ROOT/'frontier-20261028-overlap-fn-search-result.json'
SEED=2026102802
BATCH=100000
BATCHES_PER_DENSITY=10
DENSITIES=(0.12,0.25,0.40,0.60)


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    entries=json.loads(raw)['primal_values'];values={tuple(x['entropy_variables']):Fraction(x['value']) for x in entries}
    BASE='abcdefghij'
    h=[Fraction(0)]+[values[tuple(BASE[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(x.denominator for x in h));H=np.array([int(x*scale) for x in h],dtype=np.int64)
    rng=np.random.default_rng(SEED);bits=(1<<np.arange(10,dtype=np.int64))
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    totals=[];found=None
    for density in DENSITIES:
        scanned=0
        for batch in range(BATCHES_PER_DENSITY):
            sample=(rng.random((BATCH,5,10))<density)
            masks=(sample*bits).sum(axis=2,dtype=np.int64)
            valid=np.all(masks[:,:4]!=0,axis=1)
            A,B,C,D,Z=(masks[valid,i] for i in range(5));scanned+=len(A)
            if not len(A):continue
            a=I(A,B,C|Z);c=a+I(A,B,D|Z)+I(C,D,Z)-I(A,B,Z)
            d=I(A,C,B|Z)+I(B,C,A|Z)
            if np.any(a<0) or np.any(d<0):raise ValueError('SHANNON_INPUT_FAILURE')
            zero=(d==0)&(c<0)
            if np.any(zero):
                j=int(np.flatnonzero(zero)[0]);n=int(a[j]//(-c[j])+1)
            else:
                nstar=np.ones(len(A),dtype=np.int64);nz=d>0
                nstar[nz]=np.maximum(1,-np.floor_divide(c[nz],d[nz])-1)
                maximum=int(max(np.max(np.abs(a)),np.max(np.abs(c)),np.max(np.abs(d)),1))
                nmax=int(nstar.max())
                if 2*maximum*(nmax+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
                twice=2*a+2*nstar*c+nstar*(nstar+1)*d
                bad=np.flatnonzero(twice<0)
                if not len(bad):continue
                j=int(bad[0]);n=int(nstar[j])
            args=[int(x[j]) for x in (A,B,C,D,Z)]
            slack=Fraction(int(2*a[j]+2*n*c[j]+n*(n+1)*d[j]),2*scale)
            if not slack<0:raise ValueError(('BAD_WITNESS',args,n,slack))
            found={'masks':args,'n':n,'exact_slack':str(slack),
                   'scaled_a':int(a[j]),'scaled_c':int(c[j]),'scaled_d':int(d[j]),
                   'density':density,'batch':batch}
            break
        totals.append({'density':density,'nonempty_substitutions_checked':scanned})
        if found:break
    out={'input_sha256':EXPECTED,'seed':SEED,'scale':scale,'batch_size':BATCH,
         'batches_per_density':BATCHES_PER_DENSITY,'densities':DENSITIES,
         'counts':totals,'witness':found,'elapsed_s':time.monotonic()-started,
         'limits':'Random overlapping-block substitutions on one relaxation point; no witness does not establish all-overlap validity or any original bound.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
