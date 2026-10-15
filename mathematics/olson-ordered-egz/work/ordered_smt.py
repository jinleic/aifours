#!/usr/bin/env python3
"""Bounded existential ordered-word search, with a monotone Horn encoding.

The solver carries (prefix, selected length, right-ordered product). It never
permutes selected entries. UNKNOWN is not UNSAT. A model is independently
checked by raw subset enumeration before reporting a counterexample candidate.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import time
import z3


def semidirect_c3_c4():
    elements = list(itertools.product(range(3), range(4)))
    index = {g: i for i, g in enumerate(elements)}
    table = [[index[((a + (-1 if b % 2 else 1) * c) % 3, (b + d) % 4)]
              for c, d in elements] for a, b in elements]
    return elements, table, 0


def alternating4():
    def even(p):
        return sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2 == 0
    elements = [p for p in itertools.permutations(range(4)) if even(p)]
    index = {p: i for i, p in enumerate(elements)}
    table = [[index[tuple(a[b[i]] for i in range(4))] for b in elements] for a in elements]
    return elements, table, 0


def check_group(table, e):
    n = len(table)
    assert all(len(row) == n and set(row) == set(range(n)) for row in table)
    assert all(table[e][a] == a and table[a][e] == a for a in range(n))
    assert all(any(table[a][b] == e and table[b][a] == e for b in range(n)) for a in range(n))
    assert all(table[table[a][b]][c] == table[a][table[b][c]]
               for a, b, c in itertools.product(range(n), repeat=3))


def raw_histogram(table, e, word, selected):
    counts = [0] * len(table)
    for indices in itertools.combinations(range(len(word)), selected):
        product = e
        for i in indices:
            product = table[product][word[i]]
        counts[product] += 1
    assert sum(counts) == math.comb(len(word), selected)
    return counts


def dp_products(table, e, word, selected):
    layers = [{e}] + [set() for _ in range(selected)]
    for a in word:
        for k in range(selected, 0, -1):
            layers[k].update(table[g][a] for g in layers[k - 1])
    return layers[selected]


def solve(table, e, length, selected, milliseconds, fixed_word=None):
    n = len(table)
    solver = z3.SolverFor('QF_FD')
    solver.set(timeout=milliseconds, max_memory=3072)
    choice = [[z3.Bool(f'x_{i}_{a}') for a in range(n)] for i in range(length)]
    for row in choice:
        solver.add(z3.PbEq([(b, 1) for b in row], 1))
    reach = {}
    def r(t, k, g):
        # States unable to attain the final selected length are irrelevant.
        if k < max(0, selected - (length - t)) or k > min(t, selected):
            return z3.BoolVal(False)
        key = t, k, g
        if key not in reach:
            reach[key] = z3.Bool(f'r_{t}_{k}_{g}')
        return reach[key]
    solver.add(r(0, 0, e))
    for t in range(length):
        for k in range(max(0, selected - (length - t)), min(t, selected) + 1):
            for g in range(n):
                previous = r(t, k, g)
                if k >= max(0, selected - (length - t - 1)):
                    solver.add(z3.Implies(previous, r(t + 1, k, g)))
                if k < selected:
                    for a in range(n):
                        solver.add(z3.Implies(z3.And(previous, choice[t][a]),
                                              r(t + 1, k + 1, table[g][a])))
    solver.add(z3.Not(r(length, selected, e)))
    if fixed_word is not None:
        assert len(fixed_word) == length
        for i, a in enumerate(fixed_word):
            solver.add(choice[i][a])
    started = time.monotonic()
    answer = solver.check()
    elapsed = time.monotonic() - started
    record = {'answer': str(answer), 'solver_seconds': elapsed,
              'timeout_ms': milliseconds, 'reachable_variables': len(reach),
              'sequence_length': length, 'selected_length': selected,
              'reason_unknown': solver.reason_unknown() if answer == z3.unknown else None}
    if answer == z3.sat:
        model = solver.model()
        word = [next(a for a in range(n) if z3.is_true(model.eval(choice[i][a])))
                for i in range(length)]
        histogram = raw_histogram(table, e, word, selected)
        assert histogram[e] == 0, 'SAT model fails independent raw enumeration'
        assert dp_products(table, e, word, selected) == {g for g, count in enumerate(histogram) if count}
        record.update(sequence=word, raw_subset_count=sum(histogram), product_histogram=histogram)
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('group', choices=['C3rtC4', 'A4'])
    parser.add_argument('--seconds', type=int, default=180)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    elements, table, e = semidirect_c3_c4() if args.group == 'C3rtC4' else alternating4()
    check_group(table, e)
    n = len(table)
    controls = []
    if args.group == 'C3rtC4':
        a, b = elements.index((1, 0)), elements.index((0, 1))
        short_word = [a] * (n - 1) + [b] * (n - 1)
        short = solve(table, e, len(short_word), n, 5000, short_word)
        assert short['answer'] == 'sat'
        controls.append({'kind': 'one-short-known-extremal', **short})
        extended = solve(table, e, 2 * n - 1, n, 5000, short_word + [e])
        assert extended['answer'] == 'unsat'
        controls.append({'kind': 'identity-extension-positive-witness', **extended})
    result = {'schema': 'ordered-olson-smt/1', 'group': args.group, 'elements': elements,
              'table': table, 'identity': e, 'z3_version': z3.get_version_string(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'scope': 'One fixed finite group; only SAT plus independently verified witness refutes full conjecture',
              'controls': controls, 'search': solve(table, e, 2 * n - 1, n, args.seconds * 1000)}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'group': args.group, 'controls': [c['answer'] for c in controls],
                      'search': result['search']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
