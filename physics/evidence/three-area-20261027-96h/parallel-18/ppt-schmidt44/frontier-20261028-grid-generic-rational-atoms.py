#!/usr/bin/env python3
"""Numerical cone fitting from exactly rational SR<=2 projected-range atoms.

The atoms have exact Fraction row certificates, but fitted weights/residuals
are FLOATING and cannot establish a decomposition without separate rational
weight reconstruction. The one local map is not a general 4x4 test.
"""
from fractions import Fraction as F
from itertools import product
import json
import numpy as np


VALUES=(F(-2),F(-1),F(-1,2),F(0),F(1,2),F(1),F(2))
OUT='frontier-20261028-grid-generic-rational-atoms-run-v1.json'


def atom(alpha,beta,b,f):
    if not alpha or not f: raise ValueError
    v0=v1=v2=lam=F(1,4)
    a=F(1)
    d=v1*f-alpha*b-beta
    c=(1+v2*f-beta*b)/alpha
    e=alpha+beta*d-v0*f
    h=lam*f/alpha
    gamma=(lam*e+c)/h
    delta=v1*e-gamma*b
    i=gamma*c+delta*b-v2*e
    g=gamma+delta*d-v0*e
    rows=((a,b,c,h),(d,a,b,F(0)),
          (e+v0*f,-d+v1*f,a+v2*f,lam*f),
          (g+v0*e,v1*e,i+v2*e,lam*e+c))
    for j in range(4):
        if rows[2][j]!=alpha*rows[0][j]+beta*rows[1][j]:
            raise AssertionError('row2 certificate')
        if rows[3][j]!=gamma*rows[0][j]+delta*rows[1][j]:
            raise AssertionError('row3 certificate')
    return (a,b,c,d,e,f,g,i,h)


def feature(m):
    out=list(np.diag(m))
    for i in range(9):
        for j in range(i+1,9): out.append(m[i,j])
    return np.array(out,dtype=np.float64)


def main():
    rational=[]; params=[]; columns=[]
    for j in range(1,9):
        xi=tuple(F(int(k==j)) for k in range(9))
        rational.append(xi);params.append(('basis',str(j)))
    for a,b,c,d in product(VALUES,repeat=4):
        if not a or not d: continue
        xi=atom(a,b,c,d)
        rational.append(xi);params.append(tuple(map(str,(a,b,c,d))))
    for xi in rational:
        x=np.array([float(v) for v in xi]); x/=np.linalg.norm(x)
        columns.append(feature(np.outer(x,x)))
    P=np.column_stack(columns)
    target=feature(np.diag([1,1,3,1,3,3,3,3,3]))
    L=np.linalg.norm(P,ord=2)**2
    x=np.zeros(len(rational)); y=x.copy(); t=1.0
    for _ in range(10000):
        new=np.maximum(0,y-(P.T@(P@y-target))/L)
        tn=(1+np.sqrt(1+4*t*t))/2
        y=new+((t-1)/tn)*(new-x);x=new;t=tn
    residual=P@x-target
    active=[]
    for j,w in enumerate(x):
        if w>1e-9:
            q=rational[j];norm2=sum(v*v for v in q)
            active.append({'parameters':params[j], 'atom':[str(v) for v in q],
                           'coefficient_float':float(w/float(norm2))})
    result={'source':'https://arxiv.org/html/2509.07086v1 Eq.11',
            'v0_v1_v2_lambda':['1/4']*4,'kernel_vector':['-1','-1','-1','4','-1'],
            'grid_values':[str(v) for v in VALUES], 'exact_atoms':len(rational),
            'fit_iterations':10000,'float_feature_residual_l2':float(np.linalg.norm(residual)),
            'float_relative_residual':float(np.linalg.norm(residual)/np.linalg.norm(target)),
            'positive_weights':len(active),'active_atoms':active,
            'limits':'Fraction row identities certify atom rank; weights/fit are floating only, not a state decomposition or no-go'}
    with open(OUT,'x',encoding='utf-8') as f: json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!='active_atoms'},indent=2))


if __name__=='__main__': main()
