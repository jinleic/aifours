#!/usr/bin/env python3
"""Depth-first exact cut/omission scan for one frozen AP/e0 candidate."""
import argparse
import functools
import hashlib
import importlib.util
import json

spec=importlib.util.spec_from_file_location('gen','frontier-20261028-olson-kappa1-gen-parser.py')
gen=importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)


def scan(word,p):
    count=0
    @functools.lru_cache(None)
    def rec(seq):
        nonlocal count
        count+=1
        if gen.parse(seq,p) is not None:return True
        for i in range(len(seq)-1):
            a,b=seq[i],seq[i+1]
            if a[1]!=b[1]:continue
            if (a[0]==b[0] if a[1] else (a[0]+b[0])%p==0):
                reduced=seq[:i]+seq[i+2:]
                if not reduced or rec(reduced):return True
        return False
    unique=set()
    for cut in range(len(word)):
        v=word[cut:]+word[:cut]
        for i in range(len(v)):
            u=v[:i]+v[i+1:]
            if u in unique:continue
            unique.add(u)
            if rec(u):return {'outcome':'TREE_FOUND','cut':cut,'omit':i,
                              'unique_examined':len(unique),'reduced_states':count}
    return {'outcome':'NO_TREE_BY_REVERSE_REMOVAL','unique_examined':len(unique),'reduced_states':count}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('--p',type=int,required=True)
    parser.add_argument('--output',required=True);args=parser.parse_args()
    with open(args.input,'rb') as source:raw=source.read()
    data=json.loads(raw)
    if data['kind']!='UNPROMOTED_AP_ODD_RUN_E0_CANDIDATES':raise ValueError('INPUT_KIND')
    item=next(c for c in data['cases'] if c['p']==args.p)
    word=tuple(tuple(v) for v in item['word'])
    if len(word)!=4*args.p-1 or len({x for x,e in word if not e})!=1:
        raise ValueError('INPUT_SHAPE_OR_SIX_BASE')
    result={'result':'AP_E0_DFS_IP_SCAN_COMPLETED','p':args.p,'input_sha256':hashlib.sha256(raw).hexdigest(),
            'scan':scan(word,args.p),
            'scope':'one fixed word; reused GEN parser, grammar/OLD status unreviewed'}
    with open(args.output,'x',encoding='utf-8') as out:
        json.dump(result,out,sort_keys=True,indent=2);out.write('\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
