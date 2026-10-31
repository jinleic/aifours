#!/usr/bin/env python3
"""q30 maximal Fourier-product search with proved support-cardinality lemmas.

For two same-parity transversal rows the five w_u=z_u+z_{u+5} obey
sum w_u=sum zeta5^(ku)w_u=0; nonzero support has at least3. The 20 added
lemmas are logical consequences, not assumptions. Unknown is not no-go.
"""
import hashlib
from pathlib import Path
base=Path(__file__).resolve().parent/'frontier-20261028-bh30-transversal-smt-v1.py'
raw=base.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8682f8b0363e1ed6e36dba31a5f1c59b50c4ca9b7ed498f4356b52f6ae7096e3'
s=raw.decode().replace('frontier-20261028-bh30-transversal-smt-v1.json','frontier-20261028-bh30-vandermonde-smt-v1.json')
s=s.replace('S.set(timeout=120000,random_seed=9)','S.set(timeout=120000,random_seed=17)')
needle="print('constraints',len(S.assertions()),'exact root components',len(root),flush=True)"
assert s.count(needle)==1
extra='''# Maximality: for dephased K, no two columns differ by a nontrivial
# zeta10 character. The k=0 case already follows from orthogonality.
for r in range(10):
 for s in range(r+1,10):
  for k in range(1,10):
   S.add(z3.Or(*[((X[t][s]-X[t][r]-3*k*t)%30)!=0 for t in range(1,10)]))
# Proved Vandermonde support: the number of antipodal coordinate pairs
# is at most2 or exactly5; 3,4 would leave nonzero support 2,1.
for r in range(10):
 for s in range(r+1,10):
  if (s-r)%2==0:
   n=z3.Sum(*[z3.If(((X[u+5][s]-X[u+5][r]-X[u][s]+X[u][r])%30)==15,1,0) for u in range(5)])
   S.add(z3.Or(n<=2,n==5))
'''
s=s.replace(needle,extra+needle)
s=s.replace("'method':'exact Z3 over Q(zeta6) tensor Q(zeta5); no rank/ray assumption'", "'method':'exact Z3 q30 maximal target plus 20 entailed Vandermonde support lemmas'")
s=s.replace("'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),", "'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'base_sha256':'8682f8b0363e1ed6e36dba31a5f1c59b50c4ca9b7ed498f4356b52f6ae7096e3',")
s=s.replace("obj['original_vector_check']={'row_grams':rowchecks", "assert not dups\n obj['original_vector_check']={'row_grams':rowchecks")
exec(compile(s,str(base),'exec'),globals())
