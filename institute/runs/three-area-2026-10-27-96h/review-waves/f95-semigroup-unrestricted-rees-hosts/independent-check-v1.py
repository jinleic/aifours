#!/usr/bin/env python3
"""Independent exact checks of pinned Rees host claims (standard library only)."""
from itertools import product, permutations
from collections import Counter

def test_band(X, mul):
    assert all(mul(x,x)==x for x in X)
    assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(X,repeat=3))
    for e in X:
        C={mul(mul(e,x),e) for x in X}
        assert all(mul(mul(mul(mul(x,y),x),z),x)==mul(mul(mul(x,y),z),x) for x,y,z in product(C,repeat=3))
    return len(X)

def build_table(S, op):
    position={x:i for i,x in enumerate(S)}
    return [[position[op(x,y)] for y in S] for x in S]

def structure(S, table):
    n=len(S); E=[i for i in range(n) if table[i][i]==i]; eset=set(E)
    assert all(any(table[table[x][y]][x]==x and table[table[y][x]][y]==y for y in range(n)) for x in range(n))
    assert all(not (table[e][s]==e==table[s][e]) or s in eset for e in E for s in range(n))
    for e in E:
        local={table[table[e][x]][e] for x in range(n)}
        le=tuple(x for x in local if x in eset)
        assert all(table[x][y] in eset for x,y in product(le,repeat=2))
        assert all(table[table[table[table[x][y]][x]][z]][x]==table[table[table[x][y]][z]][x] for x,y,z in product(le,repeat=3))
    return E

def signatures(table):
    n=len(table); E=[table[i][i]==i for i in range(n)]; out=[]
    for s in range(n):
        v=bytearray()
        for a in range(-1,n):
            left=s if a<0 else table[a][s]
            v.append(E[left])
            v.extend(E[table[left][b]] for b in range(n))
        out.append(bytes(v))
    return out

def tau_check(S, stable, D, dtable, actor):
    ss=signatures(stable); ds=signatures(dtable); index={x:i for i,x in enumerate(D)}
    assert all((ss[i]==ss[j])==(ds[index[actor(S[i])]]==ds[index[actor(S[j])]]) for i in range(len(S)) for j in range(len(S)))
    assert all((stable[i][i]==i)==(dtable[index[actor(s)]][index[actor(s)]]==index[actor(s)]) for i,s in enumerate(S))
    return len(set(ss)),len(set(ds))

# Five-base multiplication is derived from (R right-zero) semidirect C2,
# rather than read from the candidate's multiplication table.
def a5(x,y):
    if x==4: return y
    if y==4: return x
    r,g=divmod(x,2); s,h=divmod(y,2)
    return 2*((g+s)%2)+(g+h)%2

def theta5(x): return 0 if x==4 else x%2

# Fixed B0 table is part of the definition, not a computed result.
B0=((0,2,2,4,4),(0,1,2,1,4),(0,2,2,2,4),(0,3,2,3,4),(0,4,2,4,4))
def m0(x,y): return B0[x][y]
test_band(tuple(range(5)),m0)
assert [{m0(m0(e,x),e) for x in range(5)} for e in range(5)]==[{0},{1,2,4},{2},{2,3,4},{4}]
assert any(m0(m0(m0(m0(x,y),x),z),x)!=m0(m0(m0(x,y),z),x) for x,y,z in product(range(5),repeat=3))
def tc(x,c,r):
    u=(1,3)[c]; v=(4,0)[r]
    return ((2,v),(v,4),(4,v),(v,2),(u,v))[x]
good=outside=fail=0
for r,d,p in [(r,d,4) for r,d in product(range(2),repeat=2)]+[(0,0,1),(1,0,3),(1,1,1),(0,1,3)]:
    for c,m,a,b in product(range(2),range(2),range(5),range(5)):
        shift=(theta5(a)+theta5(p))%2
        right=tc(b,d,m); right=right[::-1] if shift else right
        left=tc(a,c,r)
        rhs=(m0(left[0],right[0]),m0(left[1],right[1]))
        ok=tc(a5(a5(a,p),b),c,m)==rhs
        if (r,d,p)==(0,1,3): outside+=1; fail+=not ok
        else: good+=1; assert ok
assert (good,outside,fail)==(700,100,20)
print('triangular: B0 associative, locally regular but not globally regular; valid laws=700; excluded=100, failures=20')

def band5(P):
    m=len(P); n=len(P[0]); U=[('u',i) for i in range(n)]; V=[('v',j) for j in range(m)]; W=[('w',r) for r in range(2)]
    def f(j,i):
        x=P[j][i]
        return 1 if x==1 else 0 if x==3 else (i+j)%2
    def op(x,y):
        if y[0]!='u': return y
        return x if x[0]!='v' else W[f(x[1],y[1])]
    def coeff(s):
        i,a,j=s
        return ((W[0],V[j]),(V[j],W[1]),(W[1],V[j]),(V[j],W[0]),(U[i],V[j]))[a]
    return U+V+W,op,coeff

def source5(P):
    ni=len(P[0]); nl=len(P)
    S=list(product(range(ni),range(5),range(nl)))
    def sm(x,y): return (x[0],a5(a5(x[1],P[x[2]][y[0]]),y[1]),y[2])
    def actor(x): return (x[0],theta5(x[1]),x[2])
    D=list(product(range(ni),range(2),range(nl)))
    def dm(x,y): return (x[0],(x[1]+theta5(P[x[2]][y[0]])+y[1])%2,y[2])
    return S,sm,actor,D,dm

# All 2x2 matrices over all five base elements: direct comparison of the
# weak-E condition and the proposed allowed-matrix classification.
allowed=0; excluded=0; laws=0
for entries in product(range(5),repeat=4):
    P=(entries[:2],entries[2:]); S,sm,act,D,dm=source5(P); tab=build_table(S,sm)
    E=[k for k in range(len(S)) if tab[k][k]==k]; eset=set(E)
    weu=all(not (tab[e][x]==e==tab[x][e]) or x in eset for e in E for x in range(len(S)))
    admissible=all(p in (1,3,4) for p in entries)
    assert weu==admissible
    if not admissible: excluded+=1; continue
    allowed+=1; T,op,co=band5(P); test_band(T,op)
    assert len({(act(s),co(s)) for s in S})==len(S)
    for s,t in product(S,repeat=2):
        w=(theta5(s[1])+theta5(P[s[2]][t[0]]))%2
        z=co(t)[::-1] if w else co(t); y=co(s)
        assert co(sm(s,t))==(op(y[0],z[0]),op(y[1],z[1]))
        assert act(sm(s,t))==dm(act(s),act(t))
        laws+=1
assert (allowed,excluded,laws)==(81,544,32400)
print('five-base all 625 2x2 matrices: WEU iff allowed; 81 allowed bands, 32400 full host laws and fibre injections')

P5=((4,4,4),(4,1,3),(4,3,1))
T,op,co=band5(P5); test_band(T,op); S,sm,act,D,dm=source5(P5)
stab=build_table(S,sm); dtab=build_table(D,dm); E=structure(S,stab)
assert len({(act(s),co(s)) for s in S})==len(S)
for s,t in product(S,repeat=2):
    c=co(t); c=c[::-1] if (theta5(s[1])+theta5(P5[s[2]][t[0]]))%2 else c
    b=co(s)
    assert co(sm(s,t))==(op(b[0],c[0]),op(b[1],c[1]))
    assert act(sm(s,t))==dm(act(s),act(t))
assert not any(all(p==4 or (ct[i]<=rt[j] and p==(1 if rt[j]==ct[i] else 3)) for j,row in enumerate(P5) for i,p in enumerate(row)) for ct in product(range(2),repeat=3) for rt in product(range(2),repeat=3))
tauS,tauD=tau_check(S,stab,D,dtab,act)
print(f'five-base 3x3: source={len(S)}, idempotents={len(E)}, natural actor={len(D)}, tau classes={tauS}, all {len(S)**2} products; contexts={len(S)*(len(S)+1)**2}; row has 1 and 3; no triangular tags')

# S3 acts nontrivially on both rectangle coordinates: sign on L, natural on R.
G=tuple(permutations(range(3))); one=(0,1,2)
def compose(g,h): return tuple(g[h[k]] for k in range(3))
def inverse(g): return tuple(g.index(k) for k in range(3))
def parity(g): return sum(g[i]>g[j] for i in range(3) for j in range(i+1,3))%2
assert any(compose(g,h)!=compose(h,g) for g,h in product(G,repeat=2))
L=range(2); R=range(3); K=list(product(L,R))
def ka(k1,k2): return (k1[0],k2[1])
def kaction(g,k): return (k[0]^parity(g),g[k[1]])
assert all(kaction(g,ka(x,y))==ka(kaction(g,x),kaction(g,y)) for g,x,y in product(G,K,K))
assert all(kaction(compose(g,h),k)==kaction(g,kaction(h,k)) for g,h,k in product(G,G,K))
q=(1,2,0)
# First row and final column are units; active entries share q but have different K labels.
P=((None,None,None),((1,0,q),(0,2,q),None))
I=range(3); La=range(2); A=[None]+list(product(L,R,G)); S=list(product(I,A,La)); D=list(product(I,G,La))
def theta(a): return one if a is None else a[2]
def am(a,b):
    if a is None:return b
    if b is None:return a
    return (a[0],a[2][b[1]],compose(a[2],b[2]))
def sm(s,t): return (s[0],am(am(s[1],P[s[2]][t[0]]),t[1]),t[2])
def actor(s): return (s[0],theta(s[1]),s[2])
def dm(s,t): return (s[0],compose(compose(s[1],theta(P[s[2]][t[0]])),t[1]),t[2])
UR=[('ur',i) for i in I]; VR=[('vr',j,g) for j in La for g in G if g!=one]; WR=[('wr',r) for r in R]
UL=[('ul',j) for j in La]; VL=[('vl',i,g) for i in I for g in G if g!=one]; WL=[('wl',l) for l in L]
def mr(x,y):
    if y[0]!='ur': return y
    if x[0]!='vr': return x
    p=P[x[1]][y[1]]; label=inverse(x[2])[p[1]] if p is not None and p[2]==x[2] else 0
    return ('wr',label)
def ml(x,y):
    if y[0]!='ul': return y
    if x[0]!='vl': return x
    p=P[y[1]][x[1]]; label=p[0] if p is not None and p[2]==x[2] else 1
    return ('wl',label)
TR=UR+VR+WR; TL=UL+VL+WL; test_band(TR,mr); test_band(TL,ml)
def coeff(s):
    i,a,l=s; g=theta(a)
    right={k:(UR[i] if a is None else ('wr',inverse(g)[a[1]])) if k==g else ('vr',l,compose(inverse(g),k)) for k in G}
    left={k:(UL[l] if a is None else ('wl',a[0])) if k==one else ('vl',i,k) for k in G}
    return left,right

C={s:coeff(s) for s in S}
assert len({(actor(s),tuple(C[s][0][g] for g in G),tuple(C[s][1][g] for g in G)) for s in S})==len(S)
for s,t in product(S,repeat=2):
    w=compose(theta(s[1]),theta(P[s[2]][t[0]])); left,right=C[s]; left2,right2=C[t]; destL,destR=C[sm(s,t)]
    assert all(destL[k]==ml(left2[compose(k,w)],left[k]) for k in G)
    assert all(destR[k]==mr(right[k],right2[compose(inverse(w),k)]) for k in G)
    assert actor(sm(s,t))==dm(actor(s),actor(t))
stab=build_table(S,sm); dtab=build_table(D,dm); E=structure(S,stab); tauS,tauD=tau_check(S,stab,D,dtab,actor)
assert tauS==tauD
for l,r in product(L,R):
    bad=(l,r,one); s=(0,None,1); e=(0,bad,1)
    def badmul(x,y):
        pp=bad if (x[2],y[0])==(1,0) else P[x[2]][y[0]]
        return (x[0],am(am(x[1],pp),y[1]),y[2])
    assert badmul(s,s)==e and badmul(e,e)==e and badmul(e,s)==e==badmul(s,e) and s!=e
print(f'S3 rectangular: nonabelian, nontrivial actions on both L/R, TR={len(TR)}, TL={len(TL)}, source={len(S)}, idempotents={len(E)}, natural actor={len(D)}, tau classes={tauS}')
print(f'S3: both host laws and injection on all {len(S)**2} pairs; full source/context purity/tau check on {len(S)*(len(S)+1)**2} contexts; all six forbidden-idempotent WEU controls')
print('PASS: exact finite checks only; they do not prove arbitrary-index theorems or imported pushforward')
