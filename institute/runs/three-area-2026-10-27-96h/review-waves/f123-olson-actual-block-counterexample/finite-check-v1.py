#!/usr/bin/env python3
"""Finite actual-word diagnostic; no author checker is imported or executed.

Represent r^a s^b by (a,b), with s r s = r^(-1).  Full cyclic words,
not their rotation-deleted projections, determine actual reflection blocks.
The reverse scan counts every original-index reflection subsequence by its full
product.  No conclusion is drawn about other primes or a named SEL predicate.
"""
import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations
import json
from math import comb
from pathlib import Path
import subprocess
import sys

MANIFEST = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f123-olson-actual-block-counterexample/manifest-v1.json')
MANIFEST_SHA = '71777b4b6013d9775a9fd78e1ea6b27602f2e707a9d903cd19cabee504155e39'
P11_SELECTOR = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 27, 29, 31, 33, 35, 37, 38, 39, 41]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def frozen_inputs():
    data = MANIFEST.read_bytes()
    require(sha256(data).hexdigest() == MANIFEST_SHA, 'manifest SHA-256 mismatch')
    manifest = json.loads(data)
    pins = [{'role': 'manifest', 'path': str(MANIFEST), 'sha256': MANIFEST_SHA,
             'bytes': len(data), 'LF': data.count(b'\n')}]
    for entry in manifest['inputs_in_read_order']:
        content = Path(entry['path']).read_bytes()
        actual = (sha256(content).hexdigest(), len(content), content.count(b'\n'))
        expected = (entry['sha256'], entry['bytes'], entry['LF'])
        require(actual == expected, 'input pin mismatch: ' + entry['path'])
        pins.append({'role': entry['role'], 'path': entry['path'],
                     'sha256': actual[0], 'bytes': actual[1], 'LF': actual[2]})
    return pins


def multiply(left, right, p):
    a, b = left
    c, d = right
    return ((a + (c if b == 0 else -c)) % p, b ^ d)


def product(word, indices, p):
    x = (0, 0)
    for i in indices:
        x = multiply(x, word[i], p)
    return x


def word_for(p):
    z, rho = (0, 1), (1, 0)
    word = [z, rho, z, rho] + [z] * (2 * p - 3) + [rho]
    for j in range(1, p - 1):
        word.extend([(j, 1), rho])
    word.append((p - 1, 1))
    return word


def reflection_indices(word):
    return [i for i, (_, kind) in enumerate(word) if kind == 1]


def actual_blocks(word):
    """Start only at full-token cyclic boundaries and walk contiguous tokens."""
    n = len(word)
    refs = reflection_indices(word)
    require(n > 0 and refs, 'a nonempty word with reflections is required')
    starts = [i for i in refs if word[(i - 1) % n] != word[i]]
    if not starts:
        require(len(refs) == n, 'no start despite a rotation')
        return [{'value': word[0][0], 'positions': list(range(n)), 'length': n}]
    blocks = []
    for start in starts:
        positions = [start]
        i = (start + 1) % n
        while i != start and word[i] == word[start]:
            positions.append(i)
            i = (i + 1) % n
        blocks.append({'value': word[start][0], 'positions': positions, 'length': len(positions)})
    require(sorted(i for b in blocks for i in b['positions']) == refs,
            'actual cyclic blocks do not partition reflection positions')
    return blocks


def projected_runs(word):
    """Separately group the cyclic rotation-deleted reflection sequence."""
    refs = reflection_indices(word)
    labels = [word[i][0] for i in refs]
    require(labels, 'projection must contain reflections')
    m = len(labels)
    starts = [q for q in range(m) if labels[q] != labels[(q - 1) % m]]
    if not starts:
        return [{'value': labels[0], 'reflection_positions': refs, 'length': m}]
    runs = []
    for start in starts:
        positions = [refs[start]]
        q = (start + 1) % m
        while q != start and labels[q] == labels[start]:
            positions.append(refs[q])
            q = (q + 1) % m
        runs.append({'value': labels[start], 'reflection_positions': positions,
                     'length': len(positions)})
    require(sorted(i for b in runs for i in b['reflection_positions']) == refs,
            'projected runs do not partition reflection positions')
    return runs


def parity_counts(blocks):
    return {'odd': sum(b['length'] % 2 == 1 for b in blocks),
            'even': sum(b['length'] % 2 == 0 for b in blocks)}


def raw_graph(word):
    """Each reflection is a vertex; inspect its entire actual gap including wrap."""
    n = len(word)
    refs = reflection_indices(word)
    require(len(refs) >= 3, 'raw graph fixture requires at least three reflections')
    gaps, edges = [], []
    for q, i in enumerate(refs):
        j = refs[(q + 1) % len(refs)]
        positions = [(i + d) % n for d in range(1, (j - i) % n)]
        require(all(word[k][1] == 0 for k in positions), 'gap contains a reflection')
        equal = word[i][0] == word[j][0]
        present = bool(positions) or not equal
        gaps.append({'from_reflection_vertex': q,
                     'to_reflection_vertex': (q + 1) % len(refs),
                     'rotation_positions': positions, 'equal_endpoints': equal,
                     'edge_present': present})
        if present:
            edges.append((q, (q + 1) % len(refs)))
    return refs, gaps, edges


def graph_info(vertex_count, edges):
    neighbors = [set() for _ in range(vertex_count)]
    for a, b in edges:
        require(a != b and 0 <= a < vertex_count and 0 <= b < vertex_count,
                'invalid edge')
        neighbors[a].add(b)
        neighbors[b].add(a)
    require(sum(map(len, neighbors)) == 2 * len(edges), 'duplicate graph edge')
    unseen = set(range(vertex_count))
    sizes = []
    while unseen:
        root = min(unseen)
        stack = [root]
        unseen.remove(root)
        size = 0
        while stack:
            a = stack.pop()
            size += 1
            for b in neighbors[a] & unseen:
                unseen.remove(b)
                stack.append(b)
        sizes.append(size)

    @lru_cache(maxsize=None)
    def optimum(mask):
        if not mask:
            return ()
        low = mask & -mask
        a = low.bit_length() - 1
        rest = mask ^ low
        best = optimum(rest)
        for b in sorted(neighbors[a]):
            bit = 1 << b
            if rest & bit:
                candidate = ((a, b),) + optimum(rest ^ bit)
                if len(candidate) > len(best):
                    best = candidate
        return best

    matching = optimum((1 << vertex_count) - 1)
    flat = [v for pair in matching for v in pair]
    require(len(flat) == len(set(flat)), 'matching reuses a vertex')
    require(all(b in neighbors[a] for a, b in matching), 'matching uses absent edge')
    return {'components_sorted': sorted(sizes), 'edge_count': len(edges),
            'matching_size_exact': len(matching), 'matching_vertices': matching,
            'matching_dp_states': optimum.cache_info().currsize}


def reverse_count_distribution(word, p, target):
    """Prepend or omit each original reflection, counting all index choices."""
    refs = reflection_indices(word)
    states = {(0, 0, 0): 1}
    for index in reversed(refs):
        updated = dict(states)
        for (k, exponent, parity), count in states.items():
            if k == target:
                continue
            a, b = multiply(word[index], (exponent, parity), p)
            key = (k + 1, a, b)
            updated[key] = updated.get(key, 0) + count
        states = updated
    for k in range(target + 1):
        row = {(a, b): count for (length, a, b), count in states.items() if length == k}
        require(sum(row.values()) == comb(len(refs), k), 'index-subsequence count mismatch')
        require(all(b == k % 2 and 0 <= a < p for a, b in row),
                'product parity or residue invalid')
    return {a: states.get((target, a, target % 2), 0) for a in range(p)}


def direct_distribution(word, p, target):
    counts = Counter()
    for indices in combinations(reflection_indices(word), target):
        counts[product(word, indices, p)] += 1
    return {a: counts[(a, target % 2)] for a in range(p)}


def equal_rotation_triples(word):
    triples = []
    n = len(word)
    for i in range(n):
        j, k = (i + 1) % n, (i + 2) % n
        if word[i][1] == word[k][1] == 1 and word[j][1] == 0 and word[i][0] == word[k][0]:
            triples.append({'indices': [i, j, k], 'reflection_value': word[i][0],
                            'rotation_value': word[j][0]})
    return triples


def move_equal_gap(word):
    changed = list(word)
    require(changed[:5] == [(0, 1), (1, 0), (0, 1), (1, 0), (0, 1)],
            'mutation source is not the first occupied equal gap')
    moved = changed.pop(1)
    zeros = [i for i, token in enumerate(changed) if token == (0, 1)]
    require(zeros[3] == zeros[2] + 1, 'mutation destination is not an empty equal gap')
    destination = zeros[3]
    changed.insert(destination, moved)
    require([x for x in changed if x[1] == 1] == [x for x in word if x[1] == 1],
            'mutation altered the reflection projection')
    return changed, {'removed_original_rotation_index': 1,
                     'inserted_before_mutated_index': destination,
                     'source_reflection_vertices': [0, 1],
                     'destination_reflection_vertices': [2, 3]}


def boundary_controls():
    # The two zero reflections join across the cyclic array boundary.
    wrapped = [(0, 1), (1, 0), (2, 1), (0, 1)]
    actual = actual_blocks(wrapped)
    require(parity_counts(actual) == {'odd': 1, 'even': 1}, 'cyclic block join missed')
    require(any(b['positions'] == [3, 0] for b in actual), 'wrap block indices wrong')
    # Deliberately incorrect: split at the array cut, ignoring cyclic adjacency.
    linear = []
    previous = None
    for i, token in enumerate(wrapped):
        if token[1] == 0:
            previous = None
        elif token != previous:
            linear.append({'length': 1})
            previous = token
        else:
            linear[-1]['length'] += 1
    require(parity_counts(linear) == {'odd': 3, 'even': 0}, 'linear mutant not distinguished')
    _, empty_gaps, _ = raw_graph(wrapped)
    require(empty_gaps[-1]['rotation_positions'] == [] and
            empty_gaps[-1]['equal_endpoints'] and not empty_gaps[-1]['edge_present'],
            'empty equal wrap gap misclassified')
    # Here the array cut lies inside an occupied equal-endpoint gap.
    occupied = [(1, 0), (0, 1), (2, 1), (0, 1)]
    _, occupied_gaps, _ = raw_graph(occupied)
    require(occupied_gaps[-1]['rotation_positions'] == [0] and
            occupied_gaps[-1]['equal_endpoints'] and occupied_gaps[-1]['edge_present'],
            'occupied equal wrap gap misclassified')
    # Deliberate wrong interpretations of internal empty equal and unequal gaps.
    fixture = [(0, 1), (0, 1), (1, 0), (0, 1), (2, 1)]
    _, gaps, _ = raw_graph(fixture)
    correct = [g['edge_present'] for g in gaps]
    wrong_all_empty_occupied = [True if not g['rotation_positions'] else g['edge_present'] for g in gaps]
    wrong_only_occupied = [bool(g['rotation_positions']) for g in gaps]
    require(correct == [False, True, True, True], 'fixture edge vector wrong')
    require(wrong_all_empty_occupied == [True, True, True, True] and
            wrong_only_occupied == [False, True, False, False], 'empty-gap mutants not distinguished')
    return {'cyclic_word': wrapped, 'correct_cyclic_blocks': actual,
            'correct_parity': parity_counts(actual), 'wrong_linear_parity': parity_counts(linear),
            'empty_equal_wrap_gap': empty_gaps[-1],
            'occupied_equal_wrap_word': occupied, 'occupied_equal_wrap_gap': occupied_gaps[-1],
            'internal_gap_fixture': fixture, 'correct_edges_by_cyclic_gap': correct,
            'wrong_all_empty_are_occupied_edges': wrong_all_empty_occupied,
            'wrong_only_occupied_edges': wrong_only_occupied}


def check_case(p):
    word = word_for(p)
    refs = reflection_indices(word)
    rotations = [i for i, (_, kind) in enumerate(word) if kind == 0]
    require(len(word) == 4 * p - 1 and len(refs) == 3 * p - 2 and len(rotations) == p + 1,
            'word token counts incorrect')
    require(all(0 <= a < p and b in (0, 1) for a, b in word), 'invalid group element')
    require(all(word[i][0] != 0 for i in rotations), 'zero rotation')
    labels = Counter(word[i][0] for i in refs)
    require(labels == Counter({0: 2 * p - 1, **{i: 1 for i in range(1, p)}}),
            'reflection multiplicities incorrect')
    actual, projected = actual_blocks(word), projected_runs(word)
    require(parity_counts(actual) == {'odd': p + 2, 'even': 0}, 'actual block parity')
    require(parity_counts(projected) == {'odd': p, 'even': 0}, 'projected run parity')
    require([b['length'] for b in actual if b['value'] == 0] == [1, 1, 2 * p - 3],
            'actual zero blocks')
    require([b['length'] for b in projected if b['value'] == 0] == [2 * p - 1],
            'projected zero run')
    refs2, gaps, edges = raw_graph(word)
    require(refs2 == refs and all(len(g['rotation_positions']) <= 1 for g in gaps),
            'non-singleton actual rotation gap')
    graph = graph_info(len(refs), edges)
    require(graph['components_sorted'] == [1] * (2 * p - 5) + [p + 3], 'raw component sizes')
    require(graph['edge_count'] == p + 2 and graph['matching_size_exact'] == (p + 3) // 2,
            'raw graph matching')
    dist = reverse_count_distribution(word, p, 2 * p)
    require(dist[0] == 0 and all(dist[x] > 0 for x in range(1, p)),
            'reflection-only support not exactly nonzero residues')
    triples = equal_rotation_triples(word)
    require(any(t['indices'] == [0, 1, 2] and t['rotation_value'] != 0 for t in triples),
            'actual equal-reflection rotation triple absent')

    changed, movement = move_equal_gap(word)
    changed_actual = actual_blocks(changed)
    require(parity_counts(changed_actual) == {'odd': p, 'even': 2}, 'moved-gap block counts')
    require(projected_runs(changed) != [], 'empty moved projection')
    require([x for x in changed if x[1] == 1] == [x for x in word if x[1] == 1],
            'moved-gap projection mismatch')
    changed_dist = reverse_count_distribution(changed, p, 2 * p)
    require(changed_dist == dist, 'moved-gap changed all-reflection product distribution')
    _, changed_gaps, changed_edges = raw_graph(changed)
    require(not changed_gaps[0]['edge_present'] and changed_gaps[2]['edge_present'],
            'occupied equal edge did not move')
    changed_graph = graph_info(len(refs), changed_edges)

    # A real positive REF identity: make the first nonzero tail reflection zero,
    # then select the first 2p reflection indices, all of them equal.
    positive = list(word)
    positive[refs[2 * p - 1]] = (0, 1)
    positive_indices = refs[:2 * p]
    require(all(positive[i] == (0, 1) for i in positive_indices), 'positive REF fixture')
    positive_product = product(positive, positive_indices, p)
    require(positive_product == (0, 0), 'positive reflection selector is not identity')
    positive_dist = reverse_count_distribution(positive, p, 2 * p)
    require(positive_dist[0] > 0, 'reverse reachability missed positive REF identity')

    instance = {'p': p, 'word_tokens_0_based': [f"{'s' if b else 'r'}{a}" for a, b in word],
                'word_length': len(word), 'reflections': len(refs), 'rotations': len(rotations),
                'reflection_label_multiplicities': dict(sorted(labels.items())),
                'actual_blocks': actual, 'actual_parity': parity_counts(actual),
                'projected_runs': projected, 'projected_parity': parity_counts(projected),
                'raw_gaps': gaps, 'raw_graph': graph,
                'matching_at_most_p_minus_3': graph['matching_size_exact'] <= p - 3,
                'reflection_2p_product_multiplicities_by_residue': dist,
                'number_of_all_2p_index_choices': sum(dist.values()),
                'equal_reflection_rotation_triples': triples,
                'moved_equal_gap': {'movement': movement,
                                    'actual_blocks': changed_actual,
                                    'actual_parity': parity_counts(changed_actual),
                                    'same_reflection_projection': True,
                                    'same_exact_reflection_product_counts': True,
                                    'raw_graph': changed_graph},
                'positive_reflection_identity_control': {
                    'changed_original_token_index': refs[2 * p - 1],
                    'selected_original_indices': positive_indices,
                    'direct_product': positive_product,
                    'identity_selections_counted_by_reverse_dp': positive_dist[0]}}
    if p == 7:
        brute = direct_distribution(word, p, 2 * p)
        require(brute == dist, 'direct all-index p7 enumeration disagrees with reverse DP')
        instance['p7_direct_all_original_index_enumeration'] = {
            'combinations_enumerated': comb(len(refs), 2 * p),
            'exact_distribution_matches_reverse_dp': True}
    return instance, word


def selector_controls(word):
    p, target = 11, 22
    chosen = P11_SELECTOR
    require(len(chosen) == target and chosen == sorted(set(chosen)) and
            all(0 <= i < len(word) for i in chosen), 'original p11 selector index error')
    trace = []
    acc = (0, 0)
    for index in chosen:
        acc = multiply(acc, word[index], p)
        trace.append({'original_index': index, 'token': word[index], 'prefix_product': acc})
    require(acc == (0, 0), 'original p11 selector does not multiply to identity')
    require(any(word[i][1] == 0 for i in chosen) and any(word[i][1] == 1 for i in chosen),
            'original p11 selector is not mixed')
    chosen_set = set(chosen)
    mutant = None
    for removed in chosen:
        for replacement in range(len(word)):
            if replacement in chosen_set:
                continue
            candidate = sorted((chosen_set - {removed}) | {replacement})
            if product(word, candidate, p) != (0, 0):
                mutant = {'removed_index': removed, 'replacement_index': replacement,
                          'indices': candidate, 'product': product(word, candidate, p)}
                break
        if mutant is not None:
            break
    require(mutant is not None and len(mutant['indices']) == target,
            'nonidentity selector mutation not found')
    return {'original_0_based_indices': chosen, 'length': target,
            'rotation_count': sum(word[i][1] == 0 for i in chosen),
            'reflection_count': sum(word[i][1] == 1 for i in chosen),
            'product': acc, 'prefix_trace': trace,
            'one_index_nonidentity_mutation': mutant}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = clock()
    pins = frozen_inputs()
    source = Path(__file__).read_bytes()
    group_sanity = {}
    for p in (7, 11, 13, 17):
        r, s = (1, 0), (0, 1)
        srs = multiply(multiply(s, r, p), s, p)
        require(multiply(s, s, p) == (0, 0) and srs == (p - 1, 0), 'dihedral law')
        require(product([r] * p, range(p), p) == (0, 0), 'rotation order law')
        group_sanity[p] = {'s_squared': multiply(s, s, p), 's_r_s': srs,
                           'r_to_p': product([r] * p, range(p), p)}
    cases = []
    p11_word = None
    for p in (7, 11, 13, 17):
        result, word = check_case(p)
        cases.append(result)
        if p == 11:
            p11_word = word
    require(p11_word is not None, 'missing p11 case')
    result = {'status': 'PASS_FINITE_DIAGNOSTIC',
              'scope': 'four specified finite words; no all-prime, full L_RES, or named SEL conclusion',
              'SEL_scope_note': 'The frozen packet does not contain the full literal SEL definition. Equal-reflection multiplicity and actual equal-reflection/rotation/equal-reflection triples are counted, but SEL coverage is not independently asserted.',
              'clock_before_run': start, 'input_pins': pins,
              'checker_path': str(Path(__file__).resolve()),
              'checker_sha256': sha256(source).hexdigest(),
              'checker_bytes': len(source), 'checker_LF': source.count(b'\n'),
              'python_version': sys.version,
              'dihedral_group_sanity': group_sanity,
              'boundary_mutation_controls': boundary_controls(),
              'instances': cases, 'p11_original_mixed_selector': selector_controls(p11_word)}
    result['clock_before_exclusive_receipt_write'] = clock()
    with open(args.output, 'x', encoding='utf-8') as out:
        json.dump(result, out, sort_keys=True, indent=2)
        out.write('\n')
    print(json.dumps({'status': result['status'], 'output': args.output,
                      'p': [case['p'] for case in cases],
                      'checker_sha256': result['checker_sha256']}, sort_keys=True))


if __name__ == '__main__':
    main()
