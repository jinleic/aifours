# Exact diagnostic at one changed fifth contact w=8.000001. The general local
# existence proof uses continuity, not these finite parameter-corner checks.
from fractions import Fraction as Q

def node_bounds(w):return (9*w-36)/(6*w+25),9*w/(8*w+27),w/(w+1)
def node_boundary(u,lam,v,w):
 E0=root_cubic([u,Q(3),Q(6)],lam);E1=root_cubic([Q(1),Q(2),w],Q(1));O0=root_cubic([Q(1),Q(6),w],Q(1));O1=root_cubic([Q(2),Q(3),v],Q(1))
 lo=[E0[0],O0[0],-E1[1],-O1[1],E0[2],O0[2],-E1[3]];hi=[E1[0],O1[0],-E0[1],-O0[1],E1[2],O1[2],-E0[3]]
 if not all(0<lo[j]<=hi[j] for j in range(7)):raise ValueError('WIDTH')
 def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],Q(1)]
 return [mk(E0,O0),mk(E0,O1),mk(E1,O0),mk(E1,O1)]

def node_sample(w,branch,x,z,y):
 a,b,c=node_bounds(w);u=(1-x)*a+x*b if branch==1 else (1-x)*b+x*c
 lo=(2+3*w)/(9*u+18);up=(w+3)/(u+9) if branch==1 else w/(9*u)
 den=(9*u+18)*(u+9) if branch==1 else (9*u+18)*(9*u)
 if lo>up or den<=0:raise ValueError('BOUNDS')
 lam=(1-z)*lo+z*up;v=(1-y)*(w+2)+y*(7*w/5);vertices=node_boundary(u,lam,v,w)
 contacts=[(2,Q(1)),(3,Q(2)),(1,Q(3)),(0,Q(6)),(2,w)];T=[]
 for ci,t in contacts:
  a=vertices[ci];ep=-a[2]+2*a[4]*t-3*a[6]*t*t;op=-a[3]+2*a[5]*t-3*t*t
  T.append([ep*(-t)**(j//2) if j%2==0 else t*op*(-t)**((j-1)//2) for j in range(8)])
 M=[[row[j] for j in (1,2,3,4,5)] for row in T];D=det5(M);rhs=[-row[0]-1000*row[6]-row[7] for row in T];b=[Q(0)]*8;b[0]=-D*den**3;b[6]=-1000*D*den**3;b[7]=-D*den**3
 for col,j in enumerate((1,2,3,4,5)):
  A=[[rhs[i] if k==col else M[i][k] for k in range(5)] for i in range(5)];b[j]=-det5(A)*den**3
 if any(sum(row[j]*b[j] for j in range(8)) for row in T):raise ValueError('TANGENCY')
 vals=b[:];groups={i:[] for i in range(4)}
 for ci,t in contacts:groups[ci].append(t)
 for ci,a in enumerate(vertices):
  p=pairing_polynomial(a,b)
  for t in groups[ci]:p=quotient_by_root(quotient_by_root(p,t),t)
  for l,r in parts[ci]:vals.extend(beta(p,l,r))
 center=[sum(a[j] for a in vertices)/4 for j in range(8)];p=pairing_polynomial(center,b)
 for l,r in parts[4]:vals.extend(beta(p,l,r))
 return vals
w=Q(8000001,1000000);samples=[]
for branch in (1,2):
 for x in (Q(0),Q(1)):
  for z in (Q(0),Q(1)):
   for y in (Q(0),Q(1)):
    vals=node_sample(w,branch,x,z,y);samples.append({'branch':branch,'x':str(x),'z':str(z),'y':str(y),'count':len(vals),'min':str(min(vals)),'positive':all(v>0 for v in vals)})
print('shifted fifth-contact exact parameter vertices:',{'w':str(w),'corners':len(samples),'all_positive':all(s['positive'] for s in samples),'minimum':str(min(Q(s['min']) for s in samples))})
