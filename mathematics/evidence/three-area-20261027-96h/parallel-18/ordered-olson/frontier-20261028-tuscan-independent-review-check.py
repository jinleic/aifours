#!/usr/bin/env python3
"""Independently reconstruct two Tuscan-2(11) candidate obstructions.

The source files are read as bytes once and SHA-pinned. No author checker or
solver code is imported. Bounds are tiny for these two explicit candidates.
"""

import argparse
from collections import defaultdict
import hashlib
import itertools
import json


N = 11
EXPECTED_FIRST = '5a941a6c3f6fa3b65a9f9d1972eb70e94c55b6cb11b72ee41baf7d3f4707be05'
EXPECTED_SECOND = '99ec9dc0b9970fbd282d07330cf03d3cc1d217fb3c2de2299759b9dfd3c69c29'
FIXED_IDS = (2, 3, 6, 7, 8, 11)  # one-based author labels
FIXED_LITERAL = [
    [6,9,2,4,7,1,8,5,0,10,3],
    [4,10,7,2,1,0,3,5,9,8,6],
    [8,0,2,9,6,1,3,7,10,4,5],
    [10,8,1,4,6,2,5,3,9,7,0],
    [9,1,10,2,0,4,8,3,6,5,7],
    [3,10,0,8,2,7,5,6,4,1,9],
]


def read_rows(path, expected):
    with open(path, 'rb') as stream:
        raw = stream.read()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('source SHA mismatch')
    rows = json.loads(raw)['rows']
    validate_rows(rows)
    return rows


def validate_rows(rows):
    if not isinstance(rows, list) or len(rows) != N:
        raise ValueError('wrong row count')
    for row in rows:
        if not isinstance(row, list) or len(row) != N:
            raise ValueError('wrong row length')
        if any(not isinstance(x, int) or isinstance(x, bool) or x < 0 or x >= N for x in row):
            raise ValueError('out-of-range or noninteger symbol')
        if len(set(row)) != N:
            raise ValueError('row is not a permutation')
    if len({tuple(row) for row in rows}) != N:
        raise ValueError('duplicate source rows')


def events(row, distance):
    return {(row[i], row[i+distance]) for i in range(N-distance)}


def profile(rows, endpoints):
    seen = [defaultdict(list), defaultdict(list)]
    conflicts = defaultdict(list)
    for rid, row in enumerate(rows, 1):
        for distance in (1, 2):
            for event in events(row, distance):
                seen[distance-1][event].append(rid)
    for distance in (1, 2):
        for event, locations in seen[distance-1].items():
            for a, b in itertools.combinations(locations, 2):
                conflicts[(a, b)].append({'kind': 'distance_' + str(distance), 'event': event})
    if endpoints:
        for a, b in itertools.combinations(range(N), 2):
            if rows[a][0] == rows[b][0]:
                conflicts[(a+1, b+1)].append({'kind': 'same_first', 'symbol': rows[a][0]})
            if rows[a][-1] == rows[b][-1]:
                conflicts[(a+1, b+1)].append({'kind': 'same_last', 'symbol': rows[a][-1]})
    return seen, conflicts


def vertex_covers(edges, max_size):
    examined = 0
    minimum = None
    solutions = []
    vertices = range(1, N+1)
    for size in range(max_size+1):
        for chosen in itertools.combinations(vertices, size):
            examined += 1
            selected = set(chosen)
            if all(a in selected or b in selected for a, b in edges):
                if minimum is None:
                    minimum = size
                if size == minimum:
                    solutions.append(chosen)
    return {'subsets_examined': examined, 'minimum_size': minimum, 'minimum_covers': solutions}


def independent_subsets(edges, size):
    result = []
    for chosen in itertools.combinations(range(1, N+1), size):
        selected = set(chosen)
        if all(not (a in selected and b in selected) for a, b in edges):
            result.append(chosen)
    return result


def enumerate_compatible(fixed):
    forbidden1 = set().union(*(events(row, 1) for row in fixed))
    forbidden2 = set().union(*(events(row, 2) for row in fixed))
    firsts = {row[0] for row in fixed}
    lasts = {row[-1] for row in fixed}
    nodes = 0
    results = []

    def visit(prefix, remaining):
        nonlocal nodes
        nodes += 1
        if not remaining:
            if prefix[-1] not in lasts:
                results.append(tuple(prefix))
            return
        for symbol in remaining:
            if not prefix and symbol in firsts:
                continue
            if len(prefix) == N-1 and symbol in lasts:
                continue
            if prefix and (prefix[-1], symbol) in forbidden1:
                continue
            if len(prefix) >= 2 and (prefix[-2], symbol) in forbidden2:
                continue
            visit(prefix + [symbol], remaining - {symbol})

    visit([], set(range(N)))
    possible_events = set(forbidden1)
    for row in results:
        possible_events.update(events(row, 1))
    universe = {(a, b) for a in range(N) for b in range(N) if a != b}
    return {'prefix_nodes_in_this_implementation': nodes,
            'eligible_rows_count': len(results), 'eligible_rows': sorted(results),
            'fixed_adjacency_events': len(forbidden1),
            'fixed_distance2_events': len(forbidden2),
            'unused_and_unsupported_adjacencies': sorted(universe - possible_events),
            'fixed_starts': sorted(firsts), 'fixed_ends': sorted(lasts)}


def intended_mutation_error(rows, transform, expected):
    changed = [row.copy() for row in rows]
    transform(changed)
    try:
        validate_rows(changed)
    except ValueError as exc:
        if str(exc) == expected:
            return expected
        raise ValueError('mutation failed for unintended reason: ' + str(exc)) from exc
    raise ValueError('invalid mutation unexpectedly passed')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('first')
    parser.add_argument('second')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    first = read_rows(args.first, EXPECTED_FIRST)
    second = read_rows(args.second, EXPECTED_SECOND)

    first_seen, first_conflicts = profile(first, False)
    covers_first = vertex_covers(sorted(first_conflicts), 4)
    for cover in covers_first['minimum_covers']:
        kept = [row for i, row in enumerate(first, 1) if i not in cover]
        for distance in (1, 2):
            all_events = [pair for row in kept for pair in events(row, distance)]
            if len(all_events) != len(set(all_events)):
                raise ValueError('first-candidate cover leaves collision')

    second_seen, second_conflicts = profile(second, True)
    covers_second = vertex_covers(sorted(second_conflicts), 5)
    independent_sixes = independent_subsets(sorted(second_conflicts), 6)
    fixed = [second[i-1] for i in FIXED_IDS]
    if fixed != FIXED_LITERAL:
        raise ValueError('six-row literal does not match pinned source')
    for distance in (1, 2):
        all_events = [pair for row in fixed for pair in events(row, distance)]
        if len(all_events) != len(set(all_events)):
            raise ValueError('fixed six already violate event condition')
    if len({row[0] for row in fixed}) != 6 or len({row[-1] for row in fixed}) != 6:
        raise ValueError('fixed six violate necessary endpoint condition')
    completion = enumerate_compatible(fixed)
    for row in completion['eligible_rows']:
        if sorted(row) != list(range(N)):
            raise ValueError('backtracking produced non-permutation')
        if (events(row, 1) & set().union(*(events(x, 1) for x in fixed)) or
                events(row, 2) & set().union(*(events(x, 2) for x in fixed))):
            raise ValueError('backtracking produced forbidden event')

    mutation_results = [
        intended_mutation_error(first, lambda x: x[0].__setitem__(0, x[0][1]), 'row is not a permutation'),
        intended_mutation_error(first, lambda x: x[0].__setitem__(0, N), 'out-of-range or noninteger symbol'),
        intended_mutation_error(first, lambda x: x.__setitem__(0, x[1].copy()), 'duplicate source rows'),
    ]
    payload = {
        'result': 'INDEPENDENT_FINITE_RECONSTRUCTION',
        'inputs': {'first_sha256': EXPECTED_FIRST, 'second_sha256': EXPECTED_SECOND},
        'first_candidate': {
            'distinct_d1': len(first_seen[0]), 'distinct_d2': len(first_seen[1]),
            'event_conflict_edges_one_based': sorted(first_conflicts), 'cover_enumeration': covers_first,
        },
        'second_candidate': {
            'distinct_d1': len(second_seen[0]), 'distinct_d2': len(second_seen[1]),
            'event_and_endpoint_conflicts_one_based': sorted(second_conflicts),
            'cover_enumeration': covers_second, 'conflict_free_six_row_sets': independent_sixes,
            'fixed_row_ids_one_based': FIXED_IDS, 'fixed_rows': fixed, 'completion': completion,
        },
        'mutation_controls_intended_reasons': mutation_results,
        'scope': 'only the two pinned candidate arrays and this six-row subset; not a global T2(11) solver',
    }
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(payload, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': payload['result'],
                      'first_distinct': [len(first_seen[0]), len(first_seen[1])],
                      'first_conflict_edges': sorted(first_conflicts),
                      'first_minimum_cover': covers_first['minimum_size'],
                      'first_minimum_covers': covers_first['minimum_covers'],
                      'second_distinct': [len(second_seen[0]), len(second_seen[1])],
                      'second_cover_through_five_examined': covers_second['subsets_examined'],
                      'second_conflict_free_sixes': independent_sixes,
                      'compatible_rows': completion['eligible_rows_count'],
                      'independent_prefix_nodes': completion['prefix_nodes_in_this_implementation'],
                      'unsupported_adjacencies': completion['unused_and_unsupported_adjacencies'],
                      'mutations': mutation_results, 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()
