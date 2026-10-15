#!/usr/bin/env python3
"""Independent raw-subset audit of saved search misses; never an acceptance claim."""
import itertools
import json
import math
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
from verify import finite_certificate


def validate(table, identity):
    n = len(table)
    assert n > 0 and type(identity) is int and 0 <= identity < n
    assert all(len(row) == n and all(type(x) is int and 0 <= x < n for x in row) for row in table)
    assert all(table[identity][a] == a and table[a][identity] == a for a in range(n))
    assert all(any(table[a][b] == identity and table[b][a] == identity for b in range(n)) for a in range(n))
    assert all(table[table[a][b]][c] == table[a][table[b][c]]
               for a, b, c in itertools.product(range(n), repeat=3))


def independent_representation(name, table):
    if name == 'A4':
        elements = [p for p in itertools.permutations(range(4))
                    if sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0]
        multiply = lambda a, b: tuple(a[b[i]] for i in range(4))
    elif name == 'D7':
        elements = [tuple((a + (-x if b else x)) % 7 for x in range(7))
                    for b in range(2) for a in range(7)]
        multiply = lambda a, b: tuple(a[b[i]] for i in range(7))
    else:
        # A faithful realization of Dic_3 in GL(2,F_7).
        def multiply(a, b):
            return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % 7
                         for i in range(2) for j in range(2))
        r, s = (3, 0, 0, 5), (0, 1, 6, 0)
        powers = [(1, 0, 0, 1)]
        for _ in range(5):
            powers.append(multiply(powers[-1], r))
        elements = powers + [multiply(a, s) for a in powers]
    assert len(elements) == len(set(elements)) == len(table)
    index = {a: i for i, a in enumerate(elements)}
    expected = [[index[multiply(a, b)] for b in elements] for a in elements]
    assert table == expected


def dp_counts(table, sequence, length, identity):
    n = len(table)
    dp = [[0] * n for _ in range(length + 1)]
    dp[0][identity] = 1
    for a in sequence:
        for k in range(length, 0, -1):
            for g in range(n):
                dp[k][table[g][a]] += dp[k-1][g]
    return dp[length]


def audit(name):
    start = time.monotonic()
    path = Path(name + '-search-best.json')
    record = json.loads(path.read_text())
    table, e, sequence = record['table'], record['identity'], record['sequence']
    n = len(table)
    validate(table, e)
    independent_representation(name, table)
    assert len(sequence) == 2*n-1
    assert all(type(a) is int and 0 <= a < n for a in sequence)
    histogram = [0] * n
    first = []
    for indices in itertools.combinations(range(len(sequence)), n):
        product = e
        for index in indices:
            product = table[product][sequence[index]]
        histogram[product] += 1
        if product == e and len(first) < 5:
            first.append(list(indices))
    assert sum(histogram) == math.comb(len(sequence), n)
    assert histogram == dp_counts(table, sequence, n, e)
    assert histogram[e] == record['identity_subset_count']
    assert histogram[e] > 0, 'Candidate found: switch to the full resolution protocol'
    try:
        finite_certificate(path)
    except ValueError as error:
        rejection = str(error)
        assert rejection.startswith('Ordered identity witness exists: ')
    else:
        raise AssertionError('Frozen checker accepted a search miss')
    result = dict(group=name, group_order=n, sequence_length=len(sequence),
                  raw_subsets_checked=sum(histogram), product_histogram=histogram,
                  identity_subset_count=histogram[e], first_identity_indices_zero_based=first,
                  group_axioms_checked=True, independent_representation_agrees=True,
                  raw_dp_and_search_counts_agree=True, frozen_checker_rejection=rejection,
                  elapsed_seconds=time.monotonic()-start)
    print(json.dumps(result), flush=True)
    return result


if __name__ == '__main__':
    results = [audit(name) for name in ['Dic3', 'A4', 'D7']]
    d7 = json.loads(Path('D7-search-best.json').read_text())
    short = dict(table=d7['table'], identity=0, sequence=[1]*13+[7]*13)
    assert len(short['sequence']) == 26
    assert dp_counts(short['table'], short['sequence'], 14, 0)[0] == 0
    controls = Path('audit-controls')
    controls.mkdir(exist_ok=True)
    short_path = controls / 'one-short-D7.json'
    short_path.write_text(json.dumps(short) + '\n')
    try:
        finite_certificate(short_path)
    except ValueError as error:
        assert str(error) == 'Sequence length differs from 2|G|-1'
        control = dict(length=26, required_length=27, frozen_rejection=str(error),
                       identity_14_subsets_by_dp=0, counterexample=False)
    else:
        raise AssertionError('One-short word accepted')
    Path('raw-audit.json').write_text(json.dumps(dict(status='no_counterexample',
        exhaustive_group_sequence_coverage=False, results=results,
        one_short_control=control), indent=2) + '\n')
