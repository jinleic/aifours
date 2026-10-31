#!/usr/bin/env python3
"""Exact full-target accretive ratio cone for the level-six 125 source.

L=B+C is used as the left test, NOT the disproved A^T shortcut. Three real
symmetric Gram forms are certified positive definite by exact rational LDL.
No positivity of the nonsymmetrizable Lie form is assumed.
"""
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('al6',ROOT/'frontier-20261028-level6-alternate-type-minor-search.py')
al6=importlib.util.module_from_spec(spec);spec.loader.exec_module(al6)


def pivots_positive(M):
    n=len(M);A=[row[:] for row in M];piv=[]
    for z in range(n):
        d=A[z][z];assert d>0,('nonpositive LDL pivot',z,d);piv.append(d)
        for i in range(z+1,n):
            for j in range(i,n):
                q=A[i][j]-A[i][z]*A[z][j]/d;A[i][j]=q;A[j][i]=q
    return piv


def main():
    P=json.loads((ROOT/'frontier-20261028-level6-free-22-pencil-v1.json').read_text());rows=al6.full_rows(P)
    n=P['joint_horizontal_kernel_dim'];assert n==34 and len(rows)==235
    words=sorted(rows);data=[rows[w] for w in words]
    H0=[];HL=[];HK=[]
    for i in range(n):
        row0=[];rowL=[];rowK=[]
        for j in range(n):
            a0=ll=kk=Q(0)
            for v in data:
                Li=Q(v[i][1])+Q(v[i][2]);Lj=Q(v[j][1])+Q(v[j][2])
                Ki=Q(v[i][1])-Q(v[i][2]);Kj=Q(v[j][1])-Q(v[j][2])
                a0+=Li*Q(v[j][0])+Q(v[i][0])*Lj
                ll+=2*Li*Lj;kk+=Li*Kj+Ki*Lj
            row0.append(a0);rowL.append(ll);rowK.append(kk)
        H0.append(row0);HL.append(rowL);HK.append(rowK)
    lam=Q(9,2)
    plus=[[lam*HL[i][j]+HK[i][j] for j in range(n)] for i in range(n)]
    minus=[[lam*HL[i][j]-HK[i][j] for j in range(n)] for i in range(n)]
    forms={'H0':H0,'lambda_HL_plus_HK':plus,'lambda_HL_minus_HK':minus}
    pivots={name:[str(q) for q in pivots_positive(M)] for name,M in forms.items()}
    result={'degree':P['degree'],'source_dim':P['free_source_dim'],'whole_lowest_dim':n,
            'target_word_rows':words,'full_target_affine_entries':[[[str(q) for q in e] for e in row] for row in data],
            'lambda':'9/2','matrix_definitions':'L=B+C,K=B-C; H0=L^T A+A^T L; HL=2 L^T L; HK=L^T K+K^T L',
            'symmetric_forms':{name:[[str(q) for q in row] for row in M] for name,M in forms.items()},
            'strict_positive_LDL_pivots':pivots,'pivot_count_each':n,
            'condition':'(r-6)+(s-6) >= (9/2)*abs(r-s), r,s>=6',
            'status':'ALL_THREE_SYMMETRIC_FORMS_STRICTLY_POSITIVE_DEFINITE',
            'scope':'full current-round target pencil at named free-Levi/PBW inputs; not formal or external-model review'}
    out=ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS full target 235 rows; H0 and (9/2)HL ± HK each have 34 positive exact LDL pivots;',out.name,flush=True)

if __name__=='__main__':main()
