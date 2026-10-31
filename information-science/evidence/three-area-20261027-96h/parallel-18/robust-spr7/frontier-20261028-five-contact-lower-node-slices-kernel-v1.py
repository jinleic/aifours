# Exact fixed-w tensor slices for 27/4<=w<=15/2 with three active-bound
# branches. A failed Bernstein sign is only a failed fixed partition.
from fractions import Fraction as Q
from math import comb

def sub_low_sample(w,branch,x,z,y):
 umin=(9*w-36)/(6*w+25);ua=(3*w-16)/9;us=9*w/(8*w+27);cap=w/9
 if branch==1:u=(1-x)*umin+x*ua;low=(2+3*w)/(9*u+18);high=(w+3)/(u+9);den=(9*u+18)*(u+9)
 elif branch==2:u=(1-x)*ua+x*(w-6);low=Q(1);high=(w+3)/(u+9);den=u+9
 else:u=(1-x)*us+x*cap;low=Q(1);high=w/(9*u);den=9*u
 if low>high or den<=0:raise ValueError('BOUNDS')
 lam=(1-z)*low+z*high;v=(1-y)*(w+2)+y*7*w/5;vertices=bndry(u,lam,v,w)
 contacts=[(2,Q(1)),(3,Q(2)),(1,Q(3)),(0,Q(6)),(2,w)];T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 A=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(A);rhs=[-row[0]-1000*row[6]-row[7] for row in T];b=[Q(0)]*8
 b[0]=-D*den**3;b[6]=-1000*D*den**3;b[7]=-D*den**3
 for col,j in enumerate((1,2,3,4,5)):
  M=[[rhs[i] if k==col else A[i][k] for k in range(5)] for i in range(5)];b[j]=-det5(M)*den**3
 if not b[7]>0 or any(sum(row[j]*b[j] for j in range(8)) for row in T):raise ValueError('TANGENCY')
 vals=b[:];groups={i:[] for i in range(4)}
 for ci,t in contacts:groups[ci].append(t)
 for ci,a in enumerate(vertices):
  p=pairing_polynomial(a,b)
  for t in groups[ci]:p=quotient_by_root(quotient_by_root(p,t),t)
  for l,r in parts[ci]:vals.extend(beta(p,l,r))
 center=[sum(a[j] for a in vertices)/4 for j in range(8)];p=pairing_polynomial(center,b)
 for l,r in parts[4]:vals.extend(beta(p,l,r))
 return vals

def sub_low_slice(w,branch):
 xx=[Q(j,6) for j in range(7)];zz=[Q(j,3) for j in range(4)]
 IX=inverse([[Q(comb(6,k))*x**k*(1-x)**(6-k) for k in range(7)] for x in xx]);IZ=inverse([[Q(comb(3,k))*z**k*(1-z)**(3-k) for k in range(4)] for z in zz])
 vals=[[[sub_low_sample(w,branch,x,z,y) for y in zz] for z in zz] for x in xx];n=len(vals[0][0][0]);mins=[]
 for j in range(n):
  a1=[[[sum(IX[A][i]*vals[i][B][C][j] for i in range(7)) for C in range(4)] for B in range(4)] for A in range(7)]
  a2=[[[sum(IZ[B][b]*a1[A][b][C] for b in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  a3=[[[sum(IZ[C][c]*a2[A][B][c] for c in range(4)) for C in range(4)] for B in range(4)] for A in range(7)]
  mins.append(min(v for plane in a3 for row in plane for v in row))
 return {'w':str(w),'branch':branch,'all_positive':all(v>0 for v in mins),'minimum':str(min(mins)),'polynomials':n,'coefficients':112*n}
sub_slices=[]
for w in (Q(19,3),Q(27,4)):
 for branch in (1,2):sub_slices.append(sub_low_slice(w,branch))
print('sub-eight three-branch tensor slices:',sub_slices)
