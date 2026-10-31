#!/usr/bin/env python3
"""Rebuild mixed-left forms directly and certify 68 Sylvester minors."""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('det',ROOT/'frontier-20261028-level5-type-determinant.py')
det=importlib.util.module_from_spec(spec);spec.loader.exec_module(det)


def main():
    raw=(ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    P=json.loads(raw);C=json.loads((ROOT/'frontier-20261028-level6-226-mixed-left-cone-certificate-v1.json').read_text())
    assert C['status']=='BOTH_MIXED_LEFT_SLOPE_FORMS_STRICTLY_PD'
    data=[[[Q(q) for q in e] for e in row] for row in P['full_target_affine_entries']];n=34;m=len(data);assert m==235
    A=[[row[i][0] for i in range(n)] for row in data]
    L=[[row[i][1]+row[i][2] for i in range(n)] for row in data]
    K=[[row[i][1]-row[i][2] for i in range(n)] for row in data]
    X=[[L[h][i]+A[h][i]/50 for i in range(n)] for h in range(m)]
    HL=[[sum((X[h][i]*L[h][j]+L[h][i]*X[h][j] for h in range(m)),Q(0)) for j in range(n)] for i in range(n)]
    HK=[[sum((X[h][i]*K[h][j]+K[h][i]*X[h][j] for h in range(m)),Q(0)) for j in range(n)] for i in range(n)]
    lam=Q(217,50);results={}
    for key,sgn in [('lambda_HLx_plus_HKx',1),('lambda_HLx_minus_HKx',-1)]:
        M=[[lam*HL[i][j]+sgn*HK[i][j] for j in range(n)] for i in range(n)]
        assert M==[[Q(q) for q in row] for row in C['forms'][key]]
        minors=[]
        for size in range(1,n+1):
            sub=[row[:size] for row in M[:size]];scales=[math.lcm(*(q.denominator for q in row)) for row in sub]
            integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(sub)]
            d=Q(det.bareiss(integer),math.prod(scales));assert d>0;minors.append(str(d))
        results[key]=minors
    out=ROOT/'frontier-20261028-level6-226-mixed-left-cone-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'degree':[2,2,6],'target_rows':m,'source_columns':n,'gamma':'1/50','lambda':'217/50',
                               'positive_principal_determinants':results,'status':'PASS_68_EXACT_POSITIVE_MIXED_LEFT_SYLVESTER_MINORS',
                               'scope':'given independently tree-replayed full target matrices; no original-source formal/external-model review'},indent=2)+'\n')
    print('PASS X=L+A/50, lambda=217/50: direct full-target construction and 68 positive exact Sylvester minors;',out.name)

if __name__=='__main__':main()
