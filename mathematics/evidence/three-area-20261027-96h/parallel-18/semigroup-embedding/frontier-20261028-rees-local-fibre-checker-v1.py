#!/usr/bin/env python3
"""Exact finite check of RF-good Rees sources and inverse-fibre maxima.

Uses the same-owner pinned 15-element base multiplication; exhausts its 16
good-entry matrices, their full local corners and the 3-element inverse
submonoid. It is a finite check, not an independent universal proof.
"""
import importlib.util
from hashlib import sha256
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE=HERE/'frontier-20261028-tight-nonunit-rees-checker-v1.py'
PIN='0398f9ed436b7fdbe2be250d4f6f07db134bded4ec77c6e58ff2945cf3c70bee'
if sha256(BASE.read_bytes()).hexdigest()!=PIN:raise ValueError('base pin')
spec=importlib.util.spec_from_file_location('base',BASE)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def require(ok,why):
    if not ok:raise ValueError(why)


def main():
    R=[None]+list(product(range(2),repeat=2))
    A=[(r,U,h) for r in R for h in range(2) for U in ((0,1) if h==0 else (0,))]
    one=(None,1,0);p=(None,0,1);z=(None,0,0)
    I=[one,p,z]
    require(all(m.am(a,b) in I for a,b in product(I,repeat=2)),'inverse submonoid closure')
    inv={a:[b for b in I if m.am(m.am(a,b),a)==a and m.am(m.am(b,a),b)==b] for a in I}
    require(all(len(v)==1 for v in inv.values()),'inverse uniqueness')
    E=[a for a in I if m.am(a,a)==a]
    def below(a,b):
        return any(m.am(e,b)==a==m.am(b,f) for e,f in product(E,repeat=2))
    good=[];maxima=[]
    for c in I:
        rf=all(m.am(m.am(a,c),a)==a for a in I if a[2]==c[2])
        maximum=all(below(a,c) for a in I if a[2]==c[2])
        require(rf==maximum,('RF/max mismatch',c))
        if rf:good.append(c)
        if maximum:maxima.append(c)
    require(set(good)=={one,p}==set(maxima),'inverse fibre maxima')
    goodP=[one,p];S=list(product(range(2),A,range(2)))
    regular=nonregular=nonorth=noninverse=0
    for entries in product(goodP,repeat=4):
        P=((entries[0],entries[1]),(entries[2],entries[3]))
        def mul(a,b):return (a[0],m.am(m.am(a[1],P[a[2]][b[0]]),b[1]),b[2])
        def idem(a):return mul(a,a)==a
        if not all(any(mul(mul(a,b),a)==a and mul(mul(b,a),b)==b for b in S) for a in S):
            nonregular+=1;continue
        regular+=1
        E=[a for a in S if idem(a)]
        if any(not idem(mul(a,b)) for a,b in product(E,repeat=2)):nonorth+=1
        saw_noninverse=False
        for e in E:
            corner={mul(mul(e,a),e) for a in S}
            ce=[a for a in corner if idem(a)]
            require(all(idem(mul(a,b)) for a,b in product(ce,repeat=2)),'local idempotent closure')
            require(all(mul(mul(mul(mul(a,b),a),c),a)==mul(mul(mul(a,b),c),a)
                        for a,b,c in product(ce,repeat=3)),'local regular-band identity')
            if any(mul(a,b)!=mul(b,a) for a,b in product(ce,repeat=2)):saw_noninverse=True
        noninverse+=int(saw_noninverse)
    require((regular,nonregular)==(7,9),'regularity census')
    print('RF_good_matrices=16 regular=',regular,' nonregular=',nonregular,sep='')
    print('regular_sources_nonorthodox=',nonorth,' nonlocally_inverse=',noninverse,sep='')
    print('PASS all regular source corners orthodox with regular idempotent bands')
    print('inverse_submonoid_size=3 theta_fibre_maxima=',maxima,sep='')
    print('PASS exact RF iff maximum in both group fibres for all inverse-submonoid elements')
    print('LIMIT: finite same-owner base only; arbitrary-source result requires written proof')


if __name__=='__main__':main()
