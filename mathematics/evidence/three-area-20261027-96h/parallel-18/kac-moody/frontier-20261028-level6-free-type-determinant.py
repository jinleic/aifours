#!/usr/bin/env python3
"""Complete exact total-degree interpolation of a level-six affine minor."""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('helpers',ROOT/'frontier-20261028-level5-35-alternate-minor-search.py')
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--a',type=int,required=True);ap.add_argument('--b',type=int,required=True);args=ap.parse_args()
    a,b=args.a,args.b
    P=json.loads((ROOT/f'frontier-20261028-level6-free-{a}{b}-pencil-v1.json').read_text())
    assert P['status']=='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    out=ROOT/f'frontier-20261028-level6-free-{a}{b}-determinant-v1.json'
    if out.exists():raise FileExistsError(out)
    data,scale=h.int_rows([[[Q(x) for x in e] for e in row] for row in P['matrix']]);n=len(data)
    coeff=h.polynomial(data,scale,{})
    signs=sorted({1 if x>0 else -1 for x in coeff.values()})
    result={'degree':P['degree'],'matrix_size':n,'variables':'x=r-6,y=s-6','total_degree_bound':n,
            'grid_evaluations':(n+1)*(n+2)//2,'all_grid_values_reconstructed':True,
            'determinant_coefficients':[{'x_power':i,'y_power':j,'coefficient':str(q)} for (i,j),q in sorted(coeff.items())],
            'signs':signs,'constant_coefficient':str(coeff.get((0,0),0)),
            'status':'ONE_SIGN_ALL_ORTHANT' if len(signs)==1 and coeff.get((0,0),0) else 'MIXED_OR_ZERO_CONSTANT',
            'scope':'entire free-Levi source; actual r,s>=6 source identification must be proved separately',
            'not_formal_or_external_model_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE level6',P['degree'],'size',n,'terms',len(coeff),'signs',signs,result['status'],out.name,flush=True)

if __name__=='__main__':main()
