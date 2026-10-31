#!/usr/bin/env python3
"""Bounded original-word diagnostics for the frozen f66 proof; not a universal proof."""
import hashlib
import itertools
import json
import random
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / 'manifest-v1.json'
MANIFEST_SHA = '0be83969f645bde8b4fb27e5b02be797d2f0b572db4ee31ec03258b1685dab71'
SEED = 0x66362D444948


class Failure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise Failure(reason)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pin_inputs():
    raw = MANIFEST.read_bytes()
    require(digest(raw) == MANIFEST_SHA, 'MANIFEST_SHA')
    manifest = json.loads(raw)
    require(len(manifest['inputs_in_read_order']) == 2, 'INPUT_COUNT')
    pins = []
    for item in manifest['inputs_in_read_order']:
        data = Path(item['path']).read_bytes()
        require(digest(data) == item['sha256'], 'SOURCE_SHA')
        require(len(data) == item['bytes'] and data.count(b'\n') == item['LF'], 'SOURCE_SIZE')
        pins.append({'path': item['path'], 'sha256': digest(data),
                     'bytes': len(data), 'LF': data.count(b'\n')})
    return pins


def band(p, word):
    require(p >= 3 and p % 2 and all(p % d for d in range(2, int(p ** .5) + 1)), 'ODD_PRIME')
    require(len(word) == 4 * p - 1, 'WORD_LENGTH')
    require(all(t in (0, 1) and 0 <= x < p for t, x in word), 'WORD_SYMBOL')
    require(sum(t == 0 for t, _ in word) == 3 * p - 3, 'ROTATION_COUNT')
    require(sum(t == 1 for t, _ in word) == p + 2, 'REFLECTION_COUNT')


def product(p, word, indices):
    exp = parity = 0
    for i in indices:
        t, x = word[i]
        exp = (exp + (-x if parity else x)) % p
        parity ^= t
    return exp, parity


def validate(p, word, indices):
    band(p, word)
    require(len(indices) == 2 * p, 'SELECTOR_LENGTH')
    require(all(isinstance(i, int) and 0 <= i < len(word) for i in indices), 'INDEX_RANGE')
    require(len(set(indices)) == len(indices), 'DUPLICATE_INDEX')
    require(all(i < j for i, j in zip(indices, indices[1:])), 'INDEX_ORDER')
    exp, parity = product(p, word, indices)
    require(parity == 0, 'ODD_REFLECTION_PARITY')
    require(exp == 0, 'NONIDENTITY_PRODUCT')


def rotate_bits(bits, shift, p):
    shift %= p
    mask = (1 << p) - 1
    return ((bits << shift) | (bits >> (p - shift))) & mask


def dp_witness(p, word):
    """Bitset reachability in original order, then backtrack and multiply independently."""
    band(p, word)
    length = 2 * p
    state = [[0, 0] for _ in range(length + 1)]
    state[0][0] = 1
    history = [tuple(tuple(row) for row in state)]
    for i, (kind, x) in enumerate(word):
        for n in range(min(i + 1, length), 0, -1):
            for old_parity in (0, 1):
                shift = x if old_parity == 0 else -x
                state[n][old_parity ^ kind] |= rotate_bits(state[n - 1][old_parity], shift, p)
        history.append(tuple(tuple(row) for row in state))
    require(state[length][0] & 1, 'DP_NO_SELECTOR')
    chosen = []
    n, parity, exp = length, 0, 0
    for i in range(len(word) - 1, -1, -1):
        previous = history[i]
        if previous[n][parity] & (1 << exp):
            continue
        kind, x = word[i]
        old_parity = parity ^ kind
        old_exp = (exp - (x if old_parity == 0 else -x)) % p
        require(n > 0 and previous[n - 1][old_parity] & (1 << old_exp), 'DP_BACKTRACK')
        chosen.append(i)
        n, parity, exp = n - 1, old_parity, old_exp
    require((n, parity, exp) == (0, 0, 0), 'DP_INITIAL_STATE')
    chosen.reverse()
    validate(p, word, chosen)
    return chosen


def signed_pair_witness(p, word, left, right):
    """Apply the unequal-pair omitted-occurrence construction to actual rotation indices."""
    require(left < right and word[left][0] == word[right][0] == 1, 'PAIR_INDICES')
    signed = {i: (x if not left < i < right else -x) % p
              for i, (kind, x) in enumerate(word) if kind == 0}
    piles = {}
    for i, value in signed.items():
        piles.setdefault(value, []).append(i)
    if max(map(len, piles.values())) > 2 * p - 2:
        return None
    pairs = []
    for _ in range(p - 1):
        leaders = sorted((len(v), k) for k, v in piles.items() if v)
        require(len(leaders) >= 2, 'GREEDY_PAIR_SHORTAGE')
        _, v = leaders[-1]
        _, u = leaders[-2]
        pairs.append((piles[v].pop(), piles[u].pop()))
    sums = {0: ()}
    for x, y in pairs:
        newer = {}
        for value, previous in sums.items():
            for index in (x, y):
                newer.setdefault((value + signed[index]) % p, previous + (index,))
        sums = newer
    require(len(sums) == p, 'UNEQUAL_PAIR_SUPPORT')
    target = (sum(signed.values()) + word[left][1] - word[right][1]) % p
    omitted = set(sums[target])
    require(len(omitted) == p - 1, 'OMISSION_DISTINCTNESS')
    indices = sorted([left, right] + [i for i in signed if i not in omitted])
    validate(p, word, indices)
    return indices


def make_word(p, a, gaps, labels):
    word = [(1, labels[0])]
    for gap, y in zip(gaps, labels[1:]):
        word.extend((0, x) for x in gap)
        word.append((1, y))
    return word


def structural_data(p, a, word):
    """Validate only the final saturated, endpoint-inside construction's hypotheses."""
    band(p, word)
    refs = [i for i, (t, _) in enumerate(word) if t]
    require(all(x in (a, (-a) % p) for t, x in word if not t), 'ROTATION_VALUES')
    require(sum(t == 0 and x == a for t, x in word) == 2 * p - 1, 'CORE_COUNT')
    require(not any(t == 0 and x == (-a) % p for t, x in word[:refs[0]] + word[refs[-1] + 1:]), 'OUTSIDE_EXTRA')
    require(refs[0] == 0 and refs[-1] == len(word) - 1, 'OUTSIDE_CORE')
    gaps = [word[x + 1:y] for x, y in zip(refs, refs[1:])]
    empty = [j for j, gap in enumerate(gaps) if not gap]
    require(len(empty) == 2, 'ADJACENT_BOUNDARY_COUNT')
    require(empty[1] == empty[0] + 1, 'ADJACENT_BOUNDARY_OVERLAP')
    triple = refs[empty[0]:empty[0] + 3]
    require(len({word[i][1] for i in triple}) == 1, 'UNEQUAL_TRIPLE')
    counts = [(sum(x == a for _, x in gap), sum(x == (-a) % p for _, x in gap)) for gap in gaps]
    big = [j for j, (c, _) in enumerate(counts) if c >= p + 1]
    require(len(big) == 1, 'NO_UNIQUE_LARGE_GAP')
    require(counts[big[0]][1] == 0, 'LARGE_GAP_EXTRA')
    for j, (c, k) in enumerate(counts):
        if j != big[0] and j not in empty:
            require(k == 1 and c <= k, 'SMALL_GAP_SATURATION')
    prefixes = [sum(t == 0 and x == a for t, x in word[:i]) for i in refs]
    g = len(set(prefixes))
    A = len(empty)
    require(sum(c == 0 for c, _ in counts) == len(refs) - g, 'ZERO_CORE_GAP_COUNT')
    require((len(refs) - g - A) + (g - 2) == p - 2, 'SATURATION_COUNT')
    return refs, triple, counts, big[0]


def endpoint_witness(p, a, word):
    refs, triple, counts, big = structural_data(p, a, word)
    first, last = refs[0], refs[-1]
    plus, minus = [], []
    for i, (kind, x) in enumerate(word):
        if kind == 0:
            signed = (x if not first < i < last else -x) % p
            if signed == a:
                plus.append(i)
            elif signed == (-a) % p:
                minus.append(i)
            else:
                raise Failure('ENDPOINT_SIGN')
    require(len(plus) == p - 2 and len(minus) == 2 * p - 1, 'ENDPOINT_MULTIPLICITIES')
    difference = (word[last][1] - word[first][1]) % p
    if difference:
        choices = [t for t in range(p - 1) if (2 * (t + 1) * a) % p == difference]
        require(len(choices) == 1, 'ENDPOINT_NONZERO_COVERAGE')
        t = choices[0]
        selected = [first, last] + plus[:t] + minus[:2 * p - 2 - t]
        branch = 'unequal_endpoints_two_reflections'
    else:
        insert = [i for i in triple if i not in (first, last)][:2]
        require(len(insert) == 2, 'TRIPLE_ENDPOINT_OVERLAP')
        selected = [first, last] + insert + plus[:p - 2] + minus[:p - 2]
        branch = 'equal_endpoints_four_reflections'
    selected.sort()
    validate(p, word, selected)
    return branch, triple, counts, big


def expect(reason, fn):
    try:
        fn()
    except Failure as error:
        require(str(error) == reason, 'CONTROL_WRONG_REASON:' + reason + ':' + str(error))
        return reason
    raise Failure('CONTROL_NOT_REJECTED:' + reason)


def controls():
    p = 5
    original = [(0, 1), (1, 0), (0, 1), (1, 0)] + [(0, 0)] * 10 + [(1, 0)] * 5
    indices = list(range(10))
    validate(p, original, indices)
    duplicate = indices[:-1] + [8]
    unordered = [1, 0] + indices[2:]
    out_of_range = indices[:-1] + [len(original)]
    commuted = original.copy()
    commuted[1], commuted[2] = commuted[2], commuted[1]
    odd = original.copy()
    odd[1], odd[10] = odd[10], odd[1]
    results = [
        expect('SELECTOR_LENGTH', lambda: validate(p, original, indices[:-1])),
        expect('DUPLICATE_INDEX', lambda: validate(p, original, duplicate)),
        expect('INDEX_ORDER', lambda: validate(p, original, unordered)),
        expect('INDEX_RANGE', lambda: validate(p, original, out_of_range)),
        expect('NONIDENTITY_PRODUCT', lambda: validate(p, commuted, indices)),
        expect('ODD_REFLECTION_PARITY', lambda: validate(p, odd, indices)),
    ]
    require(product(p, original, indices) == (0, 0), 'POSITIVE_CONTROL')
    require(product(p, commuted, indices) == (2, 0), 'ORDER_COUNTEREXAMPLE')

    # f63 correction: four equal reflections do not force every selector to use four.
    f63 = [(0, 1)] * 5 + [(1, 0)] * 4 + [(0, 2), (1, 1)]
    f63_indices = [0, 1, 2, 3, 5, 10]
    validate(3, f63, f63_indices)
    require(sum(f63[i][0] for i in f63_indices) == 2, 'F63_TWO_REFLECTIONS')

    # Consecutive differences 1,1 do not force first-to-third difference 1;
    # the first/third pair skips a reflection but no rotation, and it actually succeeds.
    triple_word = [(0, 1)] * 9 + [(1, 0), (1, 1), (1, 2)] + [(0, 3)] * 3 + [(1, 0)] * 4
    triple_indices = list(range(6)) + [9, 11, 12, 13]
    validate(5, triple_word, triple_indices)
    require((triple_word[10][1] - triple_word[9][1]) % 5 == 1 and
            (triple_word[11][1] - triple_word[10][1]) % 5 == 1 and
            (triple_word[11][1] - triple_word[9][1]) % 5 == 2, 'TRIPLE_DIFFERENCES')
    require(all(t == 1 for t, _ in triple_word[10:11]), 'TRIPLE_INTERVENING_ROTATION')

    # Saturation-specific mutation controls: a=1, p=5, two adjacent empty gaps.
    gaps = [[], [], [1] * 6, [1, 4], [1, 4], [1, 4]]
    labels = [0] * 7
    baseline = make_word(5, 1, gaps, labels)
    structural_data(5, 1, baseline)
    unequal_labels = labels.copy()
    unequal_labels[1] = 1
    results.append(expect('UNEQUAL_TRIPLE', lambda: structural_data(5, 1, make_word(5, 1, gaps, unequal_labels))))
    outside = baseline.copy()
    extra_at = next(i for i, (t, x) in enumerate(outside) if t == 0 and x == 4)
    extra = outside.pop(extra_at)
    outside.insert(0, extra)
    results.append(expect('OUTSIDE_EXTRA', lambda: structural_data(5, 1, outside)))
    no_large = [g.copy() for g in gaps]
    no_large[2].pop()
    no_large[3].insert(0, 1)
    results.append(expect('NO_UNIQUE_LARGE_GAP', lambda: structural_data(5, 1, make_word(5, 1, no_large, labels))))
    big_extra = [g.copy() for g in gaps]
    big_extra[3].remove(4)
    big_extra[2].append(4)
    results.append(expect('LARGE_GAP_EXTRA', lambda: structural_data(5, 1, make_word(5, 1, big_extra, labels))))
    return {'intended_rejections': results, 'positive_ordered_product': [0, 0],
            'commuted_product': [2, 0], 'f63_original_one_based_indices': [i + 1 for i in f63_indices],
            'first_third_original_one_based_indices': [i + 1 for i in triple_indices]}


def subset_lemma():
    counts = {}
    for p in (3, 5, 7):
        total = zsf = missing = 0
        for values in itertools.product(range(1, p), repeat=p - 2):
            total += 1
            nonempty_sums = set()
            for mask in range(1, 1 << len(values)):
                nonempty_sums.add(sum(values[i] for i in range(len(values)) if mask & (1 << i)) % p)
            if 0 in nonempty_sums:
                continue
            zsf += 1
            sums = nonempty_sums | {0}
            require(len(sums) >= p - 1, 'SUBSET_SUM_LOWER_BOUND')
            if len(sums) == p - 1:
                missing += 1
                m = next(iter(set(range(p)) - sums))
                require(all(value == (-m) % p for value in values), 'MISSING_SUM_LEMMA')
        counts[str(p)] = {'tuples': total, 'zero_sum_free': zsf, 'missing_one': missing}
    # If n is only p-3, the exact classification can fail.
    short_counterexample = None
    for values in itertools.product(range(1, 5), repeat=2):
        subset = {0, values[0], values[1], sum(values) % 5}
        if 0 not in {values[0], values[1], sum(values) % 5} and len(subset) == 4:
            m = next(iter(set(range(5)) - subset))
            if any(d != (-m) % 5 for d in values):
                short_counterexample = {'p': 5, 'n': 2, 'values': list(values),
                                        'subset_sums': sorted(subset), 'missing': m}
                break
    require(short_counterexample is not None, 'SHORT_LENGTH_COUNTEREXAMPLE')
    composite_sums = {sum(3 for i in range(8) if mask & (1 << i)) % 9 for mask in range(1 << 8)}
    require(composite_sums == {0, 3, 6}, 'COMPOSITE_COUNTEREXAMPLE')
    return {'exhaustion': counts, 'short_length_counterexample': short_counterexample,
            'composite_nonzero_swap_support_mod_9': sorted(composite_sums)}


def structured_cases(rng):
    cases = Counter()
    boundaries = Counter()

    def examine(p, a, gaps, labels):
        word = make_word(p, a, gaps, labels)
        branch, triple, counts, big = endpoint_witness(p, a, word)
        dp_witness(p, word)
        refs = [i for i, (t, _) in enumerate(word) if t]
        location = 'left' if triple[0] == refs[0] else 'right' if triple[-1] == refs[-1] else 'interior'
        cases[f'p{p}:{location}:{branch}'] += 1
        if counts[big][0] == p + 1:
            boundaries[f'p{p}:large_c_equals_p_plus_1'] += 1
        if any(c == k == 1 for c, k in counts):
            boundaries[f'p{p}:small_c_equals_k_equals_1'] += 1

    # Exhaust every saturated p=3 actual word for both core signs and all triple-compatible labels.
    p = 3
    for a in (1, 2):
        for start in range(p):
            nonempty = [j for j in range(p + 1) if j not in (start, start + 1)]
            for big in nonempty:
                small = next(j for j in nonempty if j != big)
                for core_in_small, order in ((0, 0), (1, 0), (1, 1)):
                    gaps = [[] for _ in range(p + 1)]
                    gaps[big] = [a] * (2 * p - 1 - core_in_small)
                    gaps[small] = [(-a) % p] if not core_in_small else ([a, (-a) % p] if not order else [(-a) % p, a])
                    for labels in itertools.product(range(p), repeat=p + 2):
                        if labels[start] == labels[start + 1] == labels[start + 2]:
                            examine(p, a, gaps, labels)

    # Systematic triple locations and equal/unequal endpoints, with reproducible random placements.
    for p in (5, 7, 11):
        for start in range(p):
            for rep in range(40):
                a = rng.randrange(1, p)
                available = [j for j in range(p + 1) if j not in (start, start + 1)]
                big = rng.choice(available)
                small = [j for j in available if j != big]
                big_count = (p + 1 if rep % 4 == 0 else 2 * p - 1 if rep % 4 == 1
                             else rng.randint(p + 1, 2 * p - 1))
                active = set(rng.sample(small, 2 * p - 1 - big_count))
                gaps = [[] for _ in range(p + 1)]
                gaps[big] = [a] * big_count
                for j in small:
                    gaps[j] = [(-a) % p]
                    if j in active:
                        gaps[j].insert(rng.randrange(2), a)
                labels = [rng.randrange(p) for _ in range(p + 2)]
                for j in range(start, start + 3):
                    labels[j] = labels[start]
                outside_endpoint = 0 if start == p - 1 else p + 1
                other_endpoint = p + 1 if outside_endpoint == 0 else 0
                labels[outside_endpoint] = (labels[other_endpoint] + (0 if rep % 2 == 0 else rng.randrange(1, p))) % p
                examine(p, a, gaps, labels)
    require(sum(v for k, v in cases.items() if k.startswith('p3:')) == 972, 'P3_COVERAGE_COUNT')
    for p in (3, 5, 7, 11):
        for location in ('left', 'interior', 'right'):
            for branch in ('equal_endpoints_four_reflections', 'unequal_endpoints_two_reflections'):
                require(cases[f'p{p}:{location}:{branch}'] > 0, 'MISSING_ENDPOINT_CASE')
        require(boundaries[f'p{p}:large_c_equals_p_plus_1'] > 0, 'LARGE_BOUNDARY_UNTESTED')
        require(boundaries[f'p{p}:small_c_equals_k_equals_1'] > 0, 'SMALL_BOUNDARY_UNTESTED')
    return {'cases': dict(sorted(cases.items())), 'boundary_equalities': dict(sorted(boundaries.items())),
            'total_actual_words': sum(cases.values()),
            'method': 'p=3 exhaustive within saturated final core/triple hypotheses; p=5,7,11 seeded samples'}


def general_words(rng):
    totals = Counter()
    example_majorities = {}
    for p in (3, 5, 7, 11):
        for sample in range(24):
            word = [(0, rng.randrange(p)) for _ in range(3 * p - 3)] + [(1, rng.randrange(p)) for _ in range(p + 2)]
            rng.shuffle(word)
            dp_witness(p, word)
            refs = [i for i, (t, _) in enumerate(word) if t]
            rotations = [i for i, (t, _) in enumerate(word) if not t]
            totals[f'p{p}:words'] += 1
            for left, right in itertools.combinations(refs, 2):
                chosen = rng.sample(rotations, 2 * p - 2)
                actual = sorted(chosen + [left, right])
                exp, parity = product(p, word, actual)
                predicted = (word[left][1] - word[right][1] +
                             sum(word[i][1] * (-1 if left < i < right else 1) for i in chosen)) % p
                require(parity == 0 and exp == predicted, 'ORIGINAL_INDEX_SIGN_FORMULA')
                totals[f'p{p}:pair_sign_checks'] += 1
                witness = signed_pair_witness(p, word, left, right)
                if witness is None:
                    totals[f'p{p}:above_pair_threshold'] += 1
                    example_majorities.setdefault(str(p), {'word': word, 'reflection_pair': [left, right]})
                else:
                    totals[f'p{p}:unequal_pair_witnesses'] += 1
    return {'totals': dict(sorted(totals.items())),
            'above_threshold_pair_examples': {p: data for p, data in sorted(example_majorities.items())},
            'method': '24 independently generated unrestricted band words per prime; all actual reflection pairs'}


def main():
    pins = pin_inputs()
    rng = random.Random(SEED)
    control_result = controls()
    subset_result = subset_lemma()
    structured_result = structured_cases(rng)
    general_result = general_words(rng)
    clock = subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], check=True,
                           capture_output=True, text=True).stdout.strip()
    receipt = {'status': 'PASS_BOUNDED_CONTROLS_NOT_A_UNIVERSAL_PROOF',
               'observed_clock_before_receipt_write': clock, 'manifest_sha256': MANIFEST_SHA,
               'inputs_in_order': pins, 'checker_sha256': digest(Path(__file__).read_bytes()),
               'seed': SEED, 'controls': control_result, 'subset_sum_lemma': subset_result,
               'structured_endpoint_words': structured_result, 'unrestricted_random_words': general_result,
               'limits': 'Finite diagnostic only; no human, cross-model, kernel, novelty or other-band conclusion.'}
    with (ROOT / 'checker-receipt-v1.json').open('x', encoding='utf-8') as output:
        json.dump(receipt, output, indent=2, sort_keys=True)
        output.write('\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
