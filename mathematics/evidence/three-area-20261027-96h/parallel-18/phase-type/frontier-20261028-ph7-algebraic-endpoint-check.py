#!/usr/bin/env python3
"""Exact algebraic endpoint for one actual nonuniform PH7 family.

Proves all non-phi coefficients positive on [7/9,82041/100000], phi*L
strictly decreasing there and opposite signs at the two rational endpoint
brackets. Checks full matrix identities and normalizer for symbolic c,y,z.
No float, numerical root solver or unreviewed data is used in the proof.
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
hv=sp.Matrix([h1,h2,h3,h4,h5,h6,h7])
assert all(sp.cancel(x)==0 for x in (c*sp.eye(7)-G)*hv-K*e7)
assert sp.cancel((beta*hv)[0]-1)==0

def frac(x):return F(int(sp.numer(x)),int(sp.denom(x)))
def bern(poly,lo,hi):
    p=sp.Poly(sp.cancel(poly),z);cs=[frac(x) for x in reversed(p.all_coeffs())];n=len(cs)-1;w=hi-lo
    a=[sum(cs[i]*comb(i,j)*lo**(i-j)*w**j for i in range(j,n+1)) for j in range(n+1)]
    return [sum(a[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)) for k in range(n+1)]
lo=F(7,9); a=F(820409,1000000); b=F(82041,100000);L=v['L'];positive={}
for name in ('L','p','q','w','B','C0','D1','D2','D3'):
    expression=L if name=='L' else sp.cancel(v[name]*L)
    assert sp.denom(expression)==1
    cs=bern(expression,lo,b);assert all(x>0 for x in cs),(name,cs)
    positive[name]=[str(x) for x in cs]
Fphi=sp.cancel(v['phi']*L); assert sp.denom(Fphi)==1
D=bern(sp.diff(Fphi,z),lo,b); assert all(x<0 for x in D)
A=frac(Fphi.subs(z,sp.Rational(a.numerator,a.denominator)))
B=frac(Fphi.subs(z,sp.Rational(b.numerator,b.denominator)))
assert A>0 and B<0
report={'rates':[str(x) for x in rates],'interval_for_non_phi_signs':[str(lo),str(b)],
 'root_bracket':[str(a),str(b)],'L_times_phi':str(sp.factor(Fphi)),
 'Lphi_at_bracket':[str(A),str(B)],'negative_bernstein_coefficients_of_derivative':[str(x) for x in D],
 'positive_Bernstein_coefficients_for_L_and_other_L_scaled_entries':positive,
 'checks':['symbolic full 7x7 determinant and actual numerator',
           'all seven normalizer rows and beta h=1 symbolic',
           'all non-phi physical entries positive over enlarged interval',
           'L*phi strictly decreasing and opposite signs at rational bracket'],
 'scope':'unique algebraic endpoint for this explicit nonuniform PH7 family; no all-topology optimality'}
out=ROOT/'frontier-20261028-ph7-algebraic-endpoint-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'Fraction exact identities/signs/unique-root assertions PASS')
print('bracket signs',A,B);print('negative derivative Bernstein',', '.join(map(str,D)))
for name,arr in positive.items():print(name,'min',min(map(F,arr)))
print('saved:',out)
