#!/usr/bin/env python3
"""Independent bounded check of the ordered four-reflection lemma."""
import hashlib
import itertools
import json
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson/frontier-20261028-olson-ordered-four-odd-boundary-v1.md')
EXPECTED = '7d4d356430303b1538cd1e621d0943ba9096be98fe3f53cce3184c7783a33fb5'
OUT = HERE / 'parent-ordered-four-check-result-v1.json'


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, capture_output=True, text=True).stdout.strip()


def witnesses(sequence, p):
    return sum((sequence[i] - sequence[j] + sequence[k] - sequence[l]) % p == 0
               for i, j, k, l in itertools.combinations(range(len(sequence)), 4))


def main():
    started = clock()
    actual = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if actual != EXPECTED:
        raise ValueError('SOURCE_HASH_MISMATCH')
    if OUT.exists():
        raise FileExistsError(OUT)
    cases = {}
    for p, expected_count in ((3, 16), (5, 4096)):
        histogram = Counter()
        for increments in itertools.product(range(1, p), repeat=p + 1):
            sequence = [0]
            for increment in increments:
                sequence.append((sequence[-1] + increment) % p)
            histogram[witnesses(sequence, p)] += 1
        if sum(histogram.values()) != expected_count or histogram.get(0, 0):
            raise AssertionError('QUADRUPLE_BOUND')
        short_control = list(range(p)) + [0]
        if any(short_control[i] == short_control[i + 1] for i in range(p)):
            raise AssertionError('SHORT_CONTROL_ADJACENCY')
        if witnesses(short_control, p) != 0:
            raise AssertionError('SHORT_CONTROL_EXPECTED_NO_QUADRUPLE')
        cases[str(p)] = {'normalized_sequences': sum(histogram.values()),
                         'minimum_quadruples': min(histogram),
                         'quadruple_total': sum(k*v for k, v in histogram.items()),
                         'short_p_plus_one_control': short_control,
                         'short_control_quadruples': 0}
    receipt = {
        'kind': 'PARENT_ORDERED_FOUR_FINITE_CONTROL',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'candidate_sha256': actual,
        'cases': cases,
        'limits': 'Finite p=3 and p=5 controls only; no all-prime proof, '
                  'historical residual-floor authentication, or complete '
                  'ordered-Olson solution.',
    }
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
