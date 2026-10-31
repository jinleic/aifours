#!/usr/bin/env python3
"""Independently rebuild the level-six leading map and cofactor cone.

Uses Witt/Weyl character arithmetic for full horizontal-kernel multiplicity,
independent sl3 matrices and tree-Jacobi for every recorded source/pencil
entry, and rational Gaussian determinant. No old cone guide is read.
"""
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)
D=(4,4,6)


def char_word(power,scale):
    v=Counter({(0,0):1})
    for _ in range(power):
        q=Counter()
        for (a,b),n in v.items():
            for x,y in ind.WEIGHTS:q[a+scale*x,b+scale*y]+=n
        v=q
    return v


def main():
    source=ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json'
    out=ROOT/'frontier-20261028-level6-446-leading-map-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    P=json.loads(source.read_text())
    assert P['status']=='LEADING_INJECTIVE_COFAC_CONE'
    terms=[char_word(6,1),char_word(3,2),char_word(2,3),char_word(1,6)]
    weights=set().union(*map(set,terms));character={}
    for w in weights:
        n=terms[0][w]-terms[1][w]-terms[2][w]+terms[3][w];assert n%6==0;character[w]=n//6
    def wt(a,b):return character.get((a,b),0)
    mult=wt(4,4)-wt(3,4)-wt(4,3)+wt(2,3)+wt(3,2)-wt(2,2)
    assert wt(4,4)==P['free_source_dim'] and mult==P['horizontal_kernel_dim']
    words=P['source_words'];assert tuple(words)==ind.lyndon_words(D)
    basis=[ind.ind.standard_bracket(w) for w in words]
    for w,v in zip(words,basis):assert v.get(w)==1 and min(v)==w
    coeffs=P['horizontal_kernel_coefficients'];k=len(coeffs);assert k==mult
    assert len(ind.ind.ReducedSpace([{int(j):Q(q) for j,q in c.items()} for c in coeffs]))==k
    vectors=[ind.combine(basis,c) for c in coeffs]
    for v in vectors:
        for g in ('f1','f2'):assert not ind.act(v,g,0,0)
    rows=P['target_word_pivots'];assert len(rows)==len(set(rows))==k
    def image(r,s):return [[Q(ind.d3(v,D,r,s).get(w,0)) for v in vectors] for w in rows]
    E=image(0,0);both=image(1,1);first=image(1,0);second=image(0,1)
    L=[[both[i][j]-E[i][j] for j in range(k)] for i in range(k)]
    K=[[first[i][j]-second[i][j] for j in range(k)] for i in range(k)]
    for i in range(k):
        for j in range(k):assert [L[i][j],K[i][j],E[i][j]]==[Q(q) for q in P['matrix_entries'][i][j]]
    determinant=ind.ind.determinant(L);assert determinant==Q(P['leading_determinant']) and determinant
    M=max(abs(q) for row in L for q in row);Km=max(abs(q) for row in K for q in row);Em=max(abs(q) for row in E for q in row)
    C=Q(k*k*math.factorial(k-1))*M**(k-1)/abs(determinant)
    assert (M,Km,Em,C)==tuple(Q(P[k]) for k in ('leading_entry_abs_max','difference_entry_abs_max','constant_entry_abs_max','cofactor_bound_C'))
    result={'degree':D,'free_source_dim':wt(4,4),'weyl_lowest_multiplicity':mult,
            'all_recorded_vectors_independent_and_horizontally_lowest':True,
            'tree_Jacobi_all_L_K_E_entries_equal':True,'independent_rational_gaussian_leading_determinant':str(determinant),
            'all_cofactor_bound_constants_equal':True,'status':'PASS_FULL_LEADING_MAP_AND_CONE_BOUND',
            'scope':'formal free-Levi level6; source ideal absence and analytic inequality are written proof inputs',
            'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS level6',D,'source',wt(4,4),'lowest',mult,'all matrix entries/cofactor bound',out.name,flush=True)

if __name__=='__main__':main()
