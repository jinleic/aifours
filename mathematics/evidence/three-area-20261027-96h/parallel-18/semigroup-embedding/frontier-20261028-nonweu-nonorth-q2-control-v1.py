from itertools import product
D=list(product(range(2),repeat=3))

def dm(x,y):
    i,g,lam=x; j,h,mu=y
    return i, g ^ (lam & j) ^ h, mu

def group0(a,b):
    return 0 if a==0 or b==0 else 1 + ((a-1) ^ (b-1))

def hm(x,y):
    b,d,g=x; c,f,h=y
    return b & c, dm(d,f), g ^ h

def um(x,y):
    d,g=x; f,h=y
    return dm(d,f), group0(g,h)

def phi(x):
    b,d,g=x
    return d, (0 if b==0 else g+1)

H=list(product(range(2),D,range(2)))
U=list(product(D,range(3)))
assert len(H)==32 and len(U)==24
assert {phi(x) for x in H}==set(U)
assert all(phi(hm(x,y))==um(phi(x),phi(y)) for x,y in product(H,repeat=2))
EH=[x for x in H if hm(x,x)==x]
EU=[x for x in U if um(x,x)==x]
assert len(EH)==len(EU)==8 and len({phi(x) for x in EH})==len(EH)
assert all(any(um(um(x,y),x)==x and um(um(y,x),y)==y for y in U) for x in U)
e=((0,0,0),0); x=((0,0,0),2)
assert e in EU and um(e,x)==e and um(x,e)==e and um(x,x)!=x
p=((0,0,0),1); q=((1,1,1),1)
assert p in EU and q in EU and um(p,q) not in EU
print('H=32 U=24; 1024 homomorphism pairs; surjective and idempotent-separating on all 8 idempotents')
print('U regular, nonweak-E and nonorthodox with explicit idempotent witnesses')
