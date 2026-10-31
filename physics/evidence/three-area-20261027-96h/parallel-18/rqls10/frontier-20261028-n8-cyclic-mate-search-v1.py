#!/usr/bin/env python3
"""Bounded ACTUAL-vector search for order8 QLS with cyclic resolution.

Uses 24 simultaneous polar projections, source Example2.4 and random starts.
Numerical discovery only; absence or finite residual proves nothing.
"""
import datetime,hashlib,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;checker=P/'frontier-20261028-source8-covariance-check-v1.py';raw=checker.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='504e7521ec91d932f8f29adf3711ad76c8a85d5d3d184a4779903c7eb2c8ec9f'
# Parse/check exact source in memory; do not write its pinned results again.
ns={'__file__':str(checker)};exec(compile(raw.decode().split('\nobj={',1)[0],str(checker),'exec'),ns)
V=ns['V'];z=np.exp(2j*np.pi/8);source=np.array([[sum(v[k]*z**k for k in range(4))/2 for v in V[r][c]]for r in range(8)for c in range(8)]).T
n=8;blocks=[]
for r in range(n):blocks.append([r*n+c for c in range(n)])
for c in range(n):blocks.append([r*n+c for r in range(n)])
for a in range(n):blocks.append([r*n+c for r in range(n)for c in range(n)if (r-c)%n==a])
assert len(blocks)==24 and all(len(q)==n for q in blocks)
def score(v):
 gram=v.conj().T@v;err=max(float(np.max(abs(gram[np.ix_(b,b)]-np.eye(n))))for b in blocks)
 np.fill_diagonal(gram,0);return err,float(np.max(abs(gram)))
def polar(a):u,_,v=np.linalg.svd(a,full_matrices=False);return u@v
rng=np.random.default_rng(2608);start=time.monotonic();best=1e9;bestv=None;where=None;records=[]
for seed in range(24):
 if seed<8:
  v=source+(.03+.05*seed)*(rng.normal(size=source.shape)+1j*rng.normal(size=source.shape))
 else:v=rng.normal(size=(n,n*n))+1j*rng.normal(size=(n,n*n))
 v/=np.linalg.norm(v,axis=0)
 for step in range(1,1001):
  av=np.zeros_like(v)
  for block in blocks:av[:,block]+=polar(v[:,block])
  v=av/np.linalg.norm(av,axis=0)
  if step%20==0 or step==1:
   err,mx=score(v)
   if err<best:best,bestv,where=err,v.copy(),[seed,step]
   if err<1e-10 and mx<1-1e-8:break
 err,mx=score(v);records.append({'seed':seed,'steps':step,'block_error':err,'max_pair_overlap':mx})
 if best<1e-10 and score(bestv)[1]<1-1e-8:break
np.save(P/'frontier-20261028-n8-cyclic-mate-best-v1.npy',bestv)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'source_parser_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'seed':2608,'restarts':24,'step_limit':1000,'elapsed_seconds':round(time.monotonic()-start,6),
 'best_seed_step':where,'best_block_error':best,'best_max_pair_overlap':score(bestv)[1],
 'results':records,'warning':'FLOATING discovery only; a candidate needs independent exact or rigorous verification; failure excludes nothing'}
(P/'frontier-20261028-n8-cyclic-mate-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items()if k!='results'},indent=2))
