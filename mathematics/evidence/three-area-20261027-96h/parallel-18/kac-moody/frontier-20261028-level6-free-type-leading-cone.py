#!/usr/bin/env python3
"""Exact leading-row cofactor cone for an entire free level-six type.

A mixed-sign full determinant or a bounded failed alternate search does NOT
imply a rank defect. This checks the original full-size selected minor's
leading t-coefficient and returns only the explicit proved norm cone.
"""
import argparse
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('det',ROOT/'frontier-20261028-level5-type-determinant.py')
det=importlib.util.module_from_spec(spec);spec.loader.exec_module(det)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);args=ap.parse_args();a,b=args.a,args.b
    P=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json').read_text())
    out=ROOT/f'frontier-20261028-level6-free-{a}{b}-leading-cone-v1.json'
    if out.exists():raise FileExistsError(out)
    assert P['status']=='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    A=[[[Q(q) for q in e] for e in row] for row in P['matrix']];k=len(A)
    L=[[e[1]+e[2] for e in row] for row in A]
    K=[[e[1]-e[2] for e in row] for row in A]
    E=[[e[0]-6*(e[1]+e[2]) for e in row] for row in A]
    scales=[math.lcm(*(q.denominator for q in row)) for row in L]
    integer=[[int(q*scales[i]) for q in row] for i,row in enumerate(L)]
    delta=Q(det.bareiss(integer),math.prod(scales))
    result={'degree':P['degree'],'free_source_dim':P['free_source_dim'],'horizontal_kernel_dim':k,
            'leading_determinant':str(delta),'formal_parameters':'r=t+d,s=t-d; D=tL+dK+E',
            'first_full_polynomial_mixed_not_erased':True,
            'scope':'actual full quotient only for r,s>=6 at named free-Levi/PBW source input',
            'not_formal_or_external_model_review':True}
    if not delta:result['status']='LEADING_MINOR_ZERO_NO_CONE'
    else:
        Rs=[sum((abs(q) for q in row),Q(0)) for row in L];assert all(Rs)
        H=Q(k)*math.prod(Rs)/(min(Rs)*abs(delta))
        B=max(sum((abs(q) for q in row),Q(0)) for row in K)
        G=max(sum((abs(q) for q in row),Q(0)) for row in E)
        result.update({'status':'LEADING_INJECTIVE_ROW_PRODUCT_CONE','L_row_sums':[str(q) for q in Rs],
                       'inverse_bound_H':str(H),'K_max_row_sum_B':str(B),'E_max_row_sum_G':str(G),
                       'criterion':'t > H*(B*abs(d)+G)',
                       'matrix_entries':[[[str(L[i][j]),str(K[i][j]),str(E[i][j])] for j in range(k)] for i in range(k)]})
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE level6',P['degree'],'lowest',k,'leading',result['status'],out.name,flush=True)

if __name__=='__main__':main()
