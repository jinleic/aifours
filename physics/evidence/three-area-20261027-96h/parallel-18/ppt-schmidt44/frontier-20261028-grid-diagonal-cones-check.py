#!/usr/bin/env python3
"""Exact PPT/rank2 checks for two weighted diagonal grid-cone examples."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import runpy

Z=(F(0),F(0));O=(F(1),F(0));J=(F(0),F(1))
ROOTS=(O,J,(F(-1),F(0)),(F(0),F(-1)))

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[0],-a[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x):return (a[0]*x,a[1]*x)
def conj(a):return (a[0],-a[1])

def ket(*terms):
 v=[Z]*16
 for a,b,c in terms:v[4*a+b]=add(v[4*a+b],c)
 return v

def combine(*terms):
 out=[Z]*16
 for c,v in terms:out=[add(x,mul(c,y)) for x,y in zip(out,v)]
 return out

def outer(m,w,v):
 for i,x in enumerate(v):
  for j,y in enumerate(v):m[i][j]=add(m[i][j],scale(mul(x,conj(y)),w))

def rank2(v):
 m=[v[4*i:4*i+4] for i in range(4)]
 for rr in combinations(range(4),3):
  for cc in combinations(range(4),3):
   a,b,c=rr;x,y,z=cc
   det=add(add(mul(m[a][x],add(mul(m[b][y],m[c][z]),neg(mul(m[b][z],m[c][y])))),
               neg(mul(m[a][y],add(mul(m[b][x],m[c][z]),neg(mul(m[b][z],m[c][x])))))),
           mul(m[a][z],add(mul(m[b][x],m[c][y]),neg(mul(m[b][y],m[c][x])))))
   if det!=Z:return False
 return True

def check(which):
 A=ket((0,0,O),(1,1,O),(2,2,O));B=ket((0,1,O),(1,2,O));D=ket((1,0,O),(2,1,(F(-1),F(0))))
 C=ket((0,2,O),(3,3,O)) if which=='drop3' else ket((0,2,O))
 E=ket((2,0,O)) if which=='drop3' else ket((2,0,O),(3,3,O))
 Fv=ket((2,3,O));G=ket((3,0,O));I=ket((3,2,O));H=ket((0,3,O))
 if which=='drop3':
  weights={'A':F(1),'B':F(4),'D':F(1),'C':F(25),'E':F(4),'G':F(3),'I':F(25),'H':F(25)}
  basis={'A':A,'B':B,'D':D,'C':C,'E':E,'G':G,'I':I,'H':H}
 else:
  weights={'A':F(1),'B':F(1),'D':F(4),'C':F(4),'E':F(25),'F':F(25),'G':F(25),'I':F(3)}
  basis={'A':A,'B':B,'D':D,'C':C,'E':E,'F':Fv,'G':G,'I':I}
 target=[[Z for _ in range(16)] for _ in range(16)]
 for name,w in weights.items():outer(target,w,basis[name])
 actual=[[Z for _ in range(16)] for _ in range(16)]
 for z in ROOTS:
  z2=mul(z,z);z3=mul(z2,z)
  if which=='drop3':q=combine((z,A),((F(2),F(0)),B),(z2,D),(scale(neg(z3),F(1,4)),E))
  else:q=combine((z,A),(z2,B),((F(2),F(0)),D),(scale(z3,F(1,4)),C))
  if not rank2(q):raise AssertionError('seed rank')
  outer(actual,F(1,4),q)
 leftover=dict(weights)
 for n in ('A','B','D'):leftover[n]=F(0)
 leftover['E' if which=='drop3' else 'C']-=F(1,16)
 for name,w in leftover.items():
  if w<0:raise AssertionError('negative remainder')
  if w:
   if not rank2(basis[name]):raise AssertionError('bad remainder rank')
   outer(actual,w,basis[name])
 if actual!=target:raise AssertionError('decomposition mismatch')
 if any(x[1] for row in target for x in row):raise AssertionError('unexpected complex target')
 real=[[x[0] for x in row] for row in target]
 src=runpy.run_path(str(Path(__file__).with_name('frontier-20261028-grid-state-sr2-check.py')))
 state_piv=src['exact_psd_pivots'](real);pt_piv=src['exact_psd_pivots'](src['partial_transpose'](real,4,4))
 return {'case':which,'weights':{k:str(v) for k,v in weights.items()},
         'checked_phase_vectors':4,'checked_state_entries':256,'mismatches':0,
         'state_rank':len(state_piv),'pt_rank':len(pt_piv),'pt_pivots':pt_piv}

print(json.dumps({'cases':[check('drop3'),check('drop4')]},indent=2))
