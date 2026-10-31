from collections import deque
from itertools import product, combinations

B=range(3)  # 0=identity, 1/2 right-zero
D=list(product(range(2), repeat=3))
H=list(product(B,D)); N=len(H); hi={x:i for i,x in enumerate(H)}

def band(a,b): return b if b else a
def act(g,b): return (3-b if b else 0) if g else b
def dm(x,y):
    i,g,l=x;j,h,m=y;return i,g^(l&j)^h,m
def hm(x,y):
    a,(i,g,l)=x;b,(j,h,m)=y
    return band(a,act(g^(l&j),b)),dm(x[1],y[1])
M=[[hi[hm(x,y)] for y in H] for x in H]

def quotient(a,b):
    p=list(range(N))
    def root(i):
        while p[i]!=i:
            p[i]=p[p[i]];i=p[i]
        return i
    def union(i,j):
        i=root(i);j=root(j)
        if i!=j:p[j]=i;return True
        return False
    union(a,b)
    changed=True
    while changed:
        changed=False
        for i in range(N):
            for j in range(i):
                if root(i)==root(j):
                    for k in range(N):
                        changed=union(M[k][i],M[k][j]) or changed
                        changed=union(M[i][k],M[j][k]) or changed
    roots=[root(i) for i in range(N)]
    labels={}
    cls=[labels.setdefault(r,len(labels)) for r in roots]
    n=len(labels)
    reps=[next(i for i,c in enumerate(cls) if c==k) for k in range(n)]
    Q=[[cls[M[i][j]] for j in reps] for i in reps]
    actor=[H[i][1] for i in reps]
    assert all(actor[cls[i]]==H[i][1] for i in range(N))
    assert all(Q[cls[i]][cls[j]]==cls[M[i][j]] for i,j in product(range(N), repeat=2))
    return Q,actor,tuple(cls)

def analyse(Q,actor):
    n=len(Q); E=[i for i in range(n) if Q[i][i]==i]
    assert all((actor[i][1]==(actor[i][0]&actor[i][2]))==(i in E) for i in range(n))
    assert all(any(Q[Q[x][y]][x]==x and Q[Q[y][x]][y]==y for y in range(n)) for x in range(n))
    unary=[set() for _ in range(2*n)]; pairs=[[] for _ in range(2*n)]
    def v(u,s): return u*n+s
    for u,s,t in product(range(2),range(n),range(n)):
        i,g,l=actor[s];j,h,mu=actor[t]
        z=v(u,Q[s][t]);x=v(u,s);y=v(u^g^(l&j),t)
        unary[z].update((x,y));pairs[x].append((y,z));pairs[y].append((x,z))
    def close(start):
        seen={start}; todo=deque([start])
        while todo:
            a=todo.popleft()
            for b in unary[a]:
                if b not in seen: seen.add(b);todo.append(b)
            for b,c in pairs[a]:
                if b in seen and c not in seen: seen.add(c);todo.append(c)
        return seen
    cache={}
    comps=[(x,y) for x,y in product(E,repeat=2) if x!=y and actor[x]==actor[y] and Q[x][y]==x and Q[y][x]==x]
    fails=[]
    for x,y in comps:
        if y not in cache:cache[y]=close(v(0,y))
        if v(0,x) in cache[y]:fails.append((x,y))
    orthodox=all(Q[x][y] in E for x,y in product(E,repeat=2))
    local_inverse=True
    for e in E:
        corner={Q[Q[e][x]][e] for x in range(n)}
        ce=[x for x in corner if Q[x][x]==x]
        if any(Q[x][y]!=Q[y][x] for x,y in product(ce,repeat=2)):local_inverse=False
    return len(E),len(comps),fails,orthodox,local_inverse

candidates=[]
for d in D:
    cell=[hi[(b,d)] for b in B]
    candidates.extend(combinations(cell,2))
seen={}
for a,b in candidates:
    Q,actor,partition=quotient(a,b)
    if partition not in seen:seen[partition]=(len(Q),analyse(Q,actor),(H[a],H[b]))
print('24 actor-compatible single-pair generators; distinct congruences=',len(seen),sep='')
for size,(ne,nc,fail,orth,li),pair in sorted(seen.values(),key=repr):
    print('size=',size,' E=',ne,' comparable=',nc,' failures=',len(fail),' orthodox=',orth,' locally_inverse=',li,' generator=',pair,sep='')
print('TOTAL comparable-collapses=',sum(len(data[1][2]) for data in seen.values()),'; no universal conclusion',sep='')
