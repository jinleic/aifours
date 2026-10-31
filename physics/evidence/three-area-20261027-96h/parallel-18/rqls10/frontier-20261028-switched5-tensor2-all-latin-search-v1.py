#!/usr/bin/env python3
"""Complete single-intercalate QLS5 tensor classical QLS2 transversal scan.

Uses only exact ray orthogonality and XOR constraints; arbitrary nontrivial
2x2 unitary rotations have the same ray-orthogonality pattern. Any SAT result
needs original-vector reconstruction; no SAT is scoped to this family.
"""
import collections,datetime,hashlib,itertools,json
from pathlib import Path
P=Path(__file__).resolve().parent
n=5;perms=list(itertools.permutations(range(n)));squares=[]
def latin(rows):
 if len(rows)==n:squares.append(tuple(rows));return
 r=len(rows)
 for row in perms:
  if row[0]!=r:continue
  if all(all(row[c]!=x[c]for x in rows)for c in range(n)):latin(rows+[row])
latin([tuple(range(n))]);assert len(squares)==56

def intercalates(M):
 return [(r,s,c,d,M[r][c],M[r][d])for r,s in itertools.combinations(range(n),2)for c,d in itertools.combinations(range(n),2)if M[r][c]==M[s][d] and M[r][d]==M[s][c]]
def pairgood(A,B):
 occ=[(0,r,c)for r,c in A]+[(1,r,c)for r,c in B];adj=[[]for _ in range(10)]
 for axis in (1,2):
  for z in range(5):
   v=[i for i,x in enumerate(occ)if x[axis]==z]
   assert len(v)==2
   i,j=v;parity=1 if axis==1 else 1^occ[i][0]^occ[j][0];adj[i].append((j,parity));adj[j].append((i,parity))
 val=[None]*10
 for i in range(10):
  if val[i]is not None:continue
  val[i]=0;todo=[i]
  while todo:
   x=todo.pop()
   for y,p in adj[x]:
    t=val[x]^p
    if val[y]is None:val[y]=t;todo.append(y)
    elif val[y]!=t:return None
 return [(r,val[i],c,t^val[i])for i,(t,r,c) in enumerate(occ)]
case_count=eligible_total=candidate_total=0;found=[];hist=collections.Counter();stream=P/'frontier-20261028-switched5-tensor2-all-latin-search-v1.jsonl'
with stream.open('w') as out:
 for index,M in enumerate(squares):
  for r,s,c,d,a,b in intercalates(M):
   case_count+=1;T=[[M[i][j]for j in range(n)]for i in range(n)];T[r][c]=T[s][d]=5;T[r][d]=T[s][c]=6
   buckets={q:[(i,j)for i in range(n)for j in range(n)if T[i][j]==q]for q in range(7)}
   other=[q for q in range(5)if q not in (a,b)];groups=[(a,b,*other),(5,6,*other)]
   choices=[];by=collections.defaultdict(list)
   for basis in groups:
    for Q in itertools.product(*(buckets[q]for q in basis)):
     rr=tuple(sum(x==i for x,y in Q)for i in range(n));cc=tuple(sum(y==i for x,y in Q)for i in range(n))
     if max(rr)<=2 and max(cc)<=2:choices.append((Q,rr,cc));by[rr+cc].append(Q)
   eligible_total+=len(choices);cand=0;witness=None
   for Q,rr,cc in choices:
    target=tuple(2-x for x in rr+cc)
    for V in by.get(target,[]):
     cand+=1;sol=pairgood(Q,V)
     if sol is not None:
      witness=sol;found.append({'square_index':index,'square':M,'intercalate':[r,s,c,d,a,b],'transversal':sol});break
    if witness:break
   candidate_total+=cand;hist[(len(choices),cand)]+=1
   out.write(json.dumps({'square_index':index,'intercalate':[r,s,c,d,a,b],'eligible':len(choices),'pairs_checked':cand,'found':witness is not None},separators=(',',':'))+'\n')
obj={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'stream_sha256':hashlib.sha256(stream.read_bytes()).hexdigest(),
 'clock_finish':datetime.datetime.now().astimezone().isoformat(),'reduced_latin_squares':len(squares),'single_switch_cases':case_count,
 'eligible_local_cliques':eligible_total,'candidate_pairs_checked':candidate_total,'found':found,
 'scope':'Only one nontrivial 2x2 intercalate switch of a classical Latin5 followed by tensor with the classical Latin2. No general QLS10 conclusion.'}
(P/'frontier-20261028-switched5-tensor2-all-latin-search-v1.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
