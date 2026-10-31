#!/usr/bin/env python3
"""Exact S3 check of two-sided rectangular-band evaluation Rees host."""
from itertools import product,permutations
G=tuple(permutations(range(3)));idx={g:i for i,g in enumerate(G)};e=idx[(0,1,2)]
def compose(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(idx[compose(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(6) if M[g][h]==e==M[h][g]) for g in range(6))
u=idx[(1,0,2)];v=idx[(0,2,1)];assert M[u][v]!=M[v][u]
L=range(2);R=range(3);A=(None,)+tuple(product(L,R,range(6)))
def theta(a):return e if a is None else a[2]
def am(a,b):
 if a is None:return b
 if b is None:return a
 return(a[0],G[a[2]][b[1]],M[a[2]][b[2]])
P=((None,None,None),(None,(0,1,u),(1,2,u)))
ni,nl=3,2;S=tuple(product(range(ni),A,range(nl)))
def sm(a,b):return(a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
# Right evaluation band TR.
UR=tuple(('ur',i) for i in range(ni));WR=tuple(('wr',r) for r in R)
VR=tuple(('vr',l,q) for l in range(nl) for q in range(6) if q!=e);TR=UR+VR+WR
def rm(a,b):
 if b[0]!='ur':return b
 if a[0] in ('ur','wr'):return a
 p=P[a[1]][b[1]];q=a[2]
 return ('wr',G[inv[q]][p[1]] if p is not None and p[2]==q else 0)
# Left evaluation band TL, used with opposite multiplication.
UL=tuple(('ul',l) for l in range(nl));WL=tuple(('wl',x) for x in L)
VL=tuple(('vl',i,q) for i in range(ni) for q in range(6) if q!=e);TL=UL+VL+WL
def lm(a,b):
 if b[0]!='ul':return b
 if a[0] in ('ul','wl'):return a
 p=P[b[1]][a[1]];q=a[2]
 return ('wl',p[0] if p is not None and p[2]==q else 0)
for T,m in ((TR,rm),(TL,lm)):
 assert all(m(x,x)==x for x in T)
 assert all(m(m(x,y),z)==m(x,m(y,z)) for x,y,z in product(T,repeat=3))
 for e0 in T:
  corner={m(m(e0,x),e0) for x in T}
  assert all(m(m(m(m(x,y),x),z),x)==m(m(m(x,y),z),x) for x,y,z in product(corner,repeat=3))
def br(s):
 i,a,l=s;g=theta(a);mark=UR[i] if a is None else WR[G[inv[g]][a[1]]]
 return tuple(mark if k==g else ('vr',l,M[inv[g]][k]) for k in range(6))
def bl(s):
 i,a,l=s;mark=UL[l] if a is None else WL[a[0]]
 return tuple(mark if k==e else ('vl',i,k) for k in range(6))
def ar(g,F):return tuple(F[M[inv[g]][k]] for k in range(6))
def al(g,F):return tuple(F[M[k][g]] for k in range(6))
def pr(F,H):return tuple(rm(x,y) for x,y in zip(F,H))
def pl(F,H):return tuple(lm(y,x) for x,y in zip(F,H))
def actor(s):return(s[0],theta(s[1]),s[2])
def multactor(a,b):return(a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
def weight(a,b):return M[theta(a[1])][theta(P[a[2]][b[0]])]
collapse=(0,1,1)
def qa(s):return(collapse[s[0]],theta(s[1]),s[2])
def qp(a,b):return(a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
for a,b in product(S,repeat=2):
 c=sm(a,b);w=weight(a,b)
 assert br(c)==pr(br(a),ar(w,br(b)))
 assert bl(c)==pl(bl(a),al(w,bl(b)))
 assert actor(c)==multactor(actor(a),actor(b)) and qa(c)==qp(qa(a),qa(b))
 assert a==b or actor(a)!=actor(b) or br(a)!=br(b) or bl(a)!=bl(b)
 assert a==b or qa(a)!=qa(b) or (a[0],a[2])!=(b[0],b[2]) or br(a)!=br(b) or bl(a)!=bl(b)
E={a for a in S if sm(a,a)==a}
assert all((s in E)==(multactor(actor(s),actor(s))==actor(s)) for s in S)
assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in S) for a in S)
for s in S:assert not ({sm(a,s) for a in E}&{sm(s,a) for a in E}&E) or s in E
for a in E:
 local={sm(sm(a,x),a) for x in S};le=tuple(x for x in local if x in E)
 assert all(sm(x,y) in E for x,y in product(le,repeat=2))
 assert all(sm(sm(sm(sm(x,y),x),z),x)==sm(sm(sm(x,y),z),x) for x,y,z in product(le,repeat=3))
contexts=(None,)+S
def ctx(a,s,b):
 x=s if a is None else sm(a,s)
 return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[a]==sig[b])==(qa(a)==qa(b)) for a,b in product(S,repeat=2))
for l,r in product(L,R):
 p=(l,r,e);badP=((None,None,None),(None,p,None))
 def bad(a,b):return(a[0],am(am(a[1],badP[a[2]][b[0]]),b[1]),b[2])
 s=(1,None,1);x=bad(s,s)
 assert x!=s and bad(x,x)==x and bad(x,s)==x==bad(s,x)
print('group S3 noncommutative; rectangle 2x3; source=',len(S),' natural_actor=',len(set(map(actor,S))),' actual_actor=',len(set(map(qa,S))),sep='')
print('TR=',len(TR),' TL=',len(TL),' source_idempotents=',len(E),sep='')
print('PASS both evaluation bands associative/local regular; all49284 left/right host product laws and actor-fibre injection')
print('PASS source regular/WEU/local-r, purity, retained rectangle, 223^2 contexts/source')
print('CONTROL all6 forbidden identity-group nonunit sandwiches violate WEU')
print('LIMIT finite same-author checks; arbitrary rectangular/group proof is symbolic')
