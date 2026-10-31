#!/usr/bin/env python3
"""Exact 162-source selected-target accretivity attempt.

Uses int64 matrix multiplication only after proving a rigorous bound for all
intermediates, then Python-integer fraction-free Sylvester elimination. If a
pivot is not positive, records that obstruction, never a no-go theorem.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent


def sylvester(M):
    A=[[int(q) for q in row] for row in M.tolist()];n=len(A);previous=1;piv=[]
    for k in range(n-1):
        z=A[k][k]
        if z<=0:return {'positive_definite':False,'first_nonpositive_pivot_index':k,'pivot':str(z),'verified_positive_prefix':len(piv)}
        piv.append(str(z))
        for i in range(k+1,n):
            for j in range(i,n):
                numerator=A[i][j]*z-A[i][k]*A[k][j]
                assert numerator%previous==0
                v=numerator//previous;A[i][j]=v;A[j][i]=v
        for i in range(k+1,n):A[i][k]=A[k][i]=0
        previous=z
    if A[-1][-1]<=0:return {'positive_definite':False,'first_nonpositive_pivot_index':n-1,'pivot':str(A[-1][-1]),'verified_positive_prefix':len(piv)}
    piv.append(str(A[-1][-1]));return {'positive_definite':True,'leading_principal_determinants':piv,'verified_positive_prefix':len(piv)}


def main():
    inp=ROOT/'frontier-20261028-level6-446-leading-map-cone-v1.json';raw=inp.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='606b1cfe1fdadf3d741b0d5aa649ac59a7fc7ca094ff68cf242096cc76adf3ed'
    P=json.loads(raw);assert P['status']=='LEADING_INJECTIVE_COFAC_CONE';n=162;D=10368
    rows=[[[Q(q) for q in e] for e in row] for row in P['matrix_entries']];assert len(rows)==n and all(len(row)==n for row in rows)
    assert all((q*D).denominator==1 for row in rows for e in row for q in e)
    L=np.array([[int(e[0]*D) for e in row] for row in rows],dtype=np.int64)
    K=np.array([[int(e[1]*D) for e in row] for row in rows],dtype=np.int64)
    E=np.array([[int(e[2]*D) for e in row] for row in rows],dtype=np.int64);A=6*L+E
    ml=int(np.max(np.abs(L)));mk=int(np.max(np.abs(K)));ma=int(np.max(np.abs(A)))
    bounds={'H0':2*n*ml*ma,'HL':2*n*ml*ml,'HK':2*n*ml*mk}
    assert bounds['H0']<2**63 and 10*bounds['HL']+bounds['HK']<2**63
    H0=L.T@A+A.T@L;HL=2*(L.T@L);HK=L.T@K+K.T@L
    matrices={'H0':H0,'10HL_plus_HK':10*HL+HK,'10HL_minus_HK':10*HL-HK}
    results={}
    for name,M in matrices.items():
        assert np.array_equal(M,M.T)
        results[name]=sylvester(M)
        print(name,'positive',results[name]['positive_definite'],'prefix',results[name]['verified_positive_prefix'],flush=True)
        if not results[name]['positive_definite']:break
    ok=len(results)==3 and all(v['positive_definite'] for v in results.values())
    out=ROOT/'frontier-20261028-level6-446-selected-accretivity-attempt-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':[4,4,6],'source_data_sha256':hashlib.sha256(raw).hexdigest(),
                               'dimension':n,'common_denominator':D,'lambda':'10',
                               'exact_int64_intermediate_bounds':bounds,'forms':results,
                               'status':'ALL_THREE_SELECTED_FORMS_PD' if ok else 'SELECTED_FORM_NOT_CERTIFIED_PD',
                               'scope':'selected 162 target coordinates only; no all-quadrant, full-map kernel, formal or independent review claim'},indent=2)+'\n')
    print('DONE', 'ALL_THREE_SELECTED_FORMS_PD' if ok else 'SELECTED_FORM_NOT_CERTIFIED_PD',out.name,flush=True)

if __name__=='__main__':main()
