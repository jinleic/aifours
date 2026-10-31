#!/usr/bin/env python3
"""Exact all-variable strip certificate from the full level-six mixed minor.

For y=x+g, 0<=g<=41, write P(x,x+g)=sum_j f_j(g)x^j.
For m=deg f_j, q_j(z)=(1+z)^m f_j(41z/(1+z)) has strictly
negative coefficients, proving f_j<0 on the full closed interval.  The
opposite chamber uses exact node exchange, not coefficient symmetry.
"""
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    inp=ROOT/'frontier-20261028-level6-free-22-determinant-v1.json'
    dest=ROOT/'frontier-20261028-level6-226-gap41-sign-certificate-v1.json'
    if dest.exists():raise FileExistsError(dest)
    b=inp.read_bytes();digest=hashlib.sha256(b).hexdigest()
    assert digest=='874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'
    P=json.loads(b);assert P['degree']==[2,2,6] and P['matrix_size']==34 and P['status']=='MIXED_OR_ZERO_CONSTANT'
    coef={};n=34
    for item in P['determinant_coefficients']:
        i,j=item['x_power'],item['y_power'];assert type(i)==type(j)==int and i>=0 and j>=0 and i+j<=n and (i,j) not in coef
        coef[i,j]=Q(item['coefficient']);assert coef[i,j]
    assert len(coef)==592
    # P(x,x+g) = sum_{j>=0} f_j(g)x^j.
    functions=defaultdict(lambda:defaultdict(Q))
    for (i,j),q in coef.items():
        for h in range(j+1):functions[i+j-h][h]+=q*math.comb(j,h)
    assert set(functions)==set(range(n+1))
    transformed=[];count=0
    for j in range(n+1):
        f={h:q for h,q in functions[j].items() if q};m=max(f)
        qz=[sum((f.get(h,Q(0))*41**h*math.comb(m-h,k-h) for h in range(k+1)),Q(0)) for k in range(m+1)]
        assert all(q<0 for q in qz),(j,m,qz)
        transformed.append({'x_power':j,'gap_degree':m,'transformed_coefficients':[str(q) for q in qz]})
        count+=len(qz)
    assert count==620
    xaxis={i:q for (i,j),q in coef.items() if j==0};yaxis={j:q for (i,j),q in coef.items() if i==0}
    assert coef[0,0]<0 and max(xaxis)==27 and xaxis[27]>0 and max(yaxis)==30 and yaxis[30]>0
    result={'source_mixed_polynomial_sha256':digest,'degree':P['degree'],'matrix_size':n,'gap_upper':41,
            'chamber':'r>=6, s>=r, 0<=s-r<=41; node exchange gives all |r-s|<=41',
            'coefficients_negative':True,'coefficient_functions':len(transformed),'strictly_negative_transformed_terms':count,
            'functions':transformed,'axis_constant':str(coef[0,0]),'x_axis_leading_degree':27,
            'x_axis_leading_coefficient':str(xaxis[27]),'y_axis_leading_degree':30,
            'y_axis_leading_coefficient':str(yaxis[30]),
            'axis_root_caveat':'IVT gives real positive roots of this selected minor on both coordinate axes; not a full-map kernel or integer-parameter witness',
            'status':'EXACT_ALL_VARIABLE_CLOSED_GAP41_STRIP_SIGN',
            'scope':'conditional on full actual source/ideal identification and entire polynomial determinant identity; not formal or independent-model review'}
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS closed gap<=41: 35 coefficient functions, 620 strictly negative transformed terms; both selected-minor real axis roots;',dest.name,flush=True)

if __name__=='__main__':main()
