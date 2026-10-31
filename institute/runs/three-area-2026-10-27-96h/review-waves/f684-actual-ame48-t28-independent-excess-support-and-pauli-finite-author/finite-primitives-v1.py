#!/usr/bin/env python3
"""Prospective local-primitive assay; not a full AME search or phase witness.

Standard library only. No stdin, network, subprocess, or explicit file I/O.
Cooperative deadline 50 s from import; parent must provide the separate 55 s
external supervision and audit these exact source bytes before any one run.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import sys
import time

START = time.monotonic()
LIMIT = 50.0
PAIRS = tuple(combinations(range(4), 2))
CUTS = ((0, 1), (0, 2), (0, 3))


class CheckFailure(Exception):
    pass


class GuardRejection(Exception):
    pass


class Deadline(Exception):
    pass


def tick():
    if time.monotonic() - START >= LIMIT:
        raise Deadline()


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def expect_rejection(name, wanted, action):
    try:
        action()
    except GuardRejection as exc:
        require(str(exc) == wanted, name + ': wrong rejection reason ' + str(exc))
        print('CONTROL_REJECT', name, wanted, 'SYNTHETIC_NOT_ACTUAL_COUNTEREXAMPLE')
        return
    raise CheckFailure(name + ': guard accepted its targeted bad input')


def component_sets(mask):
    """All bipartite components, including isolated rows/columns."""
    n = len(mask)
    require(all(len(row) == n for row in mask), 'non-square support mask')
    adjacency = [set() for _ in range(2 * n)]
    for r in range(n):
        for c in range(n):
            if mask[r][c]:
                adjacency[r].add(n + c)
                adjacency[n + c].add(r)
    unseen = set(range(2 * n))
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        nodes = {start}
        while stack:
            v = stack.pop()
            for neighbor in adjacency[v]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    nodes.add(neighbor)
                    stack.append(neighbor)
        result.append((frozenset(v for v in nodes if v < n),
                       frozenset(v - n for v in nodes if v >= n)))
    return result


def degree_profile(mask):
    n = len(mask)
    return (tuple(sorted(sum(row) for row in mask)),
            tuple(sorted(sum(mask[r][c] for r in range(n)) for c in range(n))))


def single_overlaps(mask):
    n = len(mask)
    found = []
    for a, b in combinations(range(n), 2):
        if sum(mask[a][c] and mask[b][c] for c in range(n)) == 1:
            found.append(('rows', a, b))
        if sum(mask[r][a] and mask[r][b] for r in range(n)) == 1:
            found.append(('columns', a, b))
    return found


def strict_positive_balance(mask):
    """Exact equivalence: every support edge lies in a perfect matching."""
    n = len(mask)
    covered = set()
    for p in permutations(range(n)):
        if all(mask[r][p[r]] for r in range(n)):
            covered.update((r, p[r]) for r in range(n))
    return all(not mask[r][c] or (r, c) in covered
               for r in range(n) for c in range(n))


def edge_mask(n, positions):
    chosen = set(positions)
    return tuple(tuple(int(n * r + c in chosen) for c in range(n))
                 for r in range(n))


def supports():
    observed = {}
    for n, ones in ((3, 8), (4, 12)):
        seen = 0
        passed = Counter()
        for edges in combinations(range(n * n), ones):
            tick()
            seen += 1
            mask = edge_mask(n, edges)
            rows, cols = degree_profile(mask)
            if min(rows + cols) < 2:
                continue
            if not strict_positive_balance(mask):
                continue
            if single_overlaps(mask):
                continue
            if len(component_sets(mask)) != 1:
                continue
            passed[(rows, cols)] += 1
            if n == 4:
                if rows == (3, 3, 3, 3) and cols == (3, 3, 3, 3):
                    for r in range(4):
                        require(sum(1 - x for x in mask[r]) == 1,
                                'regular support row missing count')
                    for c in range(4):
                        require(sum(1 - mask[r][c] for r in range(4)) == 1,
                                'regular support column missing count')
                elif rows == (2, 2, 4, 4):
                    low = [r for r in range(4) if sum(mask[r]) == 2]
                    require(len(low) == 2 and
                            all(not (mask[low[0]][c] and mask[low[1]][c])
                                for c in range(4)), 'mixed row pair not disjoint')
                elif cols == (2, 2, 4, 4):
                    low = [c for c in range(4) if sum(mask[r][c] for r in range(4)) == 2]
                    require(len(low) == 2 and
                            all(not (mask[r][low[0]] and mask[r][low[1]])
                                for r in range(4)), 'mixed column pair not disjoint')
                else:
                    raise CheckFailure('unexpected 4x4 degree shape')
        if n == 3:
            expected = {((2, 3, 3), (2, 3, 3)): 9}
            require(seen == 9 and dict(passed) == expected, '3x3 support census')
        else:
            regular = (3, 3, 3, 3)
            mixed = (2, 2, 4, 4)
            expected = {(regular, regular): 24, (mixed, regular): 36,
                        (regular, mixed): 36}
            require(seen == 1820 and dict(passed) == expected, '4x4 support census')
        observed[n] = (seen, sum(passed.values()))
        print('SUPPORT_CENSUS', n, 'examined', seen, 'admissible', sum(passed.values()),
              'degree_classes', sorted(passed.items()))
    return observed


def gram_integer(matrix, norm):
    n = len(matrix)
    require(all(len(row) == n for row in matrix), 'integer example is not square')
    for i in range(n):
        for j in range(n):
            value = sum(matrix[i][k] * matrix[j][k] for k in range(n))
            require(value == (norm if i == j else 0), 'integer Gram identity')


def unitary_examples():
    a = ((15, 12, 16), (-20, 9, 12), (0, -20, 15))
    b = ((15, 20, 0, 0), (0, 0, 15, 20),
         (-12, 9, -16, 12), (16, -12, -12, 9))
    c = ((0, 1, 1, 1), (1, 0, 1, -1),
         (1, -1, 0, 1), (1, 1, -1, 0))
    gram_integer(a, 625)
    gram_integer(b, 625)
    gram_integer(c, 3)
    require(sum(x != 0 for row in a for x in row) == 8, '3x3 example support')
    require(sum(x != 0 for row in b for x in row) == 12, '4x4 example support')
    require(sum(x != 0 for row in c for x in row) == 12, 'conference support')
    require(degree_profile(tuple(tuple(int(x != 0) for x in row) for row in b)) ==
            ((2, 2, 4, 4), (3, 3, 3, 3)), 'mixed example degrees')
    print('UNITARY_EXAMPLES', 'A/25 B/25, C/sqrt(3); integer Gram exact')
    return b


def cubes():
    vertices = tuple(product(range(2), repeat=3))
    q_histogram = Counter()
    five_max = 0
    counts = Counter()
    for size in (5, 6, 7):
        for chosen in combinations(vertices, size):
            tick()
            counts[size] += 1
            chosen = frozenset(chosen)
            faces = [(sum(v[i] == 0 for v in chosen), sum(v[i] == 1 for v in chosen))
                     for i in range(3)]
            edge_counts = []
            for i in range(3):
                edges = 0
                for v in chosen:
                    if v[i] == 0:
                        other = tuple(1 if j == i else v[j] for j in range(3))
                        edges += other in chosen
                edge_counts.append(edges)
            if size == 5:
                five_max = max(five_max, sum(edge_counts))
                require(all(x >= 1 for x in edge_counts), 'five cube missing directional edge')
                require(any(x == 1 for x in edge_counts), 'five cube lacks single overlap')
            elif size == 7:
                require(all(sorted(f) == [3, 4] for f in faces), 'seven cube face pattern')
            else:
                missing = sorted(set(vertices) - chosen)
                require(len(missing) == 2, 'six cube missing count')
                q_dirs = tuple(i for i in range(3) if missing[0][i] == missing[1][i])
                q_histogram[len(q_dirs)] += 1
                for i in range(3):
                    expected = [2, 4] if i in q_dirs else [3, 3]
                    require(sorted(faces[i]) == expected, 'six cube D/Q face mismatch')
                require(len(q_dirs) <= 2, 'three Q directions in six cube')
                if len(q_dirs) == 2:
                    d = next(i for i in range(3) if i not in q_dirs)
                    corners = {tuple(v[i] for i in q_dirs) for v in chosen}
                    require(len(corners) == 3, 'two-Q cube missing three corners')
                    require(all(sum(tuple(v[i] for i in q_dirs) == corner for v in chosen) == 2
                                for corner in corners), 'two-Q cube is not product')
                    require(all({v[d] for v in chosen
                                 if tuple(v[i] for i in q_dirs) == corner} == {0, 1}
                                for corner in corners), 'two-Q cube not both D values')
    require(dict(counts) == {5: 56, 6: 28, 7: 8}, 'cube census size')
    require(five_max == 5, 'five cube edge maximum')
    require(dict(q_histogram) == {0: 4, 1: 12, 2: 12}, 'six cube Q census')
    print('CUBE_CENSUS', sorted(counts.items()), 'five_max_edges', five_max,
          'six_Q_directions', sorted(q_histogram.items()), 'seven_faces', '3/4')


def dq_colorings():
    edges = tuple(combinations(range(4), 2))
    complement = {e: tuple(v for v in range(4) if v not in e) for e in edges}
    valid = []
    for flags in product((0, 1), repeat=6):
        tick()
        q = {e for e, flag in zip(edges, flags) if flag}
        if any(e in q and complement[e] in q for e in edges):
            continue
        valid.append(q)
    require(len(valid) == 27, 'K4 complementary-Q census')
    cases3444 = Counter()
    cases3344 = Counter()
    for q in valid:
        qdeg = [sum(v in e for e in q) for v in range(4)]
        if max(qdeg) <= 2:
            reached = {0}
            while True:
                grown = reached | {v for u in reached for v in range(4) if u != v and
                                   tuple(sorted((u, v))) not in q}
                if grown == reached:
                    break
                reached = grown
            require(len(reached) == 4, 'all-q4 D graph disconnected')
        if all(qdeg[v] <= 2 for v in (1, 2, 3)):
            d_edges = [e for e in combinations((1, 2, 3), 2) if e not in q]
            cases3444[len(d_edges)] += 1
            if not d_edges:
                require(all((0, v) not in q for v in (1, 2, 3)),
                        '3444 Q triangle has a Q edge to q3')
            if len(d_edges) == 1:
                isolated = next(v for v in (1, 2, 3) if v not in d_edges[0])
                require((0, isolated) not in q, '3444 isolated q4 lacks D to q3')
        if qdeg[2] <= 2 and qdeg[3] <= 2:
            if (2, 3) in q:
                require((0, 1) not in q, '3344 complementary Q')
                cases3344['CD_Q_AB_D'] += 1
            else:
                a_allq = (0, 2) in q and (0, 3) in q
                b_allq = (1, 2) in q and (1, 3) in q
                require(not (a_allq and b_allq), '3344 both q3 have two cross Q')
                if a_allq:
                    require((1, 2) not in q and (1, 3) not in q,
                            '3344 complement forces B cross D')
                if b_allq:
                    require((0, 2) not in q and (0, 3) not in q,
                            '3344 complement forces A cross D')
                cases3344['CD_D_one_all_Q' if a_allq or b_allq
                          else 'CD_D_each_has_D'] += 1
    print('K4_CENSUS', len(valid), '3444_induced_D_counts', sorted(cases3444.items()),
          '3344_cross_cases', sorted(cases3344.items()))


def pauli_mul(p, q):
    cyclic = {('X', 'Y'): 'Z', ('Y', 'Z'): 'X', ('Z', 'X'): 'Y'}
    result = []
    exponent = 0
    for a, b in zip(p, q):
        if a == 'I':
            result.append(b)
        elif b == 'I':
            result.append(a)
        elif a == b:
            result.append('I')
        elif (a, b) in cyclic:
            result.append(cyclic[(a, b)])
            exponent = (exponent + 1) % 4
        else:
            result.append(cyclic[(b, a)])
            exponent = (exponent + 3) % 4
    return tuple(result), exponent


def paulis():
    strings = tuple(product('XYZ', repeat=3))
    weights = Counter()
    for p in strings:
        for q in strings:
            tick()
            pq, ep = pauli_mul(p, q)
            qp, eq = pauli_mul(q, p)
            weight = sum(x != 'I' for x in pq)
            weights[weight] += 1
            require(pq == qp, 'Pauli product words differ under reversal')
            if weight == 3:
                require((ep - eq) % 4 == 2, 'weight-3 anticommutator nonzero')
            if p == q:
                require(weight == 0 and ep == 0, 'Pauli square')
    require(dict(weights) == {0: 27, 1: 162, 2: 324, 3: 216},
            'ordered Pauli weight census')
    # (I+M)^2=(denominator/2)(I+M) after rho^2=rho/2.
    coeff = (Fraction(2) - Fraction(8, 2), Fraction(1) - Fraction(8, 2))
    require(coeff == (Fraction(-2), Fraction(-3)), 'three-qubit normalization')
    print('PAULI_CENSUS', len(strings), 'ordered_products', sum(weights.values()),
          'weight_counts', sorted(weights.items()),
          'weight3_anticommutators_zero', 'rho=(I+M)/8; M^2-2M-3I=0')


def pair_counts(words, pair):
    i, j = pair
    return Counter((w[i], w[j]) for w in words)


def flat_mask(words, left):
    right = tuple(i for i in range(4) if i not in left)
    rows = sorted({tuple(w[i] for i in left) for w in words})
    cols = sorted({tuple(w[i] for i in right) for w in words})
    require(len(rows) == len(cols), 'flat mask not square')
    ri = {x: i for i, x in enumerate(rows)}
    ci = {x: i for i, x in enumerate(cols)}
    n = len(rows)
    mask = [[0] * n for _ in range(n)]
    for w in words:
        a = tuple(w[i] for i in left)
        b = tuple(w[i] for i in right)
        require(mask[ri[a]][ci[b]] == 0, 'duplicate word in cut')
        mask[ri[a]][ci[b]] = 1
    return tuple(tuple(row) for row in mask), rows, cols


def binary_block_guard(block, whole):
    for pair in PAIRS:
        local = pair_counts(block, pair)
        total = pair_counts(whole, pair)
        for value in product(range(2), repeat=2):
            if local[value] == 0 or local[value] != total[value]:
                raise GuardRejection('BLOCK_PAIR_EXTENSION_NOT_EXHAUSTED')


def models():
    cube3 = tuple(product(range(2), repeat=3))
    full_parity = frozenset([(0,) + v for v in cube3] +
                            [(1,) + v for v in cube3 if sum(v) % 2 == 0])
    all4 = frozenset(product(range(2), repeat=4))
    removed = frozenset((a, b, a ^ b, a) for a, b in product(range(2), repeat=2))
    sector = all4 - removed
    outside = frozenset(tuple(2 + x for x in w) for w in all4 if sum(w) % 2 == 0)
    require(len(full_parity) == len(sector) == 12 and len(outside) == 8,
            'synthetic model sizes')
    require(all(sum(w[i] == v for w in sector) == 6
                for i in range(4) for v in range(2)), 'sector incidence six')
    artifacts = []
    for name, block in (('FULL_CUBE_PLUS_PARITY', full_parity), ('BALANCED_SECTOR', sector)):
        tick()
        whole = block | outside
        require(len(whole) == 20, 'synthetic model union')
        binary_block_guard(block, whole)
        pair_types = []
        for pair in PAIRS:
            local = pair_counts(block, pair)
            profile = sorted(local.values())
            require(profile in ([2, 2, 4, 4], [3, 3, 3, 3]),
                    name + ' block pair profile')
            whole_profile = sorted(pair_counts(whole, pair).values())
            require(whole_profile in ([2, 2, 2, 2, 3, 3, 3, 3],
                                      [2, 2, 2, 2, 2, 2, 4, 4]),
                    name + ' global synthetic pair profile')
            pair_types.append(('Q' if profile == [2, 2, 4, 4] else 'D'))
        for left in CUTS:
            mask, rows, cols = flat_mask(whole, left)
            require(len(rows) == 8 and len(cols) == 8, name + ' cut dimensions')
            require(not single_overlaps(mask), name + ' one-overlap synthetic cut')
            comps = component_sets(mask)
            require(sorted((len(r), len(c)) for r, c in comps) ==
                    [(2, 2), (2, 2), (4, 4)], name + ' cut component census')
            br = frozenset(i for i, value in enumerate(rows) if all(x < 2 for x in value))
            bc = frozenset(i for i, value in enumerate(cols) if all(x < 2 for x in value))
            require(len(br) == len(bc) == 4 and (br, bc) in comps,
                    name + ' binary block not an entire cut component')
            require(sum(mask[r][c] for r in br for c in bc) == 12,
                    name + ' binary component does not have 12 entries')
        print('SYNTHETIC_SUPPORT_MODEL', name, 'words', len(whole),
              'binary_block', len(block), 'pair_types', ''.join(pair_types),
              'all_six_extensions_exhausted', 'all_three_cut_components_closed',
              'NO_AME_AMPLITUDES_CONSTRUCTED')
        artifacts.append((block, whole))
    return artifacts[0]


def coverage_guard(mask, components):
    n = len(mask)
    rows = set().union(*(set(r) for r, _ in components)) if components else set()
    cols = set().union(*(set(c) for _, c in components)) if components else set()
    if rows != set(range(n)) or cols != set(range(n)):
        raise GuardRejection('MISSED_COMPONENT')


def overlap_guard(mask):
    if single_overlaps(mask):
        raise GuardRejection('ONE_OVERLAP')


def balance_guard(mask):
    if not strict_positive_balance(mask):
        raise GuardRejection('NO_STRICT_POSITIVE_BALANCE')


def normalization_guard(denominator):
    if denominator != 8:
        raise GuardRejection('WRONG_THREE_QUBIT_NORMALIZATION')


def complement_q_guard(q):
    if any(tuple(v for v in range(4) if v not in e) in q for e in q):
        raise GuardRejection('COMPLEMENTARY_Q')


def two_term_guard(matrix, r, s):
    size = sum(matrix[r][c] != 0 and matrix[s][c] != 0 for c in range(len(matrix)))
    if size != 2:
        raise GuardRejection('OVERLAP_NOT_TWO_TERMS')


def scope_guard(claim):
    if claim != 'LOCAL_PRIMITIVES_ONLY_EXACT_T28_TARGET':
        raise GuardRejection('GLOBAL_MINIMUM_OR_ALL_SUPPORT_NOT_AUTHORIZED')


def controls(example, model):
    block, whole = model
    mask, _, _ = flat_mask(whole, (0, 1))
    comps = component_sets(mask)
    largest = max(comps, key=lambda c: len(c[0]))
    coverage_guard(mask, comps)
    expect_rejection('missedcomponent', 'MISSED_COMPONENT',
                     lambda: coverage_guard(mask, [largest]))
    one = ((1, 1, 0), (0, 1, 1), (1, 1, 1))
    expect_rejection('oneoverlap', 'ONE_OVERLAP', lambda: overlap_guard(one))
    unbalanced = ((1, 1, 0, 0), (1, 1, 0, 0),
                  (1, 1, 1, 1), (0, 0, 1, 1))
    expect_rejection('unbalanced', 'NO_STRICT_POSITIVE_BALANCE',
                     lambda: balance_guard(unbalanced))
    normalization_guard(8)
    expect_rejection('wrong4qubitnormalization', 'WRONG_THREE_QUBIT_NORMALIZATION',
                     lambda: normalization_guard(4))
    expect_rejection('complementQ', 'COMPLEMENTARY_Q',
                     lambda: complement_q_guard({(0, 1), (2, 3)}))
    contaminated = whole | {(0, 0, 2, 3)}
    expect_rejection('isolatedblockmissingexternalextension', 'BLOCK_PAIR_EXTENSION_NOT_EXHAUSTED',
                     lambda: binary_block_guard(block, contaminated))
    terms = [example[2][c] * example[3][c] for c in range(4)]
    require(all(terms) and sum(terms) == 0, 'four-term complex-unitary example')
    expect_rejection('false2termreduction', 'OVERLAP_NOT_TWO_TERMS',
                     lambda: two_term_guard(example, 2, 3))
    scope_guard('LOCAL_PRIMITIVES_ONLY_EXACT_T28_TARGET')
    expect_rejection('falseglobalminimumscope', 'GLOBAL_MINIMUM_OR_ALL_SUPPORT_NOT_AUTHORIZED',
                     lambda: scope_guard('GLOBAL_MINIMUM'))


def main():
    print('START local primitives only; cooperative 50s; no global tensor enumeration')
    supports()
    example = unitary_examples()
    cubes()
    dq_colorings()
    paulis()
    model = models()
    controls(example, model)
    tick()
    print('LOCAL_PRIMITIVES_PASS', 'GLOBAL_CASE_ENUMERATION_NOTTESTED',
          'AME_PHASE_WITNESS_NOTTESTED', 'ALL_SUPPORT_OR_MINIMUM_NOTTESTED',
          'PARENT_REVIEW_AND_GO_SEPARATE')


if __name__ == '__main__':
    try:
        main()
    except Deadline:
        print('INCOMPLETE cooperative_50s_deadline; no pass claimed')
        sys.exit(2)
    except CheckFailure as exc:
        print('FAIL local_primitive_check', str(exc), '; no pass claimed')
        sys.exit(1)
    except Exception as exc:
        print('ERROR unexpected', type(exc).__name__, str(exc), '; no pass claimed')
        sys.exit(1)
