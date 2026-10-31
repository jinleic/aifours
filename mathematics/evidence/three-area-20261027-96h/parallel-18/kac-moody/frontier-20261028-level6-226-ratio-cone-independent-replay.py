#!/usr/bin/env python3
"""Independently reconstruct full target ratio cone, check Sylvester minors.

Uses matrix-unit/tree-Jacobi source/target generation and integer Bareiss
leading-principal determinants, NOT producer's suffix/LDL implementation.
"""
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def load(name,file):
    sp=importlib.util.spec_from_file_location(name,ROOT/file);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
ind=load('independent','frontier-20261028-levi-critical-independent-replay.py')
det=load('det','frontier-20261028-level5-type-determinant.py')


def main():
    degree=(2,2,6)
    P=json.loads((ROOT/'frontier-20261028-level6-free-22-pencil-v1.json').read_text())
    C=json.loads((ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json').read_text())
    assert C['status']=='ALL_THREE_SYMMETRIC_FORMS_STRICTLY_POSITIVE_DEFINITE'
    out=ROOT/'frontier-20261028-level6-226-ratio-cone-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    words=P['source_words'];assert tuple(words)==ind.lyndon_words(degree)
    basis=[ind.ind.standard_bracket(w) for w in words];assert all(v.get(w)==1 and min(v)==w for w,v in zip(words,basis))
    hor=[]
    for v in basis:
        col={}
        for g,prefix in (('f1','1:'),('f2','2:')):col.update({prefix+w:q for w,q in ind.act(v,g,6,6).items()})
        hor.append(col)
    rank=len(ind.ind.ReducedSpace(hor));n=P['joint_horizontal_kernel_dim'];assert len(words)-rank==n==34
    coeffs=P['horizontal_kernel_coefficients'];assert len(ind.ind.ReducedSpace([{int(i):Q(q) for i,q in c.items()} for c in coeffs]))==n
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for g in ('f1','f2'):assert not ind.act(v,g,6,6)
    def image(r,s):return [ind.d3(v,degree,r,s) for v in vectors]
    aa=image(6,6);xx=image(7,6);yy=image(6,7)
    def diff(a,b):
        z=dict(a)
        for w,q in b.items():z[w]=z.get(w,Q(0))-q
        return {w:q for w,q in z.items() if q}
    bb=[diff(xx[i],aa[i]) for i in range(n)];cc=[diff(yy[i],aa[i]) for i in range(n)]
    target=sorted(set(w for z in aa+bb+cc for w in z));assert target==C['target_word_rows'] and len(target)==235
    data=[[[Q(aa[j].get(w,0)),Q(bb[j].get(w,0)),Q(cc[j].get(w,0))] for j in range(n)] for w in target]
    assert data==[[[Q(q) for q in e] for e in row] for row in C['full_target_affine_entries']]
    def dot(i,si,j,sj):return sum((row[i][si]*row[j][sj] for row in data),Q(0))
    L=[[row[i][1]+row[i][2] for i in range(n)] for row in data]
    K=[[row[i][1]-row[i][2] for i in range(n)] for row in data]
    H0=[[sum((L[h][i]*data[h][j][0]+data[h][i][0]*L[h][j] for h in range(len(data))),Q(0)) for j in range(n)] for i in range(n)]
    HL=[[2*sum((row[i]*row[j] for row in L),Q(0)) for j in range(n)] for i in range(n)]
    HK=[[sum((L[h][i]*K[h][j]+K[h][i]*L[h][j] for h in range(len(data))),Q(0)) for j in range(n)] for i in range(n)]
    lam=Q(9,2);forms={'H0':H0,
      'lambda_HL_plus_HK':[[lam*HL[i][j]+HK[i][j] for j in range(n)] for i in range(n)],
      'lambda_HL_minus_HK':[[lam*HL[i][j]-HK[i][j] for j in range(n)] for i in range(n)]}
    results={}
    for name,M in forms.items():
        assert M==[[Q(q) for q in row] for row in C['symmetric_forms'][name]]
        leading=[]
        for size in range(1,n+1):
            sub=[row[:size] for row in M[:size]]
            scales=[math.lcm(*(q.denominator for q in row)) for row in sub]
            integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(sub)]
            value=Q(det.bareiss(integer),math.prod(scales));assert value>0
            leading.append(str(value))
        results[name]={'positive_leading_principal_minors':leading,'count':len(leading)}
    result={'degree':degree,'source_dimension':len(words),'horizontal_rank':rank,'lowest_dimension':n,
            'full_target_word_count':len(target),'all_tree_Jacobi_target_entries_match':True,
            'all_3_symmetric_matrices_match':True,'sylvester_certificates':results,
            'status':'PASS_FULL_TARGET_AND_102_POSITIVE_SYLVESTER_MINORS',
            'scope':'exact current free-Levi source; full Cartan and seed-ideal absence are named written inputs',
            'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS level6',degree,'74 source/34 lowest/235 target rows; all entries and 102 positive Sylvester minors;',out.name,flush=True)

if __name__=='__main__':main()
