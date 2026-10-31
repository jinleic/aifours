#!/usr/bin/env python3
"""Independent finite controls for f237; none imports or executes author code."""
from functools import lru_cache
from itertools import combinations, product
from math import gcd

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)


def compatible(r, x, s, y):
    px, vx = x
    py, vy = y
    return (px == py or
            not ((r-s) % 3 == 0 or (r-s) % 11 == 0 or (vx-vy) % 5 == 0) or
            vx == vy)


def domains(anchors):
    result = []
    for r in range(33):
        result.append({(p, v) for p in range(2) for v in range(25)
                       if all(compatible(r, (p, v), a % 33, (a % 2, a % 25))
                              for a in anchors)})
    return result


def arc_reduce(ds):
    ds = [set(d) for d in ds]
    passes = 0
    while True:
        changed = False
        passes += 1
        for r in range(33):
            for x in tuple(ds[r]):
                if any(not any(compatible(r, x, s, y) for y in ds[s])
                       for s in range(33) if s != r):
                    ds[r].remove(x)
                    changed = True
            assert ds[r], ('empty residue domain', r)
        if not changed:
            return ds, passes


def check_graph():
    initial = domains(Y)
    ds, passes = arc_reduce(initial)
    pinned = {0: 0, 1: 1, 2: 13, 3: 14, 7: 7}
    for r, choices in enumerate(ds):
        p = int(r % 3 == 1)
        expected = {pinned[r % 11]} if r % 11 in pinned else set(Y)
        assert choices == {(p, v) for v in expected}, (r, choices, expected)
    assert (0, 0) in initial[3] and (0, 0) not in ds[3]
    assert ds[25] == {(1, 14)}
    assert not compatible(3, (0, 0), 25, (1, 14))
    free, _ = arc_reduce(domains(()))
    assert (0, 0) in free[1] and (1, 0) in free[0]
    print('GRAPH: 33 classes, all 33 exact domains, six free f-values in Y;',
          'arc passes=', passes)
    print('GRAPH NEGATIVES: wrong even class-3 value conflicts with class 25;',
          'without anchors the parity conclusion fails')


def sums_unique(xs, zs, n):
    return len({(x + z) % n for x in xs for z in zs}) == n


def check_dilation():
    tilings = dilations = comparisons = 0
    for n in range(2, 12):
        for size in range(1, n + 1):
            if n % size:
                continue
            zsize = n // size
            xsets = [(0,) + c for c in combinations(range(1, n), size - 1)]
            zsets = [(0,) + c for c in combinations(range(1, n), zsize - 1)]
            for xs in xsets:
                for zs in zsets:
                    if not sums_unique(xs, zs, n):
                        continue
                    tilings += 1
                    dx = {(x-y) % n for x in xs for y in xs if x != y}
                    dz = {(x-y) % n for x in zs for y in zs if x != y}
                    for x in dx:
                        for z in dz:
                            assert gcd(x, n) != gcd(z, n)
                            comparisons += 1
                    for t in range(1, 2*n + 1):
                        if gcd(t, size) != 1:
                            continue
                        tx = tuple((t*x) % n for x in xs)
                        assert len(set(tx)) == size and sums_unique(tx, zs, n)
                        dilations += 1
    assert sums_unique((0, 1), (0, 2), 4)
    assert gcd(2, 2) != 1 and not sums_unique((0, 2), (0, 2), 4)
    print('DILATION: anchored-at-zero tilings n=2..11:', tilings,
          'dilations:', dilations, 'gcd comparisons:', comparisons)
    print('DILATION NEGATIVE: t=2 is not coprime to |X|=2 and collisions occur')


def check_gcd():
    comparisons = highbits = 0
    for k, v, r in product(range(1, 8), (4, 6), (33, 3**4*11*7, 33*11**3*13)):
        n = 2**k * 5**v * r
        assert gcd(24, n) == 3 * 2**min(k, 3)
        assert gcd(12, n) == 3 * 2**min(k, 2)
        assert (gcd(24, n) == gcd(12, n)) == (k <= 2)
        comparisons += 1
        if k >= 3:
            for d in range(-128, 129):
                if d == 0 or d % 5 == 0:
                    continue
                g2 = gcd(abs(d), n) & -gcd(abs(d), n)
                expected = (d % 8 == 0) if k == 3 else (d % 16 == 8)
                assert (g2 == 8) == expected
                highbits += 1
    n = 8 * 5**4 * 33
    assert gcd(24, n) == 24 and gcd(12, n) == 12
    print('GCD: parameter cases=', comparisons, 'high-bit differences=', highbits)
    print('GCD NEGATIVE: K=3 has gcd(24,n)=24 != gcd(12,n)=12')


def phi4_odd(c):
    return c[1]+c[5]+c[9]+c[13] == c[3]+c[7]+c[11]+c[15]


def phi8_odd(c):
    return c[1]+c[9] == c[5]+c[13] and c[3]+c[11] == c[7]+c[15]


def phi16_odd(c):
    return all(c[j] == c[j+8] for j in (1, 3, 5, 7))


def check_branches():
    k3a = k3b = higha = highb = 0
    for vals in product(range(3), repeat=8):
        c = dict(zip((1, 3, 5, 7, 9, 11, 13, 15), vals))
        if c[5]+c[13] and phi8_odd(c):
            assert c[1]+c[9] > 0
            k3a += 1
        if c[7]+c[15] and phi4_odd(c):
            assert c[1]+c[9]+c[5]+c[13] > 0
            k3b += 1
        if c[13] and phi8_odd(c) and phi16_odd(c):
            assert c[9] > 0
            higha += 1
        if c[7] and phi4_odd(c) and phi16_odd(c):
            assert c[9] > 0 or c[5] > 0
            highb += 1
    c = {j: 0 for j in (1, 3, 5, 7, 9, 11, 13, 15)}
    c[1] = c[13] = 1
    assert phi8_odd(c) and not phi16_odd(c) and c[9] == 0
    c = {j: 0 for j in c}
    c[1] = c[7] = 1
    assert phi4_odd(c) and not phi16_odd(c) and c[9] == c[5] == 0
    assert (13-1) % 5 and (7-1) % 5 and (7-13) % 5
    print('BRANCHES: 3^8 folded-count vectors; K3 Phi8/Phi4 cases=', k3a, k3b,
          'K>=4 Phi8+Phi16/Phi4+Phi16 cases=', higha, highb)
    print('BRANCH NEGATIVES: deleting Phi16 allows both required high-bit conclusions to fail')


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i+j] += x*y
    return c


def divide(a, b):
    a = a[:]
    assert b[-1] == 1
    q = [0] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        offset = len(a) - len(b)
        v = a[-1]
        q[offset] += v
        for i, x in enumerate(b):
            a[offset+i] -= v*x
        while len(a) > 1 and a[-1] == 0:
            a.pop()
    assert not any(a), ('nonexact polynomial quotient', a, b)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


@lru_cache(None)
def cyclo(n):
    p = [-1] + [0] * (n-1) + [1]
    for d in divisors(n)[:-1]:
        p = divide(p, cyclo(d))
    return tuple(p)


def check_transport():
    cases = 0
    for i, r in product(range(1, 5), (1, 3, 5, 9, 15, 33)):
        p = [1]
        for d in divisors(r):
            p = mul(p, cyclo(2**i*d))
        degree = 2**(i-1)*r
        assert p == [1] + [0]*(degree-1) + [1]
        cases += 1
    p = [1]
    for d in divisors(6):
        p = mul(p, cyclo(4*d))
    assert p != [1] + [0]*11 + [1]
    for i in (2, 3, 4):
        r = 33
        h = 2**(i-1)
        qs = {res + r*k for res in range(r) for k in (0, h, 2*h, 3*h)}
        for res in range(r):
            count = [0]*(2*h)
            for q in qs:
                if q % r == res:
                    count[q % (2*h)] += 1
            assert all(count[j] == count[j+h] for j in range(h))
        qs.remove(r*h)
        count = [0]*(2*h)
        for q in qs:
            if q % r == 0:
                count[q % (2*h)] += 1
        assert any(count[j] != count[j+h] for j in range(h))
    print('TRANSPORT: exact cyclotomic identities=', cases,
          'plus 3 binary actual-fibre fold controls')
    print('TRANSPORT NEGATIVES: even R breaks the displayed identity; deleting a partner breaks a fibre')


def owns_prime_power(xs, p, j):
    period = p**j
    block = p**(j-1)
    c = [0]*period
    for x in xs:
        c[x % period] += 1
    return all(all(c[r+k*block] == c[r] for k in range(p)) for r in range(block))


def exact_cover(ps, qs, n):
    seen = bytearray(n)
    for p in ps:
        for q in qs:
            z = (p+q) % n
            assert not seen[z], ('duplicate residue', z)
            seen[z] = 1
    assert sum(seen) == n


def crt16_625(x, y):
    return y + 625*((x-y) % 16)


def check_relaxations():
    n = 330000
    for j in (3, 4):
        d = 5**(j-1)
        a = [x for x in range(10000) if (x//d) % 5 == 0]
        b = [k*d for k in range(5)]
        ps = [33*x for x in a]
        qs = [r+33*x for r in range(33) for x in b]
        assert len(ps) == 2000 and len(qs) == 165
        assert set(Y) <= set(qs) and not set(A) <= set(ps)
        exact_cover(ps, qs, n)
        assert owns_prime_power(qs, 5, j)
        assert not owns_prime_power(qs, 5, 7-j)
        # A second independent relaxation also matches the target branch's
        # cardinality and low two-power spectrum; it still omits head anchors.
        a5 = [x for x in range(625) if (x//d) % 5 == 0]
        b5 = [k*d for k in range(5)]
        aa = [crt16_625(u, x) for u in (0, 1, 8, 9) for x in a5]
        bb = [crt16_625(u, x) for u in (0, 2, 4, 6) for x in b5]
        pp = [33*x for x in aa]
        qq = [r+33*x for r in range(33) for x in bb]
        assert len(pp) == 500 and len(qq) == 660
        assert set(Y) <= set(qq) and not set(A) <= set(pp)
        exact_cover(pp, qq, n)
        assert owns_prime_power(qq, 5, j)
        assert not owns_prime_power(qq, 5, 7-j)
        assert [owns_prime_power(pp, 2, i) for i in range(1, 5)] == [True, False, False, True]
        assert [owns_prime_power(qq, 2, i) for i in range(1, 5)] == [False, True, True, False]
        print('RELAXATION: j=', j, 'exact covers n=330000:',
              '(P,Q)=(2000,165) and (500,660); Q owns Phi_5^j; head anchors absent')
    assert 4*5**3 == 500 and 2000 == 16*5**3
    print('RELAXATION NEGATIVE: P subset 33Z misses 3,8,11; neither is an anchored witness')


if __name__ == '__main__':
    check_graph()
    check_dilation()
    check_gcd()
    check_branches()
    check_transport()
    check_relaxations()
    print('ALL REQUESTED FINITE CONTROLS COMPLETED')
