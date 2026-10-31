#!/usr/bin/env python3
"""Exact Bernstein covers for three universal 8/9 amplification bounds.

Uses symbolic construction and integer Bernstein subdivision. The four-cone
blowup resolves the simultaneous infinite-rate/theta=1 corner. The JSON is a
replayable finite certificate; it is not an independent audit or PH witness.
"""
from fractions import Fraction
from itertools import product
from math import comb,lcm
from pathlib import Path
import hashlib,json,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'frontier-20261028-localdeps'))
import sympy as S

z=S.Rational(8,9);r=S.symbols('r0:3');theta=S.symbols('theta')
u=S.symbols('u0:4');scalevar=S.symbols('s');v=S.symbols('v0:3')
a=[x-1 for x in r];prod_r=S.prod(r)
real=S.prod(a)-z*sum(a)-theta*prod_r
imag=a[0]*a[1]+a[0]*a[2]+a[1]*a[2]-z
norm=real**2+z*imag**2


def transfer_polynomial(visited,bound2):
    numerator=(1-theta)**2*S.prod(x*x for x in r[:visited])*S.prod((x-1)**2+z for x in r[visited:])
    return S.Poly(S.expand(bound2*norm-numerator),*r,theta)


def compact(poly):
    expr=0
    for ex,c in poly.terms():
        term=c
        for i in range(3):term*=u[i]**ex[i]*(1-u[i])**(2-ex[i])
        term*=u[3]**ex[3]
        expr+=term
    return S.Poly(S.expand(expr),*u)


def blowup(poly,pivot):
    it=iter(v);ep=[scalevar if i==pivot else scalevar*next(it) for i in range(4)]
    expanded=S.Poly(S.expand(poly.as_expr().subs({u[i]:1-ep[i] for i in range(4)})),scalevar,*v)
    assert all(key[0]>=2 for key in expanded.monoms())
    return S.Poly(S.cancel(expanded.as_expr()/scalevar**2),scalevar,*v)


def quadratic_bound():
    h,eta,H=S.symbols('h eta H');v2=h*h*eta/3
    den=((h-1)**2-z+v2)**2+4*z*(h-1)**2
    p=S.Poly(S.expand(S.Rational(225,16)*den-(h*h+v2)**2),h,eta)
    expr=sum(c*H**ex[0]*(1-H)**(4-ex[0])*eta**ex[1] for ex,c in p.terms())
    return S.Poly(S.expand(expr),H,eta)


def digest(poly):
    rows=[[list(key),str(value)] for key,value in sorted(poly.as_dict().items())]
    return hashlib.sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()


def grid(poly):
    ds=poly.degree_list();den=lcm(*[int(c.q) for c in poly.coeffs()])
    weight=den
    for d in ds:weight*=lcm(*[comb(d,j)for j in range(d+1)])
    A=np.zeros(tuple(d+1 for d in ds),dtype=object)
    for ex,c in poly.terms():
        divisor=1
        for d,i in zip(ds,ex):divisor*=comb(d,i)
        assert weight%divisor==0
        base=c*(weight//divisor);assert base.q==1;base=int(base)
        for key in product(*(range(i,d+1)for i,d in zip(ex,ds))):
            val=base
            for k,i in zip(key,ex):val*=comb(k,i)
            A[key]+=val
    return A


def split(A,axis):
    A=np.moveaxis(A,axis,0);d=A.shape[0]-1;levels=[A]
    while len(levels[-1])>1:levels.append(levels[-1][:-1]+levels[-1][1:])
    left=np.stack([levels[k][0]*(1<<(d-k))for k in range(d+1)])
    right=np.stack([levels[d-k][-1]*(1<<k)for k in range(d+1)])
    return np.moveaxis(left,0,axis),np.moveaxis(right,0,axis)


def certify(poly):
    n=len(poly.gens);stack=[('',grid(poly))];leaves=[]
    while stack:
        path,A=stack.pop()
        if min(A.flat)>=0:leaves.append(path);continue
        assert len(path)<40,('depth limit',path)
        a,b=split(A,len(path)%n);stack.append((path+'1',b));stack.append((path+'0',a))
    return sorted(leaves)

records=[]
for name,m,bound2 in [('full3',3,S.Rational(16)),('partial2',2,S.Rational(45369,10000))]:
    pc=compact(transfer_polynomial(m,bound2))
    for pivot in range(4):
        poly=blowup(pc,pivot);leaves=certify(poly)
        records.append({'name':name,'pivot':pivot,'degrees':list(poly.degree_list()),'sha256':digest(poly),'leaves':leaves})
        print(name,'pivot',pivot,'leaves',len(leaves),flush=True)
poly=quadratic_bound();leaves=certify(poly)
records.append({'name':'quadratic','degrees':list(poly.degree_list()),'sha256':digest(poly),'leaves':leaves})
print('quadratic leaves',len(leaves),flush=True)
out=ROOT/'frontier-20261028-ph7-length-six-amplification-certificate-v1.json'
out.write_text(json.dumps({'z':'8/9','full3_squared_bound':'16','partial2_squared_bound':'45369/10000',
 'quadratic_squared_bound':'225/16','split_axis':'depth modulo dimension',
 'blowup':'compact u_i=rate/(1+rate), theta; eps_i=1-u_i; choose max eps pivot=s, others=s*v; divide polynomial by s^2',
 'records':records},indent=2)+'\n')
print('PASS: exact integer Bernstein cover, saved',out)
