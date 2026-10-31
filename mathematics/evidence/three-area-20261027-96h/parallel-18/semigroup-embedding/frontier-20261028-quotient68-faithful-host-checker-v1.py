import json
from collections import deque
from itertools import product, combinations
from pathlib import Path

root=Path(__file__).resolve().parent
J=json.loads((root/'frontier-20261028-quotient68-faithful-host-data-v1.json').read_text())
B0=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4));sig=(0,3,4,1,2)
B=list(product(range(5),range(2)));D=list(product(range(2),repeat=3));H=list(product(B,D));lookup={x:i for i,x in enumerate(H)};N=len(H)
def dm(x,y):
 i,g,l=x;j,h,m=y;return i,g^(l&j)^h,m
def hm(x,y):
 (a,k),(i,g,l)=x;(b,r),(j,h,m)=y
 return (B0[a][sig[b] if g^(l&j) else b],k&r),dm(x[1],y[1])
MH=[[lookup[hm(x,y)] for y in H] for x in H]
assert len(H)==80 and all(MH[MH[x][y]][z]==MH[x][MH[y][z]] for x,y,z in product(range(N),repeat=3))
p=list(range(N));seed=(lookup[((0,0),(0,0,0))],lookup[((2,0),(0,0,0))]);todo=deque([seed])
def find(x):
 while p[x]!=x:p[x]=p[p[x]];x=p[x]
 return x
while todo:
 x,y=todo.popleft();i=find(x);j=find(y)
 if i==j:continue
 p[j]=i
 for k in range(N):todo.append((MH[x][k],MH[y][k]));todo.append((MH[k][x],MH[k][y]))
labels={};cls=[labels.setdefault(find(i),len(labels)) for i in range(N)]
assert cls==J['partition_labels'] and max(cls)+1==68
n=68;reps=[next(i for i,c in enumerate(cls) if c==j) for j in range(n)]
Q=[[cls[MH[i][j]] for j in reps] for i in reps];actor=[H[i][1] for i in reps]
assert Q==J['source_multiplication'] and [list(d) for d in actor]==J['actual_actor']
assert all(Q[cls[i]][cls[j]]==cls[MH[i][j]] for i,j in product(range(N),repeat=2))
assert len(set(actor))==8
E=[i for i in range(n) if Q[i][i]==i];ES=set(E)
assert len(E)==34
assert all((actor[i][1]==(actor[i][0]&actor[i][2]))==(i in ES) for i in range(n))
assert all(any(Q[Q[x][y]][x]==x and Q[Q[y][x]][y]==y for y in range(n)) for x in range(n))
assert all(not(Q[e][s]==e and Q[s][e]==e) or s in ES for e,s in product(E,range(n)))
nonorth=next((x,y,Q[x][y]) for x,y in product(E,repeat=2) if Q[x][y] not in ES)
nonli=None
for e in E:
 corner={Q[Q[e][x]][e] for x in range(n)};ce=[x for x in corner if x in ES];cs=set(ce)
 assert all(Q[x][y] in cs for x,y in product(ce,repeat=2))
 assert all(Q[Q[Q[Q[x][y]][x]][z]][x]==Q[Q[Q[x][y]][z]][x] for x,y,z in product(ce,repeat=3))
 if nonli is None:nonli=next(((e,x,y) for x,y in product(ce,repeat=2) if Q[x][y]!=Q[y][x]),None)
assert nonli is not None
ctx=[None]+D
signatures=[]
for d in D:
 sigd=[]
 for x,y in product(ctx,repeat=2):
  z=d if x is None else dm(x,d)
  if y is not None:z=dm(z,y)
  sigd.append(dm(z,z)==z)
 signatures.append(tuple(sigd))
assert len(set(signatures))==8
T=J['band_table'];flip=J['band_action'];C=J['coordinates']
assert len(T)==6 and len(flip)==6 and len(C)==n and all(len(c)==5 for c in C)
assert all(T[i][i]==i and flip[flip[i]]==i for i in range(6))
assert all(T[T[x][y]][z]==T[x][T[y][z]] for x,y,z in product(range(6),repeat=3))
assert all(T[T[T[T[x][y]][z]][w]][x]==T[T[T[T[T[T[x][y]][z]][x]][z]][w]][x] for x,y,z,w in product(range(6),repeat=4))
assert all(flip[T[x][y]]==T[flip[x]][flip[y]] for x,y in product(range(6),repeat=2))
for e in range(6):
 corner={T[T[e][x]][e] for x in range(6)}
 assert all(T[T[T[T[x][y]][x]][z]][x]==T[T[T[x][y]][z]][x] for x,y,z in product(corner,repeat=3))
assert T[T[T[T[2][5]][2]][3]][2]!=T[T[T[2][5]][3]][2]
assert T[1][0]==0 and T[0][1]==1 and T[1][3]==1 and T[0][3]==0 and T[4][1]==T[4][0] and 1!=0
assert all(not(B0[e][f]==f and B0[f][e]==e and B0[e][b]==e and B0[f][b]==f and B0[a][e]==B0[a][f]) or e==f for a,b,e,f in product(range(5),repeat=4))
assert all(actor[Q[i][j]]==dm(actor[i],actor[j]) for i,j in product(range(n),repeat=2))
for i,j in product(range(n),repeat=2):
 _,g,l=actor[i];row,_,_=actor[j];w=g^(l&row)
 assert all(C[Q[i][j]][k]==T[C[i][k]][flip[C[j][k]] if w else C[j][k]] for k in range(5))
pairs=[(i,j) for i,j in combinations(range(n),2) if actor[i]==actor[j]]
assert len(pairs)==256 and all(C[i]!=C[j] for i,j in pairs)
assert C[37]!=C[61] and actor[37]==actor[61] and Q[37][61]==61 and Q[61][37]==37
assert Q[0][37]==Q[0][61]==32 and Q[37][25]==37 and Q[61][25]==61
assert all(actor[i][1]^(actor[i][2]&actor[j][0])==0 for i,j in [(0,37),(0,61),(37,25),(61,25),(37,61),(61,37)])
print('PASS H80 associativity 512000; generated actor-preserving congruence; exact quotient S68 and 8-actor tables')
print('PASS S68 regular, weak-E, local-r; E=34; nonorth witness=',nonorth,' nonlocal-inverse=',nonli,sep='')
print('PASS actor context signatures=8/8, pure and onto: actual idempotence-context quotient')
print('PASS 6-band SN, C2 automorphism, 23120 coefficient products and 256 same-actor distinct pairs')
print('PASS B6 all six local corners regular, not globally regular; B5 quasiidentity checked in all 625 assignments')
print('same-actor R pair 37,61 separated:',C[37],C[61])
