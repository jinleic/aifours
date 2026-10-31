# Bounded exact exchange for one frozen stable box. Each physical row is
# independently multiplied by a positive rational and made primitive; the
# eight coefficient axes are also positively rescaled. Neither operation
# changes existence of a strict negative certificate.
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as Q
from math import lcm,gcd
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
base=sorted(Q(t) for band in f['bands'] for t in band['nodes']);freq=set(base+[base[0]/2,base[-1]*2]);freq.update((a+b)/2 for a,b in zip(base,base[1:]))
extra=set()
for step in range(18):
 atoms=[]
 for ci,a in enumerate(cs):
  for t in sorted(freq):
   if extra and (ci,t) not in extra and t not in initial_freq:continue
   row=[axis[j]*x for j,x in enumerate(full_row(a,t))];den=lcm(*(x.denominator for x in row));integers=[int(x*den) for x in row];factor=gcd(*(abs(x) for x in integers))
   atoms.append((ci,t,[x//factor for x in integers],Q(den,factor)))
 if step==0:initial_freq=set(freq)
 mat=[[a[2][j] for a in atoms] for j in range(8)];sol=exact_minimax(mat,pivot_cap=2400)
 out={'step':step,'atoms':len(atoms),'solver_status':sol['status'],'pivots':sol['pivots']}
 if sol['status']!='CERTIFIED_OPTIMUM':out['status']='SIMPLEX_INCONCLUSIVE'
 elif sol['optimum']<0:
  weights=[sol['lambda'][i]*a[3] for i,a in enumerate(atoms)];sums=[sum(weights[i]*full_row(cs[a[0]],a[1])[j] for i,a in enumerate(atoms)) for j in range(8)]
  if not all(v<0 for v in sums):raise ValueError('CERTIFICATE')
  out.update({'status':'STRICT_NEGATIVE_ATOM_CERTIFICATE','support':[{'corner':a[0],'t':str(a[1]),'weight':str(weights[i])} for i,a in enumerate(atoms) if weights[i]>0],'coefficient_sums':list(map(str,sums))})
 elif sol['optimum']==0:out['status']='ZERO_GRID_MARGIN'
 else:
  y=sol['dual'];eps=Q(1)
  for ci,t,col,fac in atoms:
   v=sum(y[j]*col[j] for j in range(8));h=sum(col)
   if not v>0:raise ValueError('GRID_DUAL')
   if h<0:eps=min(eps,v/(-2*h))
  b=[axis[j]*(y[j]+eps) for j in range(8)];b=[x/b[7] for x in b];bad=[];proof=[]
  for ci,a in enumerate(cs):
   rr=sign_halfline(pair(a,b));proof.append(rr)
   if rr['status']=='NEGATIVE' and rr['t']!='infinity':bad.append((ci,Q(rr['t'])))
   elif rr['status']!='STRICT_POSITIVITY':bad.append((ci,None))
  if not bad:out.update({'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proof})
  elif any(t is None for ci,t in bad):out.update({'status':'HALFLINE_INCONCLUSIVE','bad':[(ci,str(t)) for ci,t in bad]})
  else:
   out.update({'status':'ADDED_NEGATIVE_NODES','bad':[(ci,str(t)) for ci,t in bad]})
   for ci,t in bad:freq.add(t);extra.add((ci,t))
 path=root/('frontier-20261028-sturm-band-primitive-simplex-step-%02d-v1.json'%step);text=json.dumps(out,indent=2,sort_keys=True)+'\n';path.write_text(text)
 print('primitive-simplex step',step,out['status'],'pivots',out['pivots'],'atoms',out['atoms'],'sha256',sha256(text.encode()).hexdigest())
 if out['status']!='ADDED_NEGATIVE_NODES':break
