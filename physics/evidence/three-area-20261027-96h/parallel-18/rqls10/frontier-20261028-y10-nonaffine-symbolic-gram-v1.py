#!/usr/bin/env python3
"""Symbolic Laurent Gram reduction for Y_10_3_278, no CAS dependency.

Variables a,b,u,r in Laurent Z[a,b,u,r]. q,s,t substituted rationally;
clear denominators and reduce by u/r defining quadratics using exact integer
polynomial arithmetic. c remains an independent unit Laurent variable.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
# Expressions as in the public MATLAB source; +/- and */ only.
S=[
 ['1','1','1','1','1','1','1','1','1','1'],
 ['1','1','u','-s*q/r','-s*q/r','s*q/r','s*q/r','-u','-1','-1'],
 ['1','1','-1','s','s/r','-s*q/b/r','-s*q/a/r','u','-1/c','1/c'],
 ['1','1','-1','s/r','s','-s*q/a/r','-s*q/b/r','u','1/c','-1/c'],
 ['1','r','q','-q','-q','q*c','-q*c','r*u/s','r*a/s','r*b/s'],
 ['1','1/r','q/r','-q/r','-q/r','-q*c/r','q*c/r','u/s','b/s','a/s'],
 ['1','a/b','a','a*c','-a*c','-a','-a','t','-r*a/s','-a/s'],
 ['1','b/a','b','-b*c','b*c','-b','-b','t*b/a','-b/s','-r*b/s'],
 ['1','-1','-c','-a*c','-b*c','-q*c','-q*c/r','-u*c','c','c'],
 ['1','-1','c','b*c','a*c','q*c/r','q*c','u*c','-c','-c']]
vars='abuqrstc';idx={x:i for i,x in enumerate(vars)}
def parse(s):
 sign=-1 if s.startswith('-')else 1;s=s.lstrip('-');v=[0]*len(vars);operation=1;token=''
 for ch in s+'*':
  if ch in '*/':
   if token!='1':assert token in idx;v[idx[token]]+=operation
   token='';operation=1 if ch=='*' else -1
  else:token+=ch
 return sign,tuple(v)
K=[[parse(x)for x in row]for row in S]
Z=(0,0,0,0);ONE={Z:1}
def poly(*terms):
 out={}
 for e,v in terms:
  out[e]=out.get(e,0)+v
 return {e:v for e,v in out.items()if v}
def add(*items):
 out={}
 for x in items:
  for e,v in x.items():out[e]=out.get(e,0)+v
 return {e:v for e,v in out.items()if v}
def neg(x):return {e:-v for e,v in x.items()}
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 z={}
 for e,a in x.items():
  for f,b in y.items():
   k=tuple(e[i]+f[i]for i in range(4));z[k]=z.get(k,0)+a*b
 return {e:v for e,v in z.items()if v}
def power(x,n):
 v=ONE
 for _ in range(n):v=mul(v,x)
 return v
def mon(a=0,b=0,u=0,r=0,c=1):return {(a,b,u,r):c}
A=mon(a=1);B=mon(b=1);U=mon(u=1);R=mon(r=1)
W=sub(sub(sub(ONE,mon(u=-1)),mon(a=-1)),mon(b=-1))
Nq=add(ONE,R);Dq=W
Ns=sub(power(Nq,2),mul(R,W));Ds=mul(Nq,sub(W,ONE))
Nt=neg(mul(mul(mul(R,U),add(A,B)),Ds));Dt=mul(B,add(mul(mul(R,add(U,ONE)),Ds),mul(add(ONE,R),Ns)))
D=sub(mul(A,B),add(A,B));C=sub(sub(mul(A,B),mul(power(A,2),B)),mul(A,power(B,2)))
N=add(neg(A),mul({Z:2},power(A,2)),neg(B),mul({Z:4},mul(A,B)),neg(mul(power(A,2),B)),mul({Z:2},power(B,2)),neg(mul(A,power(B,2))))
Pu=add(mul(D,power(U,2)),neg(mul(N,U)),C)
p=add({Z:-2},neg(mon(a=1,b=-1)),neg(mon(a=-1,b=1)))
Pr=add(power(R,2),neg(mul(p,R)),ONE)

def reduce_poly(x):
 if not x:return {}
 # Shift all Laurent exponents to nonnegative u,r; monomial is invertible on domain.
 minu=min(e[2]for e in x);minr=min(e[3]for e in x)
 if minu<0 or minr<0:x=mul(x,mon(u=max(-minu,0),r=max(-minr,0)))
 # r^2 = p*r-1; p is Laurent only in a,b.
 while x and max(e[3]for e in x)>=2:
  k=max(e[3]for e in x);top={e:v for e,v in x.items()if e[3]==k}
  x=sub(x,top)
  for e,v in top.items():
   base=mon(a=e[0],b=e[1],u=e[2],r=k-2,c=v);x=add(x,mul(base,sub(mul(p,R),ONE)))
 # Fraction-free pseudo-division by D*u^2-N*u+C, with D nonzero in domain.
 while x and max(e[2]for e in x)>=2:
  k=max(e[2]for e in x);top={e:v for e,v in x.items()if e[2]==k};lower={}
  for e,v in top.items():lower[(e[0],e[1],k-2,e[3])]=v
  x=sub(mul(D,x),mul(lower,Pu))
 return x

def coefficient(terms):
 # terms: sign and exponent tuple in [a,b,u,q,r,s,t,c]
 maxes=[]
 for j in (3,5,6):
  ks=[e[j]for sign,e in terms];maxes.append((max(0,max(ks)),max(0,-min(ks))))
 total={}
 for sign,e in terms:
  x=mon(a=e[0],b=e[1],u=e[2],r=e[4],c=sign)
  for j,(num,den),(hi,lo) in zip((3,5,6),((Nq,Dq),(Ns,Ds),(Nt,Dt)),maxes):
   x=mul(x,mul(power(num,lo+e[j]),power(den,hi-e[j])))
  total=add(total,x)
 return total

checks=[];failures=[];maxterms=0
for axis in ('col','row'):
 for i,j in itertools.combinations(range(10),2):
  groups=collections.defaultdict(list)
  for k in range(10):
   x,y=(K[k][i],K[k][j]) if axis=='col' else (K[i][k],K[j][k]);sg=x[0]*y[0];e=tuple(y[1][h]-x[1][h]for h in range(8));groups[e[7]].append((sg,e))
  for cpower,terms in groups.items():
   numerator=coefficient(terms);maxterms=max(maxterms,len(numerator));remainder=reduce_poly(numerator)
   checks.append((axis,i,j,cpower,len(numerator),len(remainder)))
   if remainder:failures.append({'axis':axis,'i':i,'j':j,'c_power':cpower,'remainder_terms':len(remainder),'sample':list(remainder.items())[:10]})
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'scope':'unit a,b,u,r,q,s,t; q,s,t rational substitutions and u/r quadratic relations; denominators nonzero',
 'gram_pairs':90,'c_coefficients_checked':len(checks),'max_numerator_terms':maxterms,'failures':failures,'status':'PASS' if not failures else 'UNRESOLVED'}
(P/'frontier-20261028-y10-nonaffine-symbolic-gram-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
