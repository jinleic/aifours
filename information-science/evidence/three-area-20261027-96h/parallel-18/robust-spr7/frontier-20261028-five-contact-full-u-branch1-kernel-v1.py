# Exact trivariate Bernstein certificate for u in [36/73,72/91],
# z in [0,1], v in [10,56/5], lambda=(1-z)*26/(9u+18)+z*11/(u+9).
# Multiply Cramer numerator by the positive denominator cubed; bidegrees are
# <=(6,3,3) for every pairing/leaf and <= those bounds for coefficients.
from fractions import Fraction as Q
from math import comb
U0,U1=Q(36,73),Q(72,91);V0,V1=Q(10),Q(56,5);gain=Q(1000)

def boundary_u(u,lam,v):
 E0=root_cubic([u,Q(3),Q(6)],lam);E1=root_cubic([Q(1),Q(2),Q(8)],Q(1));O0=root_cubic([Q(1),Q(6),Q(8)],Q(1));O1=root_cubic([Q(2),Q(3),v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]

def sample_full(u,z,v):
 den=(9*u+18)*(u+9);lam=(1-z)*Q(26)/(9*u+18)+z*Q(11)/(u+9);vertices=boundary_u(u,lam,v);T=[]
 for ci,t in wide_contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(A);rhs=[-row[0]-gain*row[6]-row[7] for row in T];b=[Q(0)]*8
 b[0]=-D*den**3;b[6]=-D*den**3*gain;b[7]=-D*den**3
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=-det5(M)*den**3
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

def B_inv(n):
 z=[Q(j,n) for j in range(n+1)];M=[[Q(comb(n,k))*x**k*(1-x)**(n-k) for k in range(n+1)] for x in z]
 return z,inverse(M)
zu,Iu=B_inv(6);zz,Iz=B_inv(3);zv,Iv=B_inv(3)
samples=[[[sample_full(U0+(U1-U0)*x,y,V0+(V1-V0)*z) for z in zv] for y in zz] for x in zu];n=len(samples[0][0][0]);mins=[]
if not all(len(v)==n for plane in samples for row in plane for v in row):raise ValueError('DIMENSION')
for j in range(n):
 a1=[[[sum(Iu[A][i]*samples[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
 a2=[[[sum(Iz[B][b]*a1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
 a3=[[[sum(Iv[C][c]*a2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
 mins.append(min(v for plane in a3 for row in plane for v in row))
branch1={'u_interval':[str(U0),str(U1)],'z_interval':['0','1'],'v_interval':[str(V0),str(V1)],'gain':str(gain),'parameter_degrees':[6,3,3],
 'parameter_polynomials':n,'parameter_bernstein_coefficients':112*n,'all_positive':all(v>0 for v in mins),'minimum':str(min(mins)),'frequency_leaf_counts':[len(x) for x in parts]}
print('full-u branch1 Bernstein:',branch1)
