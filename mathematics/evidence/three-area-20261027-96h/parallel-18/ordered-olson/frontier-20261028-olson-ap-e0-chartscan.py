#!/usr/bin/env python3
"""Independent erasable-gap chart scan of one frozen AP e0 word."""
import argparse
import hashlib
import importlib.util
import json

spec=importlib.util.spec_from_file_location('chart','frontier-20261028-olson-kappa1-ip-chart-audit.py')
chart=importlib.util.module_from_spec(spec)
spec.loader.exec_module(chart)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_AP_ODD_RUN_E0_CANDIDATES':raise ValueError('INPUT_KIND')
    case=next(c for c in data['cases'] if c['p']==args.p)
    word=tuple(tuple(v) for v in case['word'])
    if len(word)!=4*args.p-1 or len({x for x,e in word if not e})!=1:
        raise ValueError('INPUT_SHAPE_OR_SIX_BASE')
    result=chart.scan(word,args.p)
    out={'result':'AP_E0_ERASABLE_CHART_SCAN_COMPLETED','p':args.p,
         'input_sha256':hashlib.sha256(raw).hexdigest(),'scan':result,
         'scope':'one fixed word, reused chart code; grammar correctness/OLD verdict not reviewed'}
    with open(args.output,'x',encoding='utf-8') as dest:
        json.dump(out,dest,sort_keys=True,indent=2);dest.write('\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
