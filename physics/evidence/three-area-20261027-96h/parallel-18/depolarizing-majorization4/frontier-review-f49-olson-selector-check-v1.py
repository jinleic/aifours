#!/usr/bin/env python3
"""Independent exact finite checks of actual-word dihedral selectors.

No author checker or saved author result is imported. Finite experiments do not
prove the all-prime statements or the full ordered Olson conjecture.
"""

import itertools
import json
import random
from collections import Counter
from functools import lru_cache

SEED = 741492026
PRIMES = (3, 5, 7, 11)
TRIALS = 120


def multiply(p, a, b):
    return ((a[0] + b[0]) % 2, (a[1] + (-1 if a[0] else 1) * b[1]) % p)


def ordered_product(p, word, positions):
    value = (0, 0)
    for index in sorted(positions):
        value = multiply(p, value, word[index])
    return value


def random_word(p, rotations, rng):
    n = 4 * p - 1
    rot_positions = set(rng.sample(range(n), rotations))
    return [(0 if j in rot_positions else 1, rng.randrange(p)) for j in range(n)]


def potential_data(p, word, selected):
    I = set(selected)
    total = sum(word[k][1] for k in I) % p
    prefix = 0
    reflections = []
    for index, (kind, exponent) in enumerate(word):
        if kind == 0 and index in I:
            prefix = (prefix + exponent) % p
        elif kind == 1:
            reflections.append((index, (exponent + 2 * prefix) % p))
    return total, reflections


def check_crosscut(p, word, I):
    assert len(word) == 4 * p - 1 and len(I) == 2 * p - 2
    assert len(set(I)) == len(I) and all(word[k][0] == 0 for k in I)
    total, refs = potential_data(p, word, I)
    cuts = pairs = qualifying = 0
    for c in range(1, len(refs)):
        left, right = refs[:c], refs[c:]
        A, B = {x[1] for x in left}, {x[1] for x in right}
        predicted = sum(1 for _, za in left for _, zb in right if (zb - za) % p == total)
        actual = 0
        for (i, za), (j, zb) in itertools.product(left, right):
            result = ordered_product(p, word, list(I) + [i, j])
            assert result == (0, (total + za - zb) % p)
            actual += result == (0, 0)
            pairs += 1
        assert actual == predicted and actual >= len(A) + len(B) - p
        if len(A) + len(B) > p:
            assert actual >= 1
            qualifying += 1
        cuts += 1
    return cuts, pairs, qualifying


def gaps_and_pairs(word):
    gaps = [[]]
    refs = []
    for index, (kind, exponent) in enumerate(word):
        if kind == 1:
            refs.append(index)
            gaps.append([])
        else:
            gaps[-1].append((index, exponent))
    pairs = []
    for gap in gaps:
        classes = {}
        for index, exponent in gap:
            classes.setdefault(exponent, []).append(index)
        expected = min(len(gap) // 2, len(gap) - max((len(v) for v in classes.values()), default=0))
        start = len(pairs)
        while True:
            live = sorted(((len(v), exponent) for exponent, v in classes.items() if v), key=lambda x: (-x[0], x[1]))
            if len(live) < 2:
                break
            a = classes[live[0][1]].pop()
            b = classes[live[1][1]].pop()
            pairs.append((a, b))
        assert len(pairs) - start == expected
    return refs, pairs


def selected_from_pairs(p, word, refs, pairs, left, right):
    rotations = [i for i, x in enumerate(word) if x[0] == 0]
    chosen_pairs = pairs[:p - 1]
    paired_positions = {a for pair in chosen_pairs for a in pair}
    assert len(paired_positions) == 2 * (p - 1)
    outside = [i for i in rotations if i not in paired_positions]
    t = len(rotations) - (2 * p - 2)
    assert t >= p - 1 and len(outside) == t
    fixed = outside[:t - (p - 1)]
    sign = lambda k: -1 if left < k < right else 1
    fixed_sum = sum(sign(k) * word[k][1] for k in fixed) % p
    dp = {fixed_sum: ()}
    for a, b in chosen_pairs:
        assert sign(a) == sign(b) and word[a][1] != word[b][1]
        updated = {}
        for val, chosen in dp.items():
            for index in (a, b):
                updated.setdefault((val + sign(index) * word[index][1]) % p, chosen + (index,))
        dp = updated
    assert len(dp) == p
    target = (word[left][1] - word[right][1] + sum(sign(k) * word[k][1] for k in rotations)) % p
    omissions = set(fixed + list(dp[target]))
    assert len(omissions) == t
    kept = [k for k in rotations if k not in omissions] + [left, right]
    assert len(kept) == 2 * p and len(set(kept)) == 2 * p
    assert ordered_product(p, word, kept) == (0, 0)


@lru_cache(None)
def brute_matching(values):
    if len(values) < 2:
        return 0
    best = brute_matching(values[1:])
    for j in range(1, len(values)):
        if values[j] != values[0]:
            best = max(best, 1 + brute_matching(values[1:j] + values[j + 1:]))
    return best


def matching_checks():
    checked = 0
    for alphabet in (3, 5):
        for n in range(10):
            for values in itertools.combinations_with_replacement(range(alphabet), n):
                counts = Counter(values)
                formula = min(n // 2, n - max(counts.values(), default=0))
                assert brute_matching(values) == formula
                checked += 1
    return checked


def separated_pairs(types):
    n = len(types)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1]
        for j in range(i + 1, n):
            if types[i] == types[j]:
                dp[i] = max(dp[i], 1 + dp[j + 1])
    return dp[0]


def sharpness_checks():
    checked = 0
    for p in (3, 5, 7):
        universe = set(range(p))
        for mask in range(1, (1 << p) - 1):
            A = {j for j in range(p) if mask & (1 << j)}
            for delta in range(p):
                B = {(delta + j) % p for j in universe - A}
                left = sorted(A) + [min(A)] * (p + 1)
                right = sorted(B)
                assert len(left) + len(right) == 2 * p + 1
                word = [(1, x) for x in left + right] + [(0, delta)] + [(0, 0)] * (2 * p - 3)
                I = [i for i, item in enumerate(word) if item[0] == 0]
                total, refs = potential_data(p, word, I)
                assert total == delta and len(word) == 4 * p - 1
                assert all(ordered_product(p, word, I + [a[0], b[0]]) != (0, 0) for a in refs[:len(left)] for b in refs[len(left):])
                checked += 1
    return checked


def family_checks():
    cross = []
    for p in (3, 5, 7, 11, 13):
        h = (p - 1) // 2
        one_side = [j % (h + 1) for j in range(p)]
        values = one_side + one_side
        word = []
        for j in range(2 * p):
            exponent = (values[j] - 2 * min(j, 2 * p - 2)) % p
            word.append((1, exponent))
            if j < 2 * p - 1:
                word.append((0, 1))
        I = [i for i, item in enumerate(word) if item[0] == 0][:2 * p - 2]
        total, refs = potential_data(p, word, I)
        assert len(word) == 4 * p - 1 and total == (-2) % p
        assert {z for _, z in refs[:p]} == set(range(h + 1))
        assert {z for _, z in refs[p:]} == set(range(h + 1))
        assert separated_pairs([kind for kind, _ in word]) < 2 * p - 1
        i = next(i for i, z in refs[:p] if z == (0 if p == 3 else 2))
        j = next(i for i, z in refs[p:] if z == (1 if p == 3 else 0))
        assert ordered_product(p, word, I + [i, j]) == (0, 0)
        cross.append(p)
    gap = []
    for p in (5, 7, 11, 13):
        word = [(0, x) for _ in range(p - 1) for x in (1, 2)]
        word += [item for _ in range(p - 1) for item in ((1, 0), (0, 1))]
        word += [(1, 0)] * 3
        assert len(word) == 4 * p - 1
        assert separated_pairs([kind for kind, _ in word]) < 2 * p - 1
        refs, pairs = gaps_and_pairs(word)
        assert len(pairs) >= p - 1
        I = list(range(2 * p - 2))
        S, potentials = potential_data(p, word, I)
        assert S == (-3) % p != 0 and len({v for _, v in potentials}) == 1
        picked = [2 * k + (1 if k < 2 else 0) for k in range(p - 1)]
        picked += [2 * (p - 1) + 2 * k + 1 for k in range(p - 1)]
        picked += [4 * (p - 1), 4 * (p - 1) + 1]
        assert len(set(picked)) == 2 * p and ordered_product(p, word, picked) == (0, 0)
        for i, j in itertools.combinations(refs, 2):
            selected_from_pairs(p, word, refs, pairs, i, j)
        gap.append(p)
    return cross, gap


def main():
    rng = random.Random(SEED)
    cross_words = cross_cuts = cross_pairs = qualifying = 0
    gap_words = eligible_words = reflection_pairs = 0
    for p in PRIMES:
        for _ in range(TRIALS):
            R = rng.randrange(2 * p - 2, 3 * p - 1)
            word = random_word(p, R, rng)
            rotations = [i for i, entry in enumerate(word) if entry[0] == 0]
            I = sorted(rng.sample(rotations, 2 * p - 2))
            cuts, pairs, good = check_crosscut(p, word, I)
            cross_words += 1
            cross_cuts += cuts
            cross_pairs += pairs
            qualifying += good
        for _ in range(TRIALS):
            R = rng.randrange(3 * p - 3, 4 * p - 2)
            word = random_word(p, R, rng)
            refs, pairs = gaps_and_pairs(word)
            assert len(refs) >= 2
            gap_words += 1
            if len(pairs) >= p - 1:
                eligible_words += 1
                for i, j in itertools.combinations(refs, 2):
                    selected_from_pairs(p, word, refs, pairs, i, j)
                    reflection_pairs += 1
    matching = matching_checks()
    sharp = sharpness_checks()
    cross_family, gap_family = family_checks()
    control_word = [(0, 1), (1, 0), (0, 1), (1, 0), (0, 0), (0, 0)] + [(1, 0)] * 5
    control_I = [0, 2, 4, 5]
    assert len(control_word) == 11 and ordered_product(3, control_word, control_I + [1, 3]) == (0, 0)
    naive_unsigned = sum(control_word[i][1] for i in control_I) % 3
    assert naive_unsigned != 0
    print(json.dumps({"scope": "finite independent exact actual-word checks; not all-prime proof or author-result replay", "seed": SEED, "crosscut_random_words": cross_words, "crosscut_checked_cuts": cross_cuts, "crosscut_checked_ordered_products_with_cut_multiplicity": cross_pairs, "crosscut_qualifying_cuts": qualifying, "gap_random_words": gap_words, "gap_eligible_words": eligible_words, "gap_fixed_reflection_pairs_constructively_solved": reflection_pairs, "brute_gap_multisets": matching, "sharpness_actual_words": sharp, "crosscut_family_primes": cross_family, "same_gap_family_primes": gap_family, "control_rejected": "unsigned-rotation product on interleaved selected reflections", "control_direct_product": "identity", "control_naive_unsigned_rotation_exponent": naive_unsigned}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
