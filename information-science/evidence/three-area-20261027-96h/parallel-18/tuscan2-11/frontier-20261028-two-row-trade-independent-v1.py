#!/usr/bin/env python3
"""Independently enumerate all two-row T1 trades by direct path DFS.

Unlike the producer, this checker does not use bipartite matching components:
it enumerates each Hamilton path in the two-row residual digraph, then checks
whether the uniquely complementary edges form the second Hamilton cycle.
"""
import hashlib
import itertools
import json
import sys
import time
from collections import Counter
from pathlib import Path

N = 11
S = 11


def successors(row):
    sequence = [S] + list(row) + [S]
    result = [None] * 12
    for a, b in zip(sequence, sequence[1:]):
        result[a] = b
    return result


def enumerate_paths(graph):
    current = []
    def walk(v, unused):
        if not unused:
            if S in graph[v]:
                yield tuple(current)
            return
        for nxt in graph[v]:
            if unused & (1 << nxt):
                current.append(nxt)
                yield from walk(nxt, unused ^ (1 << nxt))
                current.pop()
    yield from walk(S, (1 << N) - 1)


def remaining_path(succ):
    if len(set(succ)) != 12:
        raise AssertionError('complement is not a permutation')
    used = 1 << S
    row = []
    v = S
    for _ in range(N):
        v = succ[v]
        if used & (1 << v):
            return None
        used |= 1 << v
        row.append(v)
    return tuple(row) if succ[v] == S else None


def score(rows):
    c = Counter((row[i], row[i+2]) for row in rows for i in range(N-2))
    return sum(v * (v-1) // 2 for v in c.values())


def main(argv):
    if len(argv) != 4:
        raise ValueError('usage: SCRIPT T1_INPUT PRODUCER_RESULT OUTPUT')
    source, producer, output = map(Path, argv[1:])
    raw, produced_raw = source.read_bytes(), producer.read_bytes()
    rows = json.loads(raw)['rows']
    alleged = json.loads(produced_raw)
    if (len(rows) != N or any(sorted(r) != list(range(N)) for r in rows)):
        raise ValueError('invalid rows')
    events = [(r[i], r[i+1]) for r in rows for i in range(N-1)]
    if len(set(events)) != N*(N-1):
        raise ValueError('source is not adjacency-exact')
    if len({r[0] for r in rows}) != N or len({r[-1] for r in rows}) != N:
        raise AssertionError('adjacency-exact source endpoints not distinct')
    initial = score(rows)
    expected = {tuple(x['removed_rows_1based']): x for x in alleged['per_pair']}
    records = []
    start = time.monotonic()
    minimum = initial
    for i, j in itertools.combinations(range(N), 2):
        a, b = successors(rows[i]), successors(rows[j])
        graph = [tuple(sorted({a[v], b[v]})) for v in range(12)]
        if any(len(x) != 2 for x in graph):
            raise AssertionError('rows share augmented arc')
        paths = 0
        decompositions = 0
        pair_min = initial
        fixed = [r for t, r in enumerate(rows) if t not in (i, j)]
        for first in enumerate_paths(graph):
            paths += 1
            chosen = successors(first)
            complement = [next(h for h in graph[v] if h != chosen[v]) for v in range(12)]
            second = remaining_path(complement)
            if second is None or first > second:
                continue
            decompositions += 1
            pair_min = min(pair_min, score(fixed + [first, second]))
        minimum = min(minimum, pair_min)
        exp = expected[(i+1, j+1)]
        if (decompositions != exp['hamilton_splits'] or
                pair_min != exp['best_d2_pair_collisions']):
            raise AssertionError('producer and independent exact pair scan differ')
        records.append({'rows_1based': [i+1, j+1], 'first_paths': paths,
                        'unordered_hamilton_splits': decompositions,
                        'minimum_d2_pair_collisions': pair_min})
    result = {'input_sha256': hashlib.sha256(raw).hexdigest(),
              'compared_result_sha256': hashlib.sha256(produced_raw).hexdigest(),
              'method': 'direct Hamilton-path DFS and complementary arc cycle; no matching-component enumeration',
              'pairs_checked': len(records),
              'hamilton_splits_checked': sum(r['unordered_hamilton_splits'] for r in records),
              'initial_d2_pair_collisions': initial, 'minimum_d2_pair_collisions': minimum,
              'every_pair_matches_producer': True, 'elapsed_ms': round((time.monotonic()-start)*1000),
              'per_pair': records,
              'scope': 'Only the exact two-row neighborhood of this T1 table; no global nonexistence.'}
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in ('pairs_checked','hamilton_splits_checked',
          'initial_d2_pair_collisions','minimum_d2_pair_collisions', 'every_pair_matches_producer','elapsed_ms')}))


if __name__ == '__main__':
    main(sys.argv)
