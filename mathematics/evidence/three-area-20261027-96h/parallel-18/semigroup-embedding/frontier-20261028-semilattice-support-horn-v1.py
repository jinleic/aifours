from itertools import product
from collections import deque

A=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
th=(0,1,0,1,0)
P=((4,4,4),(4,1,3),(4,4,1))
S=list(product(range(3),range(5),range(3)))
idx={s:i for i,s in enumerate(S)}
def mul(s,t): return s[0],A[A[s[1]][P[s[2]][t[0]]]][t[1]],t[2]
def q(s): return s[0],th[s[1]],s[2]
def var(u,s): return u*len(S)+idx[s]
def idem(s): return mul(s,s)==s
def le(s,t): return mul(s,t)==s and mul(t,s)==s

n=2*len(S)
unary=[set() for _ in range(n)]
binary=[[] for _ in range(n)]
relations=[]
for u,s,t in product(range(2),S,S):
    z=var(u,mul(s,t)); x=var(u,s); y=var(u ^ th[s[1]] ^ th[P[s[2]][t[0]]],t)
    relations.append((z,x,y))
    unary[z].update((x,y))
    binary[x].append((y,z)); binary[y].append((x,z))

def close(start):
    seen={start}; queue=deque([start])
    while queue:
        a=queue.popleft()
        for b in unary[a]:
            if b not in seen: seen.add(b); queue.append(b)
        for b,z in binary[a]:
            if b in seen and z not in seen: seen.add(z); queue.append(z)
    return seen

closures=[close(i) for i in range(n)]
E=[s for s in S if idem(s)]
comparable=[(a,b) for a,b in product(E,repeat=2) if a!=b and q(a)==q(b) and le(a,b)]
separated=[(a,b) for a,b in comparable if var(0,a) not in closures[var(0,b)]]
for a,b in separated:
    zeros=closures[var(0,b)]
    assert all((z in zeros)==((x in zeros) and (y in zeros)) for z,x,y in relations)
    assert var(0,b) in zeros and var(0,a) not in zeros
collapsed=[(a,b) for a,b in comparable if (a,b) not in separated]
rl=[(a,b) for a,b in product(E,repeat=2) if a!=b and q(a)==q(b) and ((mul(a,b)==a and mul(b,a)==b) or (mul(a,b)==b and mul(b,a)==a))]
assert rl and all(var(0,a) in closures[var(0,b)] and var(0,b) in closures[var(0,a)] for a,b in rl)
print('source=',len(S),'group=2 variables=',n,'relations=',len(relations),'idempotents=',len(E),sep='')
print('same-actor ordered comparable pairs=',len(comparable),'semilattice-separated=',len(separated),'semilattice-collapsed=',len(collapsed),sep='')
print('same-actor ordered distinct R/L pairs=',len(rl),'all semilattice-collapsed=',True,sep='')
if collapsed: print('collapsed example=',collapsed[0])
if separated: print('separated example=',separated[0])
