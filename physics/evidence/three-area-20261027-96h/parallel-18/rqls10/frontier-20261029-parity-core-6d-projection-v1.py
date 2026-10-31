#!/usr/bin/env python3
"""Bounded numerical 6D orthogonal-edge-coloring probe for the 4D parity core.
Floating output is NOT a witness. Exact original-vector/cell replay is required.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;src=P/'frontier-20261029-pauli60-tripartite-core-independent-v1.json';raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ac84ee76884f766f04d18c54915bb2beb317591b50b61a5c882084a0c65e41bd';data=json.loads(raw)
E=[];planes=[]
for record in data['cross_group_incidence']:
 a,b=record['groups'];M=record['shared_H4_ray_matrix']
 for i in range(5):
  for j in range(5):
   if M[i][j]==0:E.append((5*a+i,5*b+j))
assert len(E)==45 and len(set(E))==45
blocks=np.array([[k for k,(a,b) in enumerate(E)if v in(a,b)]for v in range(15)]);assert blocks.shape==(15,6)
def project(X):
 for ids in blocks:
  u,s,vh=np.linalg.svd(X[ids],full_matrices=False);X[ids]=u@vh
 return X
def metrics(X):
 err=max(float(np.max(np.abs(X[ids]@X[ids].conj().T-np.eye(6))))for ids in blocks)
 G=np.abs(X@X.conj().T);np.fill_diagonal(G,0);return err,float(G.max())
rng=np.random.default_rng(60045);runs=[]
for seed in range(20):
 X=rng.normal(size=(45,6))+1j*rng.normal(size=(45,6));best=(1e9,1e9,0);bestX=None;begin=time.monotonic()
 for it in range(1,4001):
  X=project(X)
  if it%50==0:
   e,m=metrics(X)
   if e<best[0]:best=(e,m,it);bestX=X.copy()
   if e<1e-10 and m<1-1e-8:break
 runs.append({'seed':seed,'best_error':best[0],'max_ray_overlap':best[1],'best_iteration':best[2],
  'seconds':round(time.monotonic()-begin,3),'vectors_real':bestX.real.tolist(),'vectors_imag':bestX.imag.tolist()})
 print('seed',seed,'best error',best[0],'max overlap',best[1],'iteration',best[2],flush=True)
 if best[0]<1e-10 and best[1]<1-1e-8:break
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'status':'FLOATING_HEURISTIC_ONLY','edges':E,'blocks':blocks.tolist(),
 'runs':runs,'scope':'Only 6D complement of the one 4D core, no 25-cell extension; finite residual is not a certificate.'}
(P/'frontier-20261029-parity-core-6d-projection-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print('finished',obj['clock_finish'])
