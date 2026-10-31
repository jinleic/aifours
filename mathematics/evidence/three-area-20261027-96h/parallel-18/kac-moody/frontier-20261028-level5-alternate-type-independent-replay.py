#!/usr/bin/env python3
"""Independent full-source alternative-minor replay for any level-five type."""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);ap.add_argument('--label',required=True)
    args=ap.parse_args();a,b,label=args.a,args.b,args.label
    source=json.loads((ROOT/f'frontier-20261028-level5-free-{a}{b}-pencil-v1.json').read_text())
    search=json.loads((ROOT/f'frontier-20261028-level5-{label}-alternate-minor-search-v1.json').read_text())
    assert search['status']=='ONE_SIGN_ALTERNATE' and search['first_pivot_mixed_sign_preserved']
    alt=search['result'];degree=tuple(source['degree']);words=source['source_words']
    assert tuple(words)==ind.lyndon_words(degree)
    basis=[ind.ind.standard_bracket(w) for w in words]
    for w,v in zip(words,basis):assert v.get(w)==1 and min(v)==w
    hor=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):
            col.update({prefix+w:q for w,q in ind.act(v,g,4,4).items()})
        hor.append(col)
    rank=len(ind.ind.ReducedSpace(hor));k=source['joint_horizontal_kernel_dim'];assert len(words)-rank==k
    coeffs=source['horizontal_kernel_coefficients'];assert len(coeffs)==k
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==k
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for action in ('f1','f2'):assert not ind.act(v,action,4,4)
    rows=alt['selected_target_words'];assert len(set(rows))==k
    def image(r,s):return [[Q(ind.d3(v,degree,r,s).get(w,0)) for v in vectors] for w in rows]
    A=image(4,4);R=image(5,4);S=image(4,5)
    for i in range(k):
        for j in range(k):
            assert [A[i][j],R[i][j]-A[i][j],S[i][j]-A[i][j]]==[Q(q) for q in alt['matrix'][i][j]]
    terms=alt['determinant_coefficients'];sign=alt['sign'];assert sign in (-1,1)
    assert all(sign*Q(t['coefficient'])>0 for t in terms)
    assert all(t['x_power']+t['y_power']<=k for t in terms)
    assert sign*next(Q(t['coefficient']) for t in terms if t['x_power']==t['y_power']==0)>0
    total=0
    for x in range(k+1):
        for y in range(k+1-x):
            mat=[[A[i][j]+x*(R[i][j]-A[i][j])+y*(S[i][j]-A[i][j]) for j in range(k)] for i in range(k)]
            assert ind.ind.determinant(mat)==ind.ind.eval_polynomial(terms,x,y),(x,y)
            total+=1
        print('independent row',x,'of',k,flush=True)
    assert total==(k+1)*(k+2)//2
    result={'degree':degree,'free_source_basis_dimension':len(words),'horizontal_rank':rank,
            'joint_horizontal_kernel_dimension':k,'all_source_basis_and_kernel_vectors_checked':True,
            'replaced_position_zero_based':alt['replaced_position_zero_based'],
            'old_target_word':alt['previous_target_word'],'new_target_word':alt['new_target_word'],
            'tree_jacobi_pencil_entry_check':'all three coefficients of all entries',
            'determinant_method':'rational Gaussian elimination; complete triangular unisolvent grid',
            'degree_bound':k,'grid_evaluations':total,'coefficient_count':len(terms),
            'coefficient_sign':sign,'constant_coefficient':alt['constant_coefficient'],
            'all_nonzero_coefficients_strictly_one_sign':True,
            'first_pivot_mixed_sign_preserved':True,'status':'PASS_FULL_FREE_TYPE_ALTERNATE_POLYNOMIAL',
            'scope':'free-model source and target; actual ideal descent is a separate written proof',
            'not_formal_or_external_model_review':True}
    dest=ROOT/f'frontier-20261028-level5-{label}-alternate-independent-replay-v1.json'
    if dest.exists():raise FileExistsError(dest)
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS',degree,'source',len(words),'kernel',k,'grid',total,'one-sign terms',len(terms),dest.name,flush=True)

if __name__=='__main__':main()
