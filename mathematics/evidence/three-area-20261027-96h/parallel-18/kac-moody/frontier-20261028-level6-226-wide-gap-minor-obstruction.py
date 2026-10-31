#!/usr/bin/env python3
"""Exact wide-gap IVT obstruction for ONE chosen level-six minor.

For every real gap g>=42, P(0,g)>0 but [v^34]P(v,v+g)<0,
so it has a positive real v-root. This is not a full-map/integer witness.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    inp=ROOT/'frontier-20261028-level6-free-22-determinant-v1.json';raw=inp.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'
    P=json.loads(raw);assert P['degree']==[2,2,6] and P['matrix_size']==34
    terms=P['determinant_coefficients'];coef={}
    for e in terms:
        i,j=e['x_power'],e['y_power'];assert (i,j) not in coef and i>=0 and j>=0 and i+j<=34
        coef[i,j]=Q(e['coefficient'])
    a={j:q for (i,j),q in coef.items() if i==0};assert max(a)==30
    shifted=[sum((a.get(j,Q(0))*math.comb(j,k)*42**(j-k) for j in range(k,31)),Q(0)) for k in range(31)]
    assert all(q>0 for q in shifted)
    # [v^34]P(v,v+g) is independent of g, using total degree<=34.
    leading=sum((q for (i,j),q in coef.items() if i+j==34),Q(0))
    assert leading==Q(-1454389021504438272000)
    result={'degree':P['degree'],'source_polynomial_sha256':hashlib.sha256(raw).hexdigest(),
            'shifted_P_0_42_plus_h_coefficients':[str(q) for q in shifted],
            'all_31_shifted_coefficients_strictly_positive':True,
            'v34_coefficient_of_P_v_vplusg':str(leading),'wide_gap_bound':42,
            'status':'EXACT_WIDE_GAP_SELECTED_MINOR_REAL_ROOT_OBSTRUCTION',
            'conclusion':'for EVERY real g>=42 there exists v>0 real with P(v,v+g)=0 by IVT; no full-map kernel, integer v witness, or all-minor impossibility'}
    out=ROOT/'frontier-20261028-level6-226-wide-gap-minor-obstruction-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 31 positive shifted coefficients and negative v^34 coefficient; selected minor has real root for EVERY gap>=42;',out.name)

if __name__=='__main__':main()
