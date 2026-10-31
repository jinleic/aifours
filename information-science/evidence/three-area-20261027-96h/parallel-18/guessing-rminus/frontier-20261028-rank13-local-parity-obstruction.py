#!/usr/bin/env python3
"""Exact quotient obstruction for one rank-13 R-minus triangle subcode K.

Enumerates isolated-vertex difference images directly from 30-bit basis
coordinates, without importing the preceding syndrome search implementation.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'frontier-20261028-triangle-baseline-result.json'
EXPECTED='1ef666a1eaa04836d3ae07a0f91a8883b57f7130bc26e7bd41eb7e4c47e13e82'
OUTPUT=ROOT/'frontier-20261028-rank13-local-parity-obstruction-result.json'
ACTIVE={0,3,6,9}
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}


def rank(rows):
    piv={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j in piv:x ^= piv[j]
            else:piv[j]=x;break
    return len(piv)


def span(vectors):
    values={0}
    for x in vectors:values |= {a^x for a in tuple(values)}
    return values


def main():
    raw=INPUT.read_bytes()
    if sha256(raw).hexdigest()!=EXPECTED:raise ValueError('INPUT_HASH')
    triangles=[tuple(x) for x in json.loads(raw)['chosen_triangles']]
    occ={v:[j for j,t in enumerate(triangles) if v in t] for v in range(1,11)}
    if len(triangles)!=10 or any(len(o)!=3 for o in occ.values()):raise ValueError('COVER')
    pos={(v,j):3*(v-1)+occ[v].index(j) for v in range(1,11) for j in occ[v]}
    codeform={}
    for j,t in enumerate(triangles):
        for k,v in enumerate(t):
            codeform[v,j]=(1<<(2*j)) if k==0 else (1<<(2*j+1)) if k==1 else (3<<(2*j))
    local=[]
    for v in range(1,11):
        f=0
        for j in occ[v]:
            if j in ACTIVE:f ^= codeform[v,j]
        local.append(f)
    rows=[]
    for f in local:
        if rank(rows+[f])>len(rows):rows.append(f)
    if len(rows)!=7:raise ValueError('LOCAL_RANK')
    if any(rank(rows+[codeform[v,j] for j in occ[v]])-7!=2 for v in range(1,11)):
        raise ValueError('VERTEX_IMAGE_RANK')
    rowspace={0:0}
    for i,r in enumerate(rows):
        for a,k in tuple(rowspace.items()):rowspace[a^r]=k^(1<<i)
    lambdas=[rowspace[f] for f in local]
    # A formal component bit changes its triangle syndrome, and changes one
    # of the two code coefficients only if it is the first or second bit.
    tags={}
    for j,t in enumerate(triangles):
        for k,v in enumerate(t):
            c=(1<<(2*j+k)) if k<2 else 0
            r=sum(((c&f).bit_count()&1)<<i for i,f in enumerate(rows))
            tags[v,j]=(1<<j)|(r<<10)
    bad=set()
    for v in range(1,11):
        non=set(range(1,11))-set(N[v])-{v}
        nv=span([tags[u,j] for u in sorted(non) for j in occ[u]])
        own=[tags[v,j] for j in occ[v]]
        for x in range(1,8):
            u=0
            for i in range(3):
                if x&(1<<i):u ^= own[i]
            bad.update(u^a for a in nv)
    if 0 in bad:raise ValueError('K_IS_NOT_FD')
    def local_pattern(s,r):
        out=0
        for v in range(1,11):
            offset=sum((s>>j)&1 for j in occ[v] if j in ACTIVE and triangles[j].index(v)==2)%2
            out |= ((((lambdas[v-1]&r).bit_count()&1)^offset)<<(v-1))
        return out
    patterns=Counter();zero=[];single=[]
    for s in range(1024):
        for r in range(128):
            g=local_pattern(s,r);patterns[g]+=1;quotient=s|(r<<10)
            if g==0 and quotient not in bad:zero.append([s,r])
            if g.bit_count()==1 and quotient not in bad:single.append([g.bit_length(),s,r])
    if len(patterns)!=1024 or set(patterns.values())!={128}:raise ValueError('PATTERN_IMAGE')
    if zero!=[[0,0]]:raise ValueError(('ZERO_PATTERN',zero))
    if {x[0] for x in single}!={1,9} or len(single)!=12:raise ValueError(('SINGLETON_PATTERNS',single))
    out={'baseline_result_sha256':EXPECTED,'active_triangles':sorted(ACTIVE),
         'local_forms_in_20bit_code_coordinates':local,'quotient_basis_rows':rows,
         'K_dimension':13,'K_vertex_image_ranks':[2]*10,'all_quotient_cosets_checked':1<<17,
         'isolated_vertex_difference_classes':len(bad),'image_g_patterns':len(patterns),
         'preimages_per_g_pattern':128,'g_zero_compatible_cosets':zero,
         'g_singleton_compatible_cosets':sorted(single),
         'nonzero_g_singleton_compatible_vertices':sorted({x[0] for x in single}),
         'limits':'Rules out the 16-equiprobable-K-coset/2-of-16 criterion for this K; no bound for other subcodes or general distributions.'}
    with OUTPUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
