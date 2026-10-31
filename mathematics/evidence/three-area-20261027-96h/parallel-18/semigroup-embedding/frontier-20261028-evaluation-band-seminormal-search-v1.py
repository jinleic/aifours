#!/usr/bin/env python3
"""Bounded exact search for seminormal failure in the known locally-regular T80."""
import importlib.util,random
from pathlib import Path
p=Path(__file__).with_name('frontier-20261028-local-band-base-rees-checker-v1.py')
spec=importlib.util.spec_from_file_location('source_check',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
T=mod.T;n=len(T);ids={v:i for i,v in enumerate(T)}
M=tuple(tuple(ids[mod.tm(a,b)] for b in T) for a in T)
def test(a,b,c,d):
 left=M[M[M[M[a][b]][c]][d]][a]
 right=M[M[M[M[M[M[a][b]][c]][a]][c]][d]][a]
 return left,right
rng=random.Random(176241);checked=0
for trial in range(500000):
 a,b,c,d=(rng.randrange(n) for _ in range(4));left,right=test(a,b,c,d);checked+=1
 if left!=right:
  print('COUNTEREXAMPLE checked=',checked,' Tsize=',n,' indices=',(a,b,c,d),' words=',(T[a],T[b],T[c],T[d]),' values=',(T[left],T[right]),sep='')
  break
else:print('NO_COUNTEREXAMPLE checked=',checked,' Tsize=',n,' seed=176241; not a universal claim',sep='')
