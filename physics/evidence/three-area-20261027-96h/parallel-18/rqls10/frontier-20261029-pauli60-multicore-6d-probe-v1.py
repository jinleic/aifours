#!/usr/bin/env python3
"""Enumerate distinct 4D Pauli cores, numerically probe their 6D complements.
SAT each iteration is EXACT for 4D incidence; 6D residual is heuristic only.
"""
import datetime,hashlib,itertools,json,time
from pathlib import Path
import numpy as np,z3
P=Path(__file__).resolve().parent;source=P/'frontier-20261029-pauli60-tripartite-core-search-v1.py';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='40baaa1a7d25e32c12aa9117707422bb3159a697da1d076dcba9f36ec7cd3561'
g={'__file__':str(source)};exec(compile(raw.decode().split('t0=time.monotonic();res=S.check()',1)[0],str(source),'exec'),g)
S=g['S'];X=g['X'];C=g['C'];B=g['B'];S.set(timeout=4000,random_seed=37);rng=np.random.default_rng(606001);runs=[];reason='limit';start=time.monotonic()
for case in range(100):
 q=S.check()
 if q!=z3.sat:reason=str(q)+(':'+S.reason_unknown()if q==z3.unknown else '');break
 model=S.model();ids=[i for i,x in enumerate(X)if z3.is_true(model.eval(x))];colors=[model.eval(C[i]).as_long()for i in ids];assert len(ids)==15
 groups=[[j for j,k in enumerate(colors)if k==v]for v in range(3)];assert all(len(x)==5 for x in groups);bases=[set(B[i])for i in ids]
 edges=[]
 for a,b in ((0,1),(0,2),(1,2)):
  for i in range(5):
   for j in range(5):
    if not bases[groups[a][i]]&bases[groups[b][j]]:edges.append((5*a+i,5*b+j))
 blocks=np.array([[i for i,(u,v)in enumerate(edges)if q in(u,v)]for q in range(15)]);assert len(edges)==45 and blocks.shape==(15,6)
 best=(1e9,1e9,0,0);bestX=None
 for seed in range(2):
  Q=rng.normal(size=(45,6))+1j*rng.normal(size=(45,6))
  for it in range(1,1501):
   for block in blocks:
    u,s,vh=np.linalg.svd(Q[block],full_matrices=False);Q[block]=u@vh
   if it%100==0:
    error=max(float(np.max(np.abs(Q[block]@Q[block].conj().T-np.eye(6))))for block in blocks)
    if error<best[0]:
     G=np.abs(Q@Q.conj().T);np.fill_diagonal(G,0);best=(error,float(G.max()),seed,it);bestX=Q.copy()
    if error<1e-10 and best[1]<1-1e-8:break
  if best[0]<1e-10 and best[1]<1-1e-8:break
 runs.append({'case':case,'bases_1indexed':[[j+1 for j in B[i]]for i in ids],'colors':colors,'edges':edges,
  'best_error':best[0],'max_ray_overlap':best[1],'seed':best[2],'iteration':best[3],
  'vectors_real':bestX.real.tolist(),'vectors_imag':bestX.imag.tolist()})
 print('case',case,'error',best[0],'overlap',best[1],flush=True)
 if best[0]<1e-10 and best[1]<1-1e-8:reason='NUMERIC_CANDIDATE_NOT_CERTIFIED';break
 S.add(z3.Or(*[z3.Not(X[i])for i in ids]))
 if time.monotonic()-start>100:reason='wall_limit';break
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'setup_sha256':hashlib.sha256(raw).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'status':reason,'cases_tested':len(runs),'runs':runs,
 'boundary':'The sample is not exhaustive. Nonzero errors are not no-gos; a small residual is not a 6D or QLS10 witness.'}
(P/'frontier-20261029-pauli60-multicore-6d-probe-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print('finished',reason,len(runs),obj['clock_finish'])
