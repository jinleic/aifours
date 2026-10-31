#!/usr/bin/env python3
"""Integer verifier for a quantitative normalized inverse/weight bound."""
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import json
import runpy
import sys

sys.set_int_max_str_digits(0)
HERE=Path(__file__).parent
CERT=HERE/'frontier-20261028-grid-generic-exact-certificate-v1.json'
SOURCE=HERE/'frontier-20261028-grid-rationalized-atoms-run-v1.json'
BASIS=HERE/'frontier-20261028-grid-generic-open-basis-v1.json'
INV=HERE/'frontier-20261028-grid-normalized-inverse-v1.json'
helper=runpy.run_path(str(HERE/'frontier-20261028-grid-generic-open-basis-check.py'))
safe=helper['safe']

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def features(z):
    out=[x*x+y*y for x,y in z]
    for i in range(9):
        for j in range(i+1,9):
            a,b=z[i];c,d=z[j];out.extend((a*c+b*d,b*c-a*d))
    return out

def main():
    cert=json.loads(CERT.read_text());data=json.loads(SOURCE.read_text())
    basis=json.loads(BASIS.read_text());inv=json.loads(INV.read_text())
    if inv['certificate_sha256']!=digest(CERT) or inv['basis_sha256']!=digest(BASIS):
        raise AssertionError('inverse input hashes')
    if basis['input_chart_parameters_sha256']!=digest(SOURCE):raise AssertionError('chart hash')
    atoms=cert['atoms'];orig=data['active_atoms'];den=int(cert['common_denominator']);Q=inv['scale']
    if len(atoms)!=len(orig) or len(inv['matrix'])!=81:raise AssertionError('dimensions')
    norms=[];columns=[];min_lower=F(1)
    for entry,row in zip(atoms,orig):
        N=int(entry['weight_numerator']);z=[(int(x),int(y)) for x,y in entry['coefficients']]
        s=sum(x*x+y*y for x,y in z)
        if N<=0 or s<=0 or N*s*(1<<18)<=den:raise AssertionError('normalized weight margin')
        min_lower=min(min_lower,F(N*s,den))
        params=safe(ast.parse(row['parameters'],mode='eval'))
        if not (len(params)==2 and params[0]=='basis'):
            alpha,beta,b,f=params
            for x in (alpha,beta,b,f):
                if abs(x[0])+abs(x[1])>64:raise AssertionError('parameter upper bound')
            for x in (alpha,f):
                if max(abs(x[0]),abs(x[1]))<F(1,64):raise AssertionError('parameter reciprocal bound')
            if z[0][1] or z[0][0]**2>s:raise AssertionError('normalized scaling bound')
        norms.append(s);columns.append(features(z))
    indices=basis['selected_indices_zero_based'];P=inv['matrix']
    if len(indices)!=81 or any(len(row)!=81 for row in P):raise AssertionError('basis dimensions')
    if any(sum(abs(x) for x in row)>=Q*(1<<10) for row in P):raise AssertionError('approx inverse norm')
    count=0
    for k in range(81):
        for j,idx in enumerate(indices):
            numer=sum(P[k][i]*columns[idx][i] for i in range(81))
            if k==j:numer-=Q*norms[idx]
            if 162*abs(numer)>=Q*norms[idx]:raise AssertionError(('inverse residual bound',k,j))
            count+=1
    print(json.dumps({'atoms':len(atoms),'all_normalized_weights_gt_2^-18':True,
                      'smallest_normalized_weight_float_for_display':float(min_lower),
                      'exact_parameter_bound':'C=64',
                      'approx_inverse_infinity_norm_lt':'2^10',
                      'each_exact_inverse_residual_entry_lt':'1/162',
                      'residual_entries_checked':count,
                      'therefore_exact_basis_inverse_infinity_norm_lt':'2^11',
                      'limits':'norm and weight bounds only; radius follows from stated analytic inequalities'},indent=2))


if __name__=='__main__':main()
