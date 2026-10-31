#!/usr/bin/env python3
"""Find a compact rational common numerator with a fixed positive SDP margin.
Floating-point SDP is exploratory; exact rational Sturm signs certify a returned
candidate. Import is solely the current local pairing/Sturm discovery helper;
an independent exact Bernstein verifier is still required for promotion.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import cvxpy as cp
import numpy as np

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('discovery',HERE/'frontier-20261028-sdp-witness-v1.py')
helper=importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--margin',default='1/1000')
    args=p.parse_args()
    raw=Path(args.input).read_bytes()
    data=json.loads(raw)['simplified']['certificate']
    corners=[[Q(x) for x in row] for row in data['corners']]
    lo=[Q(x) for x in data['lower']]; hi=[Q(x) for x in data['upper']]
    scale=np.array([float((lo[i]+hi[i])/2) for i in range(7)])
    margin=Q(args.margin)
    if not 0<margin<1:
        raise ValueError('margin must lie strictly between0 and1')
    x=cp.Variable(7); b=cp.hstack([x,1])
    constraints=[]
    for a in corners:
        vec=[]
        for j in range(8):
            unit=[Q(0)]*8; unit[j]=Q(1)
            vec.append(helper.pairing(a,unit))
        A=np.array([[float(vec[j][k]) for j in range(8)] for k in range(8)])
        M=cp.Variable((4,4),symmetric=True); N=cp.Variable((4,4),symmetric=True)
        constraints.extend([M>>0,N>>0])
        for k in range(8):
            m=sum(M[i,j] for i in range(4) for j in range(4) if i+j==k)
            n=sum(N[i,j] for i in range(4) for j in range(4) if i+j+1==k)
            constraints.append(A[k,:]@b==float(margin)*math.comb(7,k)+m+n)
    prob=cp.Problem(cp.Minimize(cp.norm1(cp.multiply(1/scale,x))),constraints)
    prob.solve(solver='CLARABEL',max_iter=400,tol_gap_abs=1e-9,tol_feas=1e-9,tol_gap_rel=1e-9)
    result={'status':prob.status,'objective':float(prob.value) if prob.value is not None else None,
            'margin_requested':str(margin),'iterations':prob.solver_stats.num_iters,
            'b_float':[float(v) for v in x.value]+[1.0] if x.value is not None else None}
    exact=None
    if result['b_float']:
        for den in (10,100,1000,10000,100000,1000000):
            bq=[Q(float(v)).limit_denominator(den) for v in result['b_float'][:7]]+[Q(1)]
            cert=[helper.positivity_certificate(helper.pairing(a,bq)) for a in corners]
            if all(z is not None for z in cert):
                exact={'b':[str(z) for z in bq],'max_rounding_denominator':den,
                       'corner_positive_polynomial_certificates':cert}
                break
    with Path(args.output).open('x',encoding='utf-8') as f:
        json.dump({'schema':1,'input_sha256':hashlib.sha256(raw).hexdigest(),
                   'numerical_result':result,'exact_candidate':exact,
                   'scope':'one actual box; numerical SDP does not prove global positivity, exact rational Sturm check applies only if candidate is present; independent Bernstein replay still required'},f,indent=2,sort_keys=True,allow_nan=False)
        f.write('\n')
    print('status:',result['status'],'numerical objective:',result['objective'])
    print('exact rational candidate:',json.dumps(exact['b']) if exact else 'NONE')
    if exact:
        for i,c in enumerate(exact['corner_positive_polynomial_certificates']):
            print('corner',i,'positive roots',c['positive_root_count'],'constant',c['strict_positive_constant'])


if __name__=='__main__':
    main()
