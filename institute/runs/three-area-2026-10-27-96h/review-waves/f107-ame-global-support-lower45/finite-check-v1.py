#!/usr/bin/env python3
"""Independent finite controls; reads pinned inputs only for byte identity.

Enumerate incidence matrices, balanced four-point fibres, projections, overlap
obstructions, small unitary support graphs, and exact Gaussian Pauli matrices.
No author program is imported or executed. Receipt creation is exclusive.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, prod
from pathlib import Path
import hashlib
import json
import os
import platform
import sys
import time

MANIFEST = Path(__file__).with_name('manifest-v1.json')
MANIFEST_SHA = 'b1565273e7c79e38346cc455e1a6e93943da91421f6d003d523b3005cb3b9300'

class Failure(Exception):
    pass

def need(ok, reason):
    if not ok:
        raise Failure(reason)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def source_pins():
    data = MANIFEST.read_bytes()
    need(digest(data) == MANIFEST_SHA, 'manifest hash')
    m = json.loads(data)
    out = []
    for item in m['inputs_in_read_order']:
        b = Path(item['path']).read_bytes()
        need((digest(b), len(b), b.count(b'\n')) ==
             (item['sha256'], item['bytes'], item['LF']), 'input pin')
        need(b'\r' not in b, 'input newline')
        out.append({'name': Path(item['path']).name, 'sha256': digest(b),
                    'bytes': len(b), 'LF': b.count(b'\n'), 'CR': 0})
    return out

def rows_of_width(width):
    return tuple(n for n in range(1 << width) if n.bit_count() == 2)

def incidence(width, degrees):
    answer = []
    for rows in product(rows_of_width(width), repeat=4):
        if tuple(sum((r >> c) & 1 for r in rows) for c in range(width)) == degrees:
            answer.append(rows)
    return answer

def validate_graph(graph, width, degrees):
    need(len(graph) == 4, 'graph row count')
    need(all(0 <= r < (1 << width) and r.bit_count() == 2 for r in graph),
         'graph row degree')
    need(tuple(sum((r >> c) & 1 for r in graph) for c in range(width)) == degrees,
         'graph column degree')

def even_rectangles(left, right, mask, nl, nr):
    # Count each cell directly; do not construct or XOR rectangle masks.
    return all(sum(((mask >> g) & 1) * ((left[g] >> i) & 1) *
                   ((right[g] >> j) & 1) for g in range(4)) % 2 == 0
               for i in range(nl) for j in range(nr))

def repeated_pair(g):
    pairs = [sum(1 << i for i in range(4) if g[i] == value)
             for value in set(g)]
    twice = [p for p in pairs if p.bit_count() == 2]
    need(len(twice) == 1 and len(set(g)) == 3, 'ternary duplicate form')
    return twice[0]

def split_partition(g):
    groups = tuple(sorted(sum(1 << i for i in range(4) if g[i] == value)
                          for value in set(g)))
    return groups if len(groups) == 2 and all(p.bit_count() == 2 for p in groups) else None

def parity_controls(g4, g3all, g3low):
    report = {}
    tables = {}
    for label, lefts, rights, nl, nr in [
            ('44', g4, g4, 4, 4), ('34_all_low_labels', g3all, g4, 3, 4),
            ('33_all_low_labels', g3all, g3all, 3, 3),
            ('34_low0', g3low, g4, 3, 4), ('33_low0', g3low, g3low, 3, 3)]:
        hist = Counter()
        table = {}
        for i, left in enumerate(lefts):
            for j, right in enumerate(rights):
                zeros = tuple(mask for mask in range(16)
                              if even_rectangles(left, right, mask, nl, nr))
                table[i, j] = frozenset(zeros)
                for mask in zeros:
                    if not mask:
                        continue
                    hist[str(mask.bit_count())] += 1
                    if label == '44':
                        p, q = split_partition(left), split_partition(right)
                        need(mask.bit_count() in (2, 4) and p is not None and p == q,
                             'R44 counterexample')
                        if mask.bit_count() == 2:
                            need(mask in p, 'R44 mask partition')
                    elif label.startswith('34'):
                        p, q = repeated_pair(left), split_partition(right)
                        need(mask == p and q is not None and p in q, 'R34 counterexample')
                    else:
                        p, q = repeated_pair(left), repeated_pair(right)
                        need((mask == p == q) or
                             (mask == 15 and p == (15 ^ q)), 'R33 counterexample')
        report[label] = {'ordered_matrix_pairs': len(lefts) * len(rights),
                         'masks_examined_including_empty': len(lefts) * len(rights) * 16,
                         'nonempty_even_mask_count_by_weight': dict(sorted(hist.items()))}
        tables[label] = table
    return report, tables

def balanced_binary_fibres():
    cube = tuple(product(range(2), repeat=3))
    by_type = {0: [], 1: [], 2: [], 3: []}
    pairs = ((0, 1), (0, 2), (1, 2))
    for chosen in combinations(cube, 4):
        if not all(sum(x[k] for x in chosen) == 2 for k in range(3)):
            continue
        sizes = tuple(len({(x[a], x[b]) for x in chosen}) for a, b in pairs)
        need(all(v in (2, 4) for v in sizes), 'binary projection classification')
        correlated = [i + 1 for i, size in enumerate(sizes) if size == 2]
        need(len(correlated) <= 1, 'two correlations in a balanced four-point fibre')
        by_type[correlated[0] if correlated else 0].append(chosen)
    need(all(len(x) == 2 for x in by_type.values()), 'binary fibre inventory')
    return by_type

def full_masks(types):
    return tuple(sum(1 << g for g, t in enumerate(types) if t != pair)
                 for pair in (1, 2, 3))

def symbols(bits, width):
    return tuple(i for i in range(width) if (bits >> i) & 1)

def fiber_point_options(a, graphs, kind, inventory):
    choices = [symbols(g[a], width) for g, width in zip(graphs, (3, 3, 4))]
    need(all(len(x) == 2 for x in choices), 'fiber two symbols')
    return tuple(tuple((a, choices[0][u], choices[1][v], choices[2][w])
                       for u, v, w in binary)
                 for binary in inventory[kind])

PAIR_COORDS = tuple(combinations(range(4), 2))
CUTS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
CUT_NAMES = ('AB|CD', 'AC|BD', 'AD|BC')

def projection_counts(support, coords):
    return Counter(tuple(word[i] for i in coords) for word in support)

def projection_test(support):
    need(len(support) == 16, 'support cardinality')
    for coords in PAIR_COORDS:
        counts = projection_counts(support, coords)
        need(len(counts) == 8, 'pair projection cardinality')
        need(all(v == 2 for v in counts.values()), 'pair projection multiplicity')

def overlaps(support, left, right):
    row_support = {}
    col_support = {}
    for word in support:
        r = tuple(word[i] for i in left)
        c = tuple(word[i] for i in right)
        row_support.setdefault(r, set()).add(c)
        col_support.setdefault(c, set()).add(r)
    out = []
    for axis, buckets in (('row', row_support), ('column', col_support)):
        for x, y in combinations(sorted(buckets), 2):
            common = buckets[x] & buckets[y]
            if len(common) == 1:
                out.append({'axis': axis, 'objects': [x, y],
                            'unique_common': next(iter(common)),
                            'supports': [sorted(buckets[x]), sorted(buckets[y])]})
    return out

def mixed_controls(g4, g3, tables, fibres):
    patterns = [(types, full_masks(types)) for types in product(range(4), repeat=4)]
    count = Counter()
    flatten = {scope: {name: Counter() for name in CUT_NAMES} for scope in ('nonempty', 'some_empty')}
    joint = {scope: Counter() for scope in flatten}
    first = {}
    form_distribution = Counter()
    for ib, B in enumerate(g3):
        for ic, C in enumerate(g3):
            bc = tables['33_low0'][ib, ic]
            for id_, D in enumerate(g4):
                bd = tables['34_low0'][ib, id_]
                cd = tables['34_low0'][ic, id_]
                for types, masks in patterns:
                    if masks[0] not in bc or masks[1] not in bd or masks[2] not in cd:
                        continue
                    scope = 'nonempty' if all(masks) else 'some_empty'
                    count[scope + '_parity_forms'] += 1
                    form_distribution[scope + ':' + ','.join(map(str, masks))] += 1
                    options = [fiber_point_options(a, (B, C, D), types[a], fibres)
                               for a in range(4)]
                    for bit_choices in product(range(2), repeat=4):
                        support = frozenset(word for a in range(4)
                                            for word in options[a][bit_choices[a]])
                        count[scope + '_supports_examined'] += 1
                        try:
                            projection_test(support)
                        except Failure as e:
                            count[scope + '_rejected_' + str(e).replace(' ', '_')] += 1
                            continue
                        count[scope + '_projection_survivors'] += 1
                        statuses = []
                        witnesses = {}
                        for name, (left, right) in zip(CUT_NAMES, CUTS):
                            found = overlaps(support, left, right)
                            axes = ''.join(a for a in ('R', 'C') if any(
                                x['axis'] == {'R': 'row', 'C': 'column'}[a] for x in found))
                            flatten[scope][name][axes or 'none'] += 1
                            statuses.append(axes or 'none')
                            witnesses[name] = {axis: next((x for x in found if x['axis'] == axis), None)
                                               for axis in ('row', 'column')}
                        joint[scope]['/'.join(statuses)] += 1
                        if scope == 'nonempty':
                            need(statuses[2] != 'none', 'nonempty survivor without AD|BC obstruction')
                        if scope not in first:
                            first[scope] = {'incidence_B': B, 'incidence_C': C,
                                            'incidence_D': D, 'fibre_types': types,
                                            'full_masks_BC_BD_CD': masks,
                                            'support': sorted(support), 'overlaps': witnesses}
    return {'counts': dict(sorted(count.items())),
            'normal_form_mask_distribution': dict(sorted(form_distribution.items())),
            'flattenings': {s: {k: dict(sorted(v.items())) for k, v in f.items()}
                            for s, f in flatten.items()},
            'joint_flattening_signatures': {s: dict(sorted(v.items())) for s, v in joint.items()},
            'examples': first}

def column_masks(rows, n):
    return tuple(sum(1 << r for r, row in enumerate(rows) if (row >> c) & 1)
                 for c in range(n))

def no_single_overlap(masks):
    return all((x & y).bit_count() != 1 for x, y in combinations(masks, 2))

def components(rows, n):
    # Connected components of bipartite support, including isolated vertices.
    pending = set(range(2 * n))
    parts = []
    while pending:
        todo = [min(pending)]
        seen = set()
        while todo:
            v = todo.pop()
            if v in seen:
                continue
            seen.add(v)
            if v < n:
                todo.extend(n + c for c in range(n) if (rows[v] >> c) & 1)
            else:
                c = v - n
                todo.extend(r for r in range(n) if (rows[r] >> c) & 1)
        pending -= seen
        rr = [x for x in seen if x < n]
        cc = [x - n for x in seen if x >= n]
        edges = sum((rows[r] >> c) & 1 for r in rr for c in cc)
        parts.append((len(rr), len(cc), edges))
    return tuple(sorted(parts))

def small_support_graphs(n, excess):
    target = 2 * n + excess
    all_masks = tuple(r for r in range(1 << n) if r.bit_count() >= 2)
    raw = sum(prod(comb(n, d) for d in ds)
              for ds in product(range(2, n + 1), repeat=n) if sum(ds) == target)
    count = Counter()
    examples = {}
    def descend(rows, total):
        remaining = n - len(rows)
        if total + 2 * remaining > target or total + n * remaining < target:
            return
        if not remaining:
            cols = column_masks(rows, n)
            if any(c.bit_count() < 2 for c in cols):
                count['column_degree_rejected_after_row_filter'] += 1
                return
            count['row_filter_and_column_degree'] += 1
            if not no_single_overlap(cols):
                count['column_overlap_rejected'] += 1
                return
            count['row_column_overlap_pass'] += 1
            comp = components(rows, n)
            if any(r != c for r, c, _ in comp):
                count['rectangular_component_rejected'] += 1
                examples.setdefault('rectangular', {'rows': rows, 'components': comp})
                return
            count['square_component_pass'] += 1
            examples.setdefault('square', {'rows': rows, 'components': comp})
            if excess == 2:
                shape = tuple(sorted([(3, 3, 8)] + [(2, 2, 4)] * ((n - 3) // 2)))
                need(n >= 3 and n % 2 == 1 and comp == shape,
                     'small two-excess component classification')
            if excess == 1:
                raise Failure('small one-excess graph survived')
            if excess == 0:
                need(n % 2 == 0 and all(x == (2, 2, 4) for x in comp),
                     'small zero-excess component classification')
            return
        for mask in all_masks:
            if all((mask & other).bit_count() != 1 for other in rows):
                descend(rows + (mask,), total + mask.bit_count())
    descend((), 0)
    return {'raw_row_degree_candidates': raw, 'counts': dict(sorted(count.items())),
            'examples': examples}

# Gaussian rationals: (real, imaginary), both fractions.
def G(r=0, i=0): return (Q(r), Q(i))
def plus(a, b): return (a[0] + b[0], a[1] + b[1])
def neg(a): return (-a[0], -a[1])
def mul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def conj(a): return (a[0], -a[1])
def scale(a, k): return (a[0] * k, a[1] * k)
def divide(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    need(d != 0, 'division by zero')
    return scale(mul(a, conj(b)), 1 / d)

def matrix(rows): return tuple(tuple(x for x in row) for row in rows)
def eye(n): return matrix(tuple(G(int(i == j)) for j in range(n)) for i in range(n))
def addmat(a, b): return matrix(tuple(plus(x, y) for x, y in zip(r, s)) for r, s in zip(a, b))
def scalemat(a, k): return matrix(tuple(scale(x, k) for x in r) for r in a)
def conjugate(a): return matrix(tuple(conj(x) for x in r) for r in a)
def dagger(a): return matrix(tuple(conj(a[i][j]) for i in range(len(a))) for j in range(len(a[0])))
def matmul(a, b):
    need(len(a[0]) == len(b), 'matrix dimension')
    return matrix(tuple(sum_g(mul(a[i][k], b[k][j]) for k in range(len(b)))
                        for j in range(len(b[0]))) for i in range(len(a)))
def sum_g(values):
    s = G()
    for v in values:
        s = plus(s, v)
    return s
def kron(a, b):
    return matrix(tuple(mul(a[i // len(b)][j // len(b[0])], b[i % len(b)][j % len(b[0])])
                        for j in range(len(a[0]) * len(b[0])))
                  for i in range(len(a) * len(b)))
def rank(a):
    m = [list(row) for row in a]
    pivot = 0
    for c in range(len(m[0])):
        nonzero = next((r for r in range(pivot, len(m)) if m[r][c] != G()), None)
        if nonzero is None:
            continue
        m[pivot], m[nonzero] = m[nonzero], m[pivot]
        p = m[pivot][c]
        m[pivot] = [divide(x, p) for x in m[pivot]]
        for r in range(len(m)):
            if r != pivot and m[r][c] != G():
                v = m[r][c]
                m[r] = [plus(x, neg(mul(v, y))) for x, y in zip(m[r], m[pivot])]
        pivot += 1
        if pivot == len(m):
            break
    return pivot

def partial_trace3(a, keep):
    drop = tuple(k for k in range(3) if k not in keep)
    states = tuple(product(range(2), repeat=len(keep)))
    def index(kept, traced):
        bits = [0, 0, 0]
        for pos, val in zip(keep, kept): bits[pos] = val
        for pos, val in zip(drop, traced): bits[pos] = val
        return 4 * bits[0] + 2 * bits[1] + bits[2]
    return matrix(tuple(sum_g(a[index(x, t)][index(y, t)]
                              for t in product(range(2), repeat=len(drop)))
                        for y in states) for x in states)

def pauli_controls():
    ident = eye(2)
    x = matrix(((G(), G(1)), (G(1), G())))
    y = matrix(((G(), G(0, -1)), (G(0, 1), G())))
    z = matrix(((G(1), G()), (G(), G(-1))))
    basis = (ident, x, y, z)
    def tensor(indices):
        out = basis[indices[0]]
        for index in indices[1:]: out = kron(out, basis[index])
        return out
    sy = tensor((2, 2, 2))
    spin = lambda a: matmul(matmul(sy, conjugate(a)), sy)
    pauli_counts = Counter()
    partial_count = 0
    for labels in product(range(4), repeat=3):
        p = tensor(labels)
        w = sum(i != 0 for i in labels)
        need(spin(p) == scalemat(p, (-1) ** w), 'Pauli spin sign')
        pauli_counts[str(w)] += 1
        for keep in combinations(range(3), 2):
            dropped = next(i for i in range(3) if i not in keep)
            reduced = partial_trace3(p, keep)
            expected = scalemat(kron(basis[labels[keep[0]]], basis[labels[keep[1]]]),
                                2 if labels[dropped] == 0 else 0)
            need(reduced == expected, 'Pauli partial trace')
            partial_count += 1
    eig = tuple(Q(1, 4) if sum(bits) % 2 == 0 else Q(0)
                for bits in product(range(2), repeat=3))
    rho = matrix(tuple(G(eig[i] if i == j else 0) for j in range(8)) for i in range(8))
    u = matrix(((G(Q(3, 5)), G(0, Q(4, 5))),
                (G(0, Q(4, 5)), G(Q(3, 5)))))
    need(matmul(u, dagger(u)) == eye(2) and matmul(dagger(u), u) == eye(2),
         'complex rational unitary')
    big = kron(kron(u, ident), ident)
    rotated = matmul(matmul(big, rho), dagger(big))
    positive = {}
    for name, state in (('diagonal_even', rho), ('complex_rotated', rotated)):
        need(state == dagger(state), 'state Hermitian')
        need(sum_g(state[i][i] for i in range(8)) == G(1), 'state trace')
        need(rank(state) == 4, 'state rank')
        need(matmul(state, state) == scalemat(state, Q(1, 4)), 'state eigenvalues')
        for keep in combinations(range(3), 2):
            need(partial_trace3(state, keep) == scalemat(eye(4), Q(1, 4)), 'state marginal')
        need(spin(state) == addmat(scalemat(eye(8), Q(1, 4)), scalemat(state, -1)),
             'state spin identity')
        need(matmul(spin(state), spin(state)) == scalemat(spin(state), Q(1, 4)),
             'spin PSD eigenvalues')
        positive[name] = {'rank': 4, 'spectrum': {'0': 4, '1/4': 4},
                          'all_pair_marginals': 'I4/4', 'spin_identity': True}
    need(any(x[1] != 0 for row in rotated for x in row), 'complex control not complex')
    mutant_eig = tuple(Q(1, 3) if sum(bits) % 2 == 0 and bits != (1, 1, 0) else Q(0)
                       for bits in product(range(2), repeat=3))
    mutant = matrix(tuple(G(mutant_eig[i] if i == j else 0) for j in range(8)) for i in range(8))
    need(rank(mutant) == 3, 'rank-three negative rank')
    bad_marginals = [list(keep) for keep in combinations(range(3), 2)
                     if partial_trace3(mutant, keep) != scalemat(eye(4), Q(1, 4))]
    need(bool(bad_marginals), 'rank-three mutation escaped')
    # A Hermitian trace-one operator with correct marginals and spin identity,
    # but negative eigenvalues: positivity is essential to the inequality.
    unphysical = addmat(scalemat(eye(8), Q(1, 8)), scalemat(tensor((3, 3, 3)), Q(1, 4)))
    need(all(partial_trace3(unphysical, keep) == scalemat(eye(4), Q(1, 4))
             for keep in combinations(range(3), 2)), 'non-PSD control marginal')
    need(spin(unphysical) == addmat(scalemat(eye(8), Q(1, 4)), scalemat(unphysical, -1)),
         'non-PSD control identity')
    diag = [unphysical[i][i][0] for i in range(8)]
    need(min(diag) == Q(-1, 8) and max(diag) == Q(3, 8), 'non-PSD control spectrum')
    without_conjugation = matmul(matmul(sy, tensor((2, 0, 0))), sy)
    need(without_conjugation != spin(tensor((2, 0, 0))), 'conjugation mutation escaped')
    return {'spin_signs_by_weight': dict(sorted(pauli_counts.items())),
            'basis_matrices_checked': 64, 'basis_partial_traces_checked': partial_count,
            'positive_states': positive,
            'rank_three_negative': {'rank': 3, 'bad_pair_marginals': bad_marginals},
            'non_psd_negative': {'correct_pair_marginals': True, 'spin_identity': True,
                                 'min_eigenvalue': '-1/8', 'max_eigenvalue': '3/8'},
            'omitted_conjugation_mutation': 'rejected on YII'}

def rational_unitary_control():
    m = matrix(((G(Q(3, 5)), G(Q(4, 5)), G()),
                (G(Q(-12, 25)), G(Q(9, 25)), G(Q(4, 5))),
                (G(Q(-16, 25)), G(Q(12, 25)), G(Q(-3, 5)))))
    need(matmul(m, dagger(m)) == eye(3) and matmul(dagger(m), m) == eye(3),
         'three-by-three Gram')
    need(sum(x != G() for row in m for x in row) == 8, 'three-by-three support')
    return {'matrix': [['3/5', '4/5', '0'], ['-12/25', '9/25', '4/5'],
                       ['-16/25', '12/25', '-3/5']],
            'row_and_column_Gram': 'I3 exactly', 'support': 8}

def rejected(reason, fn):
    try:
        fn()
    except Failure as e:
        need(str(e) == reason, 'wrong mutation failure: ' + str(e))
        return reason
    raise Failure('mutation escaped: ' + reason)

def targeted_controls(g4, g3, mixed):
    result = {}
    validate_graph(g4[0], 4, (2, 2, 2, 2))
    validate_graph(g3[0], 3, (2, 3, 3))
    broken = list(g4[0]); broken[0] = 1
    result['invalid_graph_row_degree'] = rejected('graph row degree',
        lambda: validate_graph(tuple(broken), 4, (2, 2, 2, 2)))
    broken = list(g4[0]); broken[0] = next(x for x in rows_of_width(4) if x != broken[0])
    result['invalid_graph_column_degree'] = rejected('graph column degree',
        lambda: validate_graph(tuple(broken), 4, (2, 2, 2, 2)))
    u = (3, 3, 12, 12); v = (3, 12, 3, 12)
    validate_graph(u, 4, (2, 2, 2, 2)); validate_graph(v, 4, (2, 2, 2, 2))
    need(split_partition(u) != split_partition(v) and not even_rectangles(u, v, 15, 4, 4),
         'incompatible 44 partitions control')
    result['different_44_partitions'] = {'graphs': [u, v], 'mask': 15, 'parity_even': False}
    ternary = (6, 6, 3, 5)
    validate_graph(ternary, 3, (2, 3, 3))
    need(even_rectangles(ternary, u, 3, 3, 4) and
         not even_rectangles(ternary, u, 15, 3, 4), 'R34 mask control')
    result['34_duplicate_vs_all_fibres'] = {'graph3': ternary, 'graph4': u,
                                            'duplicate_mask_even': 3, 'all_mask_even': False}
    support = frozenset(tuple(x) for x in mixed['examples']['nonempty']['support'])
    projection_test(support)
    removed = sorted(support)[0]
    mutated = support - {removed}
    result['deleted_support_point'] = rejected('support cardinality', lambda: projection_test(mutated))
    mutated2 = None
    for word in sorted(support):
        for position, limit in enumerate((4, 3, 3, 4)):
            for value in range(limit):
                w = word[:position] + (value,) + word[position + 1:]
                s = (support - {word}) | {w}
                if w == word or len(s) != 16:
                    continue
                try:
                    projection_test(s)
                except Failure as e:
                    if str(e) in ('pair projection cardinality', 'pair projection multiplicity'):
                        mutated2 = (word, w, str(e)); break
            if mutated2: break
        if mutated2: break
    need(mutated2 is not None, 'projection mutation not found')
    result['single_coordinate_support_mutation'] = {'old': mutated2[0], 'new': mutated2[1],
                                                     'reason': mutated2[2]}
    square = (3, 3, 12, 12)
    cycle = (3, 6, 5)
    need(no_single_overlap(square) and no_single_overlap(column_masks(square, 4)),
         '2x2 block positive support')
    need(not no_single_overlap(cycle) and not no_single_overlap(column_masks(cycle, 3)),
         'six-cycle negative support')
    result['overlap_support_positive'] = {'rows': square, 'row_and_column_unique_overlap': False}
    result['overlap_support_negative'] = {'rows': cycle, 'row_and_column_unique_overlap': True}
    rectangular = (7, 7, 24, 24, 24)
    need(no_single_overlap(rectangular) and no_single_overlap(column_masks(rectangular, 5)),
         'rectangular survivor overlap')
    need(components(rectangular, 5) == ((2, 3, 6), (3, 2, 6)), 'rectangular components')
    result['rectangular_component_negative'] = {'rows': rectangular,
        'row_and_column_overlap_filter_pass': True, 'components': components(rectangular, 5),
        'square_component_filter': 'rejected'}
    return result

def main():
    need(len(sys.argv) == 2, 'usage: checker receipt.json')
    start_clock = datetime.now(timezone.utc).isoformat()
    start = time.perf_counter()
    pins = source_pins()
    g4 = incidence(4, (2, 2, 2, 2))
    g3low = incidence(3, (2, 3, 3))
    g3all = sorted(set(graph for low in range(3)
                       for graph in incidence(3, tuple(2 if i == low else 3 for i in range(3)))))
    need((len(g4), len(g3low), len(g3all)) == (90, 12, 36), 'incidence inventory')
    parity, tables = parity_controls(g4, g3all, g3low)
    fibres = balanced_binary_fibres()
    mixed = mixed_controls(g4, g3low, tables, fibres)
    graph_inventory = {}
    for n in range(2, 6):
        for excess in range(3):
            graph_inventory[str(n) + ',' + str(excess)] = small_support_graphs(n, excess)
    unitary = rational_unitary_control()
    pauli = pauli_controls()
    controls = targeted_controls(g4, g3low, mixed)
    finish_clock = datetime.now(timezone.utc).isoformat()
    seconds = time.perf_counter() - start
    receipt = {'schema': 'independent-finite-review-v1',
               'checker_sha256': digest(Path(__file__).read_bytes()),
               'manifest_sha256': MANIFEST_SHA, 'verified_inputs_in_order': pins,
               'argv': sys.argv, 'python': sys.version, 'platform': platform.platform(),
               'pid': os.getpid(), 'clock_start_utc': start_clock,
               'clock_finish_utc': finish_clock, 'elapsed_seconds': seconds,
               'incidence_counts': {'4_by_4_degree_2': len(g4),
                                    '4_by_3_degree_2_3_3_low_label_0': len(g3low),
                                    '4_by_3_all_low_labels': len(g3all)},
               'parity': parity, 'balanced_binary_fibres_by_type': {str(k): len(v) for k, v in fibres.items()},
               'mixed': mixed, 'small_support_graphs': graph_inventory,
               'exact_rational_eight_entry_unitary': unitary, 'gaussian_pauli_shadow': pauli,
               'targeted_controls': controls,
               'scope': 'Combinatorial support survivors are not physical tensors. Universal AME reductions, source novelty, and no-OLS(6) are not established by these controls.'}
    output = Path(sys.argv[1])
    with output.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps({'receipt': str(output), 'checker_sha256': receipt['checker_sha256'],
                      'start_utc': start_clock, 'finish_utc': finish_clock,
                      'elapsed_seconds': seconds, 'incidence': receipt['incidence_counts'],
                      'mixed_counts': mixed['counts'], 'flattenings': mixed['flattenings'],
                      'small_two_excess': {str(n): graph_inventory[str(n) + ',2']['counts'] for n in range(3, 6)},
                      'shadow': pauli, 'controls': controls}, indent=2))

if __name__ == '__main__':
    main()
