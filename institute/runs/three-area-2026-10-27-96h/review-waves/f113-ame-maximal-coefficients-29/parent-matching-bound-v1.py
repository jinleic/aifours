#!/usr/bin/env python3
"""Enumerate the three-color matching relaxation independently of its author."""
import hashlib
import itertools
import json
import subprocess
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-global-ame46-maximal-coefficients29-v1.md')
EXPECTED = '2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c'
OUT = HERE / 'parent-matching-bound-result-v1.json'


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          capture_output=True, text=True, check=True).stdout.strip()


def main():
    started = clock()
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED:
        raise ValueError('SOURCE_HASH_MISMATCH')
    if OUT.exists():
        raise FileExistsError(OUT)
    perms = tuple(itertools.permutations(range(3)))
    fiber_hist, total_hist = Counter(), Counter()
    max_one_removed = 0
    all_unfixed_edge_cases = 0
    for bc, bd, cd in itertools.product(perms, repeat=3):
        total = total_removed = 0
        for a in range(3):
            allowed = [v for v in range(3) if v != a]
            cube = tuple(itertools.product(allowed, repeat=3))
            bad = [{v for v in cube if v[1] == bc[v[0]]},
                   {v for v in cube if v[2] == bd[v[0]]},
                   {v for v in cube if v[2] == cd[v[1]]}]
            survivor = len(set(cube).difference(*bad))
            fiber_hist[survivor] += 1
            total += survivor
            total_removed += len(set(cube).difference(bad[0], bad[1]))
            if all(p[a] != a for p in (bc, bd, cd)):
                all_unfixed_edge_cases += 1
                if any(len(edge) != 2 for edge in bad) or len(set.union(*bad)) < 4:
                    raise AssertionError('CUBE_EDGE_BOUND')
        total_hist[total] += 1
        max_one_removed = max(max_one_removed, total_removed)
    if sum(total_hist.values()) != 216 or max(fiber_hist) != 4 or max(total_hist) != 12:
        raise AssertionError('MATCHING_BOUND')
    if max_one_removed != 15:
        raise AssertionError('DROPPED_MATCHING_CONTROL')
    receipt = {
        'kind': 'PARENT_INDEPENDENT_THREE_COLOR_MATCHING_CONTROL',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'candidate_sha256': digest,
        'interleaf_matching_triples': sum(total_hist.values()),
        'A_fibers_examined': sum(fiber_hist.values()),
        'survivors_per_fiber_histogram': dict(sorted(fiber_hist.items())),
        'survivors_total_histogram': dict(sorted(total_hist.items())),
        'maximum_per_fiber': max(fiber_hist),
        'maximum_total': max(total_hist),
        'all_three_unfixed_edge_cases': all_unfixed_edge_cases,
        'control_drop_one_matching_maximum': max_one_removed,
        'limits': 'Enumerates an overapproximation of residual supports only. '
                  'Does not prove the active-alphabet reduction, the balanced-fiber '
                  'contradiction, no-OLS(6), or existence of an AME tensor.',
    }
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
