# Exact tensor Bernstein test: vary the first E- root u as well as lambda,v.
# Cramer and pairings have degree <=3 in EACH parameter. Gain fixed at 1000.
from fractions import Fraction as Q
from math import comb
uL,uU=Q(1,2),Q(51,100);lL,lU=Q(1040009,900000),Q(109999049,95100000);vL,vU=Q(10),Q(56,5)
z=[Q(j,3) for j in range(4)];BM=[[Q(comb(3,k))*x**k*(1-x)**(3-k) for k in range(4)] for x in z];BI=inverse(BM)

def boundary3(u,lam,v):
 E0=root_cubic([u,Q(3),Q(6)],lam);E1=root_cubic([Q(1),Q(2),Q(8)],Q(1));O0=root_cubic([Q(1),Q(6),Q(8)],Q(1));O1=root_cubic([Q(2),Q(3),v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)) or not (lo[0]<hi[0] and lo[1]<hi[1]):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]

def sample3(u,lam,v):
 vertices=boundary3(u,lam,v);T=[]
 for ci,t in wide_contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(A);rhs=[-row[0]-1000*row[6]-row[7] for row in T];b=[Q(0)]*8;b[0]=-D;b[6]=-1000*D;b[7]=-D
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=-det5(M)
 if not b[7]>0 or any(sum(row[j]*b[j] for j in range(8)) for row in T):raise ValueError('TANGENCY')
 vals=b[:];groups={i:[] for i in range(4)}
 for ci,t in wide_contacts:groups[ci].append(t)
 for ci,a in enumerate(vertices):
  p=pairing_polynomial(a,b)
  for t in groups[ci]:p=quotient_by_root(quotient_by_root(p,t),t)
  for l,r in parts[ci]:vals.extend(beta(p,l,r))
 center=[sum(v[j] for v in vertices)/4 for j in range(8)];cp=pairing_polynomial(center,b)
 for l,r in parts[4]:vals.extend(beta(cp,l,r))
 return vals
samples=[[[sample3(uL+(uU-uL)*x,lL+(lU-lL)*y,vL+(vU-vL)*z0) for z0 in z] for y in z] for x in z];n=len(samples[0][0][0])
if not all(len(v)==n for plane in samples for row in plane for v in row):raise ValueError('DIMENSION')
mins=[]
for j in range(n):
 tmp1=[[[sum(BI[a][i]*samples[i][q][r][j] for i in range(4)) for r in range(4)] for q in range(4)] for a in range(4)]
 tmp2=[[[sum(BI[b][q]*tmp1[a][q][r] for q in range(4)) for r in range(4)] for b in range(4)] for a in range(4)]
 coeff=[[[sum(BI[c][r]*tmp2[a][b][r] for r in range(4)) for c in range(4)] for b in range(4)] for a in range(4)]
 mins.append(min(v for plane in coeff for row in plane for v in row))
tri_gain={'u_interval':[str(uL),str(uU)],'lambda_interval':[str(lL),str(lU)],'v_interval':[str(vL),str(vU)],'gain':1000,
 'parameter_polynomials':n,'parameter_bernstein_coefficients':64*n,'all_positive':all(v>0 for v in mins),'minimum':str(min(mins)),
 'frequency_leaf_counts':[len(x) for x in parts]}
print('trivariate uniform gain:',tri_gain)
