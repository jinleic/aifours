#!/usr/bin/env python3
"""Exact polynomial identity for all rank-four input compressions.

Named public prior art: Sang-Jun Park, arXiv:2602.09860v1, Theorem 1.2.
This script checks the explicit Choi decomposition modulo s^2+lambda^2=1,
plus integer identities for the separate 6x6 PPT source/witness pair. It is
not a proof assistant and does not establish a global 4x4 nonexistence result.
"""
import json

# Ring Z[lambda,s]/(s^2+lambda^2-1), represented by (lambda_power,s_power).
def reduce_poly(p):
    q = {}
    todo = list(p.items())
    while todo:
        (a, b), v = todo.pop()
        if not v:
            continue
        if b >= 2:
            todo.append(((a, b-2), v))
            todo.append(((a+2, b-2), -v))
        else:
            q[(a,b)] = q.get((a,b), 0) + v
    return {k:v for k,v in q.items() if v}

def add(a,b):
    c = dict(a)
    for k,v in b.items():
        c[k] = c.get(k,0) + v
    return reduce_poly(c)

def scale(a,c):
    return reduce_poly({k:c*v for k,v in a.items()})

def mul(a,b):
    c = {}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            c[(i+k,j+l)] = c.get((i+k,j+l),0) + x*y
    return reduce_poly(c)

one={(0,0):1}; lam={(1,0):1}; s={(0,1):1}; zero={}
n=24

def vec(terms):
    v=[{} for _ in range(n)]
    for i,p,c in terms:
        v[6*i+p]=add(v[6*i+p],c)
    return v

def vadd(a,b):
    return [add(x,y) for x,y in zip(a,b)]

def vscale(a,c):
    return [mul(x,c) for x in a]

def matrix():
    return [[{} for _ in range(n)] for _ in range(n)]

def outer_into(M,v,c=1):
    nz=[i for i,x in enumerate(v) if x]
    for i in nz:
        for j in nz:
            M[i][j]=add(M[i][j],scale(mul(v[i],v[j]),c))

def partial_transpose_input(M):
    out=matrix()
    for i in range(4):
        for p in range(6):
            for j in range(4):
                for q in range(6):
                    out[6*j+p][6*i+q]=M[6*i+p][6*j+q]
    return out

def add_matrix(dst,src,c=1):
    for i in range(n):
        for j in range(n):
            dst[i][j]=add(dst[i][j],scale(src[i][j],c))

# Zero-based canonical basis: a=01-10, b=23-32, c=24-35, q=25+34.
a=vec([(0,1,one),(1,0,scale(one,-1))])
b=vec([(2,3,one),(3,2,scale(one,-1))])
c=vec([(2,4,one),(3,5,scale(one,-1))])
q=vec([(2,5,one),(3,4,one)])
u=[a,b,c]; w=[one,lam,s]
jU=vadd(vadd(a,vscale(b,lam)),vscale(c,s))
C=matrix()
for i in range(n):C[i][i]=scale(one,2)
for i in range(4):
    for j in range(4):
        C[6*i+j][6*j+i]=add(C[6*i+j][6*j+i],scale(one,-2))
outer_into(C,jU,-1)
P=matrix()
for i in range(3):
    for j in range(i+1,3):
        x=vadd(vscale(u[j],w[i]),vscale(u[i],scale(w[j],-1)))
        outer_into(P,x)
for i in range(4):
    for j in range(i+1,4):
        if (i,j) not in ((0,1),(2,3)):
            x=vec([(i,j,one),(j,i,scale(one,-1))])
            outer_into(P,x,2)
for i in (0,1):
    for p in (4,5):
        outer_into(P,vec([(i,p,one)]),2)
Q=matrix();outer_into(Q,q)
add_matrix(P,partial_transpose_input(Q),2)
assert all(not add(C[i][j],scale(P[i][j],-1)) for i in range(n) for j in range(n))

# Source/witness: j=vec(J), R=I+F+[j], W=2I-2F-[j].
d=6;N=d*d
J=[[0]*d for _ in range(d)]
for i in range(3):J[i][i+3]=1;J[i+3][i]=-1
j=[J[i][p] for i in range(d) for p in range(d)]
R=[[int(i==k)+int(i//d==k%d and i%d==k//d)+j[i]*j[k] for k in range(N)] for i in range(N)]
W=[[2*int(i==k)-2*int(i//d==k%d and i%d==k//d)-j[i]*j[k] for k in range(N)] for i in range(N)]
trace=sum(R[i][i] for i in range(N))
pair=sum(W[i][k]*R[k][i] for i in range(N) for k in range(N))
assert trace==48 and pair==-12
Rgamma=[[R[(i//d)*d+(k%d)][(k//d)*d+(i%d)] for k in range(N)] for i in range(N)]
omega=[int(i//d==i%d) for i in range(N)]
G=[[J[i%d][k//d]*J[k%d][i//d] for k in range(N)] for i in range(N)]
assert all(Rgamma[i][k] == int(i==k)+omega[i]*omega[k]+G[i][k] for i in range(N) for k in range(N))
assert all(G[i][k]==G[k][i] for i in range(N) for k in range(N))
assert all(sum(G[i][t]*G[t][k] for t in range(N))==int(i==k) for i in range(N) for k in range(N))
print(json.dumps({
    "canonical_Choi_dimension": 24,
    "all_variable_integer_polynomial_identity": "passed modulo s^2+lambda^2-1 for all 576 matrix entries",
    "decomposition": "C_U = sum of explicit PSD outer products + 2[q]^Gamma_input",
    "six_by_six_source_trace": trace,
    "six_by_six_pairing": pair,
    "source_partial_transpose_identity_and_Q_involution": "passed exactly",
    "scope": "Exact algebra supporting the written canonical-form proof; no formal proof-assistant verification and no global 4x4 conclusion."
},indent=2))
