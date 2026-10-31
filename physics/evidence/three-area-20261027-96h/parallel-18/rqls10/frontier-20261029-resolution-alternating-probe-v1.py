#!/usr/bin/env python3
"""Bounded 30-context alternating-projection experiment, non-certifying.

A near-zero residual and numerically distinct rays are only a discovery lead;
full exact vectors, norm/Gram and ray-inequality replay remain mandatory.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent;source=P/'frontier-20261028-exact-switch-grow-result-v1.json';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2023d098dc9c81b437b698601ed8709161794b7434934f83abc2f4219a6dcb6e'
w=json.loads(raw)['partial_witness'];labels=w['labels'];V=np.array(w['array'],float).reshape(100,10)/w['denominator']
rows=np.array([[10*r+c for c in range(10)]for r in range(10)]);cols=np.array([[10*r+c for r in range(10)]for c in range(10)]);labs=np.array([[10*r+c for r in range(10)for c in range(10)if labels[r][c]==t]for t in range(10)]);groups=(rows,cols,labs)
def proj(X):
 for group in groups:
  for ids in group:
   U,s,Vh=np.linalg.svd(X[ids],full_matrices=False);X[ids]=U@Vh
 return X
def metrics(X):
 G=X@X.T;err=max(float(np.max(np.abs(X[ids]@X[ids].T-np.eye(10))))for ids in np.concatenate(groups));rem=set(range(100));classes=[]
 while rem:
  i=min(rem);q={j for j in rem if abs(G[i,j])>1-1e-8};classes.append(len(q));rem-=q
 return err,len(classes),sorted(classes)
results=[]
for seed in range(12):
 rng=np.random.default_rng(3910+seed);amp=.4+.05*seed;X=V+amp*rng.normal(size=V.shape);best=None;bestX=None;begin=time.monotonic()
 for it in range(1,5001):
  X=proj(X)
  if it%100==0:
   err,count,sizes=metrics(X)
   if best is None or err<best[0]:best=(err,count,sizes,it);bestX=X.copy()
   if err<1e-10:break
 results.append({'seed':3910+seed,'amplitude':amp,'best_error':best[0],'numerical_ray_classes':best[1],'cluster_sizes':best[2],
  'best_iteration':best[3],'elapsed_seconds':round(time.monotonic()-begin,3),'matrix':bestX.tolist()})
 print('seed',seed,'best',best[:2],'iteration',best[3],flush=True)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seed_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'numpy':np.__version__,'status':'FLOATING_HEURISTIC_ONLY',
 'results':results,'scope':'A numerical matrix is not an exact 1RQLS witness; residuals and cluster counts cannot prove existence or impossibility.'}
(P/'frontier-20261029-resolution-alternating-probe-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print('finished',obj['clock_finish'])
