#!/usr/bin/env python3
"""Independently replay full level-six bivariate minor on unisolvent grid."""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);args=ap.parse_args()
    a,b=args.a,args.b;degree=(a,b,6)
    P=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json').read_text())
    D=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-determinant-v1.json').read_text())
    out=ROOT/f'frontier-20261028-level6-free-{a}{b}-determinant-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    words=P['source_words'];assert tuple(words)==ind.lyndon_words(degree)
    basis=[ind.ind.standard_bracket(w) for w in words]
    for w,v in zip(words,basis):assert v.get(w)==1 and min(v)==w
    hor=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):col.update({prefix+w:q for w,q in ind.act(v,g,6,6).items()})
        hor.append(col)
    rank=len(ind.ind.ReducedSpace(hor));k=P['joint_horizontal_kernel_dim'];assert len(words)-rank==k
    coeffs=P['horizontal_kernel_coefficients'];assert len(coeffs)==k
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==k
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for g in ('f1','f2'):assert not ind.act(v,g,6,6)
    rows=P['selected_target_words'];assert len(rows)==len(set(rows))==k
    def image(r,s):return [[Q(ind.d3(v,degree,r,s).get(w,0)) for v in vectors] for w in rows]
    A=image(6,6);R=image(7,6);S=image(6,7)
    for i in range(k):
        for j in range(k):assert [A[i][j],R[i][j]-A[i][j],S[i][j]-A[i][j]]==[Q(q) for q in P['matrix'][i][j]]
    terms=D['determinant_coefficients'];exponents=set()
    for e in terms:
        x,y=e['x_power'],e['y_power'];assert type(x)==type(y)==int and x>=0 and y>=0 and x+y<=k and (x,y) not in exponents
        exponents.add((x,y));assert Q(e['coefficient'])
    total=0
    for x in range(k+1):
        for y in range(k+1-x):
            matrix=[[A[i][j]+x*(R[i][j]-A[i][j])+y*(S[i][j]-A[i][j]) for j in range(k)] for i in range(k)]
            assert ind.ind.determinant(matrix)==ind.ind.eval_polynomial(terms,x,y),(x,y)
            total+=1
        print('level6 determinant replay row',x,'of',k,flush=True)
    assert total==(k+1)*(k+2)//2
    result={'degree':degree,'free_source_dimension':len(words),'horizontal_rank':rank,'whole_lowest_dimension':k,
            'all_recorded_basis_and_affine_entries_checked':True,'total_degree_bound_verified':k,
            'determinant_grid_points':total,'complete_polynomial_coefficients_checked':len(terms),
            'polynomial_mixed_sign_is_not_quadrant_proof':True,'status':'PASS_FULL_BIVARIATE_MINOR_POLYNOMIAL',
            'scope':'actual source/target only for r,s>=6 at named free-Levi/PBW inputs',
            'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS level6',degree,'source',len(words),'lowest',k,'grid',total,'terms',len(terms),out.name,flush=True)

if __name__=='__main__':main()
