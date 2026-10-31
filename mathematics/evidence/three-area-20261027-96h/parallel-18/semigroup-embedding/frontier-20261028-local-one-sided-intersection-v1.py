from collections import deque
from itertools import product
import json
from pathlib import Path

def congruence(T,seeds):
 n=len(T);p=list(range(n));todo=deque(seeds)
 def root(x):
  while p[x]!=x:p[x]=p[p[x]];x=p[x]
  return x
 while todo:
  a,b=todo.popleft();i=root(a);j=root(b)
  if i==j:continue
  p[j]=i
  for x in range(n):todo.append((T[a][x],T[b][x]));todo.append((T[x][a],T[x][b]))
 return [root(i) for i in range(n)]
def analyse(T,label):
 n=len(T);E=[i for i in range(n) if T[i][i]==i];left=set();right=set()
 for z in E:
  ce={T[T[z][x]][z] for x in range(n)}&set(E)
  for e,f in product(ce,repeat=2):
   efe=T[T[e][f]][e]
   if efe!=T[e][f]:left.add((efe,T[e][f]))
   if efe!=T[f][e]:right.add((efe,T[f][e]))
 L=congruence(T,left);R=congruence(T,right)
 common=[(i,j) for i in range(n) for j in range(i) if L[i]==L[j] and R[i]==R[j]]
 print(label,'size=',n,' localLRB quotient=',len(set(L)),' localRRB quotient=',len(set(R)),' nontrivial intersection pairs=',len(common),sep='')
 if common:print('FIRST',common[0])
 return L,R,common
r=Path(__file__).resolve().parent
J=json.loads((r/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
analyse(J['source_multiplication'],'S68 ')
B=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
S=list(product(range(5),repeat=2));ix={x:i for i,x in enumerate(S)}
T=[[ix[(B[x[0]][y[0]],B[y[1]][x[1]])] for y in S] for x in S]
analyse(T,'B5xB5op ')
