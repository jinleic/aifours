#!/usr/bin/env python3
"""Exact p=7,11 finite controls for the general analytic Paley rook theorem."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
result=[]
for p in (7,11):
 d=p-1;k=(p+1)//4;zero=(0,)*d;one=(1,)+(0,)*(d-1)
 def rt(t):
  t%=p
  return (-1,)*d if t==d else tuple(int(i==t)for i in range(d))
 def add(x,y):return tuple(a+b for a,b in zip(x,y))
 def neg(x):return tuple(-a for a in x)
 def mul(x,y):
  c=[0]*(2*d-1)
  for i,a in enumerate(x):
   for j,b in enumerate(y):c[i+j]+=a*b
  for i in range(len(c)-1,d-1,-1):
   v=c[i]
   for j in range(1,p):c[i-j]-=v
  return tuple(c[:d])
 QR={j*j%p for j in range(1,p)};NR=set(range(1,p))-QR
 g=zero
 for j in range(1,p):g=add(g,rt(j)if j in QR else neg(rt(j)))
 assert mul(g,g)==tuple(-p*x for x in one)
 for h in range(1,p):assert len(NR & {(j+h)%p for j in NR})==k-1
 subs=list(itertools.combinations(range(p),k));sums={A:tuple(sum(rt(t)[i]for t in A)for i in range(d))for A in subs}
 C=add(tuple((2*k-1)*x for x in one),g);count=zeros=0
 for A in subs:
  for B in subs:
   if not set(A).isdisjoint(B):continue
   count+=1;v=add(tuple(2*k*x for x in sums[A]),mul(C,sums[B]));zeros+=v==zero
 result.append({'p':p,'k':k,'nonresidue_set':sorted(NR),'disjoint_pairs':count,'zero_equations':zeros})
 assert zeros==0
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'field':'Z[x]/Phi_p','gauss_and_difference_set_checked':True,'finite_controls':result,'status':'PASS',
 'scope':'These two finite checks corroborate but do not replace the all-p written Fourier-convolution proof.'}
(P/'frontier-20261028-paley-rook-p7-p11-control-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
