#!/usr/bin/env python3
"""Find a vector blocking EVERY C+gamma*(I-P_C)A baseline left test.

Uses exact rational projection onto the full C target image. No full-map
kernel or impossibility of arbitrary left tests is asserted.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('generic',ROOT/'frontier-review-f18-ph7-independent-check.py')
generic=importlib.util.module_from_spec(spec);spec.loader.exec_module(generic)
S=generic.S


def main():
    raw=(ROOT/'frontier-20261028-level6-226-ratio-cone-certificate-v1.json').read_bytes()
    digest=hashlib.sha256(raw).hexdigest();assert digest=='ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b'
    P=json.loads(raw);data=P['full_target_affine_entries'];m=len(data);n=P['whole_lowest_dim'];assert (m,n)==(235,34)
    A=S.Matrix([[S.Rational(data[i][j][0]) for j in range(n)] for i in range(m)])
    C=S.Matrix([[S.Rational(data[i][j][2]) for j in range(n)] for i in range(m)])
    pivots=C.rref()[1];assert len(pivots)==33
    CJ=C[:,pivots];G=CJ.T*CJ;assert G.det()!=0
    U=A-CJ*(G.inv(method='DM')*(CJ.T*A));assert CJ.T*U==S.zeros(33,n)
    null=U.nullspace();assert len(null)==24
    N=S.Matrix.hstack(*null);H=C.T*A+A.T*C;R=N.T*H*N
    # The first 18 directions span a nonsingular positive prefix, while the
    # Schur complement in direction 18 is strictly negative.
    t=18;alpha=R[:t,:t].inv(method='DM')*(-R[:t,t]);q=alpha.col_join(S.Matrix([1]+[0]*(len(null)-t-1)))
    v=N*q;assert U*v==S.zeros(m,1)
    value=(v.T*H*v)[0];assert value<0
    out=ROOT/'frontier-20261028-level6-226-projected-axis-obstruction-v1.json'
    if out.exists():raise FileExistsError(out)
    result={'degree':[2,2,6],'source_ratio_certificate_sha256':digest,'target_rows':m,'source_columns':n,
            's_slope_rank':len(pivots),'slope_basis_columns':list(pivots),'orthogonal_residual_rank':n-len(null),
            'source_vector':[str(x) for x in v],'projected_A_times_vector_zero':True,
            'baseline_C_left_quadratic_value':str(value),'strictly_negative':True,
            'status':'EXACT_ALL_GAMMA_PROJECTED_AXIS_BASELINE_OBSTRUCTION',
            'scope':'only X=C+gamma*(I-proj_imC)A and unweighted tensor-word geometry; not an actual-map kernel or arbitrary-left-test impossibility'}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact C rank33, projected A rank10, vector in residual kernel has negative baseline for EVERY gamma;',out.name,flush=True)

if __name__=='__main__':main()
