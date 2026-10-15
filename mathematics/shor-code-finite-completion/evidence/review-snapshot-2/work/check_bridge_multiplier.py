#!/usr/bin/env python3
"""Exact sanity checks of the written bridge and unit-multiplier lemma.

These replay the claimed identities on explicit finite maximal codes. They are
not proofs of the general statements and do not search for a Shor completion.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_T = 3


def ud(words):
    if '' in words:
        return False
    pending = {v[len(u):] for u in words for v in words if u != v and v.startswith(u)}
    seen = set()
    while pending:
        if '' in pending:
            return False
        frozen = frozenset(pending)
        if frozen in seen:
            return True
        seen.add(frozen)
        pending = ({v[len(u):] for u in words for v in pending if v.startswith(u)}
                   | {v[len(u):] for u in pending for v in words if v.startswith(u)})
    return True


def kraft(words):
    return sum((Fraction(1, 2 ** len(w)) for w in words), Fraction())


def bridge_sets(words):
    pure = [w for w in words if set(w) == {'a'}]
    assert len(pure) == 1, 'a finite complete UD code has exactly one pure a-power'
    n = len(pure[0])
    y_raw, r_raw, l_raw = [], [], []
    for w in words:
        if w.count('b') == 1:
            i = w.index('b')
            y_raw.append((i, len(w) - i - 1))
        stripped = w.lstrip('b')
        if w.startswith('b') and set(stripped) <= {'a'}:
            r_raw.append(len(stripped))
        stripped = w.rstrip('b')
        if w.endswith('b') and set(stripped) <= {'a'}:
            l_raw.append(len(stripped))
    residues = {
        'Y': [(i % n, j % n) for i, j in y_raw],
        'R': [r % n for r in r_raw],
        'L': [l % n for l in l_raw],
    }
    # Injectivity of raw codewords into residues is part of the written bridge.
    for name, values in residues.items():
        assert len(values) == len(set(values)), f'{name} raw-to-residue map not injective'
    return n, set(residues['Y']), set(residues['R']), set(residues['L'])


def tiling_counts(n, left, factors, right):
    counts = Counter()
    for choice in product(sorted(left), *[sorted(f) for f in factors], sorted(right)):
        r, middle, l = choice[0], choice[1:-1], choice[-1]
        if not middle:
            counts[((r + l) % n,)] += 1
            continue
        image = [(r + middle[0][0]) % n]
        for (_, j), (i, _) in zip(middle, middle[1:]):
            image.append((j + i) % n)
        image.append((middle[-1][1] + l) % n)
        counts[tuple(image)] += 1
    return counts


def tiles(n, left, factors, right):
    counts = tiling_counts(n, left, factors, right)
    return len(counts) == n ** (len(factors) + 1) and set(counts.values()) == {1}


def left_multiply(n, pairs, u):
    return {(u * i % n, j) for i, j in pairs}


def right_multiply(n, pairs, u):
    return {(i, u * j % n) for i, j in pairs}


def family_tiles(n, left, family, right, max_t=MAX_T):
    for t in range(max_t + 1):
        for factors in product(family, repeat=t):
            if not tiles(n, left, factors, right):
                return False
    return True


def analyse(name, words):
    words = set(words)
    result = {'name': name, 'words': sorted(words, key=lambda w: (len(w), w)),
              'ud': ud(words), 'kraft': str(kraft(words))}
    assert result['ud'] and kraft(words) == 1, name
    n, y, r, l = bridge_sets(words)
    result.update({'n': n, 'Y': sorted(y), 'R': sorted(r), 'L': sorted(l)})
    assert len(y) == n and len(r) * len(l) == n
    result['bridge_tiles_t_le_3'] = family_tiles(n, r, [y], l)
    assert result['bridge_tiles_t_le_3']
    units = [u for u in range(1, n) if gcd(u, n) == 1]
    unit_checks = []
    for u in units:
        z_left, z_right = left_multiply(n, y, u), right_multiply(n, y, u)
        left_ok = family_tiles(n, r, [y, z_left], l)
        right_ok = family_tiles(n, r, [y, z_right], l)
        assert left_ok and right_ok, (name, u)
        unit_checks.append({'u': u, 'left_family_tiles': left_ok, 'right_family_tiles': right_ok})
    result['unit_multiplier_checks'] = unit_checks
    non_units = []
    for u in range(2, n):
        if gcd(u, n) != 1:
            non_units.append({'u': u,
                              'left_alone_tiles': family_tiles(n, r, [left_multiply(n, y, u)], l),
                              'right_alone_tiles': family_tiles(n, r, [right_multiply(n, y, u)], l)})
    result['non_unit_observations'] = non_units
    return result


def main():
    rss_example_6 = ['aaaaaa', 'abaaaa', 'baaaa', 'abaa', 'baa', 'aaaaab',
                     'abaaab', 'baaab', 'abab', 'bab', 'b']
    cordero_e = ['b', 'ab', 'aaaa', 'aaba', 'aaab', 'aabb']
    examples = {
        'cordero2023_eq7': cordero_e,
        'cordero2023_eq7_reversed': [w[::-1] for w in cordero_e],
        'rss1989_example6': rss_example_6,
        'rss1989_example6_reversed': [w[::-1] for w in rss_example_6],
        'prefix_aa_ab_b_composed_with_suffix_code': ['aa', 'b', 'aaab', 'abab', 'bab'],
    }
    analyses = [analyse(name, words) for name, words in examples.items()]

    controls = []
    # Removing a one-b boundary word leaves a UD incomplete code whose data cannot tile.
    incomplete = set(rss_example_6) - {'baa'}
    assert ud(incomplete) and kraft(incomplete) < 1
    n, y, r, l = bridge_sets(incomplete)
    controls.append({'name': 'rss_example6_minus_baa', 'kraft': str(kraft(incomplete)),
                     'bridge_family_tiles': family_tiles(n, r, [y], l)})
    assert not controls[-1]['bridge_family_tiles']
    # The identity is necessary only: deleting a two-b word keeps the same data tiling.
    incomplete = set(rss_example_6) - {'abab'}
    assert ud(incomplete) and kraft(incomplete) < 1
    n, y, r, l = bridge_sets(incomplete)
    controls.append({'name': 'rss_example6_minus_abab_no_converse', 'kraft': str(kraft(incomplete)),
                     'bridge_family_tiles': family_tiles(n, r, [y], l)})
    assert controls[-1]['bridge_family_tiles']
    # A false non-unit multiplier can destroy tiling; this shows units are not vacuous.
    witnessed = [(a['name'], item['u']) for a in analyses for item in a['non_unit_observations']
                 if not (item['left_alone_tiles'] and item['right_alone_tiles'])]
    assert witnessed
    controls.append({'name': 'non_unit_multiplier_failures', 'witnesses': witnessed})
    # Mutating a tiling family by duplicating a residue must be rejected by the tile test.
    name = 'cordero2023_eq7'
    words = set(examples[name])
    n, y, r, l = bridge_sets(words)
    y_bad = set(y)
    y_bad.remove(sorted(y)[-1])
    y_bad.add((sorted(y)[0][0], (sorted(y)[0][1] + 1) % n))
    controls.append({'name': 'cordero_eq7_mutated_Y', 'tiles': tiles(n, r, [y_bad], l)})
    assert not controls[-1]['tiles']

    # Arithmetic heart of the 8-divisor proof on the 660-multiples below 66000.
    eight_cases = []
    for n in range(660, 66000, 660):
        if n % 8 == 0:
            continue
        m = n // 4
        u = (m + 1) // 2
        if u % 2 == 0:
            u += m
        assert gcd(u, n) == 1 and 8 * u % n == 4 % n and 4 % n != 0
        s = 3 * u % n
        first, second = ((s, 4), (0, 0)), ((s, 0), (8 * u % n, 0))
        assert first != second
        image = lambda pair: (pair[0][0], (pair[0][1] + pair[1][0]) % n, pair[1][1])
        assert image(first) == image(second)
        eight_cases.append({'n': n, 'u': u})
    report = {
        'schema': 'shor-bridge-multiplier-sanity/1', 'date': '2026-10-14 PT',
        'scope': 'Replays written lemmas on explicit maximal codes up to t=3; empirical sanity only, not a general proof.',
        'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'examples': analyses, 'controls': controls,
        'eight_divisor_arithmetic_samples': {'count': len(eight_cases), 'first': eight_cases[:3]},
    }
    out = ROOT / 'evidence/bridge-multiplier-sanity.json'
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'examples': [(a['name'], a['n'], a['R'], a['L']) for a in analyses],
                      'controls': controls, 'eight_cases': len(eight_cases)}, indent=1))


if __name__ == '__main__':
    main()
