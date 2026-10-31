#!/usr/bin/env python3
"""Exact Gaussian-rational checks of the v1=0 projection chart extension."""
from fractions import Fraction as F
from itertools import combinations
import json

Z=(F(0),F(0));O=(F(1),F(0));J=(F(0),F(1))
ROOTS=(O,J,(F(-1),F(0)),(F(0),F(-1)))

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x):return (a[0]*x,a[1]*x)
def conj(a):return (a[0],-a[1])
def div(a,b):
 d=b[0]*b[0]+b[1]*b[1]
 if not d:raise ZeroDivisionError
 return scale(mul(a,conj(b)),F(1)/d)

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

def rank2(v):
 m=[v[4*i:4*i+4] for i in range(4)]
 for rr in combinations(range(4),3):
  for cc in combinations(range(4),3):
   a,b,c=rr;x,y,z=cc
   d=add(add(mul(m[a][x],add(mul(m[b][y],m[c][z]),neg(mul(m[b][z],m[c][y])))),
             neg(mul(m[a][y],add(mul(m[b][x],m[c][z]),neg(mul(m[b][z],m[c][x])))))),
         mul(m[a][z],add(mul(m[b][x],m[c][y]),neg(mul(m[b][y],m[c][x])))))
   if d!=Z:return False
 return True

def psd(m):
 a=[list(row) for row in m];piv=[]
 while a:
  if any(a[i][i][1] or a[i][i][0]<0 for i in range(len(a))):return None
  p=next((i for i in range(len(a)) if a[i][i][0]>0),None)
  if p is None:return piv if all(x==Z for row in a for x in row) else None
  s=a[p][p];piv.append(str(s[0]));rem=[j for j in range(len(a)) if j!=p]
  a=[[add(a[i][j],neg(div(mul(a[i][p],a[p][j]),s))) for j in rem] for i in rem]
 return piv

def check(v0,v2):
 U=v0[0]**2+v0[1]**2;W=v2[0]**2+v2[1]**2;A0=1+U+W
 s=scale(conj(v0),-A0/(1+A0*U))
 A=vec((0,0,O),(1,1,O),(2,2,O));B=vec((0,1,O),(1,2,O))
 D=vec((1,0,O),(2,1,(F(-1),F(0))));C=vec((0,2,O),(3,3,O))
 E=vec((2,0,O),(3,0,v0),(3,2,v2));V_F=vec((2,0,v0),(2,2,v2))
 G=vec((3,0,O));V_I=vec((3,2,O));V_H=vec((0,3,O));X=vec((2,0,O))
 V_W=combine(((F(-1),F(0)),X),(s,combine((O,V_F),(neg(v0),X))))
 target=[[Z for _ in range(16)] for _ in range(16)]
 for w,x in zip((1,1,1,3,3,3,3,3,3),(A,B,D,C,E,V_F,G,V_I,V_H)):outer(target,w,x)
 actual=[[Z for _ in range(16)] for _ in range(16)]
 for z in ROOTS:
  z2=mul(z,z);z3=mul(z2,z)
  q=combine((z,A),(O,B),(z2,D),(z3,V_W))
  if not rank2(q):raise AssertionError('rank2 phase seed')
  outer(actual,F(1,4),q)
 for x in (C,V_H):outer(actual,3,x)
 t=(neg(add(O,mul(s,v0))),mul(add(O,mul(s,v0)),v0),
    mul(add(O,mul(s,v0)),v2),s)
 HB=[[add((F(3 if i==j else 0),F(0)),neg(mul(t[i],conj(t[j]))))
      for j in range(4)] for i in range(4)]
 for i,left in enumerate((E,G,V_I,V_F)):
  for j,right in enumerate((E,G,V_I,V_F)):cross(actual,HB[i][j],left,right)
 bad=[(i,j) for i in range(16) for j in range(16) if actual[i][j]!=target[i][j]]
 if bad:raise AssertionError({'mismatches':bad})
 pt=[[target[4*(i//4)+(j%4)][4*(j//4)+(i%4)] for j in range(16)] for i in range(16)]
 return {'v0':[str(x) for x in v0],'v2':[str(x) for x in v2],
         's':[str(x) for x in s],'gram_psd_pivots':psd(HB),
         'state_pt_psd_pivots':psd(pt),'checked_rank2_phase_vectors':4,
         'entries_checked':256,'mismatches':len(bad)}

cases=[((F(2),F(0)),O),(O,(F(2),F(0))),(J,O),(Z,O),(Z,(F(2),F(0)))]
print(json.dumps({'cases':[check(v0,v2) for v0,v2 in cases]},indent=2))
