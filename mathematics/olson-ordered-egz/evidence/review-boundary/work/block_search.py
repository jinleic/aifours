#!/usr/bin/env python3
"""Exact bounded construction search; no generic word-space brute force.

For each constant-run word, enumerate selected counts per run. This is exact
for that word because an increasing-index selection has precisely such counts.
Each found identity witness is verified again by multiplying its actual letters.
A missing witness is independently checked on all raw increasing-index subsets.
"""
import hashlib
import itertools
import json
from pathlib import Path
import time
from ordered_smt import alternating4, semidirect_c3_c4, check_group, raw_histogram

ROOT = Path(__file__).resolve().parents[1]


def powers(table, e, n):
    result = []
    for a in range(n):
        row = [e]
        for _ in range(n):
            row.append(table[row[-1]][a])
        result.append(row)
    return result


def selections(capacities, selected):
    if len(capacities) == 1:
        if 0 <= selected <= capacities[0]:
            yield (selected,)
        return
    low = max(0, selected - sum(capacities[1:]))
    high = min(capacities[0], selected)
    for k in range(low, high + 1):
        for rest in selections(capacities[1:], selected - k):
            yield (k,) + rest


def identity_selection(table, e, pw, letters, choices):
    for chosen in choices:
        value = e
        for a, count in zip(letters, chosen):
            value = table[value][pw[a][count]]
        if value == e:
            return chosen
    return None


def verify_positive(table, e, letters, capacities, chosen, n):
    assert len(chosen) == len(letters) == len(capacities)
    assert sum(chosen) == n
    assert all(0 <= x <= cap for x, cap in zip(chosen, capacities))
    value = e
    for a, count in zip(letters, chosen):
        for _ in range(count):
            value = table[value][a]
    assert value == e


def search(group_name, factory):
    elements, table, e = factory()
    check_group(table, e)
    n = len(table)
    pw = powers(table, e, n)
    coverage, checked, skipped_by_multiplicity = hashlib.sha256(), 0, 0
    start = time.monotonic()
    for first in range(1, n):
        for second in range(1, n):
            third = 2 * n - 1 - first - second
            if not 1 <= third < n:
                continue
            capacities = (first, second, third)
            choices = tuple(selections(capacities, n))
            for a, b, c in itertools.product(range(n), repeat=3):
                if a == b or b == c:
                    # Adjacent equal runs merge; the resulting two-run word has
                    # some letter occurring at least n times, so is immediate.
                    skipped_by_multiplicity += 1
                    continue
                chosen = identity_selection(table, e, pw, (a, b, c), choices)
                if chosen is None:
                    word = [a] * first + [b] * second + [c] * third
                    histogram = raw_histogram(table, e, word, n)
                    assert histogram[e] == 0
                    return {'group': group_name, 'counterexample': {'table': table, 'identity': e,
                            'sequence': word, 'raw_histogram': histogram}}
                verify_positive(table, e, (a, b, c), capacities, chosen, n)
                checked += 1
                coverage.update(bytes((a, b, c) + capacities + chosen))
    return {'group': group_name, 'group_order': n, 'word_length': 2 * n - 1,
            'scope': 'All words with at most three constant runs; unrestricted words NOT covered',
            'nontrivial_three_run_words_checked': checked,
            'adjacent_equal_parameterizations_trivial': skipped_by_multiplicity,
            'words_with_any_run_at_least_n': 'Trivial by n identical entries and Lagrange',
            'witness_transcript_sha256': coverage.hexdigest(),
            'elapsed_seconds': time.monotonic() - start,
            'counterexample': None}


def main():
    result = {'schema': 'olson-three-run-search/1',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'records': [search('A4', alternating4), search('C3rtC4', semidirect_c3_c4)]}
    (ROOT / 'evidence' / 'three-run-search.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
