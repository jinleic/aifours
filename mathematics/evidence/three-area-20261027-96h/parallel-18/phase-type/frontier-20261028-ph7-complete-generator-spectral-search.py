#!/usr/bin/env python3
"""Explore full 7x7 Markov-generator spectral skeleton (all 42 edges allowed).

Four coefficient constraints force the repeated target pair after eliminating
hidden quadratic coefficients. Start from the exact v4 candidate's numerical
representative. All runs bounded and numerical; no result is a PH transfer,
rational proof, global optimum, feasibility or exclusion unless independently
verified. Complete graph may approach a reducible boundary.
"""
from pathlib import Path
import json,sys,time,numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
from scipy.optimize import minimize
from numpy.polynomial.polynomial import polymul,polypow
rng=np.random.default_rng(20261114);I,J=np.where(~np.eye(7,dtype=bool));start=time.monotonic();WALL=100
U=1.338787907158986;V=1.042029691134;Z0=.820420440784126
p=5*U+2*V-4;q=10*U*U+10*U*V-20*U+V*V-8*V-2*Z0+10
R=polymul(polypow([U,1.],5),polypow([V,1.],2))-polymul(polymul([0.,1.],polypow([1+Z0,2.,1.],2)),[q,p,1.])
D1=R[2];D3=R[0]-V*V*D1
raw=np.zeros((7,7));
for i,r in enumerate([U,U,U,U,U,V,V]):raw[i,i]=-r
for i in range(6):raw[i,i+1]=1
raw[4,0]=D1;raw[6,0]=D3
h=np.array([1.,U,U**2,U**3,U**4,U**5-D1,V*(U**5-D1)])
G=raw*h[None,:]/h[:,None]
assert np.max(np.abs(G.sum(axis=1)))<1e-10
seed=np.r_[G[I,J],Z0];low=np.r_[np.zeros(42),.5];high=np.r_[np.full(42,20.),8/9]

def char(G):
 b=np.eye(7);out=[1.]
 for k in range(1,8):
  a=G@b;ck=-np.trace(a)/k;out.append(ck);b=a+ck*np.eye(7)
 return np.array(out)

def constraints(x):
 rates=x[:42];z=x[-1];mat=np.zeros((7,7));mat[I,J]=rates;mat[np.arange(7),np.arange(7)]=-mat.sum(axis=1)
 a=char(mat);p=a[1]-4;q=a[2]-4*p-(6+2*z)
 target=np.convolve([1.,4.,6+2*z,4+4*z,(1+z)**2,0.],[1.,p,q])
 return (a[3:7]-target[3:7])/(1+np.abs(target[3:7])),p,q,mat

def eq(x):return constraints(x)[0]
def ine(x):
 _,p,q,_=constraints(x);return np.array([p-.0001,q-.0001])

assert np.linalg.norm(eq(seed),np.inf)<1e-10 and min(ine(seed))>0
rows=[];best=None
for j in range(7):
 if time.monotonic()-start>WALL:break
 if j==0:x=seed.copy()
 elif j<5:
  x=seed.copy();x[:42]=np.maximum(0,x[:42]+rng.normal(0,.01,42));x[-1]=Z0
 else:
  x=np.r_[rng.exponential(.2,42),.8]
 x=np.maximum(low,np.minimum(high,x))
 try:
  fit=minimize(lambda x:-x[-1],x,method='SLSQP',bounds=list(zip(low,high)),
   constraints=[{'type':'eq','fun':eq},{'type':'ineq','fun':ine}],options={'maxiter':1200,'ftol':1e-12,'disp':False})
 except (ValueError,np.linalg.LinAlgError) as exc:
  rows.append({'start':j,'error':str(exc)});continue
 e=float(np.linalg.norm(eq(fit.x),np.inf));item={'start':j,'z':float(fit.x[-1]),'residual_inf':e,
  'min_qp_margin':float(min(ine(fit.x))),'success':bool(fit.success),'message':str(fit.message),'iterations':int(fit.nit)}
 rows.append(item);print('run',item,flush=True)
 if e<1e-8 and min(ine(fit.x))>=0 and (best is None or fit.x[-1]>best[0]):best=(fit.x[-1],fit.x.copy())
out=ROOT/'frontier-20261028-ph7-complete-generator-spectral-search-result.json'
out.write_text(json.dumps({'runs':rows,'best_feasible_numeric_z':float(best[0])if best else None,
 'best_rates':best[1].tolist()if best else None,'elapsed_seconds':time.monotonic()-start,
 'scope':'all 42 offdiagonal generator entries allowed; numerical spectral skeleton only; no input/exit numerator, rational proof, global optimum or exclusion'},indent=2)+'\n')
print('saved:',out)
