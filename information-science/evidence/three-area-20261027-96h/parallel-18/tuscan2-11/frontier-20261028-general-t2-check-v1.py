#!/usr/bin/env python3
"""Independent general-order Tuscan-k checker for an actual row array.

Reads only the "rows" field of a JSON file. Verifies each row is a
permutation of 0..n-1 and that for every m=1..k each ordered pair (a,b)
occurs with b exactly m places right of a in at most one row (linear rows, no
wraparound). Also reports whether distance-one coverage is complete.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path


def main(argv):
    if len(argv) != 4:
        raise ValueError('usage: SCRIPT INPUT.json K OUTPUT.json')
    source, k, output = Path(argv[1]), int(argv[2]), Path(argv[3])
    raw = source.read_bytes()
    rows = json.loads(raw)['rows']
    n = len(rows)
    if n < 2 or k < 1 or k >= n:
        raise ValueError('invalid order or k')
    permutations = all(isinstance(r, list) and sorted(r) == list(range(n)) for r in rows)
    per_distance = {}
    ok = permutations
    for m in range(1, k + 1):
        counts = Counter((r[i], r[i + m]) for r in rows for i in range(n - m)) if permutations else Counter()
        repeats = sorted([list(e) for e, c in counts.items() if c > 1])
        per_distance[str(m)] = {'events': sum(counts.values()), 'distinct': len(counts), 'repeated_pairs': repeats}
        ok = ok and not repeats
    complete_d1 = permutations and per_distance['1']['distinct'] == n * (n - 1)
    result = {'input': str(source), 'input_sha256': hashlib.sha256(raw).hexdigest(), 'n': n, 'k': k,
              'all_rows_permutations': permutations, 'per_distance': per_distance,
              'distance_one_complete': complete_d1, 'is_tuscan_k_square': ok,
              'first_column': [r[0] for r in rows] if permutations else None,
              'last_column': [r[-1] for r in rows] if permutations else None}
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'n': n, 'k': k, 'is_tuscan_k_square': ok, 'distance_one_complete': complete_d1,
                      'input_sha256': result['input_sha256']}))


if __name__ == '__main__':
    main(sys.argv)
