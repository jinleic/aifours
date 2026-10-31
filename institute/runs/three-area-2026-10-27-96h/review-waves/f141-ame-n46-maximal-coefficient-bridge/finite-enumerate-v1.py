#!/usr/bin/env python3
"""Independent, finite support-graph and exact-Gram controls; standard library only."""
from collections import Counter
from datetime import datetime
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import sys
import time

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
MANIFEST_SHA = 'dc1c9fea4f62d9c90d77ec8bdce1985667b9e8866f9a22d36982239e1213fc65'
RECEIPT = HERE / 'finite-receipt-v1.json'


def ensure(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def stamp():
    return datetime.now().astimezone().isoformat(timespec='microseconds')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def component_shapes(rows):
    n = len(rows)
    visited = set()
    result = []
    for seed in range(2*n):
        if seed in visited:
            continue
        seen = {seed}
        todo = [seed]
        while todo:
            vertex = todo.pop()
            if vertex < n:
                neighbors = [n+j for j in range(n) if rows[vertex] & (1 << j)]
            else:
                neighbors = [i for i in range(n) if rows[i] & (1 << (vertex-n))]
            for neighbor in neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    todo.append(neighbor)
        visited.update(seen)
        rr = sorted(x for x in seen if x < n)
        cc = sorted(x-n for x in seen if x >= n)
        local = [sum(1 << j for j, old in enumerate(cc) if rows[i] & (1 << old)) for i in rr]
        column_degrees = [sum(bool(mask & (1 << j)) for mask in local) for j in range(len(cc))]
        canonical = min(
            tuple(sorted(sum(1 << j for j, old in enumerate(order) if mask & (1 << old))
                         for mask in local))
            for order in permutations(range(len(cc)))
        )
        result.append({'rows': len(rr), 'columns': len(cc),
                       'edges': sum(mask.bit_count() for mask in local),
                       'row_degrees': sorted(mask.bit_count() for mask in local),
                       'column_degrees': sorted(column_degrees),
                       'canonical_row_masks': list(canonical)})
    return sorted(result, key=lambda c: (c['rows'], c['columns'], c['edges'], c['canonical_row_masks']))


def graph_reason(rows):
    n = len(rows)
    if not n or any(not isinstance(mask, int) or mask < 0 or mask >= (1 << n) for mask in rows):
        return 'INVALID_SQUARE_MASKS'
    cols = tuple(sum((1 << i) for i in range(n) if rows[i] & (1 << j)) for j in range(n))
    if any(mask.bit_count() < 2 for mask in tuple(rows) + cols):
        return 'MIN_DEGREE'
    if any((a & b).bit_count() == 1 for a, b in combinations(rows, 2)):
        return 'ROW_SINGLE_OVERLAP'
    if any((a & b).bit_count() == 1 for a, b in combinations(cols, 2)):
        return 'COLUMN_SINGLE_OVERLAP'
    if any(c['rows'] != c['columns'] for c in component_shapes(rows)):
        return 'RECTANGULAR_COMPONENT'
    return 'GRAPH_SURVIVOR'


def shape_reason(rows, expected):
    graph = graph_reason(rows)
    if graph != 'GRAPH_SURVIVOR':
        return graph
    return 'EXPECTED_SHAPE' if component_shapes(rows) == expected else 'SHAPE_MISMATCH'


def integer_gram_reason(matrix, denominator):
    n = len(matrix)
    if not n or any(len(row) != n for row in matrix) or denominator <= 0:
        return 'MATRIX_FORMAT'
    gram = lambda side, i, j: sum((matrix[i][k]*matrix[j][k] if side == 'rows'
                                   else matrix[k][i]*matrix[k][j]) for k in range(n))
    for side in ('rows', 'columns'):
        if any(gram(side, i, i) != denominator**2 for i in range(n)):
            return 'GRAM_DIAGONAL'
    for side in ('rows', 'columns'):
        if any(gram(side, i, j) != 0 for i, j in combinations(range(n), 2)):
            return 'GRAM_OFFDIAGONAL'
    return 'EXACT_UNITARY'


def omega_mul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c-b*d)  # omega^2=-1-omega


def omega_add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def omega_conj(x):
    return (x[0]-x[1], -x[1])  # conjugate(omega)=omega^2=-1-omega


def omega_gram_reason(matrix):
    n = len(matrix)
    if not n or any(len(row) != n for row in matrix):
        return 'MATRIX_FORMAT'
    def gram(side, i, j):
        terms = ((matrix[i][k], matrix[j][k]) if side == 'rows'
                 else (matrix[k][i], matrix[k][j]) for k in range(n))
        total = (0, 0)
        for a, b in terms:
            total = omega_add(total, omega_mul(omega_conj(a), b))
        return total
    for side in ('rows', 'columns'):
        if any(gram(side, i, i) != (3, 0) for i in range(n)):
            return 'GRAM_DIAGONAL'
    for side in ('rows', 'columns'):
        if any(gram(side, i, j) != (0, 0) for i, j in combinations(range(n), 2)):
            return 'GRAM_OFFDIAGONAL'
    return 'EXACT_UNITARY_AFTER_DIVIDING_BY_SQRT_3'


def matrix_masks(matrix):
    return tuple(sum(1 << j for j, entry in enumerate(row) if entry != 0) for row in matrix)


def record_control(name, expected, actual, details):
    ensure(actual == expected, f'{name}: wanted {expected}, got {actual}')
    return {'name': name, 'expected_reason': expected, 'actual_reason': actual,
            'passed_for_intended_reason': True, **details}


def histogram_scan(size, pair_target, degree_target):
    examined = matches = pair_matches = 0
    maximum = -1
    max_example = None
    for x4 in range(size+1):
        for x3 in range(size-x4+1):
            for x2 in range(size-x4-x3+1):
                for x1 in range(size-x4-x3-x2+1):
                    x0 = size-x1-x2-x3-x4
                    hist = [x0, x1, x2, x3, x4]
                    examined += 1
                    pair_sum = x2+3*x3+6*x4
                    degree_sum = x1+2*x2+3*x3+4*x4
                    if pair_sum == pair_target:
                        pair_matches += 1
                        if degree_sum > maximum:
                            maximum, max_example = degree_sum, hist
                        matches += degree_sum == degree_target
    ensure(examined == comb(size+4, 4), 'histogram composition coverage failure')
    return {'histograms_examined': examined, 'pair_target_matches': pair_matches,
            'degree_and_pair_target_matches': matches,
            'maximum_degree_sum_given_pair_target': maximum,
            'histogram_at_maximum_x0_to_x4': max_example}


def incidence_design(pair_multiplicity, singles):
    counts = [0]*4
    rows = []
    for i, j in combinations(range(4), 2):
        for _ in range(pair_multiplicity[(i, j)]):
            rows.append([i, j])
            counts[i] += 1
            counts[j] += 1
    for i, amount in enumerate(singles):
        for _ in range(amount):
            rows.append([i])
            counts[i] += 1
    pair_counts = {f'{i}{j}': sum(i in row and j in row for row in rows)
                   for i, j in combinations(range(4), 2)}
    return {'words': len(rows), 'active_by_coordinate': counts,
            'active_by_coordinate_pair': pair_counts,
            'sum_k': sum(map(len, rows)),
            'sum_choose_k_2': sum(comb(len(row), 2) for row in rows)}


def main():
    started = stamp()
    clock0 = time.monotonic()
    manifest_bytes = MANIFEST.read_bytes()
    ensure(sha(manifest_bytes) == MANIFEST_SHA, 'manifest SHA mismatch')
    manifest = json.loads(manifest_bytes)
    source_records = []
    for item in manifest['inputs_in_read_order']:
        data = Path(item['path']).read_bytes()
        found = {'sha256': sha(data), 'bytes': len(data), 'LF': data.count(b'\n')}
        ensure(all(found[k] == item[k] for k in ('sha256', 'bytes', 'LF')), 'declared source mismatch: '+item['path'])
        if not item['binary']:
            data.decode('utf-8')
        source_records.append({'path': item['path'], **found, 'match': True})

    one = (1, 0)
    w = (0, 1)
    w2 = (-1, -1)
    rational = [[15,20,0],[-12,9,20],[16,-12,15]]
    rational5 = [[15,20,0,0,0],[-12,9,20,0,0],[16,-12,15,0,0],
                 [0,0,0,15,20],[0,0,0,-20,15]]
    rational4 = [[3,4,0,0],[-4,3,0,0],[0,0,3,4],[0,0,-4,3]]
    fourier = [[one,one,one],[one,w,w2],[one,w2,w]]
    controls = []
    def ctrl(name, expected, actual, **detail):
        controls.append(record_control(name, expected, actual, detail))

    r3_masks = matrix_masks(rational)
    r5_masks = matrix_masks(rational5)
    r4_masks = matrix_masks(rational4)
    ensure(r3_masks == (3,7,7) and r5_masks == (3,7,7,24,24) and r4_masks == (3,3,12,12), 'positive support masks')
    ctrl('rational_eight_entry_unitary', 'EXACT_UNITARY', integer_gram_reason(rational,25),
         numerator=rational, denominator=25, row_masks=list(r3_masks), support_size=8)
    ctrl('rational_five_dimensional_direct_sum', 'EXACT_UNITARY', integer_gram_reason(rational5,25),
         numerator=rational5, denominator=25, row_masks=list(r5_masks), support_size=12)
    ctrl('rational_four_dimensional_direct_sum', 'EXACT_UNITARY', integer_gram_reason(rational4,5),
         numerator=rational4, denominator=5, row_masks=list(r4_masks), support_size=8)
    ctrl('fourier_full_unitary', 'EXACT_UNITARY_AFTER_DIVIDING_BY_SQRT_3', omega_gram_reason(fourier),
         numerator_basis='a+b*omega with omega^2=-1-omega', numerator=fourier,
         normalization='1/sqrt(3)', support_size=9)
    ctrl('eight_entry_graph_shape', 'GRAPH_SURVIVOR', graph_reason(r3_masks), components=component_shapes(r3_masks))
    ctrl('fourier_graph_shape', 'GRAPH_SURVIVOR', graph_reason((7,7,7)), components=component_shapes((7,7,7)))
    ctrl('four_dimensional_direct_sum_graph', 'GRAPH_SURVIVOR', graph_reason(r4_masks), components=component_shapes(r4_masks))
    ctrl('five_dimensional_direct_sum_graph', 'GRAPH_SURVIVOR', graph_reason(r5_masks), components=component_shapes(r5_masks))
    ctrl('degree_deletion', 'MIN_DEGREE', graph_reason((1,7,7)),
         base=list(r3_masks), mutated=[1,7,7], change='delete row 0 column 1')
    ctrl('row_single_overlap_deletion', 'ROW_SINGLE_OVERLAP', graph_reason((3,5,7)),
         base=list(r3_masks), mutated=[3,5,7], change='delete row 1 column 1')
    ctrl('column_single_overlap_addition', 'COLUMN_SINGLE_OVERLAP', graph_reason((15,3,12,12)),
         base=list(r4_masks), mutated=[15,3,12,12], change='add row 0 columns 2 and 3')
    rectangles = (3,3,3,28,28)
    ctrl('rectangular_component_reshape', 'RECTANGULAR_COMPONENT', graph_reason(rectangles),
         base=list(r5_masks), mutated=list(rectangles),
         change='move column 2 edges from rows 1,2 to rows 3,4', components=component_shapes(rectangles))
    ctrl('wrong_connected_shape_addition', 'SHAPE_MISMATCH', shape_reason((7,7,7),component_shapes(r3_masks)),
         base=list(r3_masks), mutated=[7,7,7], change='add missing row 0 column 2; both graphs pass prior filters')
    bad_offdiag = [r[:] for r in rational]
    bad_offdiag[1][0] *= -1
    ctrl('rational_sign_flip', 'GRAM_OFFDIAGONAL', integer_gram_reason(bad_offdiag,25),
         change='negate numerator entry row 1 column 0; support and column/row norm values preserved')
    bad_diag = [r[:] for r in rational]
    bad_diag[0][0] += 1
    ctrl('rational_magnitude_change', 'GRAM_DIAGONAL', integer_gram_reason(bad_diag,25),
         change='increase numerator entry row 0 column 0 by one; support preserved')
    bad_fourier = [r[:] for r in fourier]
    bad_fourier[1][1] = one
    ctrl('fourier_phase_change', 'GRAM_OFFDIAGONAL', omega_gram_reason(bad_fourier),
         change='replace omega by 1 at row 1 column 1; support and diagonal Gram preserved')

    finite = []
    for n in (2,3,4):
        for excess in (1,2,3):
            edge_count = 2*n+excess
            counts = Counter()
            shapes = Counter()
            samples = {}
            for edges in combinations(range(n*n), edge_count):
                counts['all_labeled_edge_sets'] += 1
                rows = tuple(sum(1 << (edge % n) for edge in edges if edge // n == i) for i in range(n))
                reason = graph_reason(rows)
                if reason == 'MIN_DEGREE':
                    continue
                ensure(reason != 'INVALID_SQUARE_MASKS', 'internally generated malformed masks')
                counts['minimum_degree_both_sides'] += 1
                if reason == 'ROW_SINGLE_OVERLAP':
                    continue
                counts['no_single_row_overlap'] += 1
                if reason == 'COLUMN_SINGLE_OVERLAP':
                    continue
                counts['no_single_overlap_either_side'] += 1
                if reason == 'RECTANGULAR_COMPONENT':
                    continue
                ensure(reason == 'GRAPH_SURVIVOR', 'unexpected graph reason')
                counts['square_components'] += 1
                signature = json.dumps(component_shapes(rows), sort_keys=True, separators=(',', ':'))
                shapes[signature] += 1
                samples.setdefault(signature, list(rows))
            ensure(counts['all_labeled_edge_sets'] == comb(n*n, edge_count), f'edge subset coverage n={n}, k={edge_count}')
            finite.append({'n': n, 'excess': excess, 'edges': edge_count,
                           'counts': {name: counts[name] for name in ('all_labeled_edge_sets','minimum_degree_both_sides',
                               'no_single_row_overlap','no_single_overlap_either_side','square_components')},
                           'surviving_exact_component_shape_classes': [
                               {'components': json.loads(key), 'labeled_graphs': count, 'example_row_masks': samples[key]}
                               for key, count in sorted(shapes.items())]})
    by_case = {(v['n'],v['edges']):v for v in finite}
    ensure(by_case[(3,8)]['counts']['square_components'] == 9, 'positive eight-entry orbit coverage')
    ensure(by_case[(3,9)]['counts']['square_components'] == 1, 'positive full orbit coverage')
    ensure(all(x['counts']['square_components'] == 0 for x in finite if (x['n'],x['edges']) not in ((3,8),(3,9))),
           'unexpected additional survivor requiring assessment')

    scan = histogram_scan(29,12,44)
    ensure(scan['degree_and_pair_target_matches'] == 0 and scan['maximum_degree_sum_given_pair_target'] == 41,
           '29-word active-incidence contradiction not found')
    pairs = list(combinations(range(4),2))
    design32 = incidence_design({pair:2 for pair in pairs}, [5,5,5,5])
    ensure(design32['words'] == 32 and design32['active_by_coordinate'] == [11]*4
           and list(design32['active_by_coordinate_pair'].values()) == [2]*6
           and (design32['sum_k'],design32['sum_choose_k_2']) == (44,12), '32-word relaxed control')
    multiplicity = {pair: (3 if pair in ((0,1),(0,2),(1,2)) else 2) for pair in pairs}
    design15 = incidence_design(multiplicity, [3,3,3,5])
    ensure(design15['words'] == 29 and design15['active_by_coordinate'] == [11]*4
           and (design15['sum_k'],design15['sum_choose_k_2']) == (44,15), '15-pair relaxed control')
    ctrl('incidence_29_44_12', 'INCONSISTENT_44_12',
         'INCONSISTENT_44_12' if scan['degree_and_pair_target_matches'] == 0 else 'CONSISTENT', scan=scan)
    ctrl('incidence_relax_word_count_to_32', 'CONSISTENT_ABSTRACT_INCIDENCE',
         'CONSISTENT_ABSTRACT_INCIDENCE' if design32['words'] == 32 else 'BAD_WORD_COUNT', design=design32)
    ctrl('incidence_relax_pair_sum_to_15', 'CONSISTENT_ABSTRACT_INCIDENCE',
         'CONSISTENT_ABSTRACT_INCIDENCE' if design15['sum_choose_k_2'] == 15 else 'BAD_PAIR_COUNT', design=design15)

    receipt = {'schema': 'independent-finite-support-review-v1',
               'start_native_clock': started, 'end_native_clock_before_receipt_creation': stamp(),
               'elapsed_seconds_before_receipt_creation': time.monotonic()-clock0,
               'python_version': sys.version, 'platform': platform.platform(),
               'command': 'python3 -B finite-enumerate-v1.py',
               'checker_sha256': sha(Path(__file__).read_bytes()),
               'manifest': {'path':str(MANIFEST), 'sha256':sha(manifest_bytes), 'bytes':len(manifest_bytes),
                            'LF':manifest_bytes.count(b'\n')},
               'declared_inputs_in_manifest_order':source_records,
               'enumeration':finite, 'controls':controls,
               'limits':['The enumeration is only n=2,3,4.',
                         'The n=5 rectangular example is a targeted control, not an n=5 exhaustive enumeration.',
                         'No claim of all-n classification, physical interpretation, novelty, human review, independent model family or kernel proof.',
                         'Incidence controls are abstract active-coordinate multisets, not quadruple-support or unitary witnesses.']}
    with RECEIPT.open('x', encoding='utf-8') as output:
        json.dump(receipt, output, indent=2, sort_keys=True)
        output.write('\n')
    print(json.dumps({'receipt':str(RECEIPT), 'checker_sha256':receipt['checker_sha256'],
                      'receipt_sha256':sha(RECEIPT.read_bytes()), 'start':started,
                      'end_before_receipt':receipt['end_native_clock_before_receipt_creation'],
                      'elapsed_seconds':receipt['elapsed_seconds_before_receipt_creation'],
                      'cases':len(finite), 'intended_reason_controls':len(controls),
                      'all_controls_passed':all(x['passed_for_intended_reason'] for x in controls)}, indent=2))


if __name__ == '__main__':
    main()
