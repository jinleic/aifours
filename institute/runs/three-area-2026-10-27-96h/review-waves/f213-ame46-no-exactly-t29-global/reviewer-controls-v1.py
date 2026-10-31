#!/usr/bin/env python3
"""Independent finite checks for the f213 review; no author code or files read."""
from collections import Counter
from itertools import combinations, product
from math import comb

EDGES = tuple(combinations(range(4), 2))
D = range(6)


def faults(p_words, e_words):
    out = {name: set() for name in ('duplicate-p', 'shared', 'missing', 'singleton-e')}
    e_counts = []
    for i, j in EDGES:
        pc = Counter((w[i], w[j]) for w in p_words)
        ec = Counter((w[i], w[j]) for w in e_words)
        for a, b in product(D, repeat=2):
            key = (i, j, a, b)
            p, e = pc[a, b], ec[a, b]
            if p > 1:
                out['duplicate-p'].add(key)
            if p and e:
                out['shared'].add(key)
            if not p and not e:
                out['missing'].add(key)
            if not p and e == 1:
                out['singleton-e'].add(key)
            if not p:
                e_counts.append(e)
    return out, e_counts


def degrees(p_words, e_words, i, a, j):
    m = sum(w[i] == a for w in p_words)
    d = len({w[j] for w in e_words if w[i] == a})
    return m, d


# A combinatorial support, not a quantum state: it obeys the pair-partition
# and residual multiplicity rules and intentionally contains distance-one E words.
p_words = {(0, 0, 0, 0)}
e_words = {w for w in product(D, repeat=4) if w.count(0) <= 1}
f, ec = faults(p_words, e_words)
assert not any(f.values()), f
assert len(e_words) == 1125 and min(ec) == 25 and max(ec) == 35
for i in range(4):
    for a in D:
        for j in range(4):
            if i != j:
                m, d = degrees(p_words, e_words, i, a, j)
                assert d == 6 - m and d >= 2, (i, a, j, m, d)
assert (1, 1, 1, 1) in e_words and (1, 1, 1, 2) in e_words
print('positive combinatorial support: P=1 E=1125 pair cells=216 E extensions=25..35; 72 degree identities; distance-one E pair present')

# Remove all extensions of exactly one pair cell. This causes one missing cell
# and makes the corresponding partner degrees unequal.
missing = {w for w in e_words if not (w[0] == 1 and w[1] == 1)}
f, _ = faults(p_words, missing)
assert f['missing'] == {(0, 1, 1, 1)} and not any(f[k] for k in f if k != 'missing'), f
assert degrees(p_words, missing, 0, 1, 1) == (0, 5)
assert degrees(p_words, missing, 0, 1, 2) == (0, 6)
print('negative missing-cell mutation: detected (0,1;1,1), partner degrees 5 vs 6')

# Add an E word in the already occupied P pair cell, without losing coverage.
shared = e_words | {(0, 0, 1, 1)}
f, _ = faults(p_words, shared)
assert f['shared'] == {(0, 1, 0, 0)} and not any(f[k] for k in f if k != 'shared'), f
assert degrees(p_words, shared, 0, 0, 1) == (1, 6)
assert degrees(p_words, shared, 0, 0, 2) == (1, 5)
print('negative shared-cell mutation: detected (0,1;0,0), partner degrees 6 vs 5')

# Keep one extension in an otherwise residual pair cell, preserving all pair cells.
fiber = {w for w in e_words if w[0] == 1 and w[1] == 1}
single = (e_words - fiber) | {min(fiber)}
f, _ = faults(p_words, single)
assert f['singleton-e'] == {(0, 1, 1, 1)} and not any(f[k] for k in f if k != 'singleton-e'), f
print('negative singleton mutation: detected exactly (0,1;1,1), without missing or shared cells')

# All ordered local degree lists with sum 7 and each degree in [2,6].
profiles = {s: [v for v in product(range(2, 7), repeat=s) if sum(v) == 7] for s in range(1, 7)}
shapes = [s for s in product(range(1, 7), repeat=4)
          if all(profiles[x] for x in s) and all(s[i] * s[j] >= 7 for i, j in EDGES)]
assert shapes == [(3, 3, 3, 3)]
assert profiles[3] == [(2, 2, 3), (2, 3, 2), (3, 2, 2)]
assert not profiles[4]
assert profiles[2] and 2 * 3 < 7
print('degree profiles: sizes 1..6 counts', [len(profiles[s]) for s in range(1, 7)], '; only capacity-compatible shape', shapes[0])
print('negative size controls: 4 symbols require at least 8 degrees; sizes 2 and 3 provide only 6 pair cells')

# Seven E cells in a 3x3 active pair: degree (2,2,3) on both sides.
pair_cells = tuple(product(range(3), repeat=2))
valid_sevens = []
for chosen in combinations(pair_cells, 7):
    r = tuple(sum(a == x for a, _ in chosen) for x in range(3))
    c = tuple(sum(b == y for _, b in chosen) for y in range(3))
    if r == (2, 2, 3) and c == (2, 2, 3):
        valid_sevens.append(tuple(sorted(set(pair_cells) - set(chosen))))
assert set(valid_sevens) == {((0, 0), (1, 1)), ((0, 1), (1, 0))}
bad_complement = {(0, 0), (0, 1)}
bad_chosen = set(pair_cells) - bad_complement
assert tuple(sum(a == x for a, _ in bad_chosen) for x in range(3)) == (1, 3, 3)
print('3x3 pair check: exactly 2 degree-compatible E patterns; negative two holes in one row gives degrees (1,3,3)')

# Exhaust all nonnegative activity multiplicities for exactly 29 P words.
N = 29
examined = active_match = target_match = relaxed_match = 0
example_relaxed = None
for c0 in range(N + 1):
    for c1 in range(N - c0 + 1):
        for c2 in range(N - c0 - c1 + 1):
            for c3 in range(N - c0 - c1 - c2 + 1):
                c4 = N - c0 - c1 - c2 - c3
                counts = (c0, c1, c2, c3, c4)
                examined += 1
                active = sum(k * counts[k] for k in range(5))
                pairs = sum(comb(k, 2) * counts[k] for k in range(5))
                if active == 44:
                    active_match += 1
                    if pairs == 12:
                        target_match += 1
                    if pairs == 15:
                        relaxed_match += 1
                        example_relaxed = counts
assert examined == comb(33, 4) and active_match > 0 and target_match == 0
assert relaxed_match > 0
assert (0, 14, 15, 0, 0) != (0, 0, 0, 0, 0)
control = (0, 14, 15, 0, 0)
assert sum(control) == 29 and sum(k * control[k] for k in range(5)) == 44
assert sum(comb(k, 2) * control[k] for k in range(5)) == 15
assert sum(comb(k, 2) * control[k] for k in range(5)) != 12
values = [k - comb(k, 2) for k in range(5)]
assert values == [0, 1, 1, 0, -2] and max(values) == 1
print('activity enumeration: counts=', examined, 'with active=44:', active_match,
      'also pairs=12:', target_match, 'also pairs=15:', relaxed_match)
print('intended-reason negative: counts (0,14,15,0,0) have active=44 but pairs=15, not 12')
print('positive relaxed activity example:', example_relaxed, '; k-C(k,2)=', values)
print('all reviewer controls completed')
