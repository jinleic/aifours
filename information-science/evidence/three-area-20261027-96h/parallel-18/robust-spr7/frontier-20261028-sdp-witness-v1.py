#!/usr/bin/env python3
"""Find a monic unrestricted numerator for the exact rational candidate box.

Floating point SDP is discovery ONLY. Each rounded rational numerator is
checked exactly on the entire half-line using an independently implemented
rational Sturm chain for all four actual Kharitonov corners. A separate
checker should replay the final witness and box-stability certificates.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import cvxpy as cp
import numpy as np


def conv(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def pairing(a,b):
    ea=[a[0],-a[2],a[4],-a[6]]
    oa=[a[1],-a[3],a[5],-a[7]]
    eb=[b[0],-b[2],b[4],-b[6]]
    ob=[b[1],-b[3],b[5],-b[7]]
    first=conv(ea,eb)
    second=conv(oa,ob)
    out=first+[Q(0)]
    for j,x in enumerate(second):
        out[j+1]+=x
    return out


def trim(p):
    while p and p[-1]==0:
        p.pop()
    return p


def negative_remainder(a,b):
    r=a.copy()
    while len(r)>=len(b) and r:
        c=r[-1]/b[-1]; shift=len(r)-len(b)
        for j in range(len(b)):
            r[j+shift]-=c*b[j]
        trim(r)
    return [-x for x in r]


def sign_at_zero(p):
    return (p[0]>0)-(p[0]<0)


def sign_at_infinity(p):
    return (p[-1]>0)-(p[-1]<0)


def variations(signs):
    s=[x for x in signs if x]
    return sum(1 for a,b in zip(s,s[1:]) if a!=b)


def positivity_certificate(p):
    p=trim(p.copy())
    if not p or p[0]<=0 or p[-1]<=0:
        return None
    derivative=[Q(j)*p[j] for j in range(1,len(p))]
    seq=[p,trim(derivative)]
    while seq[-1]:
        nxt=negative_remainder(seq[-2],seq[-1])
        if not nxt:
            break
        # Positive rational normalization controls integer growth and preserves signs.
        lead_abs=abs(nxt[-1]); seq.append([x/lead_abs for x in nxt])
    z=[sign_at_zero(q) for q in seq]
    inf=[sign_at_infinity(q) for q in seq]
    count=variations(z)-variations(inf)
    if count!=0:
        return None
    return {'coefficient':[str(x) for x in p], 'sturm_signs_at_zero':z,
            'sturm_signs_at_positive_infinity':inf, 'positive_root_count':count,
            'strict_positive_constant':str(p[0]),'strict_positive_leading':str(p[-1]),
            'sequence_degrees':[len(q)-1 for q in seq]}


def solve(corners,solver):
    matrices=[]
    for a in corners:
        vectors=[]
        for j in range(8):
            unit=[Q(0)]*8; unit[j]=Q(1)
            vectors.append(pairing(a,unit))
        matrices.append(np.asarray([[float(vectors[j][k]) for j in range(8)] for k in range(8)]))
    x=cp.Variable(7)
    eps=cp.Variable(nonneg=True)
    b=cp.hstack([x,1])
    constraints=[eps<=1]
    for A in matrices:
        M=cp.Variable((4,4),symmetric=True)
        N=cp.Variable((4,4),symmetric=True)
        constraints.extend([M>>0,N>>0])
        for k in range(8):
            m=sum(M[i,j] for i in range(4) for j in range(4) if i+j==k)
            n=sum(N[i,j] for i in range(4) for j in range(4) if i+j+1==k)
            constraints.append(A[k,:]@b == math.comb(7,k)*eps+m+n)
    problem=cp.Problem(cp.Maximize(eps),constraints)
    if solver=='CLARABEL':
        problem.solve(solver=solver,max_iter=350,tol_gap_abs=1e-9,tol_feas=1e-9,tol_gap_rel=1e-9)
    else:
        problem.solve(solver=solver,eps=1e-6,max_iters=12000,verbose=False)
    if x.value is None:
        return {'status':problem.status,'margin':None,'b_float':None}
    return {'status':problem.status,'margin':float(eps.value),
            'b_float':[float(v) for v in x.value]+[1.0],
            'solver_iterations':problem.solver_stats.num_iters}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--solver',choices=('CLARABEL','SCS'),default='CLARABEL')
    args=p.parse_args()
    raw=Path(args.input).read_bytes()
    data=json.loads(raw)['simplified']['certificate']
    corners=[[Q(x) for x in a] for a in data['corners']]
    result=solve(corners,args.solver)
    exact=None
    if result['b_float']:
        for denominator in (10,100,1000,10000,100000,1000000,10000000):
            b=[Q(float(x)).limit_denominator(denominator) for x in result['b_float'][:7]]+[Q(1)]
            certs=[positivity_certificate(pairing(a,b)) for a in corners]
            if all(c is not None for c in certs):
                exact={'b':[str(x) for x in b],'rounding_max_denominator':denominator,
                       'corner_positive_polynomial_certificates':certs}
                break
    receipt={'schema':1,'input_sha256':hashlib.sha256(raw).hexdigest(),
             'solver':args.solver,'numerical_result':result,'exact_witness':exact,
             'scope':'SDP output alone is numerical; exact witness if present uses exact rational Sturm positivity on every corner, plus independent box stability certificate and four-corner fixed-b reduction for the whole box.'}
    with Path(args.output).open('x',encoding='utf-8') as f:
        json.dump(receipt,f,indent=2,sort_keys=True,allow_nan=False)
        f.write('\n')
    print('SDP STATUS:',result['status'],'numerical margin:',result['margin'])
    print('EXACT COMMON NUMERATOR:',json.dumps(exact['b']) if exact else 'NOT FOUND')
    if exact:
        for i,c in enumerate(exact['corner_positive_polynomial_certificates']):
            print('corner',i,'positive root count',c['positive_root_count'],
                  'constant',c['strict_positive_constant'],'leading',c['strict_positive_leading'])


if __name__=='__main__':
    main()
