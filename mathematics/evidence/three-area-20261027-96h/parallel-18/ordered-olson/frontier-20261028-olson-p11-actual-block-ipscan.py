#!/usr/bin/env python3
"""Scan all cuts/omissions for one frozen p=11 actual-block candidate."""
import argparse
import hashlib
import importlib.util
import json

spec=importlib.util.spec_from_file_location('ip','frontier-20261028-olson-kappa1-independent-ip-audit.py')
ip=importlib.util.module_from_spec(spec)
spec.loader.exec_module(ip)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_P11_ACTUAL_BLOCK_CANDIDATE' or data['p']!=11:
        raise ValueError('wrong frozen candidate')
    word=tuple(tuple(t) for t in data['word'])
    if len(word)!=43 or any(e==0 and x!=5 for x,e in word):
        raise ValueError('wrong length or nonuniform rotation')
    result=ip.independent_scan(word,11)
    out={'result':'P11_ACTUAL_BLOCK_BFS_IP_SCAN_COMPLETED',
         'input_sha256':hashlib.sha256(raw).hexdigest(),'scan':result,
         'scope':'one fixed word, reused BFS code; OLD/full residual and grammar audit pending'}
    with open(args.output,'x',encoding='utf-8') as dest:
        json.dump(out,dest,sort_keys=True,indent=2);dest.write('\n')
    print(json.dumps(out,sort_keys=True))


if __name__=='__main__':
    main()
