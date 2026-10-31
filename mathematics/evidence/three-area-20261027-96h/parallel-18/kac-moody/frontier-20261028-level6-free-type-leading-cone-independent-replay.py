#!/usr/bin/env python3
"""Independent entire level-six type leading-cone matrix replay."""
import argparse
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);args=ap.parse_args()
    a,b=args.a,args.b;degree=(a,b,6)
    P=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json').read_text())
    C=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-leading-cone-v1.json').read_text())
    assert C['status']=='LEADING_INJECTIVE_ROW_PRODUCT_CONE'
    out=ROOT/f'frontier-20261028-level6-free-{a}{b}-leading-cone-independent-replay-v1.json'
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
    coeff=P['horizontal_kernel_coefficients'];assert len(coeff)==k
    assert len(ind.ind.ReducedSpace([{int(i):Q(q) for i,q in c.items()} for c in coeff]))==k
    vectors=[ind.combine(basis,c) for c in coeff]
    for v in vectors:
        for g in ('f1','f2'):assert not ind.act(v,g,6,6)
    rows=P['selected_target_words'];assert len(rows)==len(set(rows))==k
    def image(r,s):return [[Q(ind.d3(v,degree,r,s).get(w,0)) for v in vectors] for w in rows]
    A=image(6,6);R=image(7,6);S=image(6,7)
    L=[[R[i][j]+S[i][j]-2*A[i][j] for j in range(k)] for i in range(k)]
    K=[[R[i][j]-S[i][j] for j in range(k)] for i in range(k)]
    E=[[A[i][j]-6*L[i][j] for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):
            assert [A[i][j],R[i][j]-A[i][j],S[i][j]-A[i][j]]==[Q(q) for q in P['matrix'][i][j]]
            assert [L[i][j],K[i][j],E[i][j]]==[Q(q) for q in C['matrix_entries'][i][j]]
    delta=ind.ind.determinant(L);assert delta==Q(C['leading_determinant']) and delta
    Rs=[sum((abs(q) for q in row),Q(0)) for row in L];assert all(Rs)
    H=Q(k)*math.prod(Rs)/(min(Rs)*abs(delta))
    B=max(sum((abs(q) for q in row),Q(0)) for row in K);G=max(sum((abs(q) for q in row),Q(0)) for row in E)
    assert H==Q(C['inverse_bound_H']) and B==Q(C['K_max_row_sum_B']) and G==Q(C['E_max_row_sum_G'])
    result={'degree':degree,'free_source_dimension':len(words),'horizontal_rank':rank,'whole_lowest_dimension':k,
            'all_lowest_vectors_and_L_K_E_entries_independently_checked':True,
            'gaussian_leading_determinant':str(delta),'row_product_inverse_bound':str(H),
            'K_max_row_sum':str(B),'E_max_row_sum':str(G),'status':'PASS_FULL_LEADING_MAP_AND_CONE_BOUND',
            'scope':'one level-six type, r,s>=6; source isomorphism and ideal absence are written inputs',
            'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS level6',degree,'source',len(words),'lowest',k,'all L/K/E entries and cone',out.name,flush=True)

if __name__=='__main__':main()
