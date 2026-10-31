#!/usr/bin/env python3
"""Exact Gaussian-rational SR2 atoms with a bounded floating cone fit.

Only atom rank is exact. Fitted weights and residual are numerical and do not
certify a decomposition or the absence of one.
"""
from fractions import Fraction as F
from itertools import product
import json
import numpy as np

Z=(F(0),F(0)); O=(F(1),F(0)); SEED=20261028
OUT='frontier-20261028-grid-generic-gaussian-atoms-run-v1.json'

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(a,x): return (a[0]*x,a[1]*x)
def div(a,b):
    n=b[0]*b[0]+b[1]*b[1]
    if not n: raise ZeroDivisionError
    return ((a[0]*b[0]+a[1]*b[1])/n,(a[1]*b[0]-a[0]*b[1])/n)

def atom(alpha,beta,b,f):
    if alpha==Z or f==Z: raise ValueError
    v=(F(1,4),F(0)); lam=v
    d=sub(sub(mul(v,f),mul(alpha,b)),beta)
    c=div(sub(add(O,mul(v,f)),mul(beta,b)),alpha)
    e=sub(add(alpha,mul(beta,d)),mul(v,f))
    h=div(mul(lam,f),alpha)
    gamma=div(add(mul(lam,e),c),h)
    delta=sub(mul(v,e),mul(gamma,b))
    i=sub(add(mul(gamma,c),mul(delta,b)),mul(v,e))
    g=sub(add(gamma,mul(delta,d)),mul(v,e))
    rows=((O,b,c,h),(d,O,b,Z),
          (add(e,mul(v,f)),add(neg(d),mul(v,f)),add(O,mul(v,f)),mul(lam,f)),
          (add(g,mul(v,e)),mul(v,e),add(i,mul(v,e)),add(mul(lam,e),c)))
    for j in range(4):
        if rows[2][j]!=add(mul(alpha,rows[0][j]),mul(beta,rows[1][j])):
            raise AssertionError('row2 certificate')
        if rows[3][j]!=add(mul(gamma,rows[0][j]),mul(delta,rows[1][j])):
            raise AssertionError('row3 certificate')
    return (O,b,c,d,e,f,g,i,h)

def feature(m):
    out=list(np.diag(m).real)
    for i in range(9):
        for j in range(i+1,9): out.extend((m[i,j].real,m[i,j].imag))
    return np.array(out,dtype=np.float64)

def main():
    values=tuple((F(a,2),F(b,2)) for a in (-4,-2,-1,0,1,2,4)
                 for b in (-2,-1,0,1,2))
    rng=np.random.default_rng(SEED)
    rational=[];params=[]
    for j in range(1,9):
        rational.append(tuple(O if k==j else Z for k in range(9)))
        params.append(('basis',str(j)))
    seen=set()
    while len(seen)<3000:
        ps=tuple(values[int(x)] for x in rng.integers(0,len(values),size=4))
        if ps[0]==Z or ps[3]==Z or ps in seen: continue
        seen.add(ps); rational.append(atom(*ps));params.append(ps)
    columns=[]
    for xi in rational:
        x=np.array([complex(float(v[0]),float(v[1])) for v in xi]);x/=np.linalg.norm(x)
        columns.append(feature(np.outer(x,x.conj())))
    P=np.column_stack(columns)
    target=feature(np.diag([1,1,3,1,3,3,3,3,3]))
    L=np.linalg.norm(P,ord=2)**2
    x=np.zeros(len(rational));y=x.copy();t=1.0
    for _ in range(8000):
        new=np.maximum(0,y-(P.T@(P@y-target))/L)
        tn=(1+np.sqrt(1+4*t*t))/2
        y=new+((t-1)/tn)*(new-x);x=new;t=tn
    residual=P@x-target
    active=[]
    for j,w in enumerate(x):
        if w>1e-9:
            q=rational[j];norm2=sum(a*a+b*b for a,b in q)
            active.append({'parameters':str(params[j]),
                           'atom':[[str(a),str(b)] for a,b in q],
                           'coefficient_float':float(w/float(norm2))})
    result={'seed':SEED,'v0_v1_v2_lambda':['1/4']*4,
            'kernel_vector':['-1','-1','-1','4','-1'],
            'exact_atoms':len(rational),'fit_iterations':8000,
            'float_feature_residual_l2':float(np.linalg.norm(residual)),
            'float_relative_residual':float(np.linalg.norm(residual)/np.linalg.norm(target)),
            'positive_weights':len(active),'active_atoms':active,
            'limits':'Gaussian-rational row relations certify atoms only; fitted coefficients are FLOATING, not a state decomposition or no-go'}
    with open(OUT,'x',encoding='utf-8') as f: json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='active_atoms'},indent=2))


if __name__=='__main__': main()
