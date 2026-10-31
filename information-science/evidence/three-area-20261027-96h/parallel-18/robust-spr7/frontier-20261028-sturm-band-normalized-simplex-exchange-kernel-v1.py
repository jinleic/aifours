# Exact exchange with per-column positive normalization and downward rational
# integer rounding. Positive duals are independently tested against ORIGINAL
# rows. Negative rounded optima are accepted only if the ORIGINAL sums are all
# strictly negative; rounding alone cannot certify a negative result.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from math import gcd,lcm
import json
root=Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/robust-spr7')
def pin(name,h):
 raw=(root/name).read_bytes()
 if sha256(raw).hexdigest()!=h:raise ValueError('PIN:'+name)
 return raw.decode()
s=pin('frontier-20261028-bounded-exact-dual-search-kernel-v1.py','bc10ea9be94ff63d729eccae52ad60e33079883a4b4ad33af898cea98535896a');exec(s[s.index('def exact_minimax'):s.index('def corners')])
s=pin('frontier-20261028-sturm-band-scaled-positive-kernel-v1.py','40e478817389f873c0cfb465dcd89a633b8d8f54c333bfb0fdca70d7769974f9');exec(s[:s.index('result=solve(0)')])
f=json.loads(pin('frontier-20261028-sturm-band-strict-certificate-case-00-v1.json','9234459cf1cf113dbb4ea823f6197deac094fef1da38494593ae9a66547732e1'))
lo=list(map(Q,f['lower']));hi=list(map(Q,f['upper']));cs=corners(lo,hi);axis=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)]
base=sorted(Q(t) for band in f['bands'] for t in band['nodes']);initial=set(base+[base[0]/2,base[-1]*2]);initial.update((a+b)/2 for a,b in zip(base,base[1:]));extra=set();step_hashes=[]
for k in range(18):
 name='frontier-20261028-sturm-band-primitive-simplex-step-%02d-v1.json'%k;raw=(root/name).read_bytes();data=json.loads(raw)
 if data['status']!='ADDED_NEGATIVE_NODES':raise ValueError('PRIOR_STATUS')
 step_hashes.append(sha256(raw).hexdigest())
 extra.update((int(ci),Q(t)) for ci,t in data['bad'])
N=10**16
for step in range(12):
 atoms=[]
 for ci,a in enumerate(cs):
  times=initial|{t for j,t in extra if j==ci}
  for t in sorted(times):
   row=[axis[j]*x for j,x in enumerate(full_row(a,t))];scale=max(abs(x) for x in row)
   if not scale:raise ValueError('ZERO_ROW')
   normalized=[x/scale for x in row];integers=[(N*x).numerator//(N*x).denominator for x in normalized]
   atoms.append((ci,t,integers,normalized,scale))
 mat=[[a[2][j] for a in atoms] for j in range(8)];sol=exact_minimax(mat,pivot_cap=2400)
 out={'step':step,'atoms':len(atoms),'solver_status':sol['status'],'pivots':sol['pivots'],'rounding':'floor(10^16 * axis_scaled_row/max_abs_row)','prior_step_hashes':step_hashes}
 if sol['status']!='CERTIFIED_OPTIMUM':out['status']='SIMPLEX_INCONCLUSIVE'
 elif sol['optimum']<=0:
  weights=[sol['lambda'][i]/a[4] for i,a in enumerate(atoms)];sums=[sum(weights[i]*full_row(cs[a[0]],a[1])[j] for i,a in enumerate(atoms)) for j in range(8)]
  if all(x<0 for x in sums):out.update({'status':'STRICT_NEGATIVE_ATOM_CERTIFICATE','support':[{'corner':a[0],'t':str(a[1]),'weight':str(weights[i])} for i,a in enumerate(atoms) if weights[i]>0],'coefficient_sums':list(map(str,sums))})
  else:out['status']='ROUNDED_NEGATIVE_NOT_CERTIFIED'
 else:
  y=sol['dual'];eps=Q(1)
  for ci,t,col,row,scale in atoms:
   val=sum(y[j]*row[j] for j in range(8));h=sum(row)
   if not val>0:raise ValueError('TRUE_GRID_DUAL')
   if h<0:eps=min(eps,val/(-2*h))
  b=[axis[j]*(y[j]+eps) for j in range(8)];b=[x/b[7] for x in b];bad=[];proof=[]
  for ci,a in enumerate(cs):
   rr=sign_halfline(pair(a,b));proof.append(rr)
   if rr['status']=='NEGATIVE' and rr['t']!='infinity':bad.append((ci,Q(rr['t'])))
   elif rr['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:out.update({'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proof})
  elif any(t is None for ci,t in bad):out.update({'status':'HALFLINE_INCONCLUSIVE','bad':[(ci,str(t)) for ci,t in bad]})
  else:
   out.update({'status':'ADDED_NEGATIVE_NODES','bad':[(ci,str(t)) for ci,t in bad]});extra.update(bad)
 path=root/('frontier-20261028-sturm-band-normalized-simplex-step-%02d-v1.json'%step);text=json.dumps(out,indent=2,sort_keys=True)+'\n';path.write_text(text)
 print('normalized-simplex step',step,out['status'],'pivots',out['pivots'],'atoms',out['atoms'],'sha256',sha256(text.encode()).hexdigest())
 if out['status']!='ADDED_NEGATIVE_NODES':break
