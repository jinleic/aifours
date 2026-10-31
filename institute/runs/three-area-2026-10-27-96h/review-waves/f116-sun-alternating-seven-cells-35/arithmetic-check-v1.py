#!/usr/bin/env python3
"""Independent finite controls for f116; no author code is imported.

This is an arithmetic and small permutation control, not a general-group proof.
It refuses to overwrite its receipt. Run once with assertions enabled.
"""
from collections import deque
from datetime import datetime
from hashlib import sha256
from itertools import product
from math import comb, factorial, gcd, prod
from pathlib import Path
import json
import subprocess
import sys

if not __debug__:
    raise RuntimeError("Assertions must be enabled")

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "arithmetic-receipt-v1.json"
if RECEIPT.exists():
    raise FileExistsError(RECEIPT)


def clock():
    return subprocess.check_output(
        ["/bin/date", "+%Y-%m-%dT%H:%M:%S%z %Z"], text=True
    ).strip()


start_clock = clock()
F = [factorial(k) for k in range(36)]
BASE = 7 * F[35]
assert BASE % 210 == 0


def survivors(a, e):
    return [k for k in range(1, e + 1)
            if (a + 2 * k) % 3 and (a + 2 * k) % 5]


# All residues and all t: the eight reduced classes are precisely those that
# an odd prime greater than 5 can occupy modulo 15. Actual sample primes here
# only illustrate those residue classes; no repunit eligibility is asserted.
allowed = [a for a in range(15) if gcd(a, 15) == 1]
assert allowed == [1, 2, 4, 7, 8, 11, 13, 14]
sieve_rows = []
for a in range(15):
    counts = [1 + len(survivors(a, t // 2)) for t in range(1, 36)]
    assert all(counts[2 * e - 1] == counts[2 * e] for e in range(1, 18))
    if a in allowed:
        assert max(counts) <= 10
    else:
        assert a % 3 == 0 or a % 5 == 0
        representative = BASE + a
        if representative % 2 == 0:
            representative += 15
        assert representative > 5
        assert representative % (3 if a % 3 == 0 else 5) == 0
    sieve_rows.append({
        "residue_mod_15": a,
        "prime_above_5_permitted": a in allowed,
        "upper_at_E_13_14_15_16_17": [1 + len(survivors(a, e))
                                      for e in range(13, 18)],
        "maximum_t_1_through_35": max(counts),
    })


def prime_by_trial(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


sample_primes = {}
n = 431
while len(sample_primes) < len(allowed):
    if prime_by_trial(n):
        a = n % 15
        assert a in allowed
        sample_primes.setdefault(a, n)
    n += 2
assert set(sample_primes) == set(allowed)

# Nonempty, disjoint supports of six cofactors, with at most ten primes.
# Every possible size is <=5; enumerate the ordered sizes independently.
support_patterns = [s for s in product(range(1, 6), repeat=6) if sum(s) <= 10]
assert len(support_patterns) == 210
assert min(s.count(1) for s in support_patterns) == 2
assert (1, 1, 2, 2, 2, 2) in support_patterns
assert sum((1, 2, 2, 2, 2, 2)) == 11

# Uniform endpoint inequalities, used only for the no-7p lemma, NOT as a
# claim that r=419 satisfies the factorial threshold at t near 35.
endpoint = 419
binomial_margin = comb(endpoint + 1, 2) - 7 * (endpoint + 35)
factorial_margin = (endpoint - 2) * (endpoint - 3) - 7 * (endpoint + 35)
assert (binomial_margin, factorial_margin) == (84812, 170294)

# Test every window and each one of its cells, in every residue class mod 7,
# at r+1 > 7*35!, hence also at every lesser threshold. Synthetic r need not
# be prime: the arithmetic lemmas do not use primality.
window_count = cancellation_count = without_cell = with_cell = 0
with_cell_binomial_seven_free = with_cell_binomial_seven_divisible = 0
max_cells = 0
for residue in range(7):
    delta = residue or 7
    if delta % 2 == 0:
        delta += 7
    r = BASE + delta
    assert r % 7 == residue and r % 2 == 1 and r + 1 > 7 * F[35]
    for t in range(1, 36):
        assert r + 1 > 7 * F[t]
        cells = {h for h in range(1, t + 1) if (r + h) % 7 == 0}
        max_cells = max(max_cells, len(cells))
        assert len(cells) <= 5
        for left in range(1, t + 1):
            for right in range(left, t + 1):
                u = right - left + 1
                b = comb(r + right, u)
                assert b * F[u] == prod(r + h for h in range(left, right + 1))
                has_cell = any(h in cells for h in range(left, right + 1))
                if has_cell:
                    with_cell += 1
                    if b % 7:
                        with_cell_binomial_seven_free += 1
                    else:
                        with_cell_binomial_seven_divisible += 1
                else:
                    without_cell += 1
                    assert u <= 6 and F[u] % 7 and b % 7
                for h in range(left, right + 1):
                    a = r + h
                    local = a // gcd(a, F[u])
                    uniform = a // gcd(a, F[t])
                    assert local % uniform == 0
                    assert b % local == 0 and b % uniform == 0 and uniform > 7
                    cancellation_count += 1
                window_count += 1
assert window_count == 7 * comb(37, 3) == 54390
assert max_cells == 5
assert with_cell_binomial_seven_free and with_cell_binomial_seven_divisible

# Arithmetic mutation controls: each defective assertion has a concrete
# counterexample. These are not counterexamples to the proven hypotheses.
a = allowed[0]
no_five_sieve = 1 + sum((a + 2 * k) % 3 != 0 for k in range(1, 18))
assert no_five_sieve == 12 and no_five_sieve > 10
r = BASE + 1
b = comb(r + 2, 2)
a_cell = r + 1
assert a_cell % 2 == 0 and b % a_cell != 0
assert b % (a_cell // gcd(a_cell, 2)) == 0
r_reverse = BASE + 55
assert r_reverse % 2 and (r_reverse + 1) % 49 == 7
assert (r_reverse + 1) % 7 == 0 and comb(r_reverse + 7, 7) % 7 != 0
r_equal = 7 * F[7] - 1
assert r_equal >= 419 and r_equal + 1 == 7 * F[7]
assert (r_equal + 1) // gcd(r_equal + 1, F[7]) == 7
r_strict = BASE + 1
assert (r_strict + 1) // gcd(r_strict + 1, F[1]) == r_strict + 1
assert (r_strict + 1) > 7 * F[1]
# Disallowed quotient-factor mutant c=7 defeats the seven-free-chain step.
assert (r + 1) % 7 != 0 and (7 * (r + 1)) % 7 == 0 and F[1] % 7 != 0
assert any(row["maximum_t_1_through_35"] > 10
           for row in sieve_rows if not row["prime_above_5_permitted"])

# Independently generate concrete actual subgroups of alternating groups on
# two blocks. P is the image of K, L its small-block kernel. Their sizes are
# extracted from explicit permutation closures, not assigned by formula.
def cycle(n, *points):
    p = list(range(n))
    for i, x in enumerate(points):
        p[x] = points[(i + 1) % len(points)]
    return tuple(p)


def multiply(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p))
               for j in range(i + 1, len(p))) % 2


def closure(n, generators):
    identity = tuple(range(n))
    seen = {identity}
    todo = deque([identity])
    while todo:
        g = todo.popleft()
        for x in generators:
            y = multiply(g, x)
            if y not in seen:
                seen.add(y)
                todo.append(y)
    return seen


def fixed_small(u):
    return tuple(range(u))


def subgroup_case(name, m, u, generators, expected):
    n = m + u
    group = closure(n, generators)
    assert all(not parity(g) for g in group)
    assert all(set(g[:m]) == set(range(m)) for g in group)
    assert {g[0] for g in group} == set(range(m))
    k = {g for g in group if not parity(g[:m])}
    assert len(group) % len(k) == 0
    h = len(group) // len(k)
    projection = {tuple(g[:m]) for g in k}
    kernel = {tuple(g[m + i] - m for i in range(u)) for g in k
              if tuple(g[:m]) == tuple(range(m))}
    assert fixed_small(u) in kernel
    assert len(k) == len(projection) * len(kernel)
    assert all(not parity(p) for p in projection)
    assert all(not parity(p) for p in kernel)
    if u == 1:
        c = 1
        assert h == 1 and len(kernel) == 1
    else:
        small_alt = F[u] // 2
        assert small_alt % len(kernel) == 0 and h in (1, 2)
        assert (2 * small_alt) % (h * len(kernel)) == 0
        c = 2 * small_alt // (h * len(kernel))
    assert F[u] % c == 0
    assert F[m] // 2 % len(projection) == 0
    total_order = F[n] // 2
    assert total_order % len(group) == 0
    actual_index = total_order // len(group)
    factorized = comb(n, u) * (F[m] // 2 // len(projection)) * c
    assert actual_index == factorized
    assert (len(group), h, len(projection), len(kernel), c) == expected
    return {"name": name, "m": m, "u": u, "H_order": len(group),
            "h": h, "P_order": len(projection), "L_order": len(kernel),
            "c": c, "u_factorial": F[u], "actual_index": actual_index}


m, u = 5, 4
n = m + u
big_alt = [cycle(n, 0, 1, i) for i in range(2, m)]
small_alt = [cycle(n, m, m + 1, m + i) for i in range(2, u)]
coupled_transpositions = multiply(cycle(n, 0, 1), cycle(n, m, m + 1))
r5 = cycle(n, 0, 1, 2, 3, 4)
reflection = multiply(cycle(n, 1, 4), cycle(n, 2, 3))
small_c3 = cycle(n, m, m + 1, m + 2)
mul2 = list(range(n))
for x in range(5):
    mul2[x] = (2 * x) % 5
coupled_normalizer = multiply(tuple(mul2), cycle(n, m, m + 1))
subgroups = [
    subgroup_case("A5 times A4", m, u, big_alt + small_alt, (720, 1, 60, 12, 2)),
    subgroup_case("full sign-matched block", m, u,
                  big_alt + small_alt + [coupled_transpositions], (1440, 2, 60, 12, 1)),
    subgroup_case("D5 times C3", m, u, [r5, reflection, small_c3], (30, 1, 10, 3, 8)),
    subgroup_case("coupled D5/C3 extension", m, u,
                  [r5, small_c3, coupled_normalizer], (60, 2, 10, 3, 4)),
]
m, u = 5, 2
n = m + u
big_alt = [cycle(n, 0, 1, i) for i in range(2, m)]
coupled_transpositions = multiply(cycle(n, 0, 1), cycle(n, m, m + 1))
subgroups += [
    subgroup_case("A5 with A2 trivial", m, u, big_alt, (60, 1, 60, 1, 2)),
    subgroup_case("sign-matched with A2 trivial", m, u,
                  big_alt + [coupled_transpositions], (120, 2, 60, 1, 1)),
]
m, u = 5, 1
subgroups.append(subgroup_case("singleton small block and C5", m, u,
                               [cycle(m + u, 0, 1, 2, 3, 4)], (5, 1, 5, 1, 1)))

receipt = {
    "scope": "Independent exact finite controls only; not a general-group or source-proof replay",
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "manifest_sha256": "45d6a1dd19ea3d528c71401327f6724e83524cbb43e902633a6a8fbb50e42818",
    "python": sys.version,
    "clock_observed_before_control": start_clock,
    "sieve": {"residues": sieve_rows, "allowed_residue_actual_small_primes": sample_primes,
              "small_primes_not_asserted_repunit_eligible_or_t35_threshold": True,
              "allowed_cases": 8 * 35, "disallowed_cases": 7 * 35},
    "pigeonhole": {"support_size_patterns": len(support_patterns),
                    "minimum_singletons": 2, "sharp_ten_support_sizes": [1, 1, 2, 2, 2, 2],
                    "eleven_counterpattern": [1, 2, 2, 2, 2, 2]},
    "endpoint_inequalities_only": {"r": endpoint, "binomial_margin": binomial_margin,
                                    "factorial_product_margin": factorial_margin,
                                    "threshold_assumed_at_endpoint": False},
    "window_controls": {"synthetic_r_formula": "7*35! + odd delta in each mod-7 class",
                        "strict_threshold_met_for_all_t": True, "windows": window_count,
                        "cell_cancellation_checks": cancellation_count,
                        "maximum_seven_cells": max_cells, "windows_without_cell": without_cell,
                        "windows_with_cell": with_cell,
                        "with_cell_binomial_seven_free": with_cell_binomial_seven_free,
                        "with_cell_binomial_seven_divisible": with_cell_binomial_seven_divisible},
    "mutations": {
        "omit_sieve_by_5": {"bad_upper_bound_at_E17": no_five_sieve},
        "claim_full_cell_divides_binomial": {"cell": str(a_cell), "remainder": str(b % a_cell)},
        "claim_seven_cell_forces_binomial_divisible_by_7": {
            "r_formula": "7*35!+55", "u": 7, "binomial_mod_7": comb(r_reverse + 7, 7) % 7},
        "weaken_strict_threshold_to_equality": {"t": 7, "synthetic_r": r_equal,
                                                 "uniform_quotient": 7},
        "author_strict_intermediate": {"t": 1, "h": 1, "relation": "equality, not >"},
        "drop_c_divides_u_factorial": {"u": 1, "disallowed_c": 7},
        "eleven_large_primes": {"six_support_sizes": [1, 2, 2, 2, 2, 2]},
        "apply_reduced_residue_bound_to_disallowed_residues": "counterexample present in sieve rows"
    },
    "permutation_generated_block_subgroups": subgroups,
    "status": "PASS"
}
receipt["clock_observed_immediately_before_receipt_write"] = clock()
encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
with RECEIPT.open("x", encoding="utf-8") as out:
    out.write(encoded)
print(encoded, end="")
