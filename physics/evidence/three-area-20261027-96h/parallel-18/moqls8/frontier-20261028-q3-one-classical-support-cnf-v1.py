#!/usr/bin/env python3
"""Necessary q3 support CNF for one explicit classical order-8 Latin square."""
import argparse,hashlib,importlib.util,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
FILE='frontier-20261028-q3-one-classical-support-relaxation-v1.py';PIN='c28e362b472f9af136199cc54aa60a1d901e88f567526a493ff212cf6e73be00'
if hashlib.sha256((H/FILE).read_bytes()).hexdigest()!=PIN:raise ValueError('Latin module pin')
spec=importlib.util.spec_from_file_location('q3net',H/FILE);net=importlib.util.module_from_spec(spec);spec.loader.exec_module(net)
V=range(8)
def build(L):
 facts={x:(x//8,x%8,L[x//8][x%8]) for x in range(64)}
 A={x:tuple(t for t in V if t not in facts[x][1:]) for x in range(8,64)}
 if any(len(z)!=6 for z in A.values()):raise ValueError('allowed axes')
 lines={(k,v):[x for x in range(64) if facts[x][k]==v] for k in range(3) for v in V}
 if any(len(line)!=8 for line in lines.values()):raise ValueError('net lines')
 n=0;C=[]
 def var():
  nonlocal n
  n+=1;return n
 def add(*z):
  if not z or any(v==0 or abs(v)>n for v in z):raise ValueError('clause')
  C.append(tuple(z))
 P={(q,x,t):var() for q in range(3) for x in A for t in A[x]}
 for q in range(3):
  for x in A:add(*(P[q,x,t] for t in A[x]))
  for line in lines.values():
   for t in V:
    if t in line:continue
    z=[x for x in line if x>=8 and t in A[x]]
    if len(z)!=6:raise ValueError('line coverage')
    add(*(P[q,x,t] for x in z))
 for x in A:
  for t in A[x]:
   for q,r in itertools.combinations(range(3),2):add(-P[q,x,t],-P[r,x,t])
 E=set()
 for line in lines.values():E.update(itertools.combinations((x for x in line if x>=8),2))
 if len(E)!=532:raise ValueError('net pair count')
 B={}
 for q in range(3):
  for x,y in sorted(E):
   common=sorted(set(A[x])&set(A[y]))
   if len(common)==1:
    t=common[0];add(-P[q,x,t],-P[q,y,t]);continue
   if len(common)<2:continue
   for t in common:B[q,x,y,t]=var()
   for t in common:
    b=B[q,x,y,t];add(-b,P[q,x,t]);add(-b,P[q,y,t]);add(b,-P[q,x,t],-P[q,y,t])
   for t in common:add(-B[q,x,y,t],*(B[q,x,y,u] for u in common if u!=t))
 triangles=0
 for x,y,z in itertools.combinations(range(8,64),3):
  if (x,y) not in E or (x,z) not in E or (y,z) not in E:continue
  common=sorted(set(A[x])&set(A[y])&set(A[z]))
  for t,u in itertools.combinations(common,2):
   triangles+=1
   for q in range(3):
    c=[]
    for a,b in ((x,y),(x,z),(y,z)):
     c.extend((-B[q,a,b,t],-B[q,a,b,u]))
     c.extend(B[q,a,b,v] for v in set(A[a])&set(A[b])-{t,u})
    add(*c)
 matching=0
 for q in range(3):
  for (k,v),line in lines.items():
   if k==0 and v==0:continue
   off=[x for x in line if x>=8];M={}
   for x in off:
    for t in A[x]:M[x,t]=var();matching+=1
   for x in off:
    opts=[M[x,t] for t in A[x]];add(*opts)
    for t in A[x]:add(-M[x,t],P[q,x,t])
    for a,b in itertools.combinations(opts,2):add(-a,-b)
   for t in V:
    opts=[M[x,t] for x in off if t in A[x]]
    for a,b in itertools.combinations(opts,2):add(-a,-b)
 for q in range(3):
  N=[]
  for x in A:
   for t,u in itertools.combinations(A[x],2):
    v=var();N.append(v);add(-v,P[q,x,t]);add(-v,P[q,x,u])
  add(*N)
 # S3 symmetry: the three nonempty disjoint support minima at x=8 are
 # distinct, so a member permutation can put them in increasing order.
 symmetry=0;x=8
 for q in (0,1):
  for t,u in itertools.product(A[x],repeat=2):
   if t>u:
    add(*([-P[q,x,t],-P[q+1,x,u]]+[P[q,x,v] for v in A[x] if v<t]+[P[q+1,x,w] for w in A[x] if w<u]));symmetry+=1
 data=('p cnf %d %d\n'%(n,len(C))+''.join(' '.join(map(str,z))+' 0\n' for z in C)).encode('ascii')
 return data,{'variables':n,'clauses':len(C),'support_variables':len(P),'net_line_pairs':len(E),
             'conditional_two_axis_triangles':triangles,'matching_variables':matching,'member_order_clauses':symmetry,
             'formula_bytes':len(data),'formula_sha256':hashlib.sha256(data).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cnf',required=True);ap.add_argument('--receipt',required=True);a=ap.parse_args();start=time.monotonic()
 data,info=build(net.latin())
 with pathlib.Path(a.cnf).open('xb') as f:f.write(data)
 info.update({'result':'GENERATED_ONLY_NO_UNSAT_CLAIM','source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'latin_source_sha256':net.PIN,'latin_module_sha256':PIN,'elapsed_seconds':time.monotonic()-start,
              'limits':'Necessary q3 support/triangle/matching constraints only; other cross-cell product conditions omitted. SAT not physical; UNSAT needs independently checked proof and audit.'})
 with pathlib.Path(a.receipt).open('x',encoding='utf-8') as f:json.dump(info,f,indent=2);f.write('\n')
 print(json.dumps(info,indent=2))
if __name__=='__main__':main()
