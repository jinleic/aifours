#!/usr/bin/env python3
"""Reviewer-owned bounded finite controls, independent of candidate code.

These are diagnostic instances, not universal proofs.  All checks use exact
integer arithmetic; no author artifact is loaded or executed.
"""
from collections import deque
from itertools import combinations
from math import gcd


def counts(n, left, right):
    out = [0] * n
    for x in left:
        for y in right:
            out[(x + y) % n] += 1
    return out


def normalized_tilings(n):
    """Enumerate tilings with 0 in each factor by exact-cover recursion."""
    full = (1 << n) - 1
    for size in range(1, n + 1):
        if n % size:
            continue
        for rest in combinations(range(1, n), size - 1):
            left = (0,) + rest
            masks = []
            for shift in range(n):
                mask = 0
                for x in left:
                    mask |= 1 << ((x + shift) % n)
                masks.append(mask)

            def complete(covered, right):
                if covered == full:
                    yield left, tuple(right)
                    return
                gap = full ^ covered
                first = (gap & -gap).bit_length() - 1
                for x in left:
                    shift = (first - x) % n
                    tile = masks[shift]
                    if not covered & tile:
                        yield from complete(covered | tile, right + [shift])

            yield from complete(masks[0], [0])


def dilation_controls():
    pairs = checks = prime_checks = nonunit_checks = 0
    for n in range(2, 17):
        for left, right in normalized_tilings(n):
            pairs += 1
            assert counts(n, left, right) == [1] * n
            for t in range(1, n + 1):
                if gcd(t, len(left)) != 1:
                    continue
                scaled = tuple((t * x) % n for x in left)
                assert len(set(scaled)) == len(left)
                assert counts(n, scaled, right) == [1] * n
                checks += 1
                if gcd(t, n) != 1:
                    nonunit_checks += 1
            for ell in (2, 3, 5, 7, 11):
                if len(left) % ell == 0:
                    continue
                scaled = tuple((ell * x) % n for x in left)
                coefficients = counts(n, scaled, right)
                assert all(c % ell == 1 for c in coefficients)
                assert sum(coefficients) == n
                assert coefficients == [1] * n
                prime_checks += 1
    # Dropping coprimality produces a repeated scaled point and failed cover.
    left, right = (0, 2, 4, 6), (0, 1)
    assert counts(8, left, right) == [1] * 8
    bad = tuple((2 * x) % 8 for x in left)
    assert gcd(2, len(left)) == 2 and len(set(bad)) < len(left)
    assert counts(8, bad, right) != [1] * 8
    # Multiplication need not be a unit modulo the ambient group.
    left, right = (0, 1, 2), (0, 3, 6, 9)
    assert counts(12, left, right) == [1] * 12
    assert gcd(2, len(left)) == 1 and gcd(2, 12) != 1
    assert counts(12, tuple(2 * x % 12 for x in left), right) == [1] * 12
    print('dilation normalized_tilings=', pairs, 'coprime_multiplier_checks=', checks,
          'prime_congruence_checks=', prime_checks, 'nonunit_ambient_checks=', nonunit_checks)
    print('dilation negatives: noncoprime t=2 repeats P in Z_8; ambient nonunit t=2 is allowed in Z_12')


def unit_orbit_controls():
    cases = 0
    for n in range(2, 91):
        units = [u for u in range(n) if gcd(u, n) == 1]
        for a in range(n):
            orbit = {(u * a) % n for u in units}
            same_gcd = {b for b in range(n) if gcd(b, n) == gcd(a, n)}
            assert orbit == same_gcd
            cases += len(same_gcd)
    assert 3 not in {(u * 2) % 12 for u in range(12) if gcd(u, 12) == 1}
    assert gcd(2, 12) != gcd(3, 12)
    print('CRT unit orbits: equal-gcd ordered pairs=', cases, 'for n=2..90')
    print('CRT negative: 2 and 3 in Z_12 have different gcds and no unit connects them')


def reduction_controls():
    odd = missing = equal_difference = 0
    for n in range(15, 2501):
        if n % 2:
            assert gcd(8, n) == gcd(1, n) == 1
            odd += 1
        for ell in (3, 5, 11):
            if n % ell:
                assert gcd(ell, n) == gcd(1, n) == 1
                missing += 1
    for n in range(330, 3961, 330):
        for ell in (3, 5, 11):
            assert 0 < ell < n and gcd(ell, n) == ell
            # Both factors containing 0 and ell have distinct representations of ell.
            c = counts(n, (0, ell), (0, ell))
            assert c[ell] >= 2
            equal_difference += 1
    print('R1/R2: odd-order witnesses=', odd, 'missing-prime witnesses=', missing,
          'scaled-equal-difference collisions=', equal_difference)


def divisors(factors):
    out = [1]
    for prime, exponent in factors.items():
        out = [d * prime ** e for d in out for e in range(exponent + 1)]
    return out


def tail_controls():
    forced = 0
    for p in (3, 5, 11):
        q1, q2 = [q for q in (3, 5, 11) if q != p]
        for k in range(1, 4):
            for v in range(2, 5):
                for extra in (1, q1, 7):
                    factors = {p: v, q1: 1, q2: 1}
                    if extra != 1:
                        factors[extra] = factors.get(extra, 0) + 1
                    odd_part = 1
                    for prime, exponent in factors.items():
                        odd_part *= prime ** exponent
                    n = 2 ** k * odd_part
                    for a in range(k + 1):
                        for g in divisors(factors):
                            if g % q1 and g % q2:
                                continue
                            if g % (p * p) == 0:
                                continue
                            ell = p if g % p == 0 else (q1 if g % q1 == 0 else q2)
                            t = g // ell
                            assert g < n and t % 2 == 1
                            assert gcd(t, p * 2 ** a) == 1
                            assert gcd(t * ell, n) == g
                            forced += 1
    n, p, q1, q2, a = 990, 3, 5, 11, 1
    p2_exception = 45
    assert gcd(p2_exception, n) == p2_exception and p2_exception % (p * p) == 0
    assert not any(gcd(t, p * 2 ** a) == 1 and gcd(t * ell, n) == p2_exception
                   for t in range(1, n + 1) for ell in (p, q1, q2))
    even_g = 10
    assert even_g % 2 == 0 and even_g % q1 == 0 and even_g % (p * p) != 0
    assert not any(gcd(t, p * 2 ** a) == 1 and gcd(t * ell, n) == even_g
                   for t in range(1, n + 1) for ell in (p, q1, q2))
    print('R3 odd-divisor forbidden-gcd witnesses=', forced)
    print('R3 negatives: gcd=45 has p^2 and is not forced out; even gcd=10 is outside the rule (n=990,p=3,a=1)')


def fibre_controls():
    ratios = 0
    for p in (3, 5, 11):
        for v in range(2, 6):
            for k in range(1, 7):
                for a in range(k + 1):
                    b = k - a
                    subgroup = p ** (v - 2) * 2 ** k
                    fibre = p ** (v - 1) * 2 ** b
                    assert subgroup % fibre != 0
                    assert subgroup * p == fibre * 2 ** a
                    ratios += 1
    # A p^2-sized head admits a constant-mod-p^2 complementary factor.
    p, n = 3, 18
    left = tuple(range(p * p))
    right = tuple(range(0, n, p * p))
    assert len(left) == p * p and counts(n, left, right) == [1] * n
    assert len({x % (p * p) for x in right}) == 1
    print('fibre noninteger ratios=', ratios)
    print('fibre negative: unanchored Z_18 with |P|=3^2 tiles and Q={0,9} is constant mod 9')


def parity_controls():
    masks = 1 << 9
    checked = accepted = 0
    for e in range(1, masks):
        evens = [i for i in range(9) if e & (1 << i)]
        for o in range(1, masks):
            odds = [i for i in range(9) if o & (1 << i)]
            all_equal = all(x == y for x in evens for y in odds)
            if all_equal:
                assert e == o and e & (e - 1) == 0
                accepted += 1
            checked += 1
    # One matching pair is insufficient to infer constant fibres.
    e, o = {0, 1}, {0, 2}
    assert e & o and len(e) > 1 and len(o) > 1
    assert not all(x == y for x in e for y in o)
    print('parity/cross-pair residue-set pairs=', checked, 'all-equal cases=', accepted)
    print('parity negative: existence of one equal cross pair does not force either fibre constant')


def graph_controls():
    graphs = 0
    for p in (3, 5, 11):
        q1, q2 = [q for q in (3, 5, 11) if q != p]
        for extra in (1, q1, 7):
            rsize = q1 * q2 * extra
            seen, queue = {0}, deque([0])
            while queue:
                x = queue.popleft()
                for step in (q1, -q1, q2, -q2):
                    y = (x + step) % rsize
                    if y not in seen:
                        seen.add(y)
                        queue.append(y)
            assert len(seen) == rsize
            graphs += 1
    rsize, steps = 15, (3, 5)
    edges = [(x, (x + step) % rsize) for x in range(rsize) for step in steps]
    partitions = 0
    for mask in range(1, (1 << rsize) - 1):
        assert any(((mask >> x) ^ (mask >> y)) & 1 for x, y in edges)
        partitions += 1
    block = {x for x in range(15) if x % 3 == 0}
    assert block and len(block) < 15
    assert all(((x in block) == (((x + 3) % 15) in block)) for x in range(15))
    print('graph connected instances=', graphs, 'nontrivial Z_15 partitions=', partitions)
    print('graph negative: step 3 alone on Z_15 leaves the residue-0 mod 3 block disconnected')


def j0_controls():
    n, pset = 330, (0, 165)
    for odd_choice in (False, True):
        qset = list(range(165))
        if odd_choice:
            qset[6] = 171
        assert counts(n, pset, qset) == [1] * n
        assert all(x in qset for x in (0, 1, 7, 13, 14))
        q = 171 if odd_choice else 6
        assert q % 165 == 6
        x = q if q % 2 else q - 1
        ell = 3 if q % 2 else 5
        assert x % 2 == 1 and x % ell == 0
        g = gcd(x, n)
        assert g % ell == 0 and gcd(g // ell, len(pset)) == 1
        assert gcd((g // ell) * ell, n) == g
        # This unanchored control tiling does not contain the needed A-witness.
        assert ell not in pset
    print('j=0 parity branches: exact unanchored Z_330 tilings checked=2')
    print('j=0 negative: without the P-anchor, the available Q difference does not contradict the tiling')


dilation_controls()
unit_orbit_controls()
reduction_controls()
tail_controls()
fibre_controls()
parity_controls()
graph_controls()
j0_controls()
print('ALL REVIEWER FINITE CONTROLS COMPLETED')
