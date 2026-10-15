#!/usr/bin/env python3
"""Exact, deterministic finite checks. Run from this target directory.

python3 work/check.py --output evidence/check-results.json
No external packages; a single process. Enumeration is a test oracle, not a
claimed polynomial implementation of an NP-hard forward problem.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
import time
from fractions import Fraction as Q
from pathlib import Path

from algorithms import augment, clip_free_costs, optimize_from_verification, inverse_linf_enumerated, optimize_bottleneck


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def vectors(n):
    return tuple(itertools.product((0, 1), repeat=n))


def families(n, include_empty=False):
    cube = vectors(n)
    for mask in range(0 if include_empty else 1, 1 << len(cube)):
        yield tuple(x for i, x in enumerate(cube) if mask >> i & 1)


class Verification:
    """Independent exhaustive YES/NO oracle; does not expose witnesses."""
    def __init__(self, feasible):
        self.feasible = frozenset(feasible)
        self.calls = 0

    def __call__(self, cost, target):
        assert target in self.feasible, "reduction queried an invalid target"
        self.calls += 1
        assert self.calls < 100_000, "nontermination guard"
        value = dot(cost, target)
        return all(value <= dot(cost, y) for y in self.feasible)


def solve_square(rows, rhs):
    """Exact Gaussian elimination, independent of production algorithms."""
    n = len(rhs)
    a = [[Q(t) for t in row] + [Q(b)] for row, b in zip(rows, rhs)]
    for col in range(n):
        pivot = next((j for j in range(col, n) if a[j][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [x / divisor for x in a[col]]
        for j in range(n):
            if j != col:
                factor = a[j][col]
                a[j] = [x - factor * y for x, y in zip(a[j], a[col])]
    return tuple(row[-1] for row in a)


def independent_linf_lp(feasible, target, c, weights):
    """Enumerate vertices of the original LP in variables (d_1,...,d_n,t).

    Constraints use a·(d,t)<=b. This does not use the ratio formula.
    The epigraph is pointed and an optimum vertex exists for these finite tests.
    """
    n = len(c)
    constraints = []
    for y in feasible:
        if y != target:
            constraints.append((tuple(a - b for a, b in zip(target, y)) + (0,), Q(0)))
    for i in range(n):
        row = [Q(0)] * (n + 1)
        row[i], row[-1] = weights[i], Q(-1)
        constraints.append((tuple(row), weights[i] * c[i]))
        row = [Q(0)] * (n + 1)
        row[i], row[-1] = -weights[i], Q(-1)
        constraints.append((tuple(row), -weights[i] * c[i]))
    constraints.append(((Q(0),) * n + (Q(-1),), Q(0)))
    optimum = None
    vertices = 0
    for selected in itertools.combinations(constraints, n + 1):
        point = solve_square([a for a, _ in selected], [b for _, b in selected])
        if point is None or not all(dot(a, point) <= b for a, b in constraints):
            continue
        vertices += 1
        if optimum is None or point[-1] < optimum:
            optimum = point[-1]
    assert optimum is not None
    return optimum, vertices


def distances(d, c, w):
    delta = [abs(a - b) for a, b in zip(d, c)]
    return (
        sum(a * b for a, b in zip(w, delta)),
        max((a * b for a, b in zip(w, delta)), default=Q(0)),
        sum(a * b * b for a, b in zip(w, delta)),
        sum(a for a, b in zip(w, delta) if b),
        max((a for a, b in zip(w, delta) if b), default=Q(0)),
    )


def satisfies(formula, assignment):
    return all(any(bool(assignment[abs(lit) - 1]) == (lit > 0) for lit in clause)
               for clause in formula)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    start_time = time.monotonic()
    rng = random.Random(20261014)
    counts = dict(augmentation_cases=0, forward_cases=0, forward_oracle_calls=0,
                  sentinel_cases=0, inverse_linf_lp_cases=0, lp_vertices=0,
                  sat_reduction_cases=0, clipping_cases=0, distance_comparisons=0,
                  uniform_hamiltonian_cases=0, unambiguous_threshold_cases=0,
                  bottleneck_cases=0, bottleneck_oracle_calls=0, negative_controls=0)
    digest = hashlib.sha256()

    # Exhaustive over every nonempty feasible subset of {0,1}^n, n<=3,
    # every feasible start, and every cost vector in {-1,0,1}^n.
    for n in range(1, 4):
        for feasible in families(n):
            for c in itertools.product((-1, 0, 1), repeat=n):
                optimum = min(dot(c, y) for y in feasible)
                for x in feasible:
                    v = Verification(feasible)
                    y = augment(v, c, x)
                    assert (y is None) == (dot(c, x) == optimum)
                    if y is not None:
                        assert y in feasible and dot(c, y) < dot(c, x)
                    assert v.calls <= n + 1
                    counts['augmentation_cases'] += 1
                    v = Verification(feasible)
                    result = optimize_from_verification(v, c, x)
                    assert result in feasible and dot(c, result) == optimum
                    counts['forward_cases'] += 1
                    counts['forward_oracle_calls'] += v.calls
                    digest.update(repr((n, feasible, c, x, result)).encode())

    # Signed, rational, and large binary-encoded coefficients; reproducible.
    for _ in range(240):
        n = rng.randrange(1, 9)
        feasible = tuple(x for x in vectors(n) if rng.randrange(4) == 0)
        if not feasible:
            feasible = (vectors(n)[0],)
        c = tuple(Q(rng.randrange(-(1 << 20), 1 << 20), rng.randrange(1, 8)) for _ in range(n))
        x = rng.choice(feasible)
        v = Verification(feasible)
        result = optimize_from_verification(v, c, x)
        assert result in feasible and dot(c, result) == min(dot(c, y) for y in feasible)
        counts['forward_cases'] += 1
        counts['forward_oracle_calls'] += v.calls
        digest.update(repr((feasible, c, x, result)).encode())

    # Empty dimension and zero objective are explicit boundary cases.
    assert optimize_from_verification(Verification(((),)), (), ()) == ()
    assert optimize_from_verification(Verification(((0,), (1,))), (0,), (1,)) == (1,)

    # The same reduction on the dummy-augmented family, including empty F.
    for n in range(1, 4):
        for feasible in families(n, include_empty=True):
            for c in itertools.product((-1, 0, 1), repeat=n):
                dummy = (1,) + (0,) * n
                lifted = (dummy,) + tuple((0,) + x for x in feasible)
                lifted_cost = (1 + sum(map(abs, c)),) + c
                result = optimize_from_verification(Verification(lifted), lifted_cost, dummy)
                assert (result == dummy) == (not feasible)
                if feasible:
                    assert result[0] == 0 and result[1:] in feasible
                    assert dot(c, result[1:]) == min(dot(c, x) for x in feasible)
                counts['sentinel_cases'] += 1

    # Compare inverse l-infinity ratio formula to independent exact LP vertices.
    for _ in range(160):
        n = rng.randrange(1, 4)
        feasible = tuple(x for x in vectors(n) if rng.randrange(2))
        if not feasible:
            feasible = (vectors(n)[0],)
        x = rng.choice(feasible)
        c = tuple(Q(rng.randrange(-3, 4), rng.randrange(1, 4)) for _ in range(n))
        w = tuple(Q(rng.randrange(1, 4), rng.randrange(1, 4)) for _ in range(n))
        d, radius = inverse_linf_enumerated(feasible, c, x, w)
        independent, vertices = independent_linf_lp(feasible, x, c, w)
        assert radius == independent
        assert distances(d, c, w)[1] == radius
        assert all(dot(d, x) <= dot(d, y) for y in feasible)
        counts['inverse_linf_lp_cases'] += 1
        counts['lp_vertices'] += vertices

    # Direct SAT -> restricted-cost family reduction on all ordered pairs of
    # clauses from this two-variable pool (includes unsatisfiable instances).
    clauses = ((), (1,), (-1,), (2,), (-2,), (1, 2), (-1, 2), (1, -2), (-1, -2))
    for formula in itertools.product(clauses, repeat=2):
        witnesses = tuple(a for a in vectors(2) if satisfies(formula, a))
        feasible = tuple(a + z for a in witnesses for z in vectors(2))
        assert bool(feasible) == bool(witnesses)
        assert any(dot((0, 0, 0, 0), x) <= 0 for x in feasible) == bool(witnesses)
        counts['sat_reduction_cases'] += 1
        if not feasible:
            continue
        # Every satisfying witness is equivalent for the allowed costs;
        # test all free targets, baseline costs, and positive weight choices.
        for z0 in vectors(2):
            target = witnesses[0] + z0
            for c in itertools.product((Q(-2), Q(0), Q(2)), repeat=2):
                d = clip_free_costs(c, z0)
                assert all(dot((0, 0) + d, target) <= dot((0, 0) + d, y) for y in feasible)
                candidates = []
                for other in itertools.product(map(Q, (-2, -1, 0, 1, 2)), repeat=2):
                    if all(dot((0, 0) + other, target) <= dot((0, 0) + other, y) for y in feasible):
                        candidates.append(other)
                for w in itertools.product((Q(1), Q(3, 2)), repeat=2):
                    actual = distances(d, c, w)
                    for j in range(5):
                        expected = min(distances(other, c, w)[j] for other in candidates)
                        assert actual[j] == expected
                        counts['distance_comparisons'] += 1
                    counts['clipping_cases'] += 1

    # Natural uniform-parameter illustration, all simple graphs on 3 and 4
    # labelled vertices. Cycles use all vertices, so have identical cost t*n.
    for n in (3, 4):
        edges = tuple(itertools.combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            graph = {edge for j, edge in enumerate(edges) if mask >> j & 1}
            cycles = []
            for perm in itertools.permutations(range(1, n)):
                cycle = (0,) + perm
                used = {tuple(sorted((cycle[i], cycle[(i + 1) % n]))) for i in range(n)}
                if used <= graph:
                    cycles.append(used)
            for t in (-2, 0, 3):
                values = [t * len(cycle) for cycle in cycles]
                assert all(value == t * n for value in values)
                counts['uniform_hamiltonian_cases'] += 1

    # Proposition U: among all possible guessed witnesses, exactly one accepts
    # a satisfiable threshold and zero accepts an unattainable threshold.
    for n in range(1, 4):
        for feasible in families(n, include_empty=True):
            for c in itertools.product((-1, 0, 1), repeat=n):
                q = tuple((1 << n) * value + (1 << i) for i, value in enumerate(c))
                oracle = Verification(feasible)
                unique = tuple(x for x in feasible if oracle(q, x))
                assert len(unique) == int(bool(feasible))
                for threshold in range(-n, n + 1):
                    accepting = sum(dot(c, x) <= threshold for x in unique)
                    attainable = any(dot(c, x) <= threshold for x in feasible)
                    assert accepting == int(attainable)
                    counts['unambiguous_threshold_cases'] += 1

    # The nonlinear min-max boundary: no empty feasible objects, arbitrary
    # feasible families, and a verifier that exposes only YES/NO at 0/1 costs.
    for n in range(1, 4):
        nonempty_cube = vectors(n)[1:]
        for mask in range(1, 1 << len(nonempty_cube)):
            feasible = tuple(x for i, x in enumerate(nonempty_cube) if mask >> i & 1)
            for c in itertools.product((-1, 0, 1), repeat=n):
                def bottleneck(cost, x):
                    return max(value for value, bit in zip(cost, x) if bit)

                optimum = min(bottleneck(c, y) for y in feasible)
                for x0 in feasible:
                    calls = [0]

                    def bottleneck_verify(query, target):
                        assert tuple(target) == x0 and target in feasible
                        assert all(value in (0, 1) for value in query)
                        calls[0] += 1
                        value = bottleneck(query, target)
                        return all(value <= bottleneck(query, y) for y in feasible)

                    result = optimize_bottleneck(bottleneck_verify, c, x0)
                    assert result in feasible and bottleneck(c, result) == optimum
                    assert calls[0] <= n + n.bit_length()
                    counts['bottleneck_cases'] += 1
                    counts['bottleneck_oracle_calls'] += calls[0]

    # Negative control: allowing costs on SAT witness coordinates invalidates
    # the restricted-cost clipping algorithm. This must be detected.
    feasible = ((0, 1, 0), (1, 0, 0), (1, 1, 0))
    assert not Verification(feasible)((1, 1, 0), (1, 1, 0))
    counts['negative_controls'] += 1

    source_hashes = {}
    for filename in ('work/algorithms.py', 'work/check.py'):
        source_hashes[filename] = hashlib.sha256(Path(filename).read_bytes()).hexdigest()
    result = {'status': 'PASS', 'date': '2026-10-14', 'seed': 20261014,
              'arithmetic': 'exact integers and fractions.Fraction', 'processes': 1,
              'counts': counts, 'forward_case_digest': digest.hexdigest(),
              'elapsed_seconds': round(time.monotonic() - start_time, 3),
              'source_sha256': source_hashes,
              'scope': 'Finite sanity checks; the universal theorems are established by proof.md, not enumeration.'}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
