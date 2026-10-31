#!/usr/bin/env python3
"""Independent single-switch tensor replay: original vectors, BK, GF2 elimination."""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
base=tuple(range(5));pool={i:[x for x in itertools.permutations(range(5))if x[0]==i]for i in range(1,5)}
squares=[]
for rows in itertools.product(*(pool[i]for i in range(1,5))):
 M=(base,)+rows
 if all(len({M[r][c]for r in range(5)})==5 for c in range(5)):squares.append(M)
assert len(squares)==56

def inter(M):
 return [(r,s,c,d,M[r][c],M[r][d])for r in range(5)for s in range(r+1,5)for c in range(5)for d in range(c+1,5)if M[r][c]==M[s][d] and M[r][d]==M[s][c]]
def basis(i):return tuple(5*int(j==i)for j in range(5))
def bitcliques(adj):
 out=[]
 def bk(R,C,X,depth):
  if depth+C.bit_count()<5:return
  if depth==5:out.append(tuple(i for i in range(25)if R>>i&1));return
  T=C|X;p=-1;best=-1
  while T:
   x=T&-T;T-=x;i=x.bit_length()-1;s=(C&adj[i]).bit_count()
   if s>best:best=s;p=i
  T=C if p<0 else C&~adj[p]
  while T:
   x=T&-T;T-=x;i=x.bit_length()-1;bk(R|x,C&adj[i],X&adj[i],depth+1);C&=~x;X|=x
 bk(0,(1<<25)-1,0,0);return out

def solvable(Q,V):
 occ=[(0,x)for x in Q]+[(1,x)for x in V];equations=[]
 for axis in (0,1):
  for k in range(5):
   ids=[i for i,(t,x) in enumerate(occ)if (x//5 if axis==0 else x%5)==k];assert len(ids)==2
   i,j=ids;rhs=1 if axis==0 else 1^occ[i][0]^occ[j][0];equations.append((1<<i)|(1<<j)|(rhs<<10))
 piv={}
 for x in equations:
  while x&1023:
   k=(x&1023&-(x&1023)).bit_length()-1
   if k in piv:x^=piv[k]
   else:piv[k]=x;break
  if (x&1023)==0 and x>>10:return False
 return True
stream=P/'frontier-20261028-switched5-tensor2-independent-v1.jsonl';cases=elig=checked=sat=0
with stream.open('w') as out:
 for M in squares:
  for r,s,c,d,a,b in inter(M):
   cases+=1;Q=[[basis(M[i][j])for j in range(5)]for i in range(5)]
   u=list([0]*5);v=list([0]*5);u[a]=3;u[b]=4;v[a]=-4;v[b]=3
   Q[r][c]=Q[s][d]=tuple(u);Q[r][d]=Q[s][c]=tuple(v)
   for row in Q:
    for x in row:assert sum(t*t for t in x)==25
   G=[x for row in Q for x in row];adj=[0]*25
   for i,j in itertools.combinations(range(25),2):
    if sum(a*b for a,b in zip(G[i],G[j]))==0:adj[i]|=1<<j;adj[j]|=1<<i
   cls=bitcliques(adj);choices=[];by=collections.defaultdict(list)
   for C in cls:
    rr=tuple(sum(x//5==i for x in C)for i in range(5));cc=tuple(sum(x%5==i for x in C)for i in range(5))
    if max(rr)<=2 and max(cc)<=2:choices.append((C,rr,cc));by[rr+cc].append(C)
   elig+=len(choices);count=0;witness=False
   for C,rr,cc in choices:
    for D in by.get(tuple(2-x for x in rr+cc),[]):
     count+=1
     if solvable(C,D):witness=True;break
    if witness:break
   sat+=witness;checked+=count
   out.write(json.dumps({'square':M,'intercalate':[r,s,c,d,a,b],'eligible':len(choices),'pairs_checked':count,'found':witness},separators=(',',':'))+'\n')
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(stream.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'reduced_latin_squares':len(squares),'single_switch_cases':cases,
 'eligible_local_cliques':elig,'candidate_pairs_checked':checked,'found_cases':sat,'status':'PASS' if sat==0 else 'SAT_FOUND',
 'scope':'Replays only a single nontrivial intercalate rotation, local5 tensor classical2; nontrivial unitary rotations share this exact orthogonality graph.'}
(P/'frontier-20261028-switched5-tensor2-independent-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
