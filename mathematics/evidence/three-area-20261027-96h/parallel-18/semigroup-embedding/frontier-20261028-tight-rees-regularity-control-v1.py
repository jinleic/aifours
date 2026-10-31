#!/usr/bin/env python3
"""Exact controls: tight nonunit sandwiches do not imply Rees regularity.

Reuses the separately pinned reviewer-owned finite base multiplication;
all source inverses are tested directly, without a solver or external data.
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


def main():
    R=[None]+list(product(range(2),repeat=2))
    A=[(r,mask,h) for r in R for h in range(2) for mask in ((0,1) if h==0 else (0,))]
    one=(None,1,0);p=(None,0,1);e=(None,1)
    if (p[0],p[1])!=m.bm(e,m.alpha(e,p[2])):raise ValueError('not tight')
    S=list(product(range(2),A,range(2)))
    def mul(x,y):return (x[0],m.am(m.am(x[1],p),y[1]),y[2])
    x=(0,one,0)
    inverses=[y for y in S if mul(mul(x,y),x)==x and mul(mul(y,x),y)==y]
    if inverses:raise ValueError('expected nonregular element')
    print('tight_nonunit_sandwich=',p,' source_size=',len(S),sep='')
    print('nonregular_element=',x,' actual_inverse_count=',len(inverses),sep='')
    print('PASS tightness alone does NOT imply full Rees-source regularity')
    print('LIMIT: one exact finite negative control, not a general classification')


if __name__=='__main__':main()
