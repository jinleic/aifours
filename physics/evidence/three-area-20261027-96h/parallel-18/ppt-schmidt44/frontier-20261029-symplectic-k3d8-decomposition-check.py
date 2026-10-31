#!/usr/bin/env python3
"""Exact k=3,d=8 compression identity over Z[lambda,s]/(lambda^2+s^2-1).

Prior-art map family: Sang-Jun Park, https://arxiv.org/html/2602.09860v1.
This finite arithmetic check does not prove the all-k written theorem.
"""
import json

def reduce_poly(p):
    out={};todo=list(p.items())
    while todo:
        (a,b),v=todo.pop()
        if not v:continue
        if b>=2:
            todo.append(((a,b-2),v));todo.append(((a+2,b-2),-v))
        else:out[(a,b)]=out.get((a,b),0)+v
    return {k:v for k,v in out.items() if v}
def add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+v
    return reduce_poly(c)
def scale(a,c):return reduce_poly({k:c*v for k,v in a.items()})
def mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():c[(i+k,j+l)]=c.get((i+k,j+l),0)+x*y
    return reduce_poly(c)
one={(0,0):1};lam={(1,0):1};s={(0,1):1}
k=3;r=2*k;d=8;N=r*d

def vec(terms):
    v=[{} for _ in range(N)]
    for i,p,c in terms:v[d*i+p]=add(v[d*i+p],c)
    return v
def vadd(a,b):return [add(x,y) for x,y in zip(a,b)]
def vscale(a,c):return [mul(x,c) for x in a]
def matrix():return [[{} for _ in range(N)] for _ in range(N)]
def outer_into(M,v,c=1):
    nz=[i for i,x in enumerate(v) if x]
    for i in nz:
        for j in nz:M[i][j]=add(M[i][j],scale(mul(v[i],v[j]),c))
def addmat(A,B,c=1):
    for i in range(N):
        for j in range(N):A[i][j]=add(A[i][j],scale(B[i][j],c))
def pt_in(A):
    B=matrix()
    for i in range(r):
        for p in range(d):
            for j in range(r):
                for q in range(d):B[j*d+p][i*d+q]=A[i*d+p][j*d+q]
    return B

antis=[]
for x in range(k):
    i,j=2*x,2*x+1
    antis.append(vec([(i,j,one),(j,i,scale(one,-1))]))
c=vec([(4,6,one),(5,7,scale(one,-1))])
h=vec([(4,7,one),(5,6,one)])
u=antis+[c];w=[one,one,lam,s]
jU=[{} for _ in range(N)]
for x,y in zip(u,w):jU=vadd(jU,vscale(x,y))
C=matrix()
for i in range(N):C[i][i]=scale(one,k)
for i in range(r):
    for j in range(r):C[i*d+j][j*d+i]=add(C[i*d+j][j*d+i],scale(one,-k))
outer_into(C,jU,-1)
P=matrix()
for i in range(len(u)):
    for j in range(i+1,len(u)):
        x=vadd(vscale(u[j],w[i]),vscale(u[i],scale(w[j],-1)))
        outer_into(P,x)
for i in range(r):
    for j in range(i+1,r):
        if (i,j) not in ((0,1),(2,3),(4,5)):
            outer_into(P,vec([(i,j,one),(j,i,scale(one,-1))]),k)
for i in range(r):
    for p in range(r,d):
        if i not in (4,5):outer_into(P,vec([(i,p,one)]),k)
Q=matrix();outer_into(Q,h);addmat(P,pt_in(Q),k)
assert all(not add(C[i][j],scale(P[i][j],-1)) for i in range(N) for j in range(N))
print(json.dumps({'k':3,'d':8,'compression_dimension':N,
                  'integer_polynomial_identity':'all 2304 entries modulo lambda^2+s^2=1',
                  'scope':'finite odd-k check only; general result uses written proof'},indent=2))
