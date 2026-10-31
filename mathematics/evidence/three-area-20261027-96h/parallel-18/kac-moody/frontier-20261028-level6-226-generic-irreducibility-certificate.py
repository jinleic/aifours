#!/usr/bin/env python3
"""Exact constant-leading determinant factor and finite-field Rabin certificate.

SymPy constructs the polynomial and modular Bezout data; a separate script
replays all polynomial identities in plain integer arithmetic.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def low(poly):
    return [int(poly.nth(i))%61 for i in range(poly.degree()+1)] if not poly.is_zero else []

def powmod(a, exponent, modulus):
    result=S.Poly(1,*modulus.gens,modulus=61)
    while exponent:
        if exponent & 1:
            result=S.rem(result*a,modulus)
        exponent//=2
        if exponent:
            a=S.rem(a*a,modulus)
    return result


def main():
    raw=(ROOT/'frontier-20261028-level6-226-modular-row-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='738977afb213e2ddec6426c852e27bdab0edbaa8611d127f6048ee84db40a217'
    Qdata=json.loads(raw);x,y=S.symbols('x y')
    Qpoly=S.Poly(sum(S.Integer(t['coefficient'])*x**t['x_power']*y**t['y_power'] for t in Qdata['Q_coefficients']),x,y)
    R,rem=S.div(Qpoly,S.Poly((x+5)**4,x,y));assert rem.is_zero and len(R.terms())==253 and R.total_degree()==21
    Ry=S.Poly(R.as_expr(),y);assert Ry.degree()==21 and Ry.LC()==2107392
    F=S.Poly(R.as_expr().subs(x,0),y,modulus=61).monic();assert F.degree()==21
    yy=S.Poly(y,y,modulus=61); h=yy; powers={}
    for k in range(1,22):
        h=powmod(h,61,F)
        if k in (3,7,21):powers[k]=h
    assert powers[21]==yy
    bez={}
    for k in (3,7):
        a,b,g=S.gcdex(powers[k]-yy,F);assert g==S.Poly(1,y,modulus=61)
        assert a*(powers[k]-yy)+b*F==g
        bez[str(k)]={'h_power':low(powers[k]),'bezout_a':low(a),'bezout_b':low(b)}
    out=ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'source_modular_Q_sha256':digest,'factorization':'Q=(x+5)^4*R',
            'R_total_degree':21,'R_degree_y':21,'R_y_leading_constant':2107392,
            'R_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(c)} for (i,j),c in sorted(R.terms())],
            'prime':61,'specialization_x':0,'monic_f61_coefficients_low_to_high':low(F),
            'frobenius_21_remainder':low(powers[21]),'bezout_certificates':bez,
            'status':'RABIN_IRREDUCIBLE_DEGREE21_SPECIALIZATION',
            'scope':'finite-field irreducibility certificate and exact factor only; generic irreducibility/Hilbert application are written proofs'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact Q=(x+5)^4 R, constant Y-degree21, F61 Rabin powers 3/7/21 and Bezout;',out.name,flush=True)

if __name__=='__main__':main()
