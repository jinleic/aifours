#!/usr/bin/env python3
"""Independent exact Fraction interval replay of the V8 halfgraph exclusions.

No fixed-point operations: all +,-,*,/ use exact rational endpoints; only
sqrt rounds outward using integer isqrt at denominator 10^45. For each claimed
excluded pair, verify its real or imaginary Gram interval misses zero.
"""
import datetime,hashlib,itertools,json,math,time
from fractions import Fraction as Q
from pathlib import Path
P=Path(__file__).resolve().parent;cert=P/'frontier-20261028-isolated-v8-interval-halfgraphs-v1.json';raw=cert.read_bytes();D=10**45
class R:
 def __init__(self,l,u=None):self.l=Q(l);self.u=Q(l if u is None else u);assert self.l<=self.u
 def __add__(a,b):
  if not isinstance(b,R):b=R(b)
  return R(a.l+b.l,a.u+b.u)
 __radd__=__add__
 def __neg__(a):return R(-a.u,-a.l)
 def __sub__(a,b):return a+(-b)
 def __rsub__(a,b):return (-a)+b
 def __mul__(a,b):
  if not isinstance(b,R):b=R(b)
  vals=[a.l*b.l,a.l*b.u,a.u*b.l,a.u*b.u];return R(min(vals),max(vals))
 __rmul__=__mul__
 def __truediv__(a,b):
  if not isinstance(b,R):b=R(b)
  assert b.l>0 or b.u<0
  return a*R(1/b.u,1/b.l)
 def sqrt(a):
  assert a.l>=0
  l=math.isqrt((a.l.numerator*D*D)//a.l.denominator);u=math.isqrt((a.u.numerator*D*D)//a.u.denominator)+1
  return R(Q(l,D),Q(u,D))
 def zero(a):return a.l<=0<=a.u
class C:
 def __init__(self,r,i=0):self.r=r if isinstance(r,R)else R(r);self.i=i if isinstance(i,R)else R(i)
 def __add__(a,b):
  if isinstance(b,int):b=C(b)
  return C(a.r+b.r,a.i+b.i)
 __radd__=__add__
 def __neg__(a):return C(-a.r,-a.i)
 def __mul__(a,b):
  if isinstance(b,int):b=C(b)
  return C(a.r*b.r-a.i*b.i,a.r*b.i+a.i*b.r)
 __rmul__=__mul__
 def conj(a):return C(a.r,-a.i)
 def maybe_zero(a):return a.r.zero() and a.i.zero()
s2=R(2).sqrt();q=(R(2)+s2).sqrt();u=q/2;c=(R(2)+q).sqrt()/2;s=(R(2)-q).sqrt()/2;v=(R(2)+(R(2)-s2).sqrt()).sqrt()/2
a=C((s/(2*v)).sqrt(),(c*v/u).sqrt());b=C(2*c*(s/v).sqrt(),-(s*(2*c/(u*v)).sqrt()));d=C(-(2*c/u*(s*v).sqrt()),-((R(1)/(2*u))*(v/(c*u)).sqrt()))
ab=a*b;bd=b*d;ad=a*d;one=C(1);minus=C(-1)
H=[[-ab,-ab,bd,bd,one,one,ad,ad],[-ab,bd,-ab,one,bd,ad,one,-ad],[bd,-ab,one,-ab,ad,bd,-ad,one],[bd,one,-ab,ad,-ab,-ad,bd,minus],[one,bd,ad,-ab,-ad,-ab,minus,bd],[one,ad,bd,-ad,-ab,minus,-ab,-bd],[ad,one,-ad,bd,minus,-ab,-bd,-ab],[ad,-ad,one,minus,bd,-bd,-ab,ab]]
data=json.loads(raw);assert len(data['certificates'])==140
orient={'V':H,'V_transpose':[list(v)for v in zip(*H)]};seen=set();excluded=0;start=time.monotonic()
for q in data['certificates']:
 E=tuple(q['half']);K=orient[q['orientation']];key=(q['orientation'],E);assert key not in seen;seen.add(key)
 allowed={tuple(v)for v in q['possible_edges']};assert len(allowed)<=2
 for c,d in itertools.combinations(range(8),2):
  if (c,d) in allowed:continue
  gram=sum((K[t][c].conj()*K[t][d]for t in E),C(0));assert not gram.maybe_zero();excluded+=1
assert len(seen)==140
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'cert_sha256':hashlib.sha256(raw).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'seconds':round(time.monotonic()-start,6),'precision_denominator':str(D),'halves_checked':len(seen),
 'excluded_edges_checked':excluded,'max_unexcluded_edges':2,'status':'PASS'}
(P/'frontier-20261028-isolated-v8-fraction-replay-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
