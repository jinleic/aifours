#!/usr/bin/env python3
"""Exact finite arithmetic controls for the E7 source-conditional packet.

Not a subgroup-classification computation or proof of the all-field theorem.
"""


def factors(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            exponent = 0
            while n % d == 0:
                n //= d
                exponent += 1
            result.append((d, exponent))
        d += 1 if d == 2 else 2
    if n > 1:
        result.append((n, 1))
    return result


def value18(x):
    return x**6 - x**3 + 1


def valuation(n, p):
    exponent = 0
    while n % p == 0:
        n //= p
        exponent += 1
    return exponent


def order(a, modulus):
    value = 1
    for exponent in range(1, modulus):
        value = value * a % modulus
        if value == 1:
            return exponent
    raise AssertionError((a, modulus))


for x in range(2, 101):
    f = value18(x)
    assert (x**3 + 1) * f == x**9 + 1
    assert f % 2 == 1
    assert valuation(f, 3) <= 1
    if x % 3 in (0, 1):
        assert f % 3 == 1
    else:
        assert f % 9 == 3

for p in (2, 3, 5, 7, 11, 13, 17, 19):
    fs = factors(value18(p))
    assert all(r == 3 or order(p, r) == 18 for r, _ in fs)
    if p >= 5:
        assert value18(p) > 3 * 19 * 37
        assert any(r > 37 or (r > 3 and e > 1) for r, e in fs)
    print(f"f=1 p={p}, Phi18={value18(p)}, factors={fs}")

for p in (2, 3, 5, 7, 11):
    fs = factors(value18(p * p))
    assert all(order(p, r) == 36 and r % 36 == 1 for r, _ in fs)
    assert any(r > 37 or e > 1 for r, e in fs)
    print(f"f=2 p={p}, Phi18(p^2)={value18(p*p)}, factors={fs}")

q = 3
e7 = q**63
for d in (2, 6, 8, 10, 12, 14, 18):
    e7 *= q**d - 1
e7 //= 2
unitary_e6 = q**36 * (q**2 - 1) * (q**5 + 1) * (q**6 - 1)
unitary_e6 *= (q**8 - 1) * (q**9 + 1) * (q**12 - 1)
rank_max_order = 4 * unitary_e6
psl2_37_order = 37 * (37**2 - 1) // 2
assert e7 % rank_max_order == 0 and e7 % psl2_37_order == 0
assert valuation(e7, 3) == 63
assert valuation(rank_max_order, 3) == 36
assert valuation(psl2_37_order, 3) == 2
assert valuation(e7 // rank_max_order, 3) == 27
assert valuation(e7 // psl2_37_order, 3) == 61
assert order(3, 37) == 18 and valuation(e7, 37) == 1
assert pow(15, 2, 37) == 3
print("E7(3): v3 group/rank-max/PSL2(37)=63/36/2; index valuations=27/61")
print("E7(3): ord_37(3)=18; v37(|G|)=1; 15^2=3 mod 37")
print("PASS: exact integer controls only; classification and all-field implications not computed")
