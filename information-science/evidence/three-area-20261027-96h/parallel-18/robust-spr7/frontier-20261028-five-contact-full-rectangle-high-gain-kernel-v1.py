# Exact bivariate Bernstein test of high-gain residual positivity over a
# continuous (lambda,v) rectangle with five fixed contact nodes. Tangent
# unknowns are Cramer polynomials; no numeric roots or floats.
from fractions import Fraction as Q
from math import comb
lamL,lamU=Q(52,45),Q(22,19);vL,vU=Q(10),Q(56,5)
z=[Q(j,3) for j in range(4)];BB=[[Q(comb(3,i))*x**i*(1-x)**(3-i) for i in range(4)] for x in z];Binv=inverse(BB)

def det5(A):return det(A)
def sample(lam,v):
 vertices=wide_boundary(lam,v);contacts=wide_contacts;T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];rhs=[-row[6] for row in T];D=det5(A)
 if not D:raise ValueError('SINGULAR')
 sign=1 if hg_det_sign>0 else -1;b=[Q(0)]*8;b[6]=sign*D
 for col,j in enumerate((1,2,3,4,5)):
  C=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=sign*det5(C)
 if b[6]<=0:raise ValueError('DETERMINANT_SIGN')
 vals=b[1:7];mapping={i:[] for i in range(4)}
 for ci,t in contacts:mapping[ci].append(t)
 for ci,a in enumerate(vertices):
  P=pairing_polynomial(a,b);res=quotient_by_root(P,Q(0))
  for t in mapping[ci]:res=quotient_by_root(quotient_by_root(res,t),t)
  for left,right in hgparts[ci]:vals.extend(beta(res,left,right))
 return vals
# Determine determinant sign at the separately certified reference.
baseT=ht;AA=[[row[j] for j in (1,2,3,4,5)] for row in baseT];hg_det_sign=det5(AA)
if not hg_det_sign:raise ValueError('REFERENCE_DETERMINANT')
samples=[[sample(lamL+(lamU-lamL)*x,vL+(vU-vL)*y) for y in z] for x in z]
size=len(samples[0][0])
if not all(len(v)==size for row in samples for v in row):raise ValueError('DIMENSIONS')
mins=[]
for j in range(size):
 coeff=[[sum(Binv[a][i]*Binv[b][k]*samples[i][k][j] for i in range(4) for k in range(4)) for b in range(4)] for a in range(4)]
 mins.append(min(min(row) for row in coeff))
wide_bivariate={'lambda_interval':[str(lamL),str(lamU)],'v_interval':[str(vL),str(vU)],'parameter_polynomials':size,'bernstein_coefficients':16*size,
 'all_positive':all(v>0 for v in mins),'minimum':str(min(mins)),'frequency_leaf_counts':[len(x) for x in hgparts]}
print('full rectangle high-gain condition:',wide_bivariate)
