# Independent factor expansion, integer-Bareiss stability, direct monomial
# obstruction, and dyadic Bernstein positive-pairing replay.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import lcm,comb
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
raw=(root/'frontier-20261028-lifted-simple-no-family-frozen-v1.json').read_bytes()
if sha256(raw).hexdigest()!='64a15a865f342f47beb94146503f67ee235acf53f15b905bb95e7c0427908800':raise ValueError('PIN')
f=json.loads(raw)
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
factor=[F(1)]
for _ in range(5):factor=mul(factor,[F(200),F(1)])
lower=mul(factor,list(map(F,f['lower_quadratic'])));upper=mul(factor,list(map(F,f['upper_quadratic'])));atom=mul(factor,list(map(F,f['second_atom_quadratic'])));b=mul(factor,list(map(F,f['good_quadratic'])))
if list(map(str,lower[:7]))!=f['lower'] or list(map(str,upper[:7]))!=f['upper'] or list(map(str,atom))!=f['second_atom'] or list(map(str,b))!=f['good_numerator']:raise ValueError('EXPANSION')
if not all(0<lower[j]<upper[j] for j in range(7)) or not all(lower[j]<=atom[j]<=upper[j] for j in range(7)) or not any(not lower[j]<=b[j]<=upper[j] for j in range(7)):raise ValueError('MEMBERSHIP')
if lower[7]!=upper[7] or lower[7]!=atom[7] or atom[7]!=b[7] or b[7]!=1:raise ValueError('LEADING')
if sum(upper[:7])+1!=F(f['coefficient_sum_bound']):raise ValueError('SUM')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
cs=corners(lower,upper)
def det(A):
 n=len(A);den=lcm(*(z.denominator for row in A for z in row));M=[[int(z*den) for z in row] for row in A];sgn=1;prev=1
 for k in range(n-1):
  if not M[k][k]:
   r=next((r for r in range(k+1,n) if M[r][k]),None)
   if r is None:return F(0)
   M[r],M[k]=M[k],M[r];sgn=-sgn
  pivot=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    v=M[i][j]*pivot-M[i][k]*M[k][j]
    if v%prev:raise ValueError('BAREISS')
    M[i][j]=v//prev
  for i in range(k+1,n):M[i][k]=0
  prev=pivot
 return F(sgn*M[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def parity(p):return [p[0],-p[2],p[4],-p[6]],[p[1],-p[3],p[5],-p[7]]
def pair(a,b):
 e,o=parity(a);x,y=parity(b);z=mul(e,x)+[F(0)]
 for j,v in enumerate(mul(o,y)):z[j+1]+=v
 return z
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [r[0] for r in rows],[r[-1] for r in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;v=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
vals=[];counts=[]
for ci,a in enumerate(cs):
 p=pair(a,b);last=F(0);count=0
 for l,r in sorted(f['frequency_leaves'][ci],key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER')
  v=leaf(p,l,r)
  if not all(x>0 for x in v):raise ValueError('SIGN')
  vals.extend(v);count+=len(v);last=r
 if last!=1:raise ValueError('COVER')
 counts.append(count)
if min(vals)!=F(f['compactified_positive_margin']):raise ValueError('MARGIN')
def monomial(a,t):
 return [sum(a[j]*(1 if ((k-j)//2)%2==0 else -1)*t**((j+k)//2) for j in range(8) if (j+k)%2==0) for k in range(8)]
A=monomial(lower,F(2));B=monomial(atom,F(3));C=[x+y for x,y in zip(A,B)]
signs=['+' if x>0 else '-' if x<0 else '0' for x in C]
if signs!=f['coefficient_signs']:raise ValueError('COEFF_SIGN')
maxval=C[7]+sum(C[j]*(upper[j] if C[j]>0 else lower[j]) for j in range(7))
if maxval!=F(f['full_box_maximum']) or maxval>=0:raise ValueError('FULL_BOX_MAX')
good=sum(C[j]*b[j] for j in range(8))
if good!=F(f['good_atom_sum']) or good<=0:raise ValueError('GOOD_VALUE')
print('independent simple lifted replay:',{'strict_hurwitz_minors':28,'bernstein_coefficients':counts,'compactified_margin':str(min(vals)),'strict_full_box_maximum':str(maxval),'good_numerator_atom_sum':str(good),'scope':'one full-dimensional septic box has a common numerator, but none inside the box'})

openraw=(root/'frontier-20261028-lifted-simple-open-separation-frozen-v1.json').read_bytes()
if sha256(openraw).hexdigest()!='ac3dfb6ddae33393572ceba011db84913dc6df3f4323081dba5b754b1d3f4efc':raise ValueError('OPEN_PIN')
g=json.loads(openraw);eps=F(g['radius']);d=F(g['distance']);Bsum=sum(b);M=-maxval;T=sum(abs(C[j]) for j in range(7));A=[sum(t**((j+k)//2) for t in (F(2),F(3)) for j in range(7) if (j+k)%2==0) for k in range(8)];L=T+sum(A[j]*(upper[j]+1) for j in range(7))+A[7];Md=M-d*T;Ld=T+sum(A[j]*(upper[j]+d+1) for j in range(7))+A[7];width=min(upper[j]-lower[j] for j in range(7));lower_min=min(lower[:7])
if (Bsum,T,M,L,Md,Ld,width,lower_min)!=(F(g['Bsum']),F(g['C_l1']),F(g['anchor_obstruction_margin']),F(g['obstruction_lipschitz']),F(g['distance_margin']),F(g['distance_lipschitz']),F(g['minimum_width']),F(g['minimum_lower'])):raise ValueError('ARITHMETIC')
checks=[eps<=1,4*eps<=width,2*eps<=lower_min,14*eps*Bsum<=1,2*eps*L<=M,2*eps*Ld<=Md,Md>0]
if not all(checks):raise ValueError('BOUND')
print('independent simple open-separation replay:',{'radius':str(eps),'distance':str(d),'checks':len(checks),'all_hold':True,'Bsum':str(Bsum),'C_l1':str(T),'anchor_dilated_margin':str(Md),'dilated_L':str(Ld),'scope':'14 endpoint dimensions; common unrestricted b exists, but every common monic numerator is farther than d from its own box'})
