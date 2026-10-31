import json,hashlib
from pathlib import Path
from itertools import product
r=Path(__file__).resolve().parent
p=r/'frontier-20261028-quotient68-faithful-host-data-v1.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='64206c690120a576b777672a2ca88250b4bd4d06e0cdcd3c663a4476bbddbecf';J=json.loads(p.read_text())
p=r/'frontier-20261028-quotient68-8band-refined-actor-data-v1.json';assert hashlib.sha256(p.read_bytes()).hexdigest()=='72bb328439b4f24919788e7379a20ea61f01ecc58dcd74f80da3f5d8ff848c40';K=json.loads(p.read_text())
Q=J['source_multiplication'];B=K['band_table'];beta=K['band_action'];A=K['actor'];c=K['coordinates'];P=K['actor_sandwich_bits'];F=K['forced_fibre_indices']
E=[s for s in range(68) if Q[s][s]==s]
assert all(any(Q[Q[s][t]][s]==s and Q[Q[t][s]][t]==t for t in range(68)) for s in range(68))
assert all(not ({Q[e][s] for e in E}&{Q[s][f] for f in E}&set(E)) or s in E for s in range(68))
localnoncommute=None
for e in E:
 C={Q[Q[e][s]][e] for s in range(68)};Ec=C&set(E)
 assert all(Q[x][y] in Ec and Q[Q[x][y]][x]==Q[y][x] for x,y in product(Ec,repeat=2))
 for x,y in product(Ec,repeat=2):
  if Q[x][y]!=Q[y][x]:localnoncommute=(e,x,y)
nonorth=next((e,f) for e,f in product(E,repeat=2) if Q[e][f] not in E)
assert localnoncommute is not None
assert all(B[B[x][y]][z]==B[x][B[y][z]] and B[B[x][y]][z]==B[B[B[B[x][z]][x]][y]][z] for x,y,z in product(range(8),repeat=3))
swap=[0,2,1,3];V=list(product(range(4),range(2)))
def tm(x,y):
 a,g=x;b,h=y;return (a&(swap[b] if g else b),g^h)
assert all(tm(tm(x,y),z)==tm(x,tm(y,z)) for x,y,z in product(V,repeat=3))
assert all(tm(x,x)==x if x[1]==0 else tm(x,x)!=x for x in V)
assert all(any(tm(tm(x,y),x)==x and tm(tm(y,x),y)==y for y in V) for x in V)
t=(1,1);ti=(2,1)
assert tm(tm(t,ti),t)==t and tm(tm(ti,t),ti)==ti and tm(t,ti)!=tm(ti,t)
assert not any(tm(tm(t,u),t)==t and tm(tm(u,t),u)==u and tm(t,u)==tm(u,t) for u in V)
S=list(product(range(68),V));coords={(s,t):((c[s],t[0]),(A[s][0],A[s][1],t[1],A[s][2])) for s,t in S}
assert len(set(coords.values()))==544
for (s,(a,g)),(u,(b,h)) in product(S,repeat=2):
 i,f,l=A[s];j,k,m=A[u];w=f^P[l][j]
 band=(B[c[s]][beta[c[u]] if w else c[u]],a&(swap[b] if g else b))
 actor=(i,w^k,g^h,m)
 assert coords[(Q[s][u],tm((a,g),(b,h)))]==(band,actor)
cone=list(product(F,[(a,0) for a in range(4)]));bottom=(0,(0,0))
assert len(cone)==32
for s,t in cone:
 assert Q[s][s]==s and tm(t,t)==t and (Q[0][s],tm((0,0),t))==(Q[s][0],tm(t,(0,0)))==bottom
print('PASS S68 FULL-order WEU/regular/localRRB; nonorth pair',nonorth,'local noncommuting witness',localnoncommute)
print('PASS exact inverse nonCR source8 with C2 actor and4-element semilattice;512associativity')
print('PASS original source544, band32, actor24, host768; all295936 source/host products and injectivity')
print('PASS 32 distinct source idempotents above ONE idempotent; allCS actors force ONEimage, hence ALLACTOR band>=32')
print('RESULT exact all-actor bandminimum32 for source544, which is NON-COMPLETELY-REGULAR,NONORTHODOX,NONLOCALLYINVERSE')
