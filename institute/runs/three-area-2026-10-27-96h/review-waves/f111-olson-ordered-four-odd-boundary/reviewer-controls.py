#!/usr/bin/env python3
"""Independent finite controls for the ordered-four and actual-word argument.

Only the Python standard library is used; this does not read, import, or run
any author program or data. All word indices in the receipt are zero based.
"""
from collections import Counter
from itertools import combinations, product
import argparse
import hashlib
import json
from pathlib import Path


def quadruple_zero(word, indices, p):
    a, b, c, d = (word[i] for i in indices)
    return (a + c - b - d) % p == 0


def find_quadruple(word, p):
    return next((q for q in combinations(range(len(word)), 4)
                 if quadruple_zero(word, q, p)), None)


def proof_for_triple_double(word, positions, a, b, p):
    apos, bpos = positions[a], positions[b]
    lo, hi = bpos
    regions = ([i for i in apos if i < lo],
               [i for i in apos if lo < i < hi],
               [i for i in apos if i > hi])
    pair = next((r[:2] for r in regions if len(r) >= 2), None)
    if pair is not None:
        witness = tuple(sorted(pair + bpos))
    else:
        assert tuple(map(len, regions)) == (1, 1, 1)
        witness = (apos[0], bpos[0], bpos[1], apos[2])
    assert len(set(witness)) == 4 and quadruple_zero(word, witness, p)
    return witness


def crossing_witness(word, p, a, b, apos, bpos, index):
    # The target is x=2a-b. Explicit positional witnesses are checked even
    # when x occurs between the other repeated value's two occurrences.
    x = (2 * a - b) % p
    assert word[index] == x and x not in (a, b)
    a1, a2 = apos
    b1, b2 = bpos
    if a1 < b1 < a2 < b2:
        if index < a1:
            q = (index, a1, b1, a2)
        elif index < a2:
            q = (a1, index, a2, b2)
        else:
            q = (a1, b1, a2, index)
    else:
        assert b1 < a1 < b2 < a2
        if index < a1:
            q = (index, a1, b2, a2)
        elif index < a2:
            q = (b1, a1, index, a2)
        else:
            q = (a1, b2, a2, index)
    assert tuple(sorted(set(q))) == q and quadruple_zero(word, q, p)
    return q


def audit_all_words(p):
    n = p + 2
    counts = Counter()
    for w in product(range(p), repeat=n):
        if any(w[i] == w[i + 1] for i in range(n - 1)):
            continue
        counts['words'] += 1
        witness = find_quadruple(w, p)
        assert witness is not None
        counts['with_original_order_zero'] += 1
        positions = {a: [i for i, v in enumerate(w) if v == a]
                     for a in set(w)}
        repeated = [a for a in positions if len(positions[a]) == 2]
        max_mult = max(map(len, positions.values()))
        if len(positions) == p:
            counts['full_support'] += 1
            for i in range(n - 2):
                t = (w[i] - w[i + 1] + w[i + 2]) % p
                for j in positions[t]:
                    if j < i or j > i + 2:
                        q = tuple(sorted((i, i + 1, i + 2, j)))
                        assert quadruple_zero(w, q, p)
                        counts['full_support_external_occurrences'] += 1
                    else:
                        assert j == i + 1
                        assert (w[i + 1] - w[i]) % p == (w[i + 2] - w[i + 1]) % p
                        counts['full_support_internal_occurrences'] += 1
        if max_mult >= 4:
            a = next(a for a in positions if len(positions[a]) >= 4)
            assert quadruple_zero(w, tuple(positions[a][:4]), p)
            counts['four_or_more'] += 1
        elif max_mult == 3:
            a = next(a for a in positions if len(positions[a]) == 3)
            other = next((b for b in positions if b != a and len(positions[b]) >= 2), None)
            if other is None:
                assert len(positions) == p
                counts['triple_only_full_support'] += 1
            else:
                # If the other value is also tripled, choose any two of it.
                reduced = dict(positions)
                reduced[other] = positions[other][:2]
                proof_for_triple_double(w, reduced, a, other, p)
                counts['triple_plus_repeat'] += 1
        else:
            assert max_mult <= 2 and len(repeated) >= 2
            counts['all_multiplicities_at_most_two'] += 1
            all_cross = True
            for a, b in combinations(repeated, 2):
                labelled = sorted([(j, a) for j in positions[a]] +
                                  [(j, b) for j in positions[b]])
                labels = tuple(v for _, v in labelled)
                q = tuple(i for i, _ in labelled)
                cross = labels in ((a, b, a, b), (b, a, b, a))
                if cross:
                    counts['crossing_pairs'] += 1
                    x = (2 * a - b) % p
                    for i in positions.get(x, []):
                        crossing_witness(w, p, a, b, positions[a], positions[b], i)
                        counts['crossing_target_occurrences'] += 1
                else:
                    all_cross = False
                    assert quadruple_zero(w, q, p)
                    kind = 'nested_pairs' if labels in ((a, b, b, a), (b, a, a, b)) else 'disjoint_pairs'
                    counts[kind] += 1
            if all_cross:
                counts['all_intervals_cross'] += 1
                a = repeated[0]
                targets = [(2 * a - b) % p for b in repeated if b != a]
                assert len(targets) == len(set(targets)) == len(repeated) - 1
                missing = set(range(p)) - set(w)
                assert len(missing) == len(repeated) - 2
                present_b = next(b for b in repeated if b != a and (2 * a - b) % p in positions)
                x = (2 * a - present_b) % p
                crossing_witness(w, p, a, present_b, positions[a], positions[present_b], positions[x][0])
                counts['pigeonhole_injection_witness'] += 1
    assert counts['words'] == p * (p - 1) ** (p + 1)
    assert counts['words'] == counts['with_original_order_zero']
    return dict(sorted(counts.items()))


def audit_local_patterns():
    counts = {}
    for p in (3, 5, 7, 11):
        c = Counter()
        for a in range(p):
            for b in range(p):
                if a == b:
                    continue
                # Every arrangement of three a's and two b's.
                for apos in combinations(range(5), 3):
                    w = tuple(a if i in apos else b for i in range(5))
                    positions = {a: [i for i, z in enumerate(w) if z == a],
                                 b: [i for i, z in enumerate(w) if z == b]}
                    proof_for_triple_double(w, positions, a, b, p)
                    c['triple_double_arrangements'] += 1
                # Every ordering of the two occurrence intervals.
                for apos in combinations(range(4), 2):
                    w = tuple(a if i in apos else b for i in range(4))
                    if w in ((a, b, a, b), (b, a, b, a)):
                        assert not quadruple_zero(w, (0, 1, 2, 3), p)
                        c['crossing_without_x'] += 1
                    else:
                        assert quadruple_zero(w, (0, 1, 2, 3), p)
                        c['disjoint_or_nested'] += 1
                x = (2 * a - b) % p
                assert x not in (a, b)
                for base in ((a, b, a, b), (b, a, b, a)):
                    for insert in range(5):
                        w = base[:insert] + (x,) + base[insert:]
                        ap = [i for i, z in enumerate(w) if z == a]
                        bp = [i for i, z in enumerate(w) if z == b]
                        crossing_witness(w, p, a, b, ap, bp, insert)
                        c['crossing_target_insertions'] += 1
        for a in range(p):
            for d in range(1, p):
                w = tuple((a + i * d) % p for i in range(p + 2))
                assert quadruple_zero(w, (0, 1, 2, p + 1), p)
                c['arithmetic_progressions'] += 1
        counts[str(p)] = dict(sorted(c.items()))
    return counts


def path_matching(edges):
    # Dynamic programming on consecutive vertices, independent of component counts.
    prev2, prev1 = 0, 0
    for edge in edges:
        prev2, prev1 = prev1, max(prev1, prev2 + int(edge))
    return prev1


def cycle_matching(bits):
    without_wrap = path_matching(bits[:-1])
    with_wrap = 1 + path_matching(bits[1:-2]) if bits[-1] else 0
    return max(without_wrap, with_wrap)


def component_sizes(bits):
    n = len(bits)
    seen = set()
    sizes = []
    for seed in range(n):
        if seed in seen:
            continue
        stack = [seed]
        seen.add(seed)
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            for u, edge in (((v + 1) % n, bits[v]),
                            ((v - 1) % n, bits[(v - 1) % n])):
                if edge and u not in seen:
                    seen.add(u)
                    stack.append(u)
        sizes.append(size)
    return sizes


def audit_raw_graphs():
    summary = {}
    for p in (3, 5, 7):
        n = 3 * p - 2
        proper = 0
        lower = 0
        for mask in range(1 << n):
            bits = tuple((mask >> i) & 1 for i in range(n))
            match = cycle_matching(bits)
            if mask == (1 << n) - 1:
                assert match == n // 2
                continue
            sizes = component_sizes(bits)
            absent = n - sum(bits)
            odd = sum(s % 2 for s in sizes)
            assert len(sizes) == absent
            assert match == (n - odd) // 2
            if match <= p - 3:
                assert odd >= p + 4 and absent >= p + 4
                lower += 1
            proper += 1
        summary[str(p)] = {'vertices': n, 'proper_graphs': proper,
                           'full_cycles': 1, 'lower_matching_graphs': lower}
    return summary


def get_runs(refs):
    # refs are (full-word index, label), ordered linearly in the original word.
    n = len(refs)
    boundary = next(i for i in range(n) if refs[i][1] != refs[(i - 1) % n][1])
    ordered = refs[boundary:] + refs[:boundary]
    runs = []
    for pair in ordered:
        if not runs or runs[-1][-1][1] != pair[1]:
            runs.append([pair])
        else:
            runs[-1].append(pair)
    assert runs[0][0][1] != runs[-1][-1][1]
    return runs


def make_word(p, variant):
    if variant == 'e0':
        labels = [i % p for i in range(p + 2)]
        specs = [(z, 1 + 2 * (p - 2) if i == 0 else 1)
                 for i, z in enumerate(labels)]
    elif variant == 'e1_equal':
        labels = [0, 1, 1] + list(range(2, p)) + [1]
        specs = [(z, 1 + 2 * (p - 3) if i == 0 else 1)
                 for i, z in enumerate(labels)]
        specs.insert(2, (0, 2))
    elif variant == 'e1_unequal':
        labels = [i % p for i in range(p + 2)]
        specs = [(z, 1 + 2 * (p - 3) if i == 0 else 1)
                 for i, z in enumerate(labels)]
        specs.insert(1, (2, 2))
    else:
        raise ValueError(variant)
    assert len(labels) == p + 2
    assert all(specs[i][0] != specs[(i + 1) % len(specs)][0]
               for i in range(len(specs)))
    refs = [z for z, length in specs for _ in range(length)]
    assert len(refs) == 3 * p - 2
    refs = refs[1:] + refs[:1]  # original start is deliberately inside a long run when possible
    word = []
    rotation_count = 0
    for i, z in enumerate(refs):
        if i % 2 == 0 and rotation_count < p + 1:
            rotation_count += 1
            word.append(('r', 1 + (rotation_count - 1) % (p - 1)))
        word.append(('s', z))
    assert rotation_count == p + 1 and len(word) == 4 * p - 1
    return word


def perm_product(word, indices, p):
    # Compose permutations of F_p directly; no alternating-sum product routine.
    result = tuple(range(p))
    for i in indices:
        typ, value = word[i]
        factor = tuple((t + value) % p if typ == 'r' else (value - t) % p
                       for t in range(p))
        result = tuple(result[factor[t]] for t in range(p))
    return result


def check_selector(word, indices, p):
    if len(indices) != 2 * p or list(indices) != sorted(set(indices)):
        raise ValueError('selector count/order/distinctness')
    if any(not 0 <= i < len(word) or word[i][0] != 's' for i in indices):
        raise ValueError('selector contains nonreflection')
    if perm_product(word, indices, p) != tuple(range(p)):
        raise ValueError('selected product nonidentity')


def audit_example(p, variant):
    word = make_word(p, variant)
    refs = [(i, value) for i, (typ, value) in enumerate(word) if typ == 's']
    runs = get_runs(refs)
    odds = [i for i, r in enumerate(runs) if len(r) % 2]
    evens = [i for i, r in enumerate(runs) if not len(r) % 2]
    assert len(odds) == p + 2 and len(evens) == (variant != 'e0')
    equal_edges = [j for j in range(len(odds))
                   if runs[odds[j]][0][1] == runs[odds[(j + 1) % len(odds)]][0][1]]
    assert len(equal_edges) == (variant == 'e1_equal')
    start = odds[(equal_edges[0] + 1) % len(odds)] if equal_edges else odds[0]
    runs = runs[start:] + runs[:start]
    odd_runs = [r for r in runs if len(r) % 2]
    odd_labels = [r[0][1] for r in odd_runs]
    assert all(odd_labels[i] != odd_labels[i + 1] for i in range(len(odd_labels) - 1))
    quad = find_quadruple(odd_labels, p)
    assert quad is not None
    chosen = set()
    for r in runs:
        paired = r[:-1] if len(r) % 2 else r
        assert len(paired) % 2 == 0
        for i in range(0, len(paired), 2):
            assert paired[i][1] == paired[i + 1][1]
            chosen.update((paired[i][0], paired[i + 1][0]))
    for i in quad:
        chosen.add(odd_runs[i][-1][0])
    cyclic_selector = [index for r in runs for index, _ in r if index in chosen]
    selector = sorted(chosen)
    assert len(selector) == 2 * p
    check_selector(word, selector, p)
    assert perm_product(word, cyclic_selector, p) == tuple(range(p))
    cut = next(k for k in range(len(selector))
               if cyclic_selector[k:] + cyclic_selector[:k] == selector)
    # Removing one selected factor is an independently checked negative control.
    try:
        check_selector(word, selector[:-1], p)
        raise AssertionError('wrong-count mutation was accepted')
    except ValueError as exc:
        assert str(exc) == 'selector count/order/distinctness'
    one_ref = next(i for i, entry in enumerate(word) if entry[0] == 'r')
    mutation = sorted([one_ref] + selector[1:])
    try:
        check_selector(word, mutation, p)
        raise AssertionError('rotation mutation was accepted')
    except ValueError as exc:
        assert str(exc) == 'selector contains nonreflection'
    graph = []
    for j, (index, value) in enumerate(refs):
        next_index, next_value = refs[(j + 1) % len(refs)]
        if j + 1 < len(refs):
            gap = word[index + 1:next_index]
        else:
            gap = word[index + 1:] + word[:next_index]
        graph.append(int(value != next_value or any(t == 'r' for t, _ in gap)))
    return {'p': p, 'variant': variant,
            'word': [f'{typ}{value}' for typ, value in word],
            'reflection_count': len(refs), 'rotation_count': len(word) - len(refs),
            'odd_run_labels_after_cut': odd_labels,
            'odd_run_quadruple_positions_zero_based': list(quad),
            'equal_cyclic_odd_edges': len(equal_edges), 'even_runs': len(evens),
            'selected_full_word_indices_zero_based': selector,
            'selected_labels_in_original_order': [word[i][1] for i in selector],
            'selected_indices_in_cut_cyclic_order': cyclic_selector,
            'cyclic_to_original_rotation': cut,
            'permutation_product': list(perm_product(word, selector, p)),
            'raw_matching': cycle_matching(tuple(graph)),
            'raw_absent_edges': len(graph) - sum(graph),
            'negative_controls': ['selector count/order/distinctness', 'selector contains nonreflection']}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    output = Path(args.output)
    if output.exists():
        raise FileExistsError(output)
    result = {
        'scope': 'Finite controls only; not an all-prime proof, historical-floor authentication, or novelty result.',
        'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'adjacent_distinct_words': {str(p): audit_all_words(p) for p in (3, 5)},
        'local_patterns': audit_local_patterns(),
        'raw_graph_masks': audit_raw_graphs(),
        'actual_examples': [audit_example(p, v) for p in (3, 5, 7, 11)
                            for v in ('e0', 'e1_equal', 'e1_unequal')],
    }
    assert any(c['cyclic_to_original_rotation'] for c in result['actual_examples'])
    with output.open('x', encoding='utf-8') as out:
        json.dump(result, out, indent=2, sort_keys=True)
        out.write('\n')
    print(json.dumps({'program_sha256': result['program_sha256'],
                      'word_totals': {p: v['words'] for p, v in result['adjacent_distinct_words'].items()},
                      'graph_totals': result['raw_graph_masks'],
                      'actual_example_count': len(result['actual_examples']),
                      'nontrivial_rotations': sum(bool(c['cyclic_to_original_rotation']) for c in result['actual_examples'])},
                     sort_keys=True))


if __name__ == '__main__':
    main()
