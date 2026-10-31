from itertools import product
Y=range(4);V=list(product(Y,range(2)));swap=[0,2,1,3]
def tm(x,y):
 a,g=x;b,h=y;return(a&(swap[b] if g else b),g^h)
def rep(x):
 a,g=x;return tuple(i^g if a&(1<<(i^g)) else -1 for i in range(2))
def comp(f,h):return tuple(-1 if h[i]==-1 else f[h[i]] for i in range(2))
I=sorted(set(map(rep,V)));assert len(I)==7
assert all(rep(tm(x,y))==comp(rep(x),rep(y)) for x,y in product(V,repeat=2))
assert all(tm(tm(x,y),z)==tm(x,tm(y,z)) for x,y,z in product(V,repeat=3))
EV={x for x in V if tm(x,x)==x};EI={x for x in I if comp(x,x)==x}
assert len(EV)==len(EI)==4 and len({rep(x) for x in EV})==4
assert all((x in EV)==(x[1]==0) for x in V)
assert all(tm(x,y)==tm(y,x) in EV for x,y in product(EV,repeat=2))
assert all(any(tm(tm(x,y),x)==x and tm(tm(y,x),y)==y for y in V) for x in V)
assert all(not ({tm(e,x) for e in EV}&{tm(x,f) for f in EV}&EV) or x in EV for x in V)
assert all(len([y for y in I if comp(comp(x,y),x)==x and comp(comp(y,x),y)==y])==1 for x in I)
for e in EI:
 C={comp(comp(e,s),e) for s in I};EC=C&EI
 assert all(comp(x,y)==comp(y,x) in EC for x,y in product(EC,repeat=2))
zero=(-1,-1);sigma=(1,0)
assert zero in EI and sigma not in EI and comp(zero,sigma)==comp(sigma,zero)==zero
print('PASS 8-element Eunitary inverse host Y4⋊C2, FULLorderWEU, pure ontoC2 withSLkernel')
print('PASS onto idempotent-separating cover of I2(size7), ALL64multiplicativity equations')
print('PASS I2 inverse/locallysemilattice, but0<=nonidempotent fullswap, hence NOTWEU')
print('RESULT standard cover-defined SL Malcev G already contains regularnonWEU I2; it is NOT the direct pure-CS kernel class')
