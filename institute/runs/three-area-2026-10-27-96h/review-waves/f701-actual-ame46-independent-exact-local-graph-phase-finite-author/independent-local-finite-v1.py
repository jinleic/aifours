#!/usr/bin/env python3
"""UNEXECUTED AUTHOR SOURCE. Local necessary conditions only; not an AME solver.

No inputs, file access, network, subprocesses, deletion, randomness, or asserts.
Parent must statically review, pin, admit and supervise before running.  The
45-second deadline and signals produce INCOMPLETE, never a scientific pass.
"""
from collections import Counter, deque
from itertools import combinations, product
from math import gcd
import json
import signal
import sys
import time

PAIRS = tuple(combinations(range(4), 2))
CUTS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
STOP_SIGNAL = None
DEADLINE = 0.0


class Incomplete(Exception):
    pass


class CheckFailure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def signal_stop(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def checkpoint():
    if STOP_SIGNAL is not None:
        raise Incomplete('signal_' + str(STOP_SIGNAL))
    if time.monotonic() >= DEADLINE:
        raise Incomplete('cooperative_45_second_deadline')


def bit(word, party):
    return (word >> party) & 1


def parity(word):
    return bin(word).count('1') % 2


def pair_value(word, parties):
    return tuple(bit(word, party) for party in parties)


def pair_cap(words):
    for pair in PAIRS:
        counts = Counter(pair_value(word, pair) for word in words)
        if any(count > 2 for count in counts.values()):
            return False
    return True


def line_neighbours(words, cut, side):
    first, second = cut if side == 0 else (cut[1], cut[0])
    neighbours = {}
    for word in words:
        line = pair_value(word, first)
        opposite = pair_value(word, second)
        neighbours.setdefault(line, set()).add(opposite)
    return neighbours


def has_one_overlap(words):
    for cut in CUTS:
        for side in (0, 1):
            groups = list(line_neighbours(words, cut, side).values())
            for left, right in combinations(groups, 2):
                if len(left & right) == 1:
                    return True
    return False


def full_two_by_two_blocks(words, cut):
    rows = line_neighbours(words, cut, 0)
    cols = line_neighbours(words, cut, 1)
    universe = set(product(range(2), repeat=2))
    if set(rows) != universe or set(cols) != universe:
        return False
    if any(len(v) != 2 for v in rows.values()):
        return False
    if any(len(v) != 2 for v in cols.values()):
        return False
    unseen = set(rows)
    components = 0
    while unseen:
        row = next(iter(unseen))
        cs = rows[row]
        rs = {r for r in rows if rows[r] == cs}
        if len(rs) != 2 or any(cols[c] != rs for c in cs):
            return False
        unseen.difference_update(rs)
        components += 1
    return components == 2


def binary_box_issue(words):
    if not pair_cap(words):
        return 'PAIR_CAP'
    if has_one_overlap(words):
        return 'ONE_OVERLAP'
    for pair in PAIRS:
        counts = Counter(pair_value(word, pair) for word in words)
        if len(counts) != 4 or any(v != 2 for v in counts.values()):
            return 'PAIR_MULTIPLICITY'
    if any(not full_two_by_two_blocks(words, cut) for cut in CUTS):
        return 'CUT_BLOCKS'
    return None


def combine_line_values(cut, row, column):
    result = 0
    for party, value in zip(cut[0], row):
        result |= value << party
    for party, value in zip(cut[1], column):
        result |= value << party
    return result


def forcing_witnesses(words):
    witnesses = []
    for cut in CUTS:
        rows = line_neighbours(words, cut, 0)
        for incomplete, one in rows.items():
            if len(one) != 1:
                continue
            for complete, two in rows.items():
                if incomplete != complete and len(two) == 2 and len(one & two) == 1:
                    other = next(iter(two - one))
                    forced = combine_line_values(cut, incomplete, other)
                    witnesses.append((cut, incomplete, forced))
    return witnesses


def check_binary_box():
    parity_classes = [frozenset(w for w in range(16) if parity(w) == p)
                      for p in (0, 1)]
    three_face_unions = set()
    face_presentations = 0
    for cls in parity_classes:
        for parties in combinations(range(4), 3):
            for values in product(range(2), repeat=3):
                faces = [{w for w in cls if bit(w, p) == v}
                         for p, v in zip(parties, values)]
                require(all(len(face) == 4 for face in faces), 'FACE_SIZE')
                union = frozenset().union(*faces)
                require(len(union) == 7, 'THREE_FACE_UNION_SIZE')
                three_face_unions.add(union)
                face_presentations += 1
    require(face_presentations == 64 and len(three_face_unions) == 16,
            'THREE_FACE_COVERAGE')

    subset_counts = []
    for cls in parity_classes:
        ordered = sorted(cls)
        seven = []
        for mask in range(256):
            subset = frozenset(ordered[i] for i in range(8) if mask & (1 << i))
            if len(subset) == 7:
                seven.append(subset)
        require(len(seven) == 8 and all(s in three_face_unions for s in seven),
                'PARITY_256_SUBSETS')
        subset_counts.append({'subsets': 256, 'size_seven': len(seven)})

    observed = set()
    for mask in range(1 << 16):
        if mask % 512 == 0:
            checkpoint()
        if bin(mask).count('1') != 7:
            continue
        words = frozenset(w for w in range(16) if mask & (1 << w))
        if words in three_face_unions:
            observed.add(words)
    require(observed == three_face_unions, 'FULL_BINARY_BOX_SUBSET_COVERAGE')

    witness_count = 0
    wrong_row_controls = 0
    for seven in sorted(observed, key=lambda s: tuple(sorted(s))):
        cls = next((c for c in parity_classes if seven < c), None)
        require(cls is not None, 'PARITY_CLASS')
        missing = cls - seven
        require(len(missing) == 1, 'UNIQUE_PARITY_EIGHTH')
        eighth = next(iter(missing))
        require(pair_cap(seven), 'SEVEN_PAIR_CAP')
        require(binary_box_issue(seven) == 'ONE_OVERLAP', 'OMITTED_EIGHTH_CONTROL')
        # With no-one-overlap omitted the partial pair-cap predicate accepts.
        require(pair_cap(seven) and has_one_overlap(seven), 'NO_OVERLAP_CONTROL')
        witnesses = forcing_witnesses(seven)
        require(witnesses and all(w[2] == eighth for w in witnesses),
                'FORCED_EIGHTH')
        witness_count += len(witnesses)
        completed = seven | {eighth}
        require(binary_box_issue(completed) is None, 'COMPLETED_SIX_PAIRS_THREE_CUTS')
        cut, deficient_row, _ = witnesses[0]
        wrong = next((w for w in range(16)
                      if w not in completed and pair_value(w, cut[0]) != deficient_row), None)
        require(wrong is not None and binary_box_issue(seven | {wrong}) == 'PAIR_CAP',
                'WRONG_ROW_CONTROL')
        wrong_row_controls += 1
    return {'all_16_vertex_box_subsets': 1 << 16,
            'per_parity_class': subset_counts,
            'three_face_presentations': face_presentations,
            'distinct_qualifying_sevens': len(observed),
            'forcing_row_witnesses': witness_count,
            'wrong_row_controls': wrong_row_controls,
            'controls': ['ONE_OVERLAP', 'OMITTED_EIGHTH', 'PAIR_CAP_WRONG_ROW'],
            'positive_fixture': 'SUPPORT_ONLY_NOT_A_STATE'}


def cube_issue(vertices):
    if len(vertices) != 4:
        return 'CUBE_CARDINALITY'
    for a, b in combinations(vertices, 2):
        if a ^ b in (1, 2, 4):
            return 'CUBE_DISTANCE1'
    return None


def check_three_cube():
    candidates = 0
    complement_pairs = set()
    independent = set()
    for chosen in combinations(range(8), 4):
        candidates += 1
        mask = sum(1 << v for v in chosen)
        complement_pairs.add(min(mask, 255 ^ mask))
        if cube_issue(chosen) is None:
            independent.add(frozenset(chosen))
    parity_sets = {frozenset(v for v in range(8) if parity(v) == p)
                   for p in (0, 1)}
    require(candidates == 70 and len(complement_pairs) == 35, 'CUBE_COVERAGE')
    require(independent == parity_sets, 'CUBE_INDEPENDENT_PARITIES')
    require(cube_issue((0, 1, 6, 7)) == 'CUBE_DISTANCE1', 'CUBE_EDGE_CONTROL')
    return {'four_vertex_subsets': candidates,
            'complement_pairs': len(complement_pairs),
            'independent_sets': len(independent),
            'controls': ['CUBE_DISTANCE1']}


def propagate_signs(n, edges):
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    signs = [0] * n
    signs[0] = 1
    pending = deque([0])
    while pending:
        a = pending.popleft()
        for b in adjacency[a]:
            if signs[b] == 0:
                signs[b] = -signs[a]
                pending.append(b)
            elif signs[b] != -signs[a]:
                return None, 'ODD_CYCLE'
    if any(value == 0 for value in signs):
        return None, 'DISCONNECTED'
    return signs, None


def has_triangle(n, edges):
    edge_set = {tuple(sorted(edge)) for edge in edges}
    return any((a, b) in edge_set and (a, c) in edge_set and (b, c) in edge_set
               for a, b, c in combinations(range(n), 3))


def integer_rank(matrix, width):
    # Integer row operations, with gcd normalization, preserve rational rank.
    rows = [list(row) for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = next((r for r in range(pivot_row, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        for r in range(pivot_row + 1, len(rows)):
            factor = rows[r][column]
            if factor == 0:
                continue
            for c in range(column, width):
                rows[r][c] = pivot_value * rows[r][c] - factor * rows[pivot_row][c]
            divisor = 0
            for value in rows[r][column:]:
                divisor = gcd(divisor, abs(value))
            if divisor > 1:
                for c in range(column, width):
                    rows[r][c] //= divisor
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def cubic_bipartite_graphs(k):
    # Each labelled graph on fixed sides {0,...,k-1} and {k,...,2k-1} once.
    choices = list(combinations(range(k), 3))
    remaining = [3] * k
    selected = [()] * k
    visits = [0]

    def generate(row):
        visits[0] += 1
        if visits[0] % 512 == 0:
            checkpoint()
        if row == k:
            if all(value == 0 for value in remaining):
                yield tuple((i, k + j) for i, choice in enumerate(selected) for j in choice)
            return
        for choice in choices:
            if any(remaining[j] == 0 for j in choice):
                continue
            for j in choice:
                remaining[j] -= 1
            left = k - row - 1
            if all(value <= left for value in remaining):
                selected[row] = choice
                yield from generate(row + 1)
            for j in choice:
                remaining[j] += 1

    yield from generate(0)


def edge_equation_issue(signs, edges):
    return 'EDGE_EQUATION' if any(signs[a] + signs[b] != 0 for a, b in edges) else None


def check_cubic_graphs():
    counts = {}
    for k in (3, 4, 5):
        n = 2 * k
        total = 0
        for edges in cubic_bipartite_graphs(k):
            total += 1
            if total % 64 == 0:
                checkpoint()
            degree = [0] * n
            for a, b in edges:
                degree[a] += 1
                degree[b] += 1
            require(all(value == 3 for value in degree), 'GRAPH_NOT_CUBIC')
            require(len(set(edges)) == len(edges), 'GRAPH_NOT_SIMPLE')
            signs, issue = propagate_signs(n, edges)
            require(issue is None, 'GRAPH_CONNECTED_BIPARTITE')
            require(not has_triangle(n, edges), 'GRAPH_TRIANGLE')
            require(edge_equation_issue(signs, edges) is None, 'GRAPH_EDGE_EQUATIONS')
            matrix = []
            for a, b in edges:
                row = [0] * n
                row[a] = row[b] = 1
                matrix.append(row)
            require(integer_rank(matrix, n) == n - 1, 'GRAPH_INTEGER_RANK')
            require(edge_equation_issue([1] * n, edges) == 'EDGE_EQUATION',
                    'GRAPH_BAD_SIGN_CONTROL')
        require(total == {3: 1, 4: 24, 5: 2040}[k], 'GRAPH_ENUMERATION_COUNT')
        counts[str(n)] = total
    five_cycle = [(i, (i + 1) % 5) for i in range(5)]
    require(not has_triangle(5, five_cycle), 'FIVE_CYCLE_CONTROL_TRIANGLE')
    require(propagate_signs(5, five_cycle)[1] == 'ODD_CYCLE', 'FIVE_CYCLE_ODD_CONTROL')
    k4 = list(combinations(range(4), 2))
    require(has_triangle(4, k4) and propagate_signs(4, k4)[1] == 'ODD_CYCLE',
            'K4_ODD_CONTROL')
    return {'fixed_bipartition_labelled_connected_graphs': counts,
            'edge_matrix_rank': 'm-1 over Q; same kernel dimension over C',
            'controls': ['EDGE_EQUATION', 'triangle_free_ODD_CYCLE', 'K4_ODD_CYCLE'],
            'scope': 'necessary edge equations for common complex z; not a tensor fixture'}


def pattern_edge(pattern, i, x, j, y):
    if i > j:
        i, j, x, y = j, i, y, x
    return bool(pattern[PAIR_INDEX[(i, j)]] & (1 << (2 * x + y)))


def pattern_issue(pattern, check_destination=True, check_complement=True,
                  check_triangle=True):
    if len(pattern) != 6 or any(bin(mask).count('1') not in (0, 2) for mask in pattern):
        return 'PAIR_COUNT'
    if check_complement:
        for first, second in ((0, 5), (1, 4), (2, 3)):
            if bool(pattern[first]) != bool(pattern[second]):
                return 'COMPLEMENT'
    destinations = [[set() for _ in range(2)] for _ in range(4)]
    for index, (i, j) in enumerate(PAIRS):
        for x, y in product(range(2), repeat=2):
            if pattern[index] & (1 << (2 * x + y)):
                destinations[i][x].add(j)
                destinations[j][y].add(i)
    if check_destination and any(len(d) > 1 for party in destinations for d in party):
        return 'DESTINATION'
    if check_triangle:
        for i, j, k in combinations(range(4), 3):
            for x, y, z in product(range(2), repeat=3):
                if (pattern_edge(pattern, i, x, j, y) and
                    pattern_edge(pattern, i, x, k, z) and
                    pattern_edge(pattern, j, y, k, z)):
                    return 'TRIANGLE'
    return None


def check_4444():
    masks = (0, 3, 5, 6, 9, 10, 12)
    total = complement_count = valid = 0
    max_edges = 0
    for pattern in product(masks, repeat=6):
        total += 1
        if total % 512 == 0:
            checkpoint()
        complement_ok = all(bool(pattern[a]) == bool(pattern[b])
                            for a, b in ((0, 5), (1, 4), (2, 3)))
        if not complement_ok:
            continue
        complement_count += 1
        if pattern_issue(pattern) is not None:
            continue
        valid += 1
        edges = sum(bin(mask).count('1') for mask in pattern)
        max_edges = max(max_edges, edges)
        require(edges <= 4 and 2 * edges <= 8, 'LOW_EDGE_BOUND')
    require(total == 7 ** 6 and complement_count == 37 ** 3, 'LOW_PATTERN_COVERAGE')
    require(valid > 1 and max_edges == 4, 'LOW_PATTERN_NONVACUITY')
    require(32 > 20 + 2 * max_edges, 'LOW_INCIDENCE_CONTRADICTION')

    dropped_destination = (9, 9, 0, 0, 9, 9)
    require(pattern_issue(dropped_destination) == 'DESTINATION', 'DESTINATION_CONTROL')
    require(pattern_issue(dropped_destination, check_destination=False) is None,
            'DESTINATION_RELAXATION_CONTROL')
    require(sum(bin(mask).count('1') for mask in dropped_destination) == 8,
            'DESTINATION_RELAXATION_EDGE_COUNT')
    dropped_complement = (9, 0, 0, 0, 0, 0)
    require(pattern_issue(dropped_complement) == 'COMPLEMENT', 'COMPLEMENT_CONTROL')
    require(pattern_issue(dropped_complement, check_complement=False) is None,
            'COMPLEMENT_RELAXATION_CONTROL')
    require(pattern_issue((1, 0, 0, 0, 0, 0)) == 'PAIR_COUNT', 'PAIR_COUNT_CONTROL')
    triangle = (9, 9, 0, 9, 0, 0)
    require(pattern_issue(triangle, check_destination=False, check_complement=False)
            == 'TRIANGLE', 'TRIANGLE_CONTROL')
    return {'all_pair_zero_or_two_patterns': total,
            'complement_symmetric_patterns': complement_count,
            'accepted_labelled_patterns': valid,
            'max_edges': max_edges, 'max_two_low_words': 2 * max_edges,
            'low_incidences': 32, 'E_words': 20,
            'controls': ['DESTINATION', 'COMPLEMENT', 'PAIR_COUNT', 'TRIANGLE'],
            'scope': 'abstract necessary low graphs, not independent physical tensors'}


def p_pair_issue(words):
    for pair in PAIRS:
        seen = set()
        for word in words:
            value = tuple(word[i] for i in pair)
            if value in seen:
                return 'P_PAIR_COLLISION', pair
            seen.add(value)
    return None, None


def u_words(index, bits):
    outside = (('outside', 0), ('outside', 1))
    low = ('low', index)
    u = 'u' + str(index)
    c1, d1, b2, d2, b3, c3 = bits
    return ((u, low, outside[c1], outside[d1]),
            (u, outside[b2], low, outside[d2]),
            (u, outside[b3], outside[c3], low))


def formula_bits(r):
    return (1 - r, r, r, 1 - r, 1 - r, r)


def check_3444():
    outside = (('outside', 0), ('outside', 1))
    z_words = (('z', outside[0], outside[0], outside[0]),
               ('z', outside[1], outside[1], outside[1]))
    assignments = list(product(range(2), repeat=6))
    singles = []
    for index in (0, 1):
        valid = []
        for bits in assignments:
            words = u_words(index, bits)
            if p_pair_issue(z_words + words)[0] is None:
                r = bits[2]
                require(bits == formula_bits(r), 'R_FORMULA')
                valid.append(r)
        require(sorted(valid) == [0, 1], 'R_INDIVIDUAL_COVERAGE')
        singles.append(sorted(valid))

    allowed_r_pairs = set()
    partial_assignments = 0
    obligation_checks = 0
    for a in assignments:
        for b in assignments:
            partial_assignments += 1
            if partial_assignments % 256 == 0:
                checkpoint()
            known = z_words + u_words(0, a) + u_words(1, b)
            if p_pair_issue(known)[0] is not None:
                continue
            require(a == formula_bits(a[2]) and b == formula_bits(b[2]), 'R_PAIR_FORMULA')
            allowed_r_pairs.add((a[2], b[2]))
            for index in (0, 1):
                for i, j in combinations((1, 2, 3), 2):
                    remaining = next(k for k in (1, 2, 3) if k not in (i, j))
                    for outside_a in range(3):
                        for outside_remaining in range(2):
                            candidate = [None] * 4
                            candidate[0] = ('outsideA', outside_a)
                            candidate[i] = candidate[j] = ('low', index)
                            candidate[remaining] = outside[outside_remaining]
                            reason, pair = p_pair_issue(known + (tuple(candidate),))
                            require(reason == 'P_PAIR_COLLISION' and
                                    pair in ((min(i, remaining), max(i, remaining)),
                                             (min(j, remaining), max(j, remaining))),
                                    'LOW_PAIR_FORCED_CONFLICT')
                            obligation_checks += 1
    require(partial_assignments == 4096, 'R_PAIR_COVERAGE')
    require(allowed_r_pairs == {(0, 1), (1, 0)}, 'R_PAIR_OPTIONS')
    require(obligation_checks == 72, 'LOW_PAIR_OBLIGATION_COVERAGE')
    same_r = z_words + u_words(0, formula_bits(0)) + u_words(1, formula_bits(0))
    require(p_pair_issue(same_r)[0] == 'P_PAIR_COLLISION', 'SAME_R_CONTROL')
    return {'single_u_r_values': singles, 'partial_outside_assignments': partial_assignments,
            'allowed_r_pairs': sorted([list(pair) for pair in allowed_r_pairs]),
            'forced_low_pair_outside_P_candidates_rejected': obligation_checks,
            'controls': ['P_PAIR_COLLISION_same_r'],
            'scope': 'SUPPORT_ONLY abstract P consequences; complement is a premise'}


def main():
    global DEADLINE
    start = time.monotonic()
    DEADLINE = start + 45.0
    signal.signal(signal.SIGTERM, signal_stop)
    signal.signal(signal.SIGINT, signal_stop)
    try:
        if len(sys.argv) != 1:
            raise CheckFailure('NO_ARGUMENTS_ACCEPTED')
        result = {'binary_box': check_binary_box(),
                  'three_cube': check_three_cube(),
                  'cubic_graphs': check_cubic_graphs(),
                  'profile_4444': check_4444(),
                  'profile_3444': check_3444()}
        checkpoint()
        result.update({'status': 'LOCAL_NECESSARY_CHECKS_PASS',
                       'elapsed_seconds': round(time.monotonic() - start, 3),
                       'not_established': ['existence or nonexistence of a complex AME(4,6)',
                                           'full N=46,t=26 exclusion',
                                           'N>=49 or a global minimum',
                                           'independent review, parent adoption, novelty, human or kernel verification']})
        print(json.dumps(result, sort_keys=True))
        return 0
    except Incomplete as exc:
        print(json.dumps({'status': 'INCOMPLETE', 'reason': str(exc)}, sort_keys=True))
        return 124
    except CheckFailure as exc:
        print(json.dumps({'status': 'FAIL', 'reason': str(exc)}, sort_keys=True))
        return 1
    except Exception as exc:
        print(json.dumps({'status': 'INCOMPLETE', 'reason': 'unexpected_' + type(exc).__name__,
                          'detail': str(exc)}, sort_keys=True))
        return 1


if __name__ == '__main__':
    sys.exit(main())
