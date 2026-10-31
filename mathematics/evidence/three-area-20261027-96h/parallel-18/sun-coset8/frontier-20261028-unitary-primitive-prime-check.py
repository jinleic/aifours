#!/usr/bin/env python3
"""Bounded exact primitive-prime and order checks for PSU(3,7^f).

Finite search is not a proof of Zsigmondy or the Sylow overgroup theorem.
"""
from math import gcd, isqrt


def isprime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def prime_factors(n):
    return [d for d in range(2, n + 1) if n % d == 0 and isprime(d)]


def witness(f, cap=1_000_000):
    n = 6*f
    for r in range(n+1, cap+1, n):
        if (isprime(r) and r != 7 and pow(7, n, r) == 1 and
                all(pow(7, n//d, r) != 1 for d in prime_factors(n))):
            return r
    raise RuntimeError(f"no bounded witness f={f} cap={cap}")


def main():
    for f in range(1, 7):
        q = 7**f
        r = witness(f)
        if r <= 7 or (q**3+1) % r:
            raise SystemExit("FAIL unitary order divisibility")
        if any(pow(7, 3*(f//k), r) == r-1 for k in prime_factors(f) if k % 2):
            raise SystemExit("FAIL beta(3,-1) subfield condition")
        unitary_order = q**3*(q**3+1)*(q*q-1)//gcd(3,q+1)
        if unitary_order % r or unitary_order <= 5040:
            raise SystemExit("FAIL group order / simple index barrier")
        print(f"f={f}, primitive_prime={r}, ord_7={6*f}, beta=PASS, "
              f"r_divides_unitary_order=YES, order_gt_7_factorial=YES")
    print("PASS: six exact bounded primitive-prime instances")


if __name__ == "__main__":
    main()
