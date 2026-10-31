#!/usr/bin/env python3
"""Independently replay full level-five invariant determinant.

Uses own separate matrix-unit / bracket-tree Jacobi engine and SymPy
polynomial determinant; producer uses tensor-word suffix lowering and
subset-polynomial determinant. No original author detector/guide is read.
The free-Levi identification and ideal-type exclusions remain proof imports.
"""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)
spec2=importlib.util.spec_from_file_location('generic',ROOT/'frontier-review-f18-ph7-independent-check.py')
generic=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(generic)
S=generic.S
D=(5,5,5)


def main():
    inp=ROOT/'frontier-20261028-invariant5-r5-s5-v1.json'
    case=json.loads(inp.read_text(encoding='utf-8'))
    words=case['source_lyndon_words']
    assert len(words)==450 and tuple(words)==ind.lyndon_words(D)
    basis=[ind.ind.standard_bracket(w) for w in words]
    # Lyndon leading-word identity proves all listed words are independent;
    # complete enumeration proves they exhaust the degree by the standard
    # free-Lie Lyndon basis theorem, not by a sampled dimension assumption.
    for word,vector in zip(words,basis):
        assert vector.get(word)==1 and min(vector)==word
    horizontal=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):
            col.update({prefix+w:q for w,q in ind.act(v,g,2,2).items()})
        horizontal.append(col)
    rank=len(ind.ind.ReducedSpace(horizontal));assert rank==444
    coeffs=case['horizontal_kernel_coefficients'];assert len(coeffs)==6
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==6
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for action in ('f1','f2','e1','e2'):
            assert not ind.act(v,action,2,2),(action,v)
    rows=case['target_f3_word_pivots'];assert len(set(rows))==6
    def at(r,s):
        return [[Q(ind.d3(v,D,r,s).get(w,0)) for v in vectors] for w in rows]
    at22=at(2,2);at32=at(3,2);at23=at(2,3)
    x,y=S.symbols('x y')
    q=lambda v:S.Rational(v.numerator,v.denominator)
    mat=S.Matrix([[q(at22[i][j])+x*q(at32[i][j]-at22[i][j])+y*q(at23[i][j]-at22[i][j])
                   for j in range(6)] for i in range(6)])
    det=S.Poly(S.expand(mat.det(method='domain-ge')),x,y)
    original=sum(S.Rational(item['coefficient'])*(x-3)**item['x_power']*(y-3)**item['y_power']
                 for item in case['determinant_coefficients'])
    assert S.expand(det.as_expr()-original)==0
    terms=det.terms();assert len(terms)==28 and all(coef>0 for _,coef in terms)
    assert det.nth(0,0)==S.Rational(151875,2)
    out={'degree':D,'independent_source_count':450,'full_horizontal_rank':rank,
         'horizontal_kernel_dimension':6,'basis_checks':'all six killed by f1,f2,e1,e2',
         'target_words':rows,'determinant_x_r_minus_2_y_s_minus_2':
             [{'x_power':a,'y_power':b,'coefficient':str(coef)} for (a,b),coef in sorted(terms)],
         'nonzero_coefficient_count':28,'strictly_positive_coefficients':True,
         'all_coefficients_equal_shifted_producer':True,
         'scope':'free-Levi model; ideal type exclusions and level-one/free-Levi construction are written inputs',
         'not_external_model_or_formal_proof':True}
    dest=ROOT/'frontier-20261028-invariant5-independent-replay-v1.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS independent 450 Lyndon/free-source columns, rank444, invariant basis6, tree-Jacobi 6x6 determinant 28 positive shifted coefficients;',dest.name,flush=True)

if __name__=='__main__':main()
