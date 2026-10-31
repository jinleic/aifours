from itertools import product
from collections import Counter
from pathlib import Path
import json,hashlib

def forced_blocks(T,variety='SN'):
 n=len(T);E=[x for x in range(n) if T[x][x]==x];ES=set(E);par={e:e for e in E};steps=[]
 def root(e):
  while par[e]!=e:par[e]=par[par[e]];e=par[e]
  return e
 def merge(a,b,why):
  x,y=root(a),root(b)
  if x==y:return False
  par[y]=x;steps.append([a,b,why]);return True
 for e,f in product(E,repeat=2):
  if T[e][f]==T[f][e]==e:merge(e,f,['comparable',e,f])
 while True:
  changed=False
  for e,f in product(E,repeat=2):
   if root(e)!=root(f):continue
   p=T[e][f]
   if p not in ES:return {'outcome':'OBSTRUCTION','reason':'nonidempotent forced block product','pair':[e,f],'product':p,'merges':steps}
   changed=merge(e,p,['block-product',e,f]) or changed
  if not changed:break
 C={}
 for e in E:C.setdefault(root(e),[]).append(e)
 for block in C.values():
  assert all(T[e][f] in block for e,f in product(block,repeat=2))
  if variety=='SL':
   for x,y in product(block,repeat=2):
    if T[x][y]!=T[y][x]:return {'outcome':'OBSTRUCTION','reason':'forced block noncommutative','pair':[x,y],'merges':steps}
  for x,y,z,w in product(block,repeat=4):
   l=T[T[T[T[x][y]][z]][w]][x];q=T[T[T[T[T[T[x][y]][z]][x]][z]][w]][x]
   if l!=q:return {'outcome':'OBSTRUCTION','reason':'forced block violates SN','quad':[x,y,z,w],'merges':steps}
 return {'outcome':'NECESSARY TEST PASSES ONLY','block_sizes':sorted(map(len,C.values())),'merges':steps}
D=list(product(range(2),repeat=3))
def dm(a,b):
 i,g,l=a;j,h,m=b;return(i,g^(l&j)^h,m)
def add(kind):
 S=D+[kind]
 def m(a,b):
  if a==kind:return kind if kind=='zero' else b
  if b==kind:return kind if kind=='zero' else a
  return dm(a,b)
 return [[S.index(m(a,b)) for b in S] for a in S]
R={}
for name in ['zero','one']:
 T=add(name);assert all(T[T[x][y]][z]==T[x][T[y][z]] for x,y,z in product(range(9),repeat=3));R['D8^'+name]=forced_blocks(T);assert R['D8^'+name]['outcome']=='OBSTRUCTION'
T=[[D.index(dm(a,b)) for b in D] for a in D];R['D8']=forced_blocks(T);assert R['D8']['block_sizes']==[1]*4
r=Path(__file__).resolve().parent;p=r/'frontier-20261028-quotient68-faithful-host-data-v1.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf';T=json.loads(p.read_text())['source_multiplication'];R['S68']=forced_blocks(T);assert R['S68']['outcome'].startswith('NECESSARY')
N=[[0,0,0],[0,1,1],[0,2,2]];R['N3_SN']=forced_blocks(N);R['N3_SL']=forced_blocks(N,'SL');assert R['N3_SN']['block_sizes']==[3] and R['N3_SL']['outcome']=='OBSTRUCTION'
for k,v in R.items():print(k,{a:b for a,b in v.items() if a!='merges'},'merge_count',len(v['merges']))
