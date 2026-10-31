#!/usr/bin/env python3
"""Exclude z=8/9 in a 4U+W / 2V directed two-cycle spectral family.

Coefficient identities eliminate W; exact resultant eliminates V; independent
Fraction Sturm sequences show the resultant has no real U. This imposes no
positivity and proves no real solution within this stated spectral family.
"""
from fractions import Fraction as F
from math import gcd,lcm
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S
u,v,w,y=S.symbols('u v w y',real=True);z=S.Rational(8,9)
p=4*u+w+2*v-4
q=6*u*u+8*u*v+v*v+4*u*w+2*v*w-4*p-(6+2*z)
D=y*((y+1)**2+z)**2
R=S.Poly(S.expand((y+w)*(y+u)**4*(y+v)**2-D*(y*y+p*y+q)),y)
E4,E3=R.nth(4),R.nth(3);E1=S.expand(R.nth(1)-2*v*R.nth(2))
assert all(S.degree(f,w)<=1 for f in (E4,E3,E1))
A4,B4=S.diff(E4,w),E4.subs(w,0)
A3,B3=S.diff(E3,w),E3.subs(w,0)
A1,B1=S.diff(E1,w),E1.subs(w,0)
Fpoly=S.expand(A4*B3-A3*B4);Hpoly=S.expand(A4*B1-A1*B4)
assert S.expand(A4*E3-A3*E4-Fpoly)==0
assert S.expand(A4*E1-A1*E4-Hpoly)==0
fp,hp=S.Poly(Fpoly,v),S.Poly(Hpoly,v);m,n=fp.degree(),hp.degree()
assert (m,n)==(4,5)
resultant=S.resultant(Fpoly,Hpoly,v)
# Independent Sylvester determinant construction, then polynomial equality.
mat=S.zeros(m+n)
for i in range(n):
 for j,c in enumerate(fp.all_coeffs()):mat[i,i+j]=c
for i in range(m):
 for j,c in enumerate(hp.all_coeffs()):mat[n+i,i+j]=c
assert S.cancel(mat.det(method='domain-ge')-resultant)==0
const,factors=S.factor_list(resultant,u)
assert [(S.degree(f,u),mult)for f,mult in factors]==[(2,3),(6,1),(6,1),(24,1)]
assert S.expand(const*S.prod(f**mult for f,mult in factors)-resultant)==0

def trim(p):
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def primitive(p):
 den=1
 for x in p:den=lcm(den,x.denominator)
 vals=[int(x*den)for x in p];d=0
 for x in vals:d=gcd(d,abs(x))
 return [F(x//d)for x in vals]if d else [F(0)]

def rem(a,b):
 a=trim(a[:]);b=trim(b[:])
 while len(a)>=len(b) and any(a):
  c=a[-1]/b[-1];shift=len(a)-len(b)
  for j,x in enumerate(b):a[j+shift]-=c*x
  trim(a)
 return a

def variations(signs):
 nz=[1 if x>0 else -1 for x in signs if x]
 return sum(nz[i]!=nz[i-1]for i in range(1,len(nz)))

def sturm(poly):
 p=primitive([F(int(c.p),int(c.q))for c in reversed(S.Poly(poly,u).all_coeffs())])
 q=primitive([j*p[j]for j in range(1,len(p))]);seq=[p,q]
 while any(seq[-1]):
  r=primitive([-x for x in rem(seq[-2],seq[-1])])
  if not any(r):break
  seq.append(r)
 minus=variations([p[-1]*(-1)**(len(p)-1)for p in seq]);plus=variations([p[-1]for p in seq])
 return minus,plus,len(seq)

records=[]
for factor,mult in factors:
 left,right,count=sturm(factor);assert left==right
 records.append({'degree':int(S.degree(factor,u)),'multiplicity':int(mult),'polynomial':str(factor),
                 'sturm_minus_infinity':left,'sturm_plus_infinity':right,'sequence_length':count})
assert [(r['sturm_minus_infinity'],r['sturm_plus_infinity'])for r in records]==[(1,1),(3,3),(3,3),(12,12)]
out=ROOT/'frontier-20261028-ph7-asymmetric-cycle-89-resultant-certificate.json'
out.write_text(json.dumps({'z':'8/9','p':str(p),'q':str(q),
 'conditions':['E4=[y^4]R=0','E3=[y^3]R=0','E1=[y]R-2v[y^2]R=0'],
 'linear_w_eliminants':{'F':str(Fpoly),'H':str(Hpoly)},
 'resultant_coefficient':str(const),'factor_sturm_records':records,
 'checks':['full coefficient extraction','elimination identities without division',
           'Sylvester determinant equals resultant','exact factorization','pure Fraction Sturm count zero for each factor'],
 'scope':'all real U,V,W and all feedbacks for this 4U+W / 2V two-cycle spectral subfamily; not all PH7'},indent=2)+'\n')
print('SymPy',S.__version__,'plus independent Fraction Sturm PASS: four resultant factors have no real roots')
print('degrees/multiplicities:',[(r['degree'],r['multiplicity'])for r in records]);print('saved:',out)
