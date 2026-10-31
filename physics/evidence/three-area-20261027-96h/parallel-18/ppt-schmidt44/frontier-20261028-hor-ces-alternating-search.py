#!/usr/bin/env python3
"""Bounded FLOATING alternating local-filter search for CES projector overlap."""
from contextlib import redirect_stdout
from hashlib import sha256
import io,json,runpy,numpy as np
path='frontier-20261028-hor-crosshatch-coordinate-search.py'
expected='e5e5a9aa73ad414e36f7c5060a9ea0fa5c4fb3007600ed8ab5fe3599742bc49e'
assert sha256(open(path,'rb').read()).hexdigest()==expected
# Source vectors are the explicit additive H⊗Q/Pi source. This is not a certificate.
buf=io.StringIO()
with redirect_stdout(buf):h=runpy.run_path(path)
assert json.loads(buf.getvalue())['bob_coordinate_cuts']==495
Q=[v.reshape(4,12) for v in h['vs']]
I=np.eye(4);D=np.diag([1,5,-9,3]);U=np.diag(np.ones(3),1);L=U.T
P=sum(np.outer(v.reshape(-1),v.reshape(-1))/w for v,w in ((I,4),(D,116),(U,3),(L,3)))
def opt(Ts):
 n=Ts[0].shape[1];G=np.zeros((n,n),complex);H=np.zeros((n,n),complex)
 for T in Ts:G+=T.conj().T@T;H+=T.conj().T@P@T
 g,v=np.linalg.eigh((G+G.conj().T)/2);keep=g>1e-10*max(1,g.max())
 R=v[:,keep]/np.sqrt(g[keep]);A=R.conj().T@H@R;ev,evec=np.linalg.eigh((A+A.conj().T)/2)
 x=R@evec[:,-1];return float(ev[-1]),x/np.linalg.norm(x)
def optB(A):
 Ts=[]
 for q in Q:
  qq=A@q;T=np.zeros((16,48),complex)
  for i in range(4):
   for j in range(4):T[4*i+j,12*j:12*(j+1)]=qq[i,:]
  Ts.append(T)
 v,k=opt(Ts);return v,k.reshape(4,12)
def optA(K):
 Ts=[]
 for q in Q:
  qq=q@K.T;T=np.zeros((16,16),complex)
  for i in range(4):
   for j in range(4):T[4*i+j,4*i:4*i+4]=qq[:,j]
  Ts.append(T)
 v,a=opt(Ts);return v,a.reshape(4,4)
rng=np.random.default_rng(20261031);runs=[]
for trial in range(10):
 A=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));A/=np.linalg.norm(A);start=None
 for step in range(20):
  v,K=optB(A);v,A=optA(K)
  if start is None:start=v
 runs.append({'start_float':start,'end_float':v})
print(json.dumps({'seed':20261031,'runs':runs,'best_float':max(x['end_float'] for x in runs),
 'exact_rank2_lower_bound':'2925/3074','limits':'FLOATING local alternating opt, no global optimum or valid 2-block-positive witness; candidate search only.'},indent=2))
