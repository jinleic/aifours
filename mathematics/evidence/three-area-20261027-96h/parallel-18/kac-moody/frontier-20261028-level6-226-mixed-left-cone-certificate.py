#!/usr/bin/env python3
"""Exact full-target type125 cone using X=L+(1/50)A and lambda=217/50."""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ratio',ROOT/'frontier-20261028-level6-226-ratio-cone-certificate.py')
ratio=importlib.util.module_from_spec(spec);spec.loader.exec_module(ratio)


def main():
    raw=(ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json').read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    P=json.loads(raw);n=P['whole_lowest_dim'];data=[[[Q(q) for q in e] for e in row] for row in P['full_target_affine_entries']]
    assert n==34 and len(data)==235
    old0=[[Q(q) for q in row] for row in P['symmetric_forms']['H0']]
    oldplus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_plus_HK']]
    oldminus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_minus_HK']]
    HL=[[(oldplus[i][j]+oldminus[i][j])/9 for j in range(n)] for i in range(n)]
    HK=[[(oldplus[i][j]-oldminus[i][j])/2 for j in range(n)] for i in range(n)]
    HAK=[[sum((row[i][0]*(row[j][1]-row[j][2])+(row[i][1]-row[i][2])*row[j][0] for row in data),Q(0)) for j in range(n)] for i in range(n)]
    gamma=Q(1,50);lam=Q(217,50)
    LG=[[HL[i][j]+gamma*old0[i][j] for j in range(n)] for i in range(n)]
    KG=[[HK[i][j]+gamma*HAK[i][j] for j in range(n)] for i in range(n)]
    forms={'lambda_HLx_plus_HKx':[[lam*LG[i][j]+KG[i][j] for j in range(n)] for i in range(n)],
           'lambda_HLx_minus_HKx':[[lam*LG[i][j]-KG[i][j] for j in range(n)] for i in range(n)]}
    piv={name:[str(q) for q in ratio.pivots_positive(M)] for name,M in forms.items()}
    result={'degree':[2,2,6],'source_ratio_certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'target_rows':235,'source_columns':n,'gamma':'1/50','lambda':'217/50',
            'mixed_left':'X=L+(1/50)A, L=B+C, K=B-C',
            'HAK':[[str(q) for q in row] for row in HAK],
            'forms':{name:[[str(q) for q in row] for row in M] for name,M in forms.items()},
            'strict_positive_LDL_pivots':piv,'status':'BOTH_MIXED_LEFT_SLOPE_FORMS_STRICTLY_PD',
            'scope':'given separately replayed full target pencil; baseline and HL positivity follow from original H0/HL'}
    out=ROOT/'frontier-20261028-level6-226-mixed-left-cone-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS X=L+A/50, lambda=217/50: both 34x34 slope forms have positive LDL pivots;',out.name,flush=True)

if __name__=='__main__':main()
