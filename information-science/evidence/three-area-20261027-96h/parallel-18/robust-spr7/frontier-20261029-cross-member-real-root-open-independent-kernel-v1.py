# Exact rational angular-interval replay, independent of any floating point.
# Uses Machin pi bounds, alternating atan series, atanh log bounds, sign-only
# root-interval classification, and Bareiss strict Hurwitz determinants.
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from math import lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return json.loads(raw)
f=pin('frontier-20261029-cross-member-real-root-obstruction-frozen-v1.json','3c4670d112845021bb15d9eecfded656455e488650d585f70d3538483ee976ed');box=pin(f['source_box'],f['source_box_sha256']);batch=pin(f['common_numerator_batch'],f['common_numerator_batch_sha256'])
lo=list(map(F,box['lower']));hi=list(map(F,box['upper']));w1=F(f['omega1']);w2=F(f['omega2']);slack=F(f['strict_cross_slack_at_least'])
if not all(0<lo[j]<hi[j] for j in range(7)) or not 0<w1<w2:raise ValueError('INPUT')
def corners(lo,hi):
 out=[]
 for e,o in ((0,0),(0,1),(1,0),(1,1)):
  out.append([(lo[j] if not(e if j%2==0 else o) else hi[j]) if j%4 in (0,1) else (hi[j] if not(e if j%2==0 else o) else lo[j]) for j in range(7)]+[F(1)])
 return out
cs=corners(lo,hi)
def det(A):
 n=len(A);d=lcm(*(v.denominator for row in A for v in row));M=[[int(v*d) for v in row] for row in A];sgn=1;prev=1
 for k in range(n-1):
  if not M[k][k]:
   q=next((i for i in range(k+1,n) if M[i][k]),None)
   if q is None:return F(0)
   M[q],M[k]=M[k],M[q];sgn=-sgn
  p=M[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):
    z=M[i][j]*p-M[i][k]*M[k][j]
    if z%prev:raise ValueError('BAREISS')
    M[i][j]=z//prev
  for i in range(k+1,n):M[i][k]=0
  prev=p
 return F(sgn*M[-1][-1],d**n)
for a in cs:
 H=[[a[6-2*i+j] if 0<=6-2*i+j<=7 else F(0) for j in range(7)] for i in range(7)]
 for n in range(1,8):
  if det([row[:n] for row in H[:n]])<=0:raise ValueError('HURWITZ')
def atan_series(x,N):
 if not 0<=x<=1:raise ValueError('ATAN_RANGE')
 z=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(2*N)),F(0))
 return z,z+x**(4*N+1)/(4*N+1)
N=f['pi_series_order'];a,b=atan_series(F(1,5),N);c,d=atan_series(F(1,239),N);PL=16*a-4*d;PU=16*b-4*c
if not 3<PL<PU<4:raise ValueError('PI')
def atan_interval(x):
 if x<0:raise ValueError('ATAN')
 if x>1:
  l,h=atan_interval(1/x);return PL/2-h,PU/2-l
 if x>F(1,2):
  l,h=atan_series((1-x)/(1+x),f['atan_series_order']);return PL/4-h,PU/4-l
 return atan_series(x,f['atan_series_order'])
def phase(a,w):
 t=w*w;E=a[0]-a[2]*t+a[4]*t*t-a[6]*t**3;O=a[1]-a[3]*t+a[5]*t*t-a[7]*t**3
 if not E or not O:raise ValueError('AXIS')
 # Checker independently isolates the three positive roots by derivative-free
 # rational Sturm division; Hurwitz interlacing guarantees all simple.
 def ev(p,x):return sum(v*x**j for j,v in enumerate(p))
 def trim(p):
  while len(p)>1 and p[-1]==0:p.pop()
  return p
 def rem(p,q):
  p=p[:]
  while len(p)>=len(q) and p!=[0]:
   z=p[-1]/q[-1];shift=len(p)-len(q)
   for j,v in enumerate(q):p[shift+j]-=z*v
   trim(p)
  return p
 def sturm(p):
  seq=[trim(p[:]),trim([F(j)*p[j] for j in range(1,len(p))])]
  while len(seq[-1])>1:
   z=[-v for v in rem(seq[-2],seq[-1])]
   if all(v==0 for v in z):raise ValueError('REPEATED')
   seq.append(trim(z))
  return seq
 def var(seq,x):
  v=[1 if z>0 else -1 for z in (ev(p,x) for p in seq) if z]
  return sum(v[i]!=v[i-1] for i in range(1,len(v)))
 e=[a[0],-a[2],a[4],-a[6]];o=[a[1],-a[3],a[5],-a[7]];se=sturm(e);so=sturm(o);q=var(se,F(0))-var(se,t)+var(so,F(0))-var(so,t)
 x=abs(w*O/E) if q%2==0 else abs(E/(w*O));l,h=atan_interval(x)
 return q*PL/2+l,q*PU/2+h
def log_interval(r,N):
 z=(r-1)/(r+1);a=sum((2*z**(2*j+1)/F(2*j+1) for j in range(N)),F(0));return a,a+2*z**(2*N+1)/((2*N+1)*(1-z*z))
ph=[[phase(a,w) for w in (w1,w2)] for a in cs];ll,lu=log_interval(w2/w1,f['log_series_order']);threshold_lo=PL+F(7,2)*ll;threshold_hi=PU+F(7,2)*lu
cross=ph[f['p_corner']][1][0]-ph[f['q_corner']][0][1]
if not cross>threshold_hi+slack:raise ValueError('CROSS_PHASE')
for j in range(4):
 upper=ph[j][1][1]-ph[j][0][0]
 if not upper<threshold_lo-F(f['strict_same_corner_slack_at_least']):raise ValueError('SAME_CORNER')
rec=next(x for x in batch['cases'] if x['case']==f['common_numerator_case'])
if rec['box_sha256']!=f['source_box_sha256'] or not all(F(x)>0 for x in rec['b']):raise ValueError('COMMON_B_PIN')
print('independent cross-member phase replay:',{'hurwitz_minors':28,'actual_cross_pair':[f['q_corner'],f['p_corner']],'frequencies':[str(w1),str(w2)],'cross_margin_gt':str(slack),'all_four_same_corner_margins_gt':f['strict_same_corner_slack_at_least'],'pi_atan_log_exact_series_order':12,'scope':'no all-real-rooted common numerator; no single corner proves this criterion at the same two frequencies; unrestricted common b separately certified'})

openraw=(root/'frontier-20261029-cross-member-real-root-open-frozen-v1.json').read_bytes()
if sha256(openraw).hexdigest()!='c7cb51372254110849102c4516b7b6dac81ac388bb6070a9615125aa971d92c2':raise ValueError('OPEN_PIN')
g=json.loads(openraw);eps=F(g['radius']);bounds=[]
for w in (w1,w2):
 for a in cs:
  t=w*w;e=a[0]-a[2]*t+a[4]*t*t-a[6]*t**3;o=w*(a[1]-a[3]*t+a[5]*t*t-t**3);de=eps*(1+t+t*t+t**3);do=eps*w*(1+t+t*t)
  if not(abs(e)>2*de and abs(o)>2*do):raise ValueError('PHASE_AXIS')
  bounds.append(2*(de+do)/max(abs(e),abs(o)))
if list(map(str,bounds))!=g['phase_deviation_bounds'] or not all(v<F(g['phase_deviation_upper']) for v in bounds) or not 2*F(g['phase_deviation_upper'])<slack:raise ValueError('PHASE_MARGIN')
b=list(map(F,rec['b']));delta=F(rec['compactified_minimum'])
if sum(b)!=F(g['numerator_l1']) or delta!=F(g['anchor_margin']) or not(14*eps*sum(b)<=delta and all(lo[j]-eps>0 and lo[j]+eps<hi[j]-eps for j in range(7))):raise ValueError('COMMON_B_MARGIN')
print('independent open cross-member root obstruction:',{'endpoint_dimensions':14,'radius':str(eps),'strict_phase_error_bound':g['phase_deviation_upper'],'phase_checks':8,'same_corner_nontrigger_checks':4,'fixed_common_numerator':True,'scope':'all nearby boxes require at least one nonreal numerator pair via two actual members, while each individual corner fails this particular same-frequency criterion'})
