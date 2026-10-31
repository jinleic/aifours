#!/usr/bin/env python3
"""Exact S3/nontrivial-action check for the row-coded Rees host construction."""
from itertools import product, permutations
G=tuple(permutations(range(3))); n=len(G); one=G.index((0,1,2))
idx={g:i for i,g in enumerate(G)}
def compose(g,h):return tuple(g[h[x]] for x in range(3))
M=tuple(tuple(idx[compose(g,h)] for h in G) for g in G)
inv=tuple(next(h for h in range(n) if M[g][h]==one==M[h][g]) for g in range(n))
u=idx[(1,0,2)];v=idx[(0,2,1)]
assert M[u][v]!=M[v][u]
R=range(3); top=3
A=(None,)+tuple(product(R,range(n)))
def theta(a):return one if a is None else a[1]
def am(a,b):
    if a is None:return b
    if b is None:return a
    return (G[a[1]][b[0]],M[a[1]][b[1]])
P=((None,None,None),(None,(0,u),(1,v)),(None,(2,u),(0,v)))
S=tuple(product(range(3),A,range(3)))
def sm(s,t,P=P):return (s[0],am(am(s[1],P[s[2]][t[0]]),t[1]),t[2])
def labels(P):
    result=[]
    for row in P:
        d={}
        for p in row:
            if p is None:continue
            r,g=p
            assert g!=one and (g not in d or d[g]==r)
            d[g]=r
        result.append(tuple(d.get(g,0) for g in range(n)))
    return tuple(result)
L=labels(P)
def beta(s,L=L):
    a=s[1];g=theta(a);lam=s[2]
    return tuple((top if a is None else a[0]) if k==g
                 else G[g][L[lam][M[inv[g]][k]]] for k in range(n))
def action(g,b):
    return tuple(top if b[M[inv[g]][k]]==top else G[g][b[M[inv[g]][k]]]
                 for k in range(n))
def bm(b,c):return tuple(x if y==top else y for x,y in zip(b,c))
def actor(s):return (s[0],theta(s[1]),s[2])
def actor_mul(a,b):return (a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
def weight(s,t,P=P):return M[theta(s[1])][theta(P[s[2]][t[0]])]
def idem(s):return sm(s,s)==s
E=tuple(s for s in S if idem(s))
assert all(any(sm(sm(s,t),s)==s and sm(sm(t,s),t)==t for t in S) for s in S)
assert all(not ({sm(e,s) for e in E}&{sm(s,e) for e in E}&set(E)) or idem(s) for s in S)
for e in E:
    local={sm(sm(e,s),e) for s in S}
    es=tuple(s for s in local if idem(s))
    assert all(idem(sm(a,b)) for a,b in product(es,repeat=2))
    assert all(sm(sm(sm(sm(a,b),a),c),a)==sm(sm(sm(a,b),c),a) for a,b,c in product(es,repeat=3))
assert all(idem(s)==(actor_mul(actor(s),actor(s))==actor(s)) for s in S)
for s,t in product(S,repeat=2):
    assert actor(sm(s,t))==actor_mul(actor(s),actor(t))
    assert beta(sm(s,t))==bm(beta(s),action(weight(s,t),beta(t)))
    assert s==t or actor(s)!=actor(t) or beta(s)!=beta(t)

# These two source columns have identical group sandwich rows, but different R-labels.
# Their actor quotient coalesces them; its physical host retains the old rectangle.
col=(0,1,1)
def target(s):return (s[0],theta(s[1]),col[s[2]])
def tmul(a,b):return (a[0],M[M[a[1]][theta(P[a[2]][b[0]])]][b[1]],b[2])
for s,t in product(S,repeat=2):
    assert target(sm(s,t))==tmul(target(s),target(t))
    oldrect=(s[0],s[2]);newrect=(t[0],t[2])
    rectprod=(oldrect[0],newrect[1])
    assert rectprod==(sm(s,t)[0],sm(s,t)[2])
    assert s==t or target(s)!=target(t) or oldrect!=newrect or beta(s)!=beta(t)
# Verify the true source tau against the 36-element target by every actual/absent context.
contexts=(None,)+S
Eset=set(E)
def ctx(a,s,b):
    x=s if a is None else sm(a,s)
    return x if b is None else sm(x,b)
sig={s:bytes(ctx(a,s,b) in Eset for a,b in product(contexts,repeat=2)) for s in S}
assert all((sig[s]==sig[t])==(target(s)==target(t)) for s,t in product(S,repeat=2))
# Break row-label uniqueness using two distinct labels at the same group weight.
badP=((None,None,None),(None,(0,u),(1,u)),(None,(2,u),(0,v)))
s=(0,None,1);t=(2,None,0)
assert beta(sm(s,t,badP))!=bm(beta(s),action(weight(s,t,badP),beta(t)))
print('G=S3 order6, noncommuting generators=',u,v,'; R=3 nontrivial permutation action')
print('source=',len(S),' idempotents=',len(E),' original_actor=',len(set(map(actor,S))),' actual_tau_actor=',len(set(map(target,S))),sep='')
print('PASS regular, weak-E, all local orthodox/regular-band corners; actor purity')
print('PASS all29241 source/actor/physical-host products and same-actor injections')
print('PASS actual quotient and retained-rectangle host, full 172^2 contexts per source')
print('CONTROL same-row same-weight different labels breaks the displayed coefficient law')
print('LIMIT exact finite same-author check; not all-row ambiguity or all-original-source theorem')
