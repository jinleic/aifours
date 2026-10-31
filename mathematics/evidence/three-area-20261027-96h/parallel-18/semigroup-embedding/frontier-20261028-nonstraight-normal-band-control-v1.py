from itertools import product

N=range(3)  # 0 is zero; 1,2 are left-zero elements

def mul(a,b):
    return 0 if a==0 or b==0 else a

def order(a,b):
    return mul(a,b)==a and mul(b,a)==a

def wedge(a,b):
    candidates=[c for c in N if mul(a,c)==c and mul(c,b)==c]
    maxima=[c for c in candidates if all(order(d,c) for d in candidates)]
    assert len(maxima)==1
    return maxima[0]

assert all(mul(mul(x,y),z)==mul(x,mul(y,z)) for x,y,z in product(N,repeat=3))
assert all(mul(x,x)==x for x in N)
assert all(mul(mul(mul(x,y),z),w)==mul(mul(mul(x,z),y),w) for x,y,z,w in product(N,repeat=4))
assert all(mul(mul(mul(mul(a,b),c),d),a)==mul(mul(mul(mul(mul(mul(a,b),c),a),c),d),a) for a,b,c,d in product(N,repeat=4))
for e in N:
    corner={mul(mul(e,x),e) for x in N}
    assert all(mul(x,y)==mul(y,x) for x,y in product(corner,repeat=2))
assert all(wedge(a,b)==mul(a,b) for a,b in product(N,repeat=2))
assert wedge(0,1)==wedge(1,0) and wedge(0,2)==wedge(2,0)
assert wedge(1,2)!=wedge(2,1)
print('N=3: normal and seminormal, all local corners semilattices; wedge=multiplication')
print('wedge-commutation: 1~0~2 but 1 not~2; maximal semilattices {0,1}, {0,2}')
