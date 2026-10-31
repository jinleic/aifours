# Exact bivariate Bernstein search for one fixed gain valid on the whole
# high-gain parameter rectangle. Cramer determinants clear denominators.
from fractions import Fraction as Q
from math import comb

def refine_union(*arrs):
 endpoints=sorted({x for arr in arrs for seg in arr for x in seg})
 return [(endpoints[j],endpoints[j+1]) for j in range(len(endpoints)-1)]
origparts=[[(Q(z['left']),Q(z['right'])) for z in pr['leaves']] for pr in five_frozen['boundary_proofs']]
parts=[refine_union(hgparts[i],origparts[i]) for i in range(4)]
center0=[(Q(l)+Q(u))/2 for l,u in zip(five_frozen['boundary_lower'],five_frozen['boundary_upper'])]+[Q(1)]
cbase=[(Q(z['left']),Q(z['right'])) for z in five_frozen['center_proof']['leaves']]
centerparts=refine_union(cbase,*parts);parts.append(centerparts)

def gain_sample(lam,v,gain):
 vertices=wide_boundary(lam,v);contacts=wide_contacts;center=[sum(a[j] for a in vertices)/4 for j in range(8)];T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(A);sgn=1 if hg_det_sign>0 else -1
 if not sgn*D>0:raise ValueError('DET_SIGN')
 rhs=[-row[0]-gain*row[6]-row[7] for row in T];b=[Q(0)]*8;b[0]=sgn*D;b[6]=sgn*D*gain;b[7]=sgn*D
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=sgn*det5(M)
 if any(sum(row[j]*b[j] for j in range(8)) for row in T):raise ValueError('TANGENCY')
 vals=b[:];groups={i:[] for i in range(4)}
 for ci,t in contacts:groups[ci].append(t)
 for ci,a in enumerate(vertices):
  p=pairing_polynomial(a,b)
  for t in groups[ci]:p=quotient_by_root(quotient_by_root(p,t),t)
  for left,right in parts[ci]:vals.extend(beta(p,left,right))
 cp=pairing_polynomial(center,b)
 for left,right in parts[4]:vals.extend(beta(cp,left,right))
 return vals

zg=[Q(j,3) for j in range(4)];B3=[[Q(comb(3,i))*x**i*(1-x)**(3-i) for i in range(4)] for x in zg];BI=inverse(B3)
wide_uniform_gain=[]
for gain in (1000,10000,100000,1000000,10000000,100000000):
 samples=[[gain_sample(lamL+(lamU-lamL)*x,vL+(vU-vL)*y,Q(gain)) for y in zg] for x in zg];size=len(samples[0][0]);mins=[]
 if not all(len(v)==size for row in samples for v in row):raise ValueError('DIMENSION')
 for j in range(size):
  coeff=[[sum(BI[a][i]*BI[b][k]*samples[i][k][j] for i in range(4) for k in range(4)) for b in range(4)] for a in range(4)]
  mins.append(min(v for row in coeff for v in row))
 rec={'gain':gain,'parameter_polynomials':size,'parameter_coefficients':16*size,'min':str(min(mins)),
      'frequency_leaf_counts':[len(v) for v in parts]}
 if all(v>0 for v in mins):rec['status']='UNIFORM_GAIN_CERTIFIED';wide_uniform_gain.append(rec);break
 rec['status']='SIGN_NOT_CERTIFIED';wide_uniform_gain.append(rec)
print('full rectangle uniform gain bivariate:',wide_uniform_gain)
