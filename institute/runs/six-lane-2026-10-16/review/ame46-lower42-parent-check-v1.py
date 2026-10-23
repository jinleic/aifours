"""Independent parent verification of the finite binary-support/phase facts behind s>=42.
No worker imports. Enumerate support bitmasks, test all pair marginals directly, and recognize 2x2 blocks by
identical row-neighbour masks (not graph traversal). Produce exact integer phase-kernel certificates.
Coordinatewise increasing relabelling transports every binary certificate to every 2^4 subcube of [6]^4.
"""
import itertools
import json
import math
import subprocess
from collections import Counter
from pathlib import Path


def pop(x):
    return bin(x).count('1')


def bits(x, i):
    return (x >> i) & 1


def pair_value(x, pair):
    return 2 * bits(x, pair[0]) + bits(x, pair[1])


def uniform(S):
    for pair in itertools.combinations(range(4), 2):
        c = Counter(pair_value(x, pair) for x in S)
        if c != Counter({0: 2, 1: 2, 2: 2, 3: 2}):
            return False
    return True


def block_vectors(S, rowcoords, colcoords):
    at = {(pair_value(x, rowcoords), pair_value(x, colcoords)): x for x in S}
    neighbours = {r: sum(1 << c for rr, c in at if rr == r) for r in range(4)}
    groups = {}
    for r, mask in neighbours.items():
        if pop(mask) != 2:
            raise ValueError('non-two row degree')
        groups.setdefault(mask, []).append(r)
    if len(groups) != 2 or any(len(rs) != 2 for rs in groups.values()):
        raise ValueError('not two twin-row pairs')
    masks = list(groups)
    if masks[0] & masks[1] or masks[0] | masks[1] != 15:
        raise ValueError('blocks do not partition columns')
    out = []
    for mask, rs in sorted(groups.items()):
        cs = [c for c in range(4) if (mask >> c) & 1]
        r0, r1 = sorted(rs)
        c0, c1 = cs
        v = [0] * 16
        for r, c, sign in ((r0, c0, 1), (r0, c1, -1), (r1, c0, -1), (r1, c1, 1)):
            v[at[(r, c)]] = sign
        out.append(v)
    return out


def check_certificate(vectors, weights, rhs=None):
    if rhs is None:
        rhs = [1] * len(vectors)
    total = [sum(w * v[j] for v, w in zip(vectors, weights)) for j in range(16)]
    if any(total):
        raise ValueError('nonzero phase-coefficient sum')
    right = sum(w * r for w, r in zip(weights, rhs))
    if right % 2 != 1:
        raise ValueError('even phase RHS')
    return right


def obstruction(blocks):
    for chosen in itertools.product(*blocks):
        for s, t in itertools.product((-1, 1), repeat=2):
            w = (1, s, t)
            try:
                right = check_certificate(chosen, w)
            except ValueError:
                continue
            return chosen, w, right
    raise ValueError('no odd phase-kernel certificate')


def main():
    uniform_sets = [frozenset(c) for c in itertools.combinations(range(16), 8) if uniform(c)]
    expected = {frozenset(x for x in range(16) if pop(x & U) % 2 == c)
                for U in range(16) if pop(U) in (3, 4) for c in (0, 1)}
    if len(uniform_sets) != 10 or set(uniform_sets) != expected:
        raise ValueError('binary OA classification mismatch')
    reshapes = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    rows = []
    first = None
    for S in uniform_sets:
        blocks = [block_vectors(S, r, c) for r, c in reshapes]
        vec, weights, right = obstruction(blocks)
        if first is None:
            first = (S, vec, weights)
        rows.append({'support': sorted(S), 'blocks_per_reshape': [len(x) for x in blocks],
                     'phase_vectors': vec, 'weights': weights, 'odd_rhs': right})
    S, vec, weights = first
    controls = {}
    altered = [list(v) for v in vec]
    altered[0][next(j for j, v in enumerate(altered[0]) if v)] += 1
    try:
        check_certificate(altered, weights)
    except ValueError as e:
        controls['coefficient_corruption'] = str(e)
    try:
        check_certificate(vec, weights, [0, 1, 1])
    except ValueError as e:
        controls['RHS_corruption'] = str(e)
    # A zero linear combination of two identical valid block equations has even RHS, not a contradiction.
    try:
        check_certificate([vec[0], vec[0]], [1, -1])
    except ValueError as e:
        controls['consistent_duplicate_equations'] = str(e)
    mutant = set(S)
    mutant.remove(min(mutant))
    mutant.add(next(x for x in range(16) if x not in S))
    controls['support_corruption'] = 'nonuniform pair marginals' if not uniform(mutant) else 'UNEXPECTED-ACCEPT'
    wanted = {'coefficient_corruption': 'nonzero phase-coefficient sum',
              'RHS_corruption': 'even phase RHS', 'consistent_duplicate_equations': 'even phase RHS',
              'support_corruption': 'nonuniform pair marginals'}
    rec = {'recorded': subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip(),
           'subsets_enumerated': math.comb(16, 8), 'uniform_subsets': len(uniform_sets),
           'parity_types': {'weight3': 8, 'weight4': 2}, 'certificates': rows, 'controls': controls,
           'subcube_coverage': {'count': math.comb(6, 2) ** 4,
                               'method': 'Coordinatewise increasing bijections preserve all pair labels, twin-row blocks and the exact signed zero sums; no extra amplitude assumption.'},
           'verdict': 'PASS' if len(rows) == 10 and controls == wanted else 'FAIL'}
    with open(Path(__file__).with_suffix('.json'), 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({k: rec[k] for k in ('recorded', 'subsets_enumerated', 'uniform_subsets', 'controls', 'verdict')}))


if __name__ == '__main__':
    main()
