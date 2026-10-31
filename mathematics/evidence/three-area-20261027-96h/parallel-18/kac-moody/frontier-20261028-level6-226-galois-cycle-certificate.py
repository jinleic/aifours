#!/usr/bin/env python3
"""Exact finite-field irreducible factor certificates for (2,19)/(1,20).

The 21-cycle at p61 is certified separately.  Cycle-to-Galois and group
arguments are written imports, not a program-generated theorem.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def low(f,p):return [int(f.nth(i))%p for i in range(f.degree()+1)] if not f.is_zero else []


def powmod(a,e,f,p):
    result=S.Poly(1,*f.gens,modulus=p)
    while e:
        if e&1:result=S.rem(result*a,f)
        e//=2
        if e:a=S.rem(a*a,f)
    return result


def main():
    raw=(ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297'
    P=json.loads(raw);y=S.symbols('y');r0=sum(S.Integer(t['coefficient'])*y**t['y_power'] for t in P['R_coefficients'] if t['x_power']==0)
    outcomes=[]
    for p,expected in ((59,[2,19]),(467,[1,20])):
        assert all(p%d for d in range(2,math.isqrt(p)+1)) and 2107392%p
        f=S.Poly(r0,y,modulus=p).monic();assert f.degree()==21
        factors=S.factor_list(f)[1];assert sorted(g.degree() for g,e in factors for _ in range(e))==expected and all(e==1 for g,e in factors)
        factors=sorted([g.monic() for g,e in factors],key=lambda v:v.degree());prod=S.Poly(1,y,modulus=p)
        for g in factors:prod*=g
        assert prod==f
        pair_a,pair_b,pair_g=S.gcdex(factors[0],factors[1]);assert pair_g==S.Poly(1,y,modulus=p)
        checks=[]
        for g in factors:
            n=g.degree();checks0={};yy=S.Poly(y,y,modulus=p);h=yy;powers={}
            divisors=list(S.factorint(n)) if n>1 else []
            wanted={n//ell for ell in divisors}|{n}
            for k in range(1,n+1):
                h=powmod(h,p,g,p)
                if k in wanted:powers[k]=h
            assert powers[n]==S.rem(yy,g)
            for ell in divisors:
                k=n//ell;a,b,z=S.gcdex(powers[k]-yy,g);assert z==S.Poly(1,y,modulus=p)
                assert a*(powers[k]-yy)+b*g==z
                checks0[str(k)]={'h_power':low(powers[k],p),'bezout_a':low(a,p),'bezout_b':low(b,p)}
            checks.append({'degree':n,'factor_low_to_high':low(g,p),
                           'frobenius_n_remainder':low(powers[n],p),'proper_prime_divisor_checks':checks0})
        outcomes.append({'prime':p,'pattern':expected,'monic_full_polynomial':low(f,p),'factors':checks,
                         'pairwise_bezout_a':low(pair_a,p),'pairwise_bezout_b':low(pair_b,p)})
    out=ROOT/'frontier-20261028-level6-226-galois-cycle-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'generic_irreducibility_certificate_sha256':digest,'specialization_x':0,
                               'cycles':outcomes,'status':'EXACT_FINITE_FIELD_CYCLE_DATA',
                               'scope':'finite field factors only; Frobenius specialization and Galois-group deduction are named written inputs'},indent=2)+'\n')
    print('PASS p59 irreducible factor degrees2+19 and p467 degrees1+20, all Rabin/Bezout/product identities;',out.name)

if __name__=='__main__':main()
