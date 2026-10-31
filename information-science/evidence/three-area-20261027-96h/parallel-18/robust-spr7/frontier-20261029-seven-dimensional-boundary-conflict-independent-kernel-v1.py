# Independent direct factor, monomial tangent, rank and two-point sign replay
# for a seven-generator boundary obstruction. No optimizer is imported.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261029-seven-dimensional-boundary-conflict-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='a7bb7609a5fdfe05a8821363e8f6a498b286c3068759fcd77f24466760a8afa5':raise ValueError('PIN')
f=json.loads(raw);sh=f['shape'];ts=list(map(F,sh['nodes']));u=F(sh['u']);v=F(sh['v']);lam=F(sh['lambda'])
if not 0<u<ts[0]<ts[1]<ts[2]<ts[3]<ts[4]<v:raise ValueError('ORDER')
def cubic(rs,scale):
 p=[-scale]
 for r in rs:
  q=[F(0)]*(len(p)+1)
  for i,x in enumerate(p):q[i]-=r*x;q[i+1]+=x
  p=q
 return p
Em=cubic([u,ts[2],ts[3]],lam);Ep=cubic([ts[0],ts[1],ts[4]],F(1));Om=cubic([ts[0],ts[3],ts[4]],F(1));Op=cubic([ts[1],ts[2],v],F(1))
lo=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]];hi=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]]
if list(map(str,lo))!=f['boundary_lower'] or list(map(str,hi))!=f['boundary_upper'] or not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('WIDTH')
def mk(e,o):return [e[0],o[0],-e[1],-o[1],e[2],o[2],-e[3],F(1)]
cs=[mk(Em,Om),mk(Em,Op),mk(Ep,Om),mk(Ep,Op)];mid=[(lo[j]+hi[j])/2 for j in range(7)]+[F(1)];ds=[mid]
for _ in range(3):ds.append([F(j+1)*ds[-1][j+1] for j in range(7)]+[F(0)])
G=[[cs[2*k][j] if j%2==0 else F(0) for j in range(8)] for k in (0,1)]+[[cs[k][j] if j%2 else F(0) for j in range(8)] for k in (0,1)]+ds[1:4]
def det(A):
 n=len(A);den=lcm(*(v.denominator for row in A for v in row));M=[[int(v*den) for v in row] for row in A];prev=1;sgn=1
 for k in range(n-1):
  if not M[k][k]:
   p=next((i for i in range(k+1,n) if M[i][k]),None)
   if p is None:return F(0)
   M[p],M[k]=M[k],M[p];sgn=-sgn
  p=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=M[i][j]*p-M[i][k]*M[k][j]
    if v%prev:raise ValueError('BAREISS')
    M[i][j]=v//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sgn*M[-1][-1],den**n)
def pair(a,b,t,derivative=False):
 z=F(0)
 for i in range(8):
  for j in range(8):
   if (i+j)%2:continue
   k=(i+j)//2;v=a[i]*b[j]*(1 if ((j-i)//2)%2==0 else -1)
   if derivative:
    if k:z+=v*k*t**(k-1)
   else:z+=v*t**k
 return z
ct=[(2,ts[0]),(3,ts[1]),(1,ts[2]),(0,ts[3]),(2,ts[4])];T=[]
for ci,t in ct:
 if any(pair(cs[ci],g,t)!=0 for g in G):raise ValueError('CONTACT')
 T.append([pair(cs[ci],g,t,True) for g in G])
tdet=det([r[:5] for r in T]);gdet=det([[G[j][i] for j in range(7)] for i in range(7)])
if tdet!=F(f['tangent_rank_minor']) or gdet!=F(f['generator_rank_minor']) or not(tdet and gdet):raise ValueError('RANK')
U=list(map(F,f['U']));V=list(map(F,f['V']));UC=list(map(F,f['U_generators']));VC=list(map(F,f['V_generators']))
if U[7]!=1 or V[7]!=0 or not all(sum(UC[k]*G[k][j] for k in range(7))==U[j] and sum(VC[k]*G[k][j] for k in range(7))==V[j] for j in range(8)):raise ValueError('NULLSPACE')
if any(sum(T[i][k]*UC[k] for k in range(7)) or sum(T[i][k]*VC[k] for k in range(7)) for i in range(5)):raise ValueError('TANGENCY')
P=[[pair(cs[int(ci)],g,F(t)) for g in (U,V)] for ci,t in f['physical_pair_nodes']];cross=P[0][0]*P[1][1]-P[1][0]*P[0][1]
if [[str(x) for x in r] for r in P]!=f['physical_pair_rows'] or cross!=F(f['conflict_determinant']) or not(P[0][1]>0>P[1][1] and cross>0):raise ValueError('CONFLICT')
print('boundary seven-span independent replay:',{'positive_widths':7,'contact_tangent_rank':5,'generator_rank':7,'nullspace_basis_leading':[str(U[7]),str(V[7])],'pairing_direction_signs':['+','-'],'strict_conflict':True,'scope':'no boundary nonzero numerator in seven-generator span with nonnegative leading coefficient can have all pairings nonnegative'})
