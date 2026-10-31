#!/usr/bin/env python3
"""Exact independent symbolic check of all-c normalization for PH7 band.

Computes the same seven-state matrix from its explicit rate definitions using
rational SymPy expressions, constructs h by recursion, checks every actual row
equation and the initial probability identity for symbolic c,z. No numerical
sampling, model inference, or external source is used.
"""
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as sp
from itertools import combinations
c,z=sp.symbols('c z',positive=True)
u1,u2,u3,v1,v2,v3=map(sp.Rational,['657/500','34/25','701/500','333/250','973/1000','1083/1000'])
rates=(u1,u2,u3,v1,v2,v3)
e={k:sum(sp.prod(t) for t in combinations(rates,k)) for k in range(1,7)}
a,b,c3,e4,e5,e6=(e[k] for k in range(1,7))
h0=b+4*a-a*a-6; L=b-4*a+10-2*z; N=4*h0+4-c3-b*(4-a)-4*z
p=N/L;q=(a-4)*p+h0-2*z;w=p+4-a;B=p-u1-u2;C0=q-u1*u2-u1*B
phi=e4+c3*w-((6+2*z)*q+(4+4*z)*p+(1+z)**2)
R2=e5+e4*w-(4+4*z)*q-(1+z)**2*p;R1=e6+e5*w-(1+z)**2*q;R0=e6*w
D1=R2-phi*(u1+u2+u3)
D2=R1-phi*(u1*u2+u1*u3+u2*u3)-(v2+v3)*D1
D3=R0-phi*u1*u2*u3-v2*v3*D1-v3*D2
G=sp.zeros(7)
for i,x in enumerate((u1,u2,u3,w,v1,v2,v3)):G[i,i]=-x
for i,j in ((0,1),(1,2),(2,3),(3,4),(4,5),(5,6)):G[i,j]=1
G[4,0],G[5,0],G[6,0],G[6,3]=D1,D2,D3,phi
Q=c*c+p*c+q; K=c*((c+1)**2+z)**2
h1=1/Q;h2=(c+u1)*h1;h3=(c+u2)*h2;h4=(c+u3)*h3
h7=(K+D3*h1+phi*h4)/(c+v3);h6=(h7+D2*h1)/(c+v2);h5=(h6+D1*h1)/(c+v1)
h=sp.Matrix([h1,h2,h3,h4,h5,h6,h7]);gamma=sp.Matrix([0,0,0,0,0,0,K])
beta=sp.Matrix([[C0,B,1,0,0,0,0]])
res=[sp.cancel(x) for x in ((c*sp.eye(7)-G)*h-gamma)]
assert res==[0]*7,res
assert sp.cancel((beta*h)[0]-1)==0
# Alpha and exit expressions are definitions; the spectral, sign and interval
# premises are checked by the separate complete symbolic determinant/positivity
# certificate, not assumed from a numerical experiment here.
report={'rates':[str(x) for x in rates],
        'symbolic_checks':['all seven equations (cI-G)h=K e7 identically in c,z',
                           'beta h=1 identically in c,z'],
        'h_definition':['1/Q(c)','(c+u1)/Q(c)','(c+u1)(c+u2)/Q(c)',
                        '(c+u1)(c+u2)(c+u3)/Q(c)',
                        '(h6+D1 h1)/(c+v1)','(h7+D2 h1)/(c+v2)',
                        '(K+D3 h1+phi h4)/(c+v3)'],
        'scope':'symbolic normalization only; positivity and spectral claims require the companion band certificate'}
out=ROOT/'frontier-20261028-ph7-seven-band-normalizer-certificate.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print('SymPy',sp.__version__,'all 7 row equations and beta*h=1 symbolic assertions PASS')
print('saved:',out)
