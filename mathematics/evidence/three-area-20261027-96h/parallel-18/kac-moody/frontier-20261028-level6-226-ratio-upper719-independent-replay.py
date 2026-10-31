#!/usr/bin/env python3
"""Check the two 719/160 upper forms by exact Sylvester determinants."""
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
    P=json.loads(raw);U=json.loads((ROOT/'frontier-20261028-level6-226-ratio-upper719-certificate-v1.json').read_text())
    assert U['status']=='BOTH_UPPER_FORMS_STRICTLY_PD'
    plus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_plus_HK']]
    minus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_minus_HK']];n=len(plus);assert n==34
    # (719/160)HL±HK = (719/1440)(plus+minus) ± (plus-minus)/2.
    values={}
    for name,sgn in [('upper_HL_plus_HK',1),('upper_HL_minus_HK',-1)]:
        M=[[Q(719,1440)*(plus[i][j]+minus[i][j])+sgn*(plus[i][j]-minus[i][j])/2 for j in range(n)] for i in range(n)]
        assert M==[[Q(q) for q in row] for row in U['forms'][name]]
        minors=[]
        for k in range(1,n+1):
            rows=[row[:k] for row in M[:k]];scales=[math.lcm(*(q.denominator for q in row)) for row in rows]
            integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(rows)]
            d=Q(det.bareiss(integer),math.prod(scales));assert d>0;minors.append(str(d))
        values[name]=minors
    out=ROOT/'frontier-20261028-level6-226-ratio-upper719-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'lambda_upper':'719/160','dimension':n,'positive_principal_determinants':values,
                               'status':'PASS_68_EXACT_POSITIVE_SYLVESTER_MINORS',
                               'scope':'given independently reconstructed original target Gram forms; no global optimum/formal/external model claim'},indent=2)+'\n')
    print('PASS lambda=719/160: 68 exact positive leading-principal determinants;',out.name)

if __name__=='__main__':main()
