#!/usr/bin/env python3
"""Independently reconstruct and check the negative 57x57 principal minor.

This checks only the selected-target Euclidean left test H0; it is NOT a
full-map kernel or a no-go theorem for other target metrics/left tests.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('det',ROOT/'frontier-20261028-level5-type-determinant.py')
det=importlib.util.module_from_spec(spec);spec.loader.exec_module(det)


def main():
    raw=(ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);old=json.loads((ROOT/'frontier-20261028-level6-446-selected-accretivity-attempt-v1.json').read_text())
    assert old['status']=='SELECTED_FORM_NOT_CERTIFIED_PD' and old['forms']['H0']['first_nonpositive_pivot_index']==56
    D=10368;n=162;m=57
    data=[[[Q(q) for q in e] for e in row] for row in P['matrix_entries']]
    assert len(data)==n and all(len(row)==n for row in data)
    L=[[int(data[k][j][0]*D) for j in range(m)] for k in range(n)]
    E=[[int(data[k][j][2]*D) for j in range(m)] for k in range(n)]
    assert all(Q(L[k][j],D)==data[k][j][0] and Q(E[k][j],D)==data[k][j][2] for k in range(n) for j in range(m))
    A=[[6*L[k][j]+E[k][j] for j in range(m)] for k in range(n)]
    H=[[sum(L[k][i]*A[k][j]+A[k][i]*L[k][j] for k in range(n)) for j in range(m)] for i in range(m)]
    assert H[0][0]>0
    value=det.bareiss(H);assert value<0 and value==int(old['forms']['H0']['pivot'])
    result={'degree':[4,4,6],'dimension':162,'selected_target_rows':162,'common_scale_denominator':D,
            'positive_first_diagonal_scaled':str(H[0][0]),'negative_57_by_57_leading_determinant_scaled':str(value),
            'status':'PASS_SELECTED_H0_HAS_BOTH_SIGNS',
            'scope':'ONLY H0=L^T A+A^T L on original selected target rows; no full-target or D3 kernel conclusion'}
    out=ROOT/'frontier-20261028-level6-446-selected-accretivity-obstruction-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact selected H0 first diagonal >0 and 57x57 principal determinant <0;',out.name)

if __name__=='__main__':main()
