#!/usr/bin/env python3
"""Independent entire small-row quotient and alternate-minor replay."""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser()
    for x in ('a','b','r'):ap.add_argument('--'+x,type=int,required=True)
    args=ap.parse_args();a,b,r=args.a,args.b,args.r;degree=(a,b,5)
    P=json.loads((ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-pencil-v1.json').read_text())
    Z=json.loads((ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-alternate-v1.json').read_text())
    assert Z['status']=='ONE_SIGN_ALTERNATE' and Z['first_pivot_mixed_sign_preserved'];A=Z['result']
    out=ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-alternate-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    spaces=ind.ideal_spaces(degree,r,5);ideal=spaces.get(degree,ind.ind.ReducedSpace())
    source=ind.source_basis(degree);target=ind.target_space(spaces,degree)
    assert len(source)==P['free_source_dim'] and len(ideal)==P['source_ideal_dim']
    for v in ideal.pivots.values():assert not source.remainder(v)
    basis=[ind.ind.standard_bracket(w) for w in P['quotient_source_words']]
    combined=ind.ind.ReducedSpace(ideal.pivots.values())
    for v in basis:
        assert not source.remainder(v)
        assert combined.insert(v)
    assert len(combined)==len(source) and len(basis)==P['quotient_source_dim']
    for s in (4,5):
        for v in ideal.pivots.values():assert not target.remainder(ind.delta(v,degree,r,s)),('ideal leakage',s)
    hor=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):
            col.update({prefix+w:q for w,q in ind.act(v,g,r,4).items()})
        hor.append(ind.restrict(target.remainder(col),('1:','2:')))
    rank=len(ind.ind.ReducedSpace(hor));k=P['joint_horizontal_kernel_dim'];assert len(basis)-rank==k
    coeffs=P['horizontal_kernel_coefficients'];assert len(coeffs)==k
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==k
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:assert not ind.restrict(target.remainder(ind.delta(v,degree,r,4)),('1:','2:'))
    rows=A['selected_target_words'];assert len(set(rows))==k
    def image(s):return [[Q(target.remainder(ind.delta(v,degree,r,s)).get('3:'+w,0)) for v in vectors] for w in rows]
    R=image(4);S=image(5)
    for i in range(k):
        for j in range(k):assert [R[i][j],S[i][j]-R[i][j]]==[Q(q) for q in A['matrix'][i][j]]
    poly=[Q(q) for q in A['determinant_coefficients']];sign=A['sign'];assert sign in (-1,1)
    assert sign*poly[0]>0 and all(sign*q>=0 for q in poly)
    for y in range(k+1):
        matrix=[[R[i][j]+y*(S[i][j]-R[i][j]) for j in range(k)] for i in range(k)]
        assert ind.ind.determinant(matrix)==sum(q*y**i for i,q in enumerate(poly)),y
    result={'degree':degree,'r':r,'s_class':'>=4','free_source_dimension':len(source),
            'whole_fixed_row_ideal_source_dimension':len(ideal),'quotient_source_dimension':len(basis),
            'horizontal_rank':rank,'joint_horizontal_kernel_dimension':k,
            'independent_whole_source_ideal_target_reconstruction':True,
            'all_ideal_derivatives_landed_in_full_targets_s4_s5':True,
            'quotient_tree_jacobi_all_pencil_entries':True,'grid_determinants':k+1,
            'coefficient_sign':sign,'nonzero_coefficient_count':sum(bool(q) for q in poly),
            'constant_coefficient':str(poly[0]),'first_pivot_mixed_sign_preserved':True,
            's4_extra_154star_seed_not_built':'selected-type exclusion remains written obligation',
            'status':'PASS_ENTIRE_SMALLROW_ALTERNATE_QUOTIENT_POLYNOMIAL','not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS alternate r',r,degree,'free',len(source),'ideal',len(ideal),'quotient',len(basis),'kernel',k,'grid',k+1,'one-sign terms',sum(bool(q) for q in poly),out.name,flush=True)

if __name__=='__main__':main()
