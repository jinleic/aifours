#!/usr/bin/env python3
"""Independent stdlib-only replay of the 2D strict-sign CAD certificate.

Bivariate polynomial arithmetic reconstructs the spectral elimination and
six sign polynomials. All 23 projection factorizations are checked at 61
rational v values; degree<=60 makes this an exact identity. Independent
Fraction Sturm chains check every projection and section root; 82 rational
sign cells are verified literally. No scientific libraries or eval used.
"""
import ast,json,math,time
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parent
C=json.loads((ROOT/'frontier-20261028-ph7-equal-outer-open-cad-certificate.json').read_text())

# Sparse bivariate polynomials in (s,v), exact rational coefficients.
def clean(a):return {k:x for k,x in a.items()if x}
def con(x):return {(0,0):Q(x)}if x else {}
def add(a,b):
 o=a.copy()
 for k,x in b.items():o[k]=o.get(k,Q(0))+x
 return clean(o)
def neg(a):return {k:-x for k,x in a.items()}
def sub(a,b):return add(a,neg(b))
def scale(a,c):return clean({k:x*Q(c)for k,x in a.items()})
def mul(a,b):
 o={}
 for (i,j),x in a.items():
  for (k,l),y in b.items():o[(i+k,j+l)]=o.get((i+k,j+l),Q(0))+x*y
 return clean(o)
def pw(a,n):
 o=con(1)
 for _ in range(n):o=mul(o,a)
 return o
def sum_p(*a):
 o={}
 for x in a:o=add(o,x)
 return o
s={(1,0):Q(1)};v={(0,1):Q(1)};s2=pw(s,2);s3=pw(s,3);s4=pw(s,4)
v2=pw(v,2);v3=pw(v,3);v4=pw(v,4);v5=pw(v,5)
d=sum_p(scale(v2,45),scale(v,-54),con(17));den=scale(d,9)
a2=scale(sum_p(mul(s,sum_p(scale(v3,162),scale(v2,-972),scale(v,972),con(-306))),
                 scale(v3,-648),scale(v2,2313),scale(v,-1998),con(629)),-2)
a3=sum_p(mul(s,sum_p(scale(v4,243),scale(v3,-1458),scale(v2,4293),scale(v,-3780),con(1190))),
         scale(v4,-972),scale(v3,5832),scale(v2,-14112),scale(v,11448),con(-3604))
a4=neg(sum_p(mul(s,sum_p(scale(v5,1458),scale(v4,-8748),scale(v3,25758),scale(v2,-44712),scale(v,33048),con(-10404))),
             scale(v5,-5832),scale(v4,34992),scale(v3,-103032),scale(v2,165843),scale(v,-116586),con(36703)))
n3=sub(scale(pw(a3,2),9),scale(mul(a2,a4),2))
p2=sub(mul(den,s2),scale(a2,2))
p3=sum_p(mul(den,s3),scale(mul(s,a2),-3),scale(a3,3))
p4=sum_p(mul(pw(den,2),s4),scale(mul(den,mul(s2,a2)),-4),scale(pw(a2,2),2),
         scale(mul(den,mul(s,a3)),4),scale(mul(d,a4),-4))
h=sum_p(scale(mul(p2,p4),5),scale(mul(den,pw(p3,2)),-5),neg(mul(s2,mul(den,p4))),
        scale(mul(s,mul(den,mul(p2,p3))),2),neg(pw(p2,3)))
polys=[sub(s,con(4)),a2,a3,a4,n3,h]
assert [(max(i for i,j in p),max(j for i,j in p))for p in polys]==[(1,0),(1,3),(1,4),(1,5),(2,8),(4,10)]

# Independently check coefficient elimination after clearing positive 81*d.
D=scale(d,81);p=add(add(s,scale(v,2)),con(-4))
qnum=add(scale(a2,9),mul(D,sum_p(scale(mul(v,s),2),v2,scale(p,-4),con(Q(-70,9)))))
t4=sum_p(scale(qnum,4),mul(D,sum_p(scale(p,Q(70,9)),con(Q(68,9)))))
t3=sum_p(scale(qnum,Q(70,9)),mul(D,sum_p(scale(p,Q(68,9)),con(Q(289,81)))))
t2=sum_p(scale(qnum,Q(68,9)),mul(D,scale(p,Q(289,81))))
t1=scale(qnum,Q(289,81))
assert not sum_p(t4,scale(mul(v,a2),-18),neg(mul(v2,mul(s,D))),scale(a3,-9))
assert not sum_p(t3,scale(mul(v,a3),-18),scale(mul(v2,a2),-9),neg(a4))
assert not sum_p(scale(mul(v2,a4),-3),scale(mul(v3,a3),-18),neg(t1),scale(mul(v,t2),2))
A=add(scale(pw(sub(v,con(1)),2),9),con(8))
assert not sum_p(t2,scale(mul(v,a4),-2),scale(mul(v2,a3),-9),neg(mul(sub(s,con(4)),pw(A,3))))

# Parse printed coefficient polynomials as data, not executable code.
def parse(node):
 if isinstance(node,ast.Constant)and isinstance(node.value,int):return con(node.value)
 if isinstance(node,ast.Name)and node.id in ('s','v'):return s if node.id=='s' else v
 if isinstance(node,ast.UnaryOp)and isinstance(node.op,ast.USub):return neg(parse(node.operand))
 if isinstance(node,ast.BinOp):
  x=parse(node.left)
  if isinstance(node.op,ast.Pow):
   assert isinstance(node.right,ast.Constant)and isinstance(node.right.value,int)and node.right.value>=0
   return pw(x,node.right.value)
  y=parse(node.right)
  if isinstance(node.op,ast.Add):return add(x,y)
  if isinstance(node.op,ast.Sub):return sub(x,y)
  if isinstance(node.op,ast.Mult):return mul(x,y)
 raise ValueError(ast.dump(node))
assert all(parse(ast.parse(txt,mode='eval').body)==p for txt,p in zip(C['polynomials'],polys))
factors=[parse(ast.parse(r['polynomial'],mode='eval').body)for r in C['projection_factor_records']]
assert all(all(i==0 for i,j in p)for p in factors)

def eval_bi(p,ss,vv):return sum(c*ss**i*vv**j for (i,j),c in p.items())
def slice_s(p,vv):
 n=max(i for i,j in p);out=[Q(0)]*(n+1)
 for (i,j),c in p.items():out[i]+=c*vv**j
 return trim(out)
def slice_v(p):
 n=max(j for i,j in p);out=[Q(0)]*(n+1)
 for (i,j),c in p.items():out[j]+=c
 return trim(out)
def trim(p):
 while len(p)>1 and not p[-1]:p.pop()
 return p
def primitive(p):
 den=math.lcm(*(x.denominator for x in p));ints=[int(x*den)for x in p];g=math.gcd(*ints)
 return [Q(x//g)for x in ints]if g else[Q(0)]
def remainder(a,b):
 a=trim(a[:]);b=trim(b[:])
 while len(a)>=len(b) and any(a):
  c=a[-1]/b[-1];k=len(a)-len(b)
  for j,x in enumerate(b):a[j+k]-=c*x
  trim(a)
 return a
def sturm(p):
 a=primitive(trim(p[:]));assert len(a)>1
 b=primitive([i*a[i]for i in range(1,len(a))]);seq=[a,b]
 while len(seq[-1])>1:
  r=primitive([-x for x in remainder(seq[-2],seq[-1])])
  if not any(r):break
  seq.append(r)
 return seq
def value(p,x):
 out=Q(0)
 for c in reversed(p):out=out*x+c
 return out
def variations(seq,x):
 a=[p[-1]if x is None else value(p,x)for p in seq];a=[1 if z>0 else -1 for z in a if z]
 return sum(a[i]!=a[i-1]for i in range(1,len(a)))
def count(seq,lo,hi):return variations(seq,lo)-variations(seq,hi)
def det(A):
 A=[row[:]for row in A];d=Q(1);n=len(A)
 for k in range(n):
  ix=next((i for i in range(k,n)if A[i][k]),None)
  if ix is None:return Q(0)
  if ix!=k:A[k],A[ix]=A[ix],A[k];d=-d
  x=A[k][k];d*=x
  for i in range(k+1,n):
   c=A[i][k]/x
   for j in range(k+1,n):A[i][j]-=c*A[k][j]
   A[i][k]=Q(0)
 return d
def resultant(f,g):
 m=len(f)-1;n=len(g)-1;M=[[Q(0)]*(m+n)for _ in range(m+n)]
 for i in range(n):
  for j,x in enumerate(reversed(f)):M[i][i+j]=x
 for i in range(m):
  for j,x in enumerate(reversed(g)):M[n+i][i+j]=x
 return det(M)

# Replay all projection polynomial identities over Q. Every leading coefficient
# has v-degree<=10, every discriminant<=60 and every resultant<=52.
labels=['s-4','s2','s3','s4','newton3','hankel3'];start=time.monotonic()
assert len(C['projection_records'])==23 and len(factors)==17
for rec in C['projection_records']:
 left,right=rec['name'].split(':');i=labels.index(left);done=0;vv=0
 while done<61:
  sections=[slice_s(p,Q(vv))for p in polys];a=sections[i]
  if right=='lead':actual=a[-1]
  elif right=='disc':
   # Skip specializations with a zero global leading coefficient.
   if len(a)-1!=max(x for x,y in polys[i]):vv+=1;continue
   derivative=[k*a[k]for k in range(1,len(a))];n=len(a)-1
   actual=Q((-1)**(n*(n-1)//2))*resultant(a,derivative)/a[-1]
  else:
   j=labels.index(right);b=sections[j]
   if len(a)-1!=max(x for x,y in polys[i]) or len(b)-1!=max(x for x,y in polys[j]):vv+=1;continue
   actual=resultant(a,b)
  expected=Q(rec['scale'])
  for idx,m in rec['factors']:expected*=eval_bi(factors[idx],Q(0),Q(vv))**m
  assert actual==expected,(rec['name'],vv)
  done+=1;vv+=1
print('23 projection identities replayed at 61 exact values each',flush=True)

# Independently count every positive projection root and verify its isolator.
fseq=[sturm(slice_v(p))for p in factors];allroots=[]
for i,rec in enumerate(C['projection_factor_records']):
 ints=[(Q(a),Q(b))for a,b in rec['positive_root_intervals']]
 assert count(fseq[i],Q(0),None)==len(ints)
 for lo,hi in ints:
  assert 0<lo<hi and value(slice_v(factors[i]),lo)!=0 and value(slice_v(factors[i]),hi)!=0
  assert count(fseq[i],lo,hi)==1;allroots.append((lo,hi,i))
allroots.sort();given=[(Q(a),Q(b),i)for a,b,i in C['ordered_positive_projection_roots']]
assert allroots==given and len(allroots)==25
assert all(allroots[i][1]<allroots[i+1][0]for i in range(24))

sections=C['sections'];assert len(sections)==26;celltotal=0
for cell,rec in enumerate(sections):
 vv=Q(rec['v']);lo=Q(0)if cell==0 else allroots[cell-1][1];hi=None if cell==25 else allroots[cell][0]
 assert vv>lo and (hi is None or vv<hi)
 for f in factors:assert eval_bi(f,Q(0),vv)!=0
 ps=[slice_s(p,vv)for p in polys];records=[(Q(a),Q(b),j)for a,b,j in rec['s_roots']]
 assert records==sorted(records) and all(records[i][1]<records[i+1][0]for i in range(len(records)-1))
 for j in range(1,6):
  sq=sturm(ps[j]);loc=[(a,b)for a,b,i in records if i==j]
  assert value(ps[j],Q(4))!=0 and count(sq,Q(4),None)==len(loc)
  for a,b in loc:assert Q(4)<a<b and value(ps[j],a)!=0 and value(ps[j],b)!=0 and count(sq,a,b)==1
 sm=rec['samples'];assert len(sm)==len(records)+1
 for j,entry in enumerate(sm):
  ss=Q(entry['s']);lo=Q(4)if j==0 else records[j-1][1];hi=None if j==len(records)else records[j][0]
  assert ss>lo and (hi is None or ss<hi)
  signs=[value(p,ss)for p in ps];assert all(x!=0 for x in signs)
  idx=int(entry['negative_constraint_index']);assert 0<=idx<len(signs)and signs[idx]<0
  celltotal+=1
assert celltotal==82
print('Independent stdlib Fraction CAD replay PASS: 25 projection roots, 26 base intervals, 82 empty strict-sign cells')
print('elapsed_seconds',time.monotonic()-start)
