#!/usr/bin/env python3
"""Independent direct inclusion-exclusion replay for every factor cover."""
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-two-syndrome-full-census-result.json','c36f2adbf02f6dc926693c29d991f8d9c4c58536c64159c132f8f14fc559f47c')
OUT=ROOT/'frontier-20261028-two-syndrome-full-independent-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def masks_direct(J):
    fs=[t for t in range(10) if J>>t&1];k=len(fs);allf=(1<<k)-1
    factor=[sum(1<<i for i,t in enumerate(fs) if v in TRI[t]) for v in range(1,11)]
    uv=[0]*1024;size=[0]*1024
    for M in range(1,1024):
        bit=M&-M;v=bit.bit_length()-1;p=M^bit;uv[M]=uv[p]|factor[v];size[M]=size[p]+factor[v].bit_count()
    base=[1<<(size[M]-uv[M].bit_count()) for M in range(1024)];full=[base[M] if uv[M]==allf else 0 for M in range(1024)]
    nb=[sum(1<<(u-1) for u in N[v]) for v in range(1,11)];out=[]
    for M in range(1,1024):
        if not all(M&nb[v] for v in range(10) if M>>v&1):continue
        a=b=0;L=M
        while True:
            sign=-1 if (M.bit_count()-L.bit_count())&1 else 1
            a+=sign*base[L];b+=sign*full[L]
            if not L:break
            L=(L-1)&M
        if a<0 or b<0:raise ValueError('NEGATIVE_COUNT')
        if a or b:out.append(M)
    return out


def colorcheck(masks,color):
    if len(color)!=10 or any(c not in (0,1,2) for c in color):raise ValueError('COLOR_FORMAT')
    C=[sum(1<<i for i,c in enumerate(color) if c==j) for j in range(3)]
    if any(any(D&~mask==0 for mask in C) for D in masks):raise ValueError('COLOR')


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw)
    table={r['factor_mask']:r for r in src['cases']};covers={J for J in range(1,1024) if set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))==set(N)}
    if len(covers)!=420 or set(table)!=covers:raise ValueError('COVERAGE')
    counts={};checked_masks=0;first=None
    for J,r in sorted(table.items()):
        direct=masks_direct(J)
        if direct!=r['allowed_difference_masks']:raise ValueError(('MASKS',J))
        checked_masks+=len(direct);k=str(J.bit_count());counts.setdefault(k,{'covers':0,'colorable':0,'no_universal_color':0});counts[k]['covers']+=1
        if r['color'] is None:counts[k]['no_universal_color']+=1
        else:
            colorcheck(direct,r['color']);counts[k]['colorable']+=1
            if first is None:first=direct
    if counts!=src['cover_counts']:raise ValueError('COUNTS')
    try:colorcheck(first,[0]*10)
    except ValueError as exc:
        if str(exc)!='COLOR':raise ValueError('WRONG_REASON')
    else:raise ValueError('CONTROL')
    out={'source_receipt_sha256':SOURCE[1],'factor_subsets':1023,'noncovers':603,'covers_checked':len(table),
         'allowed_mask_entries_checked':checked_masks,'cover_counts':counts,'all_checked':True,
         'controls':{'monochrome_color':'COLOR'},
         'limits':'Exact support-mask and supplied-color replay. Nonexistence of colors in the 95 residual cases requires separate fractional-dual certificates.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
