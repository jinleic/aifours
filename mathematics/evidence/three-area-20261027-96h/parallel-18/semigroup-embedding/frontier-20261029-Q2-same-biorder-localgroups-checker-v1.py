from itertools import product
D=list(product(range(2),repeat=3));S=D+['zero'];B=list(product(range(2),repeat=2))+['zero'];H=list(product(B,range(2)))
def m(x,y,twist):
 if x=='zero' or y=='zero':return 'zero'
 i,g,l=x;j,h,u=y;return(i,g^((l&j) if twist else 0)^h,u)
def neg(x,y):return m(x,y,True)
def pos(x,y):return m(x,y,False)
def bm(x,y):return 'zero' if x=='zero' or y=='zero' else(x[0],y[1])
def hm(x,y):return(bm(x[0],y[0]),x[1]^y[1])
def cover(x):
 b,g=x;return 'zero' if b=='zero' else(b[0],g,b[1])
def phi(x):return 'zero' if x=='zero' else(x[0],x[1]^(x[2]&x[0]),x[2])
def forget(x):return 'zero' if x=='zero' else(x[0],x[2])
EN={x for x in S if neg(x,x)==x};EP={x for x in S if pos(x,x)==x};EH={x for x in H if hm(x,x)==x}
assert len(EN)==len(EP)==len(EH)==5 and set(map(phi,EN))==EP
assert set(map(cover,H))==set(S) and len(set(map(cover,EH)))==5
assert all(cover(hm(x,y))==pos(cover(x),cover(y)) for x,y in product(H,repeat=2))
for mult in [neg,pos]:
 assert all(mult(mult(x,y),z)==mult(x,mult(y,z)) for x,y,z in product(S,repeat=3))
 E={e for e in S if mult(e,e)==e}
 assert all(any(mult(mult(x,y),x)==x and mult(mult(y,x),y)==y for y in S) for x in S)
 for e in E:
  C={mult(mult(e,x),e) for x in S};EC=C&E
  assert all(mult(x,y)==mult(y,x) in EC for x,y in product(EC,repeat=2))
 assert all(forget(mult(x,y))==bm(forget(x),forget(y)) for x,y in product(S,repeat=2))
 assert len(set(map(forget,E)))==5
# Full regular-biordered-set data: all four Green preorders and every basic product.
basiccount=0
for e,f in product(EN,repeat=2):
 en,fn=neg(e,f),neg(f,e);a,b=phi(e),phi(f);ap,bp=pos(a,b),pos(b,a)
 signs=(en==e,en==f,fn==e,fn==f);assert signs==(ap==a,ap==b,bp==a,bp==b)
 if any(signs):assert en in EN and phi(en)==ap;basiccount+=1
 def sandwich(mult,e,f):
  p=mult(e,f);V=[v for v in S if mult(mult(p,v),p)==p and mult(mult(v,p),v)==v]
  return {mult(mult(f,v),e) for v in V}
 W=sandwich(neg,e,f);Z=sandwich(pos,a,b);assert len(W)==len(Z)==1 and {phi(w) for w in W}==Z
# Abstract local groups and the complete Green R/L/J eggbox agree under phi.
for i,l in product(range(2),repeat=2):
 C=[(i,g,l) for g in range(2)]
 assert all(phi(neg(x,y))==pos(phi(x),phi(y)) for x,y in product(C,repeat=2))
for mult in [neg,pos]:
 for x in S:
  right={x}|{mult(x,y) for y in S};left={x}|{mult(y,x) for y in S};two={x}|right|left|{mult(mult(a,x),b) for a,b in product(S,repeat=2)}
  if mult is neg:
   assert {phi(y) for y in right}==({phi(x)}|{pos(phi(x),y) for y in S})
   assert {phi(y) for y in left}==({phi(x)}|{pos(y,phi(x)) for y in S})
   assert {phi(y) for y in two}==({phi(x)}|{pos(phi(x),y) for y in S}|{pos(y,phi(x)) for y in S}|{pos(pos(a,phi(x)),b) for a,b in product(S,repeat=2)})
assert all(bm(bm(bm(x,y),z),x)==bm(bm(bm(x,z),y),x) for x,y,z in product(B,repeat=3))
assert neg((0,0,0),(1,1,1)) not in EN and all(neg('zero',e)==neg(e,'zero')=='zero' for e in EN)
assert all(pos(e,f) in EP for e,f in product(EP,repeat=2))
print('PASS negative9/positive9:1458associativity,regular,locallyinverse;normalband-byC2 host10 ->positive9 ALL100products/idsep')
print('PASS E-biorder5 isomorphic:25four-preordercomparisons,',basiccount,'basicproducts,ALL25singleton sandwich sets')
print('PASS four corresponding maximalgroups C2 plusbottom trivialgroup andcomplete R/L/J principalidealdata agree under explicitbijection')
print('PASS both haveidseponto samepositive normalband5;negative9 hasNONCLOSED E=upper0,positive9 hasclosednormal E')
print('RESULT Q2eligibilitycannotdependONLYonEbiorder/pseudosemilattice+abstractlocalgroups/Greeneggbox;cross-cellmultiplication/curvatureremainsessential')
