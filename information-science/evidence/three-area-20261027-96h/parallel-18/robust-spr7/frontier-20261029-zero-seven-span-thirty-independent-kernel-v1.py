# Independent exact replay of 30 origin-plus-five-contact boundary cases.
# Reconstruct factors, actual corners, seven-generator identity, contact-square
# residual leaves, center pairing leaves and rational midpoint Hurwitz minors.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import comb,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=pin('frontier-20261029-zero-seven-span-thirty-frozen-v1.json','4a9da3881cd3d526324aaeaa6ec4a5628d668d1d0453e9aabbc2905ae5c44ed5');sh=pin(f['shape_file'],f['shape_sha256'])['shapes']
if [x['case'] for x in f['cases']]!=list(range(30)):raise ValueError('CASES')
def mul(a,b):
 z=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def cubic(rs,scale):
 p=[-scale]
 for r in rs:p=mul(p,[-r,F(1)])
 return p
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
    z=M[i][j]*p-M[i][k]*M[k][j]
    if z%prev:raise ValueError('BAREISS')
    M[i][j]=z//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sgn*M[-1][-1],den**n)
def pair(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]];z=mul(e(a),e(b))+[F(0)]
 for j,v in enumerate(mul(o(a),o(b))):z[j+1]+=v
 while len(z)>1 and z[-1]==0:z.pop()
 return z
def divide(p,r):
 z=[F(0)]*(len(p)-1);z[-1]=p[-1]
 for j in range(len(z)-2,-1,-1):z[j]=p[j+1]+r*z[j+1]
 if p[0]+r*z[0]:raise ValueError('ROOT')
 while len(z)>1 and z[-1]==0:z.pop()
 return z
def split(v):
 a=[v]
 while len(a[-1])>1:a.append([(x+y)/2 for x,y in zip(a[-1],a[-1][1:])])
 return [r[0] for r in a],[r[-1] for r in a[::-1]]
def leaf(p,a,b):
 n=len(p)-1;v=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return v
  m=(l+r)/2;L,R=split(v)
  if b<=m:r=m;v=L
  elif a>=m:l=m;v=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('DEPTH')
def check(p,ls):
 last=F(0);count=0;minimum=None
 for l,r in sorted(ls,key=lambda x:F(x[0])):
  l,r=F(l),F(r)
  if l!=last or l>=r:raise ValueError('COVER')
  vals=leaf(p,l,r)
  if not all(v>0 for v in vals):raise ValueError('SIGN')
  minimum=min(vals) if minimum is None else min(minimum,min(vals));count+=len(vals);last=r
 if last!=1:raise ValueError('COVER')
 return minimum,count
results=[];total_coeff=0;total_minors=0
for rec in f['cases']:
 i=rec['case'];candidate=pin(rec['source'],rec['source_sha256']);ts=list(map(F,sh[i]['nodes']));v=F(sh[i]['v']);lam=F(sh[i]['lambda']);a,bb,c,d,e=ts
 Em=cubic([F(0),c,d],lam);Ep=cubic([a,bb,e],F(1));Om=cubic([a,d,e],F(1));Op=cubic([bb,c,v],F(1))
 lo=[Em[0],Om[0],-Ep[1],-Op[1],Em[2],Om[2],-Ep[3]];hi=[Ep[0],Op[0],-Em[1],-Om[1],Ep[2],Op[2],-Em[3]]
 if lo[0]!=0 or not all(lo[j]<hi[j] for j in range(7)) or not all(lo[j]>0 for j in range(1,7)):raise ValueError('WIDTH')
 def member(E,O):return [E[0],O[0],-E[1],-O[1],E[2],O[2],-E[3],F(1)]
 cs=[member(Em,Om),member(Em,Op),member(Ep,Om),member(Ep,Op)];mid=[(lo[j]+hi[j])/2 for j in range(7)]+[F(1)];ds=[mid]
 for _ in range(3):ds.append([F(j+1)*ds[-1][j+1] for j in range(7)]+[F(0)])
 G=[[cs[2*k][j] if j%2==0 else F(0) for j in range(8)] for k in (0,1)]+[[cs[k][j] if j%2 else F(0) for j in range(8)] for k in (0,1)]+ds[1:4];coef=list(map(F,candidate['generator_coefficients']));b=list(map(F,candidate['b']))
 if len(coef)!=7 or b[7]!=1 or not all(x>0 for x in b) or not all(sum(coef[k]*G[k][j] for k in range(7))==b[j] for j in range(8)):raise ValueError('SPAN')
 H=[[mid[6-2*x+y] if 0<=6-2*x+y<=7 else F(0) for y in range(7)] for x in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('MID_HURWITZ')
  total_minors+=1
 ct=[(2,a),(3,bb),(1,c),(0,d),(2,e)];counts=[]
 for ci,aa in enumerate(cs):
  p=pair(aa,b)
  if ci in (0,1):p=divide(p,F(0))
  for cj,t in ct:
   if ci==cj:p=divide(divide(p,t),t)
  leaves=[[x['left'],x['right']] for x in candidate['leaves'][ci]];_,num=check(p,leaves);counts.append(num);total_coeff+=num
 margin,num=check(pair(mid,b),rec['center_leaves']);total_coeff+=num
 if margin!=F(rec['center_margin']):raise ValueError('CENTER_MARGIN')
 results.append({'case':i,'residual_bernstein_counts':counts,'center_bernstein_count':num,'center_margin':str(margin)})
 print('origin-contact independent case',i,'strict residual/center coefficients',sum(counts)+num)
out={'status':'WRITTEN-checked-in-kernel; author candidate, not parent adoption','frozen_sha256':'4a9da3881cd3d526324aaeaa6ec4a5628d668d1d0453e9aabbc2905ae5c44ed5','cases':results,'midpoint_hurwitz_minors':total_minors,'strict_bernstein_coefficients':total_coeff,'scope':'30 specified radial families; sign-band stability and affine center-to-boundary interpolation are written deductions; no arbitrary-box claim'}
p=root/'frontier-20261029-zero-seven-span-thirty-independent-result-v1.json';txt=json.dumps(out,sort_keys=True,indent=2)+'\n';p.write_text(txt);print('origin-contact seven-span independent batch',len(results),'midpoint minors',total_minors,'strict coefficients',total_coeff,'sha256',sha256(txt.encode()).hexdigest())
