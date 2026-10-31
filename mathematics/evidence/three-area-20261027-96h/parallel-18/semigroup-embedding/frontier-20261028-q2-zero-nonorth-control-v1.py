from itertools import product
D=list(product(range(2),repeat=3))
ZERO='z'
S=D+[ZERO]

def mul(x,y):
    if x==ZERO or y==ZERO:
        return ZERO
    i,g,lam=x; j,h,mu=y
    return i, g ^ (lam & j) ^ h, mu

assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(S,repeat=3))
E=[x for x in S if mul(x,x)==x]
assert len(S)==9 and len(E)==5
assert all(any(mul(mul(x,y),x)==x and mul(mul(y,x),y)==y for y in S) for x in S)
assert all(mul(ZERO,x)==mul(x,ZERO)==ZERO for x in S)
for e in E:
    corner={mul(mul(e,x),e) for x in S}
    idem=[x for x in corner if mul(x,x)==x]
    assert all(mul(x,y)==mul(y,x) for x,y in product(idem,repeat=2))
a=(0,0,0); b=(1,1,1); ab=mul(a,b)
assert a in E and b in E and ab not in E
assert all(mul(ZERO,e)==mul(e,ZERO)==ZERO for e in E)
print('S=9, E=5, associativity triples=729; regular and locally inverse')
print('0 below all idempotents; nonidempotent product:',a,b,'->',ab)
