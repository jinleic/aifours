# Exact finite-grid/continuum exchange for five actual stable merged boxes.
# Downward integer row rounding is used only to propose witnesses; every
# negative candidate is checked on the original rational atom rows.
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return raw.decode()
s=pin('frontier-20261028-bounded-exact-dual-search-kernel-v1.py','bc10ea9be94ff63d729eccae52ad60e33079883a4b4ad33af898cea98535896a');exec(s[s.index('def exact_minimax'):s.index('def corners')])
s=pin('frontier-20261028-sturm-band-scaled-positive-kernel-v1.py','40e478817389f873c0cfb465dcd89a633b8d8f54c333bfb0fdca70d7769974f9');exec(s[:s.index('result=solve(0)')])
def run(case):
 path=root/('frontier-20261028-merged-hull-candidate-%02d-v1.json'%case);raw=path.read_bytes();f=json.loads(raw);lo=list(map(Q,f['lower']));hi=list(map(Q,f['upper']));cs=corners(lo,hi);axis=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)];grid={Q(0),Q(1,10),Q(10),Q(20)}
 for t in map(Q,[1,2,3,6,8]):
  for d in (Q(0),Q(1,10),Q(1,100),Q(1,1000)):
   if t+d>=0:grid.add(t+d)
   if t-d>=0:grid.add(t-d)
 extra={(ci,Q(t)) for ci,st,t in f['shared_b_failure'] if st=='NEGATIVE' and t is not None};N=10**18
 for step in range(20):
  atoms=[]
  for ci,a in enumerate(cs):
   for t in sorted(grid|{x for j,x in extra if j==ci}):
    vec=[axis[j]*v for j,v in enumerate(full_row(a,t))];scale=max(abs(v) for v in vec);norm=[v/scale for v in vec];r=[(N*v).numerator//(N*v).denominator for v in norm];atoms.append((ci,t,scale,norm,r))
  C=[[a[4][j] for a in atoms] for j in range(8)];sol=exact_minimax(C,pivot_cap=2000);out={'case':case,'step':step,'source_sha256':sha256(raw).hexdigest(),'atoms':len(atoms),'pivots':sol['pivots'],'solver_status':sol['status']}
  if sol['status']!='CERTIFIED_OPTIMUM':out['status']='SIMPLEX_INCONCLUSIVE'
  elif sol['optimum']<=0:
   w=[sol['lambda'][i]/a[2] for i,a in enumerate(atoms)];sums=[sum(w[i]*full_row(cs[a[0]],a[1])[j] for i,a in enumerate(atoms)) for j in range(8)]
   if all(v<0 for v in sums):out.update({'status':'STRICT_NEGATIVE_ATOM_CERTIFICATE','support':[{'corner':a[0],'t':str(a[1]),'weight':str(w[i])} for i,a in enumerate(atoms) if w[i]>0],'coefficient_sums':list(map(str,sums))})
   else:out['status']='ROUNDED_NEGATIVE_NOT_CERTIFIED'
  else:
   y=sol['dual'];eps=Q(1)
   for ci,t,scale,norm,r in atoms:
    v=sum(y[j]*norm[j] for j in range(8));h=sum(norm)
    if v<=0:raise ValueError('GRID')
    if h<0:eps=min(eps,v/(-2*h))
   b=[axis[j]*(y[j]+eps) for j in range(8)];b=[v/b[7] for v in b];proof=[];bad=[]
   for ci,a in enumerate(cs):
    r=sign_halfline(pair(a,b));proof.append(r)
    if r['status']=='NEGATIVE' and r['t']!='infinity':bad.append((ci,Q(r['t'])))
    elif r['status']!='STRICT_POSITIVITY':bad.append((ci,None))
   if not bad:out.update({'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proof})
   elif any(t is None for ci,t in bad):out['status']='HALFLINE_INCONCLUSIVE'
   else:out.update({'status':'ADDED_NEGATIVE_NODES','bad':[(ci,str(t)) for ci,t in bad]});extra.update(bad)
  p=root/('frontier-20261028-merged-hull-case-%02d-step-%02d-v1.json'%(case,step));txt=json.dumps(out,indent=2,sort_keys=True)+'\n';p.write_text(txt)
  print('merged hull',case,'step',step,out['status'],'pivots',out['pivots'],'sha256',sha256(txt.encode()).hexdigest())
  if out['status']!='ADDED_NEGATIVE_NODES':return out
 return out
for case in range(5):
 result=run(case)
 if result['status']=='STRICT_NEGATIVE_ATOM_CERTIFICATE':break
