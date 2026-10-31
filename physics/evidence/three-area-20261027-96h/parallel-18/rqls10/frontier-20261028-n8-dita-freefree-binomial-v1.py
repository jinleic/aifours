#!/usr/bin/env python3
"""Reduce a both-free bivariate branch to monomially parameterized lines.

A 4x4 minor binomial x^d+lambda*y^(+/-d) forces x=k*y^(+/-1).
For EVERY exact eighth-root k, a 3-row cofactor identically zero in y,
with another monomial nonzero, forces a delta coordinate to vanish.
Mod p is ONLY a prescreen; exact Z[zeta8] polynomials certify each gate.
"""
import hashlib,itertools,json,os,time,datetime
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent;helper=P/'frontier-20261028-n8-dita-freefree-separable-v1.py';raw=helper.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='f2ee7531fc6305615fdcaddceb44ef89eda1761d2d9cf1ffcb98ac0fb4ed3a7f'
code=raw.decode().split("limit=int(os.environ.get('LIMIT','0'))",1)[0]
exec(compile(code,str(helper),'exec'),globals())
src=P/'frontier-20261028-n8-dita-freefree-separable-full-survivors-v1.jsonl'
rows4=[(1,3,4,6)]+[q for q in itertools.combinations(range(16),4)if q!=(1,3,4,6) and sorted(Counter(i//4 for i in q).values())==[2,2]]
rows3=[(1,3,4)]+[q for q in itertools.combinations(range(16),3)if q!=(1,3,4)]
per3=[]
for q in itertools.permutations(range(3)):
 sign=-1 if sum(q[i]>q[j]for i in range(3)for j in range(i+1,3))%2 else 1;per3.append((q,sign))
def relation(poly,exact):
 nz=[(divmod(i,3),v)for i,v in enumerate(poly)if v!=(Z if exact else 0)]
 if len(nz)!=2:return None
 (i,j),a=nz[0];(k,l),b=nz[1]
 if i<k:(i,j),a,(k,l),b=(k,l),b,(i,j),a
 d=i-k;dy=j-l
 if d not in (1,2) or abs(dy)!=d:return None
 eps=1 if dy==-d else -1
 if exact:ks=[q for q in range(8)if add(mul(a,rt(q*d)),b)==Z]
 else:ks=[q for q in range(8)if (a*pow(w,q*d,p)+b)%p==0]
 return (eps,ks) if len(ks)==d else None
def cofpoly(C,M,ids,omit,k,eps,exact):
 cols=[t for t in range(4)if t!=omit];out={};zero=Z if exact else 0
 for q,sign in per3:
  v=ONE if exact else 1;deg=0
  for ii,j in enumerate(q):
   t=cols[j];r=ids[ii];b,c=divmod(r,4);a=(b%2)*(t%2);bb=(c%2)*(M[t]%2)
   deg+=eps*a+bb+(1 if eps==-1 else 0)
   if exact:v=mul(v,mul(C[r][t],rt(k*a)))
   else:v=v*C[r][t]*pow(w,k*a,p)%p
  if exact:out[deg]=add(out.get(deg,Z),tuple(sign*x for x in v))
  else:out[deg]=(out.get(deg,0)+sign*v)%p
 return {d:v for d,v in out.items()if v!=zero}
def witness(C,Cm,M,k,eps):
 for ids in rows3:
  vm=[cofpoly(Cm,M,ids,t,k,eps,False)for t in range(4)]
  zero=[i for i,q in enumerate(vm)if not q];mono=[i for i,q in enumerate(vm)if len(q)==1]
  if not zero or not mono:continue
  ve=[cofpoly(C,M,ids,t,k,eps,True)for t in range(4)]
  zero=[i for i in zero if not ve[i]];mono=[i for i in mono if len(ve[i])==1]
  if zero and mono:return {'rows':ids,'zero_coordinate':zero[0],'nonzero_cofactor':mono[0],'monomial_degree':next(iter(ve[mono[0]]))}
 return None
limit=int(os.environ.get('LIMIT','0'));suffix='sample' if limit else 'full';cnt=Counter();cert=[];sur=[];start=time.monotonic()
for ix,line in enumerate(src.read_text().splitlines()):
 if limit and ix>=limit:break
 row=json.loads(line);C=base(row);M=row['mu'];Cm=[[evalmod(v)for v in r]for r in C];done=False
 for ids in rows4:
  q=relation(poly_mod(Cm,M,ids),False)
  if q is None:continue
  e=relation(poly_exact(C,M,ids),True)
  if e is None:continue
  eps,ks=e;ww=[]
  for k in ks:
   ans=witness(C,Cm,M,k,eps)
   if ans is None:break
   ww.append({'k':k,**ans})
  else:
   cert.append({'minor_rows':ids,'relation_y_power':eps,'branches':ww});cnt['binomial_zero_coordinate']+=1;done=True;break
 if not done:cnt['unresolved']+=1;cert.append(None);sur.append(row)
(P/f'frontier-20261028-n8-dita-freefree-binomial-{suffix}-certs-v1.jsonl').write_text(''.join(json.dumps(c,separators=(',',':'))+'\n'for c in cert))
(P/f'frontier-20261028-n8-dita-freefree-binomial-{suffix}-survivors-v1.jsonl').write_text(''.join(json.dumps(c,separators=(',',':'))+'\n'for c in sur))
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'helper_sha256':hashlib.sha256(raw).hexdigest(),'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'seconds':round(time.monotonic()-start,6),
 'limit':limit,'counts':dict(cnt),'unresolved':len(sur),'minor_candidates':len(rows4),'cofactor_candidates':len(rows3)}
(P/f'frontier-20261028-n8-dita-freefree-binomial-{suffix}-v1.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
