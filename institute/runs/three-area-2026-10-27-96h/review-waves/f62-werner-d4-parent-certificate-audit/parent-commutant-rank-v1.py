#!/usr/bin/env python3
"""Fresh stdlib modular replay of actual four-replica commutant witnesses.

Necessary integer commutator constraints plus independent permutation columns
have complementary rank lower bounds; the written rank sandwich is separate.
Imports no author/reviewer matrix, elimination, permutation or data loader.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path

DATA = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-local-commutant-pivot-rows.json')
EXPECTED = '1cf37f5429892ac7a8da6fe6a90ad2fb2259a692887b1368e3329ffecc9fbbb4'
OUT = Path(__file__).with_name('parent-commutant-rank-result-v1.json')


def rank(vectors, modulus):
    pivots = {}
    for vector in vectors:
        v = {k: x % modulus for k, x in vector.items() if x % modulus}
        while v:
            k = max(v)
            if k not in pivots:
                inv = pow(v[k], -1, modulus)
                pivots[k] = {j: x * inv % modulus for j, x in v.items()}
                break
            coefficient = v[k]
            for j, value in pivots[k].items():
                z = (v.get(j, 0) - coefficient * value) % modulus
                if z:
                    v[j] = z
                else:
                    v.pop(j, None)
    return len(pivots)


def weights(x, n):
    return tuple(x.count(i) for i in range(n))


def check_case(case, prime):
    n = case['dimension']
    if n not in (2, 4) or case['replicas'] != 4 or case['modulus'] != prime:
        raise ValueError('TARGET')
    basis = list(itertools.product(range(n), repeat=4))
    pairs = [(x, y) for x in basis for y in basis if weights(x, n) == weights(y, n)]
    index = {xy: k for k, xy in enumerate(pairs)}
    expected = (70, 56, 14) if n == 2 else (2716, 2692, 24)
    if len(pairs) != expected[0]:
        raise ValueError('UNKNOWN_COUNT')
    rows = []
    labels = []
    for i, j, raw_x, raw_y in case['witness_rows']:
        x, y = tuple(raw_x), tuple(raw_y)
        if i == j or i not in range(n) or j not in range(n) or x not in basis or y not in basis:
            raise ValueError('ROW_LABEL')
        wy = list(weights(y, n));wy[i] += 1;wy[j] -= 1
        if weights(x, n) != tuple(wy):
            raise ValueError('ROW_WEIGHT')
        label = (i, j, x, y)
        if label in labels:
            raise ValueError('DUPLICATE_ROW')
        labels.append(label)
        row = collections.Counter()
        for pos, value in enumerate(y):
            if value == j:
                changed = list(y);changed[pos] = i
                row[index[(x, tuple(changed))]] += 1
        for pos, value in enumerate(x):
            if value == i:
                changed = list(x);changed[pos] = j
                row[index[(tuple(changed), y)]] -= 1
        rows.append({k: v for k, v in row.items() if v})
    if len(rows) != expected[1]:
        raise ValueError('ROW_COUNT')
    # Build all actual permutation matrices on the actual four-replica basis.
    permutation_columns = []
    for permutation in itertools.permutations(range(4)):
        col = {}
        for y in basis:
            x = tuple(y[permutation[j]] for j in range(4))
            col[index[(x, y)]] = 1
        permutation_columns.append(col)
    annihilations = 0
    for row in rows:
        for col in permutation_columns:
            if sum(c for k, c in row.items() if k in col) != 0:
                raise ValueError('INTEGER_PERMUTATION_ANNIHILATION')
            annihilations += 1
    constraint_rank = rank(reversed(rows), prime)
    permutation_rank = rank(reversed(permutation_columns), prime)
    if (len(pairs), constraint_rank, permutation_rank) != expected:
        raise ValueError('RANK')
    control = None
    if n == 2:
        control = rank(rows[:-1] + [rows[0]], prime)
        if control != expected[1] - 1:
            raise ValueError('DUPLICATE_CONTROL')
    return {'dimension': n, 'replicas': 4, 'same_weight_unknowns': len(pairs),
            'selected_constraint_rows': len(rows), 'constraint_rank_mod_prime': constraint_rank,
            'permutation_span_rank_mod_prime': permutation_rank,
            'all_selected_rows_annihilate_all_24_permutations_over_integers': True,
            'integer_annihilation_checks': annihilations,
            'ranks_sum_to_unknowns': constraint_rank + permutation_rank == len(pairs),
            'duplicate_row_control_rank': control}


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    raw = DATA.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED:
        raise ValueError('INPUT_HASH')
    obj = json.loads(raw)
    p = obj['prime']
    if p != 65521 or any(p % d == 0 for d in range(2, int(p ** 0.5) + 1)):
        raise ValueError('PRIME')
    cases = obj['cases']
    if len(cases) != 2 or {c['dimension'] for c in cases} != {2, 4}:
        raise ValueError('DIMENSION_SET')
    result = {'verdict': 'PASS', 'input_sha256': digest, 'prime': p,
              'cases': [check_case(c, p) for c in cases],
              'method': 'New stdlib actual-basis/commutator/permutation construction and reverse-row/max-pivot modular elimination; no other checker imported.',
              'scope': 'Finite rank lower bounds for n=2,4 four-replica source commutants. The mathematical derivative/rank-sandwich and physical theorem are separate obligations.'}
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with OUT.open('x', encoding='utf-8') as f:
        f.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
