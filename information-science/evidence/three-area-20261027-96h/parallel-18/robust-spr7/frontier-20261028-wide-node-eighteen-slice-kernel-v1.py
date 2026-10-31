# Exact full-u,z,v tensor slices at one new fifth contact w=17/2.
# A positive slice does not by itself prove the w interval between slices.
from fractions import Fraction as Q
from math import comb
w=Q(18)
def binv(n):
 z=[Q(j,n) for j in range(n+1)];return z,inverse([[Q(comb(n,k))*x**k*(1-x)**(n-k) for k in range(n+1)] for x in z])
zu,Iu=binv(6);zz,Iz=binv(3);zv,Iv=binv(3);wide_slice=[]
for branch in (1,2):
 samples=[[[node_sample(w,branch,x,z,y) for y in zv] for z in zz] for x in zu];n=len(samples[0][0][0]);mins=[]
 if not all(len(v)==n for plane in samples for row in plane for v in row):raise ValueError('DIMENSION')
 for j in range(n):
  a1=[[[sum(Iu[A][i]*samples[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
  a2=[[[sum(Iz[B][b]*a1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  a3=[[[sum(Iv[C][c]*a2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  mins.append(min(v for plane in a3 for row in plane for v in row))
 wide_slice.append({'w':str(w),'branch':branch,'parameter_polynomials':n,'parameter_coefficients':112*n,'all_positive':all(v>0 for v in mins),'minimum':str(min(mins))})
print('w=18 refined exact tensor slices:',wide_slice)
