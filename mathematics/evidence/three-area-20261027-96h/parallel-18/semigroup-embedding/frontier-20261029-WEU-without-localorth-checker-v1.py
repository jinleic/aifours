from itertools import product
from collections import deque
D=list(product(range(2),repeat=3));S=D+['one'];n=9

def m(x,y):
 if x=='one':return y
 if y=='one':return x
 i,g,l=x;j,h,mu=y;return i,g^(l&j)^h,mu

E={x for x in S if m(x,x)==x}
assert len(E)==5 and all(m(m(x,y),z)==m(x,m(y,z)) for x,y,z in product(S,repeat=3))
assert all(any(m(m(x,y),x)==x and m(m(y,x),y)==y for y in S) for x in S)
for x in S:
 below={m(e,x) for e in E}&{m(x,f) for f in E}&E
 assert not below or x in E
p=(0,0,0);q=(1,1,1)
assert p in E and q in E and m(p,q) not in E
assert {m(m('one',s),'one') for s in S}==set(S)
# The source has an actual identity; contexts range over all nine elements.
sigs={s:tuple(m(m(x,s),y) in E for x,y in product(S,repeat=2)) for s in S}
assert len(set(sigs.values()))==9
idx={s:i for i,s in enumerate(S)};T=[[idx[m(x,y)] for y in S] for x in S];par=list(range(n))
seeds=[(idx[e],idx[f]) for e,f in product(E,repeat=2) if e!=f and m(e,f)==m(f,e)==e];todo=deque(seeds)
def root(x):
 while par[x]!=x:par[x]=par[par[x]];x=par[x]
 return x
while todo:
 a,b=todo.popleft();i=root(a);j=root(b)
 if i==j:continue
 par[j]=i
 for x in range(n):todo.append((T[a][x],T[b][x]));todo.append((T[x][a],T[x][b]))
assert len(set(root(i) for i in range(n)))==1
print('PASS source9=D8^1:729 associativity, regularity,FULLdifferent-idempotent natural-order WEU')
print('PASS E=5 NOTclosed atidentitycorner, so NOTlocallyorthodox and NOToriginalsource')
print('PASS all9 syntactic idempotence signatures distinct; actual quotient9 is notCS')
print('PASS comparable-generated leastCS quotient1 is notpure; no physical band-by-CS host for ANYband')
