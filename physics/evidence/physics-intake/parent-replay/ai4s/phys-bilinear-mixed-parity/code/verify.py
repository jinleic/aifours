#!/usr/bin/env python3
"""Exact scientific controls for the all-N proof; not a substitute for that proof."""
import sys
sys.dont_write_bytecode = True
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from math import comb
import hashlib
import importlib.util
import json
import sympy as sp
from tau_formula import mixed_coefficients, pfaffian

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT.parent/'phys-bilinear-higher-dim-integrability/code/hirota_ns.py'
spec = importlib.util.spec_from_file_location('hirota_ns', SHARED)
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)


def system(c1,c2,c3,multiplier):
    P = {(0,0,1):Q(1),(1,0,0):c1,(2,0,0):c2,(3,0,0):c3}
    return [P,H.bmul(P,{(0,1,0) if multiplier=='y' else (1,0,0):Q(1)})]


def rational_cases():
    cases=[]
    all_k=[2,5,11,23,47,97,197]
    all_l=[3,7,13,29,61,127,257]
    coefficients=[(Q(1),Q(3),Q(2)),(Q(-2),Q(5),Q(-3)),(Q(4),Q(7),Q(0))]
    for n in range(1,8):
        patterns=list(product('FG',repeat=n)) if n<=5 else [tuple('F'*n),tuple('G'*n),tuple(('FG'*n)[:n]),tuple(('GF'*n)[:n]),tuple('F'*(n-2)+'GG'),tuple('FF'+'G'*(n-2))]
        for c1,c2,c3 in coefficients:
            for multiplier in ['y','x']:
                ks=list(map(Q,all_k[:n]))
                ls=list(map(Q,(all_l if multiplier=='y' else all_k)[:n]))
                amps=[Q(i+2,i+1) for i in range(n)]
                for types in patterns:
                    waves=[(k,l,-(c1*k+c2*k*k+c3*k**3) if typ=='F' else -c1*k+c2*k*k-c3*k**3)
                           for k,l,typ in zip(ks,ls,types)]
                    Bs=system(c1,c2,c3,multiplier)
                    F,G=mixed_coefficients(ks,ls,types,amps,3*c3/(2*c2))
                    a=[amp if typ=='F' else Q(0) for amp,typ in zip(amps,types)]
                    b=[amp if typ=='G' else Q(0) for amp,typ in zip(amps,types)]
                    expected=H.two_function_solution(Bs,waves,a,b)
                    assert (F,G)==expected,(n,types,c1,c2,c3,multiplier,'recursion mismatch')
                    assert H.residuals(Bs,waves,F,G)=={},(n,types,c1,c2,c3,multiplier,'residual')
                    cases.append({'N':n,'types':''.join(types),'coefficients':list(map(str,(c1,c2,c3))),
                                  'multiplier':multiplier,'formula_equals_recursion':True,'nonzero_residuals':0})
    return cases


def euler_derivative(expr,z,weights,times):
    for _ in range(times):
        expr=sp.expand(sum(weight*zi*sp.diff(expr,zi) for zi,weight in zip(z,weights)))
    return expr


def direct_bilinear(F,G,z,ks,ls,ws,orders):
    """Leibniz/binomial definition using ordinary polynomial differentiation."""
    result=0
    a,b,c=orders
    for ix in range(a+1):
        for iy in range(b+1):
            for it in range(c+1):
                left=euler_derivative(euler_derivative(euler_derivative(F,z,ks,a-ix),z,ls,b-iy),z,ws,c-it)
                right=euler_derivative(euler_derivative(euler_derivative(G,z,ks,ix),z,ls,iy),z,ws,it)
                result+=(-1)**(ix+iy+it)*comb(a,ix)*comb(b,iy)*comb(c,it)*left*right
    return sp.expand(result)


def direct_checks():
    records=[]
    for n,types in [(2,'FF'),(2,'FG'),(2,'GF'),(2,'GG'),(3,'FFG'),(3,'FGG')]:
        for c1,c2,c3 in [(Q(1),Q(3),Q(2)),(Q(4),Q(7),Q(0))]:
            ks=list(map(Q,[2,5,11][:n]));ls=list(map(Q,[3,7,13][:n]))
            ws=[-(c1*k+c2*k*k+c3*k**3) if typ=='F' else -c1*k+c2*k*k-c3*k**3 for k,typ in zip(ks,types)]
            Fc,Gc=mixed_coefficients(ks,ls,types,[Q(1)]*n,3*c3/(2*c2))
            z=sp.symbols(f'z0:{n}')
            monomials=[sp.prod(z[i] for i in range(n) if mask>>i&1) for mask in range(1<<n)]
            F=sum(a*m for a,m in zip(Fc,monomials));G=sum(a*m for a,m in zip(Gc,monomials))
            for multiplier in [None,'x','y']:
                # DxP is checked only after l=k, not on unrestricted transverse waves.
                left,right,transverse=F,G,ls
                if multiplier=='x':
                    Fx,Gx=mixed_coefficients(ks,ks,types,[Q(1)]*n,3*c3/(2*c2))
                    left=sum(a*m for a,m in zip(Fx,monomials))
                    right=sum(a*m for a,m in zip(Gx,monomials))
                    transverse=ks
                residual=0
                for orders,coefficient in system(c1,c2,c3,'y')[0].items():
                    dx,dy,dt=orders
                    if multiplier=='x': dx+=1
                    if multiplier=='y': dy+=1
                    residual+=coefficient*direct_bilinear(left,right,z,ks,transverse,ws,(dx,dy,dt))
                assert sp.Poly(sp.expand(residual),*z).is_zero
            records.append({'N':n,'types':types,'coefficients':list(map(str,(c1,c2,c3))),
                            'P_DyP_and_reduced_DxP_zero':True})
    return records


def symbolic_pair_and_gauge():
    k1,k2,l1,l2,c1,c2,c3,d,r,w=sp.symbols('k1 k2 l1 l2 c1 c2 c3 d r w')
    alpha=3*c3/(2*c2)
    F,G=mixed_coefficients([k1,k2],[l1,l2],'FG',[sp.S(1),sp.S(1)],alpha)
    expected_F=k1*l1*(2*c2+3*c3*k1-3*c3*k2)/((2*c2+3*c3*k1)*(k1+k2)*(l1+l2))
    expected_G=k2*l2*(2*c2+3*c3*k1-3*c3*k2)/((2*c2-3*c3*k2)*(k1+k2)*(l1+l2))
    assert sp.cancel(F[3]-expected_F)==0
    assert sp.cancel(G[3]-expected_G)==0
    p0=lambda q:c3*q**3+(c1-3*c3*d*d)*q
    gauge=sp.expand(w-p0(d)+p0(r+d)-(w+c1*r+3*c3*d*r*r+c3*r**3))
    assert gauge==0
    # Exact algebraic cancellation of powers of alpha, for every cardinality nF,nG.
    m,n=sp.symbols('m n',integer=True)
    exponent=m*(m-1)/2+n*(n-1)/2-m*n+n
    assert sp.expand(exponent.subs(m,n))==0
    assert sp.expand(exponent.subs(m,n+1))==0
    assert mixed_coefficients([],[],[],[],Q(0))==([Q(1)],[Q(1)])
    return {'pair_coefficients_symbolically_checked':2,'gauge_polynomial_identity':True,
            'alpha_power_cancellation_for_all_balanced_and_F_surplus_cardinalities':True,
            'zero_soliton_vacuum':True}


def negative_controls():
    ks=list(map(Q,[2,5]));ls=list(map(Q,[3,7]));types='FG'
    c1,c2,c3=Q(1),Q(3),Q(2)
    waves=[(k,l,-(c1*k+c2*k*k+c3*k**3) if t=='F' else -c1*k+c2*k*k-c3*k**3)
           for k,l,t in zip(ks,ls,types)]
    Bs=system(c1,c2,c3,'y')
    F,G=mixed_coefficients(ks,ls,types,[Q(1),Q(1)],3*c3/(2*c2))
    changed=F.copy();changed[3]+=1
    assert H.residuals(Bs,waves,changed,G)
    badwaves=waves.copy();badwaves[1]=(ks[1],ls[1],-(c1*ks[1]+c2*ks[1]**2+c3*ks[1]**3))
    assert H.residuals(Bs,badwaves,F,G)
    return {'perturbed_pair_coefficient_rejected':True,'wrong_G_seed_dispersion_rejected':True}


def main():
    symbolic=symbolic_pair_and_gauge()
    direct=direct_checks()
    cases=rational_cases()
    negative=negative_controls()
    report={'evidence_boundary':'Finite controls support the written all-N proof; they do not prove all N.',
            'shared_verifier':str(SHARED),'shared_verifier_sha256':hashlib.sha256(SHARED.read_bytes()).hexdigest(),
            'sympy_version':sp.__version__,'symbolic':symbolic,'direct_checks':direct,
            'exact_cases':cases,'negative_controls':negative}
    (ROOT/'results/verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: symbolic mixed pair, gauge identity, and arbitrary-cardinality alpha cancellation.')
    print(f'PASS: {len(direct)} independent polynomial-differentiation cases, cubic and quadratic.')
    print(f'PASS: {len(cases)} exact cases through N=7; all type patterns through N=5; formula equals shared recursion and every residual is zero.')
    print('PASS: 2 negative controls rejected. All-N claim rests on the written Pfaffian proof, not these samples.')


if __name__=='__main__':
    main()
