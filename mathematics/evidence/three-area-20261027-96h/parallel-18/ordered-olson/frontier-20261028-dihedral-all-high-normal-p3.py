#!/usr/bin/env python3
"""Exercise the p=3 empty-extra boundary of the written normal forms."""
import importlib.util
import json
import random

spec=importlib.util.spec_from_file_location('normal','frontier-20261028-dihedral-all-high-normal-checker.py')
normal=importlib.util.module_from_spec(spec)
spec.loader.exec_module(normal)
rng=random.Random(2026102812)
branches={}
for kind in ('one-five','two-threes'):
    for trial in range(30):
        word=normal.family(rng,3,kind,trial)
        k=normal.check(word,3,kind)
        key=f'{kind}/k{k}'
        branches[key]=branches.get(key,0)+1
result={'result':'PASS_P3_EMPTY_EXTRA_NORMAL_LAYOUTS','p':3,'actual_words_and_selectors':sum(branches.values()),
        'branches':branches,'scope':'same-checker p=3 extension, not independent review'}
with open('frontier-20261028-dihedral-all-high-normal-p3-results.json','x',encoding='utf-8') as out:
    json.dump(result,out,sort_keys=True,indent=2)
    out.write('\n')
print(json.dumps(result,sort_keys=True))
