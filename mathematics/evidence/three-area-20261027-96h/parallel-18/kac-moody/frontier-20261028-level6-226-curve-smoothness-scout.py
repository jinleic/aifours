#!/usr/bin/env python3
"""Bounded exact modular projective smoothness scout for determinant curve.

A failed test or timeout is NOT proof of a singular characteristic-zero
curve. A PASS is an unreviewed conditional algebraic certificate and needs
independent source/smoothness/genus/Faltings review before any application.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--p',type=int,required=True);args=ap.parse_args();p=args.p
    assert p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
    raw=(ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297'
    D=json.loads(raw);x,y=S.symbols('x y')
    f=sum(S.Integer(t['coefficient'])*x**t['x_power']*y**t['y_power'] for t in D['R_coefficients'])
    assert S.Poly(f,x,y).total_degree()==21
    top=sum(S.Integer(t['coefficient'])*x**t['x_power']*y**t['y_power'] for t in D['R_coefficients'] if t['x_power']+t['y_power']==21)
    H=S.Poly(top.subs(y,1),x,modulus=p);lead=int(S.Poly(top.subs({x:1,y:0}),x).as_expr())%p
    gcd=S.gcd(H,H.diff());infinity=H.degree()==21 and lead!=0 and gcd.degree()==0
    print('prime',p,'infinity simple',infinity,'gcd degree',gcd.degree(),flush=True)
    # Geometric affine smoothness iff the Jacobian ideal is the unit ideal.
    basis=S.groebner([f,S.diff(f,x),S.diff(f,y)],x,y,modulus=p,order='grevlex',method='f5b')
    affine=any(g.as_expr()==1 for g in basis.polys)
    out=ROOT/f'frontier-20261028-level6-226-curve-smoothness-p{p}-scout-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'R_certificate_sha256':digest,'prime':p,'degree':21,
            'infinity_leading_coefficient_nonzero':bool(lead),'infinity_degree':H.degree(),
            'infinity_derivative_gcd_degree':gcd.degree(),'infinity_simple':bool(infinity),
            'affine_jacobian_groebner_basis':[str(g.as_expr()) for g in basis.polys],
            'affine_jacobian_unit_ideal':bool(affine),
            'status':'MODULAR_PROJECTIVE_SMOOTH_SCOUT' if infinity and affine else 'NOT_A_SMOOTHNESS_CERTIFICATE_AT_THIS_PRIME',
            'scope':'single exact modular CAS scout; no independent replay, characteristic-zero genus/Faltings or parameter-map conclusion'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE',result['status'],out.name,flush=True)

if __name__=='__main__':main()
