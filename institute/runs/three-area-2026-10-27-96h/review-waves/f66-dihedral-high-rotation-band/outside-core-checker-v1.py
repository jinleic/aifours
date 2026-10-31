#!/usr/bin/env python3
"""Independent bounded check of the pre-exclusion outside-core endpoint branch."""
import hashlib
import itertools
import json
import random
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST_SHA = '0be83969f645bde8b4fb27e5b02be797d2f0b572db4ee31ec03258b1685dab71'
SEED = 0x66362D4F5554


def ensure(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def multiply(p, word, selected):
    x, flip = 0, 0
    for j in selected:
        kind, exponent = word[j]
        x = (x + (-exponent if flip else exponent)) % p
        flip ^= kind
    return x, flip


def actual_word(p, a, gaps, labels, before, after):
    word = [(0, a)] * before + [(1, labels[0])]
    for gap, label in zip(gaps, labels[1:]):
        word.extend((0, exponent) for exponent in gap)
        word.append((1, label))
    word.extend([(0, a)] * after)
    return word


def examine(p, a, word):
    ensure(len(word) == 4 * p - 1, 'WORD_LENGTH')
    rotations = [i for i, item in enumerate(word) if item[0] == 0]
    refs = [i for i, item in enumerate(word) if item[0] == 1]
    ensure(len(rotations) == 3 * p - 3 and len(refs) == p + 2, 'BAND_COUNTS')
    ensure(sum(word[i][1] == a for i in rotations) == 2 * p - 1, 'CORE_COUNT')
    ensure(sum(word[i][1] == (-a) % p for i in rotations) == p - 2, 'EXTRA_COUNT')
    first, last = refs[0], refs[-1]
    outside = [i for i in rotations if not first < i < last]
    ensure(1 <= len(outside) <= p - 2, 'OUTSIDE_CORE_COUNT')
    ensure(all(word[i][1] == a for i in outside), 'EXTRA_OUTSIDE')
    gaps = [word[i + 1:j] for i, j in zip(refs, refs[1:])]
    empty = [i for i, gap in enumerate(gaps) if not gap]
    ensure(len(empty) == 2 and empty[1] == empty[0] + 1, 'TRIPLE_BOUNDARIES')
    triple = refs[empty[0]:empty[0] + 3]
    ensure(len({word[i][1] for i in triple}) == 1, 'TRIPLE_EXPONENTS')
    large = [gap for gap in gaps if sum(kind == 0 and x == a for kind, x in gap) >= p + 1]
    ensure(len(large) == 1 and all(x == a for kind, x in large[0]), 'LARGE_GAP')
    signed = {i: (word[i][1] if not first < i < last else -word[i][1]) % p for i in rotations}
    plus = [i for i in rotations if signed[i] == a]
    minus = [i for i in rotations if signed[i] == (-a) % p]
    ensure(len(plus) == p - 2 + len(outside), 'PLUS_COUNT')
    ensure(len(minus) == 2 * p - 1 - len(outside), 'MINUS_COUNT')
    ensure(len(plus) >= p - 1 and len(minus) >= p - 1, 'OPPOSITE_PAIR_COUNT')
    pairs = list(zip(plus[:p - 1], minus[:p - 1]))
    target = (sum(signed.values()) + word[first][1] - word[last][1]) % p
    supports, chosen = set(), None
    for mask in range(1 << (p - 1)):
        omitted = [pair[(mask >> j) & 1] for j, pair in enumerate(pairs)]
        residue = sum(signed[i] for i in omitted) % p
        supports.add(residue)
        if residue == target and chosen is None:
            chosen = set(omitted)
    ensure(supports == set(range(p)) and chosen is not None, 'SWAP_SUPPORT')
    selected = sorted([first, last] + [i for i in rotations if i not in chosen])
    ensure(len(selected) == 2 * p and len(set(selected)) == 2 * p, 'SELECTOR_INDICES')
    ensure(multiply(p, word, selected) == (0, 0), 'ORDERED_PRODUCT')
    location = 'left' if triple[0] == first else 'right' if triple[-1] == last else 'interior'
    placement = 'both' if first > 0 and last < len(word) - 1 else 'left' if first > 0 else 'right'
    return location, placement, len(outside), selected


def main():
    raw = (ROOT / 'manifest-v1.json').read_bytes()
    ensure(sha(raw) == MANIFEST_SHA, 'MANIFEST_SHA')
    manifest = json.loads(raw)
    pins = []
    for source in manifest['inputs_in_read_order']:
        data = Path(source['path']).read_bytes()
        ensure(sha(data) == source['sha256'] and len(data) == source['bytes'] and
               data.count(b'\n') == source['LF'], 'SOURCE_PIN')
        pins.append(source['sha256'])
    rng = random.Random(SEED)
    counts, equalities, examples = Counter(), Counter(), {}

    def consume(p, a, gaps, labels, before, after):
        word = actual_word(p, a, gaps, labels, before, after)
        location, placement, n_outside, selector = examine(p, a, word)
        endpoint_relation = 'equal' if labels[0] == labels[-1] else 'unequal'
        counts[f'p{p}:{location}:{placement}:{endpoint_relation}'] += 1
        if n_outside == 1:
            equalities[f'p{p}:plus_exactly_p_minus_1'] += 1
        if n_outside == p - 2:
            equalities[f'p{p}:minus_exactly_p_plus_1'] += 1
        if str(p) not in examples:
            examples[str(p)] = {'word_type_exponent': word, 'selector_one_based': [i + 1 for i in selector],
                                'outside_core': n_outside, 'triple_location': location}

    # Exhaust the specified normalized p=3 outside-core family, including both core signs,
    # all triple locations, big-gap locations, endpoint sides and triple-compatible labels.
    p = 3
    for a in (1, 2):
        for start in range(p):
            available = [j for j in range(p + 1) if j not in (start, start + 1)]
            for big in available:
                small = next(j for j in available if j != big)
                gaps = [[] for _ in range(p + 1)]
                gaps[big] = [a] * (p + 1)
                gaps[small] = [(-a) % p]
                for before, after in ((1, 0), (0, 1)):
                    for labels in itertools.product(range(p), repeat=p + 2):
                        if labels[start] == labels[start + 1] == labels[start + 2]:
                            consume(p, a, gaps, labels, before, after)
    ensure(sum(v for key, v in counts.items() if key.startswith('p3:')) == 648, 'P3_COUNT')

    for p in (5, 7, 11):
        for start in range(p):
            for rep in range(24):
                a = rng.randrange(1, p)
                available = [j for j in range(p + 1) if j not in (start, start + 1)]
                big = rng.choice(available)
                small = [j for j in available if j != big]
                n_outside = 1 if rep % 4 == 0 else p - 2 if rep % 4 == 1 else rng.randrange(1, p - 1)
                moved = set(rng.sample(small, n_outside))
                gaps = [[] for _ in range(p + 1)]
                gaps[big] = [a] * (p + 1)
                for j in small:
                    gaps[j] = [(-a) % p] if j in moved else [a, (-a) % p]
                before = 0 if rep % 3 == 0 else n_outside if rep % 3 == 1 else rng.randrange(n_outside + 1)
                after = n_outside - before
                labels = [rng.randrange(p) for _ in range(p + 2)]
                for j in range(start, start + 3):
                    labels[j] = labels[start]
                outside_endpoint = 0 if start == p - 1 else p + 1
                other_endpoint = p + 1 if outside_endpoint == 0 else 0
                labels[outside_endpoint] = (labels[other_endpoint] + (0 if rep % 2 == 0 else rng.randrange(1, p))) % p
                consume(p, a, gaps, labels, before, after)
    for p in (3, 5, 7, 11):
        for side in ('left', 'interior', 'right'):
            ensure(any(key.startswith(f'p{p}:{side}:') and value for key, value in counts.items()), 'TRIPLE_COVERAGE')
        ensure(equalities[f'p{p}:plus_exactly_p_minus_1'] > 0, 'PLUS_BOUNDARY')
        ensure(equalities[f'p{p}:minus_exactly_p_plus_1'] > 0, 'MINUS_BOUNDARY')
    clock = subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], check=True,
                           capture_output=True, text=True).stdout.strip()
    receipt = {'status': 'PASS_BOUNDED_OUTSIDE_CORE_NOT_A_UNIVERSAL_PROOF',
               'observed_clock_before_receipt_write': clock, 'manifest_sha256': MANIFEST_SHA,
               'source_sha256_in_read_order': pins, 'checker_sha256': sha(Path(__file__).read_bytes()),
               'seed': SEED, 'counts': dict(sorted(counts.items())), 'boundary_counts': dict(sorted(equalities.items())),
               'total_actual_words': sum(counts.values()), 'example_words_and_witnesses': examples,
               'method': 'Each word tests all 2^(p-1) opposite-pair omissions; each selected witness is multiplied in original order.',
               'limits': 'p3 exhaustive only in this specified big-gap/saturated family, not over all words; larger primes sampled.'}
    with (ROOT / 'outside-core-receipt-v1.json').open('x', encoding='utf-8') as output:
        json.dump(receipt, output, indent=2, sort_keys=True)
        output.write('\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
