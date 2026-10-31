#!/usr/bin/env python3
"""Independent integer-polynomial replay for f46 Walsh congruences.

No author code or author results are read. All 257 coefficients, all 15
symbolic A_t terms and both polynomial substitutions are checked modulo 512.
"""
from hashlib import sha256
from math import comb
from pathlib import Path
import json

OUT=Path(__file__).with_name('frontier-review-f46-walsh-symbolic-check-result.json')
MOD=512


def multiply(a,b):
    result=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]+=x*y
    return result


def linear_power(constant,slope,n):
    return [comb(n,k)*constant**(n-k)*slope**k for k in range(n+1)]


def substitute(poly,constant,slope):
    result=[0]*len(poly)
    for n,c in enumerate(poly):
        for j in range(n+1):result[j]+=c*comb(n,j)*constant**(n-j)*slope**j
    return result


def check():
    factor=[0]*243
    for j in range(122):factor[2*j]=(-1)**j*comb(121,j)
    H=[0]*15
    for j in range(8):H[2*j]=(-1)**j*comb(7,j)
    for j in range(7):H[2*j+1]=256*(-1)**j*comb(6,j)
    product=multiply(factor,H)
    expected=[comb(256,j) for j in range(257)]
    bad=[j for j,(a,b) in enumerate(zip(product,expected)) if (a-b)%MOD]
    if bad:raise ValueError(('GLOBAL_POLYNOMIAL',bad[0]))
    assert len(product)==len(expected)==257
    expected6={1:[256 if t<0 else 0 for t in range(-7,8)],
               -1:[256 if t>0 else 0 for t in range(-7,8)]}
    expected7={1:[128 if t==0 else 256 if t==-4 else 0 for t in range(-7,8)],
               -1:[128 if t==0 else 256 if t==4 else 0 for t in range(-7,8)]}
    rows={}
    for const,slope in ((1,-1),(-1,1)):
        term6=[];term7=[]
        for t in range(-7,8):
            B=multiply(linear_power(1,-1,7+t),linear_power(1,1,7-t))
            transformed=substitute(B,const,slope)
            term6.append(transformed[6]%MOD);term7.append(transformed[7]%MOD)
        background=substitute(H,const,slope)
        if term6!=expected6[const]:raise ValueError(('DEG6_TERMS',const))
        if term7!=expected7[const]:raise ValueError(('DEG7_TERMS',const))
        if background[6]%MOD!=0 or background[7]%MOD!=128:
            raise ValueError(('H_TERMS',const,background[6]%MOD,background[7]%MOD))
        rows[str(const)]={'u6_A_coeffs_mod512':term6,'u7_A_coeffs_mod512':term7,
                          'u6_H_mod512':background[6]%MOD,'u7_H_mod512':background[7]%MOD}
    # Verify binomial v_2 identity in the finite combinatorial lemma.
    for j in range(1,129):
        x=comb(128,j);v=0
        while x%2==0:x//=2;v+=1
        t=j;w=0
        while t%2==0:t//=2;w+=1
        if v!=7-w:raise ValueError(('BINOMIAL_VALUATION',j,v,w))
    # A changed H coefficient must be detected by the global coefficient test.
    mutant=H.copy();mutant[0]+=1;bad_mutant=multiply(factor,mutant)
    first=next((j for j,(a,b) in enumerate(zip(bad_mutant,expected)) if (a-b)%MOD),None)
    if first!=0:raise ValueError(('MUTATION_NOT_DETECTED',first))
    return {'global_identity_coefficients_checked':257,'substitution_A_terms_each':15,
            'all_A_terms_t_from_minus7_to_plus7':list(range(-7,8)),
            'substitution_coefficients':rows,'binomial_2adic_valuations_checked':128,
            'mutation_first_rejected_degree':first,
            'T_zero_energy_upper':36*384+16*(511-384),
            'total_k_squared_energy':16384,
            'even_deviation_energy_lower_after_odd_max':16384-256*49,
            'max_even_nonzero_square':36,
            'limits':'Polynomial arithmetic only; no f, Walsh spectrum, or coding witness generated; written implications require separate logical review.'}


def main():
    out=check()
    with OUT.open('x',encoding='utf-8') as stream:json.dump(out,stream,indent=2);stream.write('\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
