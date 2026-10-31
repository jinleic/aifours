#!/usr/bin/env python3
"""Direct trial division and order for Phi_36(7); no cap-search inference."""
from math import isqrt

n = 7**12 - 7**6 + 1
for d in range(2, isqrt(n)+1):
    if n % d == 0:
        raise SystemExit(f"COMPOSITE: n={n}, factor={d}")
if pow(7, 36, n) != 1 or pow(7, 18, n) == 1 or pow(7, 12, n) == 1:
    raise SystemExit("FAIL: multiplicative order is not 36")
# f=6; only odd prime factor is3; beta asks 7^(3*f/3) != -1 mod n.
if pow(7, 6, n) == n-1:
    raise SystemExit("FAIL: beta(3,-1)")
print("Phi36_at_7:", n)
print("trial_division_primality: PASS")
print("ord_7: 36")
print("f6_beta_condition: PASS")
