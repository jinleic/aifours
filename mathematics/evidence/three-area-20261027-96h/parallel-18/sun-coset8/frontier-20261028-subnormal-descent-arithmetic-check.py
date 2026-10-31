#!/usr/bin/env python3
"""Exact bounded divisor checks for the general prime subnormal descent."""
from math import gcd

primes = (2, 3, 5, 7, 11)
counts = {"regular_quotient_free": 0, "regular_quotient_p": 0,
          "private_selected": 0, "mixed_regular_fibres": 0}

for p in primes:
    for r in range(1, 61):
        for a in range(1, p*r + 1):
            if (p*r) % a:
                continue
            c_selected = p*r // a
            for s in range(1, 61):
                if gcd(r, s) != 1:
                    continue
                for d in (1, p):
                    if a % d or (p*s) % d:
                        continue
                    c_other = p*s // d
                    if r % p:
                        if a % p:
                            if d != 1:
                                raise SystemExit("FAIL regular quotient-free")
                            counts["regular_quotient_free"] += 1
                        else:
                            if c_selected % p == 0 or gcd(c_selected, c_other) != 1:
                                raise SystemExit("FAIL regular quotient-p")
                            counts["regular_quotient_p"] += 1
                    else:
                        if s % p == 0:
                            raise SystemExit("FAIL private ownership")
                        counts["private_selected"] += 1
            if r % p == 0:
                for s in range(1, 21):
                    for t in range(1, 21):
                        if gcd(r, s) == gcd(r, t) == gcd(s, t) == 1:
                            if s % p == 0 or t % p == 0 or gcd(p*s, t) != 1:
                                raise SystemExit("FAIL mixed regular fibres")
                            counts["mixed_regular_fibres"] += 1
print("bounded_divisor_case_counts:", counts)
print("PASS: all checked divisor/fibre implications")
