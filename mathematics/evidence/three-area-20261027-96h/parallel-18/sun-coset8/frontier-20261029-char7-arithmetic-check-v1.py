#!/usr/bin/env python3
"""Exact integer checks for the characteristic-7 packet.

1. Factor Phi_n(7) for n in {6,12,8,16,9,18,36,30,60}; report the prime factors r with
   multiplicative order of 7 modulo r equal to n (p-primitive prime divisors of 7^n-1).
2. Check the size conditions used from BBGT Table C for q=7 and q=49.
3. Check the prime support of |PSL2(49)|/7.
Integer arithmetic only; Miller-Rabin with fixed bases (deterministic below 3.3e24) and
Pollard rho with a fixed seed; every reported factorization is re-multiplied exactly.
"""
import random
from math import gcd


def cyclotomic_value(n, x):
    # Phi_n(x) = prod_{d|n} (x^d - 1)^{mu(n/d)}, computed exactly with integers
    def mobius(m):
        res, p = 1, 2
        while p * p <= m:
            if m % p == 0:
                m //= p
                if m % p == 0:
                    return 0
                res = -res
            p += 1
        if m > 1:
            res = -res
        return res
    num, den = 1, 1
    for d in range(1, n + 1):
        if n % d == 0:
            mu = mobius(n // d)
            if mu == 1:
                num *= x ** d - 1
            elif mu == -1:
                den *= x ** d - 1
    if num % den:
        raise ValueError("non-integral cyclotomic value")
    return num // den


def is_prime(n):
    if n < 2:
        return False
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in bases:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in bases:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    if n >= 3_317_044_064_679_887_385_961_981:
        raise ValueError("outside deterministic Miller-Rabin range")
    return True


def rho(n, rng):
    if n % 2 == 0:
        return 2
    while True:
        c = rng.randrange(1, n)
        x = y = rng.randrange(2, n)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
        if d != n:
            return d


def factor(n, rng):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    for p in range(2, 10000):
        if n % p == 0:
            return [p] + factor(n // p, rng)
    d = rho(n, rng)
    return sorted(factor(d, rng) + factor(n // d, rng))


def order_mod(a, r):
    k, x = 1, a % r
    while x != 1:
        x = x * a % r
        k += 1
    return k


def main():
    rng = random.Random(20261029)
    primitive = {}
    for n in (6, 12, 8, 16, 9, 18, 36, 30, 60):
        v = cyclotomic_value(n, 7)
        fs = factor(v, rng)
        prod = 1
        for f in fs:
            prod *= f
        if prod != v or not all(is_prime(f) for f in fs):
            raise SystemExit(f"FAIL factorization {n}")
        primitive[n] = sorted({r for r in fs if order_mod(7, r) == n})
        print(f"Phi_{n}(7) = {v} = {' * '.join(map(str, fs))}; p-primitive: {primitive[n]}")
    # BBGT Table C size conditions at q=7 (f=1) and q=49 (f=2)
    need = {"G2 r_6 (q=7): some r>13": max(primitive[6]) > 13,
            "G2 r_6 (q=49): some r>13": max(primitive[12]) > 13,
            "F4 r_8 (q=7): some r>17": max(primitive[8]) > 17,
            "F4 r_8 (q=49): some r>17": max(primitive[16]) > 17,
            "E6 r_9 (q=7): some r>19": max(primitive[9]) > 19,
            "E6 r_9 (q=49): some r>19": max(primitive[18]) > 19,
            "2E6 r_18 (q=7): some r>19": max(primitive[18]) > 19,
            "E7 r_18 (q=7): some r>37": max(primitive[18]) > 37,
            "E7 r_18 (q=49): some r>37": max(primitive[36]) > 37,
            "E8 r_30 (q=7): some r>61": max(primitive[30]) > 61,
            "E8 r_30 (q=49): some r>61": max(primitive[60]) > 61}
    for k, ok in need.items():
        if not ok:
            raise SystemExit(f"FAIL {k}")
        print("PASS", k)
    order_psl2_49 = 49 * (49 * 49 - 1) // 2
    cof = order_psl2_49 // 7
    primes = sorted(set(factor(cof, rng)))
    print(f"|PSL2(49)| = {order_psl2_49}; |PSL2(49)|/7 = {cof} has primes {primes} ({len(primes)} < 8);"
          f" 2520 % |PSL2(49)| = {2520 % order_psl2_49}")
    if len(primes) >= 8 or 2520 % order_psl2_49 == 0:
        raise SystemExit("FAIL PSL2(49) support")
    print("PASS all characteristic-7 arithmetic checks")


if __name__ == "__main__":
    main()
