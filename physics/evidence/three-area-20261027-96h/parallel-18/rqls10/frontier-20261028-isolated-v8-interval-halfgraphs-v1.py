#!/usr/bin/env python3
"""Rational outward interval halfgraph gate for Valtonen V8B and transpose.

All endpoints are integers over 10^60. +,-,*,/,sqrt round OUTWARD; isqrt
is integer. A Gram interval excluding 0 certifies nonorthogonality. Zero
uncertain edges are retained; <=3 retained edges excludes a perfect matching.
Hadamard identity itself is imported from the named primary Proposition3.1.
"""
import datetime,hashlib,itertools,json,math
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;B=10**60
class I:
 def __init__(self,l,u=None):self.l=l;self.u=l if u is None else u;assert self.l<=self.u
 def __add__(a,b):
  if isinstance(b,int):b=I(b*B)
  return I(a.l+b.l,a.u+b.u)
 __radd__=__add__
 def __neg__(a):return I(-a.u,-a.l)
 def __sub__(a,b):return a+(-b if isinstance(b,I) else -b)
 def __rsub__(a,b):return (-a)+b
 def __mul__(a,b):
  if isinstance(b,int):b=I(b*B)
  v=[a.l*b.l,a.l*b.u,a.u*b.l,a.u*b.u];return I(min(v)//B,-((-max(v))//B))
 __rmul__=__mul__
 def inv(a):
  assert a.l>0 or a.u<0
  return I((B*B)//a.u,-((-B*B)//a.l))
 def __truediv__(a,b):
  if isinstance(b,int):b=I(b*B)
  return a*b.inv()
 def sqrt(a):
  assert a.l>=0
  return I(math.isqrt(a.l*B),math.isqrt(a.u*B)+1)
 def contains0(a):return a.l<=0<=a.u
class C:
 def __init__(self,r,i=0):self.r=r if isinstance(r,I) else I(r*B);self.i=i if isinstance(i,I) else I(i*B)
 def __add__(a,b):
  if isinstance(b,int):b=C(b)
  return C(a.r+b.r,a.i+b.i)
 __radd__=__add__
 def __neg__(a):return C(-a.r,-a.i)
 def __sub__(a,b):return a+(-b)
 def __mul__(a,b):
  if isinstance(b,int):b=C(b)
  return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
 __rmul__=__mul__
 def conj(a):return C(a.r,-a.i)
 def maybe_zero(a):return a.r.contains0() and a.i.contains0()
s2=I(2*B).sqrt();A=(I(2*B)+s2).sqrt();c8=A/2;c16=(I(2*B)+A).sqrt()/2;s16=(I(2*B)-A).sqrt()/2;c3=(I(2*B)+(I(2*B)-s2).sqrt()).sqrt()/2
x1=(s16/(2*c3)).sqrt();x2=(c16*c3/c8).sqrt()
y1=2*c16*(s16/c3).sqrt();y2=-(s16*(2*c16/(c8*c3)).sqrt())
z1=-(2*c16/c8*(s16*c3).sqrt());z2=-(I(B)/(2*c8)*(c3/(c16*c8)).sqrt())
a=C(x1,x2);b=C(y1,y2);c=C(z1,z2)
for v in (a,b,c):q=v.conj()*v;assert q.r.l<=B<=q.r.u and q.i.contains0()
ab=a*b;bc=b*c;ac=a*c;one=C(1);negone=C(-1)
H=[[-ab,-ab,bc,bc,one,one,ac,ac],[-ab,bc,-ab,one,bc,ac,one,-ac],[bc,-ab,one,-ab,ac,bc,-ac,one],[bc,one,-ab,ac,-ab,-ac,bc,negone],[one,bc,ac,-ab,-ac,-ab,negone,bc],[one,ac,bc,-ac,-ab,negone,-ab,-bc],[ac,one,-ac,bc,negone,-ab,-bc,-ab],[ac,-ac,one,negone,bc,-bc,-ab,ab]]
allcert=[];hist={};maxedges={}
for orient in ('V','V_transpose'):
 K=H if orient=='V' else [list(row)for row in zip(*H)]
 # These enclosures corroborate, but do NOT prove, the imported exact CH identity.
 for c,d in itertools.combinations(range(8),2):
  v=sum((K[t][c].conj()*K[t][d]for t in range(8)),C(0));assert v.maybe_zero()
 counts=Counter();maxe=0
 for E in itertools.combinations(range(8),4):
  edges=[]
  for c,d in itertools.combinations(range(8),2):
   v=sum((K[t][c].conj()*K[t][d]for t in E),C(0))
   if v.maybe_zero():edges.append((c,d))
  # Even a complete matching requires four edges, so <=3 is decisive.
  assert len(edges)<=3
  counts[len(edges)]+=1;maxe=max(maxe,len(edges));allcert.append({'orientation':orient,'half':E,'possible_edges':edges})
 hist[orient]=dict(counts);maxedges[orient]=maxe
obj={'source':'https://arxiv.org/html/2505.22947v1 Proposition3.1 and V8 definition',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'endpoint_scale':str(B),'precision_note':'integer outward enclosures and integer isqrt; no floats',
 'source_import':'Proposition 3.1 asserts this exact V8 is complex Hadamard',
 'halves_per_orientation':70,'possible_edge_histograms':hist,'maximum_possible_edges':maxedges,'certificates':allcert}
(P/'frontier-20261028-isolated-v8-interval-halfgraphs-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({k:v for k,v in obj.items()if k!='certificates'},indent=2))
