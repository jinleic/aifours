#!/usr/bin/env python3
"""Exact symbolic FINITE table checks for the written tensor-source proof.

This does not compute an original quotient rank or prove the all-word/all-height
operator identities. Those are written induction and finite-Hom arguments in
the companion proof. r,s remain independent formal symbols, never selected
parameter samples. No source/evidence file is edited or deleted.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.dont_write_bytecode=True
import sympy as sp

ROOT=Path(__file__).resolve().parent


def unit(i,j):
    answer=sp.zeros(3);answer[i-1,j-1]=1;return answer


def bracket(a,b):return a*b-b*a


def zero(a):return all(sp.expand(x)==0 for x in a)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='frontier-20261029-tensor-source-delta-check-v1.json');args=ap.parse_args()
    output=(ROOT/args.output).resolve();assert output.is_relative_to(ROOT) and not output.exists()
    r,s=sp.symbols('r s');E1=unit(1,2);E2=unit(2,3);F1=unit(2,1);F2=unit(3,2);Z=unit(1,3)
    H1=unit(1,1)-unit(2,2);H2=unit(2,2)-unit(3,3);H13=H1+H2
    B=[unit(3,1),-unit(3,2),unit(2,1),H13,H1,-E1,-E2,-2*Z]
    weights=[(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)]
    flat=sp.Matrix.hstack(*(sp.Matrix(9,1,list(x)) for x in B));assert flat.rank()==8

    def coordinates(a):
        assert sp.expand(sp.trace(a))==0
        c=sp.Matrix([a[2,0],-a[2,1],a[1,0],-a[2,2],-a[1,1],-a[0,1],-a[1,2],-sp.Rational(1,2)*a[0,2]])
        assert zero(sum((c[i]*B[i] for i in range(8)),sp.zeros(3))-a)
        return c

    action={name:sp.Matrix.hstack(*(coordinates(bracket(a,b)) for b in B))
        for name,a in [('E1',E1),('E2',E2),('F1',F1),('F2',F2),('H1',H1),('H2',H2)]}
    X=action['E1'];Y=action['E2'];ZX=bracket(X,Y);v=sp.eye(8)[:,0]
    literal=[v,X*v,Y*v,ZX*v,X*Y*v,ZX*X*v,ZX*Y*v,ZX*ZX*v]
    assert sp.Matrix.hstack(*literal)==sp.eye(8)
    assert zero(X*X*v) and zero(Y*Y*v)
    assert zero(bracket(X,ZX)) and zero(bracket(Y,ZX))
    assert zero(bracket(action['F1'],bracket(action['F1'],action['F2'])))
    assert zero(bracket(action['F2'],bracket(action['F2'],action['F1'])))
    for i in (1,2):
        for j in (1,2):
            expected=action['H'+str(i)] if i==j else sp.zeros(8)
            assert zero(bracket(action['E'+str(i)],action['F'+str(j)])-expected)

    # In p0=sl3+z_C write h3=a H1+b H2+z3, with z3 commuting
    # with sl3. Its scalar action on M is2-r-s; no division by it.
    a=-(2*r+s)/3;b=-(r+2*s)/3;H3finite=a*H1+b*H2
    assert sp.expand(2*a-b+r)==0 and sp.expand(-a+2*b+s)==0
    h3_checks=[]
    for j,(aa,bb) in enumerate(weights):
        residual=bracket(H3finite,B[j])+(2-r-s)*B[j]-(2-r*aa-s*bb)*B[j]
        assert zero(residual)
        h3_checks.append({'index':j,'horizontal_charge':[aa,bb],'weight':str(2-r*aa-s*bb),'zero_residual':True})

    # delta(v)=-h3. Record the independent central z3 coefficient, not
    # an unannounced identification of h3 with a traceless3x3 matrix.
    delta=[-H3finite,-r*E1,-s*E2,-(r+s)*Z,-s*Z,sp.zeros(3),sp.zeros(3),sp.zeros(3)]
    central=[-1,0,0,0,0,0,0,0]
    checks=[]
    for name,e in [('E1',E1),('E2',E2)]:
        for j in range(8):
            coefficients=action[name][:,j]
            rhs=sum((coefficients[k]*delta[k] for k in range(8)),sp.zeros(3))
            residual=bracket(e,delta[j])-rhs
            central_residual=-sum(coefficients[k]*central[k] for k in range(8))
            assert zero(residual) and sp.expand(central_residual)==0,(name,j)
            checks.append({'raising':name,'letter':j,'entire_finite_and_central_residuals_zero':True})
    all_entries=[entry for matrix in list(action.values())+delta for entry in matrix]
    assert not any(entry.has(sp.Float) for entry in all_entries)
    record={'owner':'MathKacMoody-2','kind':'EXACT_SYMBOLIC_FINITE_LETTER_TABLE_VERIFICATION_ONLY',
        'parameters':'Independent formal r,s; no numerical parameter instance selected.',
        'basis_rank':8,'literal_word_order_reconstructed':True,'fixed_positive_Serre_and_finite_A2_checks':True,
        'finite_actions':{name:[[str(matrix[i,j]) for j in range(8)] for i in range(8)] for name,matrix in action.items()},
        'h3_letter_weight_identities':h3_checks,'delta_positive_Levi_equivariance_identities':checks,
        'delta_finite_parts':[[[str(matrix[i,j]) for j in range(3)] for i in range(3)] for matrix in delta],
        'delta_z3_coefficients':central,'h3_decomposition':{'H1':str(a),'H2':str(b),'z3_action_on_M':'2-r-s'},
        'exact_arithmetic':'SymPy symbolic integers/rationals; no Float nodes. Constant denominator3 is the finiteA2 Cartan inverse,not a parameter or full-Cartan inverse.',
        'sympy_version':sp.__version__,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status':'PASS_ALL16_SYMBOLIC_EQUIVARIANCE_AND8_H3_IDENTITIES',
        'not_machine_verified':'The all-word recursive Chevalley identities,all-height negative fixed Serres,faithfulness,triangular spanning,whole Serre ideal split and original tau callers are WRITTEN PROOFS,not bounded checks or formal/kernel/native-library verification. No quotient rank,D3 injectivity or novelty acceptance.'}
    with output.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('PASS symbolic tensor-source finite table:8 H3 identities,16 full delta identities; no selected parameter',output.name,flush=True)


if __name__=='__main__':main()
