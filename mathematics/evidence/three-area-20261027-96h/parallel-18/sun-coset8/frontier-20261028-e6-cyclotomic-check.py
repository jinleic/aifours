#!/usr/bin/env python3
"""Exact finite integer controls for E6; no subgroup classification is computed."""


def factor(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            count = 0
            while n % d == 0:
                n //= d
                count += 1
            result.append((d, count))
        d += 1 if d == 2 else 2
    if n > 1:
        result.append((n, 1))
    return result


def val(n, p):
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count


def order(a, r):
    power = 1
    for d in range(1, r):
        power = power * a % r
        if power == 1:
            return d
    raise AssertionError((a, r))


def phi9(x):
    return x**6 + x**3 + 1


def phi18(x):
    return x**6 - x**3 + 1


for x in range(2, 101):
    assert (x**3 - 1) * phi9(x) == x**9 - 1
    assert (x**3 + 1) * phi18(x) == x**9 + 1
    assert phi9(x) % 2 == phi18(x) % 2 == 1
    assert val(phi9(x), 3) <= 1 and val(phi18(x), 3) <= 1

for p in (2, 3, 5, 7, 11, 13, 17, 19):
    fs = factor(phi9(p))
    assert all(r == 3 or order(p, r) == 9 for r, _ in fs)
    assert any(r > 19 or (r > 3 and e > 1) for r, e in fs)
    print(f"f=1 p={p}, Phi9={phi9(p)}, factors={fs}")

for p in (3, 5, 7, 11, 13, 17, 19):
    fs = factor(phi18(p))
    assert all(r == 3 or (order(p, r) == 18 and order(p*p, r) == 9)
               for r, _ in fs)
    assert any(r > 19 or (r > 3 and e > 1) for r, e in fs)
    print(f"f=2 p={p}, Phi18(p)={phi18(p)}, factors={fs}")

q = 4
group_order = q**36
for d in (2, 5, 6, 8, 9, 12):
    group_order *= q**d - 1
group_order //= 3
Q = q**3
rank_order = 3 * (Q**3 * (Q**3 - 1) * (Q**2 - 1) // 3)
j3_order = 2**7 * 3**5 * 5 * 17 * 19
psl19_order = 19 * (19**2 - 1) // 2
assert all(group_order % m == 0 for m in (rank_order, j3_order, psl19_order))
assert val(group_order, 2) == 72
assert (val(rank_order, 2), val(j3_order, 2), val(psl19_order, 2)) == (18, 7, 2)
assert tuple(val(group_order // m, 2) for m in (rank_order, j3_order, psl19_order)) == (54, 65, 70)
assert order(q, 19) == 9 and val(group_order, 19) == 1
assert phi18(2) == 3 * 19 and pow(2, 9, 19) == 18
print("E6(4): v2 group/rank-max/J3/PSL2(19)=72/18/7/2; indices=54/65/70")
print("E6(4): ord_19(4)=9; v19(|G|)=1; 2^9=-1 mod 19")
print("PASS: finite integer controls only; maximal subgroup assertions are external imports")
