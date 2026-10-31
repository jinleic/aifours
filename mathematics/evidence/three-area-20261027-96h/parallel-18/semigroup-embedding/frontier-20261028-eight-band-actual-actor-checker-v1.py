#!/usr/bin/env python3
"""Direct exact check of the literal eight-band physical host (no solver)."""
from itertools import product
A=range(5)
T=((0,1,2,3,0),(3,2,1,0,1),(0,1,2,3,2),(3,2,1,0,3),(0,1,2,3,4))
P=((4,4,4),(4,1,4),(4,4,3))
th=(0,1,0,1,0)
B=((0,1,7,0,6,0,6,7),
   (0,1,1,7,1,6,6,7),
   (0,1,2,7,1,5,6,7),
   (0,1,7,3,4,0,6,7),
   (0,1,1,3,4,6,6,7),
   (0,1,2,0,6,5,6,7),
   (0,1,1,0,6,6,6,7),
   (0,1,7,7,1,0,6,7))
act=(1,0,3,2,5,4,6,7)
beta=((0,0,7),(6,6,0),(6,6,1),(1,1,7),(5,5,2))
S=tuple(product(range(3),A,range(3)))
def sm(a,b):return (a[0],T[T[a[1]][P[a[2]][b[0]]]][b[1]],b[2])
def q(s):return (s[0],th[s[1]],s[2])
def qm(a,b):return (a[0],(a[1]+th[P[a[2]][b[0]]]+b[1])%2,b[2])
def bm(a,b):return B[a][b]
def coef(s):return beta[s[1]][s[2]]
def mult_band(s,t,action=act):
    w=(th[s[1]]+th[P[s[2]][t[0]]])%2
    v=coef(t)
    return bm(coef(s),action[v] if w else v)
assert all(bm(a,a)==a for a in range(8))
assert all(bm(bm(a,b),c)==bm(a,bm(b,c)) for a,b,c in product(range(8),repeat=3))
assert all(bm(bm(bm(bm(a,b),a),c),a)==bm(bm(bm(a,b),c),a)
           for a,b,c in product(range(8),repeat=3))
assert all(act[act[a]]==a for a in range(8))
assert all(act[bm(a,b)]==bm(act[a],act[b]) for a,b in product(range(8),repeat=2))
assert any(act[a]!=a for a in range(8))
for s,t in product(S,repeat=2):
    assert q(sm(s,t))==qm(q(s),q(t))
    assert coef(sm(s,t))==mult_band(s,t)
    assert s==t or q(s)!=q(t) or coef(s)!=coef(t)
E={s for s in S if sm(s,s)==s}
assert all((s in E)==(q(s)==qm(q(s),q(s))) for s in S)
contexts=(None,)+S
def ctx(a,s,b):
    x=s if a is None else sm(a,s)
    return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in E for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(q(s)==q(t)) for s,t in product(S,repeat=2))
nontriv=sum(coef(sm(s,t))!=mult_band(s,t,tuple(range(8))) for s,t in product(S,repeat=2))
assert nontriv>0
# Distinct p and x share the actor: suppressing their different band values breaks injection.
collapsed=lambda s: beta[1][s[2]] if s[1]==3 else coef(s)
collisions=sum(1 for s,t in product(S,repeat=2) if s!=t and q(s)==q(t) and collapsed(s)==collapsed(t))
assert collisions>0
print('B_size=8 source_size=45 actor_size=',len(set(map(q,S))),' source_idempotents=',len(E),sep='')
print('PASS all512 B associativity+regular-band laws; 64 automorphism products; involution')
print('PASS all2025 source/actor/host products; all2025 same-actor injectivity comparisons')
print('PASS 46^2 source contexts per element; actual q_tau and purity')
print('CONTROL trivial action fails source products=',nontriv,'; p/x coefficient collapse causes ordered collisions=',collisions,sep='')
print('LIMIT exact same-author finite witness, not all-source SEP or independent review')
