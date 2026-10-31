#!/usr/bin/env python3
"""Exploratory floating alternating projections, never a proof or a witness.

Searches H and F_n elementwise H both complex Hadamard without family
restrictions. A small residual would need exact reconstruction and an
independent original-vector replay; a positive residual is not a no-go.
"""
import datetime,hashlib,json,sys,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
cases=[]
for n in (8,10):
 t=np.arange(n);F=np.exp((2j*np.pi/n)*np.outer(t,t));I=np.eye(n)
 def phase(M):
  a=np.abs(M);return M/np.where(a>1e-14,a,1)
 def U(M):
  u,s,vh=np.linalg.svd(M,full_matrices=False);return np.sqrt(n)*(u@vh)
 def metrics(M):
  U0=phase(M);T=F*U0
  return (float(np.max(np.abs(U0.conj().T@U0/n-I))),float(np.max(np.abs(T.conj().T@T/n-I))))
 for seed in (0,1,2):
  rng=np.random.default_rng(20261028+100*n+seed);M=np.exp(2j*np.pi*rng.random((n,n)));best=1e9;bestM=None;bestit=0;begin=time.monotonic()
  for it in range(1,3001):
   M=phase(M);M=U(M);M=np.conj(F)*U(F*M)
   if it%10==0:
    q=metrics(M);score=max(q)
    if score<best:best=score;bestM=phase(M);bestit=it
    if score<1e-10:break
  cases.append({'n':n,'seed':20261028+100*n+seed,'iterations':it,'best_iteration':bestit,'best_max_offdiagonal':best,
   'two_gram_errors':metrics(bestM),'seconds':round(time.monotonic()-begin,3),
   'phase_matrix_radians':np.angle(bestM).tolist()})
  print(n,seed,it,best,flush=True)
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'numpy_version':np.__version__,
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'status':'FLOATING_HEURISTIC_ONLY','cases':cases,
 'boundary':'A finite-precision iterate is not an exact Hadamard, transversal, proof of impossibility, or unrestricted QLS10 result.'}
(P/'frontier-20261028-even-fourier-alternating-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
