# Exact (w,x,z,y) tensor test on w in [19/3,27/4] for a fixed branch.
# After positive Q(w)^6 clearing, every frequency-leaf/center/numerator
# parameter polynomial has degree <=(23,6,3,3). Test all Bernstein coefficients.
from fractions import Fraction as Q
from math import comb

def invbern(deg):
 z=[Q(j,deg) for j in range(deg+1)]
 A=[[Q(comb(deg,k))*x**k*(1-x)**(deg-k) for k in range(deg+1)] for x in z]
 return z,inverse(A)
wg,Iw=invbern(23);xg,Ix=invbern(6);zg,Iz=invbern(3);yg,Iy=invbern(3)
parts=[[(Q(l),Q(r)) for l,r in arr] for arr in node_interval_frozen['frequency_leaves']]
ii=parts[3].index((Q(7,8),Q(1)));parts[3][ii:ii+1]=[(Q(7,8),Q(15,16)),(Q(15,16),Q(1))]

def certify_lower_node_branch(branch):
 layers=[]
 for zw in wg:
  w=Q(19,3)+Q(5,12)*zw;clear=lowQ(w,branch)**6
  samples=[[[sub_low_sample(w,branch,x,z,y) for y in yg] for z in zg] for x in xg];n=len(samples[0][0][0]);values=[]
  if not all(len(v)==n for plane in samples for row in plane for v in row):raise ValueError('DIMENSION')
  for j in range(n):
   a1=[[[sum(Ix[A][i]*samples[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
   a2=[[[sum(Iz[B][b]*a1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   a3=[[[sum(Iy[C][c]*a2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
   values.extend(v*clear for plane in a3 for row in plane for v in row)
  layers.append(values)
 if not all(len(v)==len(layers[0]) for v in layers):raise ValueError('LAYERS')
 minimum=None;negative=0
 for j in range(len(layers[0])):
  coeff=[sum(Iw[k][i]*layers[i][j] for i in range(24)) for k in range(24)];mn=min(coeff)
  if mn<=0:negative+=1
  if minimum is None or mn<minimum:minimum=mn
 return {'branch':branch,'w_interval':['19/3','27/4'],'degrees':[23,6,3,3],'shape_polynomials':n,
  'shape_bernstein_coefficients':len(layers[0]),'full_tensor_coefficients':24*len(layers[0]),
  'all_positive':negative==0,'nonpositive_fibers':negative,'minimum':str(minimum)}
lower_node_branch1=certify_lower_node_branch(1)
print('lower-node interval branch1:',lower_node_branch1)
