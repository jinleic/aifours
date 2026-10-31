#!/usr/bin/env python3
"""Selected exact divisor bounds for the factorial-terminal lemma."""

from math import comb, factorial, gcd

for r, t in ((419, 3), (2540173, 9), (279417613, 11), (43589145937, 13)):
    assert r+1 > 7*factorial(t) and t < r
    count = 0
    for left in range(1, t+1):
        for right in range(left+1, t+1):
            u = right-left+1
            b = comb(r+right, u)
            for h in range(left, right+1):
                if h % 2:
                    a = r+h
                    d = a//gcd(a, factorial(u))
                    assert 7 < d < r and b % d == 0
                    count += 1
    for h in range(1, t+1):
        if (r+h) % 7 == 0:
            assert 7 < (r+h)//7 < r
    print(f"r={r}, t={t}, bounded even-numerator divisors checked={count}")
print("PASS: four selected integer controls only; no source or subgroup proof verified")
