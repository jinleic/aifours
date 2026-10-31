#!/usr/bin/env python3
"""Exact adjacency-preserving three-row replacements of one T1 square.

Remove three augmented Hamilton cycles. Enumerate EVERY Hamilton cycle in
those residual arcs; remove it, split the residual 2-regular bipartite graph
into matching-component orientations, and retain only two Hamilton cycles.
Every replacement triple appears, modulo row order. Only linear D2 events
are scored. The time cap may leave the scan incomplete, which is recorded;
a search failure is never a nonexistence proof. Zero-score tables must be
independently checked from their actual rows.
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
M = 12


def counts(rows, distance):
    return Counter((r[i], r[i + distance]) for r in rows for i in range(N - distance))


def pair_score(counter):
    return sum(v * (v - 1) // 2 for v in counter.values())


def excess(counter):
    return sum(v - 1 for v in counter.values() if v > 1)


def succ(row):
    nodes = [S] + list(row)
    out = [None] * M
    for a, b in zip(nodes, nodes[1:] + nodes[:1]):
        out[a] = b
    return out


def decode(perm):
    if len(set(perm)) != M:
        raise AssertionError('matching is not a permutation')
    row = []
    v = S
    seen = 1 << S
    for _ in range(N):
        v = perm[v]
        if seen & (1 << v):
            return None
        seen |= 1 << v
        row.append(v)
    if perm[v] != S:
        return None
    return tuple(row)


def all_hamilton_rows(adjacency):
    """Enumerate all residual Hamilton cycles, uniquely rooted at sentinel."""
    path = []
    def extend(v, remaining):
        if not remaining:
            if S in adjacency[v]:
                yield tuple(path)
            return
        for nxt in adjacency[v]:
            if remaining & (1 << nxt):
                path.append(nxt)
                yield from extend(nxt, remaining ^ (1 << nxt))
                path.pop()
    yield from extend(S, (1 << N) - 1)


def bipartite_split(adjacency):
    """Find one 1-factor and relative alternating components of 2-regular graph."""
    if any(len(vs) != 2 or vs[0] == vs[1] for vs in adjacency):
        raise AssertionError('expected two distinct residual arcs per vertex')
    match_head = [-1] * M
    def augment(v, seen):
        for h in adjacency[v]:
            if h in seen:
                continue
            seen.add(h)
            if match_head[h] == -1 or augment(match_head[h], seen):
                match_head[h] = v
                return True
        return False
    for v in range(M):
        if not augment(v, set()):
            raise AssertionError('2-regular bipartite graph has no perfect matching')
    p = [None] * M
    for h, v in enumerate(match_head):
        if v < 0:
            raise AssertionError('matching does not cover all heads')
        p[v] = h
    q = [next(h for h in adjacency[v] if h != p[v]) for v in range(M)]
    if len(set(p)) != M or len(set(q)) != M:
        raise AssertionError('matching complements not permutations')
    inverse = [None] * M
    for v, h in enumerate(p):
        inverse[h] = v
    relative = [inverse[q[v]] for v in range(M)]
    seen, components = set(), []
    for v in range(M):
        if v in seen:
            continue
        cycle, at = [], v
        while at not in seen:
            seen.add(at)
            cycle.append(at)
            at = relative[at]
        if at != v or len(cycle) < 2:
            raise AssertionError('bad alternating component')
        components.append(cycle)
    return p, q, components


def main(argv):
    if len(argv) != 4:
        raise ValueError('usage: SCRIPT T1_INPUT OUTPUT MAX_SECONDS')
    source, destination = Path(argv[1]), Path(argv[2])
    budget = float(argv[3])
    if budget <= 0:
        raise ValueError('MAX_SECONDS must be positive')
    raw = source.read_bytes()
    rows = json.loads(raw).get('rows')
    if (not isinstance(rows, list) or len(rows) != N or
            any(not isinstance(row, list) or len(row) != N or
                any(type(x) is not int for x in row) or sorted(row) != list(range(N))
                for row in rows)):
        raise ValueError('expected eleven permutations of 0..10')
    d1 = counts(rows, 1)
    if len(d1) != N * (N - 1) or any(v != 1 for v in d1.values()):
        raise ValueError('input does not cover every directed adjacency once')
    if len({r[0] for r in rows}) != N or len({r[-1] for r in rows}) != N:
        raise AssertionError('adjacency-exact array has repeated start or end')

    started = time.monotonic()
    deadline = started + budget
    original_score = pair_score(counts(rows, 2))
    best_score = original_score
    best_rows = [r[:] for r in rows]
    best_three = None
    complete_triples = 0
    first_cycles = 0
    orientation_representatives = 0
    decompositions = 0
    improving = 0
    per_triple = []
    cutoff = False
    witness_early_stop = False

    for i, j, k in itertools.combinations(range(N), 3):
        if time.monotonic() >= deadline:
            cutoff = True
            break
        original = [succ(rows[t]) for t in (i, j, k)]
        graph = [tuple(sorted(original[r][v] for r in range(3))) for v in range(M)]
        if any(len(set(heads)) != 3 for heads in graph):
            raise AssertionError('removed rows share an augmented arc')
        fixed = [row for r, row in enumerate(rows) if r not in (i, j, k)]
        fixed2 = counts(fixed, 2)
        entry = {'removed_rows_1based': [i + 1, j + 1, k + 1],
                 'first_hamilton_cycles': 0, 'orientation_representatives': 0,
                 'unordered_hamilton_decompositions': 0,
                 'best_d2_pair_collisions': original_score}
        for first in all_hamilton_rows(graph):
            first_cycles += 1
            entry['first_hamilton_cycles'] += 1
            if first_cycles % 128 == 0 and time.monotonic() >= deadline:
                cutoff = True
                break
            first_succ = succ(first)
            remainder = [tuple(h for h in graph[v] if h != first_succ[v]) for v in range(M)]
            p, q, components = bipartite_split(remainder)
            # Fix the first component's orientation: complementing all bits
            # only exchanges the second and third row.
            for mask in range(1 << (len(components) - 1)):
                orientation_representatives += 1
                entry['orientation_representatives'] += 1
                pp, qq = p[:], q[:]
                for ci in range(1, len(components)):
                    if mask & (1 << (ci - 1)):
                        for v in components[ci]:
                            pp[v], qq[v] = qq[v], pp[v]
                second, third = decode(pp), decode(qq)
                if second is None or third is None:
                    continue
                # Exactly one choice of first row represents an unordered
                # three-cycle decomposition; all cycles are distinct.
                if first > second or first > third:
                    continue
                decompositions += 1
                entry['unordered_hamilton_decompositions'] += 1
                combined = fixed2.copy()
                combined.update((r[c], r[c + 2]) for r in (first, second, third)
                                for c in range(N - 2))
                score = pair_score(combined)
                entry['best_d2_pair_collisions'] = min(entry['best_d2_pair_collisions'], score)
                if score < original_score:
                    improving += 1
                if score < best_score:
                    best_score = score
                    best_rows = [r[:] for r in rows]
                    best_rows[i], best_rows[j], best_rows[k] = map(list, (first, second, third))
                    best_three = [i + 1, j + 1, k + 1]
                if score == 0:
                    witness_early_stop = True
                    break
            if witness_early_stop:
                break
        if cutoff or witness_early_stop:
            break
        per_triple.append(entry)
        complete_triples += 1

    fd1, fd2 = counts(best_rows, 1), counts(best_rows, 2)
    if pair_score(fd1) != 0 or pair_score(fd2) != best_score:
        raise AssertionError('reconstructed output score mismatch')
    complete = not cutoff and not witness_early_stop and complete_triples == 165
    result = {
        'schema': 1, 'kind': 'adjacency_preserving_three_row_trades',
        'source': str(source), 'source_sha256': hashlib.sha256(raw).hexdigest(),
        'budget_seconds': budget, 'elapsed_ms': round((time.monotonic() - started) * 1000),
        'complete_neighborhood_scan': complete, 'budget_exhausted': cutoff,
        'witness_early_stop': witness_early_stop, 'row_triples_fully_scanned': complete_triples,
        'first_hamilton_cycles_visited': first_cycles,
        'orientation_representatives_checked': orientation_representatives,
        'unordered_hamilton_decompositions_checked': decompositions,
        'strict_improving_decompositions': improving,
        'initial_d2_pair_collisions': original_score, 'best_changed_rows_1based': best_three,
        'best_pair_collision_score': best_score, 'd1_pair_collisions': 0,
        'd2_pair_collisions': best_score, 'd1_excess_events': excess(fd1),
        'd2_excess_events': excess(fd2), 'zero_score_claim': best_score == 0,
        'rows': best_rows, 'per_completed_triple': per_triple,
        'scope': 'Only replacements of three slots of the pinned input, retaining the other eight and exact D1 coverage. No Latin or wrap condition. Failure is not global nonexistence.'
    }
    with destination.open('x', encoding='utf-8') as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({key: result[key] for key in (
        'complete_neighborhood_scan', 'budget_exhausted', 'witness_early_stop',
        'row_triples_fully_scanned', 'first_hamilton_cycles_visited',
        'orientation_representatives_checked', 'unordered_hamilton_decompositions_checked',
        'strict_improving_decompositions', 'initial_d2_pair_collisions',
        'best_pair_collision_score', 'best_changed_rows_1based', 'zero_score_claim', 'elapsed_ms')},
        sort_keys=True))


if __name__ == '__main__':
    main(sys.argv)
