#!/usr/bin/env python3
"""Exact two-defect check of the general symplectic compression decomposition.

Named public prior art: Sang-Jun Park, arXiv:2602.09860v1, Theorem 1.2.
Polynomial coefficients are integers; the proof for general k,d is written
in the accompanying packet. No formal verification or 4x4 no-go is claimed.
"""
import json

# Z[l1,l2,s1,s2]/(s1^2+l1^2-1,s2^2+l2^2-1).
def red(p):
    out={}; todo=list(p.items())
    while todo:
        e,v=todo.pop()
        if not v:continue
        done=False
        for l,s in ((0,2),(1,3)):
            if e[s]>=2:
                a=list(e);a[s]-=2
                b=a[:];b[l]+=2
                todo.append((tuple(a),v));todo.append((tuple(b),-v))
                done=True;break
        if not done:out[e]=out.get(e,0)+v
    return {e:v for e,v in out.items() if v}
def add(a,b):
    r=dict(a)
    for e,v in b.items():r[e]=r.get(e,0)+v
    return red(r)
def scale(a,c):return red({e:c*v for e,v in a.items()})
def mul(a,b):
    out={}
    for ea,x in a.items():
        for eb,y in b.items():
            e=tuple(i+j for i,j in zip(ea,eb));out[e]=out.get(e,0)+x*y
    return red(out)
def variable(i):
    e=[0]*4;e[i]=1;return {tuple(e):1}
one={(0,0,0,0):1};l1,l2,s1,s2=[variable(i) for i in range(4)]
r=4;d=8;N=r*d

def vec(terms):
    a=[{} for _ in range(N)]
    for i,p,v in terms:a[i*d+p]=add(a[i*d+p],v)
    return a
def vadd(a,b):return [add(x,y) for x,y in zip(a,b)]
def vscale(a,c):return [mul(x,c) for x in a]
def matrix():return [[{} for _ in range(N)] for _ in range(N)]
def outer_into(M,v,c=1):
    nz=[i for i,x in enumerate(v) if x]
    for i in nz:
        for j in nz:M[i][j]=add(M[i][j],scale(mul(v[i],v[j]),c))
def add_matrix(A,B,c=1):
    for i in range(N):
        for j in range(N):A[i][j]=add(A[i][j],scale(B[i][j],c))
def pt_in(A):
    B=matrix()
    for i in range(r):
        for p in range(d):
            for j in range(r):
                for q in range(d):B[j*d+p][i*d+q]=A[i*d+p][j*d+q]
    return B

a1=vec([(0,1,one),(1,0,scale(one,-1))])
a2=vec([(2,3,one),(3,2,scale(one,-1))])
c1=vec([(0,4,one),(1,5,scale(one,-1))])
c2=vec([(2,6,one),(3,7,scale(one,-1))])
q1=vec([(0,5,one),(1,4,one)])
q2=vec([(2,7,one),(3,6,one)])
u=[a1,a2,c1,c2];w=[l1,l2,s1,s2]
j=[{} for _ in range(N)]
for x,y in zip(u,w):j=vadd(j,vscale(x,y))
C=matrix()
for i in range(N):C[i][i]=scale(one,2)
for i in range(r):
    for j0 in range(r):C[i*d+j0][j0*d+i]=add(C[i*d+j0][j0*d+i],scale(one,-2))
outer_into(C,j,-1)
P=matrix()
for i in range(len(u)):
    for j0 in range(i+1,len(u)):
        x=vadd(vscale(u[j0],w[i]),vscale(u[i],scale(w[j0],-1)))
        outer_into(P,x)
for i in range(r):
    for j0 in range(i+1,r):
        if (i,j0) not in ((0,1),(2,3)):
            outer_into(P,vec([(i,j0,one),(j0,i,scale(one,-1))]),2)
for i in range(r):
    for p in range(r,d):
        if not (i in (0,1) and p in (4,5)) and not (i in (2,3) and p in (6,7)):
            outer_into(P,vec([(i,p,one)]),2)
for q in (q1,q2):
    M=matrix();outer_into(M,q);add_matrix(P,pt_in(M),2)
assert all(not add(C[i][j],scale(P[i][j],-1)) for i in range(N) for j in range(N))
print(json.dumps({"dimension":N,"defective_symplectic_pairs":2,
                  "integer_polynomial_identity":"all 1024 entries, modulo s1^2+l1^2=1 and s2^2+l2^2=1",
                  "scope":"Exact identity only; general theorem uses the accompanying written canonical-form argument."},indent=2))
