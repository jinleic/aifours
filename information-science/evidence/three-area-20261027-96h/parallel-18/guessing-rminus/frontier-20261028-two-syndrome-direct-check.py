#!/usr/bin/env python3
"""Direct bit-assignment replay of all <=6-factor two-coset support masks."""
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import numpy as np

ROOT=Path(__file__).resolve().parent
SOURCE=('frontier-20261028-two-syndrome-mobius-census-result.json','a1be7e3a7dc9b491cbe3395d2c9342c7fd419b086ea3144ec4971c79df31e957')
OUT=ROOT/'frontier-20261028-two-syndrome-direct-check-result.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),
   5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),
   9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))


def direct(J):
    fs=[t for t in range(10) if J>>t&1];k=len(fs);codes=np.arange(1<<(3*k),dtype=np.uint32)
    vm=np.zeros(len(codes),dtype=np.uint16);sy=np.zeros(len(codes),dtype=np.uint8)
    for j,t in enumerate(fs):
        T=TRI[t];a=(codes>>(3*j))&1;b=(codes>>(3*j+1))&1;c=(codes>>(3*j+2))&1
        for v,x in zip(T,(a,b,c)):vm|=x.astype(np.uint16)<<(v-1)
        sy|=((a^b^c).astype(np.uint8)<<j)
    nb=[sum(1<<(u-1) for u in N[v]) for v in range(1,11)]
    allowed=np.array([M!=0 and all(M&nb[v] for v in range(10) if M>>v&1) for M in range(1024)],dtype=bool)
    keep=((sy==0)|(sy==(1<<k)-1))&allowed[vm]
    return sorted(int(x) for x in np.unique(vm[keep])),len(codes)


def check_color(masks,color):
    if len(color)!=10 or any(x not in (0,1,2) for x in color):raise ValueError('COLORS')
    cls=[sum(1<<i for i,x in enumerate(color) if x==k) for k in range(3)]
    if any(any(D&~C==0 for C in cls) for D in masks):raise ValueError('COLOR')


def no_color(masks,color_masks):
    mins=[]
    for D in sorted(masks,key=lambda x:(x.bit_count(),x)):
        if not any(M&D==M for M in mins):mins.append(D)
    possible=np.ones(color_masks.shape[1],dtype=bool)
    for D in mins:
        possible &=np.all((color_masks&D)!=D,axis=0)
        if not np.any(possible):return True
    return not np.any(possible)


def main():
    raw=(ROOT/SOURCE[0]).read_bytes()
    if sha256(raw).hexdigest()!=SOURCE[1]:raise ValueError('HASH')
    src=json.loads(raw);records=src['cases'];table={r['factor_mask']:r for r in records}
    covers={J for J in range(1,1024) if J.bit_count()<=6 and set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))==set(N)}
    if len(table)!=254 or set(table)!=covers:raise ValueError('COVERAGE')
    colors=np.array([(0,)+c for c in product(range(3),repeat=9)],np.uint8);cm=np.zeros((3,len(colors)),np.uint16)
    for v in range(10):
        for c in range(3):cm[c]|=(colors[:,v]==c).astype(np.uint16)<<v
    assignments=0;counts={};firstcolored=None
    for J,r in sorted(table.items()):
        masks,n=direct(J);assignments+=n
        if masks!=r['allowed_difference_masks']:raise ValueError(('MASK_MISMATCH',J))
        k=str(J.bit_count());counts.setdefault(k,{'covers':0,'colorable':0,'no_universal_color':0});counts[k]['covers']+=1
        if r['color'] is None:
            if not no_color(masks,cm):raise ValueError(('MISSED_COLOR',J))
            counts[k]['no_universal_color']+=1
        else:
            check_color(masks,r['color']);counts[k]['colorable']+=1
            if firstcolored is None:firstcolored=(masks,r['color'])
    if counts!=src['cover_counts']:raise ValueError(('COUNTS',counts))
    controls={};masks,color=firstcolored
    try:check_color(masks,[0]*10)
    except ValueError as exc:
        if str(exc)!='COLOR':raise ValueError(('WRONG_REASON',str(exc)))
        controls['monochrome']='COLOR'
    else:raise ValueError('CONTROL_ACCEPTED')
    out={'source_receipt_sha256':SOURCE[1],'cases_checked':len(table),'raw_factor_bit_assignments_checked':assignments,
         'cover_counts':counts,'all_checked':True,'mutation_controls':controls,
         'limits':'Direct finite support-mask/color replay only; conditional graph entropy implications remain written mathematics.'}
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
