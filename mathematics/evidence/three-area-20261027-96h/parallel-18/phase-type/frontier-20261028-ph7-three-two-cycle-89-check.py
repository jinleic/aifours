#!/usr/bin/env python3
"""Exact z=8/9 exclusion: five common rates 3U+2W, two equal outer rates.

Eliminate W via two 4x4 Sylvester resultants, then V via an 18x18 resultant.
Its factorization is strictly positive for U>0 by exact rational Bernstein
subdivision on [0,2] and positive shifted powers on [2,infinity).
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,v,w,y=S.symbols('u v w y',real=True);z=S.Rational(8,9)
base=(y+u)**3*(y+w)**2*(y+v)**2;B=S.Poly(base,y)
p=B.nth(6)-4;q=B.nth(5)-4*p-(6+2*z)
D=y*((y+1)**2+z)**2;R=S.Poly(S.expand(base-D*(y*y+p*y+q)),y)
E4,E3=R.nth(4),R.nth(3);E1=S.expand(R.nth(1)-2*v*R.nth(2))
assert [S.degree(f,w)for f in (E4,E3,E1)]==[2,2,2]
Fpoly=S.resultant(E4,E3,w);Hpoly=S.resultant(E4,E1,w)
assert [S.degree(Fpoly,u),S.degree(Fpoly,v),S.degree(Hpoly,u),S.degree(Hpoly,v)]==[10,8,10,10]

def sylvester(f,g,var):
 Fp,Hp=S.Poly(f,var),S.Poly(g,var);m,n=Fp.degree(),Hp.degree();M=S.zeros(m+n)
 for i in range(n):
  for j,c in enumerate(Fp.all_coeffs()):M[i,i+j]=c
 for i in range(m):
  for j,c in enumerate(Hp.all_coeffs()):M[n+i,i+j]=c
 return M

assert S.cancel(sylvester(E4,E3,w).det(method='domain-ge')-Fpoly)==0
assert S.cancel(sylvester(E4,E1,w).det(method='domain-ge')-Hpoly)==0
res=S.resultant(Fpoly,Hpoly,v);constant,factors=S.factor_list(res,u)
assert [(S.degree(f,u),m)for f,m in factors]==[(1,6),(2,12),(6,1),(30,1),(66,1)]
assert S.expand(constant*S.prod(f**m for f,m in factors)-res)==0
assert S.expand(factors[1][0]-(9*(u-1)**2+8))==0

def frac(c):return F(int(S.numer(c)),int(S.denom(c)))
def bernstein(poly,left,right):
 P=S.Poly(poly,u);n=P.degree();coeff=[frac(P.nth(i))for i in range(n+1)];lo=F(left);width=F(right)-lo
 power=[sum(coeff[i]*comb(i,j)*lo**(i-j)*width**j for i in range(j,n+1))for j in range(n+1)]
 return [sum(power[j]*F(comb(k,j),comb(n,j))for j in range(k+1))for k in range(n+1)]
def split(b):
 levels=[b]
 while len(levels[-1])>1:levels.append([(x+y)/2 for x,y in zip(levels[-1],levels[-1][1:])])
 return [x[0]for x in levels],[x[-1]for x in levels][::-1]
def cover(poly):
 stack=[(bernstein(poly,0,2),F(0),F(2),0)];leaves=[]
 while stack:
  b,lo,hi,depth=stack.pop()
  if all(x>0 for x in b):leaves.append((lo,hi));continue
  assert depth<12,(lo,hi)
  left,right=split(b);mid=(lo+hi)/2;stack.append((right,mid,hi,depth+1));stack.append((left,lo,mid,depth+1))
 leaves.sort();assert leaves[0][0]==0 and leaves[-1][1]==2
 assert all(leaves[i][1]==leaves[i+1][0]for i in range(len(leaves)-1))
 tail=S.Poly(S.expand(poly.subs(u,u+2)),u)
 assert all(c>0 for c in tail.all_coeffs())
 return [[str(a),str(b)]for a,b in leaves]
records=[]
for factor,multiplicity in factors[2:]:
 leaves=cover(factor)
 records.append({'degree':int(S.degree(factor,u)),'multiplicity':multiplicity,'polynomial':str(factor),
                 'bernstein_positive_subintervals_0_to_2':leaves,'positive_shifted_power_tail_from_2':True})
out=ROOT/'frontier-20261028-ph7-three-two-cycle-89-certificate.json'
out.write_text(json.dumps({'scope':'common rates 3U+2W, outer V,V; U>0; all feedbacks; spectral only, not unrestricted PH7',
 'z':'8/9','p':str(p),'q':str(q),'conditions':['E4=0','E3=0','E1=0'],
 'first_resultant_degrees_in_U_V':[[10,8],[10,10]],'outer_factor_constant':str(constant),
 'outer_factors':[{'degree':1,'multiplicity':6,'polynomial':str(factors[0][0])},
                  {'degree':2,'multiplicity':12,'polynomial':str(factors[1][0])}]+records,
 'checks':['both first resultants equal literal 4x4 Sylvester determinants',
           'second resultant exact factorization','Bernstein positive [0,2] and shifted-power tail for degree 6,30,66 factors'],
 'realizability_claim':'excluded for this family only; not all topologies'},indent=2)+'\n')
print('SymPy',S.__version__,'Fraction Bernstein PASS: all 3U+2W/V,V spectral graphs excluded at z=8/9')
print('factor degrees:',[(r['degree'],len(r['bernstein_positive_subintervals_0_to_2']))for r in records]);print('saved:',out)
