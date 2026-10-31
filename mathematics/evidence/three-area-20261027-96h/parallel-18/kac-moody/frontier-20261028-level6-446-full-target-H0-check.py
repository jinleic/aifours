#!/usr/bin/env python3
"""Exact positivity/obstruction of the 1780-row 446 H0 left test.

Block int64 Gram products are admitted only under a proved per-block bound;
block results accumulate in Python arbitrary-precision integers.  The full
symmetric leading-minor sequence is evaluated by integer Bareiss recurrence.
No D3 kernel or global no-go follows from a failed test.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent


def main():
    inp=ROOT/'frontier-20261028-level6-446-full-target-pencil-v1.json';raw=inp.read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='f4289288531b1b8aa169121c5709968924a075b4b7e749874c75ae7ab53331f3'
    P=json.loads(raw);assert P['status']=='ALL_NONZERO_TREE_JACOBI_TARGET_ROWS_RECONSTRUCTED'
    m=P['target_row_count'];n=P['whole_lowest_dim'];D=10368;assert m==1780 and n==162
    L=np.zeros((m,n),dtype=np.int64);E=np.zeros((m,n),dtype=np.int64)
    for i,row in enumerate(P['rows']):
        for e in row['entries']:
            j=e['column'];lv,ev=Q(e['L']),Q(e['E']);assert (lv*D).denominator==(ev*D).denominator==1
            li,ei=int(lv*D),int(ev*D);assert abs(li)<2**62 and abs(ei)<2**62
            L[i,j]=li;E[i,j]=ei
    ml=int(np.max(np.abs(L)));me=int(np.max(np.abs(E)));assert 6*ml+me<2**63
    A=6*L+E;ma=int(np.max(np.abs(A)))
    block=max(1,min(m,(2**63-1)//(2*ml*ma)))
    assert 2*block*ml*ma<2**63
    H=np.zeros((n,n),dtype=object)
    for a in range(0,m,block):
        lb=L[a:a+block,:];ab=A[a:a+block,:]
        h=lb.T@ab+ab.T@lb
        H+=h.astype(object)
    assert np.array_equal(H,H.T)
    Aint=[[int(v) for v in row] for row in H.tolist()];prev=1;piv=[];failure=None
    for k in range(n-1):
        q=Aint[k][k]
        if q<=0:failure={'first_nonpositive_pivot_index':k,'pivot':str(q)};break
        piv.append(str(q))
        for i in range(k+1,n):
            for j in range(i,n):
                v=Aint[i][j]*q-Aint[i][k]*Aint[k][j];assert v%prev==0
                v//=prev;Aint[i][j]=v;Aint[j][i]=v
        for i in range(k+1,n):Aint[i][k]=Aint[k][i]=0
        prev=q
        if (k+1)%16==0:print('full target H0 positive leading pivots',k+1,'of',n,flush=True)
    if failure is None:
        if Aint[-1][-1]<=0:failure={'first_nonpositive_pivot_index':n-1,'pivot':str(Aint[-1][-1])}
        else:piv.append(str(Aint[-1][-1]))
    result={'degree':[4,4,6],'input_sha256':digest,'target_rows':m,'source_columns':n,
            'common_denominator':D,'gram_form':'H0=L^T(6L+E)+(6L+E)^T L',
            'int64_block_size':block,'int64_per_block_abs_bound':2*block*ml*ma,
            'verified_positive_leading_pivots':len(piv),'positive_pivots':piv,'failure':failure,
            'status':'FULL_TARGET_H0_PD' if failure is None else 'FULL_TARGET_H0_NOT_PD',
            'scope':'given independent-tree full target pencil; no source/rank/full map theorem or independent review'}
    out=ROOT/'frontier-20261028-level6-446-full-target-H0-check-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE full target H0',result['status'],'positive prefix',len(piv),out.name,flush=True)

if __name__=='__main__':main()
