#!/usr/bin/env python3
"""Small exact primitive-prime controls for the 3D4(q) written candidate."""


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        result.append(n)
    return result


def order(a, r):
    x = 1
    for i in range(1, r):
        x = x * a % r
        if x == 1:
            return i
    raise AssertionError((a, r))


for p in (2, 3, 5, 7):
    for f in (1, 2, 3):
        q = p**f
        cyclotomic = q**4 - q**2 + 1
        assert (q**2 + 1) * cyclotomic == q**6 + 1
        assert ((q**2 - q + 1) * (q**2 + q + 1) * cyclotomic
                == q**8 + q**4 + 1)
        candidates = [r for r in factors(cyclotomic) if order(p, r) == 12*f]
        assert candidates
        r = candidates[0]
        assert r > 7 and order(q, r) == 12
        for k in factors(f):
            assert pow(p, 6*f // k, r) != r - 1
        print(f"p={p} f={f} q={q} primitive_r={r}")
print("PASS: exact integer examples only, not a source or theorem verification")
