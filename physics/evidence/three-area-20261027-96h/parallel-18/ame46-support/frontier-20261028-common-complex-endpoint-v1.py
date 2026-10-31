#!/usr/bin/env python3
"""Directly materialize/check both equal-angle four-party endpoints."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    obj=importlib.util.module_from_spec(spec);spec.loader.exec_module(obj)
    return obj


def main():
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('dense',type=Path)
    p.add_argument('phase',type=Path);p.add_argument('search_receipt',type=Path);p.add_argument('out',type=Path);a=p.parse_args()
    dense=module('dense',a.dense);phase=module('phase',a.phase)
    source,table_sha=dense.load_table(a.table)
    original={k:(x,y,0,0) for k,(x,y) in source.items()}
    endpoints={}
    for name,z in (('real',0),('imaginary',1)):
        state=original
        for axis in range(4): state=phase.apply_gate(state,axis,1,2,z)
        check=phase.verify_six(state,4)
        if len(state)!=60: raise ValueError(f'{name} endpoint support {len(state)}')
        endpoints[name]=state
        print(name,'support',len(state),'intersection with source',len(set(state)&set(original)),
              'normalization denominator',check['denominator'],'six marginals',check['marginals'])
    prior=json.loads(a.search_receipt.read_text())
    recorded={tuple(item[:4]):tuple(item[4:]) for item in prior['best_coefficients_Qsqrt2_i']}
    if recorded!=endpoints['real']: raise ValueError('real endpoint differs from search receipt')
    result={'table_sha256':table_sha,
            'real_support':60,'imaginary_support':60,'input_support':len(original),
            'intersection_input_real':len(set(original)&set(endpoints['real'])),
            'intersection_input_imaginary':len(set(original)&set(endpoints['imaginary'])),
            'intersection_real_imaginary':len(set(endpoints['real'])&set(endpoints['imaginary'])),
            'real_exact_check':phase.verify_six(endpoints['real'],4),
            'imaginary_exact_check':phase.verify_six(endpoints['imaginary'],4),
            'real_matches_search_receipt':True,
            'imaginary_coefficients_Qsqrt2_i':[[*k,*v] for k,v in sorted(endpoints['imaginary'].items())],
            'scope':'Equal-support transformations within the same LU orbit; no lower-support or novelty claim.'}
    with a.out.open('x',encoding='utf-8') as out:json.dump(result,out,indent=2);out.write('\n')
    json.dump({k:v for k,v in result.items() if k!='imaginary_coefficients_Qsqrt2_i'},sys.stdout,indent=2);print()


if __name__=='__main__':main()
