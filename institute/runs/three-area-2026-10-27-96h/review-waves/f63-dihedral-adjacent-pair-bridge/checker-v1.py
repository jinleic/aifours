#!/usr/bin/env python3
"""Independent, bounded original-order check for the f63 review; stdlib only."""
from collections import Counter
from hashlib import sha256
from heapq import heappop, heappush
from itertools import combinations, product
from pathlib import Path
from random import Random
import json
import subprocess

HERE = Path(__file__).resolve().parent
INPUTS = (
    (Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-core-and-four-reflections-v1.md'), '5e7f65b8764d4f52ccddadd9ea2934d0635ca5c2085a3c41e520b336a93c767f'),
    (Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-dihedral-two-adjacent-pairs-v1.md'), 'fc4b420c2d4f66b2be06640dec5a161567fa35c4024e626653c15d8f29e8e363'),
)


class CheckFailure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def original_product(p, word, indices):
    # Elements are (rotation exponent, reflection parity). Multiply in input order.
    x = parity = 0
    for index in indices:
        y, flip = word[index]
        x = (x + (y if parity == 0 else -y)) % p
        parity ^= flip
    return x, parity


def check_witness(p, word, indices):
    require(len(indices) == 2 * p, 'SELECTION_COUNT')
    require(all(0 <= i < len(word) for i in indices), 'INDEX_RANGE')
    require(all(i < j for i, j in zip(indices, indices[1:])), 'INDEX_ORDER_OR_DUPLICATE')
    x, parity = original_product(p, word, indices)
    require(parity == 0, 'REFLECTION_PARITY')
    require(x == 0, 'NONZERO_EXPONENT')


def expect_failure(expected, fn):
    try:
        fn()
    except CheckFailure as exc:
        require(str(exc) == expected, 'WRONG_CONTROL_REASON: ' + str(exc))
        return expected
    raise CheckFailure('CONTROL_UNEXPECTEDLY_ACCEPTED: ' + expected)


def subset_lemma():
    result = {}
    for p in (3, 5, 7):
        tested = zsf = one_missing = full = 0
        for seq in product(range(1, p), repeat=p - 2):
            tested += 1
            sums = {0}
            good = True
            for d in seq:
                if (-d) % p in sums:
                    good = False
                    break
                sums |= {(s + d) % p for s in sums}
            if not good:
                continue
            zsf += 1
            require(len(sums) >= p - 1, 'SUBSET_GROWTH')
            if len(sums) == p:
                full += 1
                continue
            one_missing += 1
            missing = (set(range(p)) - sums).pop()
            require(all(d == (-missing) % p for d in seq), 'EQUALITY_LEMMA')
            # Independently check all the omitted-index sets used in the proof.
            for i, d in enumerate(seq):
                other = {0}
                for j, e in enumerate(seq):
                    if j != i:
                        other |= {(s + e) % p for s in other}
                require(len(other) == p - 2, 'OMITTED_SET_SIZE')
                require(set(range(p)) - other == {missing, (missing - d) % p}, 'OMITTED_SET_COMPLEMENT')
                require((-d) % p not in other, 'ZERO_SUM_FREE_OMITTED_SET')
        result[str(p)] = {'tuples': tested, 'zero_sum_free': zsf,
                          'one_missing': one_missing, 'full_subset_sum': full}
    return result


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(total - first, parts - 1):
            yield (first,) + rest


def pairing_multiplicity_check():
    result = {}
    for p in (3, 5, 7):
        all_counts = qualifying = 0
        for counts in compositions(3 * p - 3, p):
            all_counts += 1
            if max(counts) > 2 * p - 2:
                continue
            qualifying += 1
            remaining = list(counts)
            reachable = {0}
            for step in range(p - 1):
                order = sorted(range(p), key=lambda v: remaining[v], reverse=True)
                a, b = order[:2]
                require(remaining[b] > 0 and a != b, 'UNEQUAL_PAIR_UNAVAILABLE')
                remaining[a] -= 1
                remaining[b] -= 1
                reachable |= {(s + a - b) % p for s in reachable}
                require(len(reachable) >= min(p, step + 2), 'PAIR_SWAP_GROWTH')
            require(reachable == set(range(p)), 'PAIR_SWAP_NOT_FULL')
        result[str(p)] = {'multiplicity_vectors': all_counts, 'qualifying_vectors': qualifying}
    return result


def signed_pair_witness(p, word, i, j):
    rotations = [k for k, (_, parity) in enumerate(word) if parity == 0]
    signed = {k: ((-word[k][0]) if i < k < j else word[k][0]) % p for k in rotations}
    buckets = [[] for _ in range(p)]
    for k in rotations:
        buckets[signed[k]].append(k)
    maximum = max(map(len, buckets))
    if maximum > 2 * p - 2:
        return maximum, None
    heap = [(-len(v), value) for value, v in enumerate(buckets) if v]
    from heapq import heapify
    heapify(heap)
    pairs = []
    for _ in range(p - 1):
        require(len(heap) >= 2, 'ACTUAL_PAIRING_UNAVAILABLE')
        ca, va = heappop(heap)
        cb, vb = heappop(heap)
        first, second = buckets[va].pop(), buckets[vb].pop()
        pairs.append((first, second))
        ca += 1
        cb += 1
        if ca:
            heappush(heap, (ca, va))
        if cb:
            heappush(heap, (cb, vb))
    omitted = {a for a, _ in pairs}
    base = (sum(signed[k] for k in rotations if k not in omitted)
            + word[i][0] - word[j][0]) % p
    possibilities = {0: ()}
    for n, (a, b) in enumerate(pairs):
        delta = (signed[a] - signed[b]) % p
        for subtotal, choices in list(possibilities.items()):
            possibilities.setdefault((subtotal + delta) % p, choices + (n,))
    require(len(possibilities) == p, 'ACTUAL_SWAP_COVERAGE')
    for n in possibilities[(-base) % p]:
        a, b = pairs[n]
        omitted.remove(a)
        omitted.add(b)
    selected = sorted([k for k in rotations if k not in omitted] + [i, j])
    check_witness(p, word, selected)
    return maximum, selected


def actual_signed_pair_samples():
    rng = Random(20261028)
    stats = {}
    for p in (3, 5, 7):
        eligible = ineligible = words = 0
        for _ in range(40):
            word = ([(rng.randrange(p), 0) for _ in range(3 * p - 3)]
                    + [(rng.randrange(p), 1) for _ in range(p + 2)])
            rng.shuffle(word)
            refl = [k for k, (_, parity) in enumerate(word) if parity]
            for i, j in combinations(refl, 2):
                _, selected = signed_pair_witness(p, word, i, j)
                eligible += selected is not None
                ineligible += selected is None
            words += 1
        stats[str(p)] = {'words': words, 'eligible_actual_pairs_with_direct_identity_witness': eligible,
                         'ineligible_pairs': ineligible}
    # A deliberately independent variant of the disclosed failed first diagnostic:
    # exactly one core rotation lies between the two chosen reflections.
    variants = {}
    for p in (5, 7):
        word = ([(1, 0)] * (2 * p - 2) + [(0, 1), (1, 0), (0, 1)]
                + [(p - 1, 0)] * (p - 2) + [(0, 1)] * p)
        i, j = 2 * p - 2, 2 * p
        require(len(word) == 4 * p - 1, 'FIRST_DIAGNOSTIC_VARIANT_LENGTH')
        maximum, selected = signed_pair_witness(p, word, i, j)
        require(maximum == 2 * p - 2 and selected is not None, 'FIRST_DIAGNOSTIC_VARIANT')
        variants[str(p)] = {'signed_maximum': maximum, 'actual_witness_indices_zero_based': selected}
    return stats, variants


def two_pair_word(p, a, b, y1, y2, core_slot, extra_slot, separated):
    # Each item carries a private chosen flag; actual adjacency is tested below.
    bins = [[], [], []]
    bins[core_slot].extend([((a, 0), True)] * (p - 2))
    bins[extra_slot].extend([((b, 0), True)] * (p - 2))
    if separated:
        bins[1].append(((a, 0), False))
        spare = p
    else:
        require(core_slot != 1 and extra_slot != 1, 'CONTIGUOUS_PAIR_SLOT')
        spare = p + 1
    bins[2].extend([((a, 0), False)] * spare)
    pair1 = [((y1, 1), True), (((y1 - a - b) % p, 1), True)]
    pair2 = [((y2, 1), True), (((y2 - a - b) % p, 1), True)]
    items = bins[0] + pair1 + bins[1] + pair2 + bins[2] + [((0, 1), False)] * (p - 2)
    word = [g for g, _ in items]
    chosen = [i for i, (_, yes) in enumerate(items) if yes]
    refl = [i for i in chosen if word[i][1]]
    require(len(word) == 4 * p - 1, 'TWO_PAIR_WORD_LENGTH')
    require(sum(e == 0 for _, e in word) == 3 * p - 3, 'TWO_PAIR_ROTATION_COUNT')
    require(sum(e == 1 for _, e in word) == p + 2, 'TWO_PAIR_REFLECTION_COUNT')
    require(refl[1] == refl[0] + 1 and refl[3] == refl[2] + 1, 'PAIR_ADJACENCY')
    require((refl[2] > refl[1] + 1) == separated, 'PAIR_SEPARATION')
    require(sum(word[i] == (a, 0) for i in chosen) == p - 2, 'SELECTED_CORE_COUNT')
    require(sum(word[i] == (b, 0) for i in chosen) == p - 2, 'SELECTED_EXTRA_COUNT')
    check_witness(p, word, chosen)
    return word, chosen, refl


def two_pair_checks_and_controls():
    stats = {}
    exemplar = None
    for p in (3, 5, 7):
        categories = Counter()
        for a in range(1, p):
            for b in range(p):
                if b == a:
                    continue
                category = 'b_zero' if b == 0 else ('b_minus_a' if b == (-a) % p else 'other_b')
                for y1 in range(p):
                    for y2 in range(p):
                        for separated in (False, True):
                            slots = range(3) if separated else (0, 2)
                            for core_slot, extra_slot in product(slots, repeat=2):
                                word, chosen, refl = two_pair_word(p, a, b, y1, y2, core_slot, extra_slot, separated)
                                categories[category] += 1
                                categories['separated' if separated else 'contiguous'] += 1
                                if exemplar is None and p == 3 and b == 0 and separated:
                                    exemplar = word, chosen, refl
        stats[str(p)] = dict(categories)
    word, chosen, refl = exemplar
    p = 3
    unused_rotation = next(i for i, (_, e) in enumerate(word) if e == 0 and i not in chosen)
    parity_mutation = sorted([i for i in chosen if i != refl[0]] + [unused_rotation])
    exponent_word = list(word)
    exponent_word[refl[0]] = ((word[refl[0]][0] + 1) % p, 1)
    duplicate = sorted(chosen[:-1] + [chosen[0]])
    controls = {
        'replace_one_selected_reflection_with_unused_rotation': expect_failure('REFLECTION_PARITY', lambda: check_witness(p, word, parity_mutation)),
        'change_one_selected_reflection_exponent': expect_failure('NONZERO_EXPONENT', lambda: check_witness(p, exponent_word, chosen)),
        'duplicate_an_actual_index': expect_failure('INDEX_ORDER_OR_DUPLICATE', lambda: check_witness(p, word, duplicate)),
    }
    # Correct product is 1-1=0; an all-plus calculation falsely obtains 2.
    p = 5
    crossed = ([(1, 0), (0, 1), (1, 0), (0, 1)] + [(0, 0)] * 6
               + [(0, 0)] * 4 + [(0, 1)] * 5)
    indices = list(range(10))
    check_witness(p, crossed, indices)
    all_plus = sum(crossed[i][0] for i in indices if crossed[i][1] == 0) % p
    require(all_plus == 2 and original_product(p, crossed, indices) == (0, 0), 'CROSSING_SIGN_CONTROL')
    controls['crossing_rotation_all_plus_mutant'] = {'actual_product': [0, 0], 'wrong_exponent': all_plus}
    # Correct reflection term is y-z; reversing it produces 2 instead of zero.
    sign_word = ([(1, 0)] + [(0, 0)] * 7 + [(1, 1), (2, 1)]
                 + [(0, 0)] * 4 + [(0, 1)] * 5)
    check_witness(p, sign_word, list(range(10)))
    wrong_reflection_sign = (1 + 2 - 1) % p
    require(wrong_reflection_sign == 2, 'REFLECTION_SIGN_CONTROL')
    controls['reflection_difference_reversed_mutant'] = {'actual_product': [0, 0], 'wrong_exponent': wrong_reflection_sign}
    return stats, controls


def corrected_family_checks():
    result = {}
    for p in (5, 7, 11, 13):
        word = ([(1, 0)] * (2 * p - 1) + [(4 % p, 1)] * 2 + [(p - 1, 0)]
                + [(4 % p, 1)] * 3
                + [g for _ in range(p - 3) for g in ((p - 1, 0), (4 % p, 1))])
        rotations = [i for i, (_, e) in enumerate(word) if not e]
        reflections = [i for i, (_, e) in enumerate(word) if e]
        require(len(word) == 4 * p - 1 and len(rotations) == 3 * p - 3
                and len(reflections) == p + 2, 'FAMILY_ACTUAL_COUNTS')
        runs = []
        parity_runs = []
        for _, e in word:
            if parity_runs and parity_runs[-1][0] == e:
                parity_runs[-1][1] += 1
            else:
                parity_runs.append([e, 1])
        runs = [n for e, n in parity_runs if e]
        require(runs == [2, 3] + [1] * (p - 3), 'FAMILY_REFLECTION_RUNS')
        require(sum(n % 2 for _, n in parity_runs) == 2 * p - 3, 'FAMILY_ODD_RUNS')
        chosen = sorted(rotations[:p - 2] + rotations[2 * p - 1:] + reflections[:4])
        check_witness(p, word, chosen)
        all_pair_count = 0
        for i, j in combinations(reflections, 2):
            signed = [((-word[k][0]) if i < k < j else word[k][0]) % p for k in rotations]
            counts = Counter(signed)
            require(counts[1] >= 2 * p - 1 and max(counts.values()) > 2 * p - 2,
                    'FAMILY_SIGNED_SELECTOR_QUALIFIED')
            minus = counts[p - 1]
            require(minus <= p - 2 and counts[1] + minus == 3 * p - 3,
                    'FAMILY_SIGNED_COUNTS')
            # q negative signed values can be selected iff these explicit bounds hold.
            low = max(0, 2 * p - 2 - counts[1])
            high = min(minus, 2 * p - 2)
            support = {(2 * p - 2 - 2 * q) % p for q in range(low, high + 1)}
            require(0 not in support, 'FAMILY_TWO_REFLECTION_IDENTITY')
            all_pair_count += 1
        require(sum(word[i][0] for i in rotations[:2 * p - 2]) % p == p - 2,
                'FAMILY_FIXED_CORE_SUM')
        result[str(p)] = {'rotation_count': len(rotations), 'reflection_count': len(reflections),
                          'reflection_runs': runs, 'odd_type_runs': 2 * p - 3,
                          'all_reflection_pairs_checked': all_pair_count,
                          'four_reflection_actual_indices_zero_based': chosen}
    return result


def witness3(word):
    # Exact left-to-right subset DP; stage masks record every exponent per parity/length.
    even, odd = [0] * 7, [0] * 7
    even[0] = 1
    stages = [(even[:], odd[:])]
    for t, (x, flip) in enumerate(word, 1):
        for k in range(min(t, 6), 0, -1):
            if flip:
                v = odd[k - 1]
                n = (-x) % 3
                even[k] |= ((v << n) | (v >> (3 - n))) & 7
                v = even[k - 1]
                n = x
                odd[k] |= ((v << n) | (v >> (3 - n))) & 7
            else:
                v = even[k - 1]
                n = x
                even[k] |= ((v << n) | (v >> (3 - n))) & 7
                v = odd[k - 1]
                n = (-x) % 3
                odd[k] |= ((v << n) | (v >> (3 - n))) & 7
        stages.append((even[:], odd[:]))
        if even[6] & 1:
            break
    if not even[6] & 1:
        return None
    exp = parity = 0
    k = 6
    chosen = []
    for t in range(len(stages) - 1, 0, -1):
        previous = stages[t - 1]
        if (previous[parity][k] >> exp) & 1:
            continue
        x, flip = word[t - 1]
        prev_parity = parity ^ flip
        prev_exp = (exp - (x if prev_parity == 0 else -x)) % 3
        require(k > 0 and (previous[prev_parity][k - 1] >> prev_exp) & 1, 'P3_BACKTRACK')
        chosen.append(t - 1)
        k -= 1
        parity, exp = prev_parity, prev_exp
    require(k == 0 and parity == 0 and exp == 0, 'P3_BACKTRACK_ORIGIN')
    chosen.reverse()
    check_witness(3, word, chosen)
    return chosen


def normalized_p3_exhaustion():
    # Scaling makes core a=1, and a common reflection shift makes the first y=0.
    # Both are automorphisms of D6 and preserve original indices and identity.
    count = missing = crosschecked = 0
    chosen_reflection_hist = Counter()
    actual_adjacent_pair_hist = Counter()
    for rot_positions in combinations(range(11), 6):
        rot_set = set(rot_positions)
        for extra in rot_positions:
            for b in (0, 2):
                for rest in product(range(3), repeat=4):
                    ys = iter((0,) + rest)
                    word = [(b if i == extra else 1, 0) if i in rot_set else (next(ys), 1)
                            for i in range(11)]
                    chosen = witness3(word)
                    count += 1
                    pairs = sum(word[i][1] and word[i + 1][1] for i in range(10))
                    actual_adjacent_pair_hist[str(pairs)] += 1
                    if chosen is None:
                        missing += 1
                    else:
                        chosen_reflection_hist[str(sum(word[i][1] for i in chosen))] += 1
                    if count % 137 == 1:
                        brute = next((indices for indices in combinations(range(11), 6)
                                      if original_product(3, word, indices) == (0, 0)), None)
                        require((brute is None) == (chosen is None), 'P3_BRUTE_DP_DISAGREEMENT')
                        if brute is not None:
                            check_witness(3, word, list(brute))
                        crosschecked += 1
    require(count == 449064, 'P3_NORMALIZED_TOTAL')
    return {'normalized_core_words': count, 'without_a_selector': missing,
            'witness_reflection_count_histogram': dict(chosen_reflection_hist),
            'actual_adjacent_pair_count_histogram': dict(actual_adjacent_pair_hist),
            'also_bruteforced_all_6_index_subsets_for': crosschecked,
            'each_returned_dp_witness_directly_multiplied': True}


def main():
    receipt = HERE / 'checker-receipt-v1.json'
    require(not receipt.exists(), 'RECEIPT_ALREADY_EXISTS')
    pins = []
    for path, expected in INPUTS:
        data = path.read_bytes()
        digest = sha256(data).hexdigest()
        require(digest == expected, 'SOURCE_PIN_MISMATCH: ' + str(path))
        pins.append({'path': str(path), 'sha256': digest, 'bytes': len(data), 'LF': data.count(b'\n')})
    lemmas = subset_lemma()
    multiplicities = pairing_multiplicity_check()
    samples, diagnostic_variant = actual_signed_pair_samples()
    pair_stats, controls = two_pair_checks_and_controls()
    family = corrected_family_checks()
    p3 = normalized_p3_exhaustion()
    now = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
    result = {'status': 'PASS_BOUNDED_CHECKS', 'observed_clock_before_receipt_write': now,
              'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'inputs_in_order': pins,
              'limits': 'Finite exact checks only; not an all-prime proof, formal certification, independent-family review or novelty check.',
              'subset_sum_lemma': lemmas, 'unequal_pairing_and_growth': multiplicities,
              'actual_signed_pair_samples': samples,
              'independently_constructed_failed_diagnostic_variants_not_the_original_first_file': diagnostic_variant,
              'explicit_two_pair_witnesses': pair_stats, 'intended_reason_controls': controls,
              'corrected_illustrative_family': family, 'p3_normalized_core_exhaustion': p3}
    with receipt.open('x', encoding='utf-8') as output:
        json.dump(result, output, indent=2, sort_keys=True)
        output.write('\n')
    print(json.dumps({'status': result['status'], 'clock': now, 'receipt': str(receipt),
                      'receipt_sha256': sha256(receipt.read_bytes()).hexdigest(),
                      'checker_sha256': result['checker_sha256'], 'p3': p3}, sort_keys=True))


if __name__ == '__main__':
    main()
