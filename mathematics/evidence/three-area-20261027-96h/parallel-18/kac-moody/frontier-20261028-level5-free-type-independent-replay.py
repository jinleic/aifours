#!/usr/bin/env python3
"""Independent whole level-five free-type determinant replay.

Build source brackets and Levi actions from the separate matrix-unit engine,
apply node-3 lowering by bracket-tree Jacobi, and use rational Gaussian
elimination rather than the producer's integer Bareiss/Newton routines.
The entire triangular interpolation grid is checked with the universal total
polynomial degree bound. Actual quotient descent is a written obligation.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True)
    args=ap.parse_args();a,b=args.a,args.b
    pp=ROOT/f'frontier-20261028-level5-free-{a}{b}-pencil-v1.json'
    dp=ROOT/f'frontier-20261028-level5-free-{a}{b}-determinant-v1.json'
    op=ROOT/f'frontier-20261028-level5-free-{a}{b}-independent-replay-v1.json'
    if op.exists():raise FileExistsError(op)
    P=json.loads(pp.read_text(encoding='utf-8'));D=json.loads(dp.read_text(encoding='utf-8'))
    degree=tuple(P['degree']);words=P['source_words'];assert tuple(words)==ind.lyndon_words(degree)
    basis=[ind.ind.standard_bracket(w) for w in words]
    for w,v in zip(words,basis):assert v.get(w)==1 and min(v)==w
    hor=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):
            col.update({prefix+w:q for w,q in ind.act(v,g,4,4).items()})
        hor.append(col)
    rank=len(ind.ind.ReducedSpace(hor));k=P['joint_horizontal_kernel_dim']
    assert len(words)-rank==k
    coeffs=P['horizontal_kernel_coefficients'];assert len(coeffs)==k
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==k
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for action in ('f1','f2'):assert not ind.act(v,action,4,4)
    rows=P['selected_target_words'];assert len(set(rows))==k
    def image(r,s):
        return [[Q(ind.d3(v,degree,r,s).get(w,0)) for v in vectors] for w in rows]
    A=image(4,4);R=image(5,4);S=image(4,5)
    for i in range(k):
        for j in range(k):
            assert [A[i][j],R[i][j]-A[i][j],S[i][j]-A[i][j]]==[Q(v) for v in P['matrix'][i][j]]
    terms=D['determinant_coefficients'];assert all(Q(t['coefficient'])>0 for t in terms)
    assert all(t['x_power']+t['y_power']<=k for t in terms)
    assert next(Q(t['coefficient']) for t in terms if t['x_power']==t['y_power']==0)>0
    total=0
    for x in range(k+1):
        for y in range(k+1-x):
            matrix=[[A[i][j]+x*(R[i][j]-A[i][j])+y*(S[i][j]-A[i][j])
                     for j in range(k)] for i in range(k)]
            actual=ind.ind.determinant(matrix)
            claimed=ind.ind.eval_polynomial(terms,x,y)
            assert actual==claimed,(x,y,actual,claimed)
            total+=1
        print('independent row',x,'of',k,flush=True)
    assert total==(k+1)*(k+2)//2
    result={'degree':degree,'free_source_basis_dimension':len(words),'horizontal_rank':rank,
            'joint_horizontal_kernel_dimension':k,'all_source_basis_and_kernel_vectors_checked':True,
            'tree_jacobi_pencil_entry_check':'all 3 coefficients of all entries',
            'determinant_method':'rational Gaussian elimination; complete triangular unisolvent grid',
            'degree_bound':k,'grid_evaluations':total,'coefficient_count':len(terms),
            'all_coefficients_strictly_positive':True,'status':'PASS_FULL_FREE_TYPE_POLYNOMIAL',
            'scope':'free-model source and target; actual ideal descent is a separate written proof',
            'not_formal_or_external_model_review':True}
    op.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS',degree,'source',len(words),'kernel',k,'grid',total,'positive terms',len(terms),op.name,flush=True)

if __name__=='__main__':main()
