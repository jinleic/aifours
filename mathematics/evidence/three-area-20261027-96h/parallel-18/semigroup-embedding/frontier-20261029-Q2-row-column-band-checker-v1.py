from itertools import product
from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parent;p=r/'frontier-20261028-quotient68-faithful-host-data-v1.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf';Q=json.loads(p.read_text())['source_multiplication']
def inspect(T):
 n=len(T);pr=list(range(n));pc=list(range(n))
 def root(p,x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 for x,y in product(range(n),repeat=2):pr[root(pr,T[x][y])]=root(pr,x);pc[root(pc,T[x][y])]=root(pc,y)
 E=[x for x in range(n) if T[x][x]==x];ans={}
 for side,p in [('row',pr),('col',pc)]:
  blocks={}
  for e in E:blocks.setdefault(root(p,e),[]).append(e)
  failures=[];closed=True
  for block in blocks.values():
   for x,y in product(block,repeat=2):
    if T[x][y] not in block:closed=False;failures.append({'closure_pair':[x,y]});break
   if not closed:continue
   for x,y,z,w in product(block,repeat=4):
    assert T[T[T[T[x][y]][z]][w]][x]==T[T[T[T[T[T[x][y]][z]][x]][z]][w]][x]
   bad=next(((x,y,z) for x,y,z in product(block,repeat=3) if T[T[T[T[x][y]][x]][z]][x]!=T[T[T[x][y]][z]][x]),None)
   if bad is not None:failures.append({'global_REG_failure':list(bad)})
  ans[side]={'E_block_sizes':sorted(map(len,blocks.values())),'closed':closed,'REG_failures':failures}
 return ans
print('S68 canonical row/col E bands:',json.dumps(inspect(Q),sort_keys=True))
# Literal B5 family x,u0,u1,v0,v1, independent of the nonband five-element A.
def b5(a,b):
 if b==0:return 0
 if a==0:return b+2 if b in (1,2) else b
 if a in (1,2):return a if b in (1,2) else b
 return a if b in (1,2) else b
B=[[b5(a,b) for b in range(5)] for a in range(5)]
assert all(B[x][x]==x for x in range(5))
assert all(B[B[x][y]][z]==B[x][B[y][z]] for x,y,z in product(range(5),repeat=3))
print('B5 canonical row/col E bands:',json.dumps(inspect(B),sort_keys=True))
