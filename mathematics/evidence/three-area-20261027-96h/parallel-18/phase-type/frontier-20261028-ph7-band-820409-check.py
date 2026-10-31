#!/usr/bin/env python3
"""Exact 7-state PH construction on [7/9,820409/1000000].

No float is used for theorem checks: symbolic determinant/numerator/normalizer
identities use SymPy QQ(z,c,y), and all Bernstein signs use Fraction.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from math import comb
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp
m=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
z,y,c=sp.symbols('z y c',real=True);m.Z=z
rates=list(map(sp.Rational,['669/500','1339/1000','671/500','669/500','1043/1000','1041/1000']))
u1,u2,u3,v1,v2,v3=rates;v=m.rational_family(rates)
G=sp.zeros(7)
for i,r in enumerate([u1,u2,u3,v['w'],v1,v2,v3]):G[i,i]=-r
for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)):G[i,j]=1
G[4,0],G[5,0],G[6,0],G[6,3]=v['D1'],v['D2'],v['D3'],v['phi']
M=y*sp.eye(7)-G;Q=y*y+v['p']*y+v['q'];Dz=y*((y+1)**2+z)**2
assert sp.cancel(M.det(method='domain-ge')-Dz*Q)==0
beta=sp.Matrix([[v['C0'],v['B'],1,0,0,0,0]]);e7=sp.Matrix([0,0,0,0,0,0,1])
assert sp.cancel((M+e7*beta).det(method='domain-ge')-M.det(method='domain-ge')-Q)==0
Qc=c*c+v['p']*c+v['q'];K=c*((c+1)**2+z)**2
h1=1/Qc;h2=(c+u1)*h1;h3=(c+u2)*h2;h4=(c+u3)*h3
h7=(K+v['D3']*h1+v['phi']*h4)/(c+v3);h6=(h7+v['D2']*h1)/(c+v2);h5=(h6+v['D1']*h1)/(c+v1)
h=sp.Matrix([h1,h2,h3,h4,h5,h6,h7])
assert all(sp.cancel(x)==0 for x in (c*sp.eye(7)-G)*h-K*e7)
assert sp.cancel((beta*h)[0]-1)==0

def as_fraction(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def bern(poly,lo,hi):
    p=sp.Poly(sp.cancel(poly),z);cs=[as_fraction(x) for x in reversed(p.all_coeffs())];n=len(cs)-1;w=hi-lo
    a=[sum(cs[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
lo=F(7,9);hi=F(820409,1000000);L=v['L'];coeff={}
for name in ('L','p','q','w','B','C0','phi','D1','D2','D3'):
    q=L if name=='L' else sp.cancel(v[name]*L)
    assert sp.denom(q)==1
    a=bern(q,lo,hi);assert all(x>0 for x in a),(name,a)
    coeff[name]=[str(x) for x in a]
report={'z_interval':[str(lo),str(hi)],'rates':[str(x) for x in rates],
 'rational_coefficients':{k:str(sp.factor(x)) for k,x in v.items()},
 'positive_Bernstein_coefficients_L_and_L_times_others':coeff,
 'checks':['full actual7x7 determinant D_z Q','actual adjugate numerator Q',
           'all seven symbolic (cI-G)h=K e7 equations','symbolic beta*h=1',
           'strict positivity of L and all physical coefficients on the entire closed interval'],
 'scope':'actual PH7 upper construction for all c,d>0, z on stated interval; not full PH7 optimal endpoint'}
out=ROOT/'frontier-20261028-ph7-band-820409-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'Fraction exact determinant/numerator/normalizer/Bernstein assertions PASS')
for k,vv in coeff.items():print(k,'degree',len(vv)-1,'min',min(map(F,vv)))
print('saved:',out)
