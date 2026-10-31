# Independent integer/Fraction replay of one exact anisotropic stable box
# and its simplified common numerator. No LP solver is used here.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
from math import comb,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def load(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=load('frontier-20261029-four-nonreal-roots-wide-box-frozen-v1.json','8d7499212660f2cd5135b38ee1125defea80f2551fc655dcb7bf666da97388ff')
g=f
lo=list(map(F,g['lower']));hi=list(map(F,g['upper']));b=list(map(F,f['b']))
if not all(F(0)<lo[j]<hi[j] for j in range(7)) or len(b)!=8 or b[7]!=1 or not all(x>0 for x in b):raise ValueError('BOX_OR_NUMERATOR')
if sum(hi)+1!=F(f['coefficient_sum_bound']):raise ValueError('SUM_BOUND')
center=list(map(F,f['center']));radius=F(f['radius'])
if b!=center or any(lo[j]!=center[j]-radius or hi[j]!=center[j]+radius for j in range(7)):raise ValueError('CENTER_RADIUS')
def parity_corner(es,os):
 ret=[]
 for j in range(7):
  side=es if j%2==0 else os
  ret.append((lo[j] if side==0 else hi[j]) if j%4 in (0,1) else (hi[j] if side==0 else lo[j]))
 return ret+[F(1)]
cs=[parity_corner(e,o) for e,o in ((0,0),(0,1),(1,0),(1,1))]
def bareiss(M):
 n=len(M);den=lcm(*(v.denominator for row in M for v in row));A=[[int(v*den) for v in row] for row in M];sgn=1;prev=1
 for k in range(n-1):
  if A[k][k]==0:
   q=next((i for i in range(k+1,n) if A[i][k]),None)
   if q is None:return F(0)
   A[k],A[q]=A[q],A[k];sgn=-sgn
  pivot=A[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    x=A[i][j]*pivot-A[i][k]*A[k][j]
    if x%prev:raise ValueError('BAREISS')
    A[i][j]=x//prev
  for i in range(k+1,n):A[i][k]=0
  prev=pivot
 return F(sgn*A[-1][-1],den**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if bareiss([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def mul(x,y):
 a=[F(0)]*(len(x)+len(y)-1)
 for i,u in enumerate(x):
  for j,v in enumerate(y):a[i+j]+=u*v
 return a
def pairing(a,b):
 e=lambda p:[p[0],-p[2],p[4],-p[6]];o=lambda p:[p[1],-p[3],p[5],-p[7]]
 p=mul(e(a),e(b))+[F(0)]
 for i,v in enumerate(mul(o(a),o(b))):p[i+1]+=v
 return p
def split(beta):
 rows=[beta]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [row[0] for row in rows],[row[-1] for row in rows[::-1]]
def leaf(p,a,b):
 n=len(p)-1;beta=[p[j]/comb(n,j) for j in range(n+1)];l=F(0);r=F(1)
 for _ in range(100):
  if l==a and r==b:return beta
  m=(l+r)/2;L,R=split(beta)
  if b<=m:r=m;beta=L
  elif a>=m:l=m;beta=R
  else:raise ValueError('NON_DYADIC')
 raise ValueError('LEAF_DEPTH')
mins=[];counts=[]
for ci,a in enumerate(cs):
 p=pairing(a,b);last=F(0);vals=[];rows=sorted(f['frequency_leaves'][ci],key=lambda r:F(r[0]))
 for l,r in rows:
  l,r=F(l),F(r)
  if last!=l or l>=r:raise ValueError('LEAF_COVER')
  beta=leaf(p,l,r)
  if not all(v>0 for v in beta):raise ValueError('LEAF_SIGN')
  vals.extend(beta);last=r
 if last!=1:raise ValueError('LEAF_COVER')
 mins.append(min(vals));counts.append(len(vals))
if min(mins)!=F(f['compactified_pairing_minimum']):raise ValueError('MARGIN')
print('independent wide nonreal-root-box replay:',{'four_corners':4,'hurwitz_minors':28,'strict_bernstein_counts':counts,'minimum':str(min(mins)),'b':list(map(str,b)),'scope':'one wide box with center common; nonreal root necessity is imported from the pinned written phase theorem'})

rawopen=(root/'frontier-20261029-resonant-root-localization-open-frozen-v1.json').read_bytes()
if sha256(rawopen).hexdigest()!='50cf9f1ebadde94ea1ab7be8f7b9aa140c91d3443dcf078d1bec3e2a1d4e94f3':raise ValueError('OPEN_PIN')
h=json.loads(rawopen);eps=F(h['radius']);delta=F(f['compactified_pairing_minimum']);B=sum(b)
if B!=F(h['numerator_l1']) or delta!=F(h['anchor_margin']) or not(14*eps*B<=delta and all(lo[j]+eps<b[j]<hi[j]-eps for j in range(7))):raise ValueError('OPEN_BOUND')
print('independent open localization stability:',{'endpoint_radius':str(eps),'endpoint_dimensions':14,'center_denominator_retained':True,'fixed_common_numerator':True,'scope':'each perturbed box has two localized upper numerator roots via the named phase theorem'})

rawref=(root/'frontier-20261029-resonant-root-localization-refined-frozen-v1.json').read_bytes()
if sha256(rawref).hexdigest()!='bc2b46631b9000c93fc550edf30f543373e7e2eaa8a712e08aa6694d70d31638':raise ValueError('REF_PIN')
z=json.loads(rawref);wm=F(z['omega_minus']);wp=F(z['omega_plus']);R=F(z['radius']);eta=F(1,100);A=1+eta*eta;ql=2*eta*wm/(A-wm*wm);qr=2*eta*wp/(wp*wp-A);up=lambda x:x-x**3/3+x**5/5;low=lambda x:x-x**3/3;e=up(ql)+up(qr);tan=(wp-wm)/(1+wp*wm);gain=low(tan);piL=F(z['pi_lower']);D=wp-wm
if not(0<ql<1 and 0<qr<1 and 0<tan<1 and 0<R<wm):raise ValueError('ATAN_RANGE')
if list(map(str,[ql,qr]))!=z['quadratic_error_ratios'] or e!=F(z['quadratic_deficit_upper']) or tan!=F(z['linear_tan_increment']) or gain!=F(z['linear_phase_lower']):raise ValueError('REF_VALUES')
if not(2*piL>3*e-gain+3*D/R+4*D/(2*wm) and piL>3*e-gain+2*D/R+3*D/(2*wm)):raise ValueError('REF_GAPS')
print('independent refined localization replay:',{'radius':str(R),'segment':[str(wm),str(wp)],'atan_rational_bounds':3,'j0_j1_gaps':2,'scope':'every common numerator of each certified nearby box has at least two upper roots within this segment neighborhood'})
