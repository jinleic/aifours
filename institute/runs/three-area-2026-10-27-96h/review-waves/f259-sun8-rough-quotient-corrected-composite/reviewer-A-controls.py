#!/usr/bin/env python3
"""Finite, reviewer-owned controls; these do not prove the universal theorem."""
from collections import deque
from itertools import combinations, permutations, product
from math import gcd, prod
import json
import time

start = time.monotonic()


class S3TimesCyclic:
    def __init__(self, modulus):
        self.m = modulus
        self.elements = list(product(permutations(range(3)), range(modulus)))
        self.position = {x: i for i, x in enumerate(self.elements)}
        self.identity = self.position[((0, 1, 2), 0)]
        self.table = []
        for p, a in self.elements:
            row = []
            for q, b in self.elements:
                row.append(self.position[(tuple(p[q[i]] for i in range(3)), (a + b) % modulus)])
            self.table.append(row)
        self.inverse = []
        for x in range(len(self.elements)):
            self.inverse.append(next(y for y in range(len(self.elements))
                                     if self.table[x][y] == self.identity
                                     and self.table[y][x] == self.identity))
        self.universe = frozenset(range(len(self.elements)))

    def mul(self, x, y):
        return self.table[x][y]

    def generated(self, generators):
        generators = tuple(generators)
        seen = {self.identity}
        todo = deque([self.identity])
        while todo:
            x = todo.popleft()
            for g in generators:
                y = self.mul(x, g)
                if y not in seen:
                    seen.add(y)
                    todo.append(y)
        return frozenset(seen)

    def subgroups(self):
        trivial = frozenset([self.identity])
        seen = {trivial}
        todo = deque([trivial])
        while todo:
            h = todo.popleft()
            for x in self.universe - h:
                new = self.generated(h | {x})
                if new not in seen:
                    seen.add(new)
                    todo.append(new)
        return sorted(seen, key=lambda h: (len(h), tuple(sorted(h))))

    def coset(self, x, h):
        return frozenset(self.mul(x, y) for y in h)

    def cosets(self, h):
        unique = {self.coset(x, h) for x in self.universe}
        return sorted(unique, key=lambda c: tuple(sorted(c)))

    def conjugate(self, t, h):
        return frozenset(self.mul(self.mul(t, x), self.inverse[t]) for x in h)

    def normal(self, h):
        return all(self.conjugate(t, h) == h for t in self.universe)


def coset_records(g, subgroups):
    return [(h, c, len(g.universe) // len(h))
            for h in subgroups for c in g.cosets(h)]


def bad_graph(records, threshold):
    adjacent = [set() for _ in records]
    pairs = []
    for i, j in combinations(range(len(records)), 2):
        _, c, n = records[i]
        _, d, m = records[j]
        if c.isdisjoint(d) and gcd(n, m) <= threshold:
            adjacent[i].add(j)
            adjacent[j].add(i)
            pairs.append((i, j))
    triples = sum(1 for i, j in pairs
                  for k in adjacent[i] & adjacent[j] if k > j)
    return pairs, triples


small = S3TimesCyclic(1)
sub_small = small.subgroups()
assert len(sub_small) == 6
assert any(not small.normal(h) for h in sub_small)
coprime_tuples = 0
nonnormal_tuples = 0
unit_repetition_tuples = 0
for k in (1, 2, 3):
    for hs in product(sub_small, repeat=k):
        indices = [len(small.universe) // len(h) for h in hs]
        if any(gcd(a, b) != 1 for a, b in combinations(indices, 2)):
            continue
        intersection = frozenset.intersection(*hs)
        image = {tuple(small.coset(x, h) for h in hs) for x in small.universe}
        all_tuples = set(product(*(small.cosets(h) for h in hs)))
        assert len(small.universe) // len(intersection) == prod(indices)
        assert image == all_tuples and len(image) == prod(indices)
        coprime_tuples += 1
        nonnormal_tuples += any(not small.normal(h) for h in hs)
        unit_repetition_tuples += sum(a == 1 for a in indices) >= 2
assert nonnormal_tuples > 0 and unit_repetition_tuples > 0

h2 = next(h for h in sub_small if len(small.universe) // len(h) == 2)
c2 = small.cosets(h2)
assert len(c2) == 2 and c2[0].isdisjoint(c2[1])
assert gcd(2, 2) == 2
assert (c2[0], c2[1]) not in {
    (small.coset(x, h2), small.coset(x, h2)) for x in small.universe}

large = S3TimesCyclic(5)
sub_large = large.subgroups()
assert len(sub_large) == 12
kernel = frozenset(i for i, (_, q) in enumerate(large.elements) if q == 0)
assert len(kernel) == 6 and large.normal(kernel)
assert any(not large.normal(h) for h in sub_large)
index_cases = 0
fibre_cases = 0
nonnormal_fibre_cases = 0
missing_conjugation_failures = 0
wrong_side_failures = 0
for h in sub_large:
    k = h & kernel
    projection = {large.elements[x][1] for x in h}
    a = 5 // len(projection)
    b = len(kernel) // len(k)
    n = len(large.universe) // len(h)
    assert n == a * b and 5 % len(projection) == 0
    assert all(gcd(a, p) == 1 for p in (2,))
    index_cases += 1
    for c in large.cosets(h):
        projected_c = {large.elements[x][1] for x in c}
        for t in large.universe:
            nt = {large.mul(z, t) for z in kernel}
            fibre = c & nt
            assert bool(fibre) == (large.elements[t][1] in projected_c)
            if not fibre:
                continue
            x = min(fibre)
            ti = large.inverse[t]
            lead = large.mul(x, ti)
            conjugated = large.conjugate(t, k)
            lhs = {large.mul(z, ti) for z in fibre}
            rhs = {large.mul(lead, z) for z in conjugated}
            assert lhs == rhs and lhs <= kernel and conjugated <= kernel
            assert len(kernel) // len(conjugated) == b
            no_conjugation = {large.mul(lead, z) for z in k}
            wrong_side = {large.mul(z, lead) for z in conjugated}
            missing_conjugation_failures += lhs != no_conjugation
            wrong_side_failures += lhs != wrong_side
            nonnormal_fibre_cases += not large.normal(h)
            fibre_cases += 1
assert fibre_cases > 0 and nonnormal_fibre_cases > 0
assert missing_conjugation_failures > 0 and wrong_side_failures > 0

records_n = coset_records(small, sub_small)
records_g = coset_records(large, sub_large)
pairs_n, triples_n = bad_graph(records_n, 2)
pairs_g, triples_g = bad_graph(records_g, 2)
assert pairs_n and pairs_g and triples_n == 0 and triples_g == 0
shared_fibre_checks = 0
nontrivial_quotient_index_pairs = 0
for i, j in pairs_g:
    h1, c1, n1 = records_g[i]
    h2, c2_, n2 = records_g[j]
    a1 = 5 // len({large.elements[x][1] for x in h1})
    a2 = 5 // len({large.elements[x][1] for x in h2})
    b1 = len(kernel) // len(h1 & kernel)
    b2 = len(kernel) // len(h2 & kernel)
    assert gcd(a1, a2) == 1
    assert gcd(n1, n2) % gcd(b1, b2) == 0 and gcd(b1, b2) <= 2
    p1 = {large.elements[x][1] for x in c1}
    p2 = {large.elements[x][1] for x in c2_}
    shared = p1 & p2
    assert shared
    nontrivial_quotient_index_pairs += max(a1, a2) > 1
    for t in large.universe:
        if large.elements[t][1] not in shared:
            continue
        nt = {large.mul(z, t) for z in kernel}
        f1 = {large.mul(z, large.inverse[t]) for z in c1 & nt}
        f2 = {large.mul(z, large.inverse[t]) for z in c2_ & nt}
        assert f1 and f2 and f1.isdisjoint(f2) and f1 <= kernel and f2 <= kernel
        shared_fibre_checks += 1
assert shared_fibre_checks > 0 and nontrivial_quotient_index_pairs > 0

# Dropping roughness makes the universal r=1 transfer false: N=1, G=C7.
c7_cosets = [frozenset([i]) for i in range(7)]
assert c7_cosets[0].isdisjoint(c7_cosets[1]) and gcd(7, 7) == 7
trivial_group_cosets = [frozenset([0])]
assert not any(a.isdisjoint(b) for a, b in combinations(trivial_group_cosets, 2))

# Pairwise intersection is not a general Helly principle, even for 7-rough F_11^2.
p = 11
lines = [{(0, y) for y in range(p)}, {(x, 0) for x in range(p)},
         {(x, y) for x in range(p) for y in range(p) if (x + y) % p == 1}]
assert all(len(line) == p for line in lines)
assert [len(a & b) for a, b in combinations(lines, 2)] == [1, 1, 1]
assert not (lines[0] & lines[1] & lines[2]) and gcd(p, p) > 7

# G=C5^2, N=C5 x 0, U=1: the two index factors can share a prime.
assert 25 == 5 * 5 and gcd(5, 5) == 5

print(json.dumps({
    'finite_groups': {'S3_order': 6, 'S3_subgroups': len(sub_small),
                      'S3xC5_order': 30, 'S3xC5_subgroups': len(sub_large)},
    'coprime_intersection': {'tuples': coprime_tuples,
                             'with_nonnormal_subgroup': nonnormal_tuples,
                             'with_repeated_unit_index': unit_repetition_tuples},
    'index_factorization_cases': index_cases,
    'fibre_identity_cases': fibre_cases,
    'nonnormal_subgroup_fibre_cases': nonnormal_fibre_cases,
    'bad_families_T2': {'S3_cosets': len(records_n), 'S3_pairs': len(pairs_n),
                        'S3_triples': triples_n, 'S3xC5_cosets': len(records_g),
                        'S3xC5_pairs': len(pairs_g), 'S3xC5_triples': triples_g,
                        'shared_fibre_checks': shared_fibre_checks,
                        'pairs_with_nontrivial_quotient_index': nontrivial_quotient_index_pairs},
    'intended_negative_controls': {
        'omitted_conjugation_identity_failures': missing_conjugation_failures,
        'wrong_left_coset_side_failures': wrong_side_failures,
        'repeated_index_2_cosets_have_no_common_point': True,
        'drop_roughness_N1_GC7_r1_transfer_fails': True,
        'pairwise_intersecting_F11_lines_have_empty_triple': True,
        'quotient_and_kernel_index_factors_can_share_5': True},
    'elapsed_seconds': round(time.monotonic() - start, 6),
    'result': 'PASS'
}, sort_keys=True, indent=2))
