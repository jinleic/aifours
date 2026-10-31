from itertools import product

B = range(3)  # 0 is 1; 1,2 are right-zero elements
D = list(product(range(2), repeat=3))

def bm(a, b):
    return b if b else a

def dm(x, y):
    i, g, lam = x
    j, h, mu = y
    return (i, g ^ (lam & j) ^ h, mu)

def prod(x, y):
    return bm(x[0], y[0]), dm(x[1], y[1])

S = list(product(B, D))
assert len(S) == 24
assert all(prod(prod(x,y),z) == prod(x,prod(y,z)) for x,y,z in product(S,repeat=3))
assert all(bm(bm(bm(bm(a,b),c),d),a) == bm(bm(bm(bm(bm(bm(a,b),c),a),c),d),a) for a,b,c,d in product(B,repeat=4))
E = [x for x in S if prod(x,x) == x]
assert len(E) == 12
assert all(any(prod(prod(x,y),x) == x and prod(prod(y,x),y) == y for y in S) for x in S)
e, f = (0,(0,0,0)), (0,(1,1,1))
assert e in E and f in E and prod(e,f) not in E
base = (0,(0,0,0))
p, q = (1,(0,0,0)), (2,(0,0,0))
assert all(x in E and prod(prod(base,x),base) == x for x in (p,q))
assert prod(p,q) == q and prod(q,p) == p and p != q
print('S=24, associativity triples=13824, idempotents=12, all elements have inverses')
print('B=3, seminormal checks=81; E not closed; a local corner has noncommuting idempotents')
