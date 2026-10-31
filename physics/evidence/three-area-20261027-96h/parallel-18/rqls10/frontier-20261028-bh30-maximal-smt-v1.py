#!/usr/bin/env python3
"""Exact full BH(10,30) Fourier-product 100-ray+transversal SMT.

Reuse the pinned generic q30 encoding, adding the equivalent 405 character
exclusions for every pair of columns. This is stricter than the generic T
search and targets maximal cardinality. Unknown is NOT exclusion.
"""
import hashlib
from pathlib import Path
base=Path(__file__).resolve().parent/'frontier-20261028-bh30-transversal-smt-v1.py'
raw=base.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8682f8b0363e1ed6e36dba31a5f1c59b50c4ca9b7ed498f4356b52f6ae7096e3'
s=raw.decode()
s=s.replace('frontier-20261028-bh30-transversal-smt-v1.json','frontier-20261028-bh30-maximal-smt-v1.json')
s=s.replace('S.set(timeout=120000,random_seed=9)','S.set(timeout=120000,random_seed=12)')
needle="print('constraints',len(S.assertions()),'exact root components',len(root),flush=True)"
assert s.count(needle)==1
extra='''# With first coordinate dephased, two product cells are parallel iff two
# K columns differ by the character zeta10^(k*t), k=1,...,9; k=0 is
# already excluded by column orthogonality. This is exactly 100 rays.
for r in range(10):
 for s in range(r+1,10):
  for k in range(1,10):
   S.add(z3.Or(*[((X[t][s]-X[t][r]-3*k*t)%30)!=0 for t in range(1,10)]))
'''
s=s.replace(needle,extra+needle)
s=s.replace("'method':'exact Z3 over Q(zeta6) tensor Q(zeta5); no rank/ray assumption'", "'method':'exact Z3 over Q(zeta6) tensor Q(zeta5); plus 405 character exclusions for 100 rays'")
s=s.replace("'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),", "'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'base_sha256':'8682f8b0363e1ed6e36dba31a5f1c59b50c4ca9b7ed498f4356b52f6ae7096e3',")
s=s.replace("obj['original_vector_check']={'row_grams':rowchecks", "assert not dups\n obj['original_vector_check']={'row_grams':rowchecks")
exec(compile(s,str(base),'exec'),globals())
