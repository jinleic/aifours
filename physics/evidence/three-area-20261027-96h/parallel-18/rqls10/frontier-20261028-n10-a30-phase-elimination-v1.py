#!/usr/bin/env python3
"""Certify every A.30 halfgraph matching either impossible or a,b in Q(zeta12)."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent;source=P/'frontier-20261028-n10-a30-halfgraph-symbolic-v1.py';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='e8c50ef8571237c6d0d2643eb775c95bda16cf6ee95d9194abfa5c0883f92913'
G={'__file__':str(source)};exec(compile(raw.decode().split('case_counts=collections.Counter()',1)[0],str(source),'exec'),G)
terms=G['terms'];admissible=G['admissible'];matchings=G['matchings'];mul=G['mul'];neg=G['neg'];add=G['add'];Z=G['Z'];ONE=(1,0,0,0)
def eqpoly(poly):
 (u,c),(v,d)=sorted(poly.items());exp=(v[0]-u[0],v[1]-u[1]);n=neg(c);den=d
 if exp[0]<0 or exp[0]==0 and exp[1]<0:exp=(-exp[0],-exp[1]);n,den=den,n
 return exp,n,den
def pw(x,n):
 y=ONE
 for _ in range(n):y=mul(y,x)
 return y
def substitute(poly,var,num,den):
 lo=min(k[var]for k in poly);hi=max(k[var]for k in poly);out={}
 for key,c in poly.items():
  z=mul(c,mul(pw(num,key[var]-lo),pw(den,hi-key[var])));q=key[1-var];out[q]=add(out.get(q,Z),z)
 return {k:v for k,v in out.items()if v!=Z}
out=P/'frontier-20261028-n10-a30-phase-elimination-v1.jsonl';counts=collections.Counter();halves=0;matchinghalves=0
with out.open('w') as f:
 for E0 in itertools.combinations(range(1,10),4):
  halves+=1;E=(0,)+E0;polys={(c,d):terms(E,c,d)for c,d in itertools.combinations(range(10),2)};typ={k:admissible(v)for k,v in polys.items()};adj=[['']*10 for _ in range(10)]
  for (c,d),v in typ.items():adj[c][d]=adj[d][c]=v
  matches=list(matchings((1<<10)-1,adj,[]));matchinghalves+=bool(matches)
  for match in matches:
   seen={};bad=False;multi=[]
   for edge in match:
    if typ[edge]=='multinomial':multi.append(edge)
    if typ[edge]=='binomial_possible':
     exp,n,den=eqpoly(polys[edge])
     if exp in seen and mul(n,seen[exp][1])!=mul(seen[exp][0],den):bad=True
     seen[exp]=(n,den)
   evidence={'E':E,'matching':match,'binomial_exponents':list(seen),'multinomial_edges':multi}
   if bad:status='inconsistent_binomials'
   elif (1,0) in seen and (0,1) in seen:status='both_parameters_in_field_direct'
   elif len(seen)==1 and len(multi)==1:
    exp,(n,den)=next(iter(seen.items()));assert exp in [(1,0),(0,1)];var=0 if exp==(1,0) else 1
    reduced=substitute(polys[multi[0]],var,n,den);assert len(reduced)==2 and max(reduced)-min(reduced)==1
    status='both_parameters_in_field_substitution';evidence['substituted_laurent_polynomial']={str(k):v for k,v in reduced.items()}
   else:status='UNRESOLVED'
   counts[status]+=1;evidence['status']=status;f.write(json.dumps(evidence,separators=(',',':'))+'\n')
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'matrix_checker_sha256':hashlib.sha256(raw).hexdigest(),
 'stream_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'clock_finish':datetime.datetime.now().astimezone().isoformat(),
 'halves':halves,'matching_halves':matchinghalves,'counts':dict(counts),'status':'PASS' if not counts['UNRESOLVED'] else 'UNRESOLVED'}
(P/'frontier-20261028-n10-a30-phase-elimination-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
