#!/usr/bin/env python3
"""Exact IVT brackets for real zeros of ONE selected mixed minor.

A minor zero is not a kernel of the full map or an integer witness. No root
uniqueness or maximality conclusion is drawn.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent


def main():
    inp=ROOT/'frontier-20261028-level6-free-22-determinant-v1.json';raw=inp.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='874380d72b439e04819dfaf29df900eb1a4d66ae18e53bc3287b2d05b162bfa8'
    P=json.loads(raw);terms=P['determinant_coefficients']
    def val(x,y):return sum((Q(e['coefficient'])*x**e['x_power']*y**e['y_power'] for e in terms),Q(0))
    xlow,xhigh=Q(11),Q(23,2);ylow,yhigh=Q(41),Q(83,2)
    vals={'P(11,0)':val(xlow,0),'P(23/2,0)':val(xhigh,0),'P(0,41)':val(0,ylow),'P(0,83/2)':val(0,yhigh)}
    assert vals['P(11,0)']<0<vals['P(23/2,0)'] and vals['P(0,41)']<0<vals['P(0,83/2)']
    result={'degree':P['degree'],'source_polynomial_sha256':hashlib.sha256(raw).hexdigest(),
            'exact_values':{k:str(v) for k,v in vals.items()},
            'real_positive_zero_brackets':{'x_axis':['11','23/2'],'y_axis':['41','83/2']},
            'status':'EXACT_OPPOSITE_ENDPOINT_SIGNS_BOTH_AXES',
            'scope':'IVT yields >=1 real zero of this selected minor in each open interval; no uniqueness, full-map kernel, integer witness or global impossibility'}
    out=ROOT/'frontier-20261028-level6-226-minor-root-brackets-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact IVT signs: selected-minor real roots x in (11,23/2), y in (41,83/2);',out.name)

if __name__=='__main__':main()
