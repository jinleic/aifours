# NONVERDICT float screen: exact rational band-root boxes, float simplex over
# normalized actual-corner atoms on a finite frequency grid. A negative LP value
# means only "no certificate on this grid"; it is not a positive theorem.
import random
from fractions import Fraction as F
import numpy as np
def cub(roots,lam):
 a,b,c=roots;return [lam*a*b*c,-lam*(a*b+a*c+b*c),lam*(a+b+c),-lam]
def sig(r):return r[0]+r[1]+r[2],r[0]*r[1]+r[0]*r[2]+r[1]*r[2],r[0]*r[1]*r[2]
def make_box(bands,Kc):
 (e1a,e1b),(o1a,o1b),(e2a,e2b),(o2a,o2b),(e3a,e3b),(o3a,o3b)=bands
 em,ep,om,op=(e1a,e2b,e3a),(e1b,e2a,e3b),(o1a,o2b,o3a),(o1b,o2a,o3b)
 s1m,s2m,s3m=sig(em);s1p,s2p,s3p=sig(ep);lo=max(F(1),s2p/s2m);hi=min(s1p/s1m,s3p/s3m)
 if lo>hi:return None
 a1,a2,a3=sig(om);b1,b2,b3=sig(op)
 if not(b1>=a1 and b2<=a2 and b3>=a3):return None
 K=lo+(hi-lo)*Kc;Em,Ep,Om,Op=cub(em,K),cub(ep,F(1)),cub(om,F(1)),cub(op,F(1))
 if not all(Ep[i]-Em[i]>=0 and Op[i]-Om[i]>=0 for i in range(4)):return None
 return dict(Em=Em,Ep=Ep,Om=Om,Op=Op,R=bands)
def ev(c,t):return c[0]+c[1]*t+c[2]*t*t+c[3]*t**3
def grid(b,n=14):
 ts=set()
 for a,c in b['R']:
  for i in range(n+1):ts.add(a+(c-a)*F(i,n))
  for i in range(1,n):
   g=F(round(float(a)*(float(c)/float(a))**(i/n)*10**6),10**6)
   if a<g<c:ts.add(g)
 R=b['R']
 for k in range(5):ts.add((R[k][1]+R[k+1][0])/2)
 ts.update({R[0][0]/2,R[-1][1]*2,R[-1][1]*10});return sorted(x for x in ts if x>0)
def columns(b,ts):
 Ec=[(b['Em'][i]+b['Ep'][i])/2 for i in range(4)];Oc=[(b['Om'][i]+b['Op'][i])/2 for i in range(4)];c=[float(x) for x in (Ec[0],Oc[0],-Ec[1],-Oc[1],Ec[2],Oc[2],-Ec[3],-Oc[3])];cols=[]
 for Ex in (b['Em'],b['Ep']):
  for Ox in (b['Om'],b['Op']):
   for t in ts:
    tf=float(t);E=float(ev(Ex,t));O=float(ev(Ox,t));Ecv=c[0]-c[2]*tf+c[4]*tf**2-c[6]*tf**3;Ocv=c[1]-c[3]*tf+c[5]*tf**2-c[7]*tf**3
    n=((E*E+tf*O*O)*(Ecv*Ecv+tf*Ocv*Ocv))**0.5
    cols.append([(E*(-tf)**(j//2) if j%2==0 else tf*O*(-tf)**((j-1)//2))*c[j]/n for j in range(8)])
 return np.array(cols).T
def lp(A,tol=1e-12):
 m,N=A.shape;nv=N+2+m;T=np.zeros((m+1,nv+1));T[:m,:N]=A;T[:m,N]=1;T[:m,N+1]=-1;T[:m,N+2:N+2+m]=np.eye(m);T[m,:N]=1;T[m,-1]=1
 v=(-A).min(axis=0);a0=int(np.argmax(v));jm=int(np.argmin(-A[:,a0]));basis=[N+2+j for j in range(m) if j!=jm]+[N if v[a0]>=0 else N+1,a0]
 T=np.linalg.inv(T[:,basis])@T;c=np.zeros(nv);c[N]=1;c[N+1]=-1
 for _ in range(5000):
  red=c-c[basis]@T[:,:nv];cand=[k for k in range(nv) if red[k]>tol and k not in basis]
  if not cand:
   x=np.zeros(nv);x[basis]=T[:,-1];return x[N]-x[N+1]
  k=min(cand);col=T[:,k];r=min((T[i,-1]/col[i],basis[i],i) for i in range(m+1) if col[i]>tol)[2];T[r]/=T[r,k]
  for i in range(m+1):
   if i!=r:T[i]-=T[i,k]*T[r]
  basis[r]=k
 return None
rng=random.Random(7);vals=[]
while len(vals)<100:
 e1a=F(rng.randint(30,70),100);e1b=e1a+F(rng.randint(1,30),100);o1a=e1b+F(rng.randint(1,20),1000);o1b=o1a*F(rng.randint(150,1000),100);e2a=o1b+F(rng.randint(1,20),1000);e2b=e2a*F(rng.randint(120,800),100);o2a=e2b*F(rng.randint(101,300),100);o2b=o2a*F(rng.randint(101,2000),100);e3a=o2b*F(rng.randint(101,300),100);e3b=e3a*F(rng.randint(101,3000),100);o3a=e3b*F(rng.randint(101,300),100);o3b=o3a*F(rng.randint(101,3000),100)
 b=make_box([(e1a,e1b),(o1a,o1b),(e2a,e2b),(o2a,o2b),(e3a,e3b),(o3a,o3b)],F(rng.randint(0,4),4))
 if b:vals.append(lp(columns(b,grid(b))))
print({'boxes':len(vals),'grid_certificates_found':sum(1 for v in vals if v is not None and v>0),'max_lp_value':max(v for v in vals if v is not None),'scope':'NONVERDICT float grid screen'})
