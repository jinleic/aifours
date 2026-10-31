#!/usr/bin/env python3
"""Independent exact replay of the f72 pinned BH(10,5) certificate.

Only stdlib; does not import, execute, or read any author producer/checker.
The receipt is exclusively created only after all checks and controls succeed.
"""
import hashlib
import itertools
import json
import platform
import subprocess
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / 'manifest-v1.json'
RECEIPT = HERE / 'receipt-v1.json'
MANIFEST_SHA = 'f36d49b3d25ce08534a3081f7c491af09ee5a08b0c73e01c12ed6ed83fa2ca46'
BASE = (0, 0, 1, 1, 2, 2, 3, 3, 4, 4)
ZERO = (0,) * 10
FULL = (1 << 10) - 1


class Reject(Exception):
    def __init__(self, code, detail=''):
        self.code = code
        super().__init__(code + (': ' + str(detail) if detail else ''))


def need(condition, code, detail=''):
    if not condition:
        raise Reject(code, detail)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def clock():
    return subprocess.check_output(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True
    ).strip()


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, 'duplicate_json_key', key)
        out[key] = value
    return out


def no_constant(value):
    raise Reject('nonfinite_json_number', value)


def parse_json(data):
    return json.loads(data.decode('utf-8'), object_pairs_hook=unique_object,
                      parse_constant=no_constant)


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def balanced10(a, b):
    counts = [0] * 5
    for x, y in zip(a, b):
        counts[(x - y) % 5] += 1
    return counts == [2] * 5


def generate_rows():
    # Choose positions of each symbol, rather than permuting a multiset or
    # traversing the author's recursive generator. The first zero is fixed.
    candidates = []
    generated = 0
    for zero in range(1, 10):
        positions = tuple(p for p in range(1, 10) if p != zero)
        for one in itertools.combinations(positions, 2):
            rem1 = tuple(p for p in positions if p not in one)
            for two in itertools.combinations(rem1, 2):
                rem2 = tuple(p for p in rem1 if p not in two)
                for three in itertools.combinations(rem2, 2):
                    four = tuple(p for p in rem2 if p not in three)
                    row = [0] * 10
                    for symbol, sites in ((1, one), (2, two), (3, three), (4, four)):
                        for site in sites:
                            row[site] = symbol
                    generated += 1
                    if balanced10(row, BASE):
                        candidates.append(tuple(row))
    candidates.sort()
    need(generated == 22680, 'generation_count', generated)
    need(len(candidates) == len(set(candidates)) == 1075,
         'candidate_count', len(candidates))
    for row in candidates:
        need(row[0] == 0 and balanced10(row, ZERO) and balanced10(row, BASE),
             'generated_row_invalid', row)
    return generated, candidates


def compatibility(rows):
    adjacency = [0] * len(rows)
    count = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if balanced10(rows[i], rows[j]):
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
                count += 1
    return adjacency, count


def eligible_triangles(adjacency):
    triangles = 0
    eligible = {}
    for a, neighbors in enumerate(adjacency):
        for b in bits(neighbors & ~((1 << (a + 1)) - 1)):
            for c in bits(neighbors & adjacency[b] & ~((1 << (b + 1)) - 1)):
                triangles += 1
                common = adjacency[a] & adjacency[b] & adjacency[c]
                if common.bit_count() >= 5:
                    eligible[(a, b, c)] = common.bit_count()
    return triangles, eligible


def column_graph(rows):
    adjacency = [0] * 10
    for c in range(10):
        for d in range(c + 1, 10):
            residues = {(row[d] - row[c]) % 5 for row in rows}
            if len(residues) == 5:
                adjacency[c] |= 1 << d
                adjacency[d] |= 1 << c
    return tuple(adjacency)


def perfect_matching(adjacency):
    @lru_cache(maxsize=None)
    def solve(mask):
        if mask == 0:
            return ()
        firstbit = mask & -mask
        c = firstbit.bit_length() - 1
        for d in bits(adjacency[c] & (mask ^ firstbit)):
            result = solve(mask ^ firstbit ^ (1 << d))
            if result is not None:
                return ((c, d),) + result
        return None
    return solve(FULL)


def record_coverage(records, eligible, row_count):
    need(type(records) is list, 'records_type')
    seen = {}
    for record in records:
        need(type(record) is dict, 'record_type')
        keys = set(record)
        need(keys in ({'triple', 'isolated'}, {'triple', 'odd_component'}),
             'record_keys', sorted(keys))
        t = record['triple']
        need(type(t) is list and len(t) == 3 and
             all(type(x) is int and 0 <= x < row_count for x in t) and
             t[0] < t[1] < t[2], 'triple_format', t)
        triple = tuple(t)
        need(triple in eligible, 'unexpected_triple', triple)
        need(triple not in seen, 'duplicate_triple', triple)
        seen[triple] = record
    missing = eligible.keys() - seen.keys()
    need(not missing, 'missing_triple', min(missing) if missing else '')
    return seen


def verify_witness(record, graph):
    if 'isolated' in record:
        c = record['isolated']
        need(type(c) is int and 0 <= c < 10, 'isolate_format', c)
        need(graph[c] == 0, 'isolate_not_isolated', c)
        return 'isolated'
    cut = record['odd_component']
    need(type(cut) is list and all(type(c) is int and 0 <= c < 10 for c in cut)
         and len(set(cut)) == len(cut), 'cut_format', cut)
    need(0 < len(cut) < 10 and len(cut) % 2 == 1, 'cut_parity', cut)
    cutmask = sum(1 << c for c in cut)
    need(all(graph[c] & (FULL ^ cutmask) == 0 for c in cut), 'cut_crosses', cut)
    return 'odd_cut'


def reject_control(name, expected, function, controls):
    try:
        function()
    except Reject as exc:
        need(exc.code == expected, 'wrong_control_rejection',
             (name, expected, exc.code))
        controls[name] = {'result': 'REJECTED', 'reason': exc.code}
        return
    raise Reject('control_not_rejected', name)


def cyclo5(values):
    count = [0] * 5
    for exponent in values:
        count[exponent % 5] += 1
    return tuple(count[i] - count[4] for i in range(4))


def cyclo10(coeff):
    # Phi_10(X) = X^4-X^3+X^2-X+1.
    reduced = list(coeff)
    for k in range(9, 3, -1):
        a = reduced[k]
        reduced[k] = 0
        reduced[k - 1] += a
        reduced[k - 2] -= a
        reduced[k - 3] += a
        reduced[k - 4] -= a
    return tuple(reduced[:4])


def full_bh_clique(adjacency):
    def search(mask, chosen, remaining):
        if remaining == 0:
            return chosen
        while mask.bit_count() >= remaining:
            bit = mask & -mask
            v = bit.bit_length() - 1
            mask -= bit
            result = search(mask & adjacency[v], chosen + (v,), remaining - 1)
            if result is not None:
                return result
        return None
    return search((1 << len(adjacency)) - 1, (), 8)


def dephase(matrix, first, second, pivot):
    secondrow = tuple((matrix[second][c] - matrix[second][pivot] -
                       matrix[first][c] + matrix[first][pivot]) % 5
                      for c in range(10))
    order = (pivot,) + tuple(sorted((c for c in range(10) if c != pivot),
                                    key=lambda c: (secondrow[c], c)))
    normalized = tuple(tuple((matrix[t][c] - matrix[t][pivot] -
                              matrix[first][c] + matrix[first][pivot]) % 5
                             for c in order) for t in range(10))
    need(normalized[first] == ZERO and normalized[second] == BASE and
         all(row[0] == 0 for row in normalized), 'normalization_failure')
    return order, normalized


def permuted_graph(graph, order):
    return tuple(sum(1 << j for j, oldj in enumerate(order)
                     if graph[oldi] & (1 << oldj)) for oldi in order)


def main():
    observed_start = clock()
    manifest_bytes = MANIFEST.read_bytes()
    need(sha(manifest_bytes) == MANIFEST_SHA, 'manifest_hash')
    manifest = parse_json(manifest_bytes)
    pins = manifest['inputs_in_read_order']
    need(len(pins) == 2, 'input_manifest_shape')
    inputs = []
    for pin in pins:  # Deliberately read the entire proof before the certificate.
        data = Path(pin['path']).read_bytes()
        need(len(data) == pin['bytes'] and data.count(b'\n') == pin['LF'] and
             sha(data) == pin['sha256'], 'input_pin', pin['path'])
        data.decode('utf-8')
        inputs.append(data)
    cert = parse_json(inputs[1])
    need(type(cert) is dict and set(cert) == {
        'row_order', 'candidate_count', 'triples_examined', 'certificates', 'scope'
    }, 'certificate_top_keys')
    need(cert['row_order'] == 'lexicographic deduplicated dephased rows' and
         type(cert['candidate_count']) is int and cert['candidate_count'] == 1075 and
         type(cert['triples_examined']) is int and cert['triples_examined'] == 53065,
         'certificate_metadata')

    generated, rows = generate_rows()
    adjacency, edge_count = compatibility(rows)
    need(edge_count == 26715, 'edge_count', edge_count)
    triangle_count, eligible = eligible_triangles(adjacency)
    need(triangle_count == 53065 and len(eligible) == 16064,
         'triangle_counts', (triangle_count, len(eligible)))
    seen = record_coverage(cert['certificates'], eligible, len(rows))
    graphs = {}
    witness_types = Counter()
    isolate_histogram = Counter()
    for triple in sorted(eligible):
        graph = column_graph((ZERO, BASE) + tuple(rows[i] for i in triple))
        graphs[triple] = graph
        witness_types[verify_witness(seen[triple], graph)] += 1
        isolate_histogram[sum(not neighbors for neighbors in graph)] += 1
        need(perfect_matching(graph) is None, 'matching_survives', triple)
    need(witness_types == {'isolated': 16000, 'odd_cut': 64},
         'witness_distribution', witness_types)
    need(isolate_histogram == {0: 64, 1: 12800, 2: 3200},
         'isolate_distribution', isolate_histogram)

    controls = {}
    records = cert['certificates']
    reject_control('missing_record', 'missing_triple',
                   lambda: record_coverage(records[:-1], eligible, len(rows)), controls)
    reject_control('duplicate_record', 'duplicate_triple',
                   lambda: record_coverage(records + [records[0]], eligible, len(rows)), controls)
    first = records[0]
    malformed = dict(first, triple=[first['triple'][0], first['triple'][0], first['triple'][2]])
    reject_control('malformed_repeated_triple_index', 'triple_format',
                   lambda: record_coverage([malformed] + records[1:], eligible, len(rows)), controls)
    malformed_bool = dict(first, triple=[False, first['triple'][1], first['triple'][2]])
    reject_control('boolean_triple_index', 'triple_format',
                   lambda: record_coverage([malformed_bool] + records[1:], eligible, len(rows)), controls)
    reject_control('unknown_record_field', 'record_keys',
                   lambda: record_coverage([dict(first, extra=0)] + records[1:], eligible, len(rows)), controls)
    invalid = next(t for t in itertools.combinations(range(len(rows)), 3) if t not in eligible)
    reject_control('unexpected_triple', 'unexpected_triple',
                   lambda: record_coverage([dict(first, triple=list(invalid))] + records[1:],
                                           eligible, len(rows)), controls)
    triple = tuple(first['triple'])
    graph = graphs[triple]
    nonisolated = next(i for i, neighbors in enumerate(graph) if neighbors)
    reject_control('false_isolated_vertex', 'isolate_not_isolated',
                   lambda: verify_witness(dict(first, isolated=nonisolated), graph), controls)
    reject_control('out_of_range_isolated_vertex', 'isolate_format',
                   lambda: verify_witness(dict(first, isolated=10), graph), controls)
    odd_record = next(r for r in records if 'odd_component' in r)
    odd_graph = graphs[tuple(odd_record['triple'])]
    cut_vertex = next(i for i, neighbors in enumerate(odd_graph) if neighbors)
    reject_control('odd_cut_crossing_edge', 'cut_crosses',
                   lambda: verify_witness(dict(odd_record, odd_component=[cut_vertex]), odd_graph), controls)
    reject_control('even_cut', 'cut_parity',
                   lambda: verify_witness(dict(odd_record, odd_component=[0, 1]), odd_graph), controls)
    reject_control('repeated_cut_vertex', 'cut_format',
                   lambda: verify_witness(dict(odd_record, odd_component=[0, 0, 1]), odd_graph), controls)
    reject_control('duplicate_json_key', 'duplicate_json_key',
                   lambda: parse_json(b'{"x":1,"x":2}'), controls)

    # A matching-positive half-frame: it is a valid triangle but has no outside
    # common candidate at all, so it must not be in the extension superset.
    half = tuple(tuple(map(int, s)) for s in (
        '0000000000', '0121230434', '0242410313', '0313140242', '0434320121'))
    need(all(balanced10(a, b) for a, b in itertools.combinations(half, 2)),
         'positive_half_row_orthogonality')
    half_matching = perfect_matching(column_graph(half))
    signatures = Counter(tuple(row[c] for row in half) for c in range(10))
    need(half_matching is not None and len(half_matching) == 5 and
         len(signatures) == 5 and set(signatures.values()) == {2}, 'positive_half_control')
    padded_half = half + half  # Only first five rows are used in this normalization.
    _, norm_half = dephase(padded_half, 0, 1, 0)
    row_index = {row: i for i, row in enumerate(rows)}
    half_triple = tuple(sorted(row_index[row] for row in norm_half[2:5]))
    half_common = (adjacency[half_triple[0]] & adjacency[half_triple[1]] &
                   adjacency[half_triple[2]]).bit_count()
    need(half_common < 5 and half_triple not in eligible, 'extension_filter_control')
    controls['matching_positive_half_but_nonextendible'] = {
        'result': 'PASS', 'matching': half_matching, 'normalized_triple': half_triple,
        'common_neighbors': half_common, 'signature_multiplicities': sorted(signatures.values())}

    # Construct one actual BH example without reading an author matrix. This
    # is a positive control, not a classification or enumeration of all BHs.
    clique = full_bh_clique(adjacency)
    need(clique is not None and len(clique) == 8, 'sample_bh_not_found')
    matrix = (ZERO, BASE) + tuple(rows[i] for i in clique)
    need(all(balanced10(a, b) for a, b in itertools.combinations(matrix, 2)),
         'sample_bh_row_check')
    columns = tuple(tuple(matrix[t][c] for t in range(10)) for c in range(10))
    need(all(balanced10(a, b) for a, b in itertools.combinations(columns, 2)),
         'sample_bh_column_check')

    # Compute actual physical vector inner products in Z[X]/Phi_10(X).
    physical = {(r, c): tuple((r*t + 2*matrix[t][c]) % 10 for t in range(10))
                for r in range(10) for c in range(10)}
    basis_pairs = 0
    for c in range(10):
        for r, s in itertools.combinations(range(10), 2):
            coeff = [0] * 10
            for x, y in zip(physical[r, c], physical[s, c]):
                coeff[(y-x) % 10] += 1
            need(cyclo10(coeff) == (0, 0, 0, 0), 'physical_column_basis', (r, s, c))
            basis_pairs += 1
    for r in range(10):
        for c, d in itertools.combinations(range(10), 2):
            coeff = [0] * 10
            for x, y in zip(physical[r, c], physical[r, d]):
                coeff[(y-x) % 10] += 1
            need(cyclo10(coeff) == (0, 0, 0, 0), 'physical_row_basis', (r, c, d))
            basis_pairs += 1

    gauged = tuple(tuple((matrix[t][c] + (3*t+1) + (2*c+3)) % 5
                          for c in range(10)) for t in range(10))
    half_count = dephasing_count = physical_opposite_count = 0
    wrong_conjugation = wrong_fourier_sign = None
    for e in itertools.combinations(range(10), 5):
        other = tuple(t for t in range(10) if t not in e)
        order_t = tuple(itertools.chain.from_iterable(zip(e, other)))
        gamma = column_graph(tuple(matrix[t] for t in e))
        need(gamma == column_graph(tuple(gauged[t] for t in e)), 'gauge_graph_changed', e)
        half_count += 1
        for c, d in itertools.combinations(range(10), 2):
            differences = tuple((matrix[t][d] - matrix[t][c]) % 5 for t in range(10))
            se = cyclo5(differences[t] for t in e)
            so = cyclo5(differences[t] for t in other)
            need(all(se[i] + so[i] == 0 for i in range(4)), 'sample_column_sum')
            edge = bool(gamma[c] & (1 << d))
            need(edge == (se == (0, 0, 0, 0)), 'cyclotomic_edge_sign', (e, c, d))
            wrong_add = len({(matrix[t][d] + matrix[t][c]) % 5 for t in e}) == 5
            if wrong_conjugation is None and edge != wrong_add:
                wrong_conjugation = {'E': e, 'c': c, 'd': d,
                                     'correct_edge': edge, 'wrong_add_edge': wrong_add}
            if wrong_fourier_sign is None and not edge:
                wrong_fourier_sign = {'E': e, 'c': c, 'd': d,
                                      'S_E': se, 'S_O': so,
                                      'wrong_plus_is_zero': True,
                                      'correct_minus_is_zero': False}
            for r in range(5):
                actual = [0] * 10
                expected = [0] * 10
                for t, old_t in enumerate(order_t):
                    x = (r*t + 2*matrix[old_t][c]) % 10
                    y = ((r+5)*t + 2*matrix[old_t][d]) % 10
                    actual[(y-x) % 10] += 1
                    expected[(2*differences[old_t]) % 10] += 1 if t % 2 == 0 else -1
                need(cyclo10(actual) == cyclo10(expected), 'physical_opposite_sign', (e, c, d, r))
                need((cyclo10(actual) == (0, 0, 0, 0)) == edge,
                     'physical_opposite_zero', (e, c, d, r))
                physical_opposite_count += 1
        for firstrow in e:
            for secondrow in e:
                if secondrow == firstrow:
                    continue
                for pivot in range(10):
                    order, normalized = dephase(matrix, firstrow, secondrow, pivot)
                    selected = tuple(sorted(row_index[normalized[t]] for t in e
                                            if t != firstrow and t != secondrow))
                    need(selected in seen, 'sample_dephasing_not_covered', (e, selected))
                    need(graphs[selected] == permuted_graph(gamma, order),
                         'dephased_graph_mismatch', (e, selected))
                    common = adjacency[selected[0]] & adjacency[selected[1]] & adjacency[selected[2]]
                    outside = [row_index[normalized[t]] for t in other]
                    need(len(set(outside)) == 5 and all(common & (1 << v) for v in outside),
                         'outside_rows_not_common', (e, selected))
                    dephasing_count += 1
    need(half_count == 252 and dephasing_count == 50400 and
         physical_opposite_count == 56700, 'sample_scope_counts',
         (half_count, dephasing_count, physical_opposite_count))
    need(wrong_conjugation is not None and wrong_fourier_sign is not None, 'sign_control_missing')
    controls['wrong_conjugation_sign'] = {'result': 'DISTINGUISHED', **wrong_conjugation}
    controls['wrong_opposite_fourier_plus_sign'] = {'result': 'DISTINGUISHED', **wrong_fourier_sign}
    controls['sample_row_column_gauge'] = {'result': 'PASS', 'halves': half_count}
    controls['sample_all_half_row_pivot_normalizations'] = {
        'result': 'PASS', 'halves': half_count, 'normalizations': dephasing_count}
    controls['actual_physical_basis_and_opposite_pairs'] = {
        'result': 'PASS', 'basis_inner_products': basis_pairs,
        'opposite_row_inner_products': physical_opposite_count}

    receipt = {
        'schema_version': 1,
        'kind': 'INDEPENDENT_F72_EXACT_REPLAY',
        'observed_start_native_clock': observed_start,
        'observed_clock_before_receipt_creation': clock(),
        'python': sys.version,
        'platform': platform.platform(),
        'manifest': {'path': str(MANIFEST), 'bytes': len(manifest_bytes), 'sha256': sha(manifest_bytes)},
        'pinned_inputs_in_read_order': [dict(path=pin['path'], bytes=len(data),
            LF=data.count(b'\n'), sha256=sha(data)) for pin, data in zip(pins, inputs)],
        'checker': {'path': str(Path(__file__).resolve()),
                    'sha256': sha(Path(__file__).read_bytes())},
        'complete_finite_checks': {
            'balanced_rows_before_filter': generated, 'candidate_rows': len(rows),
            'compatibility_edges': edge_count, 'all_triangles': triangle_count,
            'eligible_triangles_with_at_least_five_common_neighbors': len(eligible),
            'certificate_records_exactly_once': len(seen),
            'verified_isolated_witnesses': witness_types['isolated'],
            'verified_odd_cut_witnesses': witness_types['odd_cut'],
            'isolate_count_histogram': dict(sorted(isolate_histogram.items())),
            'independent_matching_dp_no_perfect_matching': len(graphs),
        },
        'sample_bh_control': {'clique_indices': clique,
                              'exponent_rows': [''.join(map(str, row)) for row in matrix],
                              'all_halves': half_count,
                              'first_second_pivot_normalizations': dephasing_count,
                              'physical_opposite_pairs': physical_opposite_count},
        'controls': controls,
        'limitations': [
            'Entire finite certificate was checked; the positive actual BH is one example only.',
            'Universality over BH matrices depends on the separate written normalization and physical caller.',
            'No arbitrary complex Hadamard, arbitrary QLS10, classification, formal-kernel or priority claim.',
            'No author checker or producer was read, imported or executed.',
        ],
    }
    with RECEIPT.open('x', encoding='utf-8') as out:
        json.dump(receipt, out, indent=2, sort_keys=True)
        out.write('\n')
    print('PASS: complete finite replay, witnesses, independent matching DP and targeted controls')
    print('PASS: one BH sample, all 252 halves and 50400 first/second/pivot normalizations')
    print('receipt', RECEIPT)
    print('clock', receipt['observed_clock_before_receipt_creation'])


if __name__ == '__main__':
    try:
        main()
    except Reject as exc:
        print('FAIL', exc, file=sys.stderr)
        sys.exit(1)
