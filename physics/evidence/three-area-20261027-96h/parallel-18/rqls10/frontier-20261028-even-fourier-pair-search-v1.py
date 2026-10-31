#!/usr/bin/env python3
"""Bounded numerical discovery ONLY: K and K∘F_n both Hadamard.
T is normalized to (r,r). No failed optimization is an obstruction.
"""
import datetime,hashlib,json,time
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
start=datetime.datetime.now().astimezone().isoformat();rng=np.random.default_rng(137137)
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'start':start,'seed':137137,'steps':2500,'bounds':{'4':8,'6':8,'8':32,'10':8},'orders':{}}
t0=time.monotonic()
for n,count in [(4,8),(6,8),(8,32),(10,8)]:
 F=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n);I=np.eye(n)
 best=float('inf');besttheta=None;bestseed=None
 for restart in range(count):
  theta=rng.uniform(-np.pi,np.pi,(n,n));theta[0,:]=0;theta[:,0]=0
  m=np.zeros_like(theta);v=np.zeros_like(theta)
  for step in range(1,2501):
   K=np.exp(1j*theta);M=K*F
   E=K.conj().T@K/n-I;G=M.conj().T@M/n-I
   val=float(np.sum(abs(E)**2)+np.sum(abs(G)**2))
   if val<best:best,besttheta,bestseed=val,theta.copy(),(restart,step)
   grad=(4/n)*(np.imag(np.conj(K)*(K@E))+np.imag(np.conj(M)*(M@G)))
   grad[0,:]=0;grad[:,0]=0
   m=.9*m+.1*grad;v=.999*v+.001*grad*grad
   rate=.04 if step<2000 else .01
   theta-=rate*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8)
   if val<1e-20:break
 K=np.exp(1j*besttheta);M=K*F
 max1=float(np.max(abs(K.conj().T@K/n-I)));max2=float(np.max(abs(M.conj().T@M/n-I)))
 np.save(P/f'frontier-20261028-even-fourier-n{n}-best-v1.npy',besttheta)
 result['orders'][str(n)]={'best_objective':best,'best_restart_step':bestseed,'max_K_gram_error':max1,'max_twisted_gram_error':max2}
 print('n',n,result['orders'][str(n)],flush=True)
result['elapsed_seconds']=time.monotonic()-t0;result['finish']=datetime.datetime.now().astimezone().isoformat()
(P/'frontier-20261028-even-fourier-pair-search-v1.json').write_text(json.dumps(result,indent=2)+'\n')
print('complete',result['elapsed_seconds'],flush=True)
