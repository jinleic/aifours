#!/usr/bin/env python3
"""Independent q2 base + arbitrary-support two-axis triangle clause audit."""
import argparse,collections,hashlib,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
SRC='frontier-20261028-source-wanless-max2-first-pair-v1.txt';PIN='710f00cc7ad78afa54987d1b57938b9d0e9ae3ba30589383b82ee652d0102dfd'
def facts():
 b=(H/SRC).read_bytes()
 if hashlib.sha256(b).hexdigest()!=PIN:raise ValueError('source pin')
 z=[s.strip() for s in b.decode('ascii').splitlines() if s.strip()]
 if z[0].split()[:3]!=['8','8','4254'] or len(z)!=17:raise ValueError('source layout')
 T=[[[ord(c)-97 for c in z[1+8*k+i]] for i in range(8)] for k in range(2)]
 for S in T:
  if any(sorted(row)!=list(range(8)) for row in S) or any(sorted(S[i][j] for i in range(8))!=list(range(8)) for j in range(8)):raise ValueError('Latin')
 if len({(T[0][i][j],T[1][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('MOLS')
 out={}
 for i in range(8):
  for j in range(8):out[8*i+j]=(i,j,*(T[k][0].index(T[k][i][j]) for k in range(2)))
 return out

def expected(f):
 V=range(8);A={x:tuple(t for t in V if t not in f[x][1:]) for x in range(8,64)}
 if any(len(x)!=5 for x in A.values()):raise ValueError('allowed')
 L=[[x for x in range(64) if f[x][k]==v] for k in range(4) for v in V]
 if any(len(x)!=8 for x in L):raise ValueError('net')
 n=0;clauses=[]
 def var():
  nonlocal n
  n+=1;return n
 def add(*x):clauses.append(tuple(sorted(x)))
 P={(q,x,t):var() for q in range(2) for x in sorted(A) for t in A[x]}
 for q in range(2):
  for x in sorted(A):add(*(P[q,x,t] for t in A[x]))
  for line in L:
   for t in V:
    if t in line:continue
    z=[x for x in line if x>=8 and t in A[x]]
    if len(z)!=5:raise ValueError('line coverage')
    add(*(P[q,x,t] for x in z))
 for x in sorted(A):
  for t in A[x]:add(-P[0,x,t],-P[1,x,t])
 def adj(x,y):return any(a==b for a,b in zip(f[x],f[y]))
 E=[(x,y) for x,y in itertools.combinations(range(8,64),2) if adj(x,y)]
 if len(E)!=700:raise ValueError('net edge count')
 B={}
 for q in range(2):
  for x,y in E:
   common=sorted(set(A[x])&set(A[y]))
   if len(common)==1:
    t=common[0];add(-P[q,x,t],-P[q,y,t]);continue
   if len(common)<2:continue
   for t in common:B[q,x,y,t]=var()
   for t in common:
    b=B[q,x,y,t];add(-b,P[q,x,t]);add(-b,P[q,y,t]);add(b,-P[q,x,t],-P[q,y,t])
   for t in common:add(-B[q,x,y,t],*(B[q,x,y,u] for u in common if u!=t))
 for q in range(2):
  N=[]
  for x in sorted(A):
   for t,u in itertools.combinations(A[x],2):
    v=var();N.append(v);add(-v,P[q,x,t]);add(-v,P[q,x,u])
  add(*N)
 nt=0
 # Direct three-cell iteration, not producer graph-neighbor iteration.
 for x,y,z in itertools.combinations(range(8,64),3):
  if not(adj(x,y) and adj(x,z) and adj(y,z)):continue
  common3=sorted(set(A[x])&set(A[y])&set(A[z]))
  for t,u in itertools.combinations(common3,2):
   nt+=1
   for q in range(2):
    C=[]
    for i,j in ((x,y),(x,z),(y,z)):
     C.extend((-B[q,i,j,t],-B[q,i,j,u]))
     C.extend(B[q,i,j,a] for a in sorted(set(A[i])&set(A[j])) if a not in (t,u))
    add(*C)
 return n,collections.Counter(clauses),nt

def parse(b):
 L=b.decode('ascii').splitlines();h=L[0].split()
 if h[:2]!=['p','cnf']:raise ValueError('header')
 n,m=map(int,h[2:]);C=[]
 for line in L[1:]:
  z=[int(v) for v in line.split()]
  if not z or z[-1]!=0 or 0 in z[:-1] or any(abs(k)>n for k in z[:-1]):raise ValueError('clause')
  C.append(tuple(sorted(z[:-1])))
 if len(C)!=m:raise ValueError('clause count')
 return n,collections.Counter(C)

def main():
 p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 data=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(data).hexdigest()!=a.cnf_sha:raise ValueError('formula hash')
 n,C,t=expected(facts());m,D=parse(data)
 if n!=m or C!=D:raise ValueError('clause multiset mismatch')
 k=next(iter(D));mut=D.copy();mut[k]-=1
 if mut[k]==0:del mut[k]
 if mut==C:raise ValueError('clause omission not rejected')
 out={'result':'PASS_INDEPENDENT_Q2_FULL_CLAUSE_MULTISET',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'formula_sha256':a.cnf_sha,'source_pair_sha256':PIN,'variables':n,'clauses':sum(C.values()),
      'four_net_pairs':700,'candidate_axis_triangles':t,'added_triangle_clauses':2*t,
      'omitted_clause_mutation':'rejected','elapsed_seconds':time.monotonic()-start,
      'limits':'Independent encoder audit only; q2 physical reduction, native proof and source claims require separate review.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
