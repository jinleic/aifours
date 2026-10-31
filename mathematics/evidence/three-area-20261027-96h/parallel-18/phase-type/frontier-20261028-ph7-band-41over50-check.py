#!/usr/bin/env python3
"""Exact symbolic certificate for an actual PH7 band through 41/50.

Six rational chain rates define the actual matrix. Full polynomial determinant,
actual adjugate numerator, all-seven all-c normalizer equations and every
coefficient sign on the closed z interval are checked over exact rationals.
"""
from fractions import Fraction as F
from importlib.machinery import SourceFileLoader
from math import comb
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp
m=SourceFileLoader('nu',str(ROOT/'frontier-20261028-ph7-nonuniform-search.py')).load_module()
z,y,c=sp.symbols('z y c',real=True);m.Z=z
rates=list(map(sp.Rational,['1331/1000','341/250','1339/1000','33/25','257/250','132/125']))
u1,u2,u3,v1,v2,v3=rates
v=m.rational_family(rates)
G=sp.zeros(7)
for i,r in enumerate([u1,u2,u3,v['w'],v1,v2,v3]):G[i,i]=-r
for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)):G[i,j]=1
G[4,0],G[5,0],G[6,0],G[6,3]=v['D1'],v['D2'],v['D3'],v['phi']
M=y*sp.eye(7)-G; Q=y*y+v['p']*y+v['q']; Dz=y*((y+1)**2+z)**2
assert sp.cancel(M.det(method='domain-ge')-Dz*Q)==0
beta=sp.Matrix([[v['C0'],v['B'],1,0,0,0,0]]);e7=sp.Matrix([0,0,0,0,0,0,1])
assert sp.cancel((M+e7*beta).det(method='domain-ge')-M.det(method='domain-ge')-Q)==0
Qc=c*c+v['p']*c+v['q'];K=c*((c+1)**2+z)**2
h1=1/Qc;h2=(c+u1)*h1;h3=(c+u2)*h2;h4=(c+u3)*h3
h7=(K+v['D3']*h1+v['phi']*h4)/(c+v3);h6=(h7+v['D2']*h1)/(c+v2);h5=(h6+v['D1']*h1)/(c+v1)
h=sp.Matrix([h1,h2,h3,h4,h5,h6,h7])
assert all(sp.cancel(x)==0 for x in (c*sp.eye(7)-G)*h-K*e7)
assert sp.cancel((beta*h)[0]-1)==0

def frac(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def bern(poly,lo,hi):
    p=sp.Poly(sp.cancel(poly),z);cs=[frac(x) for x in reversed(p.all_coeffs())];n=len(cs)-1;w=hi-lo
    a=[sum(cs[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
lo=F(7,9);hi=F(41,50); L=v['L']; cert={}
for name in ('L','p','q','w','B','C0','phi','D1','D2','D3'):
    expr=L if name=='L' else sp.cancel(v[name]*L)
    assert sp.denom(expr)==1
    co=bern(expr,lo,hi);assert all(x>0 for x in co),(name,co)
    cert[name]=[str(x) for x in co]
report={'z_interval':[str(lo),str(hi)],'rates':[str(x) for x in rates],
 'rational_coefficients':{k:str(sp.factor(x)) for k,x in v.items()},
 'positive_Bernstein_coefficients_L_and_L_times_others':cert,
 'checks':['all coefficients of actual 7x7 determinant D_z*Q','actual adjugate numerator Q',
           'all seven (cI-G)h=K e7 equations symbolically','beta*h=1 symbolically',
           'strict positivity of L and every physical coefficient on full closed band'],
 'scope':'actual PH7 upper construction for all c,d>0, z in interval; not all-topology endpoint'}
out=ROOT/'frontier-20261028-ph7-band-41over50-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'Fraction exact determinant/numerator/normalizer/Bernstein assertions PASS')
for name,co in cert.items(): print(name,'degree',len(co)-1,'min',min(map(F,co)))
print('saved:',out)
