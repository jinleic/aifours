#!/usr/bin/env python3
"""Independent clause-multiset reconstruction for a q1 support formula."""
import argparse,collections,hashlib,itertools,json,pathlib,time
H=pathlib.Path(__file__).parent
P=[('frontier-20261028-source-wanless-max3-order8-v1.txt','95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67',114),
   ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt','f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5',3)]
def parse_nets():
 nets=[]
 for name,pin,n in P:
  b=(H/name).read_bytes()
  if hashlib.sha256(b).hexdigest()!=pin:raise ValueError('input pin')
  lines=[x.strip() for x in b.decode('ascii').splitlines() if x.strip()]
  if lines[0].split()[:3]!=['8','8',str(n)] or len(lines)!=1+8*n:raise ValueError('input count')
  S=[[[ord(z)-97 for z in lines[1+8*k+i]] for i in range(8)] for k in range(n)]
  for B in S:
   if any(sorted(x)!=list(range(8)) for x in B) or any(sorted(B[i][j] for i in range(8))!=list(range(8)) for j in range(8)):raise ValueError('not Latin')
  for k in range(0,n,3):
   T=S[k:k+3]
   for a,b in itertools.combinations(range(3),2):
    if len({(T[a][i][j],T[b][i][j]) for i in range(8) for j in range(8)})!=64:raise ValueError('not MOLS')
   nets.append([(i,j,T[0][i][j],T[1][i][j],T[2][i][j]) for i in range(8) for j in range(8)])
 return nets

def reconstruct(points,r,c,anchor):
 rowvals=[anchor]+[i for i in range(8) if i!=anchor];other=[i for i in range(5) if i not in (r,c)]
 def point(i,j):
  z=[p for p in points if p[r]==rowvals[i] and p[c]==j]
  if len(z)!=1:raise ValueError('not OA2')
  return z[0]
 first=[point(0,j) for j in range(8)];facts={}
 for i in range(8):
  for j in range(8):
   p=point(i,j);labels=[]
   for q in other:
    z=[k for k in range(8) if first[k][q]==p[q]]
    if len(z)!=1:raise ValueError('firstrow')
    labels.append(z[0])
   facts[8*i+j]=(i,j,*labels)
 return facts

def expected(facts):
 A={x:tuple(k for k in range(8) if k not in facts[x][1:]) for x in range(8,64)}
 if any(len(z)!=4 for z in A.values()):raise ValueError('allowed count')
 lines=[[x for x in range(64) if facts[x][k]==v] for k in range(5) for v in range(8)]
 if any(len(z)!=8 for z in lines):raise ValueError('net lines')
 n=0;clauses=[]
 def var():
  nonlocal n
  n+=1;return n
 def add(*z):clauses.append(tuple(sorted(z)))
 P={(x,t):var() for x in sorted(A) for t in A[x]}
 for x in sorted(A):add(*(P[x,t] for t in A[x]))
 for line in lines:
  for t in range(8):
   if t in line:continue
   z=[x for x in line if x>=8 and t in A[x]]
   if len(z)!=4:raise ValueError('axis coverage')
   add(*(P[x,t] for x in z))
 def adj(x,y):return any(a==b for a,b in zip(facts[x],facts[y]))
 E=[(x,y) for x,y in itertools.combinations(range(8,64),2) if adj(x,y)]
 if len(E)!=868:raise ValueError('edge count')
 for x,y in E:
  C=sorted(set(A[x])&set(A[y]))
  if len(C)==1:add(-P[x,C[0]],-P[y,C[0]])
  elif len(C)>=2:
   B={t:var() for t in C}
   for t in C:
    b=B[t];add(-b,P[x,t]);add(-b,P[y,t]);add(b,-P[x,t],-P[y,t])
   for t in C:add(-B[t],*(B[u] for u in C if u!=t))
 triangles=[]
 for x,y,z in itertools.combinations(range(8,64),3):
  if not(adj(x,y) and adj(y,z) and adj(x,z)):continue
  C=set(A[x])&set(A[y])
  if len(C)==2 and C==set(A[y])&set(A[z]) and C==set(A[x])&set(A[z]):
   t,u=sorted(C);triangles.append((x,y,z,t,u))
   add(-P[x,t],-P[x,u],-P[y,t],-P[y,u],-P[z,t],-P[z,u])
 N=[]
 for x in sorted(A):
  for t,u in itertools.combinations(A[x],2):
   z=var();N.append(z);add(-z,P[x,t]);add(-z,P[x,u])
 add(*N)
 return n,collections.Counter(clauses),len(triangles)

def parse_cnf(b):
 n=m=None;C=[]
 for line in b.decode('ascii').splitlines():
  z=line.split()
  if not z or z[0]=='c':continue
  if z[0]=='p':
   if n is not None or len(z)!=4 or z[1]!='cnf':raise ValueError('header')
   n,m=int(z[2]),int(z[3]);continue
  q=list(map(int,z))
  if n is None or not q or q[-1]!=0 or 0 in q[:-1] or any(abs(t)>n for t in q[:-1]):raise ValueError('clause')
  C.append(tuple(sorted(q[:-1])))
 if n is None or m!=len(C):raise ValueError('count')
 return n,collections.Counter(C)

def main():
 p=argparse.ArgumentParser();p.add_argument('--cnf',required=True);p.add_argument('--cnf-sha',required=True);p.add_argument('--species',type=int,required=True);p.add_argument('--row-class',type=int,required=True);p.add_argument('--column-class',type=int,required=True);p.add_argument('--anchor',type=int,required=True);p.add_argument('--output',required=True);a=p.parse_args();start=time.monotonic()
 b=pathlib.Path(a.cnf).read_bytes()
 if hashlib.sha256(b).hexdigest()!=a.cnf_sha:raise ValueError('formula hash')
 nets=parse_nets()
 if len(nets)!=39 or a.species not in range(39) or a.row_class not in range(5) or a.column_class not in range(5) or a.column_class==a.row_class or a.anchor not in range(8):raise ValueError('case')
 facts=reconstruct(nets[a.species],a.row_class,a.column_class,a.anchor)
 n,C,nt=expected(facts);m,D=parse_cnf(b)
 if n!=m or C!=D:raise ValueError('formula clauses do not match')
 # A checker of multiset equality must reject omissions, additions, and sign changes.
 key=next(iter(D));omit=D.copy();omit[key]-=1
 if omit[key]==0:del omit[key]
 add=D.copy();add[(1,)]+=1
 flipped=D.copy();flipped[key]-=1
 if flipped[key]==0:del flipped[key]
 changed=tuple(sorted((-key[0],*key[1:])));flipped[changed]+=1
 if omit==C or add==C or flipped==C:raise ValueError('mutation undetected')
 out={'result':'PASS_INDEPENDENT_FULL_CNF_CLAUSE_MULTISET',
      'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      'formula_sha256':a.cnf_sha,'case':[a.species,a.row_class,a.column_class,a.anchor],
      'variables':n,'clauses':sum(C.values()),'two_axis_triangles':nt,
      'mutations':{'omitted_clause':'rejected','added_clause':'rejected','flipped_literal':'rejected'},
      'elapsed_seconds':time.monotonic()-start,
      'limits':'Checks the encoding against stated support/triangle clauses only; mathematical necessity, Hcat and proof checker remain separate.'}
 with pathlib.Path(a.output).open('x',encoding='utf-8') as h:json.dump(out,h,indent=2);h.write('\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
