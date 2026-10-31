#!/usr/bin/env python3
"""Exact outsider conflict profile of one actual 88-word R-minus strategy."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

INPUT = Path(__file__).with_name('frontier-20261028-fd-law-search-precise-result.json')
OUTPUT = Path(__file__).with_name('frontier-20261028-binary-conflict-profile-result.json')
NEIGHBOURS = {
    1: (2, 3, 4, 5, 6, 7), 2: (1, 3, 7, 9, 10),
    3: (1, 2, 4, 8, 9), 4: (1, 3, 5, 8, 10),
    5: (1, 4, 6, 9, 10), 6: (1, 5, 7, 8, 9),
    7: (1, 2, 6, 8, 10), 8: (3, 4, 6, 7, 9, 10),
    9: (2, 3, 5, 6, 8), 10: (2, 4, 5, 7, 8),
}


def conflict(a, b):
    for v, neighbours in NEIGHBOURS.items():
        if ((a >> (v-1)) & 1) != ((b >> (v-1)) & 1):
            if all(((a >> (u-1)) & 1) == ((b >> (u-1)) & 1) for u in neighbours):
                return True
    return False


def main():
    raw = INPUT.read_bytes()
    support = sorted(json.loads(raw)['support_words_one_based_bitsets'])
    assert len(support) == len(set(support)) == 88
    assert all(not conflict(a, b) for a, b in combinations(support, 2))
    S = set(support)
    outsiders = []
    for x in range(1024):
        if x not in S:
            blockers = [y for y in support if conflict(x, y)]
            outsiders.append({'word': x, 'conflicts': len(blockers), 'blockers': blockers})
    hist = Counter(entry['conflicts'] for entry in outsiders)
    minimum = min(hist)
    best = [entry for entry in outsiders if entry['conflicts'] == minimum]
    result = {
        'input_sha256': sha256(raw).hexdigest(), 'support_size': 88,
        'binary_domain_size': 1024, 'outsiders_checked': len(outsiders),
        'outsider_conflict_histogram': dict(sorted(hist.items())),
        'minimum_conflicts_per_outsider': minimum, 'minimum_witnesses': best,
        'exact_local_claim': 'Any valid binary support containing any outside word and retaining this support except for deleted words must delete at least the minimum number of old support words.',
        'limits': 'One fixed 88-word support only. No bound on other binary supports, q>2, nonuniform laws or the original guessing number.',
    }
    with OUTPUT.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'minimum_witnesses'}, indent=2))
    print('minimizing_outsider_count', len(best))
    print('first_five_minimum_witnesses', best[:5])


if __name__ == '__main__':
    main()
