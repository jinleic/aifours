#!/usr/bin/env python3
"""Direct nonabelian S3 verification of arbitrary-P evaluation-band lift."""
from itertools import product,permutations
G=tuple(permutations(range(3)));idx={g:i for i,g in enumerate(G)};e=idx[(0,1,2)]
def comp(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(idx[comp(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(6) if M[g][h]==e==M[h][g]) for g in range(6))
u=idx[(1,0,2)];v=idx[(0,2,1)];assert M[u][v]!=M[v][u]
R=range(3);A=(None,)+tuple(product(R,range(6)))
def theta(a):return e if a is None else a[1]
def am(a,b):
 if a is None:return b
 if b is None:return a
 return(G[a[1]][b[0]],M[a[1]][b[1]])

def run(P,collapsed):
 ni=3;nl=3
 U=tuple(('u',i) for i in range(ni));W=tuple(('w',r) for r in R)
 V=tuple(('v',l,g) for l in range(nl) for g in range(6) if g!=e);T=U+V+W
 def selector(l,g,i):
  p=P[l][i]
  return G[inv[g]][p[0]] if p is not None and p[1]==g else 0
 def tm(a,b):
  if b[0]!='u':return b
  if a[0] in ('u','w'):return a
  return W[selector(a[1],a[2],b[1])]
 assert all(tm(x,x)==x for x in T)
 assert all(tm(tm(x,y),z)==tm(x,tm(y,z)) for x,y,z in product(T,repeat=3))
 for a in T:
  local={tm(tm(a,x),a) for x in T}
  assert all(tm(tm(tm(tm(x,y),x),z),x)==tm(tm(tm(x,y),z),x) for x,y,z in product(local,repeat=3))
 S=tuple(product(range(ni),A,range(nl)))
 def sm(a,b):return(a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
 def beta(a):
  i,x,l=a;g=theta(x);mark=U[i] if x is None else W[G[inv[g]][x[0]]]
  return tuple(mark if k==g else ('v',l,M[inv[g]][k]) for k in range(6))
 def shift(g,F):return tuple(F[M[inv[g]][k]] for k in range(6))
 def bm(F,H):return tuple(tm(x,y) for x,y in zip(F,H))
 def actor(s):return(s[0],theta(s[1]),s[2])
 def ra(a,b):return(a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
 def weight(a,b):return M[theta(a[1])][theta(P[a[2]][b[0]])]
 for a,b in product(S,repeat=2):
  assert beta(sm(a,b))==bm(beta(a),shift(weight(a,b),beta(b)))
  assert actor(sm(a,b))==ra(actor(a),actor(b))
  assert a==b or actor(a)!=actor(b) or beta(a)!=beta(b)
 E={a for a in S if sm(a,a)==a}
 assert all((a in E)==(ra(actor(a),actor(a))==actor(a)) for a in S)
 assert all(any(sm(sm(a,b),a)==a and sm(sm(b,a),b)==b for b in S) for a in S)
 for s in S:
  assert not ({sm(a,s) for a in E}&{sm(s,a) for a in E}&E) or s in E
 for a in E:
  local={sm(sm(a,x),a) for x in S};le=tuple(x for x in local if x in E)
  assert all(sm(x,y) in E for x,y in product(le,repeat=2))
  assert all(sm(sm(sm(sm(x,y),x),z),x)==sm(sm(sm(x,y),z),x) for x,y,z in product(le,repeat=3))
 if collapsed:
  collapse=(0,1,1)
  def q(s):return(collapse[s[0]],theta(s[1]),collapse[s[2]])
  def qp(a,b):return(a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
  for a,b in product(S,repeat=2):
   assert q(sm(a,b))==qp(q(a),q(b))
   assert a==b or q(a)!=q(b) or (a[0],a[2])!=(b[0],b[2]) or beta(a)!=beta(b)
 else:q=actor
 contexts=(None,)+S
 def ctx(a,s,b):
  x=s if a is None else sm(a,s)
  return x if b is None else sm(x,b)
 sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
 assert all((sig[a]==sig[b])==(q(a)==q(b)) for a,b in product(S,repeat=2))
 print('collapsed=',collapsed,' source=',len(S),' T=',len(T),' natural_actor=',len(set(map(actor,S))),' actual_actor=',len(set(map(q,S))),sep='')
 print('PASS T associative/local regular; 29241 source/host products+injection; purity, regularity, WEU, local-r, 172^2 contexts/source')
 if collapsed:print('PASS retained-rectangle host over actual q, all29241 comparisons')

# Each has one row with distinct labels at the SAME nontrivial group element.
P1=((None,None,None),(None,(0,u),(1,u)),(None,(2,u),(0,v)))
P2=((None,None,None),(None,(0,u),(1,u)),(None,(2,u),(0,u)))
run(P1,False);run(P2,True)
for r in R:
 p=(r,e);s=(1,None,1);P=((None,None,None),(None,p,None),(None,None,None))
 def bad(a,b):return(a[0],am(am(a[1],P[a[2]][b[0]]),b[1]),b[2])
 x=bad(s,s);assert x!=s and bad(x,x)==x and bad(x,s)==x==bad(s,x)
print('CONTROL all3 forbidden identity-group nonunit sandwiches give explicit WEU violation')
print('LIMIT finite same-author checks; arbitrary-group proof is symbolic')
