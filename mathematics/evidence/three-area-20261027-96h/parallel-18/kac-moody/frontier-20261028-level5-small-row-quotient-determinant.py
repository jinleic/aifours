#!/usr/bin/env python3
"""Full exact univariate minor of a fixed-small-row quotient pencil."""
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
    ap=argparse.ArgumentParser()
    for n in ('a','b','r'):ap.add_argument('--'+n,type=int,required=True)
    args=ap.parse_args();a,b,r=args.a,args.b,args.r
    P=json.loads((ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-pencil-v1.json').read_text())
    out=ROOT/f'frontier-20261028-level5-r{r}-{a}{b}-smallrow-determinant-v1.json'
    if out.exists():raise FileExistsError(out)
    if P['status']=='ZERO_HORIZONTAL_KERNEL':
        out.write_text(json.dumps({'degree':P['degree'],'r':r,'status':'ZERO_HORIZONTAL_KERNEL'},indent=2)+'\n');print('DONE ZERO_HORIZONTAL_KERNEL',out.name);return
    assert P['status']=='BASELINE_MINOR_ONLY_NOT_GLOBAL'
    rows=[[[Q(q) for q in e] for e in row] for row in P['matrix']];n=len(rows)
    scales=[math.lcm(*(q.denominator for e in row for q in e)) for row in rows]
    data=[[[int(q*scales[i]) for q in e] for e in row] for i,row in enumerate(rows)];scale=math.prod(scales)
    values=[Q(det.bareiss([[e[0]+y*e[1] for e in row] for row in data]),scale) for y in range(n+1)]
    work=values[:];difference=[]
    while work:difference.append(work[0]);work=[b-a for a,b in zip(work,work[1:])]
    coefficients=[Q(0)]*(n+1)
    for i,q in enumerate(difference):
        for j,c in enumerate(det.falling_binomial(i)):coefficients[j]+=q*c
    for y,v in enumerate(values):assert sum(q*y**j for j,q in enumerate(coefficients))==v
    nonzero=[q for q in coefficients if q];signs=sorted({1 if q>0 else -1 for q in nonzero})
    result={'degree':P['degree'],'r':r,'matrix_size':n,'variable':'y=s-4','total_degree_bound':n,
            'all_grid_values_reconstructed':True,'grid_evaluations':n+1,'determinant_coefficients':[str(q) for q in coefficients],
            'nonzero_coefficient_count':len(nonzero),'signs':signs,'constant_coefficient':str(coefficients[0]),
            'status':'ONE_SIGN_ALL_S_GE_4' if len(signs)==1 and coefficients[0] else 'MIXED_OR_ZERO_CONSTANT',
            's4_extra_154star_seed_not_built':'selected-type exclusion required',
            'not_formal_or_external_review':True}
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('DONE r',r,'degree',P['degree'],'source',n,'nonzero terms',len(nonzero),'signs',signs,result['status'],out.name,flush=True)

if __name__=='__main__':main()
