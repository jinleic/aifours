#!/usr/bin/env python3
"""Reviewer-owned finite checks; no author modules or data are imported."""
from collections import Counter
from itertools import combinations, product
from math import comb


def parity(x):
    return bin(x).count('1') & 1


def character(x, a):
    return -1 if parity(x & a) else 1


def wsum(atoms, signs, x):
    return sum(s * character(x, a) for a, s in zip(atoms, signs))


def is_affine_flat(points, dim):
    points = set(points)
    if len(points) != 1 << dim:
        return False
    origin = min(points)
    differences = {p ^ origin for p in points}
    return all(a ^ b in differences for a in differences for b in differences)


def block_class(block):
    weight = sum(abs(x) for x in block)
    values = tuple(abs(sum(block[z] * character(z, s) for z in range(4)))
                   for s in range(4))
    if weight == 0 and values == (0, 0, 0, 0):
        return 'O'
    if weight == 1 and values == (1, 1, 1, 1):
        return 'F'
    if weight == 2 and sorted(values) == [0, 0, 2, 2]:
        if values[0] == 2:
            return 'C' + str(next(s for s in range(1, 4) if values[s] == 2))
        return 'D' + str(next(s for s in range(1, 4) if values[s] == 0))
    if weight == 3 and sorted(values) == [1, 1, 1, 3]:
        return 'B' if values[0] == 3 else 'A' + str(values.index(3))
    if weight == 4 and values == (2, 2, 2, 2):
        return 'E'
    if weight == 4 and sorted(values) == [0, 0, 0, 4]:
        return 'H' if values[0] == 4 else 'G' + str(values.index(4))
    raise AssertionError((block, weight, values))


classes = Counter(block_class(b) for b in product((-1, 0, 1), repeat=4))
expected = {'O': 1, 'F': 8, 'E': 8, 'H': 2, 'B': 8}
expected.update({f'{p}{j}': {'A': 8, 'C': 4, 'D': 4, 'G': 2}[p]
                 for p in ('A', 'C', 'D', 'G') for j in (1, 2, 3)})
assert sum(classes.values()) == 81
assert classes == expected, (classes, expected)
assert block_class((0, 0, 0, 0)) != 'H'
print('block_classes', sorted(classes.items()), 'negative=zero_is_not_H')

four_hist = {}
for name, atoms in (('plane', (0, 1, 2, 3)), ('independent', (0, 1, 2, 4))):
    histograms = Counter()
    for signs in product((-1, 1), repeat=4):
        values = [abs(wsum(atoms, signs, c)) for c in range(64)]
        histogram = tuple(values.count(t) for t in (0, 2, 4))
        histograms[histogram] += 1
        if name == 'independent':
            ratios = [tuple(signs[j] * signs[0] * character(c, atoms[j])
                            for j in range(1, 4)) for c in range(64)]
            zero = {c for c, value in enumerate(values) if value == 0}
            flat = {c for c, ratio in enumerate(ratios) if ratio == (1, 1, 1)}
            hyperplane = {c for c, ratio in enumerate(ratios)
                          if ratio[0] * ratio[1] * ratio[2] == 1}
            assert is_affine_flat(flat, 3)
            assert is_affine_flat(hyperplane, 5)
            assert zero == hyperplane - flat
            assert not is_affine_flat(hyperplane - {min(hyperplane)}, 5)
    four_hist[name] = dict(histograms)
assert four_hist['plane'] == {(48, 0, 16): 8, (0, 64, 0): 8}
assert four_hist['independent'] == {(24, 32, 8): 16}
print('four_atom_histograms', four_hist, 'negative=damaged_hyperplane_rejected')

# Count sign patterns algebraically, then independently evaluate all transforms
# for one rank-six support with each possible even relation weight.
supports = {
    4: ((0, 1, 2, 3, 4, 8, 16, 32), (0, 1, 2, 3)),
    6: ((0, 1, 2, 4, 8, 16, 32, 31), (1, 2, 3, 4, 5, 7)),
    8: ((0, 1, 2, 4, 8, 16, 32, 63), tuple(range(8))),
}
eight_table = {}
for w, (atoms, relation) in supports.items():
    assert len(atoms) == len(set(atoms)) == 8
    assert len(relation) == w
    relation_xor = 0
    for j in relation:
        relation_xor ^= atoms[j]
    assert relation_xor == 0
    theoretical = []
    for syndrome in (0, 1):
        pattern_count = sum(comb(w, j) * comb(8 - w, k - j)
                            for k in (1, 4, 7)
                            for j in range(max(0, k - (8 - w)), min(w, k) + 1)
                            if j % 2 == syndrome)
        assert pattern_count % 2 == 0
        theoretical.append(pattern_count // 2)
    observed = {0: Counter(), 1: Counter()}
    for signs in product((-1, 1), repeat=8):
        syndrome = sum(signs[j] == -1 for j in relation) % 2
        count = sum(wsum(atoms, signs, c) % 3 == 0 for c in range(64))
        observed[syndrome][count] += 1
    assert observed == {0: Counter({theoretical[0]: 128}),
                        1: Counter({theoretical[1]: 128})}
    eight_table[w] = tuple(theoretical)
assert eight_table == {4: (23, 20), 6: (17, 26), 8: (35, 8)}
assert all(29 not in counts for counts in eight_table.values())
assert [(w, s) for w, counts in eight_table.items()
        for s, count in enumerate(counts) if count == 23] == [(4, 0)]
print('eight_atom_relation_counts', eight_table, 'negative=29_absent')

b0 = {u | (v << 2) for u in range(4) for v in range(16)
      if (u != 0 and bin(v).count('1') == 2)
      or (u == 0 and bin(v).count('1') in (1, 4))}
assert len(b0) == 23
coefficients = {mask: sum(character(mask, p) for p in b0)
                for mask in range(1, 64)}
assert max(abs(v) for v in coefficients.values()) == 15
assert [mask for mask, v in coefficients.items() if abs(v) == 15] == [60]
assert coefficients[60] == 15
hyperplanes = [(mask, bit, sum(parity(mask & p) == bit for p in b0))
               for mask in range(1, 64) for bit in (0, 1)]
assert max(n for _, _, n in hyperplanes) == 19
assert [(mask, bit) for mask, bit, n in hyperplanes if n == 19] == [(60, 0)]

# Encode H_* linearly as F_2^5, the even v coordinates being
# (a_0,a_1,a_2,a_0+a_1+a_2). Enumerate all 3-subspaces and cosets.
def in_hstar_to_six(p):
    u, a = p & 3, p >> 2
    v = a | (parity(a) << 3)
    return u | (v << 2)

subspaces = set()
for x, y, z in combinations(range(1, 32), 3):
    span = frozenset((0, x, y, z, x ^ y, x ^ z, y ^ z, x ^ y ^ z))
    if len(span) == 8:
        subspaces.add(span)
assert len(subspaces) == 155
intersection_histogram = Counter()
for subspace in subspaces:
    seen = set()
    for rep in range(32):
        if rep in seen:
            continue
        flat = {rep ^ x for x in subspace}
        seen.update(flat)
        intersection_histogram[sum(in_hstar_to_six(p) in b0 for p in flat)] += 1
    assert len(seen) == 32
assert sum(intersection_histogram.values()) == 620
assert 0 not in intersection_histogram
# Deliberate dimension negative: this two-flat really is disjoint.
two_flat = {0, 4, 8, 12}
assert is_affine_flat(two_flat, 2)
assert all(in_hstar_to_six(p) not in b0 for p in two_flat)
print('B0_hyperplane_max', 19, 'unique', (60, 0),
      'three_flat_intersections', sorted(intersection_histogram.items()),
      'negative=disjoint_two_flat_exists')

quadratic_zeros = Counter()
for radical_linear in range(64):
    for a, b in product((0, 1), repeat=2):
        z = sum((x * y ^ a * x ^ b * y ^ parity(radical_linear & r)) == 0
                for r in range(64) for x, y in product((0, 1), repeat=2))
        quadratic_zeros[z] += 1
assert quadratic_zeros == {64: 1, 128: 252, 192: 3}
max_energy = {z: 16 * (z - 8) + 36 * (256 - z)
              for z in quadratic_zeros}
assert max_energy == {64: 7808, 128: 6528, 192: 5248}
assert max_energy[128] < 64 * 116 and max_energy[192] < 64 * 116
assert max_energy[64] >= 64 * 116
print('rank2_zero_counts', dict(quadratic_zeros), 'energy_caps', max_energy,
      'negative=z64_not_excluded_by_cap')

raw_pairs = set()
residual = set()
for g in range(5):
    for h in range(5):
        c3, c2, d1, g2, o = 8 - 2*g - 2*h, 2 + 2*g - 2*h, 20 - 2*g + 2*h, 2, 16 + g + h
        if min(c3, c2, d1, g2, o) < 0:
            continue
        raw_pairs.add((g, h))
        counts = {'A1': 16, 'C2': c2, 'C3': c3, 'D1': d1,
                  'G2': g2, 'G3': g, 'H': h, 'O': o}
        assert sum(counts.values()) == 64
        assert 3*16 + 2*(c2+c3+d1) + 4*(g2+g+h) == 116
        assert 16 + 4*(c2+c3) + 16*h == 56
        assert 9*16 == 144
        assert 16 + 4*(c2+d1) + 16*g2 == 136
        assert 16 + 4*(c3+d1) + 16*g == 128
        if g != 3 and not (g == 1 and h != 0):
            residual.add((g, h))
expected_residual = {(0, 0), (0, 1), (1, 0), (2, 0), (2, 1), (2, 2), (4, 0)}
assert residual == expected_residual
assert (3, 0) in raw_pairs and (1, 1) in raw_pairs
assert (3, 0) not in residual and (1, 1) not in residual
print('class_count_raw_pairs', sorted(raw_pairs), 'residual', sorted(residual),
      'negative=forbidden_pairs_are_relaxation_only')

for k in (-7, -5, -3, -1, 1, 3, 5, 7):
    g = 1 if k % 4 == 1 else -1
    d = int(abs(k) in (1, 3))
    assert k*k == 35 - 2*k*g - 32*d
    assert k*k != 35 - 2*k*g - 16*d if d else True
qsign = [(-1 if ((x & 1) * ((x >> 1) & 1) ^ parity(x & 0b10110100)) else 1)
         for x in range(256)]
qwalsh = [sum(qsign[x] * character(x, a) for x in range(256)) for a in range(256)]
assert Counter(abs(x) for x in qwalsh) == {0: 252, 128: 4}
print('odd_sign_identity', 'all_8_values', 'rank2_quadratic_transform',
      {0: 252, 128: 4}, 'negative=wrong_D_coefficient_rejected')
print('ALL_EXACT_CONTROLS_COMPLETED')
