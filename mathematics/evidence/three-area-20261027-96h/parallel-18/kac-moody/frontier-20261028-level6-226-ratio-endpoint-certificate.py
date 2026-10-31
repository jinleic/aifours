#!/usr/bin/env python3
"""Bracket the exact generalized-eigenvalue endpoint of the chosen cone.

This concerns only the specific leading-left symmetrized certificate, not
optimality of the actual map.  Rational LDL/negative witness; no floats.
"""
import hashlib
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('obstruct',ROOT/'frontier-20261028-level6-226-naive-accretivity-obstruction.py')
obstruct=importlib.util.module_from_spec(spec);spec.loader.exec_module(obstruct)


def main():
    inp=ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json';raw=inp.read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    P=json.loads(raw);assert P['lambda']=='9/2' and P['status']=='ALL_THREE_SYMMETRIC_FORMS_STRICTLY_POSITIVE_DEFINITE'
    plus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_plus_HK']]
    minus=[[Q(q) for q in row] for row in P['symmetric_forms']['lambda_HL_minus_HK']]
    n=len(plus);assert n==34 and all(len(row)==n for row in plus+minus)
    HL=[[(plus[i][j]+minus[i][j])/9 for j in range(n)] for i in range(n)]
    HK=[[(plus[i][j]-minus[i][j])/2 for j in range(n)] for i in range(n)]
    low=Q(449,100);N=[[low*HL[i][j]-HK[i][j] for j in range(n)] for i in range(n)]
    # A negative Schur-complement direction: solve first 33 coordinates exactly.
    m=n-1;v=obstruct.solve([row[:m] for row in N[:m]],[-N[i][m] for i in range(m)])+[Q(1)]
    value=sum((v[i]*N[i][j]*v[j] for i in range(n) for j in range(n)),Q(0));assert value<0
    # Upper endpoint relies on the three independently replayed positive forms,
    # not on the output of this witness-only check.
    out=ROOT/'frontier-20261028-level6-226-ratio-endpoint-certificate-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'ratio_certificate_sha256':digest,'dimension':n,'lambda_lower':'449/100','lambda_upper':'9/2',
            'negative_form':'(449/100)HL-HK','exact_negative_vector':[str(q) for q in v],
            'exact_negative_quadratic_value':str(value),'negative_value_strict':True,
            'endpoint_definition':'maximum absolute real generalized eigenvalue of HK v = lambda HL v',
            'status':'EXACT_LOWER_NEGATIVE_WITNESS_AND_NAMED_UPPER_FORM',
            'scope':'sharp coefficient for this chosen symmetric-form certificate, not an optimal actual map region'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact negative direction at 449/100; named positive upper 9/2;',out.name,flush=True)

if __name__=='__main__':main()
