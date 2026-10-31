#!/usr/bin/env python3
"""Prove both generalized slope forms PD at the exact rational 719/160."""
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
    P=json.loads(raw);plus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_plus_HK']]
    minus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_minus_HK']];n=len(plus);assert n==34
    HL=[[(plus[i][j]+minus[i][j])/9 for j in range(n)] for i in range(n)]
    HK=[[(plus[i][j]-minus[i][j])/2 for j in range(n)] for i in range(n)]
    u=Q(719,160)
    forms={'upper_HL_plus_HK':[[u*HL[i][j]+HK[i][j] for j in range(n)] for i in range(n)],
           'upper_HL_minus_HK':[[u*HL[i][j]-HK[i][j] for j in range(n)] for i in range(n)]}
    pivots={key:[str(q) for q in ratio.pivots_positive(M)] for key,M in forms.items()}
    out=ROOT/'frontier-20261028-level6-226-ratio-upper719-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'source_certificate_sha256':hashlib.sha256(raw).hexdigest(),'dimension':n,'lambda_upper':'719/160',
            'forms':{key:[[str(q) for q in row] for row in M] for key,M in forms.items()},
            'strict_positive_LDL_pivots':pivots,'status':'BOTH_UPPER_FORMS_STRICTLY_PD',
            'scope':'given independently replayed original L/A target forms; no full map/global optimum claim'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS lambda=719/160: both 34x34 symmetric forms have positive LDL pivots;',out.name)

if __name__=='__main__':main()
