#!/usr/bin/env python3
"""Independent, finite necessary-condition controls; no research-code imports."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

EDGES = tuple(combinations(range(4), 2))
EDGE_INDEX = {edge: k for k, edge in enumerate(EDGES)}
MATCHINGS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
WORDS = tuple(product((0, 1), repeat=4))
SWITCHES = tuple(product((0, 1), repeat=4))


def relation(e, i, j):
    return e[EDGE_INDEX[tuple(sorted((i, j)))]]


def transformed(e, permutation, switch):
    return tuple(relation(e, permutation[i], permutation[j]) ^ switch[i] ^ switch[j]
                 for i, j in EDGES)


def orbit(e):
    return {transformed(e, p, s) for p in permutations(range(4)) for s in SWITCHES}


def core(e):
    return {word for word in WORDS if any(
        all((word[i] ^ word[j]) == relation(e, i, j) for i, j in matching)
        for matching in MATCHINGS)}


def relabel(word, switch):
    return tuple(a ^ b for a, b in zip(word, switch))


def switch_to_constant(e, constant):
    return next(s for s in SWITCHES if all(
        relation(e, i, j) ^ s[i] ^ s[j] == constant for i, j in EDGES))


def fiber_counts_ok(fiber, e, i, a):
    if len(fiber) != 5 or any(w[i] != a for w in fiber):
        return False
    for j in range(4):
        if i == j:
            continue
        neighbor = a ^ relation(e, i, j)
        if sum(w[j] == neighbor for w in fiber) != 3:
            return False
        if sum(w[j] != neighbor for w in fiber) != 2:
            return False
    return True


def pair_count(points, i, j, a, b):
    return sum(w[i] == a and w[j] == b for w in points)


def cap(e, i, j, a, b):
    return 3 if (a ^ b) == relation(e, i, j) else 2


def connected(rowsets, n):
    pending = [(0, 0)]
    seen_rows, seen_cols = set(), set()
    while pending:
        side, v = pending.pop()
        seen = seen_rows if side == 0 else seen_cols
        if v in seen:
            continue
        seen.add(v)
        if side == 0:
            pending.extend((1, c) for c in rowsets[v])
        else:
            pending.extend((0, r) for r in range(n) if v in rowsets[r])
    return len(seen_rows) == n and len(seen_cols) == n


# Examine connected support patterns with excess 0,1,2.
# A repeated degree-2 pair spans C^2; a connected block larger than 2
# cannot contain that pair. Track the weaker one-overlap condition separately.
patterns_before_span = Counter()
patterns = Counter()
for n in range(2, 5):
    cells = tuple(product(range(n), repeat=2))
    for size in range(2 * n, min(n * n, 2 * n + 2) + 1):
        for chosen in combinations(cells, size):
            rows = [set() for _ in range(n)]
            cols = [set() for _ in range(n)]
            for r, c in chosen:
                rows[r].add(c)
                cols[c].add(r)
            if min(map(len, rows)) < 2 or min(map(len, cols)) < 2:
                continue
            if any(len(rows[r] & rows[s]) == 1 for r, s in combinations(range(n), 2)):
                continue
            if connected(rows, n):
                patterns_before_span[(n, size - 2 * n)] += 1
                if n > 2 and any(len(rows[r]) == 2 and rows[r] == rows[s]
                                 for r, s in combinations(range(n), 2)):
                    continue
                patterns[(n, size - 2 * n)] += 1
assert patterns_before_span == Counter({(2, 0): 1, (3, 2): 9, (4, 2): 72}), patterns_before_span
assert patterns == Counter({(2, 0): 1, (3, 2): 9}), patterns
print('small connected support patterns:', sorted(patterns.items()))
print('intended negative (one-overlap alone admits 72 four-row patterns): removed by span argument')

# Positive realizability of the 3x3/8 shape with exact rational inner products.
q = Fraction
orthogonal = ((q(0), q(3, 5), q(4, 5)),
              (q(3, 5), q(16, 25), q(-12, 25)),
              (q(4, 5), q(-12, 25), q(9, 25)))
assert sum(x != 0 for row in orthogonal for x in row) == 8
assert all(sum(orthogonal[i][k] * orthogonal[j][k] for k in range(3)) == int(i == j)
           for i in range(3) for j in range(3))
print('positive rational orthogonal 3x3 eight-support example: yes')

# Negative: degree conditions/connectedness alone accept a 6-cycle, but a
# single row intersection excludes it by the elementary orthogonality rule.
cycle = ({0, 1}, {1, 2}, {0, 2})
assert connected(cycle, 3) and all(len(row) == 2 for row in cycle)
assert all(sum(c in row for row in cycle) == 2 for c in range(3))
assert all(len(cycle[r] & cycle[s]) == 1 for r, s in combinations(range(3), 2))
print('intended negative (one-overlap 6-cycle): rejected for one overlap')

# Recompute the activity inequality and the degree conclusion without inputs.
profiles = Counter()
for r in product((3, 4), repeat=4):
    lhs = 6 * sum(r) - sum(r[i] * r[j] for i, j in EDGES)
    profiles[tuple(sorted(r))] = lhs
    assert lhs > 9 or r.count(4) >= 3
assert dict(profiles) == {(3, 3, 3, 3): 18, (3, 3, 3, 4): 15,
                          (3, 3, 4, 4): 11, (3, 4, 4, 4): 6,
                          (4, 4, 4, 4): 0}
degrees = [d for d in product(range(2, 10), repeat=4) if sum(d) == 9]
assert len(degrees) == 4 and all(sorted(d) == [2, 2, 2, 3] for d in degrees)
assert all(any(d[i] == 2 for i in pair) for d in degrees for pair in combinations(range(4), 2))
assert 4 - len(tuple(combinations(range(4), 2))) == -2 <= 1 < 4
print('activity profile values:', sorted(profiles.items()))
print('intended negative (raw active-incidence sum exceeds words): caught by overlap correction')

# A merged party: binary split-party triangle, all eight edge signatures.
merged = Counter()
for bc, bd, cd in product((0, 1), repeat=3):
    triples = {(b, c, d) for b, c, d in product((0, 1), repeat=3)
               if (b ^ c) == bc or (b ^ d) == bd or (c ^ d) == cd}
    supports = [{(c, d) for b0, c, d in triples if b0 == b} for b in (0, 1)]
    if bc ^ bd ^ cd == 0:
        assert len(triples) == 8 and list(map(len, supports)) == [4, 4]
        merged['even_overload'] += 1
    else:
        assert len(triples) == 6 and list(map(len, supports)) == [3, 3]
        assert supports[0] != supports[1]
        merged['odd_mismatched_full_rows'] += 1
        # Intended negative: multiplicity cap ALONE does not reject this case.
        assert max(map(len, supports)) == 3
assert merged == Counter(even_overload=4, odd_mismatched_full_rows=4)
print('merged triangle cases:', dict(merged))
print('intended negative (odd triangle passes AB multiplicity-only check): detected by full-row support')

# Reconstruct switching/permutation orbits, then use direct core sets.
balanced = (0,) * 6
antibalanced = (1,) * 6
mixed = (0, 0, 0, 1, 0, 0)  # inequality BC, all other edges equal
orbits = {'balanced': orbit(balanced), 'antibalanced': orbit(antibalanced),
          'mixed': orbit(mixed)}
assert {name: len(values) for name, values in orbits.items()} == {
    'balanced': 8, 'antibalanced': 8, 'mixed': 48}
assert len(set.union(*orbits.values())) == 64
assert all(not (orbits[a] & orbits[b]) for a, b in combinations(orbits, 2))
print('switching/permutation orbit sizes:', {name: len(v) for name, v in orbits.items()})

concrete_mixed = core(mixed)
assert {(w[0], w[3]) for w in concrete_mixed if w[1:3] == (0, 1)} == set(product((0, 1), repeat=2))
checks = Counter()
for name, signatures in orbits.items():
    for e in sorted(signatures):
        forced = core(e)
        if name == 'mixed':
            overloaded = [(i, j, a, b, pair_count(forced, i, j, a, b))
                          for i, j in EDGES for a, b in product((0, 1), repeat=2)
                          if (a ^ b) == relation(e, i, j)
                          and pair_count(forced, i, j, a, b) > 3]
            assert overloaded and all(n == 4 for _, _, _, _, n in overloaded)
            checks['mixed_signatures_overload'] += 1
            continue

        constant = 0 if name == 'balanced' else 1
        switch = switch_to_constant(e, constant)
        normalized = {relabel(w, switch) for w in forced}
        expected = {w for w in WORDS if (sum(w) % 2 == 0 if constant == 0 else sum(w) == 2)}
        assert normalized == expected
        for i, j in EDGES:
            for a, b in product((0, 1), repeat=2):
                assert pair_count(forced, i, j, a, b) <= cap(e, i, j, a, b)
        checks[name + '_core_cap_ok'] += 1

        stars = {}
        uniforms = {}
        for i in range(4):
            for a in (0, 1):
                fiber = [w for w in forced if w[i] == a]
                unused = [w for w in WORDS if w[i] == a and w not in forced]
                ap = a ^ switch[i]
                uniform = relabel((ap,) * 4, switch)
                star = relabel(tuple(ap if k == i else 1 - ap for k in range(4)), switch)
                if name == 'balanced':
                    assert len(fiber) == 4
                    good = [w for w in unused if fiber_counts_ok(fiber + [w], e, i, a)]
                    assert not good
                    # Intended negative: permitting a repeated support word creates
                    # a fake completion, rejected specifically by set uniqueness.
                    assert uniform in forced and fiber_counts_ok(fiber + [uniform], e, i, a)
                    assert len(set(fiber + [uniform])) == 4
                    checks['balanced_no_completion_and_duplicate_negative'] += 1
                else:
                    assert len(fiber) == 3
                    good = [frozenset(extra) for extra in combinations(unused, 2)
                            if fiber_counts_ok(fiber + list(extra), e, i, a)]
                    assert good == [frozenset((uniform, star))]
                    one_low = forced | {uniform, star}
                    assert all(pair_count(one_low, x, y, c, d) <= cap(e, x, y, c, d)
                               for x, y in EDGES for c, d in product((0, 1), repeat=2))
                    checks['antibalanced_one_low_no_overload'] += 1
                    uniforms[i, a] = uniform
                    stars[i, a] = star
                    checks['antibalanced_unique_completion'] += 1
        if name == 'antibalanced':
            for i, j in EDGES:
                for a, b in product((0, 1), repeat=2):
                    points = forced | {uniforms[i, a], stars[i, a], uniforms[j, b], stars[j, b]}
                    ap, bp = a ^ switch[i], b ^ switch[j]
                    if ap != bp:
                        assert cap(e, i, j, a, b) == 3
                        assert pair_count(points, i, j, a, b) == 4
                        checks['antibalanced_opposite_bits_overload'] += 1
                    else:
                        k, l = [x for x in range(4) if x not in (i, j)]
                        c, d = (1 - ap) ^ switch[k], (1 - ap) ^ switch[l]
                        assert cap(e, k, l, c, d) == 2
                        assert pair_count(points, k, l, c, d) == 3
                        checks['antibalanced_same_bits_overload'] += 1

assert checks == Counter(mixed_signatures_overload=48,
                         balanced_core_cap_ok=8, antibalanced_core_cap_ok=8,
                         balanced_no_completion_and_duplicate_negative=64,
                         antibalanced_unique_completion=64,
                         antibalanced_one_low_no_overload=64,
                         antibalanced_opposite_bits_overload=96,
                         antibalanced_same_bits_overload=96), checks
print('forced-core and low-heavy exact controls:', dict(checks))
print('intended negatives: balanced/antibalanced cores and one antibalanced low fiber pass all caps;')
print('a duplicate would fake balanced completion; mixed-to-balanced loses overload')
print('all independent controls completed')
