#!/usr/bin/env python3
"""Exact parameter and positivity-bound checks for the explicit SN2 patch."""
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
helper=runpy.run_path(str(HERE/'frontier-20261028-grid-generic-open-basis-check.py'))
safe=helper['safe']


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cert=json.loads(CERT.read_text());source=json.loads(SOURCE.read_text());basis=json.loads(BASIS.read_text())
    atoms=cert['atoms'];orig=source['active_atoms'];D=int(cert['common_denominator']);C=1<<160
    if len(atoms)!=len(orig):raise AssertionError('atom mismatch')
    if basis['input_decomposition_sha256']!=digest(CERT) or basis['input_chart_parameters_sha256']!=digest(SOURCE):
        raise AssertionError('basis input hash mismatch')
    if basis['feature_dimension']!=81 or not basis['determinant_mod_prime']:
        raise AssertionError('missing nonzero determinant')
    count=0;max_scale_bits=0;max_param_ceiling=0;min_alpha=F(1);min_f=F(1)
    trace=0
    for entry,row in zip(atoms,orig):
        weight=int(entry['weight_numerator']);z=[(int(x),int(y)) for x,y in entry['coefficients']]
        if weight<=0:raise AssertionError('nonpositive')
        trace+=weight*sum(x*x+y*y for x,y in z)
        params=safe(ast.parse(row['parameters'],mode='eval'))
        if len(params)==2 and params[0]=='basis':continue
        alpha,beta,b,f=params
        for name,x in (('alpha',alpha),('beta',beta),('b',b),('f',f)):
            upper=abs(x[0])+abs(x[1])
            if upper>C:raise AssertionError(('upper',name))
            max_param_ceiling=max(max_param_ceiling,(upper.numerator+upper.denominator-1)//upper.denominator)
        for name,x in (('alpha',alpha),('f',f)):
            lower=max(abs(x[0]),abs(x[1]))
            if not lower or lower<F(1,C):raise AssertionError(('inverse',name))
            if name=='alpha':min_alpha=min(min_alpha,lower)
            else:min_f=min(min_f,lower)
        scalar=z[0][0]
        if z[0][1] or scalar<=0 or scalar>C:raise AssertionError('scale bound')
        max_scale_bits=max(max_scale_bits,scalar.bit_length());count+=1
    if trace!=21*D:raise AssertionError('coefficient trace mismatch')
    if D.bit_length()>8534:raise AssertionError('denominator bound')
    print(json.dumps({'chart_atoms_checked':count,'basis_atoms':len(atoms)-count,
                      'common_denominator_bits':D.bit_length(),
                      'max_integer_scale_bits':max_scale_bits,
                      'max_parameter_l1_ceiling':max_param_ceiling,
                      'min_alpha_component_lower_bound':str(min_alpha),
                      'min_f_component_lower_bound':str(min_f),
                      'C_bound':'2^160','base_weight_sum_norm2':'21',
                      'stated_radius':'2^-250000','verified_parameter_bounds':True},indent=2))


if __name__=='__main__':main()
