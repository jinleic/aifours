#!/usr/bin/env python3
"""Sample overlapping blocks for both infinite five-variable source families.

Finite random variables may themselves be overlapping tuples; conditioning is
also allowed to overlap. Every tested value uses integer entropy numerators.
No violation proves nothing beyond the sample.
"""
from fractions import Fraction
from hashlib import sha256
from math import comb,lcm
from pathlib import Path
import json
import time
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-separator-bound-primal.json'
EXPECTED='aadf84109c619791c5882cb688a30facdbf25b3ae5a6ddde25d17b2e7ef6b651'
OUTPUT=ROOT/'frontier-20261028-overlap-five-variable-search-result.json'
SEED=2026102804
BATCH=100000
BATCHES=30
DENSITIES=(0.12,0.22,0.35,0.50)


def main():
    started=time.monotonic();raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    items=json.loads(raw)['primal_values'];values={tuple(x['entropy_variables']):Fraction(x['value']) for x in items}
    letters='abcdefghij';h=[Fraction(0)]+[values[tuple(letters[i] for i in range(10) if m&(1<<i))] for m in range(1,1024)]
    scale=lcm(*(v.denominator for v in h));H=np.array([int(v*scale) for v in h],dtype=np.int64)
    if max(abs(int(v)) for v in H)>=10**8:raise ValueError('INTEGER_RANGE')
    def I(a,b,z):return H[a|z]+H[b|z]-H[a|b|z]-H[z]
    rng=np.random.default_rng(SEED);bits=1<<np.arange(10,dtype=np.int64)
    records=[];profiles={};second_violation=None
    for density in DENSITIES:
        checked=negative=0
        for batch in range(BATCHES):
            samples=rng.random((BATCH,6,10))<density
            masks=(samples*bits).sum(axis=2,dtype=np.int64)
            valid=np.all(masks[:,:4]!=0,axis=1)
            A,B,C,D,Z,W=(masks[valid,j] for j in range(6));checked+=len(A)
            if not len(A):continue
            g=I(A,B,Z|W);z=I(A,Z,B|W)+I(B,Z,A|W)
            c=I(A,C,B|W)+I(B,C,A|W);d=I(A,D,B|W)+I(B,D,A|W)
            v=-I(A,B,W)+I(A,B,C|W)+I(A,B,D|W)+I(C,D,W)+z
            if np.any(g<0) or np.any(c<0) or np.any(d<0):raise ValueError('NEGATIVE_SHANNON_COMPONENT')
            active=np.flatnonzero(v<0);negative+=len(active)
            for i in active:
                profile=(int(g[i]),int(v[i]),int(c[i]),int(d[i]))
                profiles.setdefault(profile,[int(x[i]) for x in (A,B,C,D,Z,W)])
            slope=-I(A,C,W)+I(A,C,B|W)+I(A,C,D|W)+I(B,D,W)+z
            Cterm=c
            if np.any((Cterm==0)&(slope<0)):
                i=int(np.flatnonzero((Cterm==0)&(slope<0))[0]);k=int(g[i]//(-slope[i])+1)
            else:
                nz=Cterm>0;kstar=np.ones(len(A),dtype=np.int64)
                kstar[nz]=np.maximum(1,-np.floor_divide(slope[nz],Cterm[nz]))
                bound=int(max(np.max(np.abs(g)),np.max(np.abs(slope)),np.max(np.abs(Cterm)),1))
                maximum=int(kstar.max())
                if 2*bound*(maximum+1)**2>=2**62:raise ValueError('INTEGER_RANGE')
                twice=2*g+2*kstar*slope+kstar*(kstar-1)*Cterm
                bad=np.flatnonzero(twice<0)
                if not len(bad):continue
                i=int(bad[0]);k=int(kstar[i])
            slack=Fraction(int(2*g[i]+2*k*slope[i]+k*(k-1)*Cterm[i]),2*scale)
            if slack>=0:raise ValueError('BAD_SECOND_WITNESS')
            second_violation={'masks':[int(x[i]) for x in (A,B,C,D,Z,W)],'k':k,'slack':str(slack)}
            break
        records.append({'density':density,'checked':checked,'negative_first_inner':negative})
        if second_violation:break
    first_violation=None;tested=0;range_blocker=None
    for (g,v,c,d),masks in profiles.items():
        if c==0 or d==0:
            count=g//(-v)+1
            cells=[(i,0) for i in range(count)] if c==0 else [(0,j) for j in range(count)]
            first_violation={'masks':masks,'profile':[g,v,c,d],'cells':cells,'slack':str(Fraction(g+count*v,scale))}
            break
        imax=(-v-1)//c;jmax=(-v-1)//d
        if max(imax,jmax)>1000:
            range_blocker={'masks':masks,'profile':[g,v,c,d],'imax':imax,'jmax':jmax};break
        value=g;alpha=beta=gamma=0;cells=[]
        for i in range(imax+1):
            for j in range((-v-1-i*c)//d+1):
                w=comb(i+j,i);alpha+=w;beta+=i*w;gamma+=j*w;value+=w*(v+i*c+j*d);cells.append((i,j))
        tested+=1
        if value<0:
            first_violation={'masks':masks,'profile':[g,v,c,d],'triplet':[alpha,beta,gamma],
                             'cells':cells,'slack':str(Fraction(value,scale))};break
    out={'point_sha256':EXPECTED,'seed':SEED,'batch':BATCH,'batches_per_density':BATCHES,
         'density_results':records,'negative_first_profiles':len(profiles),'profiles_minimized':tested,
         'family1_exact_violation':first_violation,'family1_range_blocker':range_blocker,
         'family2_exact_violation':second_violation,'elapsed_s':time.monotonic()-started,
         'limits':'Sampled, not exhaustive; one non-entropic-feasibility-unestablished LP point. No global source-family or original bound follows without a separate certificate.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
