#!/usr/bin/env python3
"""Exact bounded controls for even-dimensional unitary primitive primes."""
from math import gcd, isqrt, prod


def prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n)+1, 2))


def factors(n):
    return [d for d in range(2, n+1) if n % d == 0 and prime(d)]


def find(p, n, f, cap):
    exponent = 2*(n-1)*f
    for r in range(exponent+1, cap+1, exponent):
        if (r != p and prime(r) and pow(p, exponent, r) == 1 and
                all(pow(p, exponent//d, r) != 1 for d in factors(exponent))):
            return r
    return None


def main():
    cap, found, total = 1_000_000, 0, 0
    for n in (4, 6, 8, 10):
        for p in (2, 3):
            for f in (2, 3):
                total += 1
                r = find(p, n, f, cap)
                if r is None:
                    print(f"n={n}, p={p}, f={f}: UNKNOWN cap={cap}")
                    continue
                q = p**f
                if r <= 7 or (q**(n-1)+1) % r:
                    raise SystemExit("FAIL primitive/unitary factor")
                if any(pow(p, (n-1)*(f//k), r) == r-1 for k in factors(f) if k % 2):
                    raise SystemExit("FAIL beta")
                order = (q**(n*(n-1)//2) *
                         prod(q**j-(-1)**j for j in range(2,n+1)) // gcd(n,q+1))
                if order % r:
                    raise SystemExit("FAIL unitary order divisibility")
                found += 1
                print(f"n={n}, p={p}, f={f}, r={r}, ord_p={2*(n-1)*f}, beta=PASS")
    print(f"FINISHED: verified={found}/{total}; cap misses remain UNKNOWN")


if __name__ == "__main__":
    main()
