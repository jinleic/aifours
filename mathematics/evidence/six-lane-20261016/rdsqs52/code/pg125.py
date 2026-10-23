"""PG(1,25) = F25 ∪ {∞} as points 0..25 (∞ = 25); F25 = F5[s]/(s^2-2), a+bs -> a+5b.
Generators of PSL(2,25), PGL(2,25), and Frobenius as permutations."""
Q = 25
INF = 25

def mul(x, y):
    a, b = x % 5, x // 5
    c, d = y % 5, y // 5
    return ((a * c + 2 * b * d) % 5) + 5 * ((a * d + b * c) % 5)

def add(x, y):
    return ((x % 5 + y % 5) % 5) + 5 * ((x // 5 + y // 5) % 5)

def neg(x):
    return ((-(x % 5)) % 5) + 5 * ((-(x // 5)) % 5)

INV = {x: next(y for y in range(1, Q) if mul(x, y) == 1) for x in range(1, Q)}

def order(x):
    k, y = 1, x
    while y != 1:
        y = mul(y, x); k += 1
    return k

GEN = next(x for x in range(1, Q) if order(x) == 24)   # primitive element

def mobius(a, b, c, d):
    """x -> (a x + b)/(c x + d) on PG(1,25)."""
    out = []
    for x in range(Q + 1):
        if x == INF:
            num, den = a, c
        else:
            num, den = add(mul(a, x), b), add(mul(c, x), d)
        if den == 0:
            out.append(INF)
        else:
            out.append(mul(num, INV[den]) if num != 0 else 0)
    return tuple(out)

def frob():
    # x -> x^5 : a + b s -> a + b s^5 = a + 4 b s (since s^4 = 4)
    out = []
    for x in range(Q + 1):
        if x == INF:
            out.append(INF)
        else:
            a, b = x % 5, x // 5
            out.append(a + 5 * ((4 * b) % 5))
    return tuple(out)

T1 = mobius(1, 1, 0, 1)                      # x -> x + 1
TS = mobius(1, 5, 0, 1)                      # x -> x + s
SQ = mobius(mul(GEN, GEN), 0, 0, 1)          # x -> g^2 x
NS = mobius(GEN, 0, 0, 1)                    # x -> g x  (PGL only)
W = mobius(0, neg(1), 1, 0)                  # x -> -1/x
PSL = [T1, TS, SQ, W]
PGL = PSL + [NS]
FROB = frob()
