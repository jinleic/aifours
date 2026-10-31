#!/usr/bin/env python3
"""Independent finite controls for the written AME(4,6) proof review.

No author code is imported. Counts are necessary support conditions, not
assertions that every surviving Boolean support carries a complex unitary.
"""
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, product
from math import factorial
import json


def n5_control():
    # A is the 3-valued fiber coordinate; j is fixed in fiber j.
    singles = range(3)
    pairs = tuple(combinations(range(3), 2))
    choices = []
    for fixed in range(3):
        options = []
        for s, p, q in product(singles, pairs, pairs):
            seq = iter((p, q))
            options.append(tuple((s,) if f == fixed else next(seq) for f in range(3)))
        choices.append(options)
    hist = Counter()
    xor_fail = 0
    for specification in product(*choices):
        support = set()
        for f in range(3):
            for x in product(*(specification[j][f] for j in range(3))):
                support.add((f,) + x)
        assert len(support) == 12
        projections = {ij: {(w[ij[0]], w[ij[1]]) for w in support}
                       for ij in combinations(range(4), 2)}
        assert all(len(projections[0, j]) == 5 for j in (1, 2, 3))
        sizes = tuple(len(projections[ij]) for ij in ((1, 2), (1, 3), (2, 3)))
        hist[sizes] += 1
        eq = [specification[j][(j+1)%3] == specification[j][(j+2)%3] for j in range(3)]
        for j, k in combinations(range(3), 2):
            l = 3-j-k
            fixed_in_base = (specification[j][j][0] in specification[j][l] and
                             specification[k][k][0] in specification[k][l])
            pred = fixed_in_base and (eq[j] != eq[k])
            xor_fail += (len(projections[j+1, k+1]) == 5) != pred
    return {'normal_forms': sum(hist.values()), 'target_555': hist[5,5,5],
            'positive_control_556': hist[5,5,6], 'xor_discrepancies': xor_fail}


def bipartite(vertices):
    adj = {v: [] for v in vertices}
    for x, y in combinations(vertices, 2):
        if any(a == b for a, b in zip(x, y)):
            adj[x].append(y); adj[y].append(x)
    colors = {}
    for v in vertices:
        if v in colors: continue
        colors[v] = 0
        queue = deque([v])
        while queue:
            x = queue.popleft()
            for y in adj[x]:
                if y not in colors:
                    colors[y] = 1-colors[x]; queue.append(y)
                elif colors[y] == colors[x]:
                    return False
    return True


def n6_control(mixed):
    # Generate balanced 4-point fibers directly as subsets of the 2x2x2 cube.
    fibers = []
    for a in range(3):
        other = tuple(x for x in range(3) if x != a)
        alpha = ((0, 1), other, other) if mixed else (other, other, other)
        cube = tuple(product(*alpha))
        valid = [block for block in combinations(cube, 4)
                 if all(sum(x[j] == alpha[j][0] for x in block) == 2 for j in range(3))]
        fibers.append(valid)
    assert tuple(map(len, fibers)) == (8, 8, 8)
    result = Counter()
    for blocks in product(*fibers):
        result['total'] += 1
        words = {(a,) + x for a, block in enumerate(blocks) for x in block}
        proj = [Counter((w[i], w[j]) for w in words) for i, j in combinations(range(4), 2)]
        if any(len(p) != 6 for p in proj): continue
        result['all_pair_sizes_6'] += 1
        if any(set(p.values()) != {2} for p in proj): continue
        result['all_pair_degrees_2'] += 1
        if mixed:
            triples = {(w[0], w[2], w[3]) for w in words}
            fibered = (len(triples) == 6 and
                       all((a, b, c, d) in words for a, c, d in triples for b in (0, 1)))
            result['binary_fibered'] += fibered
            result['bipartite' if bipartite(triples) else 'odd_cycle'] += 1
    return dict(result)


def labelled_multiplicity(rows):
    v = factorial(len(rows))
    for count in Counter(rows).values(): v //= factorial(count)
    return v


def n_unitary_supports(n, excess):
    # Enumerate each multiset of row masks once, weighting by its labelings.
    masks = {d: tuple(sum(1 << j for j in ix) for ix in combinations(range(n), d))
             for d in (2, 3, 4) if d <= n}
    if excess == 0: groups = [(n, 0, 0)]
    elif excess == 1: groups = [(n-1, 1, 0)]
    else: groups = [(n-2, 2, 0), (n-1, 0, 1)]
    examined = survivors = multiset_count = 0
    block_failure = 0
    for counts in groups:
        its = [combinations_with_replacement(masks[d], count)
               if count else ((),) for d, count in zip((2, 3, 4), counts)]
        for grouped in product(*its):
            rows = sum(grouped, ())
            weight = labelled_multiplicity(rows)
            examined += weight; multiset_count += 1
            if any((a & b).bit_count() == 1 for a, b in combinations(rows, 2)): continue
            cols = tuple(sum((1 << i) for i, row in enumerate(rows) if (row >> j) & 1)
                         for j in range(n))
            if any(c.bit_count() < 2 for c in cols): continue
            if any((a & b).bit_count() == 1 for a, b in combinations(cols, 2)): continue
            survivors += weight
            if excess == 0:
                counts_by_mask = Counter(rows)
                block_ok = (all(c == 2 for c in counts_by_mask.values()) and
                            all((a & b) == 0 for a, b in combinations(counts_by_mask, 2)))
                if not block_ok: block_failure += weight
    return {'n': n, 'nnz': 2*n+excess, 'labelled_patterns_examined': examined,
            'row_multisets_examined': multiset_count, 'necessary_graph_survivors': survivors,
            'non_2x2_block_survivors_at_minimum': block_failure}


result = {'n5': n5_control(), 'n6_ternary': n6_control(False),
          'n6_one_binary': n6_control(True),
          'unitary_necessary_supports': [n_unitary_supports(n, excess)
                                          for n in (4, 6) for excess in (0, 1, 2)]}
print(json.dumps(result, indent=2, sort_keys=True))
