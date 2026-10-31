# Standalone exact replay of a ten-site separator for every h>=0 and D.
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
path=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7/frontier-20261028-operator-moment-ten-site-dual-frozen-v1.json')
raw=path.read_bytes()
if sha256(raw).hexdigest()!='0e2ebc6bd3d330cc0a678de65d66682d4040aa1035dd9934a7c99b7a994e968f':raise ValueError('HASH')
d=json.loads(raw);lo=[Q(v) for v in d['lower']];hi=[Q(v) for v in d['upper']]
if not all(0<lo[j]<hi[j] for j in range(7)):raise ValueError('BOX')
def corners(lo,hi):
 out=[]
 for es in (0,1):
  for oside in (0,1):
   a=[Q(0)]*8;a[7]=Q(1)
   for j in (0,2,4,6):a[j]=lo[j] if ((j//2)%2==0)==(es==0) else hi[j]
   for j in (1,3,5):a[j]=lo[j] if ((j//2)%2==0)==(oside==0) else hi[j]
   out.append(a)
 return out
cs=corners(lo,hi);roots={'E-':[lo[0],-hi[2],lo[4],-hi[6]],'E+':[hi[0],-lo[2],hi[4],-lo[6]],
                         'O-':[lo[1],-hi[3],lo[5],Q(-1)],'O+':[hi[1],-lo[3],hi[5],Q(-1)]}
if {k:[str(x) for x in p] for k,p in roots.items()}!=d['root_polynomials']:raise ValueError('ROOT_POLYS')
def ev(p,t):
 v=Q(0)
 for x in p[::-1]:v=v*t+x
 return v
intervals={}
for key,p in roots.items():
 intervals[key]=[(Q(a),Q(b)) for a,b in d['root_intervals'][key]]
 if len(intervals[key])!=3 or p[0]<=0 or p[-1]>=0:raise ValueError('ROOT_COUNT')
 for l,r in intervals[key]:
  if not 0<l<r or ev(p,l)*ev(p,r)>=0:raise ValueError('ROOT_BRACKET')
 if any(intervals[key][j][1]>=intervals[key][j+1][0] for j in range(2)):raise ValueError('ROOT_ORDER')
bands=[]
for j in range(3):
 for q in ('E','O'):bands.append((min(intervals[q+'-'][j][0],intervals[q+'+'][j][0]),max(intervals[q+'-'][j][1],intervals[q+'+'][j][1])))
if any(bands[j][1]>=bands[j+1][0] for j in range(5)):raise ValueError('BANDS')
def det(m):
 A=[[Q(x) for x in row] for row in m];out=Q(1);sgn=1;n=len(A)
 for k in range(n):
  i=next((i for i in range(k,n) if A[i][k]),None)
  if i is None:return Q(0)
  if i!=k:A[k],A[i]=A[i],A[k];sgn=-sgn
  v=A[k][k];out*=v
  for i in range(k+1,n):
   z=A[i][k]/v
   for j in range(k+1,n):A[i][j]-=z*A[k][j]
   A[i][k]=Q(0)
 return sgn*out
def minors(a):
 c=a[::-1]
 def v(i):return c[i] if 0<=i<8 else Q(0)
 return [det([[v(2*j-i) for j in range(1,k+1)] for i in range(1,k+1)]) for k in range(1,8)]
if not all(v>0 for a in cs for v in minors(a)):raise ValueError('HURWITZ')
def routh(a):
 rows=[[a[7],a[5],a[3],a[1]],[a[6],a[4],a[2],a[0]]]
 for k in range(6):
  p,q=rows[-2:]
  if q[0]<=0:raise ValueError('ROUTH')
  rows.append([(q[0]*p[j+1]-p[0]*q[j+1])/q[0] for j in range(3)]+[Q(0)])
 return [v[0] for v in rows]
if [str(v) for v in routh(cs[0])]!=d['reference_routh_first_column']:raise ValueError('ROUTH')
b=[Q(x) for x in d['numerator']]
if len(b)!=8 or b[-1]!=1 or not all(v>0 for v in b):raise ValueError('NUMERATOR')
def diff(a):return [Q(j)*a[j] for j in range(1,len(a))]
def add(a,b):
 out=[Q(0)]*max(len(a),len(b))
 for j,v in enumerate(a):out[j]+=v
 for j,v in enumerate(b):out[j]+=v
 return out
def pair(a,b,t):
 def par(a):return sum(a[j]*(-t)**(j//2) for j in range(0,len(a),2)),sum(a[j]*(-t)**((j-1)//2) for j in range(1,len(a),2))
 E,O=par(a);F,G=par(b);return E*F+t*O*G
def check_site(site):
 ci=site['corner'];t=Q(site['t']);a=cs[ci];ad=diff(a);bd=diff(b)
 p0=pair(a,b,t);p2=pair(ad,bd,t);p1=pair(add(a,ad),add(b,bd),t)-p0-p2
 if [str(p0),str(p1),str(p2)]!=site['quadratic_coefficients']:raise ValueError('PAIR_BINDING')
 if not(p0>0 and p1>0 and p2>0):raise ValueError('PAIR_SIGN')
 return [p0,p1,p2]
vals=[]
for site in d['sites']:vals.extend(check_site(site))
if len(d['sites'])!=10:raise ValueError('SITE_COUNT')
fault=deepcopy(d['sites'][0]);fault['quadratic_coefficients'][1]='-1'
try:check_site(fault)
except ValueError as e:
 if str(e)!='PAIR_BINDING':raise
else:raise ValueError('CONTROL_ACCEPTED')
print('independent ten-site all-h operator separator:',{'corners_minor_positive':28,'root_brackets':12,'separated_bands':6,'sites':len(d['sites']),
 'strict_quadratic_coefficients':len(vals),'minimum_coefficient':str(min(vals)),'corrupted_coefficient_rejected':True})
