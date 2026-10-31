#!/usr/bin/env python3
"""Independent symbolic differentiation replay of singular points/tangents."""
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helper',ROOT/'frontier-review-f18-ph7-independent-check.py')
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper);S=helper.S


def main():
    R=json.loads((ROOT/'frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json').read_text())
    C=json.loads((ROOT/'frontier-20261028-level6-226-curve-singular-points-v1.json').read_text())
    assert C['status']=='THREE_EXACT_RATIONAL_AFFINE_SINGULAR_POINTS';x,y=S.symbols('x y')
    f=sum(S.Integer(t['coefficient'])*x**t['x_power']*y**t['y_power'] for t in R['R_coefficients'])
    for point in C['points']:
        a,b,m=point['x'],point['y'],point['multiplicity']
        for d in range(m):
            for i in range(d+1):assert S.diff(f,x,i,y,d-i).subs({x:a,y:b})==0
        got=[S.diff(f,x,m-j,y,j).subs({x:a,y:b})/(S.factorial(m-j)*S.factorial(j)) for j in range(m+1)]
        assert [str(q) for q in got]==point['tangent_U_power_descending_coefficients'] and any(got)
    assert 2382515**2-4*221760*229152==int(C['node_quadratic_discriminant'])!=0
    t=S.symbols('t');q=S.Poly(8278*t**4+78878*t**3-383037*t**2-189922*t-11447,t)
    assert S.gcd(q,q.diff()).degree()==0
    out=ROOT/'frontier-20261028-level6-226-curve-singular-points-independent-replay-v1.json'
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps({'checked_points':[[p['x'],p['y'],p['multiplicity']] for p in C['points']],
                               'all_partial_derivatives_and_tangent_cones_match':True,
                               'node_discriminant_nonzero':True,'quartic_tangent_squarefree':True,
                               'status':'PASS_THREE_RATIONAL_SINGULARITIES_AND_TANGENTS',
                               'scope':'no normalized-genus, Faltings, physical integer kernel or novelty claim'},indent=2)+'\n')
    print('PASS exact symbolic derivative/tangent replay for 3 rational singular points;',out.name)

if __name__=='__main__':main()
