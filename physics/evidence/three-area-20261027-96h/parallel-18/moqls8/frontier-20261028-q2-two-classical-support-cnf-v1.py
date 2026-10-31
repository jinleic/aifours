#!/usr/bin/env python3
"""Exact q2 necessary-support CNF for the pinned first maximal 2-MOLS net.

No phases, magnitude assumptions or cross-cell Q/R product constraints are
encoded. Any physical q2 family must satisfy this weaker formula.
"""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q2-two-classical-support-relaxation-v1.py';PIN='8909e9b86c4c078de497dc408a82787236e32b765ccf64d99fcad6f677aeef9d'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('net module pin')
s=importlib.util.spec_from_file_location('q2net',H/FILE);net=importlib.util.module_from_spec(s);s.loader.exec_module(net)
V=range(8)
def build(T,nonclassical=True):
 facts={x:(x//8,x%8,*(L[x//8][x%8] for L in T)) for x in range(64)}
 A={x:tuple(sorted(set(V)-set(facts[x][1:]))) for x in range(8,64)}
 if any(len(S)!=5 for S in A.values()):raise ValueError('allowed support')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(4) for v in V}
 if any(len(L)!=8 for L in lines.values()):raise ValueError('net line')
 count=0;clauses=[]
 def var():
  nonlocal count
  count+=1;return count
 def add(*C):
  if not C or any(x==0 or abs(x)>count for x in C):raise ValueError('clause')
  clauses.append(C)
 P={(q,x,t):var() for q in range(2) for x in A for t in A[x]}
 for q in range(2):
  for x in A:add(*(P[q,x,t] for t in A[x]))
  for line in lines.values():
   for t in V:
    if t in line:continue
    X=[x for x in line if x>=8 and t in A[x]]
    if len(X)!=5:raise ValueError('axis line coverage')
    add(*(P[q,x,t] for x in X))
 for x in A:
  for t in A[x]:add(-P[0,x,t],-P[1,x,t])
 E=set()
 for L in lines.values():E.update(itertools.combinations((x for x in L if x>=8),2))
 for q in range(2):
  for x,y in sorted(E):
   C=sorted(set(A[x])&set(A[y]))
   if len(C)==1:
    t=C[0];add(-P[q,x,t],-P[q,y,t]);continue
   if len(C)<2:continue
   B={t:var() for t in C}
   for t in C:
    b=B[t];add(-b,P[q,x,t]);add(-b,P[q,y,t]);add(b,-P[q,x,t],-P[q,y,t])
   for t in C:add(-B[t],*(B[u] for u in C if u!=t))
 if nonclassical:
  for q in range(2):
   N=[]
   for x in A:
    for t,u in itertools.combinations(A[x],2):
     n=var();N.append(n);add(-n,P[q,x,t]);add(-n,P[q,x,u])
   add(*N)
 data=('p cnf %d %d\n'%(count,len(clauses))+''.join(' '.join(map(str,z))+' 0\n' for z in clauses)).encode('ascii')
 return data,{'variables':count,'clauses':len(clauses),'support_variables':len(P),'four_net_pairs':len(E),
              'nonclassical_required':nonclassical,'formula_bytes':len(data),'formula_sha256':hashlib.sha256(data).hexdigest()}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 data,info=build(net.actual_net(),True)
 with pathlib.Path(a.cnf).open('xb') as h:h.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'net_module_sha256':PIN,'first_pair_snapshot_sha256':net.PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'Necessary support constraints for arbitrary complex q2 only; proof, reduction review and source classification separate.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as h:json.dump(info,h,indent=2);h.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
