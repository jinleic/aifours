#!/usr/bin/env python3
"""Generate a rational approximate inverse for later exact validation.

Floating inverse is only a proposal. A separate integer verifier determines
whether it supplies a rigorous matrix norm bound.
"""
from pathlib import Path
import hashlib
import json
import sys
import numpy as np

sys.set_int_max_str_digits(0)
HERE=Path(__file__).parent
CERT=HERE/'frontier-20261028-grid-generic-exact-certificate-v1.json'
BASIS=HERE/'frontier-20261028-grid-generic-open-basis-v1.json'
OUT=HERE/'frontier-20261028-grid-normalized-inverse-v1.json'
Q=10**10

def features(z):
    out=[a*a+b*b for a,b in z]
    for i in range(9):
        for j in range(i+1,9):
            a,b=z[i];c,d=z[j];out.extend((a*c+b*d,b*c-a*d))
    return out

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    c=json.loads(CERT.read_text());basis=json.loads(BASIS.read_text());indices=basis['selected_indices_zero_based']
    cols=[]
    for j in indices:
        z=[(int(x),int(y)) for x,y in c['atoms'][j]['coefficients']]
        s=sum(a*a+b*b for a,b in z)
        cols.append(np.array(features(z),dtype=float)/float(s))
    B=np.column_stack(cols);X=np.linalg.inv(B)
    ints=[[int(round(float(x)*Q)) for x in row] for row in X]
    payload={'schema_version':1,'kind':'APPROXIMATE_NORMALIZED_INVERSE_PROPOSAL',
             'certificate_sha256':digest(CERT),'basis_sha256':digest(BASIS),
             'scale':Q,'matrix':ints,
             'limits':'proposal only; exact integer residual must be independently checked'}
    with open(OUT,'x',encoding='utf-8') as f:json.dump(payload,f,separators=(',',':'))
    print(json.dumps({'matrix_shape':list(X.shape),'float_inverse_inf_norm':float(np.linalg.norm(X,ord=np.inf)),
                      'float_inverse_residual_inf':float(np.linalg.norm(X@B-np.eye(81),ord=np.inf)),
                      'artifact':str(OUT),'limits':'floating proposal, not a certified bound'},indent=2))


if __name__=='__main__':main()
