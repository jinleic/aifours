#!/usr/bin/env python3
"""Independent ordered dihedral selector enumeration, not author code.

p=3: every raw order, each a=1,2, and all six reflection labels. Every
six-index selector is evaluated symbolically as a cyclic rotation constant
and an alternating sum of actual selected reflection labels. Its satisfying
label assignments are exact bitsets; we enumerate all assignments and test
membership. Direct multiplication DP cross-checks samples of this separate
symbolic implementation. p=5,7: seeded iid word samples plus separately
labelled gauge stress samples; every reported witness is multiplied directly.
"""
from itertools import combinations, product
from collections import Counter
import json
import random
import subprocess
import time
from pathlib import Path

OUT = Path(__file__).with_name('exact-check-results-v1.json')
SEED = 0x77D1E2A1


def multiply(word, indices, p):
    exponent = parity = 0
    for i in indices:
        x, reflection = word[i]
        exponent = (exponent + (-x if parity else x)) % p
        parity ^= reflection
    return exponent, parity


def exact_selector(word, p, size, reflections=None):
    # DP over actual index positions and actual D_(2p) group products.
    # Store one tuple of ordered, distinct indices per reachable state.
    layers = [dict() for _ in range(size + 1)]
    layers[0][(0, 0, 0)] = ()
    for i, (x, is_reflection) in enumerate(word):
        for n in range(min(size, i + 1), 0, -1):
            previous = layers[n - 1]
            dest = layers[n]
            for (e, parity, nr), inds in previous.items():
                nr2 = nr + is_reflection if reflections is not None else 0
                if reflections is not None and nr2 > reflections:
                    continue
                state = ((e + (-x if parity else x)) % p,
                         parity ^ is_reflection, nr2)
                if state not in dest:
                    dest[state] = inds + (i,)
    return layers[size].get((0, 0, reflections if reflections is not None else 0))


def check_witness(word, p, inds, size, nrefs=None):
    assert inds is not None and len(inds) == size
    assert tuple(sorted(set(inds))) == tuple(inds)
    assert all(0 <= i < len(word) for i in inds)
    if nrefs is not None:
        assert sum(word[i][1] for i in inds) == nrefs
    assert multiply(word, inds, p) == (0, 0)


def encode_choice(pattern, choice):
    # Symbolic exponent: c*a + alternating sum of chosen y's, parity=0.
    c = parity = bits = 0
    for i in choice:
        kind, value = pattern[i]
        if kind == 'R':
            bits |= 1 << value
            parity ^= 1
        else:
            c += (-value if parity else value)
    return c, bits, parity


def make_pattern(refpositions, negposition):
    refset = set(refpositions)
    ordinal = 0
    out = []
    for pos in range(11):
        if pos in refset:
            out.append(('R', ordinal))
            ordinal += 1
        else:
            out.append(('X', -1 if pos == negposition else 1))
    return out


def concrete_word(pattern, a, labels, p):
    return [((labels[value] if kind == 'R' else a * value) % p,
             int(kind == 'R')) for kind, value in pattern]


def low_edges(word, a, p):
    # Recover integer prefix walk from actual word, not signed field residues.
    q = 0
    refs = []
    for i, (x, is_reflection) in enumerate(word):
        if is_reflection:
            refs.append((i, q))
        else:
            assert x == a or x == (-a) % p
            q += 1 if x == a else -1
    edges = []
    for i, j in combinations(range(len(refs)), 2):
        delta = refs[j][1] - refs[i][1]
        if 0 <= delta <= p:
            edges.append((i, j, delta))
    separated = next(((a0, b0, c0, d0) for a0, b0, _ in edges
                      for c0, d0, _ in edges if b0 < c0), None)
    assert separated is not None
    return refs, edges, separated


def pair_rotation_sums(word, p, i, j, take):
    signed = []
    for pos, (x, is_reflection) in enumerate(word):
        if not is_reflection:
            signed.append((-x if i < pos < j else x) % p)
    # Bitsets of exactly k signed sums; include/exclude every original rotation.
    reach = [0] * (take + 1)
    reach[0] = 1
    full = (1 << p) - 1
    for n, x in enumerate(signed, 1):
        for k in range(min(n, take), 0, -1):
            b = reach[k - 1]
            shifted = ((b << x) | (b >> (p - x))) & full if x else b
            reach[k] |= shifted
    return reach[take], sum(signed) % p


def construct_four(word, p, refs, separated):
    chosen_ref_positions = [refs[k][0] for k in separated]
    by_signed_value = {}
    for i, (x, is_reflection) in enumerate(word):
        if not is_reflection:
            parity = sum(t < i for t in chosen_ref_positions) % 2
            v = (-x if parity else x) % p
            by_signed_value.setdefault(v, []).append(i)
    omit = next((v[:p] for v in by_signed_value.values() if len(v) >= p), None)
    assert omit is not None
    omitted = set(omit)
    indices = tuple(i for i, (_, is_reflection) in enumerate(word)
                    if (is_reflection and i in chosen_ref_positions)
                    or (not is_reflection and i not in omitted))
    return indices


def exhaustive_p3():
    p = 3
    label_tuples = list(product(range(p), repeat=6))
    all_assignments = (1 << len(label_tuples)) - 1
    by_refmask = {}
    for bits in range(1, 1 << 6):
        if bits.bit_count() % 2:
            continue
        masks = [0] * p
        for n, labels in enumerate(label_tuples):
            parity = total = 0
            for j in range(6):
                if bits & (1 << j):
                    total += -labels[j] if parity else labels[j]
                    parity ^= 1
            masks[total % p] |= 1 << n
        assert (masks[0] | masks[1] | masks[2]) == all_assignments
        assert all(m.bit_count() == 243 for m in masks)
        by_refmask[bits] = masks
    choices = list(combinations(range(11), 6))
    totals = Counter()
    low_pairs_examined = 0
    direct_crosschecks = 0
    words_without_two = 0
    representative = None
    patterns = 0
    for refpositions in combinations(range(11), 6):
        rotpositions = [i for i in range(11) if i not in refpositions]
        for negposition in rotpositions:
            pattern = make_pattern(refpositions, negposition)
            patterns += 1
            # Evaluate ALL distinct original six-index choices, not a
            # rearranged word. Odd parity cannot give the identity.
            coverage = {a: {2: 0, 4: 0, 6: 0} for a in (1, 2)}
            for choice in choices:
                c, bits, parity = encode_choice(pattern, choice)
                if parity:
                    continue
                nrefs = bits.bit_count()
                assert nrefs in (2, 4, 6)
                for a in (1, 2):
                    coverage[a][nrefs] |= by_refmask[bits][(-a * c) % p]
            template = concrete_word(pattern, 1, (0,) * 6, p)
            refs, edges, separated = low_edges(template, 1, p)
            # Every low pair has exactly one absent two-reflection target;
            # compute actual signed sums using a separate include/exclude DP.
            for i, j, delta in edges:
                low_pairs_examined += 1
                for a in (1, 2):
                    word0 = concrete_word(pattern, a, (0,) * 6, p)
                    reachable, total = pair_rotation_sums(word0, p, refs[i][0], refs[j][0], 4)
                    assert reachable == ((1 << p) - 1) ^ (1 << total)
                    assert total == (-2 * a * delta) % p
                    no_two = all_assignments ^ coverage[a][2]
                    pair_bits = (1 << i) | (1 << j)
                    assert not (no_two & (all_assignments ^ by_refmask[pair_bits][(-total) % p]))
            # Construct ONE legal four-reflection selector from separated
            # low edges and check it for every no-two label assignment.
            for a in (1, 2):
                word0 = concrete_word(pattern, a, (0,) * 6, p)
                four = construct_four(word0, p, refs, separated)
                c, bits, parity = encode_choice(pattern, four)
                assert len(four) == 6 and parity == 0 and bits.bit_count() == 4
                selector_mask = by_refmask[bits][(-a * c) % p]
                no_two = all_assignments ^ coverage[a][2]
                assert not (no_two & (all_assignments ^ selector_mask))
                assert not (no_two & (all_assignments ^ coverage[a][4]))
                # Enumerate each ACTUAL word (including both possible a's).
                for index, labels in enumerate(label_tuples):
                    has_two = bool((coverage[a][2] >> index) & 1)
                    has_four = bool((coverage[a][4] >> index) & 1)
                    has_six = bool((coverage[a][6] >> index) & 1)
                    totals['actual_words'] += 1
                    totals['with_two'] += has_two
                    totals['without_two_with_four'] += (not has_two and has_four)
                    totals['with_six'] += has_six
                    if not has_two:
                        words_without_two += 1
                        if representative is None:
                            w = concrete_word(pattern, a, labels, p)
                            check_witness(w, p, four, 6, 4)
                            representative = {'a': a, 'word': w,
                                              'four_reflection_witness_1_based': [x+1 for x in four]}
                    assert has_two or has_four
                # Independent direct group-product DP cross-check on two
                # deterministic label assignments for each order and a.
                for sample_index in ((patterns * 193 + a * 17) % 729,
                                     (patterns * 17 + a * 137) % 729):
                    word = concrete_word(pattern, a, label_tuples[sample_index], p)
                    for nr in (2, 4):
                        w = exact_selector(word, p, 6, nr)
                        expected = bool((coverage[a][nr] >> sample_index) & 1)
                        assert (w is not None) == expected
                        if w is not None:
                            check_witness(word, p, w, 6, nr)
                        direct_crosschecks += 1
    assert patterns == 2310
    assert totals['actual_words'] == 2 * 2310 * 729
    assert totals['actual_words'] == totals['with_two'] + totals['without_two_with_four']
    return {'p': p, 'reflections': 6, 'rotation_orders': patterns,
            'a_values': [1, 2], 'reflection_label_vectors_per_order_and_a': 729,
            **totals, 'low_pairs_examined_per_rotation_order': low_pairs_examined,
            'direct_group_dp_crosschecks_by_exact_reflection_count': direct_crosschecks,
            'no_two_count': words_without_two, 'example_no_two': representative}


def sample_word(rng, p, a, gauge):
    word = [(a, 0)] * (2*p - 2) + [((-a) % p, 0)] * (p - 2) + [(0, 1)] * (p + 3)
    rng.shuffle(word)
    q = 0
    for i, (x, is_reflection) in enumerate(word):
        if is_reflection:
            word[i] = (((-2 * a * q) % p) if gauge else rng.randrange(p), 1)
        else:
            q += 1 if x == a else -1
    return word


def sampled_primes():
    rng = random.Random(SEED)
    out = []
    counts = {}
    for p in (5, 7):
        pc = Counter()
        for gauge in (False, True):
            for sample_index in range(160):
                a = rng.randrange(1, p)
                word = sample_word(rng, p, a, gauge)
                assert len(word) == 4*p - 1
                assert Counter(x for x,t in word if not t) == Counter({a: 2*p-2, (-a)%p: p-2})
                assert sum(t for _,t in word) == p+3
                refs, edges, separated = low_edges(word, a, p)
                for i,j,delta in edges:
                    reachable, total = pair_rotation_sums(word, p, refs[i][0], refs[j][0], 2*p-2)
                    assert reachable == ((1 << p) - 1) ^ (1 << total)
                    assert total == (-2*a*delta) % p
                    pc['low_edges_checked'] += 1
                witness = exact_selector(word, p, 2*p)
                check_witness(word, p, witness, 2*p)
                w2 = exact_selector(word, p, 2*p, 2)
                if w2 is not None:
                    check_witness(word, p, w2, 2*p, 2)
                    pc['with_two_reflection_witness'] += 1
                else:
                    for i,j,delta in edges:
                        assert (word[refs[j][0]][0] - word[refs[i][0]][0] + 2*a*delta) % p == 0
                    four = construct_four(word, p, refs, separated)
                    check_witness(word, p, four, 2*p, 4)
                    pc['without_two_four_constructed'] += 1
                pc['gauge' if gauge else 'iid'] += 1
                pc['gauge_without_two' if gauge and w2 is None else 'other'] += 1
                out.append({'p': p, 'sample_type': 'gauge' if gauge else 'iid',
                            'sample_index': sample_index, 'a': a, 'word': word,
                            'selector_indices_1_based': [i+1 for i in witness],
                            'two_reflection_selector_indices_1_based': None if w2 is None else [i+1 for i in w2],
                            'constructed_four_indices_1_based': None if w2 is not None else [i+1 for i in four]})
        counts[str(p)] = dict(pc)
    return {'seed_decimal': SEED, 'per_p': counts, 'samples': out}


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    start = time.monotonic()
    exhaustive = exhaustive_p3()
    samples = sampled_primes()
    results = {'method': 'independent exact original-order D_(2p) selectors',
               'word_encoding': '[exponent modulo p, reflection bit]; 1 means r^y s',
               'p3_exhaustive': exhaustive, 'p5_p7_samples': samples,
               'elapsed_seconds': round(time.monotonic() - start, 3)}
    results['native_clock_before_receipt'] = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
        f.write('\n')
    print(json.dumps({k: v for k,v in results.items() if k != 'p5_p7_samples'}, indent=2))
    print(json.dumps({'p5_p7_sample_summary': samples['per_p'], 'seed': SEED,
                      'sample_words': len(samples['samples'])}, indent=2))
    print('receipt:', OUT)


if __name__ == '__main__':
    main()
