#!/usr/bin/env python3
"""Selected exact primitive orders; no maximal subgroups are enumerated."""


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_factors(n):
    found = []
    d = 2
    while d*d <= n:
        if n % d == 0:
            found.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        found.append(n)
    return found


for n, p, f, r in ((8, 2, 2, 257), (10, 2, 2, 41), (14, 2, 2, 29),
                   (16, 2, 2, 65537), (8, 3, 3, 6481), (10, 2, 3, 331)):
    exponent = n*f
    assert is_prime(r) and r > n+1
    assert pow(p, exponent, r) == 1
    assert all(pow(p, exponent//k, r) != 1 for k in prime_factors(exponent))
    assert pow(p**f, n//2, r) == r-1
    assert all(pow(p, (n//2)*f//k, r) != r-1 for k in prime_factors(f))
    print(f"n={n}, p={p}, f={f}, r={r}, ord_p={exponent}")
print("PASS: six exact modular examples only; no source classification verified")
