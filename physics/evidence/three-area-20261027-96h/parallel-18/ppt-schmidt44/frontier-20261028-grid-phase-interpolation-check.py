#!/usr/bin/env python3
"""Exact 4/5-phase SR2 interpolation checks for the three-head chart."""
from fractions import Fraction as F
from itertools import combinations
import json
Z=(F(0),F(0));O=(F(1),F(0));J=(F(0),F(1))
ROOTS=(O,J,(F(-1),F(0)),(F(0),F(-1)))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def div(a,b):
 d=b[0]*b[0]+b[1]*b[1]
 if not d:raise ZeroDivisionError
 q=mul(a,conj(b));return (q[0]/d,q[1]/d)
def vec(*terms):
 out=[Z]*16
 for a,b,c in terms:out[4*a+b]=add(out[4*a+b],c)
 return out
def combine(*terms):
 out=[Z]*16
 for c,v in terms:out=[add(x,mul(c,y)) for x,y in zip(out,v)]
 return out
def cross(m,c,v,w):
 for i,x in enumerate(v):
  for j,y in enumerate(w):m[i][j]=add(m[i][j],mul(c,mul(x,conj(y))))
def outer(m,w,v):cross(m,(F(w),F(0)),v,v)
def padd(p,q):
 o=dict(p)
 for k,x in q.items():o[k]=add(o.get(k,Z),x)
 return {k:x for k,x in o.items() if x!=Z}
def pneg(p):return {k:neg(x) for k,x in p.items()}
def pmul(p,q):
 o={}
 for i,a in p.items():
  for j,b in q.items():o[i+j]=add(o.get(i+j,Z),mul(a,b))
 return {k:x for k,x in o.items() if x!=Z}
def rank2pol(v):
 m=[v[4*i:4*i+4] for i in range(4)]
 for rr in combinations(range(4),3):
  for cc in combinations(range(4),3):
   a,b,c=rr;x,y,z=cc
   d=padd(padd(pmul(m[a][x],padd(pmul(m[b][y],m[c][z]),pneg(pmul(m[b][z],m[c][y])))),
               pneg(pmul(m[a][y],padd(pmul(m[b][x],m[c][z]),pneg(pmul(m[b][z],m[c][x])))))),
          pmul(m[a][z],padd(pmul(m[b][x],m[c][y]),pneg(pmul(m[b][y],m[c][x])))))
   if d:return False
 return True
def rank2(v):return rank2pol([{0:x} if x!=Z else {} for x in v])
def psd(m):
 a=[list(row) for row in m];piv=[]
 while a:
  if any(a[i][i][1] or a[i][i][0]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i][0]>0),None)
  if p is None:return piv if all(x==Z for row in a for x in row) else None
  s=a[p][p];piv.append(str(s[0]));rem=[j for j in range(len(a)) if j!=p]
  a=[[add(a[i][j],neg(div(mul(a[i][p],a[p][j]),s))) for j in rem] for i in rem]
 return piv

def check(v0,v1,v2):
 A=vec((0,0,O),(1,1,O),(2,2,O));B=vec((0,1,O),(1,2,O))
 D=vec((1,0,O),(2,1,(F(-1),F(0))));C=vec((0,2,O),(3,3,O))
 E=vec((2,0,O),(3,0,v0),(3,1,v1),(3,2,v2))
 V_F=vec((2,0,v0),(2,1,v1),(2,2,v2));G=vec((3,0,O));V_I=vec((3,2,O));V_H=vec((0,3,O))
 X=combine((O,E),(neg(v0),G),(neg(v2),V_I))
 target=[[Z for _ in range(16)] for _ in range(16)]
 for w,x in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):outer(target,w,x)
 actual=[[Z for _ in range(16)] for _ in range(16)]
 parts=((0,O,B),(1,O,A),(2,neg(O),D),(3,neg(O),X),(4,neg(v1),G))
 assert len({k%5 for k,_,_ in parts})==5
 qp=[{} for _ in range(16)]
 for degree,c,b in parts:
  for j,x in enumerate(b):
   y=mul(c,x)
   if y!=Z:qp[j]=padd(qp[j],{degree:y})
 assert rank2pol(qp)
 for _,c,b in parts:outer(actual,(c[0]*c[0]+c[1]*c[1])/2,b)
 for z in ROOTS:
  z2=mul(z,z);z3=mul(z2,z)
  q=combine((z,A),(O,B),(neg(mul(z2,v1)),V_I),(neg(z3),X))
  assert rank2(q)
  outer(actual,F(1,8),q)
 outer(actual,F(1,2),D)
 for v in (C,V_F,V_H):outer(actual,3,v)
 T=v1[0]*v1[0]+v1[1]*v1[1]; t=(O,neg(v0),neg(v2))
 H=[[add((F(3)-T/2 if i==j and i>0 else F(3) if i==j else F(0),F(0)),
         neg(mul(t[i],conj(t[j])))) for j in range(3)] for i in range(3)]
 for i,left in enumerate((E,G,V_I)):
  for j,right in enumerate((E,G,V_I)):cross(actual,H[i][j],left,right)
 assert all(actual[i][j]==target[i][j] for i in range(16) for j in range(16))
 pt=[[target[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(16)] for i in range(16)]
 return {'v0':list(map(str,v0)),'v1':list(map(str,v1)),'v2':list(map(str,v2)),
         'five_phase_all_minor_polynomials_zero':True,'four_phase_rank2_vectors':4,
         'gram_psd_pivots':psd(H),'pt_psd_pivots':psd(pt),'state_entries_checked':256}
samples=[((F(45,46),F(0)),(F(1,2),F(0)),(F(45,46),F(0))),
         ((F(1,2),F(0)),(F(2),F(0)),(F(1,2),F(0))),
         ((F(1),F(1,2)),O,(F(1,2),F(0)))]
print(json.dumps({'cases':[check(*x) for x in samples]},indent=2))
