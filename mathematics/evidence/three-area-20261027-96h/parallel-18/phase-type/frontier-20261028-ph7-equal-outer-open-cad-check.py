#!/usr/bin/env python3
"""Exact open-CAD obstruction for arbitrary five common rates, outer V,V.

Necessary strict signs s>4, s2,s3,s4>0, Newton3>0, Hankel det>0.
The equality/rank-degenerate common-rate cases are separate theorems.
A full projection factorization and all rational section/root samples are
saved for an independently implemented replay.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
s,v,y,t=S.symbols('s v y t',real=True);z=S.Rational(8,9)
d=45*v*v-54*v+17
A2=-2*((162*v**3-972*v**2+972*v-306)*s-648*v**3+2313*v**2-1998*v+629)
A3=(243*v**4-1458*v**3+4293*v**2-3780*v+1190)*s-972*v**4+5832*v**3-14112*v**2+11448*v-3604
A4=-((1458*v**5-8748*v**4+25758*v**3-44712*v**2+33048*v-10404)*s-5832*v**5+34992*v**4-103032*v**3+165843*v**2-116586*v+36703)
N3=S.expand(9*A3**2-2*A2*A4);D=9*d
P2=D*s**2-2*A2;P3=D*s**3-3*s*A2+3*A3
P4=D**2*s**4-4*D*s**2*A2+2*A2**2+4*D*s*A3-4*d*A4
HH=S.expand(5*P2*P4-5*D*P3**2-s**2*D*P4+2*s*D*P2*P3-P2**3)
polys=[s-4,S.expand(A2),S.expand(A3),S.expand(A4),N3,HH]
labels=['s-4','s2','s3','s4','newton3','hankel3']
assert [S.degree(p,s)for p in polys]==[1,1,1,1,2,4]

# Reconstruct spectral coefficient elimination before applying any inequalities.
s2,s3,s4,s5=S.symbols('s2 s3 s4 s5',real=True)
Q=y*y+(s+2*v-4)*y+(s2+2*v*s+v*v-4*(s+2*v-4)-S.Rational(70,9))
Dz=y*((y+1)**2+z)**2;T=S.Poly(S.expand(Dz*Q),y)
r3=S.expand(T.nth(4)-2*v*s2-v*v*s)
r4=S.expand(T.nth(3)-2*v*r3-v*v*s2)
resid=S.factor(-3*v*v*r4-2*v**3*r3-T.nth(1)+2*v*T.nth(2))
assert S.factor(resid.subs(s2,A2/(9*d)))==0
assert S.cancel(r3.subs(s2,A2/(9*d))-A3/(9*d))==0
assert S.cancel(r4.subs(s2,A2/(9*d))-A4/(81*d))==0
L=S.factor(T.nth(2)-2*v*r4-v*v*r3)
assert S.cancel(L.subs(s2,A2/(9*d))-(s-4)*(9*(v-1)**2+8)**3/(81*d))==0

# All leading coefficients, discriminants, and pairwise resultants project
# every possible change of the strict sign decomposition onto the v-axis.
project=[]
for label,p in zip(labels,polys):
 P=S.Poly(p,s);project.append((label+':lead',P.LC()))
 if P.degree()>1:project.append((label+':disc',S.discriminant(p,s)))
for i,j in combinations(range(len(polys)),2):project.append((labels[i]+':'+labels[j],S.resultant(polys[i],polys[j],s)))
assert len(project)==23 and all(P!=0 for _,P in project)
keys={}
for _,P in project:
 for f,m in S.factor_list(P,v)[1]:
  fp=S.Poly(f,v).clear_denoms()[1].primitive()[1]
  if fp.LC()<0:fp=-fp
  keys[tuple(fp.all_coeffs())]=fp.as_expr()
keylist=sorted(keys,key=lambda k:(len(k),tuple(k)));factors=[keys[k]for k in keylist];index={k:i for i,k in enumerate(keylist)}
assert len(factors)==17
project_records=[]
for name,P in project:
 items=[];prod=S.Integer(1)
 for f,m in S.factor_list(P,v)[1]:
  fp=S.Poly(f,v).clear_denoms()[1].primitive()[1]
  if fp.LC()<0:fp=-fp
  idx=index[tuple(fp.all_coeffs())];items.append([idx,int(m)]);prod*=factors[idx]**m
 scale=S.cancel(S.Poly(P,v).LC()/S.Poly(prod,v).LC());assert S.expand(P-scale*prod)==0
 project_records.append({'name':name,'scale':str(scale),'factors':items,'degree':int(S.degree(P,v))})

def trim(p):
 while len(p)>1 and not p[-1]:p.pop()
 return p
def primitive(p):
 den=1
 for x in p:den=lcm(den,x.denominator)
 a=[int(x*den)for x in p];g=0
 for x in a:g=gcd(g,abs(x))
 return [F(x//g)for x in a]if g else[F(0)]
def rem(a,b):
 a=trim(a[:]);b=trim(b[:])
 while len(a)>=len(b) and any(a):
  c=a[-1]/b[-1];k=len(a)-len(b)
  for i,x in enumerate(b):a[i+k]-=c*x
  trim(a)
 return a
def seq(poly,var):
 P=S.Poly(poly,var);a=primitive([F(int(x.p),int(x.q))for x in reversed(P.all_coeffs())])
 b=primitive([i*a[i]for i in range(1,len(a))]);out=[a,b]
 while len(out[-1])>1:
  c=primitive([-x for x in rem(out[-2],out[-1])])
  if not any(c):break
  out.append(c)
 return out
def evaluate(p,x):
 r=F(0)
 for c in reversed(p):r=r*x+c
 return r
def variations(q,x):
 vals=[p[-1]if x is None else evaluate(p,F(x))for p in q]
 nz=[1 if v>0 else -1 for v in vals if v];return sum(nz[i]!=nz[i-1]for i in range(1,len(nz)))
def count(q,lo,hi):return variations(q,lo)-variations(q,hi)

roots=[];factor_records=[]
for i,f in enumerate(factors):
 st=seq(f,v);iv=[]
 for (lo,hi),mult in S.intervals(f,eps=S.Rational(1,10**12)):
  if hi<=0:continue
  assert lo>0 and lo<hi and count(st,lo,hi)==1
  roots.append((lo,hi,i));iv.append([str(lo),str(hi)])
 assert count(st,0,None)==len(iv)
 factor_records.append({'polynomial':str(f),'positive_root_intervals':iv})
roots.sort(key=lambda x:x[0]);assert len(roots)==25 and all(roots[i][1]<roots[i+1][0]for i in range(24))
vs=[roots[0][0]/2]+[(roots[i][1]+roots[i+1][0])/2 for i in range(24)]+[roots[-1][1]+1]
sections=[];total=0
for vi in vs:
 sroots=[]
 for j,p in enumerate(polys[1:],1):
  P=S.Poly(p.subs(v,vi),s);st=seq(P,s);local=[]
  for (lo,hi),mult in S.intervals(P,eps=S.Rational(1,10**10)):
   if hi<=4:continue
   assert lo>4 and lo<hi and count(st,lo,hi)==1
   sroots.append((lo,hi,j));local.append((lo,hi))
  assert count(st,4,None)==len(local)
 sroots.sort(key=lambda x:x[0]);assert all(sroots[i][1]<sroots[i+1][0]for i in range(len(sroots)-1))
 ss=([S.Rational(5)]if not sroots else [(4+sroots[0][0])/2]+[(sroots[i][1]+sroots[i+1][0])/2 for i in range(len(sroots)-1)]+[sroots[-1][1]+1])
 samples=[]
 for si in ss:
  signs=[S.sign(p.subs({s:si,v:vi}))for p in polys];assert all(x!=0 for x in signs)
  failures=[j for j,x in enumerate(signs)if x<0];assert failures,(vi,si)
  samples.append({'s':str(si),'negative_constraint_index':failures[0]})
 total+=len(samples)
 sections.append({'v':str(vi),'s_roots':[[str(lo),str(hi),j]for lo,hi,j in sroots],'samples':samples})
assert len(sections)==26 and total==82
out=ROOT/'frontier-20261028-ph7-equal-outer-open-cad-certificate.json'
out.write_text(json.dumps({'scope':'strict s>4, s2/s3/s4>0, Newton3>0 and 3x3 Hankel determinant>0; no full graph assumption beyond equal outer',
 'polynomials':[str(x)for x in polys],'projection_factor_records':factor_records,'projection_records':project_records,
 'ordered_positive_projection_roots':[[str(a),str(b),i]for a,b,i in roots],
 'sections':sections,'sample_cell_count':total,'proof':'23 projection polynomials, 17 factors, 25 disjoint positive roots, 26 base intervals, 82 rational sign cells'},indent=2)+'\n')
print('SymPy',S.__version__,'and custom Fraction Sturm PASS: open system empty; 26 projection intervals and',total,'sign cells')
print('saved:',out)
