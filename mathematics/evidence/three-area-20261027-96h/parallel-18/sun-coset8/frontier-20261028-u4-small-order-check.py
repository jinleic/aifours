#!/usr/bin/env python3
"""Exact PSU4(2), PSU4(3) order arithmetic from the named formula."""
from math import gcd, prod

for q, expected in ((2, 2**6 * 3**4 * 5), (3, 2**7 * 3**6 * 5 * 7)):
    n = 4
    value = q**6 * prod(q**j-(-1)**j for j in range(2,n+1)) // gcd(n,q+1)
    print(f"q={q}, group_order={value}, factor_product={expected}")
    if value != expected or value <= 5040:
        raise SystemExit("FAIL unitary order/factorization")
print("PASS: exact U4 small-order factorizations")
