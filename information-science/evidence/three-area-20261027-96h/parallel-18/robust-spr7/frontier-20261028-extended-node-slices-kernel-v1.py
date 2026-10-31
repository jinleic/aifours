# Exact exploratory full-shape tensor slices at w=10,12,15,17. A negative
# Bernstein coefficient only means this fixed leaf certificate is inconclusive.
from fractions import Fraction as Q
from math import comb
def binv2(n):
 z=[Q(j,n) for j in range(n+1)];return z,inverse([[Q(comb(n,k))*x**k*(1-x)**(n-k) for k in range(n+1)] for x in z])
xx,Ix=binv2(6);zz,Iz=binv2(3);yy,Iy=binv2(3);extended_slices=[]
for w in (Q(10),Q(12),Q(15),Q(17)):
 for branch in (1,2):
  samples=[[[node_sample(w,branch,x,z,y) for y in yy] for z in zz] for x in xx];n=len(samples[0][0][0]);mins=[]
  for j in range(n):
   a1=[[[sum(Ix[A][i]*samples[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
   a2=[[[sum(Iz[B][b]*a1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   a3=[[[sum(Iy[C][c]*a2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   mins.append(min(v for plane in a3 for row in plane for v in row))
  extended_slices.append({'w':str(w),'branch':branch,'parameter_polynomials':n,'bernstein_coefficients':112*n,'all_positive':all(v>0 for v in mins),'minimum':str(min(mins))})
print('extended exact node slices:',extended_slices)
