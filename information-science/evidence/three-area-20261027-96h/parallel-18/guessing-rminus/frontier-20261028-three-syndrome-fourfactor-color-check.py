#!/usr/bin/env python3
"""Independent decoder-mask and coloring replay for four-factor syndrome planes."""
from hashlib import sha256
from itertools import combinations,product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
SRC=('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json','218c42798aa317236225f99e5b03f2cd6bd87c21cbaeb606ebdb54b53d1ac7a8')
OUT=ROOT/'frontier-20261028-three-syndrome-fourfactor-color-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def active_difference(factors):
    # Enumerate each factor's 3-bit difference independently; unlike the
    # producer this uses factor-local triples, not vertex-packed words.
    active=[set() for _ in range(16)]
    for bits in product(range(8),repeat=4):
        mask=0;syndrome=0
        for j,(t,x) in enumerate(zip(factors,bits)):
            if x.bit_count()&1:syndrome|=1<<j
            for i,v in enumerate(TRI[t-1]):
                if x>>i&1:mask|=1<<(v-1)
        if not mask:continue
        if any(mask>>(v-1)&1 and not any(mask>>(u-1)&1 for u in N[v]) for v in N):continue
        active[syndrome].add(mask)
    return active


def check_color(masks,color):
    if len(color)!=10 or any(c not in (0,1,2) for c in color):raise ValueError('COLOR_FORMAT')
    cols=[sum(1<<i for i,c in enumerate(color) if c==j) for j in range(3)]
    if any(D&~C==0 for D in masks for C in cols):raise ValueError('MONOCHROMATIC_DIFFERENCE')


def main():
    raw=(ROOT/SRC[0]).read_bytes()
    if sha256(raw).hexdigest()!=SRC[1]:raise ValueError('HASH')
    source=json.loads(raw);table={(tuple(r['factors']),tuple(r['syndrome_plane'])):r for r in source['cases']}
    if len(table)!=247:raise ValueError('DUPLICATE')
    covers=[F for F in combinations(range(1,11),4) if set().union(*(set(TRI[t-1]) for t in F))==set(N)]
    if len(covers)!=19:raise ValueError('COVERS')
    colors_checked=0;mask_checked=0;first=None
    for F in covers:
        g=active_difference(F)
        for a,b in combinations(range(1,16),2):
            c=a^b
            if b>=c or (a|b|c)!=15:continue
            rec=table.get((F,(a,b,c)))
            if rec is None:raise ValueError('PLANE_MISSING')
            expected=sorted(g[0]|g[a]|g[b]|g[c]);mask_checked+=len(expected)
            if expected!=rec['allowed_masks']:raise ValueError('DIFFERENCE_MASKS')
            if rec['color'] is not None:
                check_color(expected,rec['color']);colors_checked+=1
                if first is None:first=expected
    if colors_checked!=206:raise ValueError('COLOR_COUNT')
    try:check_color(first,[0]*10)
    except ValueError as e:control=str(e)
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'source_sha256':SRC[1],'all_checked':True,'covering_factor_sets':19,'plane_count':247,
         'universal_colors_checked':colors_checked,'remaining_without_supplied_color':247-colors_checked,'difference_masks_checked':mask_checked,
         'negative_control':control,'limits':'Exact independent factor-triple/mask and supplied-color checks only; absence of colors in the remaining 41 requires separate proof. Entropy lifting is written separately.'}
    with OUT.open('x',encoding='utf-8') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
