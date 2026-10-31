#!/usr/bin/env python3
"""Independent exact finite checks of selected AME(4,6) residual lemmas.

The n=5 and n=6 support spaces are generated from their written fiber normal
forms, not from author/reviewer data or code. These computations do not prove
that the normal forms cover all AME states, or prove Tarry's theorem.
"""
import hashlib
import itertools
import json
import subprocess
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/ame46-support')
INPUTS = {
    'lower42': ('frontier-20261028-global-ame46-lower42-review-packet-v2.md',
                '50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf'),
    'lower44': ('frontier-20261028-global-ame46-support-lower44-v1.md',
                '89e2de23d4777697bd4e2b55e5925f3bd50f5f07c2e0e18aeb548ddd70052a30'),
}
PAIRS = tuple(itertools.combinations(range(4), 2))


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, capture_output=True, text=True).stdout.strip()


def projections(words):
    return [Counter((w[a], w[b]) for w in words) for a, b in PAIRS]


def valid_projections(words, n, minimum):
    return all(len(c) == n and all(v >= minimum for v in c.values())
               for c in projections(words))


def n5_fiber(a):
    # The A=a fiber fixes coordinate a and contains the full product of two
    # independent two-element alphabets on the other coordinates.
    alphabets = tuple(itertools.combinations(range(3), 2))
    variable = [j for j in range(3) if j != a]
    for singleton in range(3):
        for left, right in itertools.product(alphabets, repeat=2):
            fiber = []
            for x, y in itertools.product(left, right):
                word = [a, None, None, None]
                word[1 + a] = singleton
                word[1 + variable[0]] = x
                word[1 + variable[1]] = y
                fiber.append(tuple(word))
            yield tuple(fiber)


def is_bipartite(vertices):
    adjacency = {v: [] for v in vertices}
    for u, v in itertools.combinations(vertices, 2):
        if any(a == b for a, b in zip(u, v)):
            adjacency[u].append(v)
            adjacency[v].append(u)
    color = {}
    for root in vertices:
        if root in color:
            continue
        color[root] = 0
        todo = deque([root])
        while todo:
            u = todo.popleft()
            for v in adjacency[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    todo.append(v)
                elif color[v] == color[u]:
                    return False
    return True


def n6_words(binary_patterns, binary_party):
    # Each four-word A-fiber has balanced binary variables. For a ternary
    # coordinate, normalize its missing value to the A-fiber label.
    out = []
    for a, pattern in enumerate(binary_patterns):
        available = [tuple(v for v in range(3) if v != a)] * 3
        if binary_party is not None:
            available[binary_party] = (0, 1)
        for b in pattern:
            out.append((a,) + tuple(available[j][b[j]] for j in range(3)))
    return tuple(out)


def graph_survivors(n, excess):
    masks2 = tuple(sum(1 << i for i in c)
                   for c in itertools.combinations(range(n), 2))
    masks3 = tuple(sum(1 << i for i in c)
                   for c in itertools.combinations(range(n), 3))
    checked = survivors = 0
    for exceptional in (range(n) if excess else (None,)):
        choices = [masks3 if row == exceptional else masks2 for row in range(n)]
        for rows in itertools.product(*choices):
            checked += 1
            if any((rows[i] & rows[j]).bit_count() == 1
                   for i in range(n) for j in range(i)):
                continue
            cols = tuple(sum(((rows[i] >> j) & 1) << i for i in range(n))
                         for j in range(n))
            if any(c.bit_count() < 2 for c in cols):
                continue
            if any((cols[i] & cols[j]).bit_count() == 1
                   for i in range(n) for j in range(i)):
                continue
            survivors += 1
    return {'labeled_patterns': checked, 'necessary_graph_survivors': survivors}


def orthogonal(matrix):
    n = len(matrix)
    return all(sum(matrix[i][k] * matrix[j][k] for k in range(n)) == int(i == j)
               for i in range(n) for j in range(n))


def main():
    started = clock()
    pins = {}
    for name, (filename, expected) in INPUTS.items():
        digest = hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()
        if digest != expected:
            raise ValueError('SOURCE_HASH_MISMATCH: ' + name)
        pins[name] = digest
    out_path = HERE / 'parent-residual-normalforms-result-v1.json'
    if out_path.exists():
        raise FileExistsError(out_path)

    fibers = [tuple(n5_fiber(i)) for i in range(3)]
    n5_count = n5_cardinality_five = n5_valid = relaxed_556 = 0
    for f0, f1, f2 in itertools.product(*fibers):
        words = f0 + f1 + f2
        counts = projections(words)
        n5_count += 1
        n5_cardinality_five += all(len(c) == 5 for c in counts)
        n5_valid += all(len(c) == 5 and min(c.values()) >= 2 for c in counts)
        relaxed_556 += tuple(len(c) for c in counts[3:]) == (5, 5, 6)

    bits = tuple(itertools.product(range(2), repeat=3))
    balanced = tuple(combo for combo in itertools.combinations(bits, 4)
                     if all(sum(w[j] for w in combo) == 2 for j in range(3)))
    n6_stats = {}
    mixed_example = None
    for label, binary in [('all_ternary', None), ('one_binary', 0)]:
        checked = good = odd = bipartite = 0
        for triple in itertools.product(balanced, repeat=3):
            words = n6_words(triple, binary)
            checked += 1
            if not valid_projections(words, 6, 2):
                continue
            good += 1
            if binary is not None:
                mixed_example = words
                vertices = sorted({(w[0], w[2], w[3]) for w in words})
                if len(vertices) != 6:
                    raise AssertionError('MIXED_TRIPLE_COUNT')
                if set(words) != {(a, b, c, d) for a, c, d in vertices for b in (0, 1)}:
                    raise AssertionError('MIXED_NOT_BINARY_FREE')
                if is_bipartite(vertices):
                    bipartite += 1
                else:
                    odd += 1
        n6_stats[label] = {'fiber_configurations': checked, 'all_pairs_valid': good,
                           'odd_graphs': odd, 'bipartite_graphs': bipartite}

    graphs = {str(n): {str(extra): graph_survivors(n, extra) for extra in (0, 1)}
              for n in (3, 4, 5)}
    Q = Fraction
    u3 = [[Q(3, 5), Q(4, 5), Q(0)],
          [Q(-12, 25), Q(9, 25), Q(4, 5)],
          [Q(16, 25), Q(-12, 25), Q(3, 5)]]
    if n5_count != 19683 or n5_cardinality_five or n5_valid:
        raise AssertionError('N5_NORMALFORM_CONTRADICTION_NOT_REPRODUCED')
    if len(balanced) != 8 or n6_stats['all_ternary']['all_pairs_valid'] != 0:
        raise AssertionError('N6_TERNARY_CONTROL')
    if n6_stats['one_binary'] != {'fiber_configurations': 512, 'all_pairs_valid': 4,
                                  'odd_graphs': 3, 'bipartite_graphs': 1}:
        raise AssertionError('N6_MIXED_CONTROL')
    if not orthogonal(u3) or sum(v != 0 for row in u3 for v in row) != 8:
        raise AssertionError('THREE_BY_THREE_POSITIVE_CONTROL')
    if mixed_example is None or valid_projections(mixed_example[:-1], 6, 2):
        raise AssertionError('DROPPED_TUPLE_CONTROL')
    if any(graphs[str(n)]['1']['necessary_graph_survivors'] != 0 for n in (3, 4, 5)):
        raise AssertionError('ONE_EXCESS_GRAPH_CONTROL')

    result = {
        'kind': 'PARENT_INDEPENDENT_RESIDUAL_NORMALFORM_CHECK',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'candidate_sha256': pins,
        'n5': {'fiber_options': [len(x) for x in fibers],
               'fiber_combinations': n5_count,
               'all_six_projections_size_five': n5_cardinality_five,
               'all_six_projection_sizes_and_extensions_valid': n5_valid,
               'remaining_pair_sizes_5_5_6': relaxed_556},
        'n6': n6_stats,
        'unitary_support_necessary_graphs': graphs,
        'controls': {'rational_orthogonal_3x3_eight_nonzeros': 'PASS',
                     'remove_tuple_from_valid_mixed_support': 'rejected',
                     'one_excess_n3_n4_n5': 'zero necessary graph survivors'},
        'limits': 'Finite normal-form controls only. No proof of the normal-form '
                  'reduction, unitary realizability of graph survivors, Tarry, '
                  'universal AME bound, novelty, human or kernel verification.',
    }
    with out_path.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
