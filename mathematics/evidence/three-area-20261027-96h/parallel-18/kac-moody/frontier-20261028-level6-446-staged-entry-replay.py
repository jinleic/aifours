#!/usr/bin/env python3
"""Independent ALL 162x162 level-six f3 entry replay, columnwise.

Tree-Jacobi is computed once per distinct Lyndon basis word and formal
coefficient point, then linearly assembled via the literal sparse kernel
coefficient matrix. This avoids re-decomposing each of 162 huge tensor
vectors. Source lowestness and determinant are separately verified stages.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('independent',ROOT/'frontier-20261028-levi-critical-independent-replay.py')
ind=importlib.util.module_from_spec(spec);spec.loader.exec_module(ind)


def main():
    out=ROOT/'frontier-20261028-level6-446-staged-entry-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    raw=(ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);assert P['status']=='LEADING_INJECTIVE_COFAC_CONE'
    words=P['source_words'];rows=P['target_word_pivots'];k=len(rows)
    assert len(words)==1116 and k==len(set(rows))==len(P['horizontal_kernel_coefficients'])==162
    assert tuple(words)==ind.lyndon_words((4,4,6))
    rowindex={w:i for i,w in enumerate(rows)}
    incidence=[[] for _ in words]
    for j,c in enumerate(P['horizontal_kernel_coefficients']):
        for i,q in c.items():incidence[int(i)].append((j,Q(q)))
    E=[[Q(0) for _ in range(k)] for _ in range(k)]
    L=[[Q(0) for _ in range(k)] for _ in range(k)]
    K=[[Q(0) for _ in range(k)] for _ in range(k)]
    for idx,word in enumerate(words):
        if not incidence[idx]:continue
        e=ind.tree_d3(word,0,0);rx=ind.tree_d3(word,1,0);sy=ind.tree_d3(word,0,1)
        keys=(set(e)|set(rx)|set(sy))&rowindex.keys()
        for target in keys:
            i=rowindex[target];a=Q(e.get(target,0));b=Q(rx.get(target,0));c=Q(sy.get(target,0))
            lv=b+c-2*a;kv=b-c
            for j,scale in incidence[idx]:
                E[i][j]+=scale*a;L[i][j]+=scale*lv;K[i][j]+=scale*kv
    for i in range(k):
        for j in range(k):assert [L[i][j],K[i][j],E[i][j]]==[Q(q) for q in P['matrix_entries'][i][j]],('entry mismatch',i,j)
    rowbound=json.loads((ROOT/'frontier-20261028-level6-446-row-product-bound-v1.json').read_bytes())
    RL=[sum((abs(q) for q in row),Q(0)) for row in L]
    B=max(sum((abs(q) for q in row),Q(0)) for row in K)
    G=max(sum((abs(q) for q in row),Q(0)) for row in E)
    assert RL==[Q(q) for q in rowbound['L_row_absolute_sums']]
    assert B==Q(rowbound['K_max_row_absolute_sum_B']) and G==Q(rowbound['E_max_row_absolute_sum_G'])
    result={'degree':[4,4,6],'leading_data_sha256':digest,'source_words':len(words),'lowest_vectors':k,
            'independent_tree_Jacobi_formal_points':[[0,0],[1,0],[0,1]],
            'all_L_K_E_entries_checked':k*k*3,'all_162_L_row_sums_and_K_E_row_norms_match':True,
            'row_product_bound_source':'frontier-20261028-level6-446-row-product-bound-v1.json',
            'status':'PASS_COMPLETE_INDEPENDENT_F3_ENTRY_AND_ROW_NORMS_ONLY',
            'not_checked':'source horizontal kernel completeness, leading determinant, parent adoption, formal or independent-model review'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS independent full tree-Jacobi L/K/E 78732 entries and row norms;',out.name,flush=True)

if __name__=='__main__':main()
