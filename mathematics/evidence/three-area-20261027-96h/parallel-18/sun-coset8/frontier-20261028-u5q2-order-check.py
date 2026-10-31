#!/usr/bin/env python3
"""Exact independent arithmetic for the PSU(5,2) endpoint."""
from math import gcd, prod

q, n = 2, 5
order = q**(n*(n-1)//2) * prod(q**j-(-1)**j for j in range(2,n+1)) // gcd(n,q+1)
expected = 2**10 * 3**5 * 5 * 11
print("unitary_order:", order)
print("factor_product:", expected)
print("eleven_divides_order:", order % 11 == 0)
if order != expected or order % 11:
    raise SystemExit("FAIL order/factorization")
print("PASS: exact PSU(5,2) order arithmetic")
