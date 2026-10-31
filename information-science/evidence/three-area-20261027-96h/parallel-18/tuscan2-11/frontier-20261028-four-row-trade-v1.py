#!/usr/bin/env python3
"""Bounded exact enumeration of adjacency-preserving four-row T1 trades.

For every selected four-row residual graph enumerate the first two Hamilton
cycles, then all matching-component splittings of the remaining 2-regular
bipartite graph. Row order is normalized only within the four replaced slots.
An incomplete/time-limited search is not a no-go. Any zero-score table needs
independent verification from its actual linear rows.
"""
import hashlib
import importlib.util
import itertools
import json
import sys
import time
from pathlib import Path

helper_path = Path(__file__).with_name('frontier-20261028-three-row-trade-v1.py')
spec = importlib.util.spec_from_file_location('frontier_three_row_helper', helper_path)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
N, M = helper.N, helper.M


def main(argv):
    if len(argv) != 4:
        raise ValueError('usage: SCRIPT T1_INPUT OUTPUT MAX_SECONDS')
    source, destination = Path(argv[1]), Path(argv[2])
    budget = float(argv[3])
    if budget <= 0:
        raise ValueError('MAX_SECONDS must be positive')
    raw = source.read_bytes()
    rows = json.loads(raw)['rows']
    if (len(rows) != N or any(not isinstance(r, list) or len(r) != N or
                              any(type(v) is not int for v in r) or
                              sorted(r) != list(range(N)) for r in rows)):
        raise ValueError('expected eleven permutations of 0..10')
    d1 = helper.counts(rows, 1)
    if len(d1) != N*(N-1) or any(v != 1 for v in d1.values()):
        raise ValueError('source does not have exact directed adjacency coverage')
    if len({r[0] for r in rows}) != N or len({r[-1] for r in rows}) != N:
        raise AssertionError('unexpected repeated endpoint')

    started = time.monotonic()
    deadline = started + budget
    initial = helper.pair_score(helper.counts(rows, 2))
    best, best_rows, best_group = initial, [r[:] for r in rows], None
    complete_groups = 0
    first_paths = second_paths = orientation_count = decompositions = 0
    improvements = 0
    stopped = False
    witness = False
    per_group = []
    for group in itertools.combinations(range(N), 4):
        if time.monotonic() >= deadline:
            stopped = True
            break
        arcs = [helper.succ(rows[t]) for t in group]
        graph = [tuple(sorted(arcs[r][v] for r in range(4))) for v in range(M)]
        if any(len(set(g)) != 4 for g in graph):
            raise AssertionError('removed rows share an augmented arc')
        fixed = [row for idx, row in enumerate(rows) if idx not in group]
        fixed_d2 = helper.counts(fixed, 2)
        data = {'removed_rows_1based': [t+1 for t in group], 'first_paths': 0,
                'second_paths': 0, 'orientation_representatives': 0,
                'unordered_hamilton_decompositions': 0, 'best_d2_pair_collisions': initial}
        for a in helper.all_hamilton_rows(graph):
            first_paths += 1
            data['first_paths'] += 1
            pa = helper.succ(a)
            graph3 = [tuple(h for h in graph[v] if h != pa[v]) for v in range(M)]
            for b in helper.all_hamilton_rows(graph3):
                second_paths += 1
                data['second_paths'] += 1
                if second_paths % 128 == 0 and time.monotonic() >= deadline:
                    stopped = True
                    break
                if a >= b:
                    continue
                pb = helper.succ(b)
                graph2 = [tuple(h for h in graph3[v] if h != pb[v]) for v in range(M)]
                p, q, components = helper.bipartite_split(graph2)
                for mask in range(1 << (len(components)-1)):
                    orientation_count += 1
                    data['orientation_representatives'] += 1
                    pp, qq = p[:], q[:]
                    for ci in range(1, len(components)):
                        if mask & (1 << (ci-1)):
                            for v in components[ci]:
                                pp[v], qq[v] = qq[v], pp[v]
                    c, d = helper.decode(pp), helper.decode(qq)
                    if c is None or d is None or b >= c or b >= d:
                        continue
                    decompositions += 1
                    data['unordered_hamilton_decompositions'] += 1
                    combined = fixed_d2.copy()
                    combined.update((r[i], r[i+2]) for r in (a, b, c, d)
                                    for i in range(N-2))
                    value = helper.pair_score(combined)
                    data['best_d2_pair_collisions'] = min(data['best_d2_pair_collisions'], value)
                    if value < initial:
                        improvements += 1
                    if value < best:
                        best, best_group = value, [t+1 for t in group]
                        best_rows = [r[:] for r in rows]
                        for index, new in zip(group, (a, b, c, d)):
                            best_rows[index] = list(new)
                    if value == 0:
                        witness = True
                        break
                if witness:
                    break
            if stopped or witness:
                break
        if stopped or witness:
            break
        complete_groups += 1
        per_group.append(data)

    fd1, fd2 = helper.counts(best_rows, 1), helper.counts(best_rows, 2)
    if helper.pair_score(fd1) != 0 or helper.pair_score(fd2) != best:
        raise AssertionError('candidate event score mismatch')
    out = {
        'schema': 1, 'kind': 'adjacency_preserving_four_row_trades',
        'source': str(source), 'source_sha256': hashlib.sha256(raw).hexdigest(),
        'helper_source_sha256': hashlib.sha256(helper_path.read_bytes()).hexdigest(),
        'budget_seconds': budget, 'elapsed_ms': round((time.monotonic()-started)*1000),
        'complete_neighborhood_scan': not stopped and not witness and complete_groups == 330,
        'budget_exhausted': stopped, 'witness_early_stop': witness,
        'row_quadruples_fully_scanned': complete_groups, 'first_cycles_visited': first_paths,
        'second_cycles_visited': second_paths, 'orientation_representatives_checked': orientation_count,
        'unordered_hamilton_decompositions_checked': decompositions,
        'strict_improving_decompositions': improvements,
        'initial_d2_pair_collisions': initial, 'best_changed_rows_1based': best_group,
        'best_pair_collision_score': best, 'd1_pair_collisions': 0, 'd2_pair_collisions': best,
        'd1_excess_events': helper.excess(fd1), 'd2_excess_events': helper.excess(fd2),
        'zero_score_claim': best == 0, 'rows': best_rows, 'per_completed_quadruple': per_group,
        'scope': 'Only this source table and scanned four-row replacements preserving all D1 events; no Latin, wrap or global nonexistence.'
    }
    with destination.open('x', encoding='utf-8') as stream:
        json.dump(out, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({key: out[key] for key in ('complete_neighborhood_scan','budget_exhausted',
        'witness_early_stop','row_quadruples_fully_scanned','first_cycles_visited',
        'second_cycles_visited','orientation_representatives_checked',
        'unordered_hamilton_decompositions_checked','strict_improving_decompositions',
        'initial_d2_pair_collisions','best_pair_collision_score','best_changed_rows_1based',
        'zero_score_claim','elapsed_ms')}, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv)
