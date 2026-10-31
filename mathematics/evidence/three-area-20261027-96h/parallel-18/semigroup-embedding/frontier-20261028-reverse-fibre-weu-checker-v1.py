#!/usr/bin/env python3
"""Exhaustive reverse-fibre/WEU comparison on one 15-element monoid.

No solver or external data. The independently reasoned theorem is separate;
this script reuses the same-owner pinned multiplication for the finite base.
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
    one=(None,1,0)
    require(all((a[2]==0)==(m.am(a,a)==a) for a in A),'base pure group')
    good={p for p in A if all(m.am(m.am(a,p),a)==a for a in A if a[2]==p[2])}
    bad=len(A)**4-len(good)**4
    source=list(product(range(2),A,range(2)))
    good_count=regular_count=nonregular_count=0
    for entries in product(A,repeat=4):
        P=((entries[0],entries[1]),(entries[2],entries[3]))
        def mul(s,t):return (s[0],m.am(m.am(s[1],P[s[2]][t[0]]),t[1]),t[2])
        def idem(s):return mul(s,s)==s
        offending=next(((lam,i) for lam,i in product(range(2),repeat=2) if P[lam][i] not in good),None)
        if offending is not None:
            lam,i=offending;p=P[lam][i]
            a=next(a for a in A if a[2]==p[2] and m.am(m.am(a,p),a)!=a)
            x=(i,a,lam);d=mul(x,x)
            require(mul(d,x)==d==mul(x,d) and idem(d) and d!=x,'expected WEU witness')
            continue
        good_count+=1
        E=[a for a in source if idem(a)]
        for x in source:
            r_idem=x[1][2]==P[x[2]][x[0]][2]
            require(r_idem==idem(x),'actor purity')
            left={mul(e,x) for e in E};right={mul(x,e) for e in E}
            require(not (left&right&set(E)) or idem(x),'WEU violation')
        regular=all(any(mul(mul(x,y),x)==x and mul(mul(y,x),y)==y for y in source) for x in source)
        regular_count+=int(regular);nonregular_count+=int(not regular)
    require(good_count==len(good)**4 and good_count+bad==len(A)**4,'coverage')
    print('base_size=',len(A),' reverse_fibre_good_entries=',len(good),' good_elements=',sorted(good,key=repr),sep='')
    print('sandwich_matrices=',len(A)**4,' WEU=',good_count,' nonWEU=',bad,sep='')
    print('WEU_regular=',regular_count,' WEU_nonregular=',nonregular_count,sep='')
    print('PASS all failing matrices have explicit x^3=x^2!=x with idempotent order witness')
    print('PASS every reverse-fibre-good matrix by all source natural-order tests and pure actor')
    print('LIMIT: one finite base; full theorem is proved separately')


if __name__=='__main__':main()
