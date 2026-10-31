#!/usr/bin/env python3
"""Exact AFFINE COEFFICIENT checks for the tensor-source written proof.

Independent formal parameters r,s are checked coefficientwise in the basis
1,r,s. The independent central z3 coefficient is retained separately.
Only Python integers/fractions.Fraction are used: no CAS, FLINT, floating
point or selected numerical parameter. All-height statements remain written
proofs, not extrapolations from this finite alphabet table.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent


def zero(n,m=None):return tuple(tuple(Q(0) for _ in range(n if m is None else m)) for _ in range(n))


def scale(c,a):return tuple(tuple(Q(c)*x for x in row) for row in a)


def add(a,b):
    assert len(a)==len(b) and len(a[0])==len(b[0])
    return tuple(tuple(a[i][j]+b[i][j] for j in range(len(a[0]))) for i in range(len(a)))


def mul(a,b):
    assert len(a[0])==len(b)
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(len(b))),Q(0)) for j in range(len(b[0]))) for i in range(len(a)))


def bracket(a,b):return add(mul(a,b),scale(-1,mul(b,a)))


def mv(a,v):return tuple(sum((a[i][k]*v[k] for k in range(len(v))),Q(0)) for i in range(len(a)))


def unit(i,j):return tuple(tuple(Q(int(a==i-1 and b==j-1)) for b in range(3)) for a in range(3))


def combine(coefficients,matrices):
    answer=zero(len(matrices[0]),len(matrices[0][0]))
    for c,a in zip(coefficients,matrices):answer=add(answer,scale(c,a))
    return answer


def columns(vectors):return tuple(tuple(vectors[j][i] for j in range(len(vectors))) for i in range(len(vectors[0])))


def dump_matrix(a):return [[str(x) for x in row] for row in a]


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',default='frontier-20261029-tensor-source-delta-check-v2.json');args=ap.parse_args()
    output=(ROOT/args.output).resolve();assert output.is_relative_to(ROOT) and not output.exists()
    E1=unit(1,2);E2=unit(2,3);F1=unit(2,1);F2=unit(3,2);E12=unit(1,3)
    H1=add(unit(1,1),scale(-1,unit(2,2)));H2=add(unit(2,2),scale(-1,unit(3,3)))
    B=[unit(3,1),scale(-1,unit(3,2)),unit(2,1),add(H1,H2),H1,scale(-1,E1),scale(-1,E2),scale(-2,E12)]
    weights=[(0,0),(1,0),(0,1),(1,1),(1,1),(2,1),(1,2),(2,2)]

    def coordinates(a):
        assert a[0][0]+a[1][1]+a[2][2]==0
        c=(a[2][0],-a[2][1],a[1][0],-a[2][2],-a[1][1],-a[0][1],-a[1][2],-a[0][2]/2)
        assert combine(c,B)==a
        return c

    identity=tuple(tuple(Q(int(i==j)) for j in range(8)) for i in range(8))
    assert columns([coordinates(b) for b in B])==identity  # explicit rank8 inverse
    action={name:columns([coordinates(bracket(a,b)) for b in B])
        for name,a in [('E1',E1),('E2',E2),('F1',F1),('F2',F2),('H1',H1),('H2',H2)]}
    X=action['E1'];Y=action['E2'];Z=bracket(X,Y);v=tuple(Q(int(i==0)) for i in range(8))
    literal=[v,mv(X,v),mv(Y,v),mv(Z,v),mv(X,mv(Y,v)),mv(Z,mv(X,v)),mv(Z,mv(Y,v)),mv(Z,mv(Z,v))]
    assert columns(literal)==identity
    assert mv(X,mv(X,v))==(Q(0),)*8 and mv(Y,mv(Y,v))==(Q(0),)*8
    assert bracket(X,Z)==zero(8) and bracket(Y,Z)==zero(8)
    for i,j in [(1,2),(2,1)]:assert bracket(action['F'+str(i)],bracket(action['F'+str(i)],action['F'+str(j)]))==zero(8)
    for i in (1,2):
        for j in (1,2):assert bracket(action['E'+str(i)],action['F'+str(j)])==(action['H'+str(i)] if i==j else zero(8))
    for j,(a,b) in enumerate(weights):
        assert action['H1'][j][j]==2*a-b-1 and action['H2'][j][j]==-a+2*b-1

    # h3=-(2r+s)H1/3-(r+2s)H2/3+z3; z3 acts on M by2-r-s.
    Hr=add(scale(Q(-2,3),H1),scale(Q(-1,3),H2))
    Hs=add(scale(Q(-1,3),H1),scale(Q(-2,3),H2))
    h3_checks=[]
    for j,(a,b) in enumerate(weights):
        assert add(bracket(Hr,B[j]),scale(-1,B[j]))==scale(-a,B[j])
        assert add(bracket(Hs,B[j]),scale(-1,B[j]))==scale(-b,B[j])
        h3_checks.append({'index':j,'horizontal_charge':[a,b],'weight_coefficients_1_r_s':['2',str(-a),str(-b)],'all_affine_coefficients_equal':True})

    d0=[zero(3) for _ in range(8)]
    dr=[scale(-1,Hr),scale(-1,E1),zero(3),scale(-1,E12),zero(3),zero(3),zero(3),zero(3)]
    ds=[scale(-1,Hs),zero(3),scale(-1,E2),scale(-1,E12),scale(-1,E12),zero(3),zero(3),zero(3)]
    delta_parts=[d0,dr,ds];central=[Q(-1)]+[Q(0)]*7
    checks=[]
    for name,e in [('E1',E1),('E2',E2)]:
        for j in range(8):
            coefficients=tuple(action[name][k][j] for k in range(8))
            for part in delta_parts:assert bracket(e,part[j])==combine(coefficients,part),(name,j)
            assert sum((coefficients[k]*central[k] for k in range(8)),Q(0))==0
            checks.append({'raising':name,'letter':j,'all1_r_s_and_independent_central_coefficients_equal':True})
    record={'owner':'MathKacMoody-2','kind':'EXACT_FORMAL_AFFINE_COEFFICIENT_FINITE_TABLE_VERIFICATION_ONLY',
        'parameters':'Independent formal r,s;identities checked coefficientwise in1,r,s,not by parameter sampling.',
        'basis_rank':8,'rank_evidence':'Explicit left coordinate inverse sends all8 matrices to the8 unit vectors.',
        'literal_word_order_reconstructed':True,'fixed_positive_Serre_and_finite_A2_checks':True,
        'finite_actions':{name:dump_matrix(matrix) for name,matrix in action.items()},
        'h3_letter_weight_identities':h3_checks,'delta_positive_Levi_equivariance_identities':checks,
        'delta_finite_coefficient_matrices_1_r_s':[[dump_matrix(matrix) for matrix in part] for part in delta_parts],
        'delta_independent_z3_coefficients':[str(x) for x in central],
        'h3_decomposition':{'r_finite_part':dump_matrix(Hr),'s_finite_part':dump_matrix(Hs),'z3_action_on_M_coefficients_1_r_s':['2','-1','-1']},
        'arithmetic':'Python integers/fractions.Fraction only.No Float,CAS,FLINT or selected parameter.Only constant denominator3 from finiteA2;no division by2-r-s or full-Cartan determinant.',
        'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status':'PASS_ALL16_FORMAL_EQUIVARIANCE_AND8_H3_IDENTITIES',
        'limits':'All-word recursion,all-height negative fixed Serres,faithfulness,triangular spanning,whole actual Serre ideal split and tau caller are WRITTEN PROOFS,not bounded extrapolation/formal/kernel verification.No original quotient rank,D3 injectivity,scientific adoption or novelty acceptance.'}
    with output.open('x') as stream:json.dump(record,stream,indent=2);stream.write('\n')
    print('PASS exact formal tensor-source table:8 H3 identities,16 complete delta identities;stdlib fractions only',output.name,flush=True)


if __name__=='__main__':main()
