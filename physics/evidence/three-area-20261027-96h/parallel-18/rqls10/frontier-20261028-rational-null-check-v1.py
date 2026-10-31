#!/usr/bin/env python3
"""Reconstruct modular null vectors and verify ALL rows over exact rationals.

Input modular basis uses prime-residue sparse vectors; no claim is made if
rational reconstruction fails or any integer-matrix residual is nonzero.
"""
import argparse
from fractions import Fraction
import json
from math import gcd,isqrt
from pathlib import Path


def reconstruct(residue,p):
    residue%=p
    if residue==0: return Fraction(0)
    bound=isqrt(p//2)
    a0,a1=p,residue
    b0,b1=0,1
    while abs(a1)>bound:
        q=a0//a1
        a0,a1=a1,a0-q*a1
        b0,b1=b1,b0-q*b1
    if b1==0 or abs(b1)>bound or gcd(a1,b1)!=1:
        raise ValueError(f'cannot rationally reconstruct {residue}')
    value=Fraction(a1,b1)
    if (value.numerator-residue*value.denominator)%p:
        raise ValueError('failed reconstruction congruence')
    return value


def main():
    p=argparse.ArgumentParser()
    p.add_argument('matrix')
    p.add_argument('basis')
    p.add_argument('output')
    args=p.parse_args()
    lines=Path(args.matrix).read_text().splitlines()
    nrows,ncols=map(int,lines[0].split())
    rows=[]
    for line in lines[1:]:
        parts=list(map(int,line.split()))
        assert len(parts)==1+2*parts[0]
        rows.append(list(zip(parts[1::2],parts[2::2])))
    assert len(rows)==nrows
    baselines=Path(args.basis).read_text().splitlines()
    header=baselines[0].split()
    assert header[0]=='prime' and header[2]=='columns' and int(header[3])==ncols
    prime=int(header[1]); nullity=int(header[7]); assert len(baselines)==nullity+1
    result=[]
    for line in baselines[1:]:
        parts=line.split()
        assert parts[0]=='free' and parts[2]=='nonzeros'
        free=int(parts[1]); assert int(parts[3])==len(parts)-4
        values=[Fraction(0) for _ in range(ncols)]
        for entry in parts[4:]:
            index,residue=map(int,entry.split(':'))
            values[index]=reconstruct(residue,prime)
        bad=[]
        for i,row in enumerate(rows):
            residual=sum(coeff*values[index] for index,coeff in row)
            if residual: bad.append((i,str(residual)))
        print('free',free,'reconstructed_nonzeros',sum(bool(v) for v in values),
              'nonzero_exact_row_residuals',len(bad))
        if bad:
            print('first_nonzero_residual',bad[0])
            raise ValueError('modular basis did not reconstruct a rational kernel vector')
        result.append({'free_column':free,'entries':[[i,v.numerator,v.denominator]
                      for i,v in enumerate(values) if v]})
    out={'matrix':args.matrix,'basis':args.basis,'prime':prime,'rows_checked':nrows,
         'columns':ncols,'vectors':result,
         'claim':'each listed vector satisfies every integer row exactly over Q'}
    Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print('PASS exact rational residuals for all',len(result),'vectors; wrote',args.output)


if __name__=='__main__':
    main()
