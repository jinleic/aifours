#!/usr/bin/env python3
"""Selected exact modular controls, not an all-dimensional proof."""


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def distinct_prime_factors(n):
    out = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


for n, p, f, r in ((9, 3, 3, 6481), (9, 7, 3, 73),
                   (11, 3, 3, 31), (13, 5, 3, 37)):
    exponent = (n-1)*f
    assert is_prime(r) and r > 2*n-1
    assert pow(p, exponent, r) == 1
    assert all(pow(p, exponent//k, r) != 1 for k in distinct_prime_factors(exponent))
    assert pow(p**f, n-1, r) == 1
    assert all(pow(p, (n-1)*f//k, r) != 1 for k in distinct_prime_factors(f))
    print(f"n={n}, p={p}, f={f}, r={r}, ord_p={exponent}")
print("PASS: 4 selected modular cases only; source classification not computed")
