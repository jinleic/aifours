#!/usr/bin/env python3
"""Exact divisor/factorial screen for 180 <= effective coset index < 288."""
from math import factorial
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'frontier-20261028-coset-index-screen-result.json'


def screen(limit=288):
    survivors=[];patterns=0;product_bounded=0
    for m in range(180,limit):
        z=m;v2=0
        while z%2==0:v2+=1;z//=2
        divisors=[d for d in range(3,m+1) if m%d==0]
        for binary in range(9):
            if binary and (v2==0 or 2**v2-1<binary):continue
            r=10-binary
            def visit(start,chosen,p,f):
                nonlocal patterns,product_bounded
                if len(chosen)==r:
                    patterns+=1
                    if p*p>=m**3:return
                    product_bounded+=1
                    if f%m==0:survivors.append({'m':m,'binary_count':binary,'nonbinary_indices':list(chosen)})
                    return
                for pos in range(start,len(divisors)):
                    d=divisors[pos];newp=p*d
                    if newp*newp*pow(d,2*(r-len(chosen)-1))>=m**3:break
                    visit(pos,chosen+[d],newp,f*factorial(d))
            visit(0,[],2**binary,2**binary)
    return {'m_range':[180,limit-1],'completed_index_patterns':patterns,
            'strict_product_bound_patterns':product_bounded,'factorial_divisibility_survivors':survivors}


def main():
    out=screen()
    if out['factorial_divisibility_survivors']!=[{'m':192,'binary_count':8,'nonbinary_indices':[3,3]}]:raise ValueError('UNEXPECTED_SURVIVORS')
    out['limits']='Arithmetic necessary-condition screen only; the FD/character reduction for m=192 is separate.'
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
