#!/usr/bin/env python3
"""Independent erasable-gap chart scan of frozen actual-block p11 word."""
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
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_P11_ACTUAL_BLOCK_CANDIDATE' or data['p']!=11:raise ValueError('INPUT_KIND')
    word=tuple(tuple(x) for x in data['word'])
    if len(word)!=43 or len({x for x,e in word if not e})!=1:raise ValueError('INPUT_SHAPE')
    report=chart.scan(word,11)
    result={'result':'P11_ACTUAL_BLOCK_CHART_SCAN_COMPLETED','input_sha256':hashlib.sha256(raw).hexdigest(),
            'scan':report,'scope':'one fixed word, reused chart; grammar normalization/OLD status pending review'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
