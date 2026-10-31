from itertools import product

D = list(product(range(2), repeat=3))

def mul(x, y):
    i, g, lam = x
    j, h, mu = y
    return i, g ^ (lam & j) ^ h, mu

assert all(mul(mul(x, y), z) == mul(x, mul(y, z)) for x, y, z in product(D, repeat=3))
E = [x for x in D if mul(x, x) == x]
assert len(E) == 4
for i, lam in product(range(2), repeat=2):
    identity = (i, i & lam, lam)
    cell = [(i, g, lam) for g in range(2)]
    assert identity in E
    assert all(mul(identity, x) == mul(x, identity) == x for x in cell)
    assert all(any(mul(x, y) == mul(y, x) == identity for y in cell) for x in cell)
    corner = {mul(mul(identity, x), identity) for x in D}
    assert corner == set(cell)
for i in range(2):
    row = [e for e in E if e[0] == i]
    assert all(mul(x, y) == y for x, y in product(row, repeat=2))
for lam in range(2):
    col = [e for e in E if e[2] == lam]
    assert all(mul(x, y) == x for x, y in product(col, repeat=2))
a, b = (0, 0, 0), (1, 1, 1)
c = mul(a, b)
assert a in E and b in E and c not in E
assert c == (0, 1, 1) and mul(c, c) == (0, 0, 1)
print('D=8, associativity triples=512, E=4, all four 2-element cells and corners groups')
print('idempotent rows right-zero; columns left-zero; nonorthogonal:', a, b, 'product', c, 'square', mul(c, c))
