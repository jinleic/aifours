#!/usr/bin/env python3
"""Independent bounded exact arithmetic controls for frozen f217 review."""
from math import gcd

Y = {0, 1, 7, 13, 14}
A = {0, 3, 8, 11}
F = {3, 5, 8, 11, 15, 24, 33, 55, 88, 165, 264}


def crt(residues, moduli):
    n = 1
    for modulus in moduli:
        n *= modulus
    return sum(a * (n // b) * pow(n // b, -1, b)
               for a, b in zip(residues, moduli)) % n


def make_case(e, k):
    d, m = 2**k, 5**(e + 1)
    n, h = 33*d*m, 33*d*5**e
    f = [0, 1, 13, 14, 0, 0, 0, 7, 0, 0, 0]
    g = [r if r in Y else (1 if r % 3 == 1 else 0) for r in range(33)]
    bases = [crt((g[r], f[r % 11], r), (d, m, 33)) for r in range(33)]
    q = [(base + j*h) % n for base in bases for j in range(5)]
    p = [33*(m*t + d*u) % n for t in range(d) for u in range(5**e)]
    return d, m, n, h, f, g, bases, p, q


def distinct_sums(p, q, n):
    seen = bytearray(n)
    for a in p:
        for b in q:
            seen[(a + b) % n] = 1
    return seen.count(1)


def phi_prime_power_divides(q, p, a):
    # Exact remainder criterion for Phi_(p^a) = sum_j X^(j*p^(a-1)).
    s = p**a
    block = s // p
    counts = [0]*s
    for x in q:
        counts[x % s] += 1
    return all(counts[r + j*block] == counts[r]
               for r in range(block) for j in range(1, p))


def phi33_coefficients():
    # Phi_33=(X^33-1)(X-1)/((X^3-1)(X^11-1)).
    def xm1(k):
        return [-1] + [0]*(k - 1) + [1]
    def mul(a, b):
        c = [0]*(len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i + j] += x*y
        return c
    numerator = mul(xm1(33), xm1(1))
    denominator = mul(xm1(3), xm1(11))
    remainder = numerator[:]
    quotient = [0]*(len(numerator) - len(denominator) + 1)
    for i in range(len(numerator) - 1, len(denominator) - 2, -1):
        shift = i - len(denominator) + 1
        coefficient = remainder[i]
        quotient[shift] = coefficient
        for j, coefficient_den in enumerate(denominator):
            remainder[shift + j] -= coefficient*coefficient_den
    assert not any(remainder)
    assert quotient[-1] == 1 and len(quotient) == 21
    return quotient


def phi33_remainder(q, phi33):
    values = [0]*33
    for x in q:
        values[x % 33] += 1
    for i in range(32, 19, -1):
        coefficient = values[i]
        for j, coefficient_phi in enumerate(phi33):
            values[i - 20 + j] -= coefficient*coefficient_phi
    return tuple(values[:20])


def check_case(e, k):
    d, m, n, h, f, g, bases, p, q = make_case(e, k)
    assert len(p) == len(set(p)) == d*5**e
    assert len(q) == len(set(q)) == 165
    assert Y <= set(q) and set(p) & A == {0}
    assert all(bases[y] == y for y in Y)
    for r in range(33):
        fibre = q[5*r:5*r + 5]
        assert {x % 33 for x in fibre} == {r}
        assert {x % 2 for x in fibre} == {int(r % 3 == 1)}
        assert {x % (5**e) for x in fibre} == {f[r % 11]}
        assert len({x % m for x in fibre}) == 5
    sums = distinct_sums(p, q, n)
    assert sums == n
    deltas = sorted({abs(a - b) for a in A for b in A if a != b})
    forbidden = {gcd(t*delta, n) for t in range(1, 331)
                 if gcd(t, 10) == 1 for delta in deltas}
    assert deltas == [3, 5, 8, 11] and forbidden == F
    pair_gcds = {gcd(q[i] - q[j], n)
                 for i in range(len(q)) for j in range(i)}
    assert not (pair_gcds & F)
    observed_pp = {(2, a) for a in range(1, k + 1)
                   if phi_prime_power_divides(q, 2, a)}
    observed_pp |= {(5, a) for a in range(1, e + 2)
                    if phi_prime_power_divides(q, 5, a)}
    observed_pp |= {(p0, 1) for p0 in (3, 11)
                    if phi_prime_power_divides(q, p0, 1)}
    assert observed_pp == {(3, 1), (11, 1), (5, e + 1)}
    assert [sum(x % 33 == r for x in q) for r in range(33)] == [5]*33
    phi33 = phi33_coefficients()
    assert not any(phi33_remainder(q, phi33))
    for divisor in (1, 3, 11, 33):
        s = m*divisor
        block = s // 5
        counts = [0]*s
        for x in q:
            counts[x % s] += 1
        assert all(counts[r + j*block] == counts[r]
                   for r in range(block) for j in range(1, 5))
    print('POSITIVE e=%d K=%d n=%d P=%d Q=%d sums=%d pairs=%d '
          'prime_powers=%s mixed_odd_roots=ok five_lifts=ok scalar=ok' %
          (e, k, n, len(p), len(q), sums, len(q)*(len(q)-1)//2,
           sorted(p0**a for p0, a in observed_pp)), flush=True)
    return d, m, n, h, f, g, bases, p, q


def negative_controls():
    e, k = 2, 4
    d, m, n, h, f, g, bases, p, q = make_case(e, k)
    wrong_parity = crt((0, f[4], 4), (d, m, 33))
    wrong_five_digit = crt((g[4], 5, 4), (d, m, 33))
    wrong_two_digit = crt((8, f[2], 2), (d, m, 33))
    witnessed = (gcd(wrong_parity - bases[1], n),
                 gcd(wrong_five_digit - bases[0], n),
                 gcd(wrong_two_digit - bases[0], n))
    assert witnessed == (3, 5, 8) and set(witnessed) <= F
    print('NEGATIVE scalar altered-g[4], altered-f[4], altered-g[2]: gcds=%s' %
          (witnessed,), flush=True)

    p1 = 33*d
    collision = (p1 + h) % n
    assert p1 in p and collision not in p and 0 in p
    assert 0 in q and h in q
    p_bad = [x for x in p if x != 0] + [collision]
    assert len(p_bad) == len(set(p_bad)) == len(p)
    assert (collision + 0) % n == (p1 + h) % n
    bad_sum_count = distinct_sums(p_bad, q, n)
    assert bad_sum_count == n - 165
    print('NEGATIVE tiling cardinalities preserved; collision=%d; sums=%d '
          'missing=%d' % (collision, bad_sum_count, n - bad_sum_count), flush=True)

    # Swap mixed CRT components while preserving each relevant prime-power
    # marginal.  This keeps all three prime-power divisors but breaks Phi_33.
    a = crt((0, 0, 12), (d, m, 33))
    b = crt((1, 1, 22), (d, m, 33))
    q_set = set(q)
    assert {0, 1} <= q_set and a not in q_set and b not in q_set and a != b
    q_bad = (q_set - {0, 1}) | {a, b}
    assert len(q_bad) == 165
    observed = {(2, z) for z in range(1, k + 1)
                if phi_prime_power_divides(q_bad, 2, z)}
    observed |= {(5, z) for z in range(1, e + 2)
                 if phi_prime_power_divides(q_bad, 5, z)}
    observed |= {(p0, 1) for p0 in (3, 11)
                 if phi_prime_power_divides(q_bad, p0, 1)}
    assert observed == {(3, 1), (11, 1), (5, e + 1)}
    remainder = phi33_remainder(q_bad, phi33_coefficients())
    assert any(remainder)
    print('NEGATIVE T2 mixed-component swap retains prime-power set %s; '
          'Phi_33 nonzero remainder=%s' %
          (sorted(p0**z for p0, z in observed), remainder), flush=True)

    q_missing = q_set - {(4*h) % n}
    assert not phi_prime_power_divides(q_missing, 5, e + 1)
    print('NEGATIVE five-lift: deleting one lift breaks Phi_%d' % m, flush=True)


for e0, k0 in ((2, 4), (2, 5), (3, 4), (2, 6), (3, 5), (4, 4)):
    check_case(e0, k0)
negative_controls()
print('ALL INDEPENDENT EXACT CONTROLS COMPLETED', flush=True)
