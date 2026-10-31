from fractions import Fraction as F
from itertools import combinations
import json

D=16
J=[[0]*4 for _ in range(4)]
J[0][2]=J[1][3]=1
J[2][0]=J[3][1]=-1
FJ=[[0]*D for _ in range(D)]
FL=[[0]*D for _ in range(D)]
for i in range(4):
    for j in range(4):
        FL[4*j+i][4*i+j]=1
        for k in range(4):
            for l in range(4):
                FJ[4*k+l][4*i+j]=J[j][k]*J[l][i]
I=[[int(i==j) for j in range(D)] for i in range(D)]
P=[[F(int(i//4==i%4 and j//4==j%4),4) for j in range(D)] for i in range(D)]
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
def eq(A,B): return all(A[i][j]==B[i][j] for i in range(D) for j in range(D))
def pt(A): return [[A[4*(i//4)+j%4][4*(j//4)+i%4] for j in range(D)] for i in range(D)]
def C(p,q):
    return [[F(1-p-q,16)*I[i][j]+p*P[i][j]+F(q,4)*FJ[i][j] for j in range(D)] for i in range(D)]
def expectation(A,v): return sum(v[i]*A[i][j]*v[j] for i in range(D) for j in range(D))
def vector(terms):
    v=[0]*D
    for i,j,a in terms:v[4*i+j]=a
    return v
probes=[
  vector([(0,1,1),(3,2,1)]),
  vector([(0,0,1),(2,2,1)]),
  vector([(0,0,1),(1,1,1)]),
  vector([(0,1,1),(3,2,-1)]),
]
for v in probes:
    M=[v[4*i:4*i+4] for i in range(4)]
    minors2=[M[a][c]*M[b][d]-M[a][d]*M[b][c] for a,b in combinations(range(4),2) for c,d in combinations(range(4),2)]
    minors3=[]
    for rows in combinations(range(4),3):
      for cols in combinations(range(4),3):
        a,b,c=[[M[r][s] for s in cols] for r in rows]
        minors3.append(a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]))
    assert any(minors2) and not any(minors3)
assert eq(matmul(FJ,FJ),I)
assert eq(matmul(P,P),P)
assert eq(matmul(FJ,P),[[-P[i][j] for j in range(D)] for i in range(D)])
forms=[]
for v in probes:
    e0=expectation(C(F(0),F(0)),v)
    ep=expectation(C(F(1),F(0)),v)-e0
    eq_=expectation(C(F(0),F(1)),v)-e0
    forms.append([str(8*e0),str(8*ep),str(8*eq_)])
assert forms==[['1','-1','-5'],['1','7','-5'],['1','7','-1'],['1','-1','3']]
pminus=[[F(I[i][j]-FJ[i][j],2) for j in range(D)] for i in range(D)]
pplus=[[F(I[i][j]+FJ[i][j],2) for j in range(D)] for i in range(D)]
assert eq(matmul(pminus,pminus),pminus) and eq(matmul(pplus,pplus),pplus)
assert eq(C(F(1),F(0)),P)
assert eq(C(F(0),F(1,5)),[[pplus[i][j]/10 for j in range(D)] for i in range(D)])
assert eq(C(F(-1,5),F(-2,5)),[[(pminus[i][j]-P[i][j])/5 for j in range(D)] for i in range(D)])
assert eq(pt(C(F(-1,7),F(0))),[[F(2*I[i][j]-FL[i][j],28) for j in range(D)] for i in range(D)])
V=[(F(1),F(0)),(F(0),F(1,5)),(F(-1,7),F(0)),(F(-1,5),F(-2,5))]
def inequalities(p,q): return [1-p-5*q,1+7*p-5*q,1+7*p-q,1-p+3*q]
for p,q in V: assert all(x>=0 for x in inequalities(p,q))
print(json.dumps({'rank2_probe_forms_8_times_unnormalized_expectation':forms,'four_projector_and_vertex_matrix_identities_checked':True,'all_256_entries_each':True,'plus_projector_rank':sum(pplus[i][i] for i in range(D)),'minus_minus_P_rank':str(sum((pminus[i][i]-P[i][i]) for i in range(D))),'vertices':[list(map(str,x)) for x in V]},default=str,indent=2))
