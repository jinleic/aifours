#!/usr/bin/env python3
"""Bounded p=11 search for two-sign type-III no-low-triangle prefixes."""
import importlib.util
import json

spec=importlib.util.spec_from_file_location('search','frontier-20261028-dihedral-prefix-obstruction-search.py')
search=importlib.util.module_from_spec(spec)
spec.loader.exec_module(search)
p=11
m,n=2*p-3,p-1
prefixes,nodes=search.find_prefix(p,m,n)
result={'p':p,'m':m,'n':n,'visited_nodes':nodes,'prefixes':prefixes,
        'scope':'bounded prefix search only; any no-witness proof requires independent source review'}
if prefixes is not None:
    word=search.materialize(p,m,n,prefixes)
    result['word']=word
    result['low_pair_edges']=search.verify(p,m,n,prefixes,word)
with open('frontier-20261028-dihedral-prefix-type3-p11-results.json','x',encoding='utf-8') as out:
    json.dump(result,out,sort_keys=True,indent=2)
    out.write('\n')
print(json.dumps(result,sort_keys=True))
