#!/usr/bin/env python3
"""Independently verify three-row T1 trades using only direct path DFS.

For each removed triple, enumerate a first Hamilton cycle, then every second
Hamilton cycle in its remaining arcs; the third is the uniquely complementary
arc set. Lexicographic ordering removes all row permutations. No matching
component decomposition from the producer is used.
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
    path = []
    def walk(v, unused):
        if not unused:
            if S in graph[v]:
                yield tuple(path)
            return
        for nxt in graph[v]:
            if unused & (1 << nxt):
                path.append(nxt)
                yield from walk(nxt, unused ^ (1 << nxt))
                path.pop()
    yield from walk(S, (1 << N) - 1)


def decode(succ):
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
    if len(rows) != N or any(sorted(row) != list(range(N)) for row in rows):
        raise ValueError('invalid rows')
    events = [(r[i], r[i+1]) for r in rows for i in range(N-1)]
    if len(set(events)) != N*(N-1):
        raise ValueError('source is not adjacency-exact')
    if len({r[0] for r in rows}) != N or len({r[-1] for r in rows}) != N:
        raise AssertionError('adjacency-exact source endpoints not distinct')
    if not alleged['complete_neighborhood_scan']:
        raise ValueError('producer did not complete its neighborhood scan')
    initial = score(rows)
    expected = {tuple(x['removed_rows_1based']): x for x in alleged['per_completed_triple']}
    start = time.monotonic()
    records = []
    minimum = initial
    for i, j, k in itertools.combinations(range(N), 3):
        arcs = [successors(rows[t]) for t in (i, j, k)]
        graph = [tuple(sorted({arcs[r][v] for r in range(3)})) for v in range(12)]
        if any(len(x) != 3 for x in graph):
            raise AssertionError('rows share an augmented arc')
        paths = 0
        decompositions = 0
        triple_min = initial
        fixed = [r for t, r in enumerate(rows) if t not in (i, j, k)]
        for first in enumerate_paths(graph):
            paths += 1
            p = successors(first)
            remain = [tuple(h for h in graph[v] if h != p[v]) for v in range(12)]
            for second in enumerate_paths(remain):
                if first >= second:
                    continue
                q = successors(second)
                last = [next(h for h in remain[v] if h != q[v]) for v in range(12)]
                third = decode(last)
                if third is None or second >= third:
                    continue
                decompositions += 1
                triple_min = min(triple_min, score(fixed + [first, second, third]))
        minimum = min(minimum, triple_min)
        exp = expected[(i+1, j+1, k+1)]
        if (paths != exp['first_hamilton_cycles'] or
                decompositions != exp['unordered_hamilton_decompositions'] or
                triple_min != exp['best_d2_pair_collisions']):
            raise AssertionError(f'producer and independent triple scan differ: {(i+1,j+1,k+1)}')
        records.append({'rows_1based': [i+1, j+1, k+1], 'first_paths': paths,
                        'unordered_hamilton_decompositions': decompositions,
                        'minimum_d2_pair_collisions': triple_min})
    result = {'input_sha256': hashlib.sha256(raw).hexdigest(),
              'compared_result_sha256': hashlib.sha256(produced_raw).hexdigest(),
              'method': 'nested direct Hamilton-path DFS plus unique complement; no matching components',
              'triples_checked': len(records),
              'first_paths_checked': sum(r['first_paths'] for r in records),
              'hamilton_decompositions_checked': sum(r['unordered_hamilton_decompositions'] for r in records),
              'initial_d2_pair_collisions': initial, 'minimum_d2_pair_collisions': minimum,
              'every_triple_matches_producer': True, 'elapsed_ms': round((time.monotonic()-start)*1000),
              'per_triple': records,
              'scope': 'Only the exact three-row neighborhood of this T1 table; no global nonexistence.'}
    with output.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in ('triples_checked','first_paths_checked',
          'hamilton_decompositions_checked','initial_d2_pair_collisions',
          'minimum_d2_pair_collisions','every_triple_matches_producer','elapsed_ms')}))


if __name__ == '__main__':
    main(sys.argv)
