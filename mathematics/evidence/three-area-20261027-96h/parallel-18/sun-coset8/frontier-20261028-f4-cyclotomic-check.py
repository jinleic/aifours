#!/usr/bin/env python3
"""Bounded integer controls for F4; not a maximal-subgroup computation."""


def factor(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            result.append((d, e))
        d += 1 if d == 2 else 2
    if n > 1:
        result.append((n, 1))
    return result


def val(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def order(a, r):
    power = 1
    for d in range(1, r):
        power = power * a % r
        if power == 1:
            return d
    raise AssertionError((a, r))


def phi12(x):
    return x**4 - x**2 + 1


for x in range(2, 101):
    assert (x**2 + 1) * phi12(x) == x**6 + 1
    assert phi12(x) % 2 == phi12(x) % 3 == 1

for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    fs = factor(phi12(p))
    assert all(order(p, r) == 12 for r, _ in fs)
    assert any(r > 13 or e > 1 for r, e in fs)
    print(f"odd f=1 p={p}, Phi12={phi12(p)}, factors={fs}")

for f in (1, 2, 3):
    q = 2**f
    fs = factor(phi12(q))
    primitive = [r for r, _ in fs if order(2, r) == 12 * f]
    assert primitive and all(order(q, r) == 12 for r in primitive)
    group = q**24 * (q**12 - 1) * (q**8 - 1) * (q**6 - 1) * (q**2 - 1)
    rank = 3 * q**12 * (q**8 + q**4 + 1) * (q**6 - 1) * (q**2 - 1)
    assert group % rank == 0
    assert val(group, 2) == 24 * f and val(rank, 2) == 12 * f
    assert val(group // rank, 2) == 12 * f
    if f % 2:
        ree = q**12 * (q**6 + 1) * (q**4 - 1) * (q**3 + 1) * (q - 1)
        assert group % ree == 0 and val(ree, 2) == 12 * f
        assert val(group // ree, 2) == 12 * f
    print(f"even f={f}, q={q}, primitive={primitive}, rank index v2={12*f}")

psl4_3 = 3**6 * (3**2 - 1) * (3**3 - 1) * (3**4 - 1) // 2
assert val(2 * psl4_3, 2) == 8
psl2_27 = 27 * (27**2 - 1) // 2
assert factor(psl2_27) == [(2, 2), (3, 3), (7, 1), (13, 1)]
print("q=2: PSL4(3).2 has 2-part 2^8; q=8 PSL2(27) has no prime >13")
print("PASS: exact integer controls only; source subgroup classification not checked")
