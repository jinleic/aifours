#!/usr/bin/env python3
"""Exact bounded search; hitting the cap means UNKNOWN, not nonexistence."""
from math import gcd, isqrt


def prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    return [d for d in range(2, n + 1) if n % d == 0 and prime(d)]


def witness(f, cap):
    n = 6*f
    for r in range(n+1, cap+1, n):
        if (prime(r) and r != 7 and pow(7, n, r) == 1 and
                all(pow(7, n//d, r) != 1 for d in factors(n))):
            return r
    return None


def main():
    cap = 10_000_000
    found = 0
    for f in range(1, 7):
        q = 7**f
        r = witness(f, cap)
        if r is None:
            print(f"f={f}: UNKNOWN, no witness searched up to {cap}", flush=True)
            continue
        if r <= 7 or (q**3+1) % r:
            raise SystemExit("FAIL unitary order divisibility")
        if any(pow(7, 3*(f//k), r) == r-1 for k in factors(f) if k % 2):
            raise SystemExit("FAIL beta(3,-1)")
        gorder = q**3*(q**3+1)*(q*q-1)//gcd(3,q+1)
        if gorder % r or gorder <= 5040:
            raise SystemExit("FAIL group order")
        found += 1
        print(f"f={f}, primitive_prime={r}, ord_7={6*f}, beta=PASS, "
              f"r_divides_unitary_order=YES, order_gt_7_factorial=YES", flush=True)
    print(f"FINISHED: verified={found}/6; cap misses are UNKNOWN")


if __name__ == "__main__":
    main()
