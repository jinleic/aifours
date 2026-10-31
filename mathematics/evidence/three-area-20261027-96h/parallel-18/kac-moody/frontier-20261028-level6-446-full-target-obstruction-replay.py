#!/usr/bin/env python3
"""Reconstruct and verify full-target H0's negative 125x125 minor exactly.

Block int64 dot products are bounded; their sum and general Bareiss use
unbounded Python integers. This is no D3-kernel/no-go theorem.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('det',ROOT/'frontier-20261028-level5-type-determinant.py')
det=importlib.util.module_from_spec(spec);spec.loader.exec_module(det)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);old=json.loads((ROOT/'frontier-20261028-level6-446-full-target-H0-check-v1.json').read_text())
    assert old['status']=='FULL_TARGET_H0_NOT_PD' and old['failure']['first_nonpositive_pivot_index']==124
    m=P['target_row_count'];n=125;D=10368;assert m==1780
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for q in row['entries']:
            j=q['column']
            if j>=n:continue
            li,ei=Q(q['L'])*D,Q(q['E'])*D;assert li.denominator==ei.denominator==1 and abs(li)<2**62 and abs(ei)<2**62
            L[i,j]=int(li);E[i,j]=int(ei)
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)));block=max(1,min(m,(2**63-1)//(2*ml*ma)))
    assert 2*block*ml*ma<2**63
    H=np.zeros((n,n),dtype=object)
    for start in range(0,m,block):
        l=L[start:start+block,:];a=A[start:start+block,:]
        H+=(l.T@a+a.T@l).astype(object)
    assert H[0,0]>0 and np.array_equal(H,H.T)
    value=det.bareiss([[int(v) for v in row] for row in H.tolist()])
    assert value<0 and value==int(old['failure']['pivot'])
    result={'degree':[4,4,6],'target_rows':m,'source_columns_checked':n,
            'int64_block_size':block,'int64_per_block_abs_bound':2*block*ml*ma,
            'positive_first_diagonal_scaled':str(H[0,0]),'negative_125_by_125_leading_determinant_scaled':str(value),
            'status':'PASS_FULL_TARGET_H0_HAS_BOTH_SIGNS',
            'scope':'given recorded full-target tree-Jacobi pencil; not a full-map kernel, alternate left-test impossibility or independent source proof'}
    out=ROOT/'frontier-20261028-level6-446-full-target-obstruction-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS full1780-row H0: first diagonal >0 and exact 125x125 leading determinant <0;',out.name,flush=True)

if __name__=='__main__':main()
