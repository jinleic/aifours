# Exact bounded original-decision search across frozen, strictly stable
# anisotropic boxes. Downward-rounded normalized LP rows can only produce a
# candidate; any negative certificate is checked on original rational rows.
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
def search_box(case):
 src=root/('frontier-20261028-sturm-band-strict-certificate-case-%02d-v1.json'%case);raw=src.read_bytes();f=json.loads(raw)
 if f['status']!='unsat':raise ValueError('INPUT_STATUS')
 lo=list(map(Q,f['lower']));hi=list(map(Q,f['upper']));cs=corners(lo,hi);axis=[(lo[j]+hi[j])/2 for j in range(7)]+[Q(1)]
 base=sorted(Q(t) for band in f['bands'] for t in band['nodes']);initial=set(base+[base[0]/2,base[-1]*2]);initial.update((a+b)/2 for a,b in zip(base,base[1:]));extra=set();N=10**18
 for step in range(12):
  atoms=[]
  for ci,a in enumerate(cs):
   for t in sorted(initial|{t for j,t in extra if j==ci}):
    row=[axis[j]*x for j,x in enumerate(full_row(a,t))];scale=max(abs(x) for x in row)
    if not scale:raise ValueError('ZERO_ROW')
    norm=[x/scale for x in row];vec=[(N*x).numerator//(N*x).denominator for x in norm];atoms.append((ci,t,vec,norm,scale))
  mat=[[a[2][j] for a in atoms] for j in range(8)];sol=exact_minimax(mat,pivot_cap=1800)
  out={'case':case,'step':step,'atoms':len(atoms),'pivots':sol['pivots'],'source_box_sha256':sha256(raw).hexdigest(),'solver_status':sol['status']}
  if sol['status']!='CERTIFIED_OPTIMUM':out['status']='SIMPLEX_INCONCLUSIVE'
  elif sol['optimum']<=0:
   weights=[sol['lambda'][i]/a[4] for i,a in enumerate(atoms)];sums=[sum(weights[i]*full_row(cs[a[0]],a[1])[j] for i,a in enumerate(atoms)) for j in range(8)]
   if all(v<0 for v in sums):out.update({'status':'STRICT_NEGATIVE_ATOM_CERTIFICATE','support':[{'corner':a[0],'t':str(a[1]),'weight':str(weights[i])} for i,a in enumerate(atoms) if weights[i]>0],'coefficient_sums':list(map(str,sums)),'lower':list(map(str,lo)),'upper':list(map(str,hi))})
   else:out['status']='ROUNDED_NEGATIVE_NOT_CERTIFIED'
  else:
   y=sol['dual'];eps=Q(1)
   for ci,t,col,row,scale in atoms:
    v=sum(y[j]*row[j] for j in range(8));h=sum(row)
    if v<=0:raise ValueError('TRUE_GRID_DUAL')
    if h<0:eps=min(eps,v/(-2*h))
   b=[axis[j]*(y[j]+eps) for j in range(8)];b=[v/b[7] for v in b];bad=[];proof=[]
   for ci,a in enumerate(cs):
    rr=sign_halfline(pair(a,b));proof.append(rr)
    if rr['status']=='NEGATIVE' and rr['t']!='infinity':bad.append((ci,Q(rr['t'])))
    elif rr['status']!='STRICT_POSITIVITY':bad.append((ci,None))
   if not bad:out.update({'status':'COMMON_NUMERATOR_PROVED','b':list(map(str,b)),'proofs':proof})
   elif any(t is None for ci,t in bad):out.update({'status':'HALFLINE_INCONCLUSIVE','bad':[(ci,str(t)) for ci,t in bad]})
   else:out.update({'status':'ADDED_NEGATIVE_NODES','bad':[(ci,str(t)) for ci,t in bad]});extra.update(bad)
  path=root/('frontier-20261028-sturm-band-multi-box-%02d-step-%02d-v1.json'%(case,step));text=json.dumps(out,indent=2,sort_keys=True)+'\n';path.write_text(text)
  print('multi-box',case,'step',step,out['status'],'pivots',out['pivots'],'sha256',sha256(text.encode()).hexdigest())
  if out['status']!='ADDED_NEGATIVE_NODES':return out
 return out
multi_first=search_box(1)
