#!/usr/bin/env python3
"""Derive exact globally positive factors and finite-field root-free rows.

Input P is the independently replayed full level-six minor.  Factorization
is exact in Z[x,y]; all x/y residue pairs are exhaustively checked per prime.
No assertion that the finite list covers all integers is made.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))


def main():
    raw=(ROOT/'frontier-20261028-level6-free-22-determinant-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'
    P=json.loads(raw);assert P['degree']==[2,2,6] and P['matrix_size']==34
    x,y=S.symbols('x y')
    poly=S.Poly(sum(S.Rational(a['coefficient'])*x**a['x_power']*y**a['y_power'] for a in P['determinant_coefficients']),x,y)
    f1=S.Poly((y+5)**7,x,y);f2=S.Poly((2*x+2*y+19)**2,x,y)
    q,rem=S.div(poly,f1);assert rem.is_zero
    q,rem=S.div(q,f2);assert rem.is_zero
    terms=q.terms();assert all(c.q==1 and int(c)%393216==0 for _,c in terms)
    Qpoly={(i,j):int(c)//393216 for (i,j),c in terms};assert len(Qpoly)==341 and max(i+j for i,j in Qpoly)==25
    assert math.gcd(*(abs(c) for c in Qpoly.values()))==1
    primes=[13,17,19,23,29,31,37,41,43,47];results=[]
    for p in primes:
        assert prime(p);good=[]
        for a in range(p):
            coeff=[0]*26
            for (i,j),c in Qpoly.items():coeff[j]=(coeff[j]+c*pow(a,i,p))%p
            root=False
            for b in range(p):
                value=0
                for c in reversed(coeff):value=(value*b+c)%p
                if value==0:root=True;break
            if not root:good.append(a)
        assert good
        results.append({'prime':p,'good_x_residues':good,'all_y_residues_checked':p})
    result={'degree':P['degree'],'source_polynomial_sha256':digest,
            'factorization':'P=393216*(y+5)^7*(2*x+2*y+19)^2*Q',
            'Q_total_degree':25,'Q_term_count':len(Qpoly),'Q_content':1,
            'Q_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(c)} for (i,j),c in sorted(Qpoly.items())],
            'root_free_rows':results,'status':'EXACT_FACTORIZATION_AND_ROOT_FREE_RESIDUE_ROWS',
            'scope':'for listed x residues and all integer y, Q is nonzero; physical r,s>=6 makes both stripped factors strictly positive; node exchange gives corresponding columns; not full quadrant or F6'}
    out=ROOT/'frontier-20261028-level6-226-modular-row-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact factorization and exhaustive root-free rows for 10 primes; Q degree25/341 terms;',out.name)

if __name__=='__main__':main()
