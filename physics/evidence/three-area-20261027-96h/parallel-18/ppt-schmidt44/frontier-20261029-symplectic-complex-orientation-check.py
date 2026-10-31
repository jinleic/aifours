#!/usr/bin/env python3
"""Exact Gaussian-integer check of Choi/local-unitary orientation.

Park map prior art: https://arxiv.org/html/2602.09860v1. The finite check
is supplementary to the all-d algebra, not a proof-assistant verification.
"""
import json

Z=(0,0);O=(1,0);I=(0,1)
def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def mat(n,m):return [[Z for _ in range(m)] for _ in range(n)]
def adj(A):return [[conj(A[i][j]) for i in range(len(A))] for j in range(len(A[0]))]
def mm(A,B):
    C=mat(len(A),len(B[0]))
    for i in range(len(A)):
        for k in range(len(B)):
            if A[i][k]!=Z:
                for j in range(len(B[0])):
                    C[i][j]=plus(C[i][j],mul(A[i][k],B[k][j]))
    return C
def outer(v):return [[mul(v[i],conj(v[j])) for j in range(len(v))] for i in range(len(v))]
d=4;N=d*d
J=mat(d,d)
J[0][1]=O;J[1][0]=(-1,0);J[2][3]=I;J[3][2]=(0,-1)
assert all(J[j][i]==(-J[i][j][0],-J[i][j][1]) for i in range(d) for j in range(d))
assert mm(adj(J),J)==[[O if i==j else Z for j in range(d)] for i in range(d)]
U=mat(N,N);F=mat(N,N)
for i in range(d):
    for p in range(d):
        F[d*i+p][d*p+i]=O
        for q in range(d):U[d*i+p][d*i+q]=J[p][q]
Udag=adj(U);omega=[O if i//d==i%d else Z for i in range(N)]
j=[conj(J[i][p]) for i in range(d) for p in range(d)]
jwrong=[J[i][p] for i in range(d) for p in range(d)]
rotated_omega=[sum_gauss for sum_gauss in [Z]*N]
for i in range(N):
    for a in range(N):rotated_omega[i]=plus(rotated_omega[i],mul(Udag[i][a],omega[a]))
assert rotated_omega==j
assert outer(j)!=outer(jwrong)
assert mm(mm(Udag,outer(omega)),U)==outer(j)
twisted=mm(mm(U,F),Udag)
assert mm(mm(Udag,twisted),U)==F
jj=outer(j);pt=mat(N,N)
for a in range(d):
    for b in range(d):
        for c in range(d):
            for e in range(d):pt[d*a+e][d*c+b]=jj[d*a+b][d*c+e]
# K0=conjugate(J), so conjugate(K0)=J and [j]^Gamma=(I tensor J)F(I tensor J*).
assert pt==twisted
print(json.dumps({'dimension':d,'J_original':'diag(J2,i J2)',
                  'rotated_Omega_equals_vec_conjugate_J':True,
                  'wrong_unconjugated_projector_differs':True,
                  'rotated_identity_Choi_and_twisted_swap':'exact Gaussian integer identities',
                  'source_partial_transpose_orientation':'exact Gaussian integer identity',
                  'scope':'One finite supplementary orientation check; general proof is the written index identity.'},indent=2))
